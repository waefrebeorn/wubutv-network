#!/usr/bin/env python3
"""release-inventory-scan: rebuild release/inventory.json with CONTENT IDENTITY
per item (design S6/S7): md5, duration, frame count, perceptual hash (dHash of
frames sampled at 10/50/90%), audio fingerprint (md5 + RMS of first 60s decoded
audio). Incremental: an item whose file size+mtime match the previous inventory
keeps its recorded identity. Atomic write (temp + verify + rename)."""
import hashlib, json, os, subprocess, sys, tempfile
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from catalogue import catalogue, NET
from blam_records import blam_class_for

REL = os.path.join(NET, "release")
DEST = os.path.join(REL, "inventory.json")

def md5_of(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

def probe(path):
    r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0",
                        "-show_entries", "stream=nb_frames,avg_frame_rate,duration",
                        "-show_entries", "format=duration", "-of", "json", path],
                       capture_output=True, text=True, timeout=120)
    d = json.loads(r.stdout)
    st = (d.get("streams") or [{}])[0]
    dur = float(st.get("duration") or d.get("format", {}).get("duration") or 0)
    frames = st.get("nb_frames")
    if frames in (None, "N/A"):
        num, den = (st.get("avg_frame_rate") or "24/1").split("/")
        fps = float(num) / float(den or 1)
        frames = int(round(dur * fps)) if dur else None
    else:
        frames = int(frames)
    return dur, frames

def dhash(path, t):
    r = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t:.2f}", "-i", path,
                        "-frames:v", "1", "-vf", "scale=17:16,format=gray",
                        "-f", "rawvideo", "-"], capture_output=True, timeout=120)
    px = r.stdout
    if len(px) < 17 * 16:
        return None
    bits = 0
    for row in range(16):
        for col in range(16):
            left = px[row * 17 + col]
            bits = (bits << 1) | (1 if left > px[row * 17 + col + 1] else 0)
    return f"{bits:064x}"

def audio_fp(path):
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-t", "60",
                        "-ac", "1", "-ar", "8000", "-f", "s16le", "-"],
                       capture_output=True, timeout=180)
    raw = r.stdout
    if not raw:
        return None
    import struct
    n = len(raw) // 2
    samples = struct.unpack(f"<{n}h", raw[: n * 2])
    rms = (sum(s * s for s in samples) / max(n, 1)) ** 0.5
    import math
    return {"md5_60s": hashlib.md5(raw).hexdigest(),
            "rms_db": round(20 * math.log10(rms / 32768.0), 2) if rms > 0 else -99.0,
            "seconds": round(n / 8000.0, 2)}

IG_UPLOAD_LIMIT = 100_000_000  # Instagram rejects media above this size

def postable_path(path):
    """Instagram's 100 MB upload limit (hit by MV-14, 2026-11-16): when the
    catalogue file exceeds it and a house delivery encode (<base>_50mb.mp4,
    same cut, audio copied) sits beside it at <=100 MB, the inventory points
    at the encode — that is the file the lanes can actually post. The house
    master stays on disk untouched; house_path records the provenance."""
    try:
        if os.path.getsize(path) <= IG_UPLOAD_LIMIT:
            return path, None
    except OSError:
        return path, None
    sib = path[:-4] + "_50mb.mp4" if path.endswith(".mp4") else None
    if sib and os.path.exists(sib) and os.path.getsize(sib) <= IG_UPLOAD_LIMIT:
        return sib, path
    return path, None

def identity(item, prev):
    # BLAM gate verdict from the item's on-disk gate record (None when no
    # record exists — an honest null). Stamped fresh every scan so the
    # metrics harvest, which copies features from the inventory entry,
    # finally has a blam_class to copy (it was null in 74/74 rows).
    item = {**item, "blam_class": blam_class_for(item)}
    path = item["path"]
    if not path or not os.path.exists(path):
        return {**item, "path": path, "exists": False}
    path, house_path = postable_path(path)
    if house_path:
        item = {**item, "house_path": house_path, "delivery_encode": True}
    st = os.stat(path)
    key = (st.st_size, int(st.st_mtime))
    old = prev.get(item["id"])
    if old and old.get("exists") and (old.get("size"), old.get("mtime")) == key \
            and old.get("md5"):
        return {**item, **{k: old[k] for k in
                ("exists", "size", "mtime", "md5", "duration_s", "frames",
                 "phash", "audio_fp") if k in old}, "path": path}
    dur, frames = probe(path)
    ph = [dhash(path, dur * f) for f in (0.10, 0.50, 0.90)] if dur else []
    return {**item, "path": path, "exists": True, "size": st.st_size,
            "mtime": int(st.st_mtime), "md5": md5_of(path),
            "duration_s": round(dur, 2), "frames": frames,
            "phash": ph, "audio_fp": audio_fp(path)}

def main():
    prev = {}
    if os.path.exists(DEST):
        with open(DEST) as f:
            prev = {i["id"]: i for i in json.load(f).get("items", [])}
    items = list(catalogue())
    with ThreadPoolExecutor(max_workers=4) as ex:
        done = list(ex.map(lambda it: identity(it, prev), items))
    missing = [i["id"] for i in done if not i.get("exists")]
    out = {"version": 1,
           "scanned_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
           "items": done}
    fd, tmp = tempfile.mkstemp(dir=REL, suffix=".tmp")
    with os.fdopen(fd, "w") as f:
        json.dump(out, f, indent=1)
    with open(tmp) as f:
        json.load(f)
    os.rename(tmp, DEST)
    print(f"inventory: {len(done)} items, {len(done) - len(missing)} on disk, missing: {missing}")

if __name__ == "__main__":
    sys.exit(main())
