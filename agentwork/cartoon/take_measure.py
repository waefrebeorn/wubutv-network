"""Measure a take window frame by frame: brow band, eye-plate pixels, mouth band.

Usage: take_measure.py FRAMEDIR F0 F1
Prints one line per frame so the dip / pop / settle can be read as numbers.
The eye plate is WHITE, so a closing eye is a collapse in white-pixel count, and
the brow row band moving is the head offset (they share the head group).
"""
import sys, os
import numpy as np
from PIL import Image

FD, f0, f1 = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
print("frame brow_rows  eye_white_px  mouth_rows  mouth_h")
for i in range(f0, f1):
    p = os.path.join(FD, "frame_%05d.jpg" % i)
    if not os.path.exists(p):
        print("%5d MISSING" % i)
        continue
    a = np.asarray(Image.open(p).convert("RGB"), dtype=np.int16)
    lum = 0.299 * a[:, :, 0] + 0.587 * a[:, :, 1] + 0.114 * a[:, :, 2]
    dark = lum < 80
    br = np.where(dark[185:262, 150:390].any(axis=1))[0]
    brow = (int(br.min()) + 185, int(br.max()) + 185) if len(br) else None
    white = (a[:, :, 0] > 195) & (a[:, :, 1] > 195) & (a[:, :, 2] > 195)
    wp = int(white[235:310, 150:390].sum())
    wr = np.where(white[235:310, 150:390].any(axis=1))[0]
    wspan = (int(wr.min()) + 235, int(wr.max()) + 235) if len(wr) else None
    lip = (a[:, :, 0] - a[:, :, 2] > 40) & (a[:, :, 1] < 80)
    mr = np.where(lip[265:375, 150:390].any(axis=1))[0]
    mspan = (int(mr.min()) + 265, int(mr.max()) + 265) if len(mr) else None
    mh = (mspan[1] - mspan[0] + 1) if mspan else 0
    print("%5d %-12s %5d %-12s %3d%s" % (
        i, str(brow), wp, str(wspan), mh, "" if mspan else "  (none)"))
