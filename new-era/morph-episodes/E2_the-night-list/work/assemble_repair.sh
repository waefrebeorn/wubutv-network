#!/bin/bash
# THE NIGHT LIST E2 — REPAIR assembly (replacement repair coordinator).
# Conforms U5r, builds the U6 conform edit from U6r per the logged
# U6 CONFORM PLAN, concats with the first-pass conforms u1_c..u4_c,
# probes joined == 1440f BEFORE the encode, ONE uninterrupted master
# encode to the FRESH filename masters/E2_the-night-list_v2.mp4,
# CRF-23 differential, final probe. Mirrors assemble.sh's chain.
set -e
EP=~/workspace/wubutv-network/new-era/morph-episodes/E2_the-night-list
cd "$EP"
mkdir -p work masters

# 1. conform U5r to exactly 240 frames, 1280x720, 24fps (assemble.sh chain)
ffmpeg -y -v error -i takes/u5r.mp4 \
  -vf "scale=1280:720:force_original_aspect_ratio=increase,crop=1280:720,fps=24,trim=end_frame=240,setpts=PTS-STARTPTS" \
  -af "atrim=0:10,asetpts=PTS-STARTPTS" -c:v libx264 -crf 18 -c:a aac work/u5r_c.mp4
N5=$(ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=nb_read_frames -of csv=p=0 work/u5r_c.mp4)
echo "u5r_c frames: $N5"
[ "$N5" = "240" ] || { echo "ABORT: u5r_c != 240 frames"; exit 1; }

# 2. U6 conform edit: A held-plate freeze 52f | B take f0-35 (36f) |
#    C take f42-61 (20f) | D final-plate 36f | E take f144-239 (96f).
#    Audio: the take's full 10s, continuous (speech only at 6.2s+, in E).
ffmpeg -y -v error -i takes/u6r.mp4 \
  -loop 1 -framerate 24 -i work/gfx/board_E2_held.png \
  -loop 1 -framerate 24 -i work/gfx/board_E2_final.png \
  -filter_complex "\
[1:v]scale=1280:720,fps=24,trim=end_frame=52,setpts=PTS-STARTPTS,format=yuv420p[segA]; \
[0:v]scale=1280:720:force_original_aspect_ratio=increase,crop=1280:720,fps=24,trim=start_frame=0:end_frame=36,setpts=PTS-STARTPTS,format=yuv420p[segB]; \
[0:v]scale=1280:720:force_original_aspect_ratio=increase,crop=1280:720,fps=24,trim=start_frame=42:end_frame=62,setpts=PTS-STARTPTS,format=yuv420p[segC]; \
[2:v]scale=1280:720,fps=24,trim=end_frame=36,setpts=PTS-STARTPTS,format=yuv420p[segD]; \
[0:v]scale=1280:720:force_original_aspect_ratio=increase,crop=1280:720,fps=24,trim=start_frame=144:end_frame=240,setpts=PTS-STARTPTS,format=yuv420p[segE]; \
[segA][segB][segC][segD][segE]concat=n=5:v=1:a=0[vout]; \
[0:a]atrim=0:10,asetpts=PTS-STARTPTS[aout]" \
  -map "[vout]" -map "[aout]" -c:v libx264 -crf 18 -c:a aac work/u6r_c.mp4
N6=$(ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=nb_read_frames -of csv=p=0 work/u6r_c.mp4)
echo "u6r_c frames: $N6"
[ "$N6" = "240" ] || { echo "ABORT: u6r_c != 240 frames"; exit 1; }

# 3. concat -> joined_repair; probe BEFORE the master encode (== 1440f)
printf "file 'u1_c.mp4'\nfile 'u2_c.mp4'\nfile 'u3_c.mp4'\nfile 'u4_c.mp4'\nfile 'u5r_c.mp4'\nfile 'u6r_c.mp4'\n" > work/concat_repair.txt
ffmpeg -y -v error -f concat -safe 0 -i work/concat_repair.txt -c copy work/joined_repair.mp4
N=$(ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=nb_read_frames -of csv=p=0 work/joined_repair.mp4)
echo "joined_repair frames: $N"
[ "$N" = "1440" ] || { echo "ABORT: joined_repair != 1440 frames"; exit 1; }

# 4. ONE uninterrupted master encode (assemble.sh step 3 chain, fresh name)
ffmpeg -y -v error -i work/joined_repair.mp4 -i work/gfx/bug.png \
  -f lavfi -i "anoisesrc=d=0.09:c=white:r=48000" -f lavfi -i "sine=frequency=72:d=0.16:r=48000" \
  -filter_complex "\
[0:v]setpts=N/(24*TB)[v0]; \
[v0][1:v]overlay=W-w-24:H-h-18[vout]; \
[2:a]bandpass=f=3400:w=1400,volume=1.10,atrim=0:0.09,adelay=250|250[snap]; \
[3:a]volume=0.95,afade=t=out:st=0.02:d=0.14,adelay=250|250[thump]; \
[0:a]atrim=0:60,asetpts=PTS-STARTPTS,loudnorm=I=-16:TP=-1.5:LRA=11[base]; \
[base][snap][thump]amix=inputs=3:duration=first:normalize=0[aout]" \
  -map "[vout]" -map "[aout]" -frames:v 1440 -c:v libx264 -crf 18 -preset medium \
  -c:a aac -b:a 160k -movflags +faststart masters/E2_the-night-list_v2.mp4

# 5. CRF-18 proof: size differential vs a CRF-23 encode of the same chain
ffmpeg -y -v error -i work/joined_repair.mp4 -vf "setpts=N/(24*TB)" -frames:v 1440 \
  -c:v libx264 -crf 23 -preset medium -an work/master_v2_crf23.mp4
echo "master bytes: $(stat -c%s masters/E2_the-night-list_v2.mp4)  crf23 bytes: $(stat -c%s work/master_v2_crf23.mp4)"

# 6. final probe, end to end
ffprobe -v error -count_frames -show_entries stream=codec_name,width,height,r_frame_rate,nb_read_frames,sample_rate -show_entries format=duration,size -of default=noprint_wrappers=1 masters/E2_the-night-list_v2.mp4
md5sum masters/E2_the-night-list_v2.mp4
