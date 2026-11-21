#!/usr/bin/env python3
"""Detect lyric-text change points in the Suno video by hashing the
lyric region of 1s frames. Prints time + hamming distance to previous
frame; spikes = line transitions."""
import subprocess
import sys
from pathlib import Path

from PIL import Image

PROJ = Path("/home/hatch/workspace/wubutv-network/musicvideo/MV-4_this-time-its-real")
FRAMES = PROJ / "work" / "lyric1s"
FRAMES.mkdir(parents=True, exist_ok=True)

# ranges: verse1+chorus1, and final chorus + outro
ranges = [(10, 64), (155, 238)]
for a, b in ranges:
    for t in range(a, b + 1):
        out = FRAMES / f"t{t:03d}.png"
        if not out.exists():
            subprocess.run(
                ["ffmpeg", "-y", "-v", "error", "-ss", str(t), "-i",
                 str(PROJ / "track.mp4"), "-frames:v", "1", str(out)],
                check=True,
            )


def ahash(img):
    g = img.convert("L").resize((32, 32))
    px = list(g.getdata())
    avg = sum(px) / len(px)
    bits = 0
    for p in px:
        bits = (bits << 1) | (1 if p > avg else 0)
    return bits


def ham(a, b):
    return bin(a ^ b).count("1")


prev = None
prev_t = None
for t in sorted(int(p.stem[1:]) for p in FRAMES.glob("t*.png")):
    img = Image.open(FRAMES / f"t{t:03d}.png")
    # lyric text region: y 820-1180 of 1464
    crop = img.crop((60, 820, 764, 1180))
    h = ahash(crop)
    d = ham(h, prev) if prev is not None else 0
    flag = "  <-- CHANGE" if d >= 12 else ""
    print(f"{t:3d}s ham={d:3d}{flag}")
    prev = h
    prev_t = t
