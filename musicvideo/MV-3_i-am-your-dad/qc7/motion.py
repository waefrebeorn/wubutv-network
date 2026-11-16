import sys, subprocess, json
import numpy as np
# Usage: motion.py <mp4> <vocal_start> <vocal_end>
# 160x90 gray frames at 24fps via ffmpeg rawvideo; mean abs diff per pair.
path, vs, ve = sys.argv[1], float(sys.argv[2]), float(sys.argv[3])
cmd = ["ffmpeg","-v","error","-i",path,"-vf","scale=160:90,format=gray","-f","rawvideo","-pix_fmt","gray","-"]
raw = subprocess.run(cmd, capture_output=True, check=True).stdout
W,H = 160,90
n = len(raw)//(W*H)
frames = np.frombuffer(raw[:n*W*H], dtype=np.uint8).reshape(n,H,W).astype(np.float32)
diffs = np.abs(frames[1:]-frames[:-1]).mean(axis=(1,2))  # diffs[i] between frame i and i+1, time (i+1)/24
fps = 24.0
def window_mean(a,b):
    i0, i1 = max(0,int(a*fps)), min(len(diffs),int(b*fps))
    return float(diffs[i0:i1].mean()) if i1>i0 else None
def longest_run(a,b,thr=0.5):
    i0, i1 = max(0,int(a*fps)), min(len(diffs),int(b*fps))
    best=cur=0; bs=be=0; cs=i0
    for i in range(i0,i1):
        if diffs[i]<thr:
            if cur==0: cs=i
            cur+=1
            if cur>best: best,bs,be=cur,cs,i
        else: cur=0
    return best, (bs/fps if best else None), ((be+1)/fps if best else None)
vm = window_mean(vs,ve)
lr, ls, le = longest_run(vs,ve)
print(json.dumps({"vocal_mean": vm, "longest_lt0.5_run_frames": lr, "run_start_s": ls, "run_end_s": le, "n_frames": n}))
