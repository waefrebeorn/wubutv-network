#!/usr/bin/env python3
"""Count audit for SERIAL-1 units — CEO8 ORDER 2 / S1_SEGMENT_TOTAL.md QC gate 2.

A serial about counting that miscounts on screen is dead: a count mismatch is
a RE-FIRE, not a note.

Flow (human in the loop, honest):
  1. Extract stills at 0.5s and 9.5s into --outdir (the ledger evidence).
  2. Print a heuristic advisory count (bone-color connected components —
     naive; catches papers, screens, mugs. Never ship on it alone).
  3. The operator OPENS the two stills, counts the blank cards by eye, and
     re-runs with --confirm "<n05>,<n95>".
  4. The script compares confirmed counts against --expect: mismatch ->
     exit 1 (RE-FIRE); match -> exit 0 and writes audit.json into --outdir.

Usage:
  python3 tools/count_audit.py serials/s1_02_the_receipt_16x9.mp4 \
      --outdir serials/qc/s1_02 --expect 1
  # ... view serials/qc/s1_02/t05.png and t95.png, count the cards ...
  python3 tools/count_audit.py serials/s1_02_the_receipt_16x9.mp4 \
      --outdir serials/qc/s1_02 --expect 1 --confirm "1,1"
"""
import json
import os
import subprocess
import sys

import numpy as np
from PIL import Image

BONE = np.array([244, 238, 220], dtype=np.float32)  # #F4EEDC
TOL = 42.0
W = 160


def grab(path, t, out_path):
    subprocess.run(
        ["ffmpeg", "-v", "error", "-y", "-ss", f"{t:.2f}", "-i", path,
         "-frames:v", "1", "-vf", f"scale={W}:-1", out_path],
        check=True)
    return np.asarray(Image.open(out_path).convert("RGB")).astype(np.float32)


def heuristic_count(fr):
    mask = np.abs(fr - BONE).sum(-1) < TOL * 3
    h, w = mask.shape
    parent = {}

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    for y in range(h):
        for x in range(w):
            if not mask[y, x]:
                continue
            i = y * w + x
            parent[i] = i
            if x and mask[y, x - 1]:
                parent[find(i)] = find(y * w + x - 1)
            if y and mask[y - 1, x]:
                parent[find(i)] = find((y - 1) * w + x)
    sizes = {}
    for y in range(h):
        for x in range(w):
            if not mask[y, x]:
                continue
            r = find(y * w + x)
            sizes[r] = sizes.get(r, 0) + 1
    return sum(1 for s in sizes.values() if s > 0.008 * h * w)


def main():
    path = sys.argv[1]
    outdir = sys.argv[sys.argv.index("--outdir") + 1]
    expect = int(sys.argv[sys.argv.index("--expect") + 1]) if "--expect" in sys.argv else None
    confirm = None
    if "--confirm" in sys.argv:
        confirm = [int(x) for x in sys.argv[sys.argv.index("--confirm") + 1].split(",")]
    os.makedirs(outdir, exist_ok=True)
    out = {}
    for key, t in (("t05", 0.5), ("t95", 9.5)):
        still = os.path.join(outdir, f"{key}.png")
        fr = grab(path, t, still)
        out[key] = {"still": still, "heuristic_count": heuristic_count(fr)}
    rec = {"file": path, "expect": expect, **out}
    if confirm is None:
        rec["status"] = "UNCONFIRMED — view the stills, count the cards, re-run with --confirm"
        print(json.dumps(rec, indent=1))
        sys.exit(2)
    out["t05"]["confirmed_count"] = confirm[0]
    out["t95"]["confirmed_count"] = confirm[1]
    ok = (expect is not None and confirm[0] == expect and confirm[1] == expect)
    rec["status"] = "PASS" if ok else "FAIL — count mismatch is a RE-FIRE, not a note"
    with open(os.path.join(outdir, "audit.json"), "w") as f:
        json.dump(rec, f, indent=1)
    print(json.dumps(rec, indent=1))
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
