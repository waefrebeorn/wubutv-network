#!/usr/bin/env python3
"""Per-take QC: contact frames, head-motion MAE, audio onset (BLAM-style).
Usage: qc_take.py <take.mp4> <unit> <outdir>
Audio recipe (matches FIRST3_BLAM_AUDIT method): 100ms RMS windows,
median = whole-file median window level; onset t50/t90 = first time the
level reaches median-9.03dB / median-0.91dB sustained 2 windows;
near-silence = window below median-40dB.
Video: frame MAE at 320x180 gray, 0.25s buckets.
"""
import json, subprocess, sys, os
import numpy as np

take, unit, outdir = sys.argv[1], sys.argv[2], sys.argv[3]
os.makedirs(outdir, exist_ok=True)

# contact frames
times = [0, 0.5, 2.5, 5.0, 7.5, 9.6]
for t in times:
    subprocess.run(["ffmpeg", "-v", "error", "-ss", str(t), "-i", take,
                    "-frames:v", "1", "-q:v", "3",
                    os.path.join(outdir, f"f{t}.jpg")], check=True)
sheet = os.path.join(outdir, "sheet.jpg")
subprocess.run(["ffmpeg", "-v", "error",
                "-i", os.path.join(outdir, "f0.jpg"), "-i", os.path.join(outdir, "f0.5.jpg"),
                "-i", os.path.join(outdir, "f2.5.jpg"), "-i", os.path.join(outdir, "f5.0.jpg"),
                "-i", os.path.join(outdir, "f7.5.jpg"), "-i", os.path.join(outdir, "f9.6.jpg"),
                "-filter_complex", "[0][1][2]hstack=3[top];[3][4][5]hstack=3[bot];[top][bot]vstack=2,scale=1560:-1",
                "-q:v", "3", sheet], check=True)

# --- video MAE: decode small gray frames at 4fps for 10s
raw = subprocess.run(["ffmpeg", "-v", "error", "-i", take, "-vf",
                      "fps=4,scale=320:180,format=gray", "-f", "rawvideo", "-"],
                     capture_output=True, check=True).stdout
fr = np.frombuffer(raw, dtype=np.uint8)
n = fr.size // (320 * 180)
fr = fr[:n * 320 * 180].reshape(n, 320 * 180).astype(np.float32)
mae = np.abs(np.diff(fr, axis=0)).mean(axis=1)  # mae[i] = frame i -> i+1 (0.25s steps)
buckets = mae[:12]  # 0..3s in 0.25s buckets
baseline = mae[12:].mean() if n > 13 else float("nan")
head05 = mae[:2].mean()
res = {"unit": unit, "frames_decoded": int(n),
       "mae_buckets_0_3s": [round(float(x), 2) for x in buckets],
       "mae_baseline_3_10s": round(float(baseline), 2),
       "mae_head_0_0.5s": round(float(head05), 2),
       "head_motion_ratio": round(float(head05 / baseline), 2) if baseline else None}

# --- audio onset
wav = subprocess.run(["ffmpeg", "-v", "error", "-i", take, "-ac", "1", "-ar", "16000",
                      "-f", "f32le", "-"], capture_output=True, check=True).stdout
a = np.frombuffer(wav, dtype=np.float32)
win = 1600  # 100ms
nw = len(a) // win
rms = np.sqrt((a[:nw * win].reshape(nw, win) ** 2).mean(axis=1) + 1e-12)
db = 20 * np.log10(rms)
med = float(np.median(db))
def onset(thr_db):
    for i in range(nw - 1):
        if db[i] >= thr_db and db[i + 1] >= thr_db:
            return round(i * 0.1, 2)
    return None
sil = 0
for v in db:
    if v < med - 40: sil += 1
    else: break
res.update({"audio_median_db": round(med, 1),
            "t50": onset(med - 9.03), "t90": onset(med - 0.91),
            "leading_near_silence_s": round(sil * 0.1, 2),
            "head_mean_0_1s_db": round(float(db[:10].mean()), 1),
            "head_vs_median_db": round(float(db[:10].mean() - med), 1)})
print(json.dumps(res, indent=1))
