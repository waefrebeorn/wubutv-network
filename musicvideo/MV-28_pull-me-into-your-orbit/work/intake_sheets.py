#!/usr/bin/env python3
"""Intake sheets: contact sheets of lyric-band frames at ASR-segment times
(+2s grid fill), 6 frames per sheet (2x3), each cell labeled with its time.
Usage: intake_sheets.py PROJ
Writes work/sheets/sheet_NN.png and work/sheets/times.json.
"""
import json, os, subprocess, sys

from PIL import Image, ImageDraw

PROJ = sys.argv[1]
WORK = os.path.join(PROJ, "work")
OUT = os.path.join(WORK, "sheets")
os.makedirs(OUT, exist_ok=True)
MP4 = os.path.join(PROJ, "track.mp4")

with open(os.path.join(PROJ, "asr_words.json")) as f:
    asr = json.load(f)
dur = asr["duration"]
times = set()
for s in asr["segments"]:
    times.add(round((s["start"] + s["end"]) / 2, 2))
    if s["end"] - s["start"] > 10:  # long merged segment: sample inside it
        t = s["start"] + 3.0
        while t < s["end"] - 1.5:
            times.add(round(t, 2))
            t += 4.0
times = sorted(x for x in times if 0 <= x < dur)

tmp = os.path.join(OUT, "cells")
os.makedirs(tmp, exist_ok=True)
cells = []
for i, tt in enumerate(times):
    cell = os.path.join(tmp, f"c{i:03d}.png")
    if not os.path.exists(cell):
        subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-ss",
                        f"{tt}", "-i", MP4, "-frames:v", "1",
                        "-vf", "crop=824:335:0:745", cell],
                       stdin=subprocess.DEVNULL, check=True)
    img = Image.open(cell).convert("RGB")
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 110, 26], fill="black")
    d.text((6, 6), f"t={tt:.1f}s", fill="yellow")
    cells.append((tt, img))

per = 6
sheets = []
for s in range(0, len(cells), per):
    group = cells[s:s + per]
    W, H = 824 * 2, 335 * 3
    sheet = Image.new("RGB", (W, H), "black")
    for k, (tt, img) in enumerate(group):
        sheet.paste(img, ((k % 2) * 824, (k // 2) * 335))
    name = f"sheet_{s // per:02d}.png"
    sheet.save(os.path.join(OUT, name))
    sheets.append(name)
with open(os.path.join(OUT, "times.json"), "w") as f:
    json.dump({"times": times, "sheets": sheets}, f, indent=1)
print(f"SHEETS {PROJ}: {len(times)} cells, {len(sheets)} sheets", flush=True)
