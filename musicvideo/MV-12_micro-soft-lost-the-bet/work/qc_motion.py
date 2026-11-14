#!/usr/bin/env python3
"""MV-12 motion audit: per-take frame-diff on 160x90 gray frames.
Reports mean diff overall + in the usable span (first 50f ~ 2.08s),
longest near-still run (diff < 1.0) + where, and md5s of sampled frames.
Frame rule (Slopcannon): FAIL if vocal near-dup run >= 24f during vocal
OR vocal mean diff < 0.5. The eye is the decider for held-note passages.
Usage: python3 work/qc_motion.py <take.mp4> [usable_frames]
"""
import subprocess, sys, os
import numpy as np
from PIL import Image
import hashlib

take = sys.argv[1]
usable = int(sys.argv[2]) if len(sys.argv) > 2 else 50
base = os.path.splitext(os.path.basename(take))[0]
tmp = f"/tmp/mv12_qc_{base}"
os.makedirs(tmp, exist_ok=True)
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", take, "-vf",
                "scale=160:90,format=gray", "-vsync", "0",
                f"{tmp}/f_%04d.png"], check=True)
files = sorted(os.listdir(tmp))
frames = []
for fn in files:
    frames.append(np.asarray(Image.open(os.path.join(tmp, fn)), dtype=np.float32))
n = len(frames)
diffs = [float(np.abs(frames[i + 1] - frames[i]).mean()) for i in range(n - 1)]
# near-still runs (diff < 1.0)
runs = []
cur = None
for i, d in enumerate(diffs):
    if d < 1.0:
        if cur is None:
            cur = [i, i]
        else:
            cur[1] = i
    else:
        if cur is not None:
            runs.append(tuple(cur))
            cur = None
if cur is not None:
    runs.append(tuple(cur))
runs = [(a, b, b - a + 1) for a, b in runs]
runs.sort(key=lambda r: -r[2])
print(f"{base}: {n}f, mean diff overall={np.mean(diffs):.2f}, "
      f"usable first {usable}f mean={np.mean(diffs[:usable]):.2f}")
print(f"  longest near-still runs (diff<1.0): {runs[:3]}")
# distinct-frame check: md5 of sampled full frames at 0/12/24/36/48
for idx in [0, 12, 24, 36, 48]:
    if idx < n:
        h = hashlib.md5(frames[idx].tobytes()).hexdigest()[:12]
        print(f"  frame {idx} md5 {h} diff-to-prev "
              f"{diffs[idx-1]:.2f}" if idx > 0 else f"  frame {idx} md5 {h}")
