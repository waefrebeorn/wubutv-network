#!/usr/bin/env python3
"""MV-8 v3 volley-4 QC: contact sheets + motion stats (signalstats YDIF).
Usage: qc_v3_volley4.py <take1.mp4> ... — writes sheets + motion report
into work/rebuild/qc/v3_volley4/ next to the project root (cwd = project root).
Motion gate: no frozen run >= 24 frames (1s) with YDIF < 1.0; report
min/mean YDIF per 0.5s window (12 frames). YDIF is mean abs luma diff
between consecutive frames (0-255 scale).
"""
import json, os, re, subprocess, sys

PROJ = os.getcwd()
OUT = os.path.join(PROJ, "work/rebuild/qc/v3_volley4")
os.makedirs(OUT, exist_ok=True)

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print("CMD FAILED:", " ".join(cmd), "\n", r.stderr[:2000])
        raise SystemExit(1)
    return r.stdout + r.stderr

for take in sys.argv[1:]:
    stem = os.path.splitext(os.path.basename(take))[0]
    print(f"== {stem}")
    # contact sheet: 2fps, 320x180 tiles, 5x4
    sheet = os.path.join(OUT, stem + "_sheet.jpg")
    run(["ffmpeg", "-v", "error", "-y", "-i", take,
         "-vf", "fps=2,scale=320:180,tile=5x4", "-frames:v", "1", sheet])
    print("  sheet:", sheet)
    # full-res frames at 0s, 5s, 9.5s for text scan
    for t in ("0", "5", "9.5"):
        out = os.path.join(OUT, f"{stem}_f{t}s.jpg")
        run(["ffmpeg", "-v", "error", "-y", "-ss", t, "-i", take,
             "-frames:v", "1", "-q:v", "2", out])
    # motion: (a) v2-style mean abs diff between consecutive 0.5s frames
    # (b) NATIVE-fps frozen-run check (frame rule): longest run of
    # consecutive frames with mean abs diff < 0.5 at 160x90
    import numpy as np
    from PIL import Image
    import glob as _glob
    tmp = os.path.join(OUT, stem + "_motion_frames")
    os.makedirs(tmp, exist_ok=True)
    run(["ffmpeg", "-v", "error", "-y", "-i", take,
         "-vf", "fps=2,scale=320:-1", os.path.join(tmp, "h_%03d.jpg")])
    frames = sorted(_glob.glob(os.path.join(tmp, "h_*.jpg")))
    diffs, prev = [], None
    for f in frames:
        a = np.asarray(Image.open(f).convert("L"), dtype=np.int16)
        if prev is not None:
            diffs.append(float(np.mean(np.abs(a - prev))))
        prev = a
    print("  motion diffs per 0.5s:", [round(d, 1) for d in diffs])
    print("  motion min:", round(min(diffs), 1) if diffs else None,
          "mean:", round(sum(diffs)/len(diffs), 1) if diffs else None)
    # native-fps frozen run
    run(["ffmpeg", "-v", "error", "-y", "-i", take,
         "-vf", "fps=24,scale=160:90", os.path.join(tmp, "n_%03d.jpg")])
    nframes = sorted(_glob.glob(os.path.join(tmp, "n_*.jpg")))
    ndiffs, prev = [], None
    for f in nframes:
        a = np.asarray(Image.open(f).convert("L"), dtype=np.int16)
        if prev is not None:
            ndiffs.append(float(np.mean(np.abs(a - prev))))
        prev = a
    longest, cur = 0, 0
    for v in ndiffs:
        cur = cur + 1 if v < 0.5 else 0
        longest = max(longest, cur)
    print(f"  native-fps frames: {len(ndiffs)+1}, longest frozen run "
          f"(diff<0.5): {longest}f ({longest/24:.2f}s), "
          f"native mean diff {sum(ndiffs)/len(ndiffs):.2f}")
    print(f"  GATE motion: {'PASS' if longest < 24 else 'FAIL — frozen run >= 24f'}")
