#!/usr/bin/env python3
"""BLAM gate measurement on a finished master (FIRST3_BLAM_AUDIT recipe).
A1/A2/A3: 100ms RMS windows vs whole-file median.
A4: HF bursts — 10ms frames, >6.5kHz band (one-pole HP on 48k signal);
a burst = HF level >=18dB above the file's median HF frame level and a
local peak; counted 0-1.5s vs control window 30-45s (rate-normalised).
V1/V2: frame MAE at 320x180 gray, 0.25s buckets, baseline = mean 3-10s.
Usage: blam_master.py <master.mp4>"""
import subprocess, sys
import numpy as np

path = sys.argv[1]
raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-ac", "1", "-ar", "48000",
                      "-f", "f32le", "-"], capture_output=True, check=True).stdout
a = np.frombuffer(raw, dtype=np.float32)
win = 4800
nw = len(a) // win
rms = np.sqrt((a[:nw * win].reshape(nw, win) ** 2).mean(axis=1) + 1e-12)
db = 20 * np.log10(rms)
med = float(np.median(db))
def onset(thr):
    for i in range(nw - 1):
        if db[i] >= thr and db[i + 1] >= thr:
            return round(i * 0.1, 2)
    return None
sil = 0
for v in db:
    if v < med - 40: sil += 1
    else: break
print(f"AUDIO median {med:.1f} dB | t50 {onset(med-9.03)} | t90 {onset(med-0.91)} | "
      f"leading near-silence {sil*0.1:.1f}s | head 0-1s mean {db[:10].mean():.1f} dB "
      f"({db[:10].mean()-med:+.1f} vs median)")

# HF bursts: one-pole high-pass, fc ~6.5kHz at 48k
alpha = 0.46
hp = np.empty_like(a)
prev_x, prev_y = 0.0, 0.0
# vectorised approximation: use lfilter-style via scipy-free loop on downsampled envelope
# envelope approach: frame the signal at 10ms, HF energy via first-difference energy
d = np.diff(a)
fw = 480
nf = len(d) // fw
e = np.sqrt((d[:nf * fw].reshape(nf, fw) ** 2).mean(axis=1) + 1e-12)
edb = 20 * np.log10(e)
hmed = float(np.median(edb))
def bursts(t0, t1):
    i0, i1 = int(t0 * 100), int(t1 * 100)
    seg = edb[i0:i1]
    cnt = 0
    for i in range(1, len(seg) - 1):
        if seg[i] > hmed + 18 and seg[i] >= seg[i - 1] and seg[i] >= seg[i + 1]:
            cnt += 1
    return cnt
b_head = bursts(0, 1.5)
b_ctrl = bursts(30, 45)
print(f"A4 HF bursts: head 0-1.5s = {b_head} | control 30-45s = {b_ctrl} "
      f"(rate x{(b_head/1.5) / max(b_ctrl/15, 0.001):.2f} vs control)")

rawv = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-vf",
                       "fps=4,scale=320:180,format=gray", "-f", "rawvideo", "-"],
                      capture_output=True, check=True).stdout
fr = np.frombuffer(rawv, dtype=np.uint8)
n = fr.size // (320 * 180)
fr = fr[:n * 320 * 180].reshape(n, 320 * 180).astype(np.float32)
mae = np.abs(np.diff(fr, axis=0)).mean(axis=1)
buckets = mae[:12]
baseline = mae[12:40].mean()
head = mae[:2].mean()
print(f"VIDEO buckets 0-3s: {[round(float(x),1) for x in buckets]}")
print(f"V1 head 0-0.5s mean {head:.2f} vs baseline {baseline:.2f} = {head/baseline:.2f}x | "
      f"V2 first bucket {buckets[0]:.2f} vs strongest {buckets.max():.2f} = {buckets[0]/buckets.max()*100:.0f}%")
