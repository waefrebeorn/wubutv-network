#!/usr/bin/env python3
"""Extract per-onset frame windows from the DELIVERED master for lag measurement.
For each scored onset (kind=sing), extract frames F-6 .. F+13 (20 frames) at
full 1280x720 PNG via input seeking. Output: work/correction/frames/<label>/f<absframe>.png
"""
import json, os, subprocess, sys

PROJ = os.path.expanduser("~/workspace/wubutv-network/musicvideo/MV-7_the-nobody-man")
MASTER = os.path.join(PROJ, "masters/mv7_im_the_nobody_man_16x9.mp4")
OUT = os.path.join(PROJ, "work/correction/frames")
os.makedirs(OUT, exist_ok=True)

onsets = json.load(open(os.path.join(PROJ, "work/gate_final/onsets.json")))
scored = [o for o in onsets if o["kind"] == "sing"]
for o in scored:
    F = o["frame"]
    d = os.path.join(OUT, o["label"])
    os.makedirs(d, exist_ok=True)
    start_f = max(0, F - 6)
    # seek to start_f/24 - small preroll handled by accurate seek (output seek on frames count)
    t = start_f / 24.0
    n = (F + 13) - start_f + 1
    pat = os.path.join(d, "w%02d.png")  # window index 0.. ; abs frame = start_f + idx
    if len(os.listdir(d)) >= n:
        print(o["label"], "cached", n)
        continue
    cmd = ["ffmpeg", "-v", "error", "-y", "-ss", f"{t:.4f}", "-i", MASTER,
           "-frames:v", str(n), "-vsync", "0", pat]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print("FAIL", o["label"], r.stderr[-300:]); sys.exit(1)
    json.dump({"label": o["label"], "onset_frame": F, "start_frame": start_f, "n": n},
              open(os.path.join(d, "meta.json"), "w"))
    print(o["label"], "F", F, "start", start_f, "n", n)
print("done", len(scored))
