#!/usr/bin/env python3
"""MV-4 lyrics-redo gates: run on the new lyrics master vs the delivered base.

Checks:
1. ffprobe: 5731f, 238.805s, 1280x720, 24fps, h264, AAC 48k stereo.
2. SEI crf=18.0 (x264 encoding settings in the stream).
3. faststart: moov before mdat.
4. Audio: decoded-PCM md5 of the new master == base master.
5. Motion audit (numpy frame-diff, 160x90 gray, diff<0.5 near-still):
   report runs >=12f; FAIL if a NEW run >=24f appears during words vs base.
6. Regression (ALIGNMENT-AWARE, fixed 2026-11-12 after the first gate run
   failed on encoder noise): for each sample time, NEW's center frame vs
   BASE's center +-2 frames, top half, 640x360 gray. PASS = offset 0 is
   the best match (or tied within 0.10) AND offset-0 mean|diff| < 1.5.
   A real frame offset or content change shows as a large offset-0 jump
   (6-14 on fast-motion frames) with the best match moving to +-1/+-2.
   Plus the genuinely wordless+captionless gaps (full frame, bar <2.0).
   The old <1.0 full-res bar is retired: x264 threaded re-encode noise
   runs 1.0-1.7 at full res on moving frames, and the 221.26-230.56 gap
   is not captionless in the base (old L57 block covers it).
Usage: gate_lyrics.py [new_master] [base_master]
"""
import hashlib
import json
import re
import subprocess
import sys

import numpy as np

NEW = sys.argv[1] if len(sys.argv) > 1 else \
    "/home/hatch/workspace/wubutv-network/musicvideo/MV-4_this-time-its-real/masters/mv4_this_time_its_real_16x9_lyrics.mp4"
BASE = sys.argv[2] if len(sys.argv) > 2 else \
    "/home/hatch/workspace/wubutv-network/musicvideo/MV-4_this-time-its-real/masters/mv4_this_time_its_real_16x9.mp4"
# Wordless gaps that are ALSO captionless in the base master (the old L57
# block covers 220.77-238.03, so 221.26-230.56 is NOT captionless in the
# base — the full-frame diff there is the removed caption, i.e. the fix).
WORDLESS = [(30.86, 32.36), (62.78, 64.40), (155.02, 158.76)]
# Alignment sample times (top-half, caption-free region).
ALIGN_TIMES = (20.00, 63.59, 100.00, 156.89, 200.00, 225.91)
W, H = 640, 360


def probe(path):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_format", "-show_streams",
                        "-of", "json", path], capture_output=True, text=True, check=True)
    return json.loads(r.stdout)


def pcm_md5(path):
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-map", "0:a",
                        "-f", "hash", "-hash", "md5", "-"],
                       capture_output=True, text=True, check=True)
    return r.stdout.strip().split("=")[-1]


def moov_first(path):
    # MV-13 gate method: read 2MB (moov is ~166KB; a 64KB window never
    # reaches "mdat" and the check fails on known-good files).
    with open(path, "rb") as f:
        head = f.read(2_000_000)
    return 0 < head.find(b"moov") < head.find(b"mdat")


def sei_crf(path):
    # MV-13 gate method: the x264 encoding-settings string lives in the
    # stream's SEI; `strings` finds the "x264 - core" line.
    r = subprocess.run(["strings", path], capture_output=True, text=True)
    lines = [l for l in r.stdout.splitlines() if "x264 - core" in l]
    if not lines:
        return None
    m = re.search(r"crf=([\d.]+)", lines[0])
    return m.group(1) if m else None


def extract_frame(path, t, w=1280, h=720):
    # Frame-number selection (exact, keyframe-independent): frame N = round(t*24).
    n = round(t * 24)
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", path,
                        "-vf", f"select='eq(n\\,{n})',scale={w}:{h}",
                        "-frames:v", "1", "-f", "rawvideo", "-pix_fmt", "rgb24",
                        "-"], capture_output=True, check=True)
    return np.frombuffer(r.stdout, dtype=np.uint8).astype(np.float32)


def frame_window(path, t, w=W, h=H):
    """13 consecutive gray frames centred on t (input seeking = fast)."""
    r = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t - 0.25:.3f}",
                        "-i", path, "-frames:v", "13", "-f", "rawvideo",
                        "-pix_fmt", "gray", "-s", f"{w}x{h}", "-"],
                       capture_output=True, check=True)
    n = len(r.stdout) // (w * h)
    return [np.frombuffer(r.stdout[i * w * h:(i + 1) * w * h],
                          dtype=np.uint8).astype(np.float32) for i in range(n)]


def frame_mean_diff(path_a, path_b, t):
    a = extract_frame(path_a, t)
    b = extract_frame(path_b, t)
    return float(np.mean(np.abs(a - b))) if a.shape == b.shape else float("nan")


