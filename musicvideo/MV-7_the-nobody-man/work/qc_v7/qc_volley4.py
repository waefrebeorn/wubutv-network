#!/usr/bin/env python3
"""Volley 4 QC driver: wav extract + transcribe + frame rule + 2fps sheet + RMS bins."""
import json, subprocess, sys, wave
import numpy as np

BASE = "/home/hatch/workspace/wubutv-network/musicvideo/MV-7_the-nobody-man"
TAKES = {
    "mv7_s05_t4": ("takes/media-generation-mv7v2-s05-v4-pre-chorus-1-pc1-0-e4acbb70-b259-4c87-ab3f-54a3a31f8a64.mp4", 0.5, 3.5),
    "mv7_s12_t1": ("takes/media-generation-mv7v2-s12-verse-2-v2-4-v2-6-so-0-3e5963f7-1461-459e-b0cd-3f2063aff438.mp4", 0.5, 9.5),
    "mv7_s13_t1": ("takes/media-generation-mv7v2-s13-pre-chorus-2-pc2-1-p-0-24146eaf-2c18-4e59-a8a6-f7c524112cc5.mp4", 0.5, 9.5),
    "mv7_s14_t1": ("takes/media-generation-mv7v2-s14-pre-chorus-2-pc2-3-p-0-7b5a8b0a-affc-4a1f-97ea-91f9b5a5a630.mp4", 0.5, 9.5),
    "mv7_s15_t1": ("takes/media-generation-mv7v2-s15-chorus-2-c2-1-c2-4-s-0-ba6ce068-9c0e-43ac-95aa-f5e7bf4f15a7.mp4", 0.5, 9.5),
    "mv7_s16_t1": ("takes/media-generation-mv7v2-s16-chorus-2-c2-5-c2-6-s-0-2c3694f8-072a-4efa-9288-76d7e4a9494c.mp4", 0.5, 9.5),
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
