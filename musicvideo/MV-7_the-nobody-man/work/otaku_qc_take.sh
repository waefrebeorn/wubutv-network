#!/bin/bash
# Usage: otaku_qc_take.sh <unit UXX> <take.mp4>
# Produces: work/otaku_take_words/UXX.json, work/otaku_qc/UXX_sheet.jpg, prints ffprobe + motion stats
set -e
BASE=~/workspace/wubutv-network/musicvideo/MV-7_the-nobody-man
U=$1; TAKE=$2
cd "$BASE"
ffprobe -v error -select_streams v:0 -show_entries stream=width,height,r_frame_rate,nb_frames,duration -of default=nw=1 "$TAKE"
ffmpeg -y -v error -i "$TAKE" -vn -ac 1 -ar 16000 "work/otaku_qc/${U}_16k.wav"
~/workspace/fw-venv/bin/python work/transcribe_wav.py "work/otaku_qc/${U}_16k.wav" "work/otaku_take_words/${U}.json" small 10.0
ffmpeg -y -v error -i "$TAKE" -vf "fps=2,scale=320:180,tile=5x4" -frames:v 1 "work/otaku_qc/${U}_sheet.jpg"
# motion: mean frame diff + longest near-dup run at native fps (threshold: meanabsdiff<0.5 on 160x90 gray)
python3 - "$TAKE" <<'PYEOF'
import subprocess, sys, numpy as np
f = sys.argv[1]
p = subprocess.run(["ffmpeg","-v","error","-i",f,"-vf","scale=160:90,format=gray","-f","rawvideo","-"],capture_output=True)
a = np.frombuffer(p.stdout, dtype=np.uint8)
n = len(a)//(160*90); a = a[:n*160*90].reshape(n,90,160).astype(np.int16)
if n > 1:
    d = np.abs(np.diff(a,axis=0)).mean(axis=(1,2))
    run = mx = 0
    for v in d:
        run = run+1 if v < 0.5 else 0; mx = max(mx, run)
    print(f"frames={n} mean_diff={d.mean():.2f} min_diff={d.min():.2f} max_neardup_run_frames={mx}")
else:
    print("frames<2")
PYEOF
md5sum "$TAKE"