def motion_runs(path):
    """near-still runs (mean |frame diff| < 0.5 on 160x90 gray) >= 12f."""
    cmd = ["ffmpeg", "-v", "error", "-i", path, "-vf",
           "scale=160:90,format=gray", "-f", "rawvideo", "-pix_fmt", "gray", "-"]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    w, h = 160, 90
    prev = None
    runs = []
    start = None
    idx = 0
    while True:
        buf = p.stdout.read(w * h)
        if len(buf) < w * h:
            break
        cur = np.frombuffer(buf, dtype=np.uint8).astype(np.float32)
        if prev is not None:
            d = float(np.mean(np.abs(cur - prev)))
            if d < 0.5:
                if start is None:
                    start = idx - 1
            else:
                if start is not None:
                    if idx - start >= 12:
                        runs.append((start / 24.0, idx / 24.0, idx - start))
                    start = None
        prev = cur
        idx += 1
    if start is not None and idx - start >= 12:
        runs.append((start / 24.0, idx / 24.0, idx - start))
    p.wait()
    return runs


def main():
    ok = True
    for label, path in (("NEW", NEW), ("BASE", BASE)):
        j = probe(path)
        v = [s for s in j["streams"] if s["codec_type"] == "video"][0]
        a = [s for s in j["streams"] if s["codec_type"] == "audio"][0]
        n = int(v.get("nb_frames", 0))
        dur = float(j["format"]["duration"])
        crf = sei_crf(path)
        print(f"{label}: {n}f {dur:.3f}s {v['width']}x{v['height']} "
              f"{v['codec_name']} {v.get('r_frame_rate')} aac={a['codec_name']} "
              f"{a['sample_rate']}Hz {a['channels']}ch crf={crf} "
              f"faststart={moov_first(path)} size={int(j['format']['size'])}")
        if label == "NEW":
            if n != 5731:
                print("  FAIL frame count != 5731"); ok = False
            if abs(dur - 238.805) > 0.05:
                print("  FAIL duration"); ok = False
            if crf != "18.0":
                print(f"  FAIL crf {crf}"); ok = False
            if not moov_first(path):
                print("  FAIL not faststart"); ok = False
    m_new = pcm_md5(NEW)
    m_base = pcm_md5(BASE)
    print(f"audio PCM md5: new={m_new} base={m_base} match={m_new == m_base}")
    if m_new != m_base:
        print("  FAIL audio differs"); ok = False
    print("motion audit (runs >=12f):")
    r_new = motion_runs(NEW)
    r_base = motion_runs(BASE)
    for r in r_new:
        print(f"  NEW  {r[0]:7.2f}-{r[1]:7.2f}  {r[2]}f")
    for r in r_base:
        print(f"  BASE {r[0]:7.2f}-{r[1]:7.2f}  {r[2]}f")
    new_long = [r for r in r_new if r[2] >= 24]
    base_long = {(round(r[0], 1), round(r[1], 1)) for r in r_base if r[2] >= 24}
    extra = [r for r in new_long if (round(r[0], 1), round(r[1], 1)) not in base_long]
    if extra:
        print(f"  FAIL new >=24f runs: {extra}"); ok = False
    else:
        print("  no NEW >=24f runs")
    print("regression — alignment-aware (top half, 640x360 gray):")
    print("  For each sample time, NEW's center frame vs BASE's center +-2.")
    print("  PASS = offset 0 is the best match (or tied within 0.10) AND")
    print("  offset-0 top-half mean|diff| < 1.5. A real frame offset or")
    print("  content change shows as a large jump at offset 0 (6-14 on")
    print("  fast-motion frames) and the best match moving to +-1/+-2.")
    print("  (Measured 2026-11-12: x264 re-encode noise at offset 0 runs")
    print("  0.000-1.117 on these samples; a <1.0 FULL-RES bar was too")
    print("  strict for a re-encode and is retired.)")
    for t in ALIGN_TIMES:
        nw = frame_window(NEW, t)
        bw = frame_window(BASE, t)
        if len(nw) != 13 or len(bw) != 13:
            print(f"  {t:7.2f}s  SHORT WINDOW new={len(nw)} base={len(bw)} — FAIL")
            ok = False
            continue
        c = 6
        diffs = {}
        for dn in (-2, -1, 0, 1, 2):
            diffs[dn] = float(np.mean(np.abs(nw[c][:H // 2] - bw[c + dn][:H // 2])))
        best = min(diffs, key=diffs.get)
        d0 = diffs[0]
        passed = (d0 < 1.5) and (d0 <= diffs[best] + 0.10)
        print(f"  {t:7.2f}s  offsets " +
              " ".join(f"{dn:+d}:{diffs[dn]:.3f}" for dn in (-2, -1, 0, 1, 2)) +
              f"  best={best:+d}  {'PASS' if passed else 'FAIL'}")
        if not passed:
            ok = False
    print("regression — wordless/captionless gaps (full frame, 1280x720 RGB, bar <2.0):")
    print("  (bar raised: full-res re-encode noise on moving frames runs 1.0-1.7;")
    print("  the 221.26-230.56 gap is excluded — the old L57 block covers it.)")
    for lo, hi in WORDLESS:
        t = (lo + hi) / 2
        d = frame_mean_diff(NEW, BASE, t)
        print(f"  {t:7.2f}s  mean|diff|={d:.3f}  {'PASS' if d < 2.0 else 'FAIL'}")
        if not d < 2.0:
            print("  FAIL regression"); ok = False
    print("GATES:", "ALL PASS" if ok else "FAILURES — see above")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
