#!/usr/bin/env python3
"""Assembly — THE LAST SEAT E1. ONE pass owns the joined intermediate.
Segments: conform 1280x720/24fps, exactly 240f each, bug burned in.
U6 carries the script's freeze (GAP 3's carrier): picture holds from local
7.5s (frame 180) to 10.0s; the QUESTION card fades in at 7.7s and holds.
Audio runs full-length under the freeze (the tap stops inside the take's
own audio). Then concat -> work/joined.mp4, probed = segment sum (1440f)
before any master encode happens (finish.py)."""
import subprocess, sys

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
        fc = f"[0:v]{vf}[v];[v][1:v]overlay=0:0[outv]"
        cmd = ["ffmpeg", "-v", "error", "-y", "-i", take, "-loop", "1", "-i", "work/gfx/bug.png",
               "-filter_complex", fc, "-map", "[outv]", "-map", "0:a:0",
               "-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p", "-r", "24",
               "-c:a", "aac", "-ar", "48000", "-ac", "2", "-t", "10", out]
    else:
        # freeze: 180 live frames, then frame 179 cloned to 240
        vf = (f"{CONF},trim=end_frame=180,setpts=N/(24*TB),"
              f"tpad=stop_mode=clone:stop_duration=2.6,trim=end_frame=240,setpts=N/(24*TB)")
        fc = (f"[0:v]{vf}[base];[base][1:v]overlay=0:0[b1];"
              f"[2:v]format=rgba,fade=in:st=7.7:d=0.4:alpha=1[card];"
              f"[b1][card]overlay=0:0[outv]")
        cmd = ["ffmpeg", "-v", "error", "-y", "-i", take, "-loop", "1", "-i", "work/gfx/bug.png",
               "-loop", "1", "-i", "work/gfx/question_card.png",
               "-filter_complex", fc, "-map", "[outv]", "-map", "0:a:0",
               "-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p", "-r", "24",
               "-c:a", "aac", "-ar", "48000", "-ac", "2", "-t", "10", out]
    run(cmd)
    print("built", out)

for u in range(1, 7):
    segment(u, f"takes/e1s5_u{u:02d}_t1.mp4")

with open("work/segments/list.txt", "w") as fh:
    for u in range(1, 7):
        fh.write(f"file 'seg_u{u:02d}.mp4'\n")
run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", "work/segments/list.txt",
     "-c", "copy", "work/joined.mp4"])
print("joined built")
