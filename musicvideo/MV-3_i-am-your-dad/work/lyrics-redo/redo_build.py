#!/usr/bin/env python3
"""MV-3 lyrics redo: re-encode the master from the Q5 intermediate with
ONLY the kinetic layer replaced.

Source video: masters/mv3_intermediate_16x9_q5.mp4 (CRF 12, 8516f —
verified before running). The intermediate has NO captions and NO bug,
so this rebuild is pixel-identical to the Q5 master except for the
kinetic layer + bug pass. Same final-stage command as q5_build.py
final_stage (subtitles filter + ~ WuBu ~ drawtext bug, libx264 CRF 18
preset medium, yuv420p 24fps, AAC 48k stereo 192k, faststart), with the
new work/lyrics-redo/mv3_kinetic_redo.ass in place of
captions_16x9_corrected.ass. Audio is track.mp3 (untouched, same as Q5).
Outputs: masters/mv3_i_am_your_dad_16x9_lyrics.mp4 + chat copy
masters/mv3_i_am_your_dad_16x9_lyrics_chat.mp4 (854x480 crf 23, AAC
copied untouched from the new master). Q5 + corrected masters NEVER
overwritten. Stages: final | chat (run separately).
"""
import os, subprocess, sys

PROJ = os.path.dirname(os.path.abspath(__file__))  # work/lyrics-redo
PROJ = os.path.dirname(os.path.dirname(PROJ))       # project root
ASS = os.path.join(PROJ, "work", "lyrics-redo", "mv3_kinetic_redo.ass")
INTER = os.path.join(PROJ, "masters", "mv3_intermediate_16x9_q5.mp4")
OUT = os.path.join(PROJ, "masters", "mv3_i_am_your_dad_16x9_lyrics.mp4")
CHAT = os.path.join(PROJ, "masters", "mv3_i_am_your_dad_16x9_lyrics_chat.mp4")

def frames(path):
    r = subprocess.run(["ffprobe", "-v", "error", "-count_frames",
                        "-select_streams", "v:0",
                        "-show_entries", "stream=nb_read_frames",
                        "-of", "csv=p=0", path],
                       capture_output=True, text=True, check=True)
    return int(r.stdout.strip())

def final_stage():
    assert os.path.exists(ASS), f"missing .ass: {ASS}"
    assert frames(INTER) == 8516, "intermediate is not 8516f"
    FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    bug = (f"drawtext=fontfile={FONT}:text='~ WuBu ~':fontsize=36:"
           f"fontcolor=0xFFC61E:box=1:boxcolor=black@0.5:boxborderw=12:"
           f"x=w-tw-30:y=30")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", INTER, "-i",
                    os.path.join(PROJ, "track.mp3"), "-filter_complex",
                    f"[0:v]subtitles={ASS},{bug}[v]",
                    "-map", "[v]", "-map", "1:a",
                    "-c:v", "libx264", "-crf", "18", "-preset", "medium",
                    "-pix_fmt", "yuv420p", "-r", "24", "-c:a", "aac",
                    "-ar", "48000", "-ac", "2", "-b:a", "192k",
                    "-movflags", "+faststart", OUT], check=True)
    nf = frames(OUT)
    print(f"lyrics master: {OUT}: {nf} frames (target 8516)", flush=True)
    assert nf == 8516, (OUT, nf)

def chat_stage():
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", OUT,
                    "-vf", "scale=854:480", "-c:v", "libx264", "-crf", "23",
                    "-preset", "medium", "-pix_fmt", "yuv420p", "-r", "24",
                    "-c:a", "copy", "-movflags", "+faststart", CHAT],
                   check=True)
    nf = frames(CHAT)
    sz = os.path.getsize(CHAT)
    print(f"chat copy: {CHAT}: {nf} frames, {sz} B ({sz/1048576:.1f} MB)", flush=True)
    assert nf == 8516, (CHAT, nf)
    assert sz <= 50 * 1024 * 1024, f"chat copy over 50MB: {sz}"

if __name__ == "__main__":
    stage = sys.argv[1] if len(sys.argv) > 1 else "final"
    {"final": final_stage, "chat": chat_stage}[stage]()
