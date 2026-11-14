#!/usr/bin/env python3
"""Volley 5 QC driver: wav extract + transcribe + frame rule + 2fps sheet + RMS bins."""
import json, subprocess, sys, wave
import numpy as np

BASE = "/home/hatch/workspace/wubutv-network/musicvideo/MV-7_the-nobody-man"
TAKES = {
    "mv7_s12_t2": ("takes/media-generation-mv7v2-s12-v2-verse-2-v2-4-v2-6-0-1a61d504-11f7-48f5-a378-14e910f0385e.mp4", 0.5, 9.5),
    "mv7_s13_t2": ("takes/media-generation-mv7v2-s13-v2-pre-chorus-2-pc2-0-7a93e8d9-7fa0-4a1d-a53a-987a4f2f0227.mp4", 0.5, 9.5),
    "mv7_s15_t2": ("takes/media-generation-mv7v2-s15-v2-chorus-2-c2-1-c2-0-44875e3c-d6eb-4b26-8713-3466eebad9ff.mp4", 0.5, 9.5),
    "mv7_s17_t1": ("takes/media-generation-mv7v2-s17-chorus-2-c2-7-c2-8-s-0-70773246-8933-4a21-a3b9-75bd80853392.mp4", 0.5, 9.5),
    # S18/S19 are bridge montage vehicles (no singing window): frame rule over the whole clip.
    "mv7_s18_t1": ("takes/media-generation-mv7v2-s18-bridge-montage-b1-b4-0-d8514bfa-9877-4564-9b2b-46582a9e311e.mp4", 0.0, 10.0),
    "mv7_s19_t1": ("takes/media-generation-mv7v2-s19-bridge-montage-b5-b6-0-65c522dd-c352-4d26-bf5e-16784d68469f.mp4", 0.0, 10.0),
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
