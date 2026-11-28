"""Extract frames BY FRAME NUMBER from the encoded MP4 (never by -ss seek: a fast
seek snaps to a keyframe and fakes caption bugs), measure the take, tile a clean
full-frame sheet, and save one captioned mid-frame for a visual read.

Usage: mp4_frames.py MP4 OUTDIR
"""
import os, subprocess, sys
import numpy as np
from PIL import Image

MP4, OUT = sys.argv[1:3]
os.makedirs(OUT, exist_ok=True)
PICK = ([int(x) for x in sys.argv[3].split(",")] if len(sys.argv) > 3
        else [0, 60, 150, 240, 291, 305, 308, 320, 340])
sel = "+".join("eq(n\\,%d)" % f for f in PICK)
subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", MP4, "-vf",
                "select='%s'" % sel, "-fps_mode", "passthrough",
                os.path.join(OUT, "pick_%02d.png")], check=True)
got = sorted(f for f in os.listdir(OUT) if f.startswith("pick_"))
print("extracted", len(got), got)

res = []
for k, f in enumerate(got):
    im = Image.open(os.path.join(OUT, f)).convert("RGB")
    a = np.asarray(im, dtype=np.int16)
    dark = a.max(axis=2) < 80
    sub = dark[175:250, 150:390]
    rows = np.where(sub.sum(axis=1) >= 20)[0]
    brow = (int(rows.min()) + 175, int(rows.max()) + 175) if len(rows) else None
    white = (a[:, :, 0] > 195) & (a[:, :, 1] > 195) & (a[:, :, 2] > 195)
    wp = int(white[225:275, 195:345].sum())
    lip = (a[:, :, 0] - a[:, :, 2] > 40) & (a[:, :, 1] < 80)
    mr = np.where(lip[265:380, 150:390].any(axis=1))[0]
    mh = (int(mr.max()) - int(mr.min()) + 1) if len(mr) else 0
    res.append((PICK[k], brow, wp, mh))
    print("frame %3d  brow %-11s eye_white %5d  mouth_h %2d" % (PICK[k], str(brow), wp, mh))

# clean full-frame sheet: no labels, no crop marks
tiles = [Image.open(os.path.join(OUT, f)).convert("RGB").resize((270, 480), Image.LANCZOS)
         for f in got]
sheet = Image.new("RGB", (270 * 5, 480 * 2), (8, 8, 12))
for k, t in enumerate(tiles):
    sheet.paste(t, ((k % 5) * 270, (k // 5) * 480))
sheet.save(os.path.join(OUT, "sheet_full.jpg"), quality=92)
print("sheet", os.path.join(OUT, "sheet_full.jpg"))

# one captioned mid-frame at full size for the caption read
mid = Image.open(os.path.join(OUT, "pick_03.png")).convert("RGB")
mid.save(os.path.join(OUT, "mid_full.jpg"), quality=95)
print("mid", os.path.join(OUT, "mid_full.jpg"))
