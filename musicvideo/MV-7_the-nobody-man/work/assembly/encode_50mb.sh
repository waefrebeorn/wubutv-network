#!/bin/bash
# 50MB delivery encode of the MV-7 house master: same cut, video re-encoded
# 2-pass to ~1450k, AAC audio copied untouched, faststart on.
set -e
cd ~/workspace/wubutv-network/musicvideo/MV-7_the-nobody-man
M=masters/mv7_im_the_nobody_man_16x9.mp4
O=masters/mv7_im_the_nobody_man_16x9_50mb.mp4
ffmpeg -y -i "$M" -map 0:v -map 0:a -c:v libx264 -preset medium -b:v 1450k \
  -maxrate 2200k -bufsize 2900k -pass 1 -an -f null /dev/null
ffmpeg -y -i "$M" -map 0:v -map 0:a -c:v libx264 -preset medium -b:v 1450k \
  -maxrate 2200k -bufsize 2900k -pass 2 -c:a copy -movflags +faststart "$O"
echo "done: $O"
md5sum "$O"
ls -la "$O"
