#!/usr/bin/env python3
"""Automated mouth-motion onset detector (CROSS-CHECK only; visual read governs).

For each onset window: frame-to-frame abs diff at 640x360 gray; tile the frame
40x30; per frame take the max tile-mean-diff inside the face zone (upper-middle
tiles). The mouth opening after a closed phrase gap produces a sharp localized
spike. Candidate opening frame = first frame >= F-3 whose tile-max exceeds
max(2.2 * baseline, baseline + 1.5), baseline = median tile-max over F-6..F-3,
sustained (next frame also above baseline*1.5). Also reports the argmax tile
location (face-motion centroid) for strip cropping.
"""
import json, os
import numpy as np
from PIL import Image

PROJ = os.path.expanduser("~/workspace/wubutv-network/musicvideo/MV-7_the-nobody-man")
FR = os.path.join(PROJ, "work/correction/frames")
OUT = os.path.join(PROJ, "work/correction/auto_lag.json")

onsets = json.load(open(os.path.join(PROJ, "work/gate_final/onsets.json")))
scored = [o for o in onsets if o["kind"] == "sing"]

TW, TH = 40, 30  # tile size at 640x360
results = []
for o in scored:
    d = os.path.join(FR, o["label"])
    meta = json.load(open(os.path.join(d, "meta.json")))
    start_f, F = meta["start_frame"], meta["onset_frame"]
    files = sorted(f for f in os.listdir(d) if f.startswith("w"))
    frames = []
    for f in files:
        im = Image.open(os.path.join(d, f)).convert("L").resize((640, 360))
        frames.append(np.asarray(im, dtype=np.float32))
    n = len(frames)
    # tile max diff per step i (frame i vs i-1), face zone tiles: x 3..12, y 1..7 (of 16x12)
    tilemax = [0.0] * n
    tileloc = [None] * n
    for i in range(1, n):
        diff = np.abs(frames[i] - frames[i - 1])
        best, bloc = 0.0, None
        for ty in range(1, 8):
            for tx in range(3, 13):
                t = diff[ty * TH:(ty + 1) * TH, tx * TW:(tx + 1) * TW]
                m = float(t.mean())
                if m > best:
                    best, bloc = m, (tx, ty)
        tilemax[i] = best
        tileloc[i] = bloc
    # index of onset within window
    oi = F - start_f
    base_idx = [i for i in range(0, oi) if i >= oi - 6]
    baseline = float(np.median([tilemax[i] for i in base_idx])) if base_idx else 0.0
    thr = max(2.2 * baseline, baseline + 1.5)
    cand = None
    for i in range(max(1, oi - 3), n - 1):
        if tilemax[i] > thr and tilemax[i + 1] > baseline * 1.5:
            cand = i
            break
    cand_frame = (start_f + cand) if cand is not None else None
    lag = (cand_frame - F) / 24.0 if cand_frame is not None else None
    # motion centroid over window for crop: weight tileloc of top steps
    results.append({
        "label": o["label"], "onset": o["onset"], "frame": F,
        "baseline": round(baseline, 3), "thr": round(thr, 3),
        "tilemax": [round(x, 2) for x in tilemax],
        "cand_frame": cand_frame, "auto_lag_s": (round(lag, 3) if lag is not None else None),
        "cand_tile": tileloc[cand] if cand is not None else None,
    })
    print(o["label"], "F", F, "base", round(baseline, 2), "cand", cand_frame,
          "lag", (round(lag, 3) if lag is not None else None))
json.dump(results, open(OUT, "w"), indent=1)
lags = [r["auto_lag_s"] for r in results if r["auto_lag_s"] is not None]
if lags:
    print("measured", len(lags), "of", len(results),
          "median", round(float(np.median(lags)), 3),
          "mean", round(float(np.mean(lags)), 3))
