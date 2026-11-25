#!/bin/bash
# THE NIGHT LIST E2 — V3 assembly (repair finisher, 2026-11-17).
# Script-level repair round v3 build: refired U1,U2,U3,U4,U5,U6
# (all six lines/picture per SCRIPT.md repair round v3 round 2).
# Conforms each unit to exactly 240f -> U6 conform edit (GAP-3
# freeze + final plate, boundaries set from the U6v3 frame map)
# -> concat -> probe joined_v3 == 1440f BEFORE the encode ->
# ONE uninterrupted master encode to the FRESH filename
# masters/E2_the-night-list_v3.mp4 -> CRF-23 differential ->
# final probe. Mirrors assemble_repair.sh's chain exactly.
set -e
EP=~/workspace/wubutv-network/new-era/morph-episodes/E2_the-night-list
cd "$EP"
mkdir -p work masters

conform() { # $1 = take path, $2 = out conform
  ffmpeg -y -v error -i "$1" \
    -vf "scale=1280:720:force_original_aspect_ratio=increase,crop=1280:720,fps=24,trim=end_frame=240,setpts=PTS-STARTPTS" \
    -af "atrim=0:10,asetpts=PTS-STARTPTS" -c:v libx264 -crf 18 -c:a aac "$2"
  N=$(ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=nb_read_frames -of csv=p=0 "$2")
  echo "$2 frames: $N"
  [ "$N" = "240" ] || { echo "ABORT: $2 != 240 frames"; exit 1; }
}

# 1. straight conforms U1,U2,U4,U5 (240f each)
conform takes/u1v3.mp4 work/u1v3_c.mp4
conform takes/u2v3.mp4 work/u2v3_c.mp4
conform takes/u4v3b.mp4 work/u4v3_c.mp4
conform takes/u5v3.mp4 work/u5v3_c.mp4

# 1b. U3v3 SPLICE CONFORM (finisher): the raw take speaks its
# line twice; the repeat (ASR ~6.9-8.6s, garbled tail) is cut
# from BOTH streams. Video: frames 0-162 + 208-239 (=195f) +
# cloned hold of the last frame x45 = 240f. Audio: 0-6.792s +
# two DISTINCT speech-free ambience spans of the take itself
# (8.667-10s, then 4.9-6.775s) crossfaded to 10.000s. (An
# earlier looped-ambience fill made the ASR hallucinate an
# unscripted "I'm sorry" over the loop seam; the two-span
# fill ASRs clean — do not re-loop.)
ffmpeg -y -v error -i takes/u3v3.mp4 -filter_complex \
 "[0:v]scale=1280:720:force_original_aspect_ratio=increase,crop=1280:720,fps=24,split[v1][v2];[v1]trim=start_frame=0:end_frame=163,setpts=PTS-STARTPTS[va];[v2]trim=start_frame=208:end_frame=240,setpts=PTS-STARTPTS[vb];[va][vb]concat=n=2:v=1:a=0,tpad=stop_mode=clone:stop_duration=1.875,trim=end_frame=240,format=yuv420p[vout];[0:a]asplit=3[a1][a2][a3];[a1]atrim=0:6.792,asetpts=PTS-STARTPTS[aa];[a2]atrim=8.667:10,asetpts=PTS-STARTPTS[ab];[a3]atrim=4.9:6.775,asetpts=PTS-STARTPTS[ac];[aa][ab]acrossfade=d=0.05[ax];[ax][ac]acrossfade=d=0.05,apad=whole_dur=10[aout]" \
 -map "[vout]" -map "[aout]" -t 10 -c:v libx264 -crf 18 -c:a aac work/u3v3_c.mp4
N=$(ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=nb_read_frames -of csv=p=0 work/u3v3_c.mp4)
echo "work/u3v3_c.mp4 frames: $N"
[ "$N" = "240" ] || { echo "ABORT: u3v3_c != 240 frames"; exit 1; }

# 2. U6 conform edit — PLACEHOLDER boundaries, finalized from the
#    U6v3 frame map in GATE_LOG (finisher's U6 V3 CONFORM PLAN):
#    A board_v3_held freeze 52f (GAP 3) | B take writing span |
#    C take bed/entrance span | D board_v3_final plate 36f |
#    E take tail (line + hold). Audio: take's full 10s continuous.
#    (filter graph written by assemble_v3_u6.sh at build time.)

# 3. concat -> joined_v3; probe BEFORE the master encode (== 1440f)
printf "file 'u1v3_c.mp4'\nfile 'u2v3_c.mp4'\nfile 'u3v3_c.mp4'\nfile 'u4v3_c.mp4'\nfile 'u5v3_c.mp4'\nfile 'u6v3_c.mp4'\n" > work/concat_v3.txt
ffmpeg -y -v error -f concat -safe 0 -i work/concat_v3.txt -c copy work/joined_v3.mp4
N=$(ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=nb_read_frames -of csv=p=0 work/joined_v3.mp4)
echo "joined_v3 frames: $N"
[ "$N" = "1440" ] || { echo "ABORT: joined_v3 != 1440 frames"; exit 1; }

# 4. ONE uninterrupted master encode (assemble.sh step 3 chain, fresh name)
ffmpeg -y -v error -i work/joined_v3.mp4 -i work/gfx/bug.png \
  -f lavfi -i "anoisesrc=d=0.09:c=white:r=48000" -f lavfi -i "sine=frequency=72:d=0.16:r=48000" \
  -filter_complex "\
[0:v]setpts=N/(24*TB)[v0]; \
[v0][1:v]overlay=W-w-24:H-h-18[vout]; \
[2:a]bandpass=f=3400:w=1400,volume=1.10,atrim=0:0.09,adelay=250|250[snap]; \
[3:a]volume=0.95,afade=t=out:st=0.02:d=0.14,adelay=250|250[thump]; \
[0:a]atrim=0:60,asetpts=PTS-STARTPTS,loudnorm=I=-16:TP=-1.5:LRA=11[base]; \
[base][snap][thump]amix=inputs=3:duration=first:normalize=0[aout]" \
  -map "[vout]" -map "[aout]" -frames:v 1440 -c:v libx264 -crf 18 -preset medium \
  -c:a aac -b:a 160k -movflags +faststart masters/E2_the-night-list_v3.mp4

# 5. CRF-18 proof: size differential vs a CRF-23 encode of the same chain
ffmpeg -y -v error -i work/joined_v3.mp4 -vf "setpts=N/(24*TB)" -frames:v 1440 \
  -c:v libx264 -crf 23 -preset medium -an work/master_v3_crf23.mp4
echo "master bytes: $(stat -c%s masters/E2_the-night-list_v3.mp4)  crf23 bytes: $(stat -c%s work/master_v3_crf23.mp4)"

# 6. final probe, end to end
ffprobe -v error -count_frames -show_entries stream=codec_name,width,height,r_frame_rate,nb_read_frames,sample_rate -show_entries format=duration,size -of default=noprint_wrappers=1 masters/E2_the-night-list_v3.mp4
md5sum masters/E2_the-night-list_v3.mp4
