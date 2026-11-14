#!/usr/bin/env python3
"""Dense head strips keyed off anchors.json: every 2nd frame from
(slice word-1 onset frame - 4) spanning ~44 frames, full-res face crop.
Panel i (row-major, 8 per row) = frame f0 + 2*i."""
import json, subprocess, os
import numpy as np

BASE = "/home/hatch/workspace/wubutv-network/musicvideo/MV-7_the-nobody-man"
OUT = f"{BASE}/work/rebuild2_recut"
os.makedirs(f"{OUT}/strips/dense", exist_ok=True)
W, H = 1248, 704

import sys
REFS = sys.argv[1:] or ["I1a", "I1c", "I2a", "I2c", "V1.1", "V1.4", "V1.5", "PC1.1", "PC1.2",
        "PC1.3", "PC1.4", "C1.2", "C1.3", "C1.4", "C1.5", "C1.6", "C1.8", "C2.1",
        "C1.Ta", "FC.3", "FC.7", "FC.8", "FC.9", "FC.10", "FC.Ta", "FC.Tc"]
LONG = {"I1a": 54, "I2c": 54, "FC.Tc": 54}

def decode(path):
    p = subprocess.run(["ffmpeg", "-v", "error", "-i", path,
                        "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], capture_output=True)
    a = np.frombuffer(p.stdout, dtype=np.uint8)
    n = len(a) // (W * H * 3)
    return a[:n * W * H * 3].reshape(n, H, W, 3)

def emit(frames, idxs, name, cx0, cy0, cw, ch):
    panels = [frames[i][cy0:cy0 + ch, cx0:cx0 + cw] for i in idxs]
    per = 8
    rows = []
    for gi in range(0, len(panels), per):
        batch = panels[gi:gi + per]
        while len(batch) < per:
            batch.append(np.zeros_like(panels[0]))
        rows.append(np.concatenate(batch, axis=1))
    grid = np.concatenate(rows, axis=0)
    gp = f"{OUT}/strips/dense/{name}.raw"
    grid.tofile(gp)
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
                    "-s", f"{grid.shape[1]}x{grid.shape[0]}", "-r", "1", "-i", gp,
                    "-frames:v", "1", f"{OUT}/strips/dense/{name}.jpg"], check=True)
    os.remove(gp)

def main():
    anchors = {r["ref"]: r for r in json.load(open(f"{OUT}/anchors.json"))["lines"]}
    cx0, cy0, cw, ch = int(0.30 * W), int(0.26 * H), int(0.32 * W), int(0.34 * H)
    from collections import defaultdict
    by_take = defaultdict(list)
    for ref in REFS:
        by_take[anchors[ref]["take"]].append(ref)
    for path, refs in by_take.items():
        frames = decode(path)
        for ref in refs:
            rec = anchors[ref]
            fa = int(round(rec["slice"][0]["s"] * 24))
            f0 = max(0, fa - 4)
            f1 = min(len(frames), fa + LONG.get(ref, 44))
            idxs = list(range(f0, f1, 2))
            emit(frames, idxs, ref, cx0, cy0, cw, ch)
            print(ref, "onset_frame", fa, "strip", idxs[0], "..", idxs[-1], "panels", len(idxs))
        if any(r == "C1.Ta" for r in refs) and not sys.argv[1:]:
            rec = anchors["C1.Ta"]
            w2 = rec["slice"][1]
            f_on = int(round(w2["s"] * 24))
            idxs = list(range(max(0, f_on - 10), min(len(frames), f_on + 22), 2))
            emit(frames, idxs, "C1.Ta_w2", cx0, cy0, cw, ch)
            print("C1.Ta_w2 word2 onset frame", f_on, "strip", idxs[0], "..", idxs[-1])
        del frames

if __name__ == "__main__":
    main()
