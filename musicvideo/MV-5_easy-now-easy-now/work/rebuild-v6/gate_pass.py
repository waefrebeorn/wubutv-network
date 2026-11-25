#!/usr/bin/env python3
"""MV-5 v6 gate pass data: (1) full-res frames at every grid line onset
(+0.10s) and onset+0.38s from the HOUSE MASTER for mouth-state/colour
reads; (2) audio agreement of master vs track.mp3 (per-10s-window Pearson
on 8kHz mono envelopes); (3) motion audit (per-frame mean-abs-diff at
160x90, near-dup runs >= 12f and >= 24f)."""
import json, os, subprocess, sys
import numpy as np

PROJ = "/home/hatch/workspace/wubutv-network/musicvideo/MV-5_easy-now-easy-now"
V6 = os.path.join(PROJ, "work", "rebuild-v6")
MASTER = os.path.join(PROJ, "masters", "mv5_easy_now_easy_now_16x9_v6.mp4")
FR = os.path.join(V6, "qc", "gate_frames")
os.makedirs(FR, exist_ok=True)
grid = json.load(open(os.path.join(PROJ, "work", "lyrics-redo", "grid_merged.json")))

# 1) onset frames
lines = grid["lines"]
for l in lines:
    for tag, dt in (("a", 0.10), ("b", 0.38)):
        t = min(l["start"] + dt, 206.2)
        out = os.path.join(FR, f"{l['id']}_{tag}.png")
        if not os.path.exists(out):
            subprocess.run(["ffmpeg", "-y", "-v", "error", "-ss", f"{t:.2f}",
                            "-i", MASTER, "-frames:v", "1", out], check=True)
print(f"onset frames: {len(os.listdir(FR))}", flush=True)

# 2) audio agreement
def decode_audio(path):
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-ac", "1",
                        "-ar", "8000", "-f", "f32le", "-"],
                       capture_output=True)
    return np.frombuffer(r.stdout, dtype=np.float32)

a = decode_audio(MASTER)
b = decode_audio(os.path.join(PROJ, "track.mp3"))
n = min(len(a), len(b))
a, b = a[:n], b[:n]
win = 80000  # 10 s
cors = []
for i in range(0, n - win, win):
    x, y = a[i:i + win], b[i:i + win]
    if x.std() > 1e-4 and y.std() > 1e-4:
        cors.append(float(np.corrcoef(x, y)[0, 1]))
    else:
        cors.append(1.0)  # mutual silence
print(f"audio windows: {len(cors)}  min corr {min(cors):.4f}  "
      f"mean {float(np.mean(cors)):.4f}", flush=True)

# 3) motion audit on the master (decoded luma diffs)
r = subprocess.run(["ffmpeg", "-v", "error", "-i", MASTER, "-vf",
                    "scale=160:90,fps=24,format=gray", "-f", "rawvideo", "-"],
                   capture_output=True)
buf = np.frombuffer(r.stdout, dtype=np.uint8)
nf = len(buf) // (160 * 90)
frames = buf[:nf * 160 * 90].reshape(nf, 160 * 90).astype(np.int16)
diffs = np.abs(np.diff(frames, axis=0)).mean(axis=1)
runs = []
cur = 0
for d in diffs:
    if d < 1.2:
        cur += 1
    else:
        if cur >= 12:
            runs.append(cur)
        cur = 0
if cur >= 12:
    runs.append(cur)
print(f"motion: frames {nf}  mean diff {diffs.mean():.2f}  "
      f"near-dup runs >=12f: {sorted(runs, reverse=True)[:8]}", flush=True)

json.dump({"audio_min_corr": min(cors), "audio_mean_corr": float(np.mean(cors)),
           "audio_windows": len(cors), "motion_frames": int(nf),
           "motion_mean_diff": float(diffs.mean()),
           "near_dup_runs_ge12f": sorted(runs, reverse=True)},
          open(os.path.join(V6, "qc", "gate_metrics.json"), "w"), indent=1)
print("gate metrics written", flush=True)
