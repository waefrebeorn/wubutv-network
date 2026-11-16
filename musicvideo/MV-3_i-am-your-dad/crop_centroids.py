#!/usr/bin/env python3
"""Per-scene 9:16 reframe: motion-centroid crop x for each scene's primary take.

Samples the take at 4fps, 160x90 gray; mean abs-diff column profile over
the take -> centroid in 160 coords -> x8 to 1280 coords -> 405-wide
window centered on the centroid, clamped [0, 875], rounded even.
Static takes fall back to center (440). Output: crops.json {scene: x}.
"""
import json, subprocess, os
import numpy as np

PROJ = os.path.dirname(os.path.abspath(__file__))
TAKES = os.path.join(PROJ, "takes")
PRIMARY = {
    "S01": "mv3_s01_t2.mp4", "S02": "mv3_s02_t2.mp4", "S03": "mv3_s03_t1.mp4",
    "S04": "mv3_s04_t1.mp4", "S05": "mv3_s05_t1.mp4", "S06": "mv3_s06_t1.mp4",
    "S07": "mv3_s07_t1.mp4", "S08": "mv3_s08_t1.mp4", "S09": "mv3_s09_t1.mp4",
    "S10": "mv3_s10_t1.mp4", "S11": "mv3_s11_t2.mp4", "S12": "mv3_s12_t2.mp4",
    "S13": "mv3_s13_t1.mp4", "S14": "mv3_s14_t1.mp4", "S15": "mv3_s15_t1.mp4",
    "S16": "mv3_s16_t1.mp4", "S17": "mv3_s17_t1.mp4", "S18": "mv3_s18_t2.mp4",
    "S19": "mv3_s19_t1.mp4", "S20": "mv3_s20_t1.mp4", "S21": "mv3_s21_t2.mp4",
    "S22": "mv3_s22_t1.mp4", "S23": "mv3_s23_t2.mp4", "S24": "mv3_s24_t2.mp4",
    "S25": "mv3_s25_t1.mp4", "S26": "mv3_s26_t1.mp4", "S27": "mv3_s27_t1.mp4",
    "S28": "mv3_s28_t3.mp4", "S29": "mv3_s29_t1.mp4", "S30": "mv3_s30_t3.mp4",
    "S31": "mv3_s31_t1.mp4", "S32": "mv3_s32_t1.mp4", "S33": "mv3_s33_t1.mp4",
    "S34": "mv3_s34_t1.mp4", "S35": "mv3_s35_t1.mp4", "S36": "mv3_s36_t2.mp4",
    "S37": "mv3_s37_t1.mp4", "S38": "mv3_s38_t2.mp4", "S39": "mv3_s39_t1.mp4",
}

def centroid_x(path):
    cmd = ["ffmpeg", "-v", "error", "-i", path, "-vf",
           "fps=4,scale=160:90,format=gray", "-f", "rawvideo", "-"]
    raw = subprocess.run(cmd, capture_output=True, check=True).stdout
    n = len(raw) // (160 * 90)
    if n < 2:
        return 440
    fr = np.frombuffer(raw, dtype=np.uint8).reshape(n, 90, 160).astype(np.int16)
    diff = np.abs(np.diff(fr, axis=0)).mean(axis=0)  # 90x160
    col = diff.mean(axis=0)
    tot = col.sum()
    if tot <= 0:
        return 440
    cx160 = (col * np.arange(160)).sum() / tot
    cx = cx160 * 8
    x = int(round((cx - 202) / 2) * 2)
    return max(0, min(875, x))

out = {}
for sc, fn in PRIMARY.items():
    x = centroid_x(os.path.join(TAKES, fn))
    out[sc] = x
    print(sc, fn, "crop_x=", x)
with open(os.path.join(PROJ, "crops.json"), "w") as f:
    json.dump(out, f, indent=1)
print("wrote crops.json")
