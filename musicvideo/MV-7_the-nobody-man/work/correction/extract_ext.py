#!/usr/bin/env python3
"""Extended windows (+8f..+36f) for onsets whose opening was past +11f."""
import json, os, subprocess

PROJ = os.path.expanduser("~/workspace/wubutv-network/musicvideo/MV-7_the-nobody-man")
MASTER = os.path.join(PROJ, "masters/mv7_im_the_nobody_man_16x9.mp4")
EXT = os.path.join(PROJ, "work/correction/frames_ext")
os.makedirs(EXT, exist_ok=True)

LABELS = ["I-occ6", "V1.1", "C1.1", "C1.5", "C1.8a", "C1.8b",
          "PC2.3", "C2.1", "C2.7", "FC.8", "FC.10", "FC.T1"]
onsets = {o["label"]: o for o in json.load(open(os.path.join(PROJ, "work/gate_final/onsets.json")))}

for lab in LABELS:
    o = onsets[lab]
    F = round(o["onset"] * 24)
    start = F + 8
    d = os.path.join(EXT, lab)
    os.makedirs(d, exist_ok=True)
    if os.path.exists(os.path.join(d, "meta.json")):
        print("cached", lab); continue
    sel = f"select='between(n\\,{start}\\,{F+36})'"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", MASTER,
                    "-vf", sel, "-vsync", "0", os.path.join(d, "w%02d.png")], check=True)
    n = len([f for f in os.listdir(d) if f.endswith(".png")])
    json.dump({"label": lab, "onset_frame": F, "start_frame": start, "n": n},
              open(os.path.join(d, "meta.json"), "w"))
    print("done", lab, "F", F, "frames", n)
