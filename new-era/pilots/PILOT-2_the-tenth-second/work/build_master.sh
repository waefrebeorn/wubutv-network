#!/bin/bash
# PILOT-2 assembly — ONE pass owns joined.mp4. Run once, in full.
set -e
cd ~/workspace/wubutv-network/new-era/pilots/PILOT-2_the-tenth-second
T=takes
declare -A F=( [U1]=media-generation-u1-0-08c02770-9d45-4edd-94da-0d63b610234d [U2]=media-generation-u2-0-35c160cc-91d2-4c14-85ac-4dadc3201884 [U3]=media-generation-u3-0-deae44c9-3f86-43b3-a126-1a8bdb186a4a [U4]=media-generation-u4-0-443f29ad-384e-42a9-b369-bf2a3ae91930 [U5]=media-generation-u5-0-cba3930b-0108-4670-9e9d-590632c0b196 [U6]=media-generation-u6-0-2eeb41e8-3a6e-4053-92f8-0ef2d17f56b6 )
mkdir -p work/segments
VF="scale=1280:720:flags=lanczos,fps=24,format=yuv420p"
# U1-U4, U6: straight normalize, exactly 240 frames
for u in U1 U2 U3 U4 U6; do
  [ -f work/segments/seg_$u.mp4 ] || ffmpeg -y -loglevel error -i $T/${F[$u]}.mp4 -vf "$VF" -frames:v 240 \
    -c:v libx264 -preset medium -crf 16 -c:a aac -ar 48000 -ac 2 -b:a 160k work/segments/seg_$u.mp4
done
# U5: trim the studio-anchor head frames (0.25s), stretch 234f -> 240f (1.0256x)
# setpts MUST precede fps=24 so the fps stage duplicates frames to fill the
# stretched duration (attempt 1 put fps first and produced 234f -> joined 1434f,
# caught by the joined probe gate and discarded before shipping).
ffmpeg -y -loglevel error -ss 0.25 -i $T/${F[U5]}.mp4 -vf "scale=1280:720:flags=lanczos,setpts=PTS*1.025641,fps=24,format=yuv420p" -frames:v 240 \
  -c:v libx264 -preset medium -crf 16 -c:a aac -ar 48000 -ac 2 -b:a 160k -af "atempo=0.975" work/segments/seg_U5.mp4
N5=$(ffprobe -v error -select_streams v:0 -count_frames -show_entries stream=nb_read_frames -of csv=p=0 work/segments/seg_U5.mp4)
echo "seg_U5 frames: $N5"; [ "$N5" = "240" ] || { echo "SEG_U5 FRAME GATE FAIL"; exit 1; }
# joined (the one assembly pass)
printf "file 'seg_U1.mp4'\nfile 'seg_U2.mp4'\nfile 'seg_U3.mp4'\nfile 'seg_U4.mp4'\nfile 'seg_U5.mp4'\nfile 'seg_U6.mp4'\n" > work/segments/list.txt
ffmpeg -y -loglevel error -f concat -safe 0 -i work/segments/list.txt -c copy work/joined.mp4
echo "JOINED PROBE:"
NJ=$(ffprobe -v error -select_streams v:0 -count_frames -show_entries stream=nb_read_frames -of csv=p=0 work/joined.mp4)
echo "joined frames: $NJ"; [ "$NJ" = "1440" ] || { echo "JOINED FRAME GATE FAIL"; exit 1; }
# master: CRF 18 + ~ WuBu ~ bug, faststart
printf '~ WuBu ~' > work/bug.txt
ffmpeg -y -loglevel error -i work/joined.mp4 -vf "drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf:textfile=work/bug.txt:fontsize=26:fontcolor=0xFFCF3F:borderw=2:bordercolor=black@0.55:x=w-tw-22:y=h-th-18" \
  -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p -c:a copy -movflags +faststart masters/pilot2_the-tenth-second_16x9.mp4
# chat copy: video capped, audio copied from master
ffmpeg -y -loglevel error -i masters/pilot2_the-tenth-second_16x9.mp4 -c:v libx264 -preset medium -crf 26 -maxrate 5M -bufsize 10M -c:a copy -movflags +faststart masters/pilot2_the-tenth-second_chat.mp4
echo "MASTER PROBE:"
ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=nb_read_frames,width,height,r_frame_rate -of csv=p=0 masters/pilot2_the-tenth-second_16x9.mp4
ls -la masters/
md5sum masters/*.mp4
strings masters/pilot2_the-tenth-second_16x9.mp4 | grep -o "crf=[0-9.]*" | head -1
