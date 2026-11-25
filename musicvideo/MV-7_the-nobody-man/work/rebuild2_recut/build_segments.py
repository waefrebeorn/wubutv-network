#!/usr/bin/env python3
"""MV-7 REBUILD-2 re-cut — per-line segment builder.
Warp: PCHIP swing keyframes, take mouth-event anchors -> song word onsets,
merged sub-0.1s song anchors, natural-speed boundary extrapolation.
STRUCT/MONTAGE: beat-cut chunks from the line's own take.
Emits work/rebuild2_recut/seg/<ref>.mp4 (1280x720, 24fps, no audio) +
seg_manifest.json with per-segment speeds + anchor tables."""
import json, subprocess, os, sys
import numpy as np
from scipy.interpolate import PchipInterpolator

BASE = "/home/hatch/workspace/wubutv-network/musicvideo/MV-7_the-nobody-man"
OUT = f"{BASE}/work/rebuild2_recut"
SEG = f"{OUT}/seg"
os.makedirs(SEG, exist_ok=True)
W, H, FPS = 1248, 704, 24
TOTAL_FRAMES = 4493
BEAT = 60.0 / 103.36

# FINAL VISUAL LAG TABLE — every value read by eye from full-res dense
# strips (event frame / 24) or fixstrips; supersedes all detector values.
# (Seconds added to the take word-1 audio onset.)
LAG_OVERRIDE = {
    "I1a": 0.583, "I1b": 0.0, "I1c": 0.083, "I1d": 0.0,
    "I2a": 0.417, "I2b": 0.0, "I2c": 0.583,
    "V1.1": 0.750, "V1.4": 0.250, "V1.5": 0.250, "V1.6": 0.0,
    "PC1.1": 0.667, "PC1.2": 0.083, "PC1.3": 0.417, "PC1.4": 0.250,
    "C1.1": 0.167, "C1.2": 0.0, "C1.3": 0.083, "C1.4": 0.167, "C1.5": 0.333,
    "C1.6": 0.250, "C1.7": 0.167, "C1.8": 0.417,
    "C1.Tc": 0.333, "C1.Td": 0.0,
    "C2.1": 0.333, "C2.2": 0.0, "C2.3": 0.333, "C2.4": 0.167, "C2.5": 0.083,
    "C2.6": 0.0, "C2.7": 0.333, "C2.8": 0.0,
    "V2.1": 0.167, "V2.2": 0.333, "V2.3": 0.0, "V2.4": 0.0, "V2.5": 0.333,
    "V2.6": 0.0,
    "PC2.1": 0.417, "PC2.3": 0.417, "PC2.4": 0.250, "B.6": 0.583,
    "FC.3": 0.500, "FC.4": 0.0, "FC.5": 0.0, "FC.6": 0.0, "FC.7": 0.583,
    "FC.8": 0.750, "FC.9": 0.417, "FC.10": 0.167,
    "FC.Ta": 0.500, "FC.Tb": 0.0, "FC.Tc": 0.500, "FC.Td": 0.0,
}
# Per-word lag overrides (index -> lag). C1.Ta: "man" closes for /m/ at its
# audio onset and opens +6f later; anchor the opening (run-5 fallback).
# Gate v1 corrections (eye-read from candidate frames + take strips):
# C1.Ta word-1 parting is at take f14-15, not f12 -> lag 0.625 puts the
# parting on the onset, clear open at +1. FC.6 "Flicking" opens at take
# f27 (1.125s) after the /f/ closure at the 0.95 RMS onset -> anchor the
# opening with lag 0.167 on word 0 only.
WORD_LAG_OVERRIDE = {"C1.Ta": {0: 0.625, 1: 0.250}, "FC.6": {0: 0.167}}
SUNG_END_OVERRIDE = {"I2c": 18.74}   # U04 sung_end per unit table
MONTAGE_SRC0 = {"C1.Tb": 48}         # skip R16B head-bow frames 0-36

def decode(path):
    p = subprocess.run(["ffmpeg", "-v", "error", "-i", path,
                        "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], capture_output=True)
    a = np.frombuffer(p.stdout, dtype=np.uint8)
    n = len(a) // (W * H * 3)
    return a[:n * W * H * 3].reshape(n, H, W, 3)

def write_seg(ref, out_frames):
    raw = f"/tmp/seg_{ref}.raw"
    np.stack(out_frames).tofile(raw)
    dst = f"{SEG}/{ref}.mp4"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
                    "-s", f"{W}x{H}", "-r", str(FPS), "-i", raw,
                    "-vf", "scale=1280:720:flags=lanczos", "-c:v", "libx264",
                    "-preset", "medium", "-crf", "14", "-pix_fmt", "yuv420p", dst], check=True)
    os.remove(raw)

def song_line_words(a, b):
    sw = json.load(open(f"{BASE}/SONG_WORDS.json"))["words"]
    return [w for w in sw if a - 0.01 <= w["start"] < b]

