"""Face-region hold QC: is the authored still a hold ON THE FACE?

beat_qc.py compares whole-frame mean |diff|. On this rig the frame is ~99.8% static
background, so the whole-frame number is dominated by the JPEG noise floor on the
gradient (measured 0.047 with a deliberately frozen face) and a fair comparison has
to be region-limited. This measures the same quantity inside the face box, plus the
noise floor (two frames that should be identical), for both the still window and the
loudest speech window.

Usage: face_hold_qc.py FRAMEDIR SESSION.json
"""
import sys, os, json
import numpy as np
from PIL import Image

FD, SJ = sys.argv[1:3]
S = json.load(open(SJ))
N = int(S.get("nframes", 0))
ST = S.get("still") or [0, 0]
mouth = S.get("mouth", [])

BOX = (150, 180, 390, 390)   # face + jaw, inside the head silhouette


def load(i):
    a = np.asarray(Image.open(os.path.join(FD, "frame_%05d.jpg" % i)).convert("RGB"), dtype=np.int16)
    x0, y0, x1, y1 = BOX
    return a[y0:y1, x0:x1]


def wdiff(i0, i1):
    return [float(np.abs(load(i) - load(i + 1)).mean()) for i in range(i0, min(i1, N - 1))]


best, bi = -1, 0
for i in range(0, N - 12, 6):
    m = sum(mouth[i:i + 8]) / 8.0
    if m > best and not (ST[1] > ST[0] and ST[0] - 2 <= i < ST[1] + 2):
        best, bi = m, i
L = max(8, (ST[1] - ST[0]) - 1)
st = wdiff(ST[0] + 1, ST[1] - 1) if ST[1] > ST[0] else []
sw = wdiff(bi, bi + L)
print("face box %s" % (BOX,))
print("still  %d-%d  n=%d  mean %.3f  max %.3f" % (ST[0], ST[1], len(st), np.mean(st) if st else 0,
                                                    np.max(st) if st else 0))
print("speech %d-%d  n=%d  mean %.3f  max %.3f  (loudest run, mean mouth %.2f)" % (
    bi, bi + L, len(sw), np.mean(sw), np.max(sw), best))
if st and sw:
    print("ratio still/speech %.1f%%  (gate: < 20%%)" % (100 * np.mean(st) / max(1e-9, np.mean(sw))))
    print("FACE_HOLD %s" % ("PASS" if np.mean(st) < 0.2 * np.mean(sw) else "FAIL"))
# inside the still the pose is authored frozen, so the still diffs THEMSELVES are the
# noise floor; the min is the floor with no step, the max catches the 1-frame +0.01
# moving-hold nudge the driver writes at the midpoint.
if st:
    print("still diffs min %.4f median %.4f max %.4f" % (
        np.min(st), np.median(st), np.max(st)))
