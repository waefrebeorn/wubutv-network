#!/bin/bash
set -e
cd ~/workspace/wubutv-network/musicvideo/MV-2_toll-roads-are-dumb
WORK=masters_work_v3
# 1) corrected leader hold: video-only, 7.360s frozen S01 first frame
ffmpeg -v error -y -i takes/mv2_s01_t2.mp4 -vf "trim=end_frame=1,setpts=PTS-STARTPTS,loop=loop=-1:size=1:start=0,trim=end=7.360,fps=24,format=yuv420p" -an $WORK/S01_hold.mp4
echo "hold duration:"; ffprobe -v error -show_entries stream=codec_type,duration -of csv=p=0 $WORK/S01_hold.mp4
# 2) re-concat existing segments (unchanged) + corrected hold
ffmpeg -v error -y -f concat -safe 0 -i $WORK/concat_v3.txt -c copy $WORK/video_v3_16x9.mp4
echo "video duration:"; ffprobe -v error -show_entries format=duration -of csv=p=0 $WORK/video_v3_16x9.mp4
# 3) final mux, same as script line 112
FONT=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf
ffmpeg -v error -y -i $WORK/video_v3_16x9.mp4 -i track.mp3 -i captions_v2.srt -filter_complex "[0:v]drawtext=fontfile=$FONT:text='~ WuBu ~':fontsize=32:fontcolor=0xFFC61E:x=w-tw-24:y=h-th-24:shadowcolor=0x000000:shadowx=2:shadowy=2[v]" -map "[v]" -map "1:a" -map "2:s" -c:v libx264 -crf 18 -preset medium -c:a aac -b:a 192k -ar 48000 -ac 2 -c:s mov_text -metadata:s:s:0 language=eng -movflags +faststart -t 268.01 masters/mv2_toll_roads_are_dumb_v3_16x9.mp4
echo "V3 FIX DONE"; ffprobe -v error -show_entries format=duration,size -of default=noprint_wrappers=1 masters/mv2_toll_roads_are_dumb_v3_16x9.mp4; md5sum masters/mv2_toll_roads_are_dumb_v3_16x9.mp4
