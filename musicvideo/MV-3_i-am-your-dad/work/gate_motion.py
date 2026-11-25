#!/usr/bin/env python3
"""Gate (d) motion audit for a master: per-frame mean abs diff at 160x90.

Checks (Slopcannon frame rule):
- no frozen run >= 24 frames DURING words (diff < 0.35 = near-dup)
- no scene with vocal mean-diff < 0.5
Usage: gate_motion.py <master.mp4> <out.json>
"""
import json, subprocess, sys
import numpy as np

W, H, FPS = 160, 90, 24
master, out_path = sys.argv[1], sys.argv[2]

raw = subprocess.run(
    ["ffmpeg", "-v", "error", "-i", master, "-vf", f"scale={W}:{H},format=gray",
     "-f", "rawvideo", "-"], capture_output=True, check=True).stdout
n = len(raw) // (W * H)
frames = np.frombuffer(raw[:n * W * H], dtype=np.uint8).reshape(n, W * H).astype(np.float32)
diffs = np.abs(np.diff(frames, axis=0)).mean(axis=1)  # diffs[i] = |f[i+1]-f[i]|

d = json.load(open("SONG_WORDS.json"))
words = d["words"] if isinstance(d, dict) else d
vocal = np.zeros(n, dtype=bool)
for w in words:
    a, b = int(w[1] * FPS), int(w[2] * FPS) + 1
    vocal[a:min(b, n)] = True

# frozen runs during words: diff < 0.35 sustained
frozen = diffs < 0.35
runs, cur = [], 0
for i in range(len(frozen)):
    if frozen[i] and vocal[i]:
        cur += 1
    else:
        if cur: runs.append(cur)
        cur = 0
if cur: runs.append(cur)
longest_frozen_vocal = max(runs) if runs else 0

# per-scene vocal mean diff
import os
sys.path.insert(0, os.getcwd())
import assemble_mv3_recut as base
starts = [(sc, round(st * FPS)) for sc, st, _ in base.SCENES]
scene_stats = {}
for i, (sc, sf) in enumerate(starts):
    ef = starts[i + 1][1] if i + 1 < len(starts) else n
    seg_vocal = vocal[sf:ef]
    seg_diffs = diffs[sf:ef - 1] if ef - 1 > sf else np.array([0.0])
    m = seg_diffs[seg_vocal[:len(seg_diffs)]] if seg_vocal.any() else seg_diffs
    scene_stats[sc] = {
        "vocal_mean_diff": round(float(m.mean()), 3) if len(m) else None,
        "min_mean_diff": round(float(seg_diffs.min()), 3) if len(seg_diffs) else None,
    }
bad_scenes = {s: v for s, v in scene_stats.items()
              if v["vocal_mean_diff"] is not None and v["vocal_mean_diff"] < 0.5}
report = {
    "master": master, "frames": int(n),
    "longest_frozen_run_during_words_f": int(longest_frozen_vocal),
    "frozen_gate_pass": bool(longest_frozen_vocal < 24),
    "scenes_below_0.5_vocal_mean_diff": bad_scenes,
    "scene_stats": scene_stats,
}
json.dump(report, open(out_path, "w"), indent=1)
print(json.dumps({k: report[k] for k in
                  ("frames", "longest_frozen_run_during_words_f",
                   "frozen_gate_pass", "scenes_below_0.5_vocal_mean_diff")}, indent=1))
