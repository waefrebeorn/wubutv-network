#!/bin/bash
# HOLD ON E3 PART 2 — conform segments (Part 1 method):
# each accepted take -> 1280x720, 24fps, exactly 240 frames,
# PIL chalk plate composited, audio trimmed to 10.000s @48k.
# U6: picture held from 7.5s (post freeze; lines end ~5.96s),
# plates switch U6a_t (0-4.5s) -> U6b_t (4.5-7.5s) -> freeze.
set -e
cd ~/workspace/wubutv-network/new-era/morph-episodes/E3_hold-on
A=work/assembly_part2
T=takes_part2

seg() { # $1 unit, $2 take, $3 plate
  ffmpeg -nostdin -v error -y -i $T/$2.mp4 -loop 1 -t 10 -i $A/$3 \
    -filter_complex "[0:v]scale=1280:720,fps=24,trim=end_frame=240,setpts=N/(24*TB)[v0];[1:v]format=rgba[p];[v0][p]overlay=0:0,trim=end_frame=240,setpts=N/(24*TB),format=yuv420p[v];[0:a]atrim=0:10,asetpts=N/SR/TB,aresample=48000[a]" \
    -map "[v]" -map "[a]" -c:v libx264 -preset medium -crf 10 -c:a aac -b:a 192k $A/seg_$1.mp4
  echo "built seg_$1"
}

seg U1 U1_t1 plate_U1.png
seg U2 U2_t1 plate_U2_t.png
seg U3 U3_t1 plate_U3_t.png
seg U4 U4_t1 plate_U4_t.png
seg U5 U5_t1 plate_U5_t.png

# U6: trim picture to 7.5s, clone-freeze to 10s; three plates.
ffmpeg -nostdin -v error -y -i $T/U6_t4.mp4 \
  -loop 1 -t 10 -i $A/plate_U6a_t.png \
  -loop 1 -t 10 -i $A/plate_U6b_t.png \
  -loop 1 -t 10 -i $A/plate_U6freeze_t.png \
  -filter_complex "[0:v]scale=1280:720,fps=24,trim=0:7.5,setpts=N/(24*TB),tpad=stop_mode=clone:stop_duration=2.5,trim=end_frame=240,setpts=N/(24*TB)[v0];[1:v]format=rgba[pa];[2:v]format=rgba[pb];[3:v]format=rgba[pf];[v0][pa]overlay=0:0:enable='lt(t,4.5)'[v1];[v1][pb]overlay=0:0:enable='between(t,4.5,7.5)'[v2];[v2][pf]overlay=0:0:enable='gte(t,7.5)',trim=end_frame=240,setpts=N/(24*TB),format=yuv420p[v];[0:a]atrim=0:10,asetpts=N/SR/TB,aresample=48000[a]" \
  -map "[v]" -map "[a]" -c:v libx264 -preset medium -crf 10 -c:a aac -b:a 192k $A/seg_U6.mp4
echo "built seg_U6"

for u in U1 U2 U3 U4 U5 U6; do
  ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=nb_read_frames -show_entries format=duration -of csv $A/seg_$u.mp4
done
