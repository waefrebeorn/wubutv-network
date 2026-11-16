#!/usr/bin/env python3
"""MV-14 M6 motion gate — sprint 2 calibration (M6_CALIBRATION_MV14.md).
Method matches tsm.py / m6_calibrate.py: one FFmpeg decode at 160x90
gray, native 24fps; d24 = mean abs-diff of consecutive frame pairs;
M6 = share of pairs with d24 < 0.0005 (tau_d). Longest duplicate run
in frames + seconds. Usable-window scope ONLY (the material that
enters the cut); never gate on full-take scope.
Gate: flag for EYE REVIEW when window M6 > 0.10 AND window longest
dup-run >= 0.30s. Never auto-reject on M6.
Usage: python3 mv14_m6.py <take-path> <w0> <w1>
"""
import subprocess
import sys

import numpy as np

W, H = 160, 90
TAU_D = 0.0005


def frames(path):
    cmd = ["ffmpeg", "-v", "error", "-i", path, "-vf",
           f"fps=24,scale={W}:{H},format=gray",
           "-f", "rawvideo", "-pix_fmt", "gray", "-"]
    raw = subprocess.run(cmd, capture_output=True, check=True).stdout
    arr = np.frombuffer(raw, dtype=np.uint8)
    n = len(arr) // (W * H)
    return arr[:n * W * H].reshape(n, H, W).astype(np.float32) / 255.0


def main(path, w0, w1):
    f = frames(path)
    fps = 24
    i0, i1 = int(round(w0 * fps)), int(round(w1 * fps))
    i0, i1 = max(0, i0), min(len(f), i1)
    d = np.mean(np.abs(np.diff(f, axis=0)), axis=(1, 2))
    dw = d[i0:max(i0, i1 - 1)]
    dup = dw < TAU_D
    m6 = float(dup.mean()) if len(dw) else 0.0
    longest, cur = 0, 0
    for v in dup:
        cur = cur + 1 if v else 0
        longest = max(longest, cur)
    print(f"{path}: window {w0:.2f}-{w1:.2f}s frames[{i0}:{i1}] "
          f"M6={m6:.4f} longest_dup_run={longest}f ({longest / fps:.2f}s) "
          f"median_d24={float(np.median(dw)):.4f}")
    print(f"  FLAG={'YES - eye review' if (m6 > 0.10 and longest / fps >= 0.30) else 'no'}")


if __name__ == "__main__":
    main(sys.argv[1], float(sys.argv[2]), float(sys.argv[3]))
