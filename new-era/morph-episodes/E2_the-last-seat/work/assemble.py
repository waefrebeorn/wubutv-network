#!/usr/bin/env python3
"""Assembly — THE LAST SEAT E2. ONE pass owns the joined intermediate.
Segments: conform 1280x720/24fps, exactly 240f each, bug burned in.
Shipped takes: U1 t1, U2 t1, U3 t1, U4 t2, U5 t2, U6 t1.
U6 carries the script's freeze (GAP 3's carrier): picture holds from
local 7.0s (frame 168) to 10.0s by cloning frame 167; audio runs
full-length under the freeze. Then concat -> work/joined.mp4, probed
= segment sum (1440f) before any master encode happens (finish.py)."""
import subprocess, sys

EP = "."
TAKES = {1: "takes/e2s5_u01_t1.mp4", 2: "takes/e2s5_u02_t1.mp4",
         3: "takes/e2s5_u03_t1.mp4", 4: "takes/e2s5_u04_t2.mp4",
         5: "takes/e2s5_u05_t2.mp4", 6: "takes/e2s5_u06_t1.mp4"}
CONF = "scale=1280:720:force_original_aspect_ratio=increase,crop=1280:720,setsar=1,fps=24"

def run(cmd):
    print("+", " ".join(cmd[:6]), "...")
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr[-3000:]); sys.exit(1)

def segment(u, take):
    out = f"work/segments/seg_u{u:02d}.mp4"
    if u < 6:
        vf = f"{CONF},trim=end_frame=240,setpts=N/(24*TB)"
    else:
        # freeze: 168 live frames, then frame 167 cloned to 240
        vf = (f"{CONF},trim=end_frame=168,setpts=N/(24*TB),"
              f"tpad=stop_mode=clone:stop_duration=3.1,trim=end_frame=240,setpts=N/(24*TB)")
    fc = f"[0:v]{vf}[v];[v][1:v]overlay=0:0[outv]"
    cmd = ["ffmpeg", "-v", "error", "-y", "-i", take, "-loop", "1", "-i", "work/gfx/bug.png",
           "-filter_complex", fc, "-map", "[outv]", "-map", "0:a:0",
           "-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p", "-r", "24",
           "-c:a", "aac", "-ar", "48000", "-ac", "2", "-t", "10", out]
    run(cmd)
    print("built", out)

for u in range(1, 7):
    segment(u, TAKES[u])

with open("work/segments/list.txt", "w") as fh:
    for u in range(1, 7):
        fh.write(f"file 'seg_u{u:02d}.mp4'\n")
run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", "work/segments/list.txt",
     "-c", "copy", "work/joined.mp4"])
print("joined built")
