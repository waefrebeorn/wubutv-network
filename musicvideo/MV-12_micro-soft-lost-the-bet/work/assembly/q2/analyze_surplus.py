#!/usr/bin/env python3
"""Q2 surplus analysis: per-frame motion across the FULL bridge takes
(160x90 gray mean abs-diff, same metric as qc_motion.py) + 4fps contact
sheets for eye-reading the surplus regions. Used windows from
assembly_build_mv12.py SCENES are marked; surplus = everything else.
"""
import glob, hashlib, os, subprocess
import numpy as np

BASE = "/home/hatch/workspace/wubutv-network/musicvideo/MV-12_micro-soft-lost-the-bet"
TAKES = f"{BASE}/takes"
Q2 = f"{BASE}/work/assembly/q2"
# scene -> (ledger md5, used a, used b, take frames total)
SCENES = {
 "S33": ("f46bccd0d033d3549f0362ac3f5f2c0e", 12, 32, 120),
 "S34": ("221592904d105d0f177f4e97675a7098", 12, 32, 120),
 "S35": ("99375078389f227f688f9583d27fcc18", 0, 38, 120),
 "S36": ("12e86eda2a7ffbb807418cf6fc1b29cd", 12, 34, 120),
 "S37": ("eabe9de022c8c5115c58f5a56e0ab7c6", 12, 34, 120),
 "S38": ("d0cbfe0060fca00e034c25288b4419bb", 14, 48, 120),
 "S39": ("474e4efd921e6cc446bddb54140bebaf", 0, 34, 240),
 "S40": ("e7c85c26fbe7581d0629d9039c34f2ef", 0, 41, 48),
 "S41": ("15c3acc41f29a8abfe4afdc88cd96deb", 0, 41, 240),
 "S42": ("e019fe39ee04268bf6968601301f1e93", 0, 96, 96),
}
def md5(p):
    h=hashlib.md5()
    with open(p,'rb') as f:
        for b in iter(lambda: f.read(1<<20), b''): h.update(b)
    return h.hexdigest()
by={md5(p):p for p in glob.glob(os.path.join(TAKES,'*.mp4'))}

def diffs(path, w=160, h=90):
    proc=subprocess.Popen(["ffmpeg","-v","error","-i",path,"-vf",f"scale={w}:{h},format=gray","-f","rawvideo","-"],stdout=subprocess.PIPE)
    fs=w*h; out=[]; prev=None
    while True:
        raw=proc.stdout.read(fs)
        if len(raw)<fs: break
        cur=np.frombuffer(raw,dtype=np.uint8).astype(np.float32)
        if prev is not None: out.append(float(np.abs(cur-prev).mean()))
        prev=cur
    proc.wait()
    return np.array(out)

for s,(m,a,b,nt) in SCENES.items():
    p=by[m]
    d=diffs(p)
    print(f"\n== {s} take {os.path.basename(p)[:40]} frames={len(d)+1} used f{a}-{b-1} ==")
    # 0.25s bins (6 frames)
    for k in range(0, len(d), 6):
        seg=d[k:k+6]
        t0=k/24
        mark='USED ' if (k>=a-1 and k<b) else '     '
        bar='#'*int(seg.mean()/2)
        print(f"  {mark}{t0:5.2f}s f{k:3d}-{k+len(seg)-1:3d} mean={seg.mean():6.2f} min={seg.min():5.2f} {bar}")
    # near-still runs >=6f in surplus
    runs=[]; cur=None
    for i,v in enumerate(d):
        if v<0.5:
            cur=[i,i] if cur is None else [cur[0],i]
        else:
            if cur is not None: runs.append(tuple(cur)); cur=None
    if cur is not None: runs.append(tuple(cur))
    runs=[(x,y) for x,y in runs if y-x+1>=6]
    print("  near-still runs >=6f (diff<0.5):", [(f"f{x}-{y} ({(y-x+1)}f, {(x+1)/24:.2f}-{(y+1)/24:.2f}s)") for x,y in runs] or "none")
    # contact sheet 4fps
    sheet=os.path.join(Q2,f"sheet_{s}.png")
    subprocess.run(["ffmpeg","-y","-v","error","-i",p,"-vf","fps=4,scale=320:180,tile=5x4","-frames:v","1",sheet],check=True)
    print(f"  sheet: {sheet} {os.path.getsize(sheet)} B")
print("\nDONE")
