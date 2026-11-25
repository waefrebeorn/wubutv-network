#!/bin/bash
set -e
P=/home/hatch/workspace/wubutv-network/musicvideo/MV-34_jensens-back
A=$P/work/assembly
BUG="drawtext=text='\\~ WuBu \\~':fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf:fontsize=28:fontcolor=0xFFD700:borderw=2:bordercolor=black:x=w-tw-18:y=h-th-14"
VF="ass=$A/captions_karaoke.ass,$BUG"
echo "=== twin CRF23 $(date -u +%H:%M:%SZ)"
ffmpeg -y -v error -i $P/work/joined.mp4 -vf "$VF" -an \
  -c:v libx264 -preset medium -crf 23 -r 24 $A/master_crf23.mp4
echo "=== chat copy (master <= 50MB: byte copy, fresh name)"
cp $P/masters/mv34_jensens-back_16x9.mp4 $P/masters/mv34_jensens-back_16x9_chat.mp4
ls -la $P/masters/ $A/master_crf23.mp4
echo "FINISH_DONE $(date -u +%H:%M:%SZ)"
