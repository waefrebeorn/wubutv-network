#!/usr/bin/env python3
"""MV-2 lyrics redo: burned-kinetic frame reads + v7 regression check.

1. Full-res PNGs from the lyrics master at line starts (eye reads: caption
   text correct, not cut at edges, highlight on the right word, first word
   not mid-fade faint) — one SEPARATE ffmpeg -ss call per frame (the
   multi-input gotcha: one call returns frame 0 for all outputs).
2. Regression vs the v7 master at caption-free times (2.0s, 265.0s): full
   frame mean |diff| must be tiny (encoder noise only) — proves the video
   is the v7 base untouched outside the caption layer. Also top-half diff
   at a captioned time (72.12s) must be tiny.
Frames land in work/lyrics-redo/gate/.
"""
import hashlib
import pathlib
import subprocess

import numpy as np

PROJ = pathlib.Path.home() / "workspace/wubutv-network/musicvideo/MV-2_toll-roads-are-dumb"
NEW = PROJ / "masters/mv2_toll_roads_are_dumb_v7_16x9_lyrics.mp4"
V7 = PROJ / "masters/mv2_toll_roads_are_dumb_v7_16x9.mp4"
GATE = PROJ / "work/lyrics-redo/gate"
GATE.mkdir(parents=True, exist_ok=True)

# (name, time) — line starts from the corrected grid + regression times
SHOTS = [
    ("L01_intro", 4.44),
    ("L03_widest", 20.04),
    ("L14_weaving_fix", 72.12),
    ("L17_mergers", 92.70),
    ("L34_gonna", 175.34),
    ("L35_interp_toll", 184.38),
    ("L41_parenthetical", 222.58),
    ("L42_block", 226.50),
    ("L48_outro", 258.14),
]
REGRESSION = [("reg_2s", 2.0), ("reg_265s", 265.0)]


def grab(src, t, out):
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(t),
                    "-i", str(src), "-frames:v", "1", str(out)],
                   check=True)


def frame_bytes(path):
    out = subprocess.run(["ffmpeg", "-v", "error", "-i", str(path),
                          "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(out, dtype=np.uint8)


def md5(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


seen = set()
for name, t in SHOTS:
    out = GATE / f"lyrics_{name}.png"
    grab(NEW, t, out)
    assert md5(out) not in seen, f"duplicate frame {name} (frame-0 gotcha)"
    seen.add(md5(out))
    print(f"lyrics {name} @{t}s -> {out.name} {out.stat().st_size}B md5 {md5(out)[:8]}")

for name, t in REGRESSION:
    a = GATE / f"lyrics_{name}.png"
    b = GATE / f"v7_{name}.png"
    grab(NEW, t, a)
    grab(V7, t, b)
    fa, fb = frame_bytes(a), frame_bytes(b)
    assert fa.shape == fb.shape, (fa.shape, fb.shape)
    full = float(np.abs(fa.astype(np.int16) - fb.astype(np.int16)).mean())
    # top half (y 0..360 at 720p) — above the caption band
    h, w = 720, 1280
    ia = fa.reshape(h, w, 3).astype(np.int16)
    ib = fb.reshape(h, w, 3).astype(np.int16)
    top = float(np.abs(ia[:360] - ib[:360]).mean())
    print(f"regression {name} @{t}s: full-frame mean|diff| {full:.3f}, "
          f"top-half {top:.3f} (expect <1.0, encoder noise only)")

# top-half diff at a captioned time (captions must not leak above the band)
a = GATE / "lyrics_topcheck_72.png"
b = GATE / "v7_topcheck_72.png"
grab(NEW, 72.12, a)
grab(V7, 72.12, b)
fa = frame_bytes(a).reshape(720, 1280, 3).astype(np.int16)
fb = frame_bytes(b).reshape(720, 1280, 3).astype(np.int16)
print(f"regression captioned-time 72.12s top-half mean|diff| "
      f"{float(np.abs(fa[:360] - fb[:360]).mean()):.3f}")
print(f"regression captioned-time 72.12s bottom-band mean|diff| "
      f"{float(np.abs(fa[600:] - fb[600:]).mean()):.3f} (captions live here)")
print("frames in", GATE)
