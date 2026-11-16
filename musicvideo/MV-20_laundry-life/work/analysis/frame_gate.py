#!/usr/bin/env python3
"""Frame gate: worst near-dup run + mean |diff| inside the vocal span.
Usage: frame_gate.py take.mp4 vstart vend  (times within the take)
Writes nothing; prints one line. FAIL: run>=24 during words or meandiff<0.5."""
import subprocess, sys, json
import numpy as np
f, vs, ve = sys.argv[1], float(sys.argv[2]), float(sys.argv[3])
W, H, FPS = 96, 54, 24
r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                    "-of", "json", f], capture_output=True, text=True)
dur = float(json.loads(r.stdout)["format"]["duration"])
raw = subprocess.run(["ffmpeg", "-v", "error", "-i", f, "-vf", f"fps={FPS},scale={W}:{H},format=gray",
                      "-f", "rawvideo", "-"], capture_output=True).stdout
n = len(raw) // (W * H)
fr = np.frombuffer(raw[:n * W * H], dtype=np.uint8).reshape(n, H, W).astype(np.int16)
d = np.abs(np.diff(fr, axis=0)).mean(axis=(1, 2))
i0, i1 = int(vs * FPS), min(int(ve * FPS), len(d))
seg = d[i0:i1]
near = seg < 1.0
worst = run = 0
for x in near:
    run = run + 1 if x else 0
    worst = max(worst, run)
print(f"frames={n} dur={dur:.2f} vocal_mean_diff={seg.mean():.2f} worst_neardup_run={worst}f ({worst/FPS:.2f}s) "
      f"{'FAIL' if worst >= 24 or seg.mean() < 0.5 else 'PASS'}")
