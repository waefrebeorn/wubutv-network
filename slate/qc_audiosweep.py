#!/usr/bin/env python3
"""Per-window max-volume sweep for episode QC. Prints t, max_volume dB per 0.25s window."""
import subprocess, re, sys, glob, os

pat = sys.argv[1]
t0 = float(sys.argv[2]) if len(sys.argv) > 2 else 0.0
t1 = float(sys.argv[3]) if len(sys.argv) > 3 else 10.0
step = float(sys.argv[4]) if len(sys.argv) > 4 else 0.25
f = glob.glob(pat)[0]
print(f"# file: {os.path.basename(f)}")
t = t0
while t < t1 - 1e-9:
    r = subprocess.run(
        ["ffmpeg", "-ss", f"{t:.2f}", "-t", f"{step:.2f}",
         "-i", f, "-af", "volumedetect", "-f", "null", "-"],
        capture_output=True, text=True)
    m = re.search(r"max_volume:\s*(\S+)\s*dB", r.stderr)
    mv = m.group(1) if m else "n/a"
    print(f"{t:5.2f}s  max {mv} dB")
    t += step
