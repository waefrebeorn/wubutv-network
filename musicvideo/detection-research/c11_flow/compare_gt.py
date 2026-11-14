#!/usr/bin/env python3
"""compare_gt.py — validate c11_flow against Middlebury ground-truth .flo.

Usage: compare_gt.py <valdir> <size>
  valdir: directory holding mb_<Seq>_<size>_f1.raw, _f2.raw, _gt.npy
  size: 160 or 640
Prints per-sequence: EPE vs ground truth (interior 8px cut) for c11
and cv2, EPE between c11 and cv2, mean magnitudes, fraction of
pixels with EPE<0.5 vs GT. Writes c11_flow_gt_<size>.json.
"""
import json
import os
import subprocess
import sys
import time

import numpy as np

SEQS = ["Dimetrodon", "Grove2", "Urban2", "Venus"]


def load_flow(path, w, h):
    return np.fromfile(path, dtype=np.float32).reshape(h, w, 2)


def run_c11(f1, f2, w, h, binary, tmp):
    out = tmp + ".flow"
    t0 = time.time()
    r = subprocess.run([binary, "flow", f1, f2, str(w), str(h), out],
                       capture_output=True, text=True)
    dt = time.time() - t0
    if r.returncode != 0:
        raise RuntimeError(f"c11_flow failed: {r.stderr}")
    return load_flow(out, w, h), dt


def run_cv2(f1, f2, w, h):
    import cv2
    a = np.fromfile(f1, dtype=np.uint8).reshape(h, w)
    b = np.fromfile(f2, dtype=np.uint8).reshape(h, w)
    t0 = time.time()
    fl = cv2.calcOpticalFlowFarneback(a, b, None, 0.5, 3, 15, 3, 5, 1.1, 0)
    return fl, time.time() - t0


def epe(a, b):
    return np.sqrt(((a - b) ** 2).sum(axis=-1))


def main():
    valdir, size = sys.argv[1], int(sys.argv[2])
    # "640" = native Middlebury resolution per sequence (they differ).
    native = {"Dimetrodon": (584, 388), "Grove2": (640, 480),
              "Urban2": (640, 480), "Venus": (420, 380)}
    binary = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          "c11_flow")
    tmp = os.path.join(os.path.expanduser("~"), "workspace", "tmpbuild",
                       "cmp")
    results = []
    for seq in SEQS:
        w, h = (160, 90) if size == 160 else native[seq]
        f1 = os.path.join(valdir, f"mb_{seq}_{size}_f1.raw")
        f2 = os.path.join(valdir, f"mb_{seq}_{size}_f2.raw")
        gt = np.load(os.path.join(valdir, f"mb_{seq}_{size}_gt.npy"))
        c11, t_c11 = run_c11(f1, f2, w, h, binary, tmp)
        cv, t_cv = run_cv2(f1, f2, w, h)
        b = 8
        c = c11[b:h - b, b:w - b]
        v = cv[b:h - b, b:w - b]
        g = gt[b:h - b, b:w - b]
        # .flo marks unknown flow with ~1e10; mask it out (affects
        # Dimetrodon heavily: 1135/14400 px at 160x90).
        valid = (np.abs(g[..., 0]) <= 100) & (np.abs(g[..., 1]) <= 100)
        c, v, g = c[valid], v[valid], g[valid]
        e_c = epe(c, g)
        e_v = epe(v, g)
        e_cv = epe(c, v)
        res = {
            "seq": seq,
            "size": size,
            "epe_c11_vs_gt_mean": float(e_c.mean()),
            "epe_c11_vs_gt_p50": float(np.median(e_c)),
            "epe_c11_vs_gt_p90": float(np.percentile(e_c, 90)),
            "epe_cv2_vs_gt_mean": float(e_v.mean()),
            "epe_cv2_vs_gt_p50": float(np.median(e_v)),
            "epe_c11_vs_cv2_mean": float(e_cv.mean()),
            "frac_c11_epe_lt_0.5_vs_gt": float((e_c < 0.5).mean()),
            "frac_cv2_epe_lt_0.5_vs_gt": float((e_v < 0.5).mean()),
            "mag_c11_mean": float(np.sqrt((c ** 2).sum(axis=-1)).mean()),
            "mag_cv2_mean": float(np.sqrt((v ** 2).sum(axis=-1)).mean()),
            "mag_gt_mean": float(np.sqrt((g ** 2).sum(axis=-1)).mean()),
            "t_c11_s": round(t_c11, 3),
            "t_cv2_s": round(t_cv, 3),
        }
        results.append(res)
        print(json.dumps(res, indent=2))
    out = f"c11_flow_gt_{size}.json"
    with open(out, "w") as fp:
        json.dump(results, fp, indent=2)
    print("wrote", out)


if __name__ == "__main__":
    main()
