#!/usr/bin/env python3
"""RMS energy per 0.5s + vocal-band energy, for section-boundary corroboration."""
import json, sys
import numpy as np, librosa
y, sr = librosa.load(sys.argv[1], sr=22050, mono=True)
hop = int(sr * 0.5)
rms = []
for i in range(0, len(y), hop):
    seg = y[i:i+hop]
    rms.append({"t": round(i / sr, 2), "rms": round(float(np.sqrt(np.mean(seg**2))), 4)})
with open(sys.argv[2], "w") as f:
    json.dump({"duration": round(len(y)/sr, 2), "rms_0p5s": rms}, f, indent=1)
arr = np.array([r["rms"] for r in rms])
print("dur", round(len(y)/sr, 2), "rms min/med/max", float(arr.min()), float(np.median(arr)), float(arr.max()))
# print quiet windows (rms < 25th pct) as candidate boundaries
q = np.percentile(arr, 25)
quiet = [rms[i]["t"] for i in range(len(rms)) if rms[i]["rms"] < q]
print("quiet 0.5s bins:", quiet)
