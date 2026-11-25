#!/usr/bin/env python3
"""Remaster: exact bounds + loudnorm. From work/joined.mp4 (1440f, probed).
Video: trim=end_frame=1440. Audio: loudnorm single-pass (I=-16, TP=-1.5,
LRA=11 — dynamic mode; pure gain was impossible: joined TP -0.51 dBTP vs
I -22.11 LUFS), then atrim to exactly 60.000s. Overwrites the house master
(the 1441f first encode never shipped; finish.py's assert caught it)."""
import os, subprocess, sys
sys.path.insert(0, os.path.expanduser("~/workspace/wubutv-network/new-era/episodes/E2_SHOW-5_the-last-seat/work"))
from assemble import frames, EP

joined = f"{EP}/work/joined.mp4"
master = f"{EP}/masters/E2_SHOW-5_the-last-seat_house.mp4"
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", joined,
                "-map", "0:v:0", "-map", "0:a:0",
                "-vf", "trim=end_frame=1440,setpts=N/(24*TB)",
                "-af", "loudnorm=I=-16:TP=-1.5:LRA=11,atrim=0:60,asetpts=N/SR/TB",
                "-c:v", "libx264", "-preset", "medium", "-crf", "18",
                "-pix_fmt", "yuv420p", "-r", "24",
                "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
                "-movflags", "+faststart", master], check=True)
f = frames(master)
print(f"MASTER: {master} frames={f} size={os.path.getsize(master)}", flush=True)
assert f == 1440, f"master has {f} frames"
print("REMASTER DONE")
