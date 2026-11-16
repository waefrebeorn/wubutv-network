#!/usr/bin/env python3
"""Extract onset frames from the master and tile labelled contact sheets.
Per scored onset: frame at onset + frame +6 (0.25s). Sheets: 4 cols x 4 rows
of onset-pairs (8 onsets/sheet), 640x360 -> 320x180 thumbs with labels.
"""
import json, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont
MASTER = sys.argv[1]
OUT = 'work/gate_final'
os.makedirs('/tmp/mv7f', exist_ok=True)
print('decoding master to frames...', flush=True)
subprocess.run(['ffmpeg','-v','error','-y','-i',MASTER,'-vf','scale=640:360',
                '-q:v','4','/tmp/mv7f/f%05d.jpg'], check=True)
onsets = json.load(open(f'{OUT}/onsets.json'))
scored = [o for o in onsets if o['kind'] == 'sing']
try:
    font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 20)
    small = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 16)
except Exception:
    font = ImageFont.load_default(); small = font
TW, TH, LAB = 320, 180, 26
COLS, ROWS = 4, 4  # 8 onsets per sheet (2 frames each)
per_sheet = COLS*ROWS//2
for si in range(0, len(scored), per_sheet):
    chunk = scored[si:si+per_sheet]
    sheet = Image.new('RGB', (COLS*TW, ROWS*(TH+LAB)), 'black')
    d = ImageDraw.Draw(sheet)
    for k, o in enumerate(chunk):
        row, col = divmod(k, COLS//2)
        for j, fr in enumerate([o['frame'], o['frame_plus6']]):
            x = (col*2+j)*TW; y = row*(TH+LAB)
            im = Image.open(f'/tmp/mv7f/f{fr+1:05d}.jpg').resize((TW, TH))
            sheet.paste(im, (x, y))
            tag = 'onset' if j == 0 else '+0.25s'
            d.text((x+4, y+TH+3), f"{o['label']} {o['onset']:.2f}s {tag}",
                   fill='yellow' if o['hook'] else 'white', font=small)
    p = f'{OUT}/sheet_{si//per_sheet+1:02d}.png'
    sheet.save(p)
    print('wrote', p)
print('sheets done:', (len(scored)+per_sheet-1)//per_sheet)
