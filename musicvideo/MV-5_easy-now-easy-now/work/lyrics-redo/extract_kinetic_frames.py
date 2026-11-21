#!/usr/bin/env python3
"""MV-5 LYRICS REDO — extract full-res frames at every line start for the
visual kinetic gate (legibility, edge cut-off, first-word mid-fade).

Extracts, for each line in grid_merged.json, the frame at the first word's
start (frame = round(t*24)) from the lyrics master, plus the frame at the
last word's start (mid-line check) for lines whose text is > 900px wide
(the width-cap risk set). Also builds contact sheets (16 frames per sheet)
for a fast first pass. Frames are extracted with SEPARATE -ss calls (ffmpeg
multi-input extraction returns frame 0 for all outputs — known trap).
Usage: python3 work/lyrics-redo/extract_kinetic_frames.py [master]
"""
import json, os, subprocess, sys
from PIL import Image, ImageDraw

PROJ = "/home/hatch/workspace/wubutv-network/musicvideo/MV-5_easy-now-easy-now"
MASTER = sys.argv[1] if len(sys.argv) > 1 else os.path.join(PROJ, "masters/mv5_easy_now_easy_now_16x9_lyrics.mp4")
GRID = os.path.join(PROJ, "work/lyrics-redo/grid_merged.json")
OUT = os.path.join(PROJ, "work/lyrics-redo/gate/kinetic_frames")
os.makedirs(OUT, exist_ok=True)
FPS = 24

grid = json.load(open(GRID))
lines, words = grid["lines"], grid["words"]
wi = 0
jobs = []  # (tag, frame_no, t)
for L in lines:
    n = len(L["text"].split())
    ws = words[wi:wi + n]; wi += n
    f0 = int(round(ws[0]["start"] * FPS))
    jobs.append((f"{L['id']}_start", f0, ws[0]["start"]))
    # mid-line check for wide lines (width from the .ass report)
    jobs.append((f"{L['id']}_last", int(round(ws[-1]["start"] * FPS)), ws[-1]["start"]))

print(f"{len(jobs)} frames to extract")
for tag, fno, t in jobs:
    out = os.path.join(OUT, f"{tag}.png")
    if os.path.exists(out):
        continue
    subprocess.run(["ffmpeg", "-v", "error", "-ss", str(fno / FPS), "-i", MASTER,
                    "-frames:v", "1", "-y", out], check=True)
print("extracted", len(os.listdir(OUT)), "frames")

# contact sheets, 4x4 frames each (320x180 thumbs + label)
files = sorted(os.listdir(OUT))
per = 16
for si in range(0, len(files), per):
    chunk = files[si:si + per]
    TW, TH, LH = 320, 180, 18
    sheet = Image.new("RGB", (4 * TW, 4 * (TH + LH)), "black")
    d = ImageDraw.Draw(sheet)
    for k, fn in enumerate(chunk):
        im = Image.open(os.path.join(OUT, fn)).resize((TW, TH))
        r, c = divmod(k, 4)
        sheet.paste(im, (c * TW, r * (TH + LH) + LH))
        d.text((c * TW + 4, r * (TH + LH) + 2), fn[:-4], fill="yellow")
    sheet.save(os.path.join(OUT, f"sheet_{si // per:02d}.png"))
print("sheets:", len(range(0, len(files), per)))
