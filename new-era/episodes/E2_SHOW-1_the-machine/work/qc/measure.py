#!/usr/bin/env python3
"""BLAM + head-motion measurement for one video file (audit method).
Audio: 100ms RMS windows, median of full runtime, t50/t90 (sustained 2
windows), lead near-silence, HF burst counts head vs mid control.
Video: frame-to-frame MAE at 320x180 gray, 0.25s buckets.
Usage: measure.py <file.mp4> [label]
"""
import json, subprocess, sys, math
import numpy as np

def audio_env(path):
    raw = subprocess.run(["ffmpeg","-v","error","-i",path,"-vn","-ac","1","-ar","16000","-f","f32le","-"],
                         capture_output=True).stdout
    x = np.frombuffer(raw, dtype=np.float32)
    sr = 16000; win = sr//10
    n = len(x)//win
    rms = np.array([np.sqrt(np.mean(x[i*win:(i+1)*win]**2)+1e-12) for i in range(n)])
    db = 20*np.log10(rms+1e-9)
    return db

def bursts(path, t0, t1):
    raw = subprocess.run(["ffmpeg","-v","error","-ss",str(t0),"-i",path,"-t",str(t1-t0),
                          "-vn","-ac","1","-ar","16000","-f","f32le","-"], capture_output=True).stdout
    x = np.frombuffer(raw, dtype=np.float32)
    if len(x) < 1600: return 0
    # crude HF transient proxy: high-pass via diff, count 10ms frames whose
    # HF energy spikes > 6x the window median
    d = np.abs(np.diff(x))
    win = 160
    n = len(d)//win
    e = np.array([np.mean(d[i*win:(i+1)*win]) for i in range(n)])
    med = np.median(e)+1e-9
    return int(np.sum(e > 6*med))

def mae_series(path, t_end=10.0):
    raw = subprocess.run(["ffmpeg","-v","error","-i",path,"-vf","scale=320:180,format=gray",
                          "-t",str(t_end),"-f","rawvideo","-"], capture_output=True).stdout
    fr = 320*180
    n = len(raw)//fr
    frames = np.frombuffer(raw[:n*fr], dtype=np.uint8).reshape(n, fr).astype(np.float32)
    mae = np.abs(np.diff(frames, axis=0)).mean(axis=1)
    return mae  # per-frame-step MAE, 24 per second

def main():
    path, label = sys.argv[1], (sys.argv[2] if len(sys.argv)>2 else "")
    db = audio_env(path)
    med = float(np.median(db))
    med_lin = 10**(med/20)
    rms_lin = 10**(db/20)
    def t_reach(frac):
        thr = frac*med_lin
        for i in range(len(rms_lin)-1):
            if rms_lin[i] >= thr and rms_lin[i+1] >= thr:
                return round(i*0.1, 2)
        return None
    thr_sil = max(-50.0, med + 20*math.log10(0.05))
    lead = 0.0
    for v in db:
        if v < thr_sil: lead += 0.1
        else: break
    head_db = [round(float(np.mean(db[i*5:(i+1)*5])),1) for i in range(6)]  # 0.5s means, first 3s
    mae = mae_series(path)
    buckets = [round(float(np.mean(mae[i*6:(i+1)*6])),2) for i in range(12)]  # 0.25s buckets 0-3s
    base = float(np.mean(mae[72:240])) if len(mae) >= 240 else float(np.mean(mae[72:]))
    out = {
        "label": label, "path": path,
        "audio_median_dbfs": round(med,1),
        "t50_s": t_reach(0.5), "t90_s": t_reach(0.9),
        "lead_silence_s": round(lead,2),
        "head_db_per_0.5s": head_db,
        "hf_bursts_0_1.5s": bursts(path, 0, 1.5),
        "hf_bursts_control_30s": bursts(path, 30.0, 31.5) if "master" in label else bursts(path, 5.0, 6.5),
        "mae_buckets_0_3s": buckets,
        "mae_baseline_3_10s": round(base,2),
        "mae_head_0_0.5s_ratio": round(float(np.mean(mae[0:12]))/base, 2) if base else None,
        "mae_first_bucket_vs_max_0_3s": round(float(np.mean(mae[0:6]))/max(float(np.mean(mae[i*6:(i+1)*6])) for i in range(12)), 2),
    }
    print(json.dumps(out, indent=1))

if __name__ == "__main__":
    main()
