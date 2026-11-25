#!/usr/bin/env python3
"""MV-14 motion QC — recreated 2026-11-11 after /tmp was cleared.
Numpy frame-diff on 160x90 gray frames at 4fps, matching the MV-12/13
method. Prints per-take mean/min diff, longest near-still run (>=12f
fail threshold is checked at assembly; here we report runs >=4f),
and the per-second diff series.
Usage: python3 mv14_motion.py takes/<file>.mp4 [...]
"""
import sys
import subprocess

import numpy as np


def frames(path, fps=4, w=160, h=90):
    cmd = ["ffmpeg", "-v", "error", "-i", path, "-vf",
           f"fps={fps},scale={w}:{h},format=gray",
           "-f", "rawvideo", "-pix_fmt", "gray", "-"]
    raw = subprocess.run(cmd, capture_output=True, check=True).stdout
    arr = np.frombuffer(raw, dtype=np.uint8)
    n = len(arr) // (w * h)
    return arr[:n * w * h].reshape(n, h, w).astype(np.float32)


def main(paths):
    for path in paths:
        f = frames(path)
        diffs = np.mean(np.abs(np.diff(f, axis=0)), axis=(1, 2))
        near = diffs < 2.0
        longest, cur = 0, 0
        for v in near:
            cur = cur + 1 if v else 0
            longest = max(longest, cur)
        print(f"{path}: n={len(f)} mean={diffs.mean():.2f} "
              f"min={diffs.min():.2f} max={diffs.max():.2f} "
              f"longest_near_still_frames={longest} "
              f"({longest / 4:.2f}s at 4fps)")
        print("  diffs:", [round(float(x), 1) for x in diffs])


if __name__ == "__main__":
    main(sys.argv[1:])
