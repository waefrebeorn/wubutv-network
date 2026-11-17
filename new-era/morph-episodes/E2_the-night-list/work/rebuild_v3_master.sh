#!/bin/bash
# Rebuild after the U1 refire: conform u1v3b -> u1v3_c (240f),
# concat -> joined_v3 (probe == 1440f), ONE master encode with
# the aresample=48000 fix, CRF-23 differential, final probe.
set -e
EP=~/workspace/wubutv-network/new-era/morph-episodes/E2_the-night-list
cd "$EP"
ffmpeg -y -v error -i takes/u1v3b.mp4 \
  -vf "scale=1280:720:force_original_aspect_ratio=increase,crop=1280:720,fps=24,trim=end_frame=240,setpts=PTS-STARTPTS" \
  -af "atrim=0:10,asetpts=PTS-STARTPTS" -c:v libx264 -crf 18 -c:a aac work/u1v3_c.mp4
N1=$(ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=nb_read_frames -of csv=p=0 work/u1v3_c.mp4)
echo "u1v3_c frames: $N1"; [ "$N1" = "240" ] || { echo ABORT; exit 1; }
printf "file 'u1v3_c.mp4'\nfile 'u2v3_c.mp4'\nfile 'u3v3_c.mp4'\nfile 'u4v3_c.mp4'\nfile 'u5v3_c.mp4'\nfile 'u6v3_c.mp4'\n" > work/concat_v3.txt
ffmpeg -y -v error -f concat -safe 0 -i work/concat_v3.txt -c copy work/joined_v3.mp4
N=$(ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=nb_read_frames -of csv=p=0 work/joined_v3.mp4)
echo "joined_v3 frames: $N"; [ "$N" = "1440" ] || { echo ABORT; exit 1; }
ffmpeg -y -v error -i work/joined_v3.mp4 -i work/gfx/bug.png \
  -f lavfi -i "anoisesrc=d=0.09:c=white:r=48000" -f lavfi -i "sine=frequency=72:d=0.16:r=48000" \
  -filter_complex "\
[0:v]setpts=N/(24*TB)[v0]; \
[v0][1:v]overlay=W-w-24:H-h-18[vout]; \
[2:a]bandpass=f=3400:w=1400,volume=1.10,atrim=0:0.09,adelay=250|250[snap]; \
[3:a]volume=0.95,afade=t=out:st=0.02:d=0.14,adelay=250|250[thump]; \
[0:a]atrim=0:60,asetpts=PTS-STARTPTS,loudnorm=I=-16:TP=-1.5:LRA=11[base]; \
[base][snap][thump]amix=inputs=3:duration=first:normalize=0,aresample=48000[aout]" \
  -map "[vout]" -map "[aout]" -frames:v 1440 -c:v libx264 -crf 18 -preset medium \
  -c:a aac -b:a 160k -movflags +faststart masters/E2_the-night-list_v3.mp4
ffmpeg -y -v error -i work/joined_v3.mp4 -vf "setpts=N/(24*TB)" -frames:v 1440 \
  -c:v libx264 -crf 23 -preset medium -an work/master_v3_crf23.mp4
echo "master bytes: $(stat -c%s masters/E2_the-night-list_v3.mp4)  crf23 bytes: $(stat -c%s work/master_v3_crf23.mp4)"
ffprobe -v error -count_frames -show_entries stream=codec_name,width,height,r_frame_rate,nb_read_frames,sample_rate -show_entries format=duration,size -of default=noprint_wrappers=1 masters/E2_the-night-list_v3.mp4
md5sum masters/E2_the-night-list_v3.mp4
