#!/usr/bin/env bash
# Build the cut: frames + audio -> h264/aac, then verify the delivered numbers.
set -euo pipefail
cd "$(dirname "$0")"

OUT=${1:-THE_LAMP_v2.mp4}

ffmpeg -y -v error -framerate 24 -start_number 0 -i frames/f_%04d.png \
       -i audio.wav \
       -c:v libx264 -preset slow -crf 19 -pix_fmt yuv420p -tune film \
       -c:a aac -b:a 160k -shortest -movflags +faststart "$OUT"

echo "--- delivered ---"
ffprobe -v error -show_entries stream=codec_name,width,height,avg_frame_rate \
        -show_entries format=duration,size -of default=nw=1 "$OUT"
