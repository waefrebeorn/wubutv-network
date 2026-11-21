#!/bin/bash
# THE NIGHT LIST E2 — V3 U6 conform edit (replacement finisher).
# Plan logged in GATE_LOG (U6 V3 CONFORM PLAN): A held freeze
# 52f | B take f52-83 | C take f96-161 | D final plate 36f |
# E take f186-239. Audio: take's full 10s continuous.
set -e
EP=~/workspace/wubutv-network/new-era/morph-episodes/E2_the-night-list
cd "$EP"
ffmpeg -y -v error -i takes/u6v3b.mp4 \
  -loop 1 -framerate 24 -i work/gfx/board_v3_held.png \
  -loop 1 -framerate 24 -i work/gfx/board_v3_final.png \
  -filter_complex "\
[1:v]scale=1280:720,fps=24,trim=end_frame=52,setpts=PTS-STARTPTS,format=yuv420p[segA]; \
[0:v]scale=1280:720:force_original_aspect_ratio=increase,crop=1280:720,fps=24,trim=start_frame=52:end_frame=84,setpts=PTS-STARTPTS,format=yuv420p[segB]; \
[0:v]scale=1280:720:force_original_aspect_ratio=increase,crop=1280:720,fps=24,trim=start_frame=96:end_frame=162,setpts=PTS-STARTPTS,format=yuv420p[segC]; \
[2:v]scale=1280:720,fps=24,trim=end_frame=36,setpts=PTS-STARTPTS,format=yuv420p[segD]; \
[0:v]scale=1280:720:force_original_aspect_ratio=increase,crop=1280:720,fps=24,trim=start_frame=186:end_frame=240,setpts=PTS-STARTPTS,format=yuv420p[segE]; \
[segA][segB][segC][segD][segE]concat=n=5:v=1:a=0[vout]; \
[0:a]atrim=0:10,asetpts=PTS-STARTPTS[aout]" \
  -map "[vout]" -map "[aout]" -c:v libx264 -crf 18 -c:a aac work/u6v3_c.mp4
N=$(ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=nb_read_frames -of csv=p=0 work/u6v3_c.mp4)
echo "u6v3_c frames: $N"
[ "$N" = "240" ] || { echo "ABORT: u6v3_c != 240 frames"; exit 1; }
