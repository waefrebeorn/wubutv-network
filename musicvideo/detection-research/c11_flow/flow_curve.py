#!/usr/bin/env python3
"""flow_curve.py — motion-energy curve from a video, via c11_flow.

Decodes a video to 160x90 gray frames at 12 fps (the TSM/M6
convention), runs c11_flow mag on each consecutive pair, and writes
the per-frame mean-flow-magnitude curve plus, when a cut time is
given, the cut-point energy contrast (mean of the 12 frames before
vs the 12 after the cut — the GAP-1 cut-energy check the SLERM
survey scoped for F-05).

Usage:
  flow_curve.py VIDEO.mp4 [CUT_T] [--out curve.json] [--fps 12]
    CUT_T: cut time in seconds (optional).
Prints one JSON object to stdout and, with --out, to the file.
"""
import argparse
import json
import os
import subprocess
import sys
import tempfile

import numpy as np

W, H = 160, 90


def decode_frames(video, fps):
    tmp = tempfile.mkdtemp(prefix="flow_curve_")
    cmd = ["ffmpeg", "-v", "error", "-i", video, "-vf",
           f"fps={fps},scale={W}:{H},format=gray",
           "-f", "rawvideo", os.path.join(tmp, "frames.raw")]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"ffmpeg failed: {r.stderr}")
    data = np.fromfile(os.path.join(tmp, "frames.raw"), dtype=np.uint8)
    n = len(data) // (W * H)
    return data[:n * W * H].reshape(n, H, W), tmp


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("cut_t", nargs="?", type=float, default=None)
    ap.add_argument("--out", default=None)
    ap.add_argument("--fps", type=int, default=12)
    args = ap.parse_args()

    frames, tmp = decode_frames(args.video, args.fps)
    binary = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          "c11_flow")
    curve = []
    for i in range(len(frames) - 1):
        f1 = os.path.join(tmp, "a.raw")
        f2 = os.path.join(tmp, "b.raw")
        frames[i].tofile(f1)
        frames[i + 1].tofile(f2)
        r = subprocess.run([binary, "mag", f1, f2, str(W), str(H)],
                           capture_output=True, text=True)
        if r.returncode != 0:
            raise RuntimeError(f"c11_flow failed: {r.stderr}")
        curve.append(float(r.stdout.strip().split("=")[1]))
    result = {
        "video": os.path.basename(args.video),
        "fps": args.fps,
        "n_frames": int(len(frames)),
        "curve": [round(v, 4) for v in curve],
        "curve_mean": round(float(np.mean(curve)), 4) if curve else 0.0,
        "curve_max": round(float(np.max(curve)), 4) if curve else 0.0,
    }
    if args.cut_t is not None and curve:
        ci = int(round(args.cut_t * args.fps))
        before = curve[max(0, ci - 12):ci]
        after = curve[ci:min(len(curve), ci + 12)]
        result["cut_t"] = args.cut_t
        result["cut_frame"] = ci
        result["energy_before"] = (round(float(np.mean(before)), 4)
                                   if before else None)
        result["energy_after"] = (round(float(np.mean(after)), 4)
                                  if after else None)
        if before and after:
            result["cut_contrast"] = round(
                float(np.mean(after) - np.mean(before)), 4)
    out = json.dumps(result, indent=2)
    print(out)
    if args.out:
        with open(args.out, "w") as fp:
            fp.write(out + "\n")
        print(f"wrote {args.out}", file=sys.stderr)


if __name__ == "__main__":
    main()
