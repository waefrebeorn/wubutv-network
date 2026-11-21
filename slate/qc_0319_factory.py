#!/usr/bin/env python3
"""Voice-timing QC for commercial factory 2026-10-19 0319 run (AD-310, AD-311 v1s)."""
import subprocess, struct
import numpy as np

T = "/home/hatch/workspace/wubutv-network/takes/2026-10-19"
TAKES = {
    "ad310": "media-generation-ad310-bossed-v2-0-442c8f00-5680-4466-b2f3-158ff59a6b73.mp4",
    "ad311": "media-generation-ad311-corbelled-v2-0-8deb2572-726b-408d-89e8-c1e2285d41f7.mp4",
}

def decode(path, sr=24000):
    p = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-ac", "1",
                        "-ar", str(sr), "-f", "s16le", "-"], capture_output=True)
    n = len(p.stdout) // 2
    return np.array(struct.unpack(f"<{n}h", p.stdout), dtype=np.float64) / 32768.0, sr

def harm_of(x, sr):
    ac = np.correlate(x, x, mode="full")[len(x)-1:]
    ac = ac / (ac[0] + 1e-12)
    lo, hi = int(sr / 400), int(sr / 60)
    return float(np.max(ac[lo:hi])) if hi < len(ac) else 0.0

for b, fn in TAKES.items():
    x, sr = decode(f"{T}/{fn}")
    print("=" * 20, b.upper(), "=" * 20)
    bin_n = int(sr * 0.25)
    for i in range(0, len(x) // bin_n):
        seg = x[i*bin_n:(i+1)*bin_n]
        peak = float(np.max(np.abs(seg)))
        db = 20*np.log10(peak + 1e-12)
        h = harm_of(seg, sr)
        t = i * 0.25
        flag = ""
        if db > -32 and h > 0.5:
            flag = "  <-- VOICE-GRADE"
        elif db > -12:
            flag = "  <-- loud bed"
        if flag or (7.0 <= t <= 9.5):
            print(f"{t:5.2f}s peak {db:7.2f} dB harm {h:.2f}{flag}")
