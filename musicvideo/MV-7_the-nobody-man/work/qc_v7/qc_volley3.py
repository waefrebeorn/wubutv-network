#!/usr/bin/env python3
"""Volley 3 QC driver: wav extract + transcribe + frame rule + 2fps sheet + RMS bins."""
import json, subprocess, sys, wave
import numpy as np

BASE = "/home/hatch/workspace/wubutv-network/musicvideo/MV-7_the-nobody-man"
TAKES = {
    "mv7_s01_t3": ("takes/media-generation-mv7v2-s01-v4-intro-chant-i1-so-0-27ce3c0b-70af-433b-806d-6b832f16c405.mp4", 0.5, 9.5),
    "mv7_s05_t3a": ("takes/media-generation-mv7v2-s05-v3a-pre-chorus-1-pc1-0-69783a26-930b-4f00-bac2-d97001a694b3.mp4", 0.5, 4.5),
    "mv7_s05_t3b": ("takes/media-generation-mv7v2-s05-v3b-pre-chorus-1-pc1-0-a936dfd3-e4bb-4fd0-a6c4-8565a72571e4.mp4", 0.5, 5.0),
    "mv7_s08_t2": ("takes/media-generation-mv7v2-s08-v2-chorus-1-c1-5-c1-0-485705b7-c49a-4e4e-a84e-6026abff5048.mp4", 0.5, 9.5),
    "mv7_s09_t2": ("takes/media-generation-mv7v2-s09-v2-chorus-1-c1-8-son-0-9eb3da14-e138-4ab0-9112-78f8178a9838.mp4", 0.5, 4.5),
    "mv7_s11_t1": ("takes/media-generation-mv7v2-s11-verse-2-v2-1-v2-3-so-0-862f031f-fd6d-4d6c-8837-ea591826b343.mp4", 0.5, 9.5),
}

def run(cmd, **kw):
    r = subprocess.run(cmd, capture_output=True, text=True, **kw)
    return r

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
    # 2fps contact sheet
    sheet = f"{BASE}/work/qc_v7/{tag}_sheet.png"
    run(["ffmpeg", "-v", "error", "-y", "-i", p, "-vf", "fps=2,scale=320:-1,tile=5x4", "-frames:v", "1", sheet])
    # RMS bins 0.5s
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
