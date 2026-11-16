#!/usr/bin/env python3
"""MV-4 lyrics-redo regression diagnosis: is the video at the failing times
genuinely different, or is the gate comparing the wrong frames?

For each suspect time, extract a 13-frame window (t-0.25s .. t+0.25s) from
BOTH masters (input seeking = fast) and compare NEW's center frame against
BASE's center +-2 frames, on the TOP HALF only (excludes caption pixels)
and on the FULL frame. If the best match is at offset 0 -> encoder noise
(gate bar too strict for a re-encode). If best at +-1/+-2 -> frame offset
(assembly/encode timing fault). If nothing matches -> genuine content change.
"""
import subprocess

import numpy as np

PROJ = "/home/hatch/workspace/wubutv-network/musicvideo/MV-4_this-time-its-real"
NEW = f"{PROJ}/masters/mv4_this_time_its_real_16x9_lyrics.mp4"
BASE = f"{PROJ}/masters/mv4_this_time_its_real_16x9.mp4"
W, H = 640, 360
TIMES = (100.00, 63.59, 225.91, 31.61, 156.89, 20.00, 200.00)


def window(path, t):
    """13 consecutive gray frames centred on t (frame round(t*24))."""
    start = t - 0.25
    r = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{start:.3f}", "-i", path,
                        "-frames:v", "13", "-f", "rawvideo", "-pix_fmt", "gray",
                        "-s", f"{W}x{H}", "-"], capture_output=True, check=True)
    n = len(r.stdout) // (W * H)
    return [np.frombuffer(r.stdout[i * W * H:(i + 1) * W * H],
                          dtype=np.uint8).astype(np.float32)
            for i in range(n)]


def md(a, b):
    return float(np.mean(np.abs(a - b)))


for t in TIMES:
    nw = window(NEW, t)
    bw = window(BASE, t)
    if len(nw) != 13 or len(bw) != 13:
        print(f"t={t}: window sizes new={len(nw)} base={len(bw)} — SHORT, skipping")
        continue
    c = 6  # center frame index
    print(f"t={t:7.2f}s (center frame {round(t*24)}):")
    for dn in (-2, -1, 0, 1, 2):
        top = md(nw[c][:H // 2], bw[c + dn][:H // 2])
        full = md(nw[c], bw[c + dn])
        print(f"  NEW[c] vs BASE[c{dn:+d}]: top-half={top:6.3f}  full={full:6.3f}")
