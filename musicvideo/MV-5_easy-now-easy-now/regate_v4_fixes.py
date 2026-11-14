#!/usr/bin/env python3
"""Targeted re-gate: mouth frames at the onsets changed by the gate fixes,
plus L110a (missing from the main validator's line map)."""
import os, subprocess
from PIL import Image, ImageDraw

PROJ = os.path.dirname(os.path.abspath(__file__))
MASTER = os.path.join(PROJ, "masters", "mv5_easy_now_easy_now_16x9_v4.mp4")
OUT = os.path.join(PROJ, "work", "gate_v4", "regate")
os.makedirs(OUT, exist_ok=True)

ONSETS = [  # (label, onset seconds on the app grid)
    ("I07", 15.40), ("L02", 24.48), ("L03", 26.78),
    ("L21", 62.90), ("L22", 63.90), ("L23", 65.10), ("L24", 66.10),
    ("L69", 135.90), ("L70", 137.00), ("L110a", 201.00),
]

def grab(t):
    f = int(round(t * 24))
    p = os.path.join(OUT, f"f{f}.png")
    if not os.path.exists(p):
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", MASTER,
                        "-vf", f"select='eq(n\\,{f})'", "-vsync", "0", p],
                       check=True)
    return p

tiles = []
for label, onset in ONSETS:
    row = []
    for dt, tag in ((0.0, "ONSET"), (0.15, "+0.15")):
        src = grab(onset + dt)
        im = Image.open(src).convert("RGB").resize((480, 270))
        d = ImageDraw.Draw(im)
        d.rectangle([0, 0, 480, 20], fill=(0, 0, 0))
        d.text((6, 5), f"{label} @{onset:.2f} {tag}", fill=(255, 255, 0))
        row.append(im)
    tiles.append(row)

cols, rows = 2, len(tiles)
sheet = Image.new("RGB", (cols * 480, rows * 270), (24, 24, 24))
for r, row in enumerate(tiles):
    for c, im in enumerate(row):
        sheet.paste(im, (c * 480, r * 270))
out = os.path.join(PROJ, "work", "gate_v4", "regate_fixes.png")
sheet.save(out)
print("sheet:", out)
