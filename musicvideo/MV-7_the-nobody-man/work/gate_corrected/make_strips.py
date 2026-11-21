#!/usr/bin/env python3
"""Visual probe strips v2: frames F-4..F+11 (16) per onset, face-crop per
framing class, 4x4 grid of 300px thumbs with signed frame-offset labels.
Crop classes by scene: close (Era A/C), wide (Era B desk shots), med.
Usage: make_strips.py [label ...]
"""
import json, os, sys
from PIL import Image, ImageDraw, ImageFont

PROJ = os.path.expanduser("~/workspace/wubutv-network/musicvideo/MV-7_the-nobody-man")
FR = os.path.join(PROJ, "work/gate_corrected/frames")
OUT = os.path.join(PROJ, "work/gate_corrected/strips")
os.makedirs(OUT, exist_ok=True)

# label -> (cx, cy, half) crop at 1280x720
CLOSE = (610, 270, 240)
MED = (630, 240, 220)
WIDE = (650, 195, 175)
CROP = {}
for lab in ["V2.1", "V2.2", "V2.3", "V2.4", "V2.5", "V2.6"]:
    CROP[lab] = WIDE
for lab in ["PC2.1", "PC2.2", "C2.1", "C2.2", "C2.3", "C2.5", "C2.6", "C2.7", "C2.8"]:
    CROP[lab] = MED

onsets = json.load(open(os.path.join(PROJ, "work/gate_final/onsets.json")))
scored = [o for o in onsets if o["kind"] == "sing"]
try:
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
except Exception:
    font = ImageFont.load_default()

want = sys.argv[1:]
for o in scored:
    if want and o["label"] not in want:
        continue
    d = os.path.join(FR, o["label"])
    meta = json.load(open(os.path.join(d, "meta.json")))
    start_f, F = meta["start_frame"], meta["onset_frame"]
    cx, cy, half = CROP.get(o["label"], CLOSE)
    x0 = min(max(cx - half, 0), 1280 - 2 * half)
    y0 = min(max(cy - half, 0), 720 - 2 * half)
    CW, LAB, cols = 300, 32, 4
    rows = 4
    sheet = Image.new("RGB", (cols * CW, rows * (CW + LAB)), "black")
    dr = ImageDraw.Draw(sheet)
    for k in range(16):
        af = F - 4 + k
        wi = af - start_f
        path = os.path.join(d, f"w{wi:02d}.png")
        if not os.path.exists(path):
            continue
        im = Image.open(path).crop((x0, y0, x0 + 2 * half, y0 + 2 * half)).resize((CW, CW))
        col, row = k % cols, k // cols
        x, y = col * CW, row * (CW + LAB)
        sheet.paste(im, (x, y))
        off = af - F
        tag = f"{off:+d}f ({off/24:+.2f}s)"
        colr = "yellow" if off == 0 else ("#7CFC00" if off > 0 else "white")
        dr.text((x + 4, y + CW + 4), tag, fill=colr, font=font)
    p = os.path.join(OUT, f"strip_{o['label']}.png")
    sheet.save(p)
    print("wrote", p)
