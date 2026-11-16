#!/usr/bin/env python3
"""Joint Gate measurement on the joined picture: seam MAE per boundary,
baseline (95th pct of in-unit adjacent MAE sampled every 24f, edges
excluded), and joint strips (cut-6..cut+6) per boundary.
Usage: joint_gate.py <joined.mp4> <outdir>"""
import subprocess, sys, os
import numpy as np
from PIL import Image

joined, outdir = sys.argv[1], sys.argv[2]
os.makedirs(outdir, exist_ok=True)
W, H = 320, 180
raw = subprocess.run(["ffmpeg", "-v", "error", "-i", joined, "-vf",
                      f"scale={W}:{H},format=gray", "-f", "rawvideo", "-"],
                     capture_output=True, check=True).stdout
fr = np.frombuffer(raw, dtype=np.uint8)
n = fr.size // (W * H)
fr = fr[:n * W * H].reshape(n, W * H).astype(np.float32)
print("frames decoded:", n)
mae = np.abs(np.diff(fr, axis=0)).mean(axis=1)  # mae[i]: frame i -> i+1

samples = []
for u in range(6):
    base = u * 240
    for k in range(12, 229, 24):
        samples.append(mae[base + k])
base95 = float(np.percentile(samples, 95))
print(f"BASE (95th pct in-unit adjacent MAE): {base95:.2f}  (n={len(samples)})")

for b in range(5):
    cut = (b + 1) * 240
    seam = float(mae[cut - 1])
    ratio = seam / base95 if base95 else 0
    print(f"boundary U{b+1}->U{b+2} @f{cut}: seam MAE {seam:.2f}  xBASE {ratio:.2f}")

# joint strips at full res, downscaled per-frame to 320x180, 13 frames wide
for b in range(5):
    cut = (b + 1) * 240
    start = cut - 6
    imgs = []
    for i in range(13):
        p = os.path.join(outdir, f"b{b+1}_f{start+i}.png")
        subprocess.run(["ffmpeg", "-v", "error", "-i", joined, "-vf",
                        f"select='eq(n\\,{start+i})',scale=320:180", "-frames:v", "1", p],
                       check=True)
        imgs.append(Image.open(p))
    strip = Image.new("RGB", (320 * 13, 180))
    for i, im in enumerate(imgs):
        strip.paste(im, (i * 320, 0))
    strip.save(os.path.join(outdir, f"joint_b{b+1}.jpg"), quality=88)
    print("strip", b + 1, "saved")
