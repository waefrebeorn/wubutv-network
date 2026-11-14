#!/usr/bin/env python3
"""QC for the 21:00 EDT bumper-factory run: B-1071, B-1072, B-1073 v1 takes."""
import subprocess, os, sys, json, math
import numpy as np
from PIL import Image

D = "/home/hatch/workspace/wubutv-network/takes/2026-10-16"
TAKES = {
    "b1071": "media-generation-b1071-the-oil-stain-v1-0-5c5269cf-492e-4e78-ad2b-d98cf3cc2984.mp4",
    "b1072": "media-generation-b1072-the-pigeon-spike-v1-0-14589c2c-d046-481c-8995-9f81de45f331.mp4",
    "b1073": "media-generation-b1073-the-floor-hatch-v1-0-0be638a5-eeff-41ea-a4ff-c03a0b0eda61.mp4",
}

def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)

for k, f in TAKES.items():
    p = os.path.join(D, f)
    print("=" * 60); print(k, f); print("=" * 60)
    # decode errors
    r = run(["ffmpeg", "-v", "error", "-xerror", "-i", p, "-f", "null", "-"])
    errs = r.stderr.strip()
    print("decode-errors:", "NONE" if not errs else errs[:300])
    # frames
    for t in ["0.5", "4", "5", "6", "7.5", "8", "8.5", "9.5"]:
        out = os.path.join(D, f"{k}v1_{t.replace('.','_')}.png")
        run(["ffmpeg", "-v", "error", "-y", "-ss", t, "-i", p, "-frames:v", "1", out])
    # wordmark crop (chest center-ish) at 8s and 9.5s; bug crop bottom-right at 9.5s
    for t in ["8", "9.5"]:
        src = os.path.join(D, f"{k}v1_{t.replace('.','_')}.png")
        im = Image.open(src)
        wm = im.crop((440, 330, 840, 500))  # chest band
        wm = wm.resize((wm.width * 2, wm.height * 2), Image.LANCZOS)
        wm.save(os.path.join(D, f"{k}v1_{t.replace('.','_')}_wordmark.png"))
    bug = Image.open(os.path.join(D, f"{k}v1_9_5.png")).crop((920, 620, 1280, 720))
    bug = bug.resize((bug.width * 2, bug.height * 2), Image.LANCZOS)
    bug.save(os.path.join(D, f"{k}v1_bug.png"))
    # camera frozen: 0.5 vs 9.5 diff
    a = np.asarray(Image.open(os.path.join(D, f"{k}v1_0_5.png")).convert("L"), dtype=np.float32)
    b = np.asarray(Image.open(os.path.join(D, f"{k}v1_9_5.png")).convert("L"), dtype=np.float32)
    d = np.abs(a - b)
    print(f"cam-diff 0.5-vs-9.5: mean {d.mean():.2f} top-strip {d[:100].mean():.2f}")
    # loudness
    r = run(["ffmpeg", "-v", "info", "-i", p, "-map", "0:a", "-filter:a", "ebur128=peak=true", "-f", "null", "-"])
    tail = r.stderr.splitlines()
    summary = [l for l in tail if "I:" in l and "LUFS" in l]
    peak = [l for l in tail if "Peak:" in l]
    print("loudness:", (summary[-1].strip() if summary else "?"))
    print("truepeak:", (peak[-1].strip() if peak else "?"))
    # per-0.25s bins
    wav = os.path.join(D, f"{k}v1.wav")
    run(["ffmpeg", "-v", "error", "-y", "-i", p, "-map", "0:a", "-ac", "1", "-ar", "48000", wav])
    import wave
    w = wave.open(wav)
    n = w.getnframes(); fr = w.getframerate(); sw = w.getsampwidth()
    raw = w.readframes(n); w.close()
    arr = np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0
    bins = []
    for i in range(40):
        s = arr[int(i * 0.25 * fr):int((i + 0.25) * fr)]
        if len(s) == 0: bins.append(-99); continue
        rms = np.sqrt(np.mean(s ** 2))
        bins.append(round(20 * math.log10(rms + 1e-9), 1))
    print("bins-0.25s(dBFS RMS):")
    for i in range(0, 40, 10):
        print("  ", " ".join(f"{i+j}:{bins[i+j]}" for j in range(10)))
