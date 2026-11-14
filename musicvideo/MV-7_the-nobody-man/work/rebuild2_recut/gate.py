#!/usr/bin/env python3
"""Master gate evidence: for every sung-picture line, extract the onset frame
and onset+1 frame (full-res face crop) from a candidate master and tile them
into labeled grids for visual adjudication. Also scans for near-duplicate
frame runs >= 24f during vocal spans (freeze check).
Usage: gate.py <video> <out_prefix>"""
import json, subprocess, sys, os
import numpy as np

BASE = "/home/hatch/workspace/wubutv-network/musicvideo/MV-7_the-nobody-man"
RC = f"{BASE}/work/rebuild2_recut"
FPS = 24
video, prefix = sys.argv[1], sys.argv[2]
_man = json.load(open(f"{RC}/seg_manifest.json"))
man = {m["ref"]: m for m in (_man["segments"] if isinstance(_man, dict) else _man)}
anchors = {r["ref"]: r for r in json.load(open(f"{RC}/anchors.json"))["lines"]}
GATED = [r for r, m in man.items() if m["kind"] in ("KEEP", "RESCUE", "COND")]
GATED.sort(key=lambda r: anchors[r]["a"])
print("gated lines:", len(GATED))

# decode whole video once at native res (720p, ~630MB per 10s -> stream it)
proc = subprocess.Popen(
    ["ffmpeg", "-v", "error", "-i", video, "-f", "rawvideo",
     "-pix_fmt", "rgb24", "-s", "1280x720", "-"],
    stdout=subprocess.PIPE)
W, H = 1280, 720
want = {}
for ref in GATED:
    f0 = int(round(anchors[ref]["a"] * FPS))
    want[f0] = (ref, 0)
    want[f0 + 1] = (ref, 1)
frames = {}
small_prev, small_run, max_run = None, 0, 0
run_start = 0
worst = (0, 0)
fi = -1
while True:
    buf = proc.stdout.read(W * H * 3)
    if len(buf) < W * H * 3:
        break
    fi += 1
    if fi in want:
        frames[fi] = np.frombuffer(buf, np.uint8).reshape(H, W, 3).copy()
    # freeze scan on a small luma proxy every frame (cheap approx: use the
    # buffer's green channel subsample)
    fr = np.frombuffer(buf, np.uint8).reshape(H, W, 3)[::6, ::6, 1].astype(np.int16)
    if small_prev is not None:
        d = np.abs(fr - small_prev).mean()
        if d < 1.2:
            small_run += 1
            if small_run > max_run:
                max_run, worst = small_run, (run_start, fi)
        else:
            small_run, run_start = 0, fi
    small_prev = fr
proc.wait()
total = fi + 1
print("total frames:", total, "| longest near-dup run:", max_run, "at", worst)

# grids: per line two panels (onset, +1). 6 lines per grid (12 panels, 4x3).
from PIL import Image, ImageDraw
cx0, cy0, cw, ch = int(0.30 * 1248), int(0.26 * 704), int(0.32 * 1248), int(0.34 * 704)
# video is 1280x720 (scaled from 1248x704 takes) — crop proportionally
cx0, cy0, cw, ch = int(0.30 * W), int(0.26 * H), int(0.32 * W), int(0.34 * H)
PW, PH = 340, 290
per = 6
os.makedirs(os.path.dirname(prefix), exist_ok=True)
meta = []
for gi in range(0, len(GATED), per):
    chunk = GATED[gi:gi + per]
    grid = Image.new("RGB", (4 * PW, 3 * PH), (24, 24, 24))
    dr = ImageDraw.Draw(grid)
    for li, ref in enumerate(chunk):
        f0 = int(round(anchors[ref]["a"] * FPS))
        for k in (0, 1):
            fr = frames.get(f0 + k)
            if fr is None:
                continue
            crop = Image.fromarray(fr[cy0:cy0 + ch, cx0:cx0 + cw]).resize((PW, PH - 22))
            x = (li % 2) * 2 * PW + k * PW
            y = (li // 2) * PH
            grid.paste(crop, (x, y + 22))
            dr.text((x + 6, y + 4), f"{ref} {'onset' if k == 0 else '+1'} f{f0 + k}",
                    fill=(255, 255, 90))
        meta.append({"ref": ref, "onset_frame": f0, "grid": gi // per})
    p = f"{prefix}_{gi // per:02d}.jpg"
    grid.save(p, quality=88)
    print("wrote", p)
json.dump({"gated": meta, "total_frames": total,
           "max_near_dup_run": max_run, "worst_run": worst},
          open(f"{prefix}_meta.json", "w"), indent=1)
