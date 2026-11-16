#!/bin/bash
# THE NIGHT LIST E1 — assembly. House pattern (E2_SHOW-3 recovery):
# conform each unit to exactly 240f -> concat -> probe joined == 1440f ->
# ONE uninterrupted master encode -> re-probe end to end.
# Expects takes/u1.mp4 .. takes/u6.mp4 (raw generator output).
set -e
EP=~/workspace/wubutv-network/new-era/morph-episodes/E1_the-night-list
cd "$EP"
mkdir -p work masters

# 0. overlays (bug + question card), rendered deterministically
python3 - <<'PYEOF'
from PIL import Image, ImageDraw, ImageFont
SERIF_B = "/usr/share/fonts/truetype/noto/NotoSerif-Bold.ttf"
GOLD = (255, 210, 74, 255)
bug = Image.new("RGBA", (300, 64), (0, 0, 0, 0))
d = ImageDraw.Draw(bug)
f = ImageFont.truetype(SERIF_B, 40)
d.text((150 - d.textlength("~ WuBu ~", font=f) / 2, 8), "~ WuBu ~", font=f, fill=GOLD)
bug.save("work/gfx/bug.png")
card = Image.new("RGBA", (760, 150), (10, 10, 14, 205))
d = ImageDraw.Draw(card)
d.rectangle([0, 0, 759, 6], fill=(203, 52, 30, 255))
f2 = ImageFont.truetype(SERIF_B, 52)
t = "WHOSE NAME COMES OFF?"
d.text((380 - d.textlength(t, font=f2) / 2, 48), t, font=f2, fill=(233, 226, 206, 255))
card.save("work/gfx/question_card.png")
print("overlays rendered")
PYEOF

# 1. conform each unit to exactly 240 frames, 1280x720, 24fps
for i in 1 2 3 4 5 6; do
  ffmpeg -y -v error -i "takes/u$i.mp4" \
    -vf "scale=1280:720:force_original_aspect_ratio=increase,crop=1280:720,fps=24,trim=end_frame=240,setpts=PTS-STARTPTS" \
    -af "atrim=0:10,asetpts=PTS-STARTPTS" -c:v libx264 -crf 18 -c:a aac "work/u${i}_c.mp4"
done

# 2. concat -> joined; probe BEFORE the master encode (must be exactly 1440f)
printf "file 'u1_c.mp4'\nfile 'u2_c.mp4'\nfile 'u3_c.mp4'\nfile 'u4_c.mp4'\nfile 'u5_c.mp4'\nfile 'u6_c.mp4'\n" > work/concat.txt
ffmpeg -y -v error -f concat -safe 0 -i work/concat.txt -c copy work/joined.mp4
N=$(ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=nb_read_frames -of csv=p=0 work/joined.mp4)
echo "joined frames: $N"
[ "$N" = "1440" ] || { echo "ABORT: joined != 1440 frames"; exit 1; }

# 3. ONE uninterrupted master encode: regenerated video timeline, audio 0:60,
#    bug throughout, question card over the U6 freeze (57.0-60.0s),
#    chalk-snap accent planted at 0.25s (BLAM A3 insurance, disclosed in GATE_LOG),
#    loudness pass.
ffmpeg -y -v error -i work/joined.mp4 -i work/gfx/bug.png -i work/gfx/question_card.png \
  -f lavfi -i "anoisesrc=d=0.09:c=white:r=48000" -f lavfi -i "sine=frequency=72:d=0.16:r=48000" \
  -filter_complex "\
[0:v]setpts=N/(24*TB)[v0]; \
[v0][1:v]overlay=W-w-24:H-h-18[v1]; \
[v1][2:v]overlay=(W-w)/2:H-h-120:enable='between(t,57.0,60.0)'[vout]; \
[3:a]bandpass=f=3400:w=1400,volume=0.50,atrim=0:0.09,adelay=250|250[snap]; \
[4:a]volume=0.60,afade=t=out:st=0.02:d=0.14,adelay=250|250[thump]; \
[0:a]atrim=0:60,asetpts=PTS-STARTPTS,loudnorm=I=-16:TP=-1.5:LRA=11[base]; \
[base][snap][thump]amix=inputs=3:duration=first:normalize=0[aout]" \
  -map "[vout]" -map "[aout]" -frames:v 1440 -c:v libx264 -crf 18 -preset medium \
  -c:a aac -b:a 160k -movflags +faststart masters/E1_the-night-list.mp4

# 4. CRF-18 proof: size differential vs a CRF-23 encode of the same chain
ffmpeg -y -v error -i work/joined.mp4 -vf "setpts=N/(24*TB)" -frames:v 1440 \
  -c:v libx264 -crf 23 -preset medium -an work/master_crf23.mp4
echo "master bytes: $(stat -c%s masters/E1_the-night-list.mp4)  crf23 bytes: $(stat -c%s work/master_crf23.mp4)"

# 5. chat copy only if the house master exceeds 50 MB (bitrate-capped, audio copied)
SZ=$(stat -c%s masters/E1_the-night-list.mp4)
if [ "$SZ" -gt 52428800 ]; then
  ffmpeg -y -v error -i masters/E1_the-night-list.mp4 -c:v libx264 -b:v 5600k -preset medium \
    -c:a copy -movflags +faststart masters/E1_the-night-list_chat.mp4
  echo "chat copy: $(stat -c%s masters/E1_the-night-list_chat.mp4) bytes"
fi

# 6. final probe, end to end
ffprobe -v error -count_frames -show_entries stream=codec_name,width,height,r_frame_rate,nb_read_frames -show_entries format=duration,size -of default=noprint_wrappers=1 masters/E1_the-night-list.mp4
md5sum masters/E1_the-night-list.mp4
