#!/usr/bin/env python3
"""MV-3 finals: intermediates + burned captions + corner bug + master audio.

Precedent: MV-2 v6 delivered with captions BURNED and the ~ WuBu ~
corner bug (verified on a v6 frame), despite assemble.md's
"never burn" line -- chat playback on iPhone needs burned captions.
Disclosed in ASSEMBLY_REPORT.md.
"""
import subprocess, os

PROJ = os.path.dirname(os.path.abspath(__file__))
M = os.path.join(PROJ, "masters")
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

def run(cmd):
    print(" ".join(cmd))
    subprocess.run(cmd, check=True)

def final(inter, ass, bug_size, out):
    bug = (f"drawtext=fontfile={FONT}:text='~ WuBu ~':fontsize={bug_size}:"
           f"fontcolor=0xFFC61E:box=1:boxcolor=black@0.5:boxborderw=12:"
           f"x=w-tw-30:y=30")
    run(["ffmpeg", "-y", "-v", "error", "-i", inter, "-i",
         os.path.join(PROJ, "track.mp3"), "-filter_complex",
         f"[0:v]subtitles={ass},{bug}[v]", "-map", "[v]", "-map", "1:a",
         "-c:v", "libx264", "-crf", "18", "-preset", "medium",
         "-pix_fmt", "yuv420p", "-r", "24", "-c:a", "aac", "-ar", "48000",
         "-ac", "2", "-b:a", "192k", "-movflags", "+faststart", out])

if __name__ == "__main__":
    final(os.path.join(M, "mv3_intermediate_16x9.mp4"),
          os.path.join(PROJ, "captions_16x9.ass"), 36,
          os.path.join(M, "mv3_i_am_your_dad_16x9.mp4"))
    final(os.path.join(M, "mv3_intermediate_9x16.mp4"),
          os.path.join(PROJ, "captions_9x16.ass"), 44,
          os.path.join(M, "mv3_i_am_your_dad_9x16.mp4"))
    # chat copy: scaled 16:9 final, same audio spec, faststart
    run(["ffmpeg", "-y", "-v", "error", "-i",
         os.path.join(M, "mv3_i_am_your_dad_16x9.mp4"),
         "-vf", "scale=854:480", "-c:v", "libx264", "-crf", "23",
         "-preset", "medium", "-pix_fmt", "yuv420p", "-r", "24",
         "-c:a", "aac", "-ar", "48000", "-ac", "2", "-b:a", "128k",
         "-movflags", "+faststart",
         os.path.join(M, "mv3_i_am_your_dad_16x9_chat.mp4")])
    print("finals done")
