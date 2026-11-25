#!/usr/bin/env python3
"""Fast seam scan: one decode pass per take (frames 216-239 and 0-24 as
320x180 gray PNGs), then MAE combos in numpy."""
import subprocess, os
import numpy as np
from PIL import Image

BASE = "/home/hatch/workspace/wubutv-network/new-era/episodes/E2_SHOW-1_the-machine"
TAKES = {
    "U1": "takes/media-generation-e2-u1-take3-0-c2f6e6b8-85f5-4a8d-bd0c-4d1f12759247.mp4",
    "U2": "takes/media-generation-e2-u2-take1-0-8d186a12-d9e5-49df-adcd-a9daa93196b8.mp4",
    "U3": "takes/media-generation-e2-u3-take5-0-46b36e3a-04e9-482c-bd1c-5c5e3ae7f732.mp4",
    "U4": "takes/media-generation-e2-u4-take1-0-1b939fab-9809-4f10-80b1-0ea478c65c66.mp4",
    "U5": "takes/media-generation-e2-u5-take1-0-937bf2c2-baf3-4126-ad79-dcede5d8c7b3.mp4",
    "U6": "takes/media-generation-e2-u6-take2-0-71a12e24-ce3c-4441-861f-88ac28bc872f.mp4",
}
OUT = os.path.join(BASE, "work/qc/seamframes")
os.makedirs(OUT, exist_ok=True)

def dump(unit, path):
    # head frames 0..24 and tail frames 216..239 in two passes
    for tag, sel in (("h", "lt(n\\,25)"), ("t", "gte(n\\,216)")):
        d = os.path.join(OUT, f"{unit}{tag}")
        os.makedirs(d, exist_ok=True)
        if len(os.listdir(d)) >= 20:
            continue
        subprocess.run(["ffmpeg", "-v", "error", "-i", os.path.join(BASE, path),
                        "-vf", f"select='{sel}',scale=320:180,format=gray",
                        "-vsync", "0", os.path.join(d, "%03d.png")], check=True)

def load(unit, tag):
    d = os.path.join(OUT, f"{unit}{tag}")
    files = sorted(os.listdir(d))
    return [np.asarray(Image.open(os.path.join(d, f)), dtype=np.float32) for f in files]

for u, p in TAKES.items():
    dump(u, p)

def mae(a, b):
    return float(np.mean(np.abs(a - b)))

JOINTS = [("U1", "U2"), ("U2", "U3"), ("U3", "U4"), ("U4", "U5"), ("U5", "U6")]
for up, dn in JOINTS:
    tail = load(up, "t")   # frames 216..239 -> index i = frame 216+i
    head = load(dn, "h")   # frames 0..24
    def uf(f): return tail[f - 216]
    naive = mae(uf(239), head[0])
    best = (1e9, None)
    for a in range(0, 13):
        for b in range(0, 13):
            v = mae(uf(239 - a), head[b])
            if v < best[0]:
                best = (v, (a, b))
    a, b = best[1]
    hm = mae(head[b], head[b + 12])
    print(f"{up}->{dn}: naive {naive:.1f} | best {best[0]:.1f} at tail-trim {a}f "
          f"head-trim {b}f | downstream head motion f{b}->f{b+12} {hm:.1f}")
