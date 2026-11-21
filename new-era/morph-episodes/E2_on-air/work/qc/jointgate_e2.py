#!/usr/bin/env python3
"""JOINT GATE for ON AIR E1 on work/joined.mp4: seam MAE at each cut
(320x180 gray), plus joint strips (cut -6..+6 frames) for the eye record.
Bands (carried from THE MACHINE E2 gate): PASS <=58, CONDITIONAL <=75, FAIL >75."""
import subprocess, os
import numpy as np
from PIL import Image

BASE = "/home/hatch/workspace/wubutv-network/new-era/morph-episodes/E2_on-air"
JOINED = os.path.join(BASE, "work/joined.mp4")
OUT = os.path.join(BASE, "work/qc/joints")
os.makedirs(OUT, exist_ok=True)
CUTS = [240, 480, 720, 960, 1200]
NAMES = ["U1-U2", "U2-U3", "U3-U4", "U4-U5", "U5-U6"]

sel = "gte(n\\,233)*lte(n\\,1213)"
subprocess.run(["ffmpeg", "-v", "error", "-i", JOINED, "-vf",
                f"select='{sel}',scale=320:180,format=gray",
                "-vsync", "0", os.path.join(OUT, "g%04d.png")], check=True)
subprocess.run(["ffmpeg", "-v", "error", "-i", JOINED, "-vf",
                f"select='{sel}',scale=640:360",
                "-vsync", "0", os.path.join(OUT, "c%04d.png")], check=True)

gfiles = sorted(f for f in os.listdir(OUT) if f.startswith("g"))
cfiles = sorted(f for f in os.listdir(OUT) if f.startswith("c"))
gray = {233 + i: np.asarray(Image.open(os.path.join(OUT, f)), dtype=np.float32)
        for i, f in enumerate(gfiles)}
color = {233 + i: Image.open(os.path.join(OUT, f)) for i, f in enumerate(cfiles)}

def mae(a, b):
    return float(np.mean(np.abs(a - b)))

for cut, name in zip(CUTS, NAMES):
    v = mae(gray[cut - 1], gray[cut])
    band = "PASS" if v <= 58 else ("CONDITIONAL" if v <= 75 else "FAIL")
    hm = mae(gray[cut], gray[cut + 12])
    print(f"JOINT {name} @f{cut}: seam MAE {v:.1f} -> {band} | downstream head motion f0->f12 {hm:.1f}")
    tiles = [color[cut - 6 + i].resize((320, 180)) for i in range(12)]
    strip = Image.new("RGB", (320 * 4, 180 * 3))
    for i, t in enumerate(tiles):
        strip.paste(t, ((i % 4) * 320, (i // 4) * 180))
    strip.save(os.path.join(OUT, f"strip_{name}.png"))
print("strips saved to", OUT)
