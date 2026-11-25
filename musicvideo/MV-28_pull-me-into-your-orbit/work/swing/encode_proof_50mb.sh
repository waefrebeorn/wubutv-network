#!/bin/bash
cd /home/hatch/workspace/wubutv-network/musicvideo/MV-28_pull-me-into-your-orbit
VF="ass=work/swing/captions_karaoke.ass,drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf:text='~ WuBu ~':fontcolor=gold:fontsize=28:borderw=2:bordercolor=black@0.6:x=w-tw-18:y=h-th-14"
ffmpeg -y -loglevel error -i work/swing/joined.mp4 -vf "$VF" -an -c:v libx264 -preset medium -crf 23 -pix_fmt yuv420p -r 24 work/swing/master_crf23.mp4
echo "CRF23_RC=$?"
ffmpeg -y -loglevel error -i masters/mv28_pull-me-into-your-orbit_16x9.mp4 -c:v libx264 -preset medium -b:v 1350k -maxrate 1500k -bufsize 3000k -c:a copy -c:s copy -movflags +faststart masters/mv28_pull-me-into-your-orbit_16x9_50mb.mp4
echo "MB50_RC=$?"
ls -l work/swing/master_crf23.mp4 masters/mv28_pull-me-into-your-orbit_16x9_50mb.mp4
echo PROOF_50MB_DONE
