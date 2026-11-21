#!/usr/bin/env bash
# MV-2 v2 assembly — window-first section-timing. NO peak warp, NO time-stretch.
# Trims only (from take start), Suno track sole master audio, captions in post,
# ~ WuBu ~ corner bug, 16:9 master + 9:16 blurred-pad reframe from the same cut.
set -euo pipefail
cd ~/workspace/wubutv-network/musicvideo/MV-2_toll-roads-are-dumb
WORK=masters_work_v2
rm -rf "$WORK"; mkdir -p "$WORK"
printf '~ WuBu ~' > "$WORK/bug.txt"

# Scene order: take file + frame count (240 = 10.000s @24fps; 192 = 8.01s)
declare -a TAKES=(
  mv2_s01_t2.mp4 mv2_s02_t3.mp4 mv2_s03_t2.mp4 mv2_s04_t3.mp4 mv2_s05_t3.mp4
  mv2_s06_t2.mp4 mv2_s07_t2.mp4 mv2_s08_t1.mp4 mv2_s09_t2.mp4 mv2_s10_t1.mp4
  mv2_s11_t2.mp4 mv2_s12_t3.mp4 mv2_s13_t2.mp4 mv2_s14_t1.mp4 mv2_s15_t2.mp4
  mv2_s16_t1.mp4 mv2_s17_t2.mp4 mv2_s18_t1.mp4 mv2_s19_t1.mp4 mv2_s20_t2.mp4
  mv2_s21_t1.mp4 mv2_s22_t1.mp4 mv2_s23_t1.mp4 mv2_s24_t1.mp4 mv2_s25_t2.mp4
  mv2_s26_t2.mp4 mv2_s27_t2.mp4
)
i=0
: > "$WORK/concat.txt"
for t in "${TAKES[@]}"; do
  i=$((i+1))
  frames=240
  if [ "$i" -eq 17 ]; then frames=192; fi
  ffmpeg -v error -i "takes/$t" \
    -vf "trim=start_frame=0:end_frame=$frames,setpts=PTS-STARTPTS" \
    -frames:v "$frames" -an -c:v libx264 -pix_fmt yuv420p -r 24 \
    "$WORK/part$(printf %02d $i).mp4"
  echo "file 'part$(printf %02d $i).mp4'" >> "$WORK/concat.txt"
done
ffmpeg -v error -f concat -safe 0 -i "$WORK/concat.txt" -c copy "$WORK/video_silent.mp4"

FONT=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf
[ -f "$FONT" ] || FONT=/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf

# 16:9 master
ffmpeg -v error -i "$WORK/video_silent.mp4" -i track.mp3 -i captions_v2.srt \
  -filter_complex "[0:v]drawtext=fontfile=$FONT:textfile=$WORK/bug.txt:fontcolor=0xFFC61E:fontsize=32:x=w-tw-24:y=h-th-20[v]" \
  -map "[v]" -map 1:a -map 2:s \
  -c:v libx264 -pix_fmt yuv420p -r 24 -c:a copy -c:s mov_text \
  -metadata:s:s:0 language=eng \
  masters/mv2_toll_roads_are_dumb_v2_16x9.mp4

# 9:16 reframe (blurred-pad) from the same silent cut
ffmpeg -v error -i "$WORK/video_silent.mp4" -i track.mp3 -i captions_v2.srt \
  -filter_complex "[0:v]split[a][b];[a]scale=720:1280:force_original_aspect_ratio=increase,crop=720:1280,gblur=sigma=20[bg];[b]scale=720:-2[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2,drawtext=fontfile=$FONT:textfile=$WORK/bug.txt:fontcolor=0xFFC61E:fontsize=32:x=w-tw-24:y=h-th-20[v]" \
  -map "[v]" -map 1:a -map 2:s \
  -c:v libx264 -pix_fmt yuv420p -r 24 -c:a copy -c:s mov_text \
  -metadata:s:s:0 language=eng \
  masters/mv2_toll_roads_are_dumb_v2_9x16.mp4

echo "ASSEMBLY DONE"
ffprobe -v error -show_entries format=duration -show_entries stream=codec_type,width,height -of default=noprint_wrappers=1 masters/mv2_toll_roads_are_dumb_v2_16x9.mp4
ffprobe -v error -show_entries format=duration -show_entries stream=codec_type,width,height -of default=noprint_wrappers=1 masters/mv2_toll_roads_are_dumb_v2_9x16.mp4
md5sum masters/mv2_toll_roads_are_dumb_v2_16x9.mp4 masters/mv2_toll_roads_are_dumb_v2_9x16.mp4
