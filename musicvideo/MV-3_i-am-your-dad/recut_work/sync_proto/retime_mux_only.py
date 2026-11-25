#!/usr/bin/env python3
"""MV-3 RETIMED 16:9 final mux ONLY (recovery run 2026-11-05 ~02:48 EST).

The previous R&D agent died on a sqlx pool timeout AFTER the retimed
intermediate was verified complete (8516 frames) but DURING the final
mux -- masters/mv3_i_am_your_dad_16x9_retimed.mp4 was left truncated
(30,933,040 B). This script re-runs ONLY the final mux step, verbatim
from retime_build.py: subtitles + bug + untouched master audio.
It never rebuilds the intermediate and never touches the delivered
re-cut or the rejected original cut.
"""
import os
import subprocess
import sys

PROJ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
INTER = os.path.join(PROJ, "masters", "mv3_intermediate_16x9_retimed.mp4")
OUT = os.path.join(PROJ, "masters", "mv3_i_am_your_dad_16x9_retimed.mp4")
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
bug = (f"drawtext=fontfile={FONT}:text='~ WuBu ~':fontsize=36:"
       f"fontcolor=0xFFC61E:box=1:boxcolor=black@0.5:boxborderw=12:"
       f"x=w-tw-30:y=30")

nf = subprocess.run(["ffprobe", "-v", "error", "-count_frames",
                     "-select_streams", "v:0",
                     "-show_entries", "stream=nb_read_frames",
                     "-of", "csv=p=0", INTER],
                    capture_output=True, text=True, check=True).stdout.strip()
print(f"intermediate: {nf} frames (target 8516)", flush=True)
assert int(nf) == 8516, (INTER, nf)

subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", INTER, "-i",
                os.path.join(PROJ, "track.mp3"), "-filter_complex",
                f"[0:v]subtitles={os.path.join(PROJ, 'captions_16x9.ass')},{bug}[v]",
                "-map", "[v]", "-map", "1:a",
                "-c:v", "libx264", "-crf", "18", "-preset", "medium",
                "-pix_fmt", "yuv420p", "-r", "24", "-c:a", "aac",
                "-ar", "48000", "-ac", "2", "-b:a", "192k",
                "-movflags", "+faststart", OUT], check=True)
print(f"retimed 16:9 final: {OUT}", flush=True)
print(f"size: {os.path.getsize(OUT)} bytes", flush=True)