SONG_ALL = json.load(open(f"{BASE}/SONG_WORDS.json"))["words"]

def build_warp(rec, lag, f0, f1, frames, word_lag_map=None):
    """Returns (out_frames, info). rec: anchors.json line record."""
    sl = rec["slice"]
    a, b = rec["a"], rec["b"]
    if rec["chant"]:
        # song anchors: rep onset + internal splits proportional to take slice
        t0, t1 = sl[0]["s"], sl[-1]["e"]
        span_song = (SUNG_END_OVERRIDE.get(rec["ref"]) or b) - a
        span_take = t1 - t0
        song_on = [a + (w["s"] - t0) * (span_song / span_take) for w in sl]
        song_end = a + span_song
    else:
        sw = [w for w in SONG_ALL if a - 0.01 <= w["start"] < b]
        song_on = [w["start"] for w in sw]
        song_end = sw[-1]["end"]
    # pair anchors: if counts differ, pair by proportion (first/last + index scale)
    nt, ns = len(sl), len(song_on)
    pairs = []
    if nt == ns:
        pairs = list(zip([w["s"] for w in sl], song_on))
    else:
        # use first + last + proportional mids from the longer side
        idx = [round(i * (nt - 1) / max(1, ns - 1)) if ns > 1 else 0 for i in range(ns)]
        pairs = [(sl[idx[i]]["s"], song_on[i]) for i in range(ns)]
    kt, ks = [], []
    for j, (tt, ss) in enumerate(pairs):
        wlag = lag
        if word_lag_map and j in word_lag_map:
            wlag = word_lag_map[j]
        kt.append(tt + wlag); ks.append(ss)
    # merge sub-0.1s song anchors (keep first of cluster)
    mkt, mks = [kt[0]], [ks[0]]
    for x, y in zip(kt[1:], ks[1:]):
        if y - mks[-1] < 0.1 or x - mkt[-1] < 0.04:
            continue
        mkt.append(x); mks.append(y)
    last_lag = lag
    if word_lag_map and (len(sl) - 1) in word_lag_map:
        last_lag = word_lag_map[len(sl) - 1]
    last_take_end = sl[-1]["e"] + last_lag
    # boundary anchors at natural speed
    kt2 = [mkt[0] - (ks[0] - a)] + mkt + [last_take_end + (b - song_end)]
    ks2 = [a] + mks + [b]
    # enforce strict increase on kt2
    ok_t, ok_s = [kt2[0]], [ks2[0]]
    for x, y in zip(kt2[1:], ks2[1:]):
        if x - ok_t[-1] >= 0.02 and y - ok_s[-1] >= 0.02:
            ok_t.append(x); ok_s.append(y)
    fwd = PchipInterpolator(ok_t, ok_s)
    dense_t = np.linspace(ok_t[0], ok_t[-1], 20001)
    dense_s = fwd(dense_t)
    deriv = fwd.derivative()
    tsamp = np.linspace(ok_t[0] + 0.02, ok_t[-1] - 0.02, 60)
    speeds = [float(1.0 / deriv(t)) for t in tsamp if deriv(t) != 0]
    n = len(frames)
    out = []
    for f in range(f0, f1):
        t_out = f / FPS
        t_take = float(np.interp(t_out, dense_s, dense_t))
        src = min(n - 1, max(0, int(round(t_take * FPS))))
        out.append(frames[src])
    return out, {"anchors_take": [round(x, 3) for x in ok_t],
                 "anchors_song": [round(x, 3) for x in ok_s],
                 "speed_min": round(min(speeds), 3) if speeds else None,
                 "speed_max": round(max(speeds), 3) if speeds else None,
                 "speed_mean": round(float(np.mean(speeds)), 3) if speeds else None}

def build_montage(rec, f0, f1, frames):
    """Beat-cut chunks from the line's own take, natural speed per chunk."""
    n = len(frames)
    a = rec["a"]
    src0 = MONTAGE_SRC0.get(rec["ref"], 0)
    out = []
    f = f0
    chunk_idx = 0
    total = f1 - f0
    while f < f1:
        # frames until next beat boundary (beats from segment start)
        t_rel = (f - f0) / FPS
        next_beat = (int(t_rel / BEAT) + 1) * BEAT
        L = min(f1 - f, max(1, int(round(next_beat * FPS)) - (f - f0)))
        start = (src0 + chunk_idx * 37) % max(1, n - L)
        for k in range(L):
            out.append(frames[min(n - 1, start + k)])
        f += L
        chunk_idx += 1
    return out, {"chunks": chunk_idx}

