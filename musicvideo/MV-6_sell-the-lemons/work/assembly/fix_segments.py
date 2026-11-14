#!/usr/bin/env python3
"""MV-6 gate fixes: re-render 9 pieces in place (phrase-smooth re-anchors on measured
visible mouth opens from the gate fine-strips; same render recipe as build_segments.py)."""
import os, subprocess

ROOT = os.path.expanduser("~/workspace/wubutv-network/musicvideo/MV-6_sell-the-lemons")
SEG = os.path.join(ROOT, "work/assembly/seg")

# segfile, takefile, take_in, take_out, frames
FIXES = [
    ("002_s02.mp4", "mv6_s02_t1.mp4", 3.44, 5.02, 73),    # intro hook #a: open was +0.38 late -> +0.13
    ("007_s03.mp4", "mv6_s03_t2.mp4", 4.90, 7.66, 77),    # V1 L3: open +0.21 -> +0.08
    ("011_s04.mp4", "mv6_s04_t2.mp4", 5.37, 7.18, 75),    # V1 L7: open +0.60 -> +0.12
    ("015_s05.mp4", "mv6_s05_t1.mp4", 6.35, 8.60, 77),    # C1 L3: open +0.95 -> +0.11
    ("020_s08.mp4", "mv6_s08_t3.mp4", 3.41, 6.08, 69),    # V2 L5: open +0.30 -> +0.08
    ("026_s10.mp4", "mv6_s10_t1.mp4", 5.95, 8.48, 72),    # C2 L3: open +0.63 -> +0.09
    ("027_s14.mp4", "mv6_s14_t1.mp4", 0.16, 2.48, 73),    # V3 L1: open +0.25 -> +0.09
    ("037_s16.mp4", "mv6_s16_t1.mp4", 5.99, 8.05, 75),    # FC L3: open +0.38 -> +0.11
    ("045_s05.mp4", "mv6_s06_t1.mp4", 3.90, 5.90, 43),    # C1 L7 chunk: closed-face -> S06 plate
]

def render(segfile, takefile, tin, tout, nframes):
    span = tout - tin
    f = (nframes / 24.0) / span
    vf = (f"setpts=PTS*{f:.6f},tpad=stop_mode=clone:stop_duration=1.0,fps=24,"
          f"scale=1280:720:flags=bicubic,format=yuv420p")
    out = os.path.join(SEG, segfile)
    cmd = ["ffmpeg", "-y", "-v", "error", "-ss", f"{tin:.3f}", "-t", f"{span:.3f}",
           "-i", os.path.join(ROOT, "takes", takefile), "-vf", vf,
           "-frames:v", str(nframes), "-c:v", "libx264", "-preset", "medium",
           "-crf", "16", "-an", out]
    subprocess.run(cmd, check=True)
    print(f"{segfile}: {takefile} {tin}-{tout} f={f:.3f} frames={nframes}")

if __name__ == "__main__":
    for fx in FIXES:
        render(*fx)
    print("fixes done")
