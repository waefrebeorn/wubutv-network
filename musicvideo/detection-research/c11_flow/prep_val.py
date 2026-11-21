#!/usr/bin/env python3
"""prep_val.py — build validation frame pairs for c11_flow.

Outputs (all under OUT dir, raw uint8 gray):
  synth_160x90: random-texture frames shifted by known (dx,dy)
  mb_<seq>_640 / mb_<seq>_160: Middlebury other-set frame10->frame11
    (640x480 native + 160x90 downscale, the pipeline's working size)
  mv14_<take>_160: two adjacent frames from a real MV-14 take
Also writes gt_<seq>.npy (Middlebury ground-truth flow, float32 HxWx2)
and synth truth (dx,dy) into the results manifest.
"""
import json
import os
import subprocess
import sys

import numpy as np

OUT = os.path.expanduser("~/workspace/c11_flow_val")
os.makedirs(OUT, exist_ok=True)
sys.path.insert(0, os.path.expanduser("~/workspace/cv2-throwaway"))
import cv2


def write_raw(path, arr):
    np.ascontiguousarray(arr, dtype=np.uint8).tofile(path)


def read_flo(path):
    with open(path, "rb") as fp:
        magic = np.fromfile(fp, dtype=np.float32, count=1)[0]
        assert magic == 202021.25, f"bad .flo magic {magic}"
        w = int(np.fromfile(fp, dtype=np.int32, count=1)[0])
        h = int(np.fromfile(fp, dtype=np.int32, count=1)[0])
        data = np.fromfile(fp, dtype=np.float32).reshape(h, w, 2)
    return data


manifest = {"synthetic": [], "middlebury": [], "mv14": []}

# --- 1. synthetic known shifts, 160x90 ---
rng = np.random.default_rng(7)
W, H = 160, 90
# textured canvas larger than the frame so shifts never wrap
canvas = rng.integers(0, 256, size=(H + 16, W + 16), dtype=np.uint8)
# add low-frequency structure so the polynomial has gradient everywhere
yy, xx = np.mgrid[0:H + 16, 0:W + 16]
canvas = np.clip(canvas.astype(np.float32) * 0.6
                 + 40 * np.sin(xx / 9.0) + 30 * np.cos(yy / 7.0),
                 0, 255).astype(np.uint8)
for dx, dy in [(3, 0), (0, -2), (2, 2), (-4, 1), (5, -3)]:
    x0, y0 = 8 - dx, 8 - dy
    f1 = canvas[8:8 + H, 8:8 + W]
    f2 = canvas[y0:y0 + H, x0:x0 + W]
    n = f"synth_dx{dx}_dy{dy}"
    write_raw(f"{OUT}/{n}_f1.raw", f1)
    write_raw(f"{OUT}/{n}_f2.raw", f2)
    manifest["synthetic"].append({"name": n, "dx": dx, "dy": dy})

# --- 2. Middlebury other-set (frames + gt flow) ---
MB = os.path.expanduser("~/workspace/c11_flow_val")
for seq in ["Dimetrodon", "Grove2", "Urban2", "Venus"]:
    f1p = f"{MB}/other-data/{seq}/frame10.png"
    f2p = f"{MB}/other-data/{seq}/frame11.png"
    gt = read_flo(f"{MB}/other-gt-flow/{seq}/flow10.flo")
    a = cv2.imread(f1p, cv2.IMREAD_GRAYSCALE)
    b = cv2.imread(f2p, cv2.IMREAD_GRAYSCALE)
    assert a.shape == gt.shape[:2], (seq, a.shape, gt.shape)
    write_raw(f"{OUT}/mb_{seq}_640_f1.raw", a)
    write_raw(f"{OUT}/mb_{seq}_640_f2.raw", b)
    np.save(f"{OUT}/mb_{seq}_640_gt.npy", gt)
    a90 = cv2.resize(a, (160, 90), interpolation=cv2.INTER_AREA)
    b90 = cv2.resize(b, (160, 90), interpolation=cv2.INTER_AREA)
    write_raw(f"{OUT}/mb_{seq}_160_f1.raw", a90)
    write_raw(f"{OUT}/mb_{seq}_160_f2.raw", b90)
    gt90 = cv2.resize(gt, (160, 90), interpolation=cv2.INTER_AREA) * 0.25
    np.save(f"{OUT}/mb_{seq}_160_gt.npy", gt90)
    manifest["middlebury"].append({"seq": seq, "w": 640, "h": 480})

# --- 3. real MV-14 frames, 160x90 gray ---
take = os.path.expanduser(
    "~/workspace/wubutv-network/musicvideo/MV-14_clip-it/takes/"
    "media-generation-mv14-s47-t1-0-e01ad392-dfec-494f-9cb4-232c95232730.mp4")
for tag, t in [("t1s", 1.0), ("t1s2", 1.2)]:
    out = f"{OUT}/mv14_s47_{tag}.raw"
    r = subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(t),
                        "-i", take, "-frames:v", "1", "-vf",
                        "scale=160:90,format=gray", "-f", "rawvideo", out],
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
manifest["mv14"].append({"take": "mv14-s47-t1", "frames": ["t1s", "t1s2"]})

with open(f"{OUT}/manifest.json", "w") as fp:
    json.dump(manifest, fp, indent=2)
print(json.dumps(manifest, indent=2))
print("OK")