def main():
    anchors = json.load(open(f"{OUT}/anchors.json"))["lines"]
    fixed = {}
    if os.path.exists(f"{OUT}/lags_fixed.json"):
        fixed = json.load(open(f"{OUT}/lags_fixed.json"))
    only = sys.argv[1:] or None
    # frame tiling
    lines = sorted(anchors, key=lambda r: r["a"])
    starts = [int(round(r["a"] * FPS)) for r in lines]
    manifest = []
    from collections import defaultdict
    by_take = defaultdict(list)
    for i, rec in enumerate(lines):
        f0 = starts[i]
        f1 = starts[i + 1] if i + 1 < len(lines) else int(round(183.24 * FPS))
        by_take[rec["take"]].append((rec, f0, f1))
    # outro segment spec appended under U40's take
    outro = {"ref": "OUT", "a": 183.24, "b": TOTAL_FRAMES / FPS, "kind": "OUTRO",
             "key": "U40", "chant": False, "take": lines[-1]["take"] if lines[-1]["ref"] == "FC.Td" else None}
    for path, items in by_take.items():
        if only and not any(r["ref"] in only for r, _, _ in items):
            continue
        frames = decode(path)
        for rec, f0, f1 in items:
            if only and rec["ref"] not in only:
                continue
            ref = rec["ref"]
            if rec["kind"] in ("STRUCT", "MONTAGE"):
                out, info = build_montage(rec, f0, f1, frames)
                kind_used = "MONTAGE"
            else:
                lag = rec.get("head_lag")
                if ref in fixed and fixed[ref].get("lag") is not None:
                    lag = fixed[ref]["lag"]
                if ref in LAG_OVERRIDE:
                    lag = LAG_OVERRIDE[ref]
                if lag is None:
                    lag = 0.0
                wlm = WORD_LAG_OVERRIDE.get(ref)
                if wlm is not None and 0 in wlm:
                    lag = wlm[0]
                out, info = build_warp(rec, lag, f0, f1, frames, wlm)
                kind_used = rec["kind"]
                if ref == "FC.4":
                    # bad-word rule: final "man" is truncated in U33 ->
                    # beat-cut montage from the song "man" onset to seg end
                    man_on = [w["start"] for w in SONG_ALL
                              if rec["a"] - 0.01 <= w["start"] < rec["b"]
                              and w["word"].lower().strip(",.?!") == "man"]
                    if man_on:
                        f_bad = int(round(man_on[-1] * FPS))
                        n = len(frames)
                        chunk = 0
                        f = max(f_bad, f0)
                        while f < f1:
                            t_rel = (f - f0) / FPS
                            nb = (int(t_rel / BEAT) + 1) * BEAT
                            L = min(f1 - f, max(1, int(round(nb * FPS)) - (f - f0)))
                            start = (chunk * 37) % max(1, n - L)
                            for k in range(L):
                                out[f - f0 + k] = frames[min(n - 1, start + k)]
                            f += L
                            chunk += 1
                        info["badword_montage_from"] = man_on[-1]
                if ref == "B.6":
                    # gate v1 fix: warp b=141.44 but the segment window runs
                    # to FC.1 (143.40); the interp clamped to the take's last
                    # frame -> 46f freeze. Cover the unanchored tail (ASR
                    # pickup "to the one bright light"; sheet shows a gap)
                    # with beat-cut montage from U31's own take, FC.4-style.
                    f_bad = int(round(141.62 * FPS))
                    n = len(frames)
                    chunk = 0
                    f = max(f_bad, f0)
                    while f < f1:
                        t_rel = (f - f0) / FPS
                        nb = (int(t_rel / BEAT) + 1) * BEAT
                        L = min(f1 - f, max(1, int(round(nb * FPS)) - (f - f0)))
                        start = (chunk * 37) % max(1, n - L)
                        for k in range(L):
                            out[f - f0 + k] = frames[min(n - 1, start + k)]
                        f += L
                        chunk += 1
                    info["tail_montage_from"] = 141.62
            write_seg(ref, out)
            info.update({"ref": ref, "kind": kind_used, "frames": f1 - f0, "f0": f0, "f1": f1})
            manifest.append(info)
            print(ref, kind_used, "frames", f1 - f0, info.get("speed_min"), info.get("speed_max"))
        del frames
    # outro: natural continuation from U40 take
    if not only or "OUT" in only:
        u40 = [r for r in lines if r["ref"] == "FC.Td"][0]
        frames = decode(u40["take"])
        f0 = int(round(183.24 * FPS))
        start_take = u40["slice"][-1]["e"]  # 4.28
        out = []
        for f in range(f0, TOTAL_FRAMES):
            tt = start_take + (f - f0) / FPS
            out.append(frames[min(len(frames) - 1, int(round(tt * FPS)))])
        write_seg("OUT", out)
        manifest.append({"ref": "OUT", "kind": "OUTRO", "frames": TOTAL_FRAMES - f0, "f0": f0, "f1": TOTAL_FRAMES})
        print("OUT frames", TOTAL_FRAMES - f0)
    json.dump(manifest, open(f"{OUT}/seg_manifest.json", "w"), indent=1)

if __name__ == "__main__":
    main()
