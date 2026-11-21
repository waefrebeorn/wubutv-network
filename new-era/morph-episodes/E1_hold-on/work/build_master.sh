#!/bin/bash
# HOLD ON E1 assembly: segments (with chalk inserts cut in, picture-only,
# take audio continuous) -> joined.mp4 -> master (clock overlay + bug +
# loudness). ONE assembly pass owns joined.mp4.
set -euo pipefail
cd "$(dirname "$0")/.."
EP=$PWD
SEG=work/segments
mkdir -p "$SEG" masters

SCALE="scale=1280:720:flags=lanczos,fps=24,format=yuv420p"

plain_seg () { # $1 take, $2 out
  ffmpeg -v error -y -i "$1" -vf "$SCALE" -frames:v 240 \
    -c:v libx264 -crf 10 -c:a copy "$2"
}

insert_seg () { # $1 take, $2 insdir, $3 start_frame, $4 end_frame(excl), $5 out
  ffmpeg -v error -y -i "$1" -framerate 24 -i "$2/f%03d.png" -filter_complex \
    "[0:v]${SCALE},trim=start_frame=0:end_frame=$3,setpts=PTS-STARTPTS[a];[0:v]${SCALE},trim=start_frame=$4:end_frame=240,setpts=PTS-STARTPTS[b];[1:v]format=yuv420p[ins];[a][ins][b]concat=n=3:v=1:a=0[v]" \
    -map "[v]" -map 0:a -c:v libx264 -crf 10 -c:a copy "$5"
}

# insert windows (frames @24fps), keyed to measured ASR:
# U1: 92-122 (after Rosa line1 ends 3.80s, before Laura 5.36s)
# U5: 82-129 (after "Line nine." ends 3.40s; reveal line runs under it)
# U6: 100-135 (silent writing beat, Laura line ends 3.96s, Rosa 7.14s)
insert_seg takes/U1_t1.mp4 work/gfx/inserts/ins_u1 92 123 "$SEG/seg1.mp4"
plain_seg  takes/U2_t1.mp4 "$SEG/seg2.mp4"
plain_seg  takes/U3_t1.mp4 "$SEG/seg3.mp4"
plain_seg  takes/U4_t1.mp4 "$SEG/seg4.mp4"
insert_seg takes/U5_t1.mp4 work/gfx/inserts/ins_u5 82 130 "$SEG/seg5.mp4"
insert_seg takes/U6_t1.mp4 work/gfx/inserts/ins_u6 100 136 "$SEG/seg6.mp4"

for i in 1 2 3 4 5 6; do echo "file 'segments/seg$i.mp4'"; done > work/concat.txt
ffmpeg -v error -y -f concat -safe 0 -i work/concat.txt -c copy work/joined.mp4

# verify joined = segment sum before the master encode
python3 - <<'EOF'
import subprocess
def frames(p):
    out = subprocess.run(["ffprobe","-v","error","-count_frames","-select_streams","v:0",
                          "-show_entries","stream=nb_read_frames","-of","csv=p=0",p],
                         capture_output=True, text=True)
    return int(out.stdout.strip())
tot = 0
for i in range(1,7):
    n = frames(f"work/segments/seg{i}.mp4"); print(f"seg{i}: {n}"); tot += n
j = frames("work/joined.mp4")
print(f"joined: {j}  segment sum: {tot}")
assert j == tot == 1440, "FRAME COUNT MISMATCH"
EOF

# loudness: fixed gain to -20 dBFS median (100ms RMS windows), -1 dBFS limiter
GAIN=$(python3 - <<'EOF'
import subprocess, numpy as np
raw = subprocess.run(["ffmpeg","-v","error","-i","work/joined.mp4","-ac","1","-ar","48000","-f","f32le","-"], capture_output=True).stdout
a = np.frombuffer(raw, dtype=np.float32)
win = 4800; nw = len(a)//win
rms = np.sqrt((a[:nw*win].reshape(nw,win)**2).mean(axis=1)+1e-12)
med = float(np.median(20*np.log10(rms)))
print(f"{-20.0-med:.2f}")
import sys; print(f"joined median {med:.2f} dBFS", file=sys.stderr)
EOF
)
echo "loudness gain: +$GAIN dB"

FONT=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf
FILTER="[0:v][1:v]overlay=0:0[v1];[v1]drawtext=fontfile=$FONT:text='~ WuBu ~':fontsize=26:fontcolor=0xFFCF3F:borderw=2:bordercolor=black:x=w-tw-22:y=h-th-18[v];[0:a]volume=${GAIN}dB,alimiter=limit=0.89[a]"

ffmpeg -v error -y -i work/joined.mp4 -framerate 24 -i work/gfx/clock/f%04d.png \
  -filter_complex "$FILTER" -map "[v]" -map "[a]" \
  -c:v libx264 -crf 18 -preset medium -c:a aac -b:a 160k -ar 48000 -ac 2 \
  -movflags +faststart -frames:v 1440 masters/E1_hold-on_16x9.mp4

# CRF-23 differential proof (same chain)
ffmpeg -v error -y -i work/joined.mp4 -framerate 24 -i work/gfx/clock/f%04d.png \
  -filter_complex "$FILTER" -map "[v]" -map "[a]" \
  -c:v libx264 -crf 23 -preset medium -c:a aac -b:a 160k -ar 48000 -ac 2 \
  -frames:v 1440 work/master_crf23.mp4

ls -la masters/ work/master_crf23.mp4
md5sum masters/E1_hold-on_16x9.mp4
echo BUILD_OK
