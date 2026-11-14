#!/usr/bin/env python3
"""Extended strips: frames +8f..+35f (28) per onset, same crops as make_strips."""
import json, os, sys
from PIL import Image, ImageDraw, ImageFont

PROJ = os.path.expanduser("~/workspace/wubutv-network/musicvideo/MV-7_the-nobody-man")
FR = os.path.join(PROJ, "work/correction/frames_ext")
OUT = os.path.join(PROJ, "work/correction/strips")
CLOSE = (610, 270, 240)
MED = (630, 240, 220)
WIDE = (650, 195, 175)
CROP = {}
for lab in ["V2.1", "V2.2", "V2.3", "V2.4", "V2.5", "V2.6"]:
    CROP[lab] = WIDE
for lab in ["PC2.1", "PC2.2", "C2.1", "C2.2", "C2.3", "C2.5", "C2.6", "C2.7", "C2.8"]:
    CROP[lab] = MED

try:
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
except Exception:
    font = ImageFont.load_default()

for lab in sys.argv[1:]:
    d = os.path.join(FR, lab)
    meta = json.load(open(os.path.join(d, "meta.json")))
    start_f, F = meta["start_frame"], meta["onset_frame"]
    cx, cy, half = CROP.get(lab, CLOSE)
    x0 = min(max(cx - half, 0), 1280 - 2 * half)
    y0 = min(max(cy - half, 0), 720 - 2 * half)
    CW, LAB, cols, rows = 300, 32, 4, 7
    sheet = Image.new("RGB", (cols * CW, rows * (CW + LAB)), "black")
    dr = ImageDraw.Draw(sheet)
    for k in range(28):
        af = start_f + k
        path = os.path.join(d, f"w{k+1:02d}.png")
        if not os.path.exists(path):
            continue
        im = Image.open(path).crop((x0, y0, x0 + 2 * half, y0 + 2 * half)).resize((CW, CW))
        col, row = k % cols, k // cols
        x, y = col * CW, row * (CW + LAB)
        sheet.paste(im, (x, y))
        off = af - F
        dr.text((x + 4, y + CW + 4), f"{off:+d}f ({off/24:+.2f}s)", fill="#7CFC00", font=font)
    p = os.path.join(OUT, f"stripext_{lab}.png")
    sheet.save(p)
    print("wrote", p)
