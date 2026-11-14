#!/usr/bin/env python3
"""Volley 6 QC driver: wav extract + transcribe + frame rule + 2fps sheet + RMS bins."""
import json, subprocess, sys, wave
import numpy as np

BASE = "/home/hatch/workspace/wubutv-network/musicvideo/MV-7_the-nobody-man"
TAKES = {
    "mv7_s20_t1": ("takes/media-generation-mv7v2-s20-final-chorus-fc1-fc4-0-95f874f2-e42c-4981-9b3a-4399014ab0f5.mp4", 0.5, 9.5),
    "mv7_s21_t1": ("takes/media-generation-mv7v2-s21-final-chorus-fc5-fc7-0-f901dd60-cd98-43d9-8ccb-be6c026ee373.mp4", 0.5, 9.5),
    "mv7_s22_t1": ("takes/media-generation-mv7v2-s22-final-chorus-fc8-fc9-0-8461ab5e-54b4-45ef-a0ba-e937660d824f.mp4", 0.5, 9.5),
    "mv7_s23_t1": ("takes/media-generation-mv7v2-s23-final-chorus-fc10-0-553c819f-bd9e-4823-ae36-e538adf3d0d7.mp4", 0.5, 9.5),
    # S24 chants 0.5-5.5s, then holds silent to the end: frame rule over the vocal window.
    "mv7_s24_t1": ("takes/media-generation-mv7v2-s24-final-chorus-tag-cha-0-8a6124cb-18e1-44a4-a038-d3a768b78605.mp4", 0.5, 5.5),
}

def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, **kw)

for tag, (rel, w0, w1) in TAKES.items():
    p = f"{BASE}/{rel}"
    wav = f"{BASE}/work/qc_v7/{tag}_16k.wav"
    run(["ffmpeg", "-v", "error", "-y", "-i", p, "-ar", "16000", "-ac", "1", wav])
    out = run(["python3", f"{BASE}/work/qc_v7/transcribe_take.py", wav, f"{BASE}/work/qc_v7/{tag}_words.json"])
    print(f"== {tag} transcribe rc={out.returncode}")
    print(out.stdout.strip())
    if out.returncode != 0:
        print(out.stderr[-2000:])
    fr = run(["python3", f"{BASE}/work/qc_v7/frame_rule.py", p, str(w0), str(w1)])
    print(f"== {tag} frame_rule: {fr.stdout.strip()}")
    sheet = f"{BASE}/work/qc_v7/{tag}_sheet.png"
    run(["ffmpeg", "-v", "error", "-y", "-i", p, "-vf", "fps=2,scale=320:-1,tile=5x4", "-frames:v", "1", sheet])
    with wave.open(wav, "rb") as w:
        n, ch, sw = w.getnframes(), w.getnchannels(), w.getsampwidth()
        raw = w.readframes(n)
    a = np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0
    if ch > 1:
        a = a.reshape(-1, ch)[:, 0]
    bins = []
    for i in range(20):
        seg = a[int(i * 0.5 * 16000):int((i + 1) * 0.5 * 16000)]
        bins.append(round(float(np.sqrt((seg ** 2).mean())), 4) if len(seg) else 0.0)
    print(f"== {tag} RMS 0.5s bins: {bins}")
    print(flush=True)
print("ALL DONE")
