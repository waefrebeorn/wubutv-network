#!/bin/bash
# Delivery copy of the MV-6 master, capped at 50 MB for chat sending.
# Same cut, same 228.817s, same AAC audio stream copied untouched.
# Video: 2-pass x264, target 1450 kbps (~47 MB total with 196k audio).
set -e
cd ~/workspace/wubutv-network/musicvideo/MV-6_sell-the-lemons
SRC=masters/mv6_sell_the_lemons_16x9.mp4
OUT=masters/mv6_sell_the_lemons_16x9_50mb.mp4
LOG=work/fix_2026-11-06/encode_50mb.log
: > "$LOG"
ffmpeg -y -v error -i "$SRC" -c:v libx264 -preset medium -b:v 1450k -maxrate 2200k -bufsize 2900k -pix_fmt yuv420p -pass 1 -an -f null /dev/null >>"$LOG" 2>&1
ffmpeg -y -v error -i "$SRC" -c:v libx264 -preset medium -b:v 1450k -maxrate 2200k -bufsize 2900k -pix_fmt yuv420p -pass 2 -c:a copy -movflags +faststart "$OUT" >>"$LOG" 2>&1
rm -f ffmpeg2pass-0.log ffmpeg2pass-0.log.mbtree
ls -l "$OUT" >>"$LOG"
echo "rc=0" > work/fix_2026-11-06/encode_50mb.done
