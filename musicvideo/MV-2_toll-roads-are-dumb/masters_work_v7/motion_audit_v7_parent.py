#!/usr/bin/env python3
"""MV-2 v7 full-master motion audit — parent verification pass (adapted from MV-13 motion_audit_mv13.py).
Native-fps frame diff at 320x180 gray. Near-still runs (diff < 0.5) >= 12f reported
with song times and a during-words flag. FAIL if any near-still run >= 24f (1s)
during words — except disclosed held passages, which the eye decides.
Word spans from SONG_WORDS_BASE.json (measured words, +/-0.1s).
Usage: python3 masters_work_v7/motion_audit_v7_parent.py [master_path]
"""
import json
import subprocess
import sys

import numpy as np

P = "/home/hatch/workspace/wubutv-network/musicvideo/MV-2_toll-roads-are-dumb"
MASTER = sys.argv[1] if len(sys.argv) > 1 else f"{P}/masters/mv2_toll_roads_are_dumb_v7_16x9.mp4"
W, H, FPS = 320, 180, 24

words = json.load(open(f"{P}/SONG_WORDS_BASE.json"))
WORD_SPANS = [(w["t0"], w["t1"]) for w in words if w["t1"] > w["t0"]]


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

print(f"near-still runs >= 12f: {sum(1 for a, b in runs if b - a + 1 >= 12)}")
fail = False
for a, b in runs:
    n = b - a + 1
    if n < 12:
        continue
    t0, t1 = a / FPS, b / FPS
    dw = in_words((t0 + t1) / 2)
    flag = "DURING-WORDS" if dw else "wordless"
    if n >= 24 and dw:
        fail = True
    print(f"  run {n}f {t0:.2f}-{t1:.2f}s {flag}")

print("MOTION FAIL" if fail else "MOTION PASS (no >=24f run during words)")
sys.exit(1 if fail else 0)
