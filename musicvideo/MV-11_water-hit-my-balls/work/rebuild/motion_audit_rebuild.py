#!/usr/bin/env python3
"""MV-11 full-master motion audit — native-fps frame diff at 320x180 gray.

Reads the master via ffmpeg rawvideo pipe, computes mean abs-diff between
consecutive frames, and reports:
  - overall mean diff
  - near-still runs (mean diff < 0.5) of >=12 frames, with song times
  - FAIL if any near-still run >=24f (1s) during words, per the v6 frame
    rule — except the disclosed held passages, which the eye decides.
Usage: python3 work/motion_audit.py [master_path]
"""
import subprocess
import sys

import numpy as np

BASE = "/home/hatch/workspace/wubutv-network/musicvideo/MV-11_water-hit-my-balls"
MASTER = sys.argv[1] if len(sys.argv) > 1 else f"{BASE}/masters/mv11_water_hit_my_balls_rebuild_16x9.mp4"
W, H, FPS = 320, 180, 24

# song word spans (for the "during words" flag): from LYRIC_TIMELINE anchors
WORD_SPANS = [
    (13.76, 38.94), (45.18, 50.14), (55.26, 57.56), (70.66, 101.78),
    (110.68, 111.72), (122.38, 155.06), (170.92, 172.32),
]


def in_words(t):
    return any(a - 0.1 <= t <= b + 0.1 for a, b in WORD_SPANS)


proc = subprocess.Popen(
    ["ffmpeg", "-v", "error", "-i", MASTER, "-vf",
     f"scale={W}:{H},format=gray", "-f", "rawvideo", "-"],
    stdout=subprocess.PIPE)
frame_size = W * H
diffs = []
prev = None
while True:
    raw = proc.stdout.read(frame_size)
    if len(raw) < frame_size:
        break
    cur = np.frombuffer(raw, dtype=np.uint8).astype(np.float32)
    if prev is not None:
        diffs.append(float(np.abs(cur - prev).mean()))
    prev = cur
proc.wait()
diffs = np.array(diffs)
print(f"frames: {len(diffs) + 1}, diff samples: {len(diffs)}")
print(f"overall mean diff: {diffs.mean():.2f}, min {diffs.min():.2f}, max {diffs.max():.2f}")

# near-still runs: diff < 0.5
runs = []
cur = None
for i, d in enumerate(diffs):
    if d < 0.5:
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
runs = [(a, b) for a, b in runs if b - a + 1 >= 12]
print(f"near-still runs >=12f (diff<0.5): {len(runs)}")
worst = []
for a, b in runs:
    n = b - a + 1
    t0 = (a + 1) / FPS  # diff index a = between frames a and a+1
    print(f"  {n:3d}f @ {t0:7.2f}s ({t0:.2f}-{(b + 1) / FPS:.2f}s) during-words={in_words(t0)}")
    if n >= 24:
        worst.append((n, t0))
print("FAIL-RANGE runs >=24f:", worst if worst else "none")
print("MOTION AUDIT DONE")
