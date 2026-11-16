#!/usr/bin/env python3
"""BLAM gate measurement (audit method): A1-A4 audio, V1/V2 video on first 3s.
Usage: blam_measure.py <video> [label]"""
import json, subprocess, sys
import numpy as np
from PIL import Image
import io

path = sys.argv[1]
label = sys.argv[2] if len(sys.argv) > 2 else path

# ---------- audio ----------
raw = subprocess.run(['ffmpeg','-v','error','-i',path,'-f','f32le','-ac','1',
                      '-ar','16000','-'], capture_output=True).stdout
x = np.frombuffer(raw, dtype=np.float32).copy()
sr = 16000
win = int(0.1*sr)
n = len(x)//win
rms = np.sqrt(np.mean(x[:n*win].reshape(n,win)**2, axis=1) + 1e-12)
db = 20*np.log10(rms + 1e-9)
median_db = float(np.median(db))
# t50/t90 over first 3s cumulative energy
e3 = (rms[:30]**2)
cum = np.cumsum(e3); tot = cum[-1]
t50 = float((np.argmax(cum >= 0.5*tot)+1)*0.1)
t90 = float((np.argmax(cum >= 0.9*tot)+1)*0.1)
# lead silence: initial windows below median-25dB
thr = median_db - 25
lead = 0
for v in db:
    if v < thr: lead += 1
    else: break
lead_s = lead*0.1
# A3: mean level 0-1.0s vs median
head_db = float(20*np.log10(np.sqrt(np.mean(x[:sr]**2)) + 1e-9))
a3_delta = head_db - median_db
# accent: loudest 100ms window in first 0.5s
accent_db = float(np.max(db[:5]))
# A4 crackle: high-pass bursts, head 0-1.5s vs control 30-31.5s
k = int(0.02*sr)
ma = np.convolve(x, np.ones(k)/k, mode='same')
hp = x - ma
hw = int(0.01*sr)
def bursts(t0, t1):
    seg = hp[int(t0*sr):int(t1*sr)]
    m = len(seg)//hw
    if m == 0: return 0, 0.0
    e = np.sqrt(np.mean(seg[:m*hw].reshape(m,hw)**2, axis=1) + 1e-12)
    return e, None
dur_s = len(x)/sr
ctrl_span = (30.0, 31.5) if dur_s > 32 else (5.0, 6.5)
ctrl_e, _ = bursts(*ctrl_span)
floor = float(np.median(ctrl_e)) if hasattr(ctrl_e, '__len__') else 0.0
head_e, _ = bursts(0.0, 1.5)
b_head = int(np.sum(head_e > 6*max(floor,1e-6)))
b_ctrl = int(np.sum(ctrl_e > 6*max(floor,1e-6)))

# ---------- video ----------
def frame_mae_series(t_end=10.0):
    # extract frames at native fps downscaled 320x180 gray raw
    out = subprocess.run(['ffmpeg','-v','error','-i',path,'-t',str(t_end),
                          '-vf','scale=320:180,format=gray','-f','rawvideo','-'],
                         capture_output=True).stdout
    fs = 320*180
    nf = len(out)//fs
    frames = np.frombuffer(out[:nf*fs], dtype=np.uint8).reshape(nf,180,320).astype(np.float32)
    mae = np.abs(np.diff(frames, axis=0)).mean(axis=(1,2))
    return mae  # mae[i] = |f[i+1]-f[i]|, frame i at t=i/24

mae = frame_mae_series(10.0)
fps = 24
b = []
for i in range(12):
    seg = mae[i*6:(i+1)*6]
    b.append(float(np.mean(seg)) if len(seg) else 0.0)
baseline = float(np.mean(mae[3*fps:10*fps])) if len(mae) > 10*fps else float(np.mean(mae[3*fps:]))
motion_0_05 = float(np.mean(mae[:12]))
v1 = motion_0_05/baseline if baseline > 0 else 0.0
v2_first = b[0]
v2_ok = (v2_first >= 0.5*max(b)) or (v2_first >= 4.0)

res = {
 'label': label,
 'audio': {'median_dbfs': round(median_db,1), 't50_s': t50, 't90_s': t90,
           'lead_silence_s': round(lead_s,2), 'head_db_0_1s': round(head_db,1),
           'a3_delta_db': round(a3_delta,1), 'accent_db_first_0.5s': round(accent_db,1),
           'crackle_head': b_head, 'crackle_ctrl': b_ctrl},
 'video': {'mae_buckets_0.25s': [round(v,2) for v in b],
           'baseline_mae_3_10s': round(baseline,2),
           'motion_0_0.5s': round(motion_0_05,2), 'v1_ratio': round(v1,2),
           'v2_first_bucket': round(v2_first,2), 'v2_ok': bool(v2_ok)},
 'gate': {'A1': bool(t50 <= 0.5 and t90 <= 1.5), 'A2': bool(lead_s <= 0.2),
          'A3': bool(abs(a3_delta) <= 6 or accent_db >= median_db - 6),
          'A4': bool(b_head <= 2*max(b_ctrl,1)),
          'V1': bool(v1 >= 0.6), 'V2': bool(v2_ok)}}
print(json.dumps(res, indent=1))
