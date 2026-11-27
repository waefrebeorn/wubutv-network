#!/bin/bash
# MV-29 master encode: house master (CRF 18, burned-in karaoke subs,
# ~ WuBu ~ corner bug, mov_text track, track.mp3 sole audio) + CRF-23
# size-differential proof twin + _50mb sibling (chat copy).
# Adapted from MV-28's encode_master.sh.
set -e
cd ~/workspace/wubutv-network/musicvideo/MV-29_dario-belongs-in-the-rubber-room
VF="ass=work/swing/captions_karaoke.ass,drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf:text='~ WuBu ~':fontcolor=gold:fontsize=28:borderw=2:bordercolor=black@0.6:x=w-tw-18:y=h-th-14"
MASTER=masters/mv29_dario-belongs-in-the-rubber-room_16x9.mp4
ffmpeg -nostdin -v error -y -i work/swing/joined.mp4 -i track.mp3 -i work/swing/lyrics.srt \
  -filter_complex "[0:v]${VF}[v]" -map "[v]" -map 1:a -map 2:s \
  -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p -r 24 \
  -c:a aac -b:a 192k -ar 48000 -ac 2 \
  -c:s mov_text -metadata:s:s:0 language=eng \
  -movflags +faststart "$MASTER"
echo "MASTER DONE: $MASTER"
ffmpeg -nostdin -v error -y -i work/swing/joined.mp4 \
  -vf "$VF" -an -c:v libx264 -preset medium -crf 23 -pix_fmt yuv420p -r 24 \
  work/swing/master_crf23.mp4
echo "CRF23 TWIN DONE"
SIBLING=masters/mv29_dario-belongs-in-the-rubber-room_16x9_50mb.mp4
ffmpeg -nostdin -v error -y -i "$MASTER" \
  -c:v libx264 -preset medium -b:v 1350k -maxrate 1500k -bufsize 3000k \
  -pix_fmt yuv420p -r 24 -c:a copy -c:s copy -movflags +faststart "$SIBLING"
echo "50MB SIBLING DONE: $SIBLING"
ls -la masters/ work/swing/master_crf23.mp4
