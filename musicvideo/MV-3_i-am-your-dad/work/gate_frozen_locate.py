import json, subprocess, sys
import numpy as np
W, H, FPS = 160, 90, 24
master = sys.argv[1]
raw = subprocess.run(["ffmpeg","-v","error","-i",master,"-vf",f"scale={W}:{H},format=gray","-f","rawvideo","-"], capture_output=True, check=True).stdout
n = len(raw)//(W*H)
frames = np.frombuffer(raw[:n*W*H], dtype=np.uint8).reshape(n, W*H).astype(np.float32)
diffs = np.abs(np.diff(frames, axis=0)).mean(axis=1)
d = json.load(open("SONG_WORDS.json")); words = d["words"] if isinstance(d, dict) else d
vocal = np.zeros(n, dtype=bool)
for w in words:
    vocal[int(w[1]*FPS):min(int(w[2]*FPS)+1, n)] = True
import os as _os, sys as _sys
_sys.path.insert(0, _os.getcwd())
import assemble_mv3_recut as base
starts = [(sc, round(st*FPS)) for sc, st, _ in base.SCENES]
def scene_of(f):
    s = "LEADER"
    for sc, sf in starts:
        if f >= sf: s = sc
    return s
frozen = (diffs < 0.35)
runs = []
cur, start = 0, 0
for i in range(len(frozen)):
    if frozen[i] and vocal[i]:
        if cur == 0: start = i
        cur += 1
    else:
        if cur >= 12: runs.append((cur, start))
        cur = 0
if cur >= 12: runs.append((cur, start))
runs.sort(reverse=True)
for ln, st in runs[:8]:
    print(f"run {ln}f at frame {st} = {st/FPS:.2f}s scene {scene_of(st)} (vocal)")
