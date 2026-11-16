#!/usr/bin/env python3
"""Joint seam scan: MAE (320x180 gray, 0-255) between upstream frame (239-a)
and downstream frame (b) for a,b in 0..12; plus downstream head motion
MAE f_b -> f_b+12. Prints naive (0,0) seam and best trim combo per joint."""
import subprocess, sys
import numpy as np

TAKES = {
    "U1": "takes/media-generation-e2-u1-take3-0-c2f6e6b8-85f5-4a8d-bd0c-4d1f12759247.mp4",
    "U2": "takes/media-generation-e2-u2-take1-0-8d186a12-d9e5-49df-adcd-a9daa93196b8.mp4",
    "U3": "takes/media-generation-e2-u3-take5-0-46b36e3a-04e9-482c-bd1c-5c5e3ae7f732.mp4",
    "U4": "takes/media-generation-e2-u4-take1-0-1b939fab-9809-4f10-80b1-0ea478c65c66.mp4",
    "U5": "takes/media-generation-e2-u5-take1-0-937bf2c2-baf3-4126-ad79-dcede5d8c7b3.mp4",
    "U6": "takes/media-generation-e2-u6-take2-0-71a12e24-ce3c-4441-861f-88ac28bc872f.mp4",
}
W, H = 320, 180

def frames(path, idxs):
    """Decode selected frame indices as gray arrays."""
    out = {}
    for i in idxs:
        cmd = ["ffmpeg", "-v", "error", "-i", path,
               "-vf", f"select='eq(n\\,{i})',scale={W}:{H},format=gray",
               "-frames:v", "1", "-f", "rawvideo", "-"]
        r = subprocess.run(cmd, capture_output=True)
        if len(r.stdout) == W * H:
            out[i] = np.frombuffer(r.stdout, dtype=np.uint8).astype(np.float32)
    return out

def mae(a, b):
    return float(np.mean(np.abs(a - b)))

JOINTS = [("U1", "U2"), ("U2", "U3"), ("U3", "U4"), ("U4", "U5"), ("U5", "U6")]
for up, dn in JOINTS:
    uf = frames(TAKES[up], list(range(227, 240)))
    df = frames(TAKES[dn], list(range(0, 25)))
    naive = mae(uf[239], df[0])
    best = (1e9, None)
    for a in range(0, 13):
        for b in range(0, 13):
            v = mae(uf[239 - a], df[b])
            if v < best[0]:
                best = (v, (a, b))
    a, b = best[1]
    head_motion = mae(df[b], df[b + 12])
    print(f"{up}->{dn}: naive seam MAE {naive:.1f} | best {best[0]:.1f} at "
          f"upstream tail trim {a}f, downstream head trim {b}f | "
          f"downstream head motion f{b}->f{b+12} MAE {head_motion:.1f}")
