#!/bin/bash
# MV-34 master encode: ONE uninterrupted encode from work/joined.mp4.
# Master: CRF 18 medium, AAC 48k from track.mp3 (sole master audio),
# mov_text from lyrics.srt, burned-in karaoke ASS + ~ WuBu ~ bug,
# faststart. CRF-23 twin of the SAME joined file (video only) for the
# CRF proof by size differential (this VM's ffmpeg stamps crf=23.0 in
# the SEI regardless -- the SEI is never cited). Chat copy <=50MB
# under a fresh name.
set -e
P=~/workspace/wubutv-network/musicvideo/MV-34_jensens-back
A=$P/work/assembly
mkdir -p $P/masters
BUG="drawtext=text='\\~ WuBu \\~':fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf:fontsize=28:fontcolor=0xFFD700:borderw=2:bordercolor=black:x=w-tw-18:y=h-th-14"
VF="ass=$A/captions_karaoke.ass,$BUG"

echo "=== master CRF18 $(date -u +%H:%M:%SZ)"
ffmpeg -y -v error -i $P/work/joined.mp4 -i $P/track.mp3 -i $A/lyrics.srt \
  -map 0:v:0 -map 1:a:0 -map 2:s:0 -vf "$VF" \
  -c:v libx264 -preset medium -crf 18 -r 24 \
  -c:a aac -b:a 192k -ar 48000 -ac 2 -c:s mov_text \
  -movflags +faststart $P/masters/mv34_jensens-back_16x9.mp4
echo "=== twin CRF23 $(date -u +%H:%M:%SZ)"
ffmpeg -y -v error -i $P/work/joined.mp4 -vf "$VF" -an \
  -c:v libx264 -preset medium -crf 23 -r 24 $A/master_crf23.mp4
echo "=== sizes"
ls -la $P/masters/mv34_jensens-back_16x9.mp4 $A/master_crf23.mp4
MSZ=$(stat -c%s $P/masters/mv34_jensens-back_16x9.mp4)
if [ "$MSZ" -gt 50000000 ]; then
  echo "=== chat copy (master ${MSZ} > 50MB)"
  ffmpeg -y -v error -i $P/masters/mv34_jensens-back_16x9.mp4 \
    -c:v libx264 -preset medium -b:v 1350k -maxrate 1500k -bufsize 3000k \
    -c:a copy -c:s copy -movflags +faststart \
    $P/masters/mv34_jensens-back_16x9_50mb.mp4
  ls -la $P/masters/mv34_jensens-back_16x9_50mb.mp4
else
  echo "=== chat copy (master ${MSZ} <= 50MB: byte copy, fresh name)"
  cp $P/masters/mv34_jensens-back_16x9.mp4 $P/masters/mv34_jensens-back_16x9_chat.mp4
  ls -la $P/masters/mv34_jensens-back_16x9_chat.mp4
fi
echo "ENCODE_DONE $(date -u +%H:%M:%SZ)"
