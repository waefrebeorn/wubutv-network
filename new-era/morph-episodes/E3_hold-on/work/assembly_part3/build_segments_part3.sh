#!/bin/bash
# HOLD ON E3 PART 3 — conform segments (Part 2 method):
# each accepted take -> 1280x720, 24fps, exactly 240 frames,
# PIL chalk plate composited, audio trimmed to 10.000s @48k.
# U1: plate_U1a (question + YES tallies) 0-2.0s -> plate_U1b
#     (question + smear) 2.0-10s, matched to the scrape.
# U6: plate_U6a 0-3.5s -> plate_U6b (+ WATCHER true line) as
#     her writing completes; her line lands 4.75-6.07s.
# U2 is NOT built here: U2_t1 was rejected (readable generated
# lettering) and its fail-once refire is owed to a successor;
# the successor tunes plate_U2 on U2_t2 and builds seg_U2 with
# the same seg() shape before the join.
set -e
cd ~/workspace/wubutv-network/new-era/morph-episodes/E3_hold-on
A=work/assembly_part3
T=takes_part3

seg() { # $1 unit, $2 take, $3 plate
  ffmpeg -nostdin -v error -y -i $T/$2.mp4 -loop 1 -t 10 -i $A/$3 \
    -filter_complex "[0:v]scale=1280:720,fps=24,trim=end_frame=240,setpts=N/(24*TB)[v0];[1:v]format=rgba[p];[v0][p]overlay=0:0,trim=end_frame=240,setpts=N/(24*TB),format=yuv420p[v];[0:a]atrim=0:10,asetpts=N/SR/TB,aresample=48000[a]" \
    -map "[v]" -map "[a]" -c:v libx264 -preset medium -crf 10 -c:a aac -b:a 192k $A/seg_$1.mp4
  echo "built seg_$1"
}

seg U3 U3_t1 plate_U3.png
seg U4 U4_t1 plate_U4.png
seg U5 U5_t1 plate_U5.png

# U1: two wall states across the scrape
ffmpeg -nostdin -v error -y -i $T/U1_t1.mp4 \
  -loop 1 -t 10 -i $A/plate_U1a.png \
  -loop 1 -t 10 -i $A/plate_U1b.png \
  -filter_complex "[0:v]scale=1280:720,fps=24,trim=end_frame=240,setpts=N/(24*TB)[v0];[1:v]format=rgba[pa];[2:v]format=rgba[pb];[v0][pa]overlay=0:0:enable='lt(t,2.0)'[v1];[v1][pb]overlay=0:0:enable='gte(t,2.0)',trim=end_frame=240,setpts=N/(24*TB),format=yuv420p[v];[0:a]atrim=0:10,asetpts=N/SR/TB,aresample=48000[a]" \
  -map "[v]" -map "[a]" -c:v libx264 -preset medium -crf 10 -c:a aac -b:a 192k $A/seg_U1.mp4
echo "built seg_U1"

# U6: the true line appears as her writing completes (3.5s)
ffmpeg -nostdin -v error -y -i $T/U6_t1.mp4 \
  -loop 1 -t 10 -i $A/plate_U6a.png \
  -loop 1 -t 10 -i $A/plate_U6b.png \
  -filter_complex "[0:v]scale=1280:720,fps=24,trim=end_frame=240,setpts=N/(24*TB)[v0];[1:v]format=rgba[pa];[2:v]format=rgba[pb];[v0][pa]overlay=0:0:enable='lt(t,3.5)'[v1];[v1][pb]overlay=0:0:enable='gte(t,3.5)',trim=end_frame=240,setpts=N/(24*TB),format=yuv420p[v];[0:a]atrim=0:10,asetpts=N/SR/TB,aresample=48000[a]" \
  -map "[v]" -map "[a]" -c:v libx264 -preset medium -crf 10 -c:a aac -b:a 192k $A/seg_U6.mp4
echo "built seg_U6"

for u in U1 U3 U4 U5 U6; do
  echo -n "seg_$u: "
  ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=nb_read_frames -show_entries format=duration -of csv $A/seg_$u.mp4
done
