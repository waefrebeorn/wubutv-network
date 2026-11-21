#!/bin/bash
cd /home/hatch/workspace/wubutv-network/musicvideo/MV-28_pull-me-into-your-orbit
VF="ass=work/swing/captions_karaoke.ass,drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf:text='~ WuBu ~':fontcolor=gold:fontsize=28:borderw=2:bordercolor=black@0.6:x=w-tw-18:y=h-th-14"
ffmpeg -y -loglevel error -i work/swing/joined.mp4 -i track.mp3 -i work/swing/lyrics.srt -map 0:v:0 -map 1:a:0 -map 2:0 -vf "$VF" -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p -r 24 -c:a aac -b:a 192k -ar 48000 -ac 2 -c:s mov_text -metadata:s:s:0 language=eng -movflags +faststart masters/mv28_pull-me-into-your-orbit_16x9.mp4
echo "MASTER_ENCODE_RC=$?"
ls -l masters/mv28_pull-me-into-your-orbit_16x9.mp4
echo MASTER_ONLY_DONE
