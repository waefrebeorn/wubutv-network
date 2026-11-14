#!/usr/bin/env python3
"""MV-5 v4 gate parts (c2) and (d):
- frame-diff series (160x90 gray) over the master
- (d) near-dup runs (mean abs diff < 0.5) of >= 24 frames while song words
  are playing (aligned grid); S01 leader frames 0-39 sanctioned (pre-word)
- (c2) cut-point continuity: for every piece boundary in the plan, the
  diff across the boundary frame pair in the master; a ~0 diff at a
  boundary where the take changes = suspected clone/freeze artifact.
Writes work/gate_v4/motion_v4.json.
"""
import json, os, subprocess
import numpy as np

PROJ = os.path.dirname(os.path.abspath(__file__))
MASTER = os.path.join(PROJ, "masters", "mv5_easy_now_easy_now_16x9_v4.mp4")
GATE = os.path.join(PROJ, "work", "gate_v4")
os.makedirs(GATE, exist_ok=True)
W, H, FPS = 160, 90, 24

raw = subprocess.run(["ffmpeg", "-v", "error", "-i", MASTER, "-vf",
                      f"scale={W}:{H},format=gray", "-f", "rawvideo", "-"],
                     capture_output=True).stdout
n = len(raw) // (W * H)
frames = np.frombuffer(raw[:n * W * H], dtype=np.uint8).reshape(n, H, W).astype(np.float32)
print("frames decoded:", n)
diffs = np.abs(np.diff(frames, axis=0)).mean(axis=(1, 2))
np.save(os.path.join(GATE, "diffs_v4.npy"), diffs)

# word-active spans (seconds) from aligned grid
al = json.load(open(os.path.join(PROJ, "work", "gemini_song_words_aligned.json")))["rows"]
spans = []
for r in al:
    t0 = r["app_start"] if r["app_start"] is not None else r["song_start"]
    t1 = r["app_end"] if r["app_end"] is not None else r["song_end"]
    if t0 is not None and t1 is not None:
        spans.append((t0, t1))

def words_playing(fidx):
    t = fidx / FPS
    return any(a - 0.05 <= t <= b + 0.05 for a, b in spans)

# near-dup runs
runs = []
i = 0
d = np.concatenate([diffs, [99.0]])
while i < len(d):
    if d[i] < 0.5:
        j = i
        while j < len(d) and d[j] < 0.5:
            j += 1
        runs.append((i, j - i))  # start frame, length in diffs (~frames)
        i = j
    else:
        i += 1
bad = []
for start, ln in runs:
    if ln >= 24:
        sanctioned = (start == 0 and ln <= 40)
        bad.append({"start_frame": start, "length": ln,
                    "start_s": round(start / FPS, 2),
                    "words_playing": words_playing(start + ln // 2),
                    "sanctioned_leader": sanctioned})
print("near-dup runs >=24f:", bad)

# cut-point continuity
fit = json.load(open(os.path.join(PROJ, "work", "assembly_fit_mv5_v4.json")))
pieces = []
for sc in fit["scenes"]:
    for p in fit["plan"][sc]:
        q = dict(p)
        q["scene"] = sc
        pieces.append(q)
pieces.sort(key=lambda p: p["dst0"])
cuts = []
fpos = 0
for i, p in enumerate(pieces):
    fpos += p["out"]
    if i < len(pieces) - 1 and 0 < fpos - 1 < len(diffs):
        cuts.append({"frame": fpos, "at_s": round(fpos / FPS, 2),
                     "from": f"{p['scene']}/{p['kind']}/{p['take']}",
                     "to": f"{pieces[i+1]['scene']}/{pieces[i+1]['kind']}/{pieces[i+1]['take']}",
                     "diff_across_cut": round(float(diffs[fpos - 1]), 3)})
frozen_cuts = [c for c in cuts if c["diff_across_cut"] < 0.5]
print("piece boundaries:", len(cuts), " frozen-looking cuts:", len(frozen_cuts))

json.dump({"frames": n, "mean_diff": round(float(diffs.mean()), 3),
           "neardup_runs_ge24": bad, "cuts": cuts, "frozen_cuts": frozen_cuts},
          open(os.path.join(GATE, "motion_v4.json"), "w"), indent=1)
print("wrote work/gate_v4/motion_v4.json")
