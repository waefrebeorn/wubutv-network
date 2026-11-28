"""Pre-render face QC for the clean rig: render 6 frames at chosen mouth states,
tile a face-zoom sheet, and MEASURE brows/pupils/mouth/arms on raw pixels.

Usage: face_qc.py SESSION.json OUTDIR SHEET.jpg
"""
import json, os, subprocess, sys
import numpy as np
from PIL import Image

SJ, OUTDIR, SHEET = sys.argv[1:4]
S = json.load(open(SJ))
mouth = S["mouth"]
N = len(mouth)
fps = S["fps"]

# pick frames whose mouth value is closest to each target, spread across the clip
targets = [0.0, 0.22, 0.42, 0.62, 0.82, 1.0]
picks = []
used = set()
for t in targets:
    best, bi = 1e9, None
    for i in range(0, N, 2):
        if i in used:
            continue
        d = abs(mouth[i] - t)
        # prefer later frames on ties so the 6 picks spread across the timeline
        if d < best - 1e-9 or (abs(d - best) < 1e-9 and bi is not None and i > bi):
            best, bi = d, i
    used.add(bi)
    picks.append(bi)
picks.sort()
vals = [round(mouth[i], 3) for i in picks]
print("QC picks", picks, "mouth", vals, flush=True)

qs = dict(S)
qs["nframes"] = len(picks)
qs["mouth"] = [mouth[i] for i in picks]
# The hardware gate judges the FACE, so the authored acting windows (total hold,
# brow drop) must be stripped: a suppressed blink or a dropped brow in a QC frame
# would score the pose, not the rig. Acting is verified separately by beat_qc.py.
qs.pop("still", None)
qs.pop("brow_drop", None)
# Same for the take and the word-gap accents: they are frame-indexed acting, and a
# 6-frame QC render renumbers the clip, so a dip/closed-eye frame could land on a
# hardware pick and score "no pupils" for a rig that is fine.
qs.pop("take", None)
qs.pop("accents", None)
qpath = os.path.join(os.path.dirname(SJ), "session_qc.json")
json.dump(qs, open(qpath, "w"))
os.makedirs(OUTDIR, exist_ok=True)
env = os.environ.copy()
env["BRAIN_ENV"] = qpath
env["BRAIN_OUT"] = OUTDIR
env["LD_LIBRARY_PATH"] = "/opt/data/shitpost-box/syslibs/usr/lib/x86_64-linux-gnu:" + env.get("LD_LIBRARY_PATH", "")
r = subprocess.run(["/opt/data/shitpost-box/blender/blender", "-b", "--python",
                    os.path.join(os.path.dirname(os.path.abspath(__file__)), "clean_render.py")],
                   env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
if "CLEAN_RENDER_OK" not in r.stdout:
    print("RENDER FAILED")
    print("\n".join(r.stdout.splitlines()[-20:]))
    sys.exit(1)

# ---- face zoom tiles ----
BOX = (100, 110, 440, 430)  # head + face, measured from ortho 5.68 @ 540x960 (camera z 0.05)
tiles = []
for k in range(len(picks)):
    p = os.path.join(OUTDIR, "frame_%05d.jpg" % k)
    im = Image.open(p).convert("RGB")
    crop = im.crop(BOX).resize((480, 468), Image.LANCZOS)
    tiles.append(crop)
sheet = Image.new("RGB", (480 * 3, 468 * 2), (12, 12, 16))
for k, t in enumerate(tiles):
    sheet.paste(t, ((k % 3) * 480, (k // 3) * 468))
sheet.save(SHEET, quality=92)
print("SHEET", SHEET)

# ---- measurements on the widest-open frame and the closed frame ----
# Bands are measured, not assumed: the old fixed bands (brows 240-290, eyes
# 290-345, mouth 350-440) were written for the ortho-5.0 framing and silently
# found nothing on the ortho-5.68 rig — the gate printed "pupils None / mouth 0x0"
# and passed. Locate the features by COLOUR instead, then read their rows.
FACE = (120, 150, 420, 470)

def masks(im):
    a = np.asarray(im.convert("RGB"), dtype=np.int16)
    dark = a.max(axis=2) < 80                      # brow bar + pupil (near-black)
    lip = (a[:, :, 0] - a[:, :, 2] > 40) & (a[:, :, 1] < 80)  # dark red mouth
    return dark, lip

def rows_of(mask, x0, x1, y0, y1, minpx=4, maxgap=2):
    sub = mask[y0:y1, x0:x1]
    cnt = sub.sum(axis=1)
    ys = [y for y in range(len(cnt)) if cnt[y] >= minpx]
    if not ys:
        return []
    groups, cur = [], [ys[0]]
    for y in ys[1:]:
        if y - cur[-1] <= maxgap:
            cur.append(y)
        else:
            groups.append(cur); cur = [y]
    groups.append(cur)
    return [(g[0] + y0, g[-1] + y0) for g in groups]

def extent(mask, x0, x1, y0, y1):
    sub = mask[y0:y1 + 1, x0:x1 + 1]
    xs = np.where(sub.any(axis=0))[0]
    return (int(xs.min()) + x0, int(xs.max()) + x0) if len(xs) else None

print("\n=== MEASURED (raw pixels, frame index in sheet) ===")
for k, (fi, v) in enumerate(zip(picks, vals)):
    im = Image.open(os.path.join(OUTDIR, "frame_%05d.jpg" % k))
    dark, lip = masks(im)
    x0, y0, x1, y1 = FACE
    # the cap brim is also near-black: search the brow band below it, and the
    # pupil band below that, so the gate reads the face and not the hat.
    gr_b = rows_of(dark, x0, x1, 175, 240)
    gr_p = rows_of(dark, x0, x1, 241, 300)
    brow = gr_b[0] if gr_b else None
    pup = gr_p[-1] if gr_p else None
    both = rows_of(dark, x0, x1, y0, y1)
    brim = both[0] if both and both[0][1] < 172 else None
    bw = extent(dark, x0, x1, brow[0], brow[1]) if brow else None
    pl = extent(dark, x0, 268, pup[0], pup[1]) if pup else None
    pr = extent(dark, 272, x1, pup[0], pup[1]) if pup else None
    lr = rows_of(lip, x0, x1, y0, y1, minpx=3)
    lx = extent(lip, x0, x1, lr[0][0], lr[-1][1]) if lr else None
    mh = (lr[-1][1] - lr[0][0] + 1) if lr else 0
    mw = (lx[1] - lx[0] + 1) if lx else 0
    print("f%-4d mouth=%.2f  brim %s  brow rows %s w %s  pupil rows %s  eyes %s/%s  mouth %dx%d (h/w %.2f)" % (
        fi, v, brim, brow, bw, pup, pl, pr, mw, mh, (mh / mw if mw else 0)))
