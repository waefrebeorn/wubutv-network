#!/usr/bin/env python3
"""Frame rule: per-frame mean abs diff at 160x90 gray, near-dup runs in a window."""
import subprocess, sys
import numpy as np

path, w0, w1 = sys.argv[1], float(sys.argv[2]), float(sys.argv[3])
W, H, FPS = 160, 90, 24
cmd = ["ffmpeg", "-v", "error", "-i", path, "-vf", f"fps={FPS},scale={W}:{H},format=gray", "-f", "rawvideo", "-"]
raw = subprocess.run(cmd, capture_output=True).stdout
n = len(raw) // (W * H)
frames = np.frombuffer(raw[:n * W * H], dtype=np.uint8).reshape(n, W * H).astype(np.float32)
diffs = np.abs(np.diff(frames, axis=0)).mean(axis=1)
f0, f1 = int(w0 * FPS), min(int(w1 * FPS), len(diffs))
win = diffs[f0:f1]
run = mx = 0
for d in win:
    run = run + 1 if d < 0.5 else 0
    mx = max(mx, run)
print(f"frames={n} window {w0}-{w1}s: mean_diff={win.mean():.3f} min={win.min():.3f} longest_near_dup_run(<0.5)={mx} frames")
print(f"whole-clip mean_diff={diffs.mean():.3f}")
