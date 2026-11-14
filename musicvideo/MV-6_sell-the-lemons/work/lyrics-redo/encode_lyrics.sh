#!/bin/bash
# Re-encode MV-6 with the redone kinetic layer: caption-free concat.mp4 video
# + new .ass burned in, base-master AAC copied untouched.
cd ~/workspace/wubutv-network/musicvideo/MV-6_sell-the-lemons
ffmpeg -y -i work/assembly/concat.mp4 -i masters/mv6_sell_the_lemons_16x9.mp4 \
  -filter_complex "[0:v]ass=work/lyrics-redo/mv6_kinetic_redo.ass[v]" \
  -map "[v]" -map 1:a \
  -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p -threads 6 \
  -c:a copy -movflags +faststart \
  masters/mv6_sell_the_lemons_16x9_lyrics.mp4 2>&1
echo "ENCODE RC=$?"
