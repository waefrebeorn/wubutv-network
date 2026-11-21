#!/usr/bin/env python3
"""Joint Gate (JOINT_COHESION_METHOD section 6) on the assembled master.
All five boundaries are declared BREAKs: no seam-MAE bar; seam MAE logged;
eye items read off the strips saved to work/qc/joints/.
Computes: seam MAE per joint (320x180 gray), BASE (95th pct of adjacent-frame
MAE sampled every 24f inside units, excluding 12f at unit edges), upstream
tail motion (mean MAE, last 12f of unit N), downstream head motion (mean MAE,
first 12f of unit N+1; eye item 6 floor >= 8).
Usage: joint_gate.py <master.mp4>
"""
import os, subprocess, sys
import numpy as np
from PIL import Image

EP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = f"{EP}/work/qc/joints"
os.makedirs(OUT, exist_ok=True)
W, H = 320, 180

def load_frames(path):
    out = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-map", "0:v:0",
                          "-vf", "scale=320:180,format=gray", "-f", "rawvideo", "-"],
                         capture_output=True, check=True).stdout
    n = len(out) // (W * H)
    return np.frombuffer(out[:n * W * H], dtype=np.uint8).astype(np.float64).reshape(n, W * H)

def full_frame(path, idx):
    tmp = f"{OUT}/_f{idx}.png"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", path, "-vf",
                    f"select='eq(n\\,{idx})',scale=640:360", "-vsync", "0",
                    "-frames:v", "1", tmp], check=True)
    return Image.open(tmp).convert("RGB")

def main():
    path = sys.argv[1]
    fr = load_frames(path)
    n = len(fr)
    print(f"frames loaded: {n}")
    mae = np.abs(np.diff(fr, axis=0)).mean(axis=1)  # mae[i]: frame i -> i+1
    samples = []
    for u in range(6):
        for i in range(u * 240 + 12, (u + 1) * 240 - 12, 24):
            samples.append(mae[i])
    base = float(np.percentile(samples, 95))
    print(f"BASE (95th pct intra-unit adjacent MAE): {base:.2f}")
    for j in range(5):
        cut = (j + 1) * 240  # first frame of unit j+2
        seam = float(mae[cut - 1])
        tail = float(mae[cut - 12:cut].mean())
        head = float(mae[cut:cut + 12].mean())
        print(f"JOINT U{j+1}->U{j+2} @f{cut}: seam MAE {seam:.2f} | upstream tail MAE "
              f"{tail:.2f} | downstream head MAE {head:.2f} (item6 floor 8: "
              f"{'PASS' if head >= 8 else 'FAIL'})")
        # strip: frames cut-6..cut+5 at 640x360 in a 4x3 grid
        tiles = [full_frame(path, cut - 6 + k) for k in range(12)]
        strip = Image.new("RGB", (640 * 4, 360 * 3))
        for k, t in enumerate(tiles):
            strip.paste(t, ((k % 4) * 640, (k // 4) * 360))
        strip.save(f"{OUT}/strip_U{j+1}-U{j+2}.png")
        # seam frames full-res side by side
        a = full_frame(path, cut - 1).resize((1280, 720))
        b = full_frame(path, cut).resize((1280, 720))
        pair = Image.new("RGB", (2560, 720))
        pair.paste(a, (0, 0)); pair.paste(b, (1280, 0))
        pair.save(f"{OUT}/seam_U{j+1}-U{j+2}.png")
        print(f"  strip + seam saved (U{j+1}-U{j+2})")

if __name__ == "__main__":
    main()
