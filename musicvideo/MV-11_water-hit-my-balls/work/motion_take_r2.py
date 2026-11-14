#!/usr/bin/env python3
"""MV-11 REBUILD2 per-take motion audit — native-fps frame diff at 160x90 gray.
Usage: python3 work/motion_take_r2.py <take_path>
Reports: mean diff, longest near-still run (diff<0.5) in frames + its time,
count of runs >=12f. FAIL = any run >=12f, or mean diff <0.5.
"""
import subprocess, sys
import numpy as np

path = sys.argv[1]
W, H, FPS = 160, 90, 24
proc = subprocess.Popen(
    ["ffmpeg", "-v", "error", "-i", path, "-vf",
     f"scale={W}:{H},format=gray", "-f", "rawvideo", "-"],
    stdout=subprocess.PIPE)
fs = W * H
diffs, prev = [], None
while True:
    raw = proc.stdout.read(fs)
    if len(raw) < fs:
        break
    cur = np.frombuffer(raw, dtype=np.uint8).astype(np.float32)
    if prev is not None:
        diffs.append(float(np.mean(np.abs(cur - prev))))
    prev = cur
proc.wait()
diffs = np.array(diffs)
mean = float(diffs.mean()) if len(diffs) else 0.0
# longest near-still run (diff < 0.5)
best, cur_run, best_start, run_start = 0, 0, 0, 0
for i, d in enumerate(diffs):
    if d < 0.5:
        if cur_run == 0:
            run_start = i
        cur_run += 1
        if cur_run > best:
            best, best_start = cur_run, run_start
    else:
        cur_run = 0
runs12 = 0
cur_run = 0
for d in diffs:
    if d < 0.5:
        cur_run += 1
        if cur_run == 12:
            runs12 += 1
    else:
        cur_run = 0
print(f"MOTION frames={len(diffs)} mean_diff={mean:.2f} "
      f"longest_near_still={best}f@{best_start/FPS:.2f}s runs>=12f={runs12}")
print("MOTION_VERDICT:", "FAIL" if (best >= 12 or mean < 0.5) else "PASS")
