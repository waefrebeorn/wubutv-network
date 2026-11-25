import json, subprocess, sys, os
import numpy as np
from PIL import Image

ROOT = os.path.dirname(os.path.abspath(__file__))  # work/rebuild/qc
PROJ = os.path.dirname(os.path.dirname(os.path.dirname(ROOT)))  # project root
TAKES = ["H1-B_v2", "I-A_v2", "I-B_v2", "V-0_v2", "PH-A_v2", "H2-A_v2"]

def run(cmd):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if r.returncode != 0:
        print("FAIL:", cmd, r.stderr[-500:])
    return r

for t in TAKES:
    short = t.replace("_v2", "").lower().replace("-", "")
    qdir = os.path.join(ROOT, short)
    os.makedirs(qdir, exist_ok=True)
    mp4 = os.path.join(PROJ, "takes", t + ".mp4")
    wav = os.path.join(qdir, t.lower() + "_take16k.wav")
    wjson = os.path.join(qdir, t.lower() + "_words.json")
    run(f'ffmpeg -y -v error -i "{mp4}" -vn -ac 1 -ar 16000 "{wav}"')
    run(f'/home/hatch/workspace/fw-venv/bin/python "{os.path.join(ROOT, "transcribe_take.py")}" "{wav}" "{wjson}"')
    run(f'ffmpeg -y -v error -i "{mp4}" -vf fps=2,scale=320:-1 "{qdir}/f_%03d.jpg"')
    # motion: mean abs diff between consecutive 0.5s frames
    import glob
    frames = sorted(glob.glob(qdir + "/f_*.jpg"))
    diffs = []
    prev = None
    for f in frames:
        a = np.asarray(Image.open(f).convert("L"), dtype=np.float32)
        if prev is not None:
            diffs.append(float(np.mean(np.abs(a - prev))))
        prev = a
    print(t, "frames:", len(frames), "motion diffs per 0.5s:", [round(d,1) for d in diffs])
    print(t, "motion min:", round(min(diffs),1) if diffs else None, "mean:", round(sum(diffs)/len(diffs),1) if diffs else None)
