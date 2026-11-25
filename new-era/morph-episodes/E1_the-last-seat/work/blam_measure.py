#!/usr/bin/env python3
"""BLAM gate measurement — replicates FIRST3_BLAM_AUDIT_2026-11-15.md §2/§4 methodology.
Usage: blam_measure.py <video> [label]
Audio bars are computed against the file's OWN median window level (100ms RMS windows).
A1 t50<=0.5s, t90<=1.5s (sustained 2 windows) | A2 dead head <=0.2s |
A3 head 0-1s mean within 6 dB of median, or accent <=0.5s | A4 HF bursts head <=2x control.
V1 mean frame-MAE 0-0.5s >= 0.6x baseline (3-10s) | V2 first 0.25s bucket >= 50% of
strongest 0-3s bucket or >= 4.0 absolute. Frame MAE at 320x180 gray.
"""
import json, subprocess, sys
import numpy as np

def audio_pcm(path):
    out = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-map", "0:a:0",
                          "-ac", "1", "-ar", "48000", "-f", "s16le", "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(out, dtype=np.int16).astype(np.float64) / 32768.0

def hf_bursts(x, sr, t0, t1):
    """Count HF transient bursts in [t0,t1): 5ms windows of >6kHz energy spiking
    above 8x the local median, 20ms refractory."""
    seg = x[int(t0 * sr):int(t1 * sr)]
    if len(seg) < sr // 10:
        return 0
    # crude highpass: subtract 1ms moving average
    k = max(1, sr // 1000)
    ma = np.convolve(seg, np.ones(k) / k, mode="same")
    hf = seg - ma
    w = sr // 200  # 5ms
    n = len(hf) // w
    rms = np.sqrt((hf[:n * w].reshape(n, w) ** 2).mean(axis=1) + 1e-12)
    med = np.median(rms)
    thr = max(8.0 * med, 1e-4)
    count, last = 0, -10
    for i, v in enumerate(rms):
        if v > thr and i - last >= 4:
            count += 1
            last = i
    return count

def frame_maes(path):
    out = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-map", "0:v:0",
                          "-vf", "scale=320:180,format=gray", "-f", "rawvideo", "-"],
                         capture_output=True, check=True).stdout
    fw = 320 * 180
    n = len(out) // fw
    fr = np.frombuffer(out[:n * fw], dtype=np.uint8).astype(np.float64).reshape(n, fw)
    return np.abs(np.diff(fr, axis=0)).mean(axis=1)  # len n-1, mae[i] = frame i -> i+1

def main():
    path = sys.argv[1]
    label = sys.argv[2] if len(sys.argv) > 2 else path
    sr = 48000
    x = audio_pcm(path)
    win = sr // 10
    n = len(x) // win
    rms = np.sqrt((x[:n * win].reshape(n, win) ** 2).mean(axis=1) + 1e-12)
    med = float(np.median(rms))
    med_db = 20 * np.log10(med + 1e-12)

    def sustained(level_frac):
        thr = level_frac * med
        for i in range(n - 1):
            if rms[i] >= thr and rms[i + 1] >= thr:
                return round(i * 0.1, 2)
        return None

    t50, t90 = sustained(0.5), sustained(0.9)
    dead_thr = max(10 ** (-50 / 20), 0.05 * med)
    dead = 0
    for v in rms:
        if v < dead_thr:
            dead += 1
        else:
            break
    dead_head = round(dead * 0.1, 2)
    head_mean_db = 20 * np.log10(float(rms[:10].mean()) + 1e-12)
    accent = bool(rms[:5].max() >= med)  # a window at/above median within 0.5s
    a3_pass = (head_mean_db >= med_db - 6.0) or accent
    bursts_head = hf_bursts(x, sr, 0.0, 1.5)
    dur = len(x) / sr
    c0 = max(1.5, dur / 2 - 0.75)
    bursts_ctrl = hf_bursts(x, sr, c0, c0 + 1.5)
    ratio = (bursts_head / bursts_ctrl) if bursts_ctrl > 0 else (float("inf") if bursts_head else 0.0)

    maes = frame_maes(path)
    fps = 24.0
    def mae_range(a, b):
        i0, i1 = int(a * fps), min(int(b * fps), len(maes))
        return float(maes[i0:i1].mean()) if i1 > i0 else 0.0
    base = mae_range(3.0, 10.0)
    open_mae = mae_range(0.0, 0.5)
    v1 = open_mae / base if base > 0 else 0.0
    buckets = [mae_range(i * 0.25, (i + 1) * 0.25) for i in range(12)]
    v2_first = buckets[0]
    v2_pass = v2_first >= 0.5 * max(buckets) or v2_first >= 4.0

    res = {
        "label": label,
        "median_dbfs": round(med_db, 2),
        "A1_t50_s": t50, "A1_t90_s": t90,
        "A1_pass": bool(t50 is not None and t50 <= 0.5 and t90 is not None and t90 <= 1.5),
        "A2_dead_head_s": dead_head, "A2_pass": bool(dead_head <= 0.2),
        "A3_head_mean_db": round(head_mean_db, 2), "A3_delta_db": round(head_mean_db - med_db, 2),
        "A3_accent_le_0.5s": accent, "A3_pass": bool(a3_pass),
        "A4_bursts_head_0_1.5s": bursts_head, "A4_bursts_control": bursts_ctrl,
        "A4_ratio": (round(ratio, 2) if ratio != float("inf") else "inf"),
        "A4_pass": bool(ratio <= 2.0),
        "V1_open_mae": round(open_mae, 2), "V1_baseline_mae": round(base, 2),
        "V1_ratio": round(v1, 2), "V1_pass": bool(v1 >= 0.6),
        "V2_first_bucket_mae": round(v2_first, 2), "V2_max_bucket_mae": round(max(buckets), 2),
        "V2_pass": bool(v2_pass),
        "buckets_0_3s": [round(b, 1) for b in buckets],
    }
    print(json.dumps(res, indent=1))

if __name__ == "__main__":
    main()
