import subprocess, sys
import numpy as np
path = sys.argv[1]
W,H = 640,360; FS = W*H
p = subprocess.Popen(["ffmpeg","-v","error","-i",path,"-vf","scale=640:360,format=gray","-f","rawvideo","-"], stdout=subprocess.PIPE)
prev=None; n=0; runs=[]; cur=0; start=0
while True:
    buf = p.stdout.read(FS)
    if len(buf) < FS: break
    a = np.frombuffer(buf, dtype=np.uint8).astype(np.int16); n+=1
    if prev is not None:
        d = float(np.abs(a-prev).mean()); i = n-2  # diff index = pair ending at frame n-1
        if d < 0.5:
            if cur==0: start=i
            cur+=1
        else:
            if cur>=2: runs.append((start,cur))
            cur=0
    prev=a
if cur>=2: runs.append((start,cur))
p.wait()
print("frames", n)
for s,l in runs:
    print(f"run start_frame={s} len={l} t={s/24:.2f}s..{(s+l)/24:.2f}s")
print("total runs>=2:", len(runs))
