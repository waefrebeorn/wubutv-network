#!/usr/bin/env python3
"""Finish — THE LAST SEAT E1. Loudness by MEASUREMENT (loudnorm analysis on
the joined intermediate), applied as pure gain (dynamics untouched), then
ONE uninterrupted master encode from work/joined.mp4 with the frame-exact
guards the E2 race lesson bought: trim=end_frame=1440 on video, atrim on
audio, -t 60. Then a CRF-23 video-only control encode of the same chain —
the CRF-18 proof on this ffmpeg is the size differential (the SEI string
reads 23.0 regardless; AGENTS.md 2026-11-15)."""
import subprocess, json, sys, re

JOINED = "work/joined.mp4"
MASTER = "masters/E1_the-last-seat_MASTER.mp4"
CONTROL = "work/qc/master_crf23.mp4"

def measure(path):
    r = subprocess.run(["ffmpeg", "-i", path, "-vn", "-af", "loudnorm=print_format=json",
                        "-f", "null", "-"], capture_output=True, text=True)
    m = re.search(r"\{[^}]*\"input_i\"[^}]*\}", r.stderr, re.S)
    d = json.loads(m.group(0))
    return float(d["input_i"]), float(d["input_tp"])

I, TP = measure(JOINED)
gain = min(-16.0 - I, -1.0 - TP)
print(f"joined: I={I:.2f} LUFS TP={TP:.2f} dBTP -> pure gain {gain:+.2f} dB")

def encode(crf, out, video_only=False):
    cmd = ["ffmpeg", "-v", "error", "-y", "-i", JOINED,
           "-vf", "trim=end_frame=1440,setpts=N/(24*TB)"]
    if video_only:
        cmd += ["-an"]
    else:
        cmd += ["-af", f"volume={gain:.2f}dB,atrim=0:60,asetpts=N/SR/TB",
                "-c:a", "aac", "-ar", "48000", "-ac", "2"]
    cmd += ["-c:v", "libx264", "-crf", str(crf), "-pix_fmt", "yuv420p", "-r", "24",
            "-movflags", "+faststart", "-t", "60", out]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr[-3000:]); sys.exit(1)
    print("encoded", out)

encode(18, MASTER)
encode(23, CONTROL, video_only=True)
I2, TP2 = measure(MASTER)
print(f"master: I={I2:.2f} LUFS TP={TP2:.2f} dBTP")
