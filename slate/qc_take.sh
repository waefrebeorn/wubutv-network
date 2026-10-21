#!/usr/bin/env bash
# QC helper: specs, decode errors, tiles, audio profile.
# usage: qc_take.sh <take.mp4> <prefix>
set -u
TAKE="$1"; PRE="$2"
DIR="$(dirname "$TAKE")"

echo "== SPECS =="
ffprobe -v error -select_streams v:0 -show_entries stream=width,height,avg_frame_rate,nb_frames,duration,codec_name -of default=noprint_wrappers=1 "$TAKE"
echo "== DURATION =="
ffprobe -v error -show_entries format=duration,size -of default=noprint_wrappers=1 "$TAKE"
echo "== DECODE ERRORS =="
ffmpeg -v error -i "$TAKE" -f null - 2>&1 | head -20
echo "(end decode check)"
echo "== TILES =="
for t in 0.5 2 4 6 8 9.5; do
  ts=$(echo "$t" | tr . p)
  ffmpeg -v error -y -ss "$t" -i "$TAKE" -frames:v 1 "$DIR/${PRE}_${ts}s.png"
done
ls "$DIR/${PRE}_"*s.png
echo "== AUDIO: overall =="
ffmpeg -hide_banner -nostats -i "$TAKE" -af volumedetect -f null - 2>&1 | grep -E "max_volume|mean_volume" | head -4
echo "== AUDIO: true peak =="
ffmpeg -hide_banner -nostats -i "$TAKE" -af ebur128=peak=true:framelog=quiet -f null - 2>&1 | grep -iE "true peak|peak" | tail -4
echo "== AUDIO: per-0.5s peaks (dBFS) =="
python3 - "$TAKE" <<'EOF'
import subprocess, sys, re
take = sys.argv[1]
for i in range(20):
    t0 = i*0.5
    o = subprocess.run(["ffmpeg","-hide_banner","-nostats","-ss",str(t0),"-t","0.5","-i",take,
                        "-af","volumedetect","-f","null","-"],
                       capture_output=True, text=True).stderr
    m = re.search(r"max_volume:\s*(-?[\d.]+|-inf)\s*dB", o)
    print(f"bin {t0:4.1f}s peak {m.group(1) if m else 'n/a'} dB")
EOF
