#!/usr/bin/env python3
"""Re-read TRUE first frames for onsets where round(t*24) missed by 1 frame.
Reads true first frame + true+6 from the already-decoded /tmp/mv7f frames.
"""
import json
from PIL import Image, ImageDraw, ImageFont
# (label, onset, true_first_frame) for the -1 cases + FC.5
FIX = [
    ("V1.3", 24.62, 590), ("V1.4", 26.82, 643), ("V1.5", 29.42, 705),
    ("V1.6", 31.74, 761), ("PC1.4", 42.90, 1029), ("C1.2", 49.40, 1185),
    ("C1.4", 53.82, 1291), ("C1.T2", 70.48, 1691), ("C1.T3", 73.16, 1755),
    ("V2.1", 75.84, 1819), ("V2.2", 78.50, 1883), ("V2.3", 80.58, 1933),
    ("V2.4", 82.94, 1990), ("FC.5", 152.88, 3670),
]
try:
    small = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 16)
except Exception:
    small = ImageFont.load_default()
TW, TH, LAB = 320, 180, 26
COLS, ROWS = 4, 4
per_sheet = COLS*ROWS//2
for si in range(0, len(FIX), per_sheet):
    chunk = FIX[si:si+per_sheet]
    sheet = Image.new('RGB', (COLS*TW, ROWS*(TH+LAB)), 'black')
    d = ImageDraw.Draw(sheet)
    for k, (label, t, fr) in enumerate(chunk):
        row, col = divmod(k, COLS//2)
        for j, f in enumerate([fr, fr+6]):
            x = (col*2+j)*TW; y = row*(TH+LAB)
            im = Image.open(f'/tmp/mv7f/f{f+1:05d}.jpg').resize((TW, TH))
            sheet.paste(im, (x, y))
            tag = 'TRUE onset' if j == 0 else '+0.25s'
            d.text((x+4, y+TH+3), f"{label} {t:.2f}s {tag} f{f}",
                   fill='cyan', font=small)
    p = f'work/gate_final/corr_{si//per_sheet+1:02d}.png'
    sheet.save(p); print('wrote', p)
