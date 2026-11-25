#!/usr/bin/env python3
"""Extract single frames from a video via ffmpeg rawvideo pipe (avoids the
image2/PNG muxer, which is currently failing with EPERM in this environment).
Usage: extract_frame.py <video> <time_s> <out_png> [width height]
"""
import subprocess, sys
from PIL import Image

video, t, out = sys.argv[1], sys.argv[2], sys.argv[3]
W, H = (int(sys.argv[4]), int(sys.argv[5])) if len(sys.argv) > 5 else (1280, 720)
cmd = ["ffmpeg", "-v", "error", "-y", "-ss", t, "-i", video,
       "-frames:v", "1", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"]
raw = subprocess.run(cmd, stdout=subprocess.PIPE, check=True).stdout
need = W * H * 3
if len(raw) < need:
    raise SystemExit(f"short read: got {len(raw)} bytes, need {need}")
Image.frombytes("RGB", (W, H), raw[:need]).save(out)
print(f"wrote {out} ({len(raw)} bytes raw)")
