#!/usr/bin/env python3
"""Build labeled mouth-audit sheets from extracted master frames.

Usage: build_sheets.py <frames_dir> <onsets.json> <out_prefix>
Each sheet: up to 8 onset rows; row = label | frame@onset | frame@onset+4f.
Face crop: 640x480 box centered on (crops[scene]+202, 250), clamped.
Crops are shown at 300x225. A header row labels the two columns.
"""
import json, os, sys
from PIL import Image, ImageDraw

PROJ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CROPS = json.load(open(os.path.join(PROJ, "crops.json")))

def crop_face(img, scene):
    cx = CROPS.get(scene, 428) + 202
    cy = 250
    w, h = 640, 480
    x0 = max(0, min(1280 - w, cx - w // 2))
    y0 = max(0, min(720 - h, cy - h // 2))
    return img.crop((x0, y0, x0 + w, y0 + h))

def main():
    frames_dir, onsets_path, out_prefix = sys.argv[1], sys.argv[2], sys.argv[3]
    onsets = json.load(open(onsets_path))
    CW, CH, LW, HDR = 300, 225, 170, 34
    per = 8
    sheets = []
    for si in range(0, len(onsets), per):
        batch = onsets[si:si + per]
        W = LW + CW * 2 + 12
        H = HDR + len(batch) * (CH + 4)
        sheet = Image.new("RGB", (W, H), (24, 24, 24))
        d = ImageDraw.Draw(sheet)
        d.text((LW + 80, 10), "@ ONSET", fill=(255, 255, 120))
        d.text((LW + CW + 60, 10), "@ ONSET +0.17s", fill=(255, 255, 120))
        for ri, o in enumerate(batch):
            y = HDR + ri * (CH + 4)
            n0 = int(o["t"] * 24)
            label = f"{o['t']:.2f} {o['label']}\n{o['scene']}\n{','.join(k.split(':')[0] for k in o['kinds'])}"
            for li, line in enumerate(label.split("\n")):
                d.text((8, y + 30 + li * 26), line, fill=(255, 255, 255))
            for ci, n in enumerate((n0, n0 + 4)):
                p = os.path.join(frames_dir, f"f_{n:05d}.png")
                if os.path.exists(p):
                    im = Image.open(p)
                    im = crop_face(im, o["scene"]).resize((CW, CH))
                    sheet.paste(im, (LW + ci * (CW + 6), y))
                else:
                    d.text((LW + ci * (CW + 6) + 60, y + 100), "MISSING", fill=(255, 80, 80))
        out = f"{out_prefix}_{si // per + 1:02d}.jpg"
        sheet.save(out, quality=90)
        sheets.append(out)
        print("wrote", out, "onsets", [f"{o['t']:.2f}" for o in batch])
    print(f"{len(sheets)} sheets")

if __name__ == "__main__":
    main()
