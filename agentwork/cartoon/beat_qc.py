"""Beat QC: prove the authored stillness is a hold, not a dead render, and that the
brow drop actually landed in the shipped pixels.

Usage: beat_qc.py FRAMEDIR SESSION.json
Prints: mean |diff| between consecutive frames inside the still window, in a speech
window of the same length, and the measured brow row band before vs after the drop.
"""
import sys, os, json
import numpy as np
from PIL import Image

FD, SJ = sys.argv[1:3]
S = json.load(open(SJ))
FPS = int(S.get("fps", 24))
N = int(S.get("nframes", 0))
ST = S.get("still") or [0, 0]
BD = S.get("brow_pop") or S.get("brow_drop") or [0, 0]
mouth = S.get("mouth", [])

def load(i):
    return np.asarray(Image.open(os.path.join(FD, "frame_%05d.jpg" % i)).convert("RGB"), dtype=np.int16)

def diffs(a, b):
    return np.abs(a - b)

def wdiff(i0, i1):
    vals = []
    for i in range(i0, min(i1, N - 1)):
        vals.append(diffs(load(i), load(i + 1)).mean())
    return vals

# speech window: pick a run of frames with the highest mouth values outside the still
best, bi = -1, 0
try:
    for i in range(0, N - 8, 8):
        m = sum(mouth[i:i + 8]) / 8
        if m > best and not (ST[1] > ST[0] and ST[0] <= i < ST[1]):
            best, bi = m, i
except Exception:
    pass
sw = wdiff(bi, bi + max(8, (ST[1] - ST[0]) - 1)) if ST[1] > ST[0] else wdiff(bi, bi + 8)
st = wdiff(ST[0] + 1, ST[1] - 1) if ST[1] > ST[0] else [0.0]
print("still window %s mean |diff| %.3f  max %.3f  (n=%d)" % (ST, np.mean(st), np.max(st), len(st)))
print("speech window %d-%d mean |diff| %.3f  max %.3f  (n=%d)" % (
    bi, bi + max(8, (ST[1] - ST[0]) - 1) if ST[1] > ST[0] else bi + 8,
    np.mean(sw), np.max(sw), len(sw)))
print("STILL_HOLD %s (still must be < 20%% of speech motion)" %
      ("PASS" if np.mean(st) < 0.2 * max(1e-6, np.mean(sw)) else "FAIL"))

# brow row band: dark horizontal bar in rows 175-245, columns 150-390
def brow_row(i):
    a = load(i)
    dark = a.max(axis=2) < 80
    sub = dark[175:245, 150:390]
    rows = np.where(sub.sum(axis=1) >= 20)[0]
    if not len(rows):
        return None
    return (int(rows.min()) + 175, int(rows.max()) + 175)

ref_i = ST[0] - 6 if ST[0] > 8 else 0
b_ref = brow_row(ref_i)
b_drop = brow_row(min(N - 1, BD[0] + 6)) if BD[1] > BD[0] else None
print("brow rows before drop (f%d) %s -> after drop (f%d) %s" % (ref_i, b_ref, min(N - 1, BD[0] + 6), b_drop))
if b_ref and b_drop:
    print("BROW_DROP delta %+d px" % (b_drop[0] - b_ref[0]))
