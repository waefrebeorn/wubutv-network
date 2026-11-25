#!/bin/bash
set -e
cd ~/workspace/wubutv-network/musicvideo/MV-15_unread-dms
for s in S01 S02 S03 S04 S05 S06 S07 S08 S09 S10 S11 S12 S13 S14 S15 S16 S17 S18 S19 S20 S21 S22 S23 S24; do echo "file '$(pwd)/work/conformed/$s.mp4'"; done > work/concat_list.txt
# PASS 1: pre-grain picture (glitch hits + kinetic ASS + grade + vignette), video only, CRF18 medium
ffmpeg -v error -y -f concat -safe 0 -i work/concat_list.txt -vf "rgbashift=rh=10:gh=-8:bh=6:enable='between(t,13.51,13.63)+between(t,14.31,14.43)+between(t,15.91,16.03)+between(t,16.71,16.83)+between(t,17.51,17.63)+between(t,57.04,57.16)+between(t,59.04,59.16)+between(t,146.64,146.76)',hue=h='if(between(t,124.72,124.97)+between(t,125.76,126.01)+between(t,127.66,127.91)+between(t,128.18,128.43),160,0)',subtitles=work/overlays/kinetic.ass,eq=saturation=0.88,vignette=PI/5,format=yuv420p" -c:v libx264 -preset medium -crf 18 -r 24 work/master_pregrain.mp4
echo "pass1 done"
# PASS 2: shipped master = pregrain + house grain + track audio as AAC
ffmpeg -v error -y -i work/master_pregrain.mp4 -i track.mp3 -map 0:v -map 1:a -vf "noise=alls=13:allf=t+u,format=yuv420p" -c:v libx264 -preset medium -crf 18 -r 24 -c:a aac -b:a 192k -ar 48000 -movflags +faststart masters/mv15_unread_dms_16x9.mp4
echo "pass2 done"
