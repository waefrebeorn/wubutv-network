"""Motion gate for MV-2 v6 volley 6: 0.5s-sampled grayscale mean abs diff at
160x90 via ffmpeg rawvideo. Prints diffs per take; a zero run during the
vocal is a motion FAIL.
"""
import pathlib, subprocess
import numpy as np
proj = pathlib.Path.home() / "workspace/wubutv-network/musicvideo/MV-2_toll-roads-are-dumb"
takes = ["mv2_r1_t3.mp4", "mv2_s08_t6.mp4", "mv2_s23_t7.mp4",
         "mv2_r3_t2.mp4", "mv2_r4_t1.mp4", "mv2_r5_t1.mp4"]
for fname in takes:
    path = str(proj / "takes" / fname)
    cmd = ["ffmpeg", "-v", "error", "-i", path, "-vf", "fps=2,scale=160:90,format=gray",
           "-f", "rawvideo", "-pix_fmt", "gray", "-"]
    raw = subprocess.run(cmd, capture_output=True, check=True).stdout
    n = len(raw) // (160 * 90)
    frames = np.frombuffer(raw, dtype=np.uint8).reshape(n, 160 * 90).astype(np.int16)
    diffs = [round(float(np.mean(np.abs(frames[i] - frames[i - 1]))), 1) for i in range(1, n)]
    print(fname, "frames=", n, "diffs(0.5s)=", diffs)
