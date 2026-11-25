#!/usr/bin/env python3
"""E2 SHOW-3 measurement harness — BLAM gate + joint gate + tail scan.

Conventions follow FIRST3_BLAM_AUDIT_2026-11-15: 100 ms RMS windows
vs the file's own median loudness; frame MAE at 320x180 gray; HF
burst counts (highpass 5 kHz envelope peaks > 6x local median) in
0-1.5 s vs a mid-video 1.5 s control window.
"""
import json
import subprocess
import sys
import os

import numpy as np

W, H = 320, 180


def wav(path, hp=False):
    cmd = ["ffmpeg", "-v", "error", "-i", path]
    if hp:
        cmd += ["-af", "highpass=f=5000"]
    cmd += ["-ac", "1", "-ar", "48000", "-f", "f32le", "-"]
    raw = subprocess.run(cmd, capture_output=True).stdout
    return np.frombuffer(raw, dtype=np.float32)


def gray_frames(path, t0, t1):
    dur = t1 - t0
    cmd = ["ffmpeg", "-v", "error", "-ss", str(t0), "-i", path,
           "-t", str(dur), "-vf", f"scale={W}:{H},format=gray",
           "-f", "rawvideo", "-"]
    raw = subprocess.run(cmd, capture_output=True).stdout
    n = len(raw) // (W * H)
    return np.frombuffer(raw[: n * W * H], dtype=np.uint8).reshape(n, W * H).astype(np.float32)


def probe(path):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0",
         "-show_entries", "stream=nb_frames,r_frame_rate,duration",
         "-of", "json", path], capture_output=True, text=True).stdout
    s = json.loads(out)["streams"][0]
    return s


def audio_metrics(path):
    x = wav(path)
    sr = 48000
    win = sr // 10
    n = len(x) // win
    rms = np.sqrt(np.mean(x[: n * win].reshape(n, win) ** 2, axis=1) + 1e-12)
    db = 20 * np.log10(rms + 1e-9)
    med = np.median(rms)
    med_db = 20 * np.log10(med + 1e-9)

    def t_reach(frac):
        thr = med * frac
        for i in range(n - 1):
            if rms[i] >= thr and rms[i + 1] >= thr:
                return round(i * 0.1, 2)
        return None

    silence_thr = max(10 ** (-50 / 20), med * 0.05)
    lead = 0
    for r in rms:
        if r < silence_thr:
            lead += 1
        else:
            break
    head_db = float(np.mean(db[:10])) if n >= 10 else None

    hp = wav(path, hp=True)
    hop = 240  # 5 ms
    m = len(hp) // hop
    env = np.max(np.abs(hp[: m * hop].reshape(m, hop)), axis=1)

    def bursts(a, b):
        i0, i1 = int(a * 200), int(b * 200)
        seg = env[i0:i1]
        if len(seg) == 0:
            return 0
        thr = np.median(seg) * 6 + 1e-6
        cnt, i = 0, 1
        while i < len(seg) - 1:
            if seg[i] > thr and seg[i] >= seg[i - 1] and seg[i] >= seg[i + 1]:
                cnt += 1
                i += 10  # 50 ms refractory
            else:
                i += 1
        return cnt

    dur = len(x) / sr
    c0 = max(0.0, dur / 2 - 0.75)
    return {
        "median_dbfs": round(float(med_db), 1),
        "t50_s": t_reach(0.5), "t90_s": t_reach(0.9),
        "lead_silence_s": round(lead * 0.1, 2),
        "head_db_0_1s": round(head_db, 1) if head_db is not None else None,
        "head_minus_median_db": round(head_db - med_db, 1) if head_db is not None else None,
        "hf_bursts_head": bursts(0.0, 1.5),
        "hf_bursts_control": bursts(c0, c0 + 1.5),
    }


def mae_buckets(path, fps=24):
    fr = gray_frames(path, 0, 10.0)
    if len(fr) < 2:
        return {}
    mae = np.mean(np.abs(np.diff(fr, axis=0)), axis=1)  # per frame-step
    buckets = {}
    for b in range(12):
        seg = mae[b * 6:(b + 1) * 6]
        buckets[f"{b*0.25:.2f}-{(b+1)*0.25:.2f}"] = round(float(np.mean(seg)), 2) if len(seg) else None
    base = mae[72:216]  # 3-9 s steps approx (frame idx at 24fps)
    baseline = float(np.mean(base)) if len(base) else None
    m005 = float(np.mean(mae[:12])) if len(mae) >= 12 else None
    return {
        "buckets_0_3s": buckets,
        "baseline_mae_3_10s": round(baseline, 2) if baseline else None,
        "motion_0_0.5s": round(m005, 2) if m005 else None,
        "v1_ratio": round(m005 / baseline, 2) if (m005 and baseline) else None,
        "first_bucket": buckets.get("0.00-0.25"),
        "strongest_bucket_0_3s": max(v for v in buckets.values() if v is not None),
    }


def blam(path):
    a = audio_metrics(path)
    v = mae_buckets(path)
    res = {"file": os.path.basename(path), "audio": a, "video": v}
    checks = {}
    if a["t50_s"] is not None:
        checks["A1"] = a["t50_s"] <= 0.5 and (a["t90_s"] is not None and a["t90_s"] <= 1.5)
    checks["A2"] = a["lead_silence_s"] <= 0.2
    checks["A3"] = (a["head_minus_median_db"] is not None and a["head_minus_median_db"] >= -6)
    checks["A4"] = a["hf_bursts_head"] <= 2 * max(1, a["hf_bursts_control"])
    if v.get("v1_ratio") is not None:
        checks["V1"] = v["v1_ratio"] >= 0.6
        checks["V2"] = (v["first_bucket"] >= 0.5 * v["strongest_bucket_0_3s"]) or (v["first_bucket"] >= 4.0)
    res["checks"] = {k: bool(v) for k, v in checks.items()}
    return res


def tail_scan(path):
    """Find the joint frame: scan final 15% of frames; return the last
    frame index whose following-frame MAE is >= the take's median MAE."""
    info = probe(path)
    nb = int(info.get("nb_frames") or 0)
    fr = gray_frames(path, 0, 10.0)
    n = len(fr)
    mae = np.mean(np.abs(np.diff(fr, axis=0)), axis=1)
    med = float(np.median(mae))
    start = int(n * 0.85)
    joint = n - 2
    for i in range(n - 2, start, -1):
        if mae[i] >= med:
            joint = i
            break
    return {"frames_read": n, "nb_frames_probe": nb, "median_mae": round(med, 2),
            "joint_frame_idx": int(joint), "joint_mae": round(float(mae[joint]), 2)}


def seam(png_a, png_b):
    from PIL import Image
    a = np.asarray(Image.open(png_a).convert("L").resize((W, H)), dtype=np.float32)
    b = np.asarray(Image.open(png_b).convert("L").resize((W, H)), dtype=np.float32)
    return round(float(np.mean(np.abs(a - b))), 2)


if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "blam":
        print(json.dumps(blam(sys.argv[2]), indent=1))
    elif mode == "tail":
        print(json.dumps(tail_scan(sys.argv[2]), indent=1))
    elif mode == "seam":
        print(json.dumps({"seam_mae": seam(sys.argv[2], sys.argv[3])}))
    elif mode == "audio":
        print(json.dumps(audio_metrics(sys.argv[2]), indent=1))
