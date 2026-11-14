#!/usr/bin/env python3
"""compare_flow.py — validate c11_flow against cv2.calcOpticalFlowFarneback.

Frames are raw uint8 gray (W*H). Runs both implementations with the
same defaults (pyr_scale 0.5, levels 3, winsize 15, iterations 3,
poly_n 5, poly_sigma 1.1, flags 0) and reports, per pair:
  mean endpoint error (EPE) between the two flow fields,
  mean magnitude of each, Pearson corr of magnitudes,
  fraction of pixels with EPE < 0.5 px (interior only, 8px border cut),
  mean |u|/|v| bias, runtime of each.
Usage: compare_flow.py pair1_f1.raw pair1_f2.raw [pair2 ...] W H
"""
import json
import os
import subprocess
import sys
import time

import numpy as np


def load_flow(path, w, h):
    return np.fromfile(path, dtype=np.float32).reshape(h, w, 2)


def c11_flow(f1, f2, w, h, binary, tmp):
    out = tmp + ".flow"
    t0 = time.time()
    r = subprocess.run([binary, "flow", f1, f2, str(w), str(h), out],
                       capture_output=True, text=True)
    dt = time.time() - t0
    if r.returncode != 0:
        raise RuntimeError(f"c11_flow failed: {r.stderr}")
    return load_flow(out, w, h), dt, r.stdout.strip()


def cv2_flow(f1, f2, w, h):
    import cv2
    a = np.fromfile(f1, dtype=np.uint8).reshape(h, w)
    b = np.fromfile(f2, dtype=np.uint8).reshape(h, w)
    t0 = time.time()
    fl = cv2.calcOpticalFlowFarneback(a, b, None, 0.5, 3, 15, 3, 5, 1.1, 0)
    return fl, time.time() - t0


def compare_pair(f1, f2, w, h, binary, name):
    tmp = os.path.join(os.path.expanduser("~"), "workspace", "tmpbuild",
                       "cmp")
    c11, t_c11, stats = c11_flow(f1, f2, w, h, binary, tmp)
    cv, t_cv = cv2_flow(f1, f2, w, h)
    # interior only: Farneback window (15) + pyramid blur corrupts borders
    b = 8
    c = c11[b:h - b, b:w - b]
    v = cv[b:h - b, b:w - b]
    diff = c - v
    epe = np.sqrt((diff ** 2).sum(axis=2))
    mag_c = np.sqrt((c ** 2).sum(axis=2))
    mag_v = np.sqrt((v ** 2).sum(axis=2))
    corr = float(np.corrcoef(mag_c.ravel(), mag_v.ravel())[0, 1])
    return {
        "pair": name,
        "epe_mean": float(epe.mean()),
        "epe_p50": float(np.median(epe)),
        "epe_p90": float(np.percentile(epe, 90)),
        "frac_epe_lt_0.5": float((epe < 0.5).mean()),
        "mag_c11_mean": float(mag_c.mean()),
        "mag_cv2_mean": float(mag_v.mean()),
        "mag_corr": corr,
        "bias_u": float(diff[..., 0].mean()),
        "bias_v": float(diff[..., 1].mean()),
        "t_c11_s": round(t_c11, 3),
        "t_cv2_s": round(t_cv, 3),
        "c11_stats": stats,
    }


def main():
    args = sys.argv[1:]
    if len(args) < 4 or (len(args) - 2) % 2 != 0:
        print(__doc__)
        sys.exit(2)
    w, h = int(args[-2]), int(args[-1])
    frames = args[:-2]
    binary = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          "c11_flow")
    results = []
    for i in range(0, len(frames), 2):
        f1, f2 = frames[i], frames[i + 1]
        name = f"{f1.split('/')[-1]} -> {f2.split('/')[-1]}"
        res = compare_pair(f1, f2, w, h, binary, name)
        results.append(res)
        print(json.dumps(res, indent=2))
    with open("c11_flow_validation.json", "w") as fp:
        json.dump(results, fp, indent=2)
    print("wrote c11_flow_validation.json")


if __name__ == "__main__":
    main()
