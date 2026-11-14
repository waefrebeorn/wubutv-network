#!/usr/bin/env python3
"""Motion audit ON THE DELIVERED MASTER FILES (not on takes).

Decodes to 160x90 gray, mean abs diff per consecutive pair.
Near-dup threshold: mean abs diff < 0.5 (QC convention).
Gate: longest near-dup run DURING WORDS must be < 24f.
Word windows = union of LYRIC_TIMELINE line spans (L01..L40).
Reports mean diff, longest run overall, longest run in word windows,
exact-duplicate frames (diff == 0), and every run >= 12f.
"""
import subprocess, sys, os
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from make_captions_mv3 import LINES

def audit(path):
    cmd = ["ffmpeg", "-v", "error", "-i", path, "-vf",
           "scale=160:90,format=gray", "-f", "rawvideo", "-"]
    raw = subprocess.run(cmd, capture_output=True, check=True).stdout
    n = len(raw) // (160 * 90)
    fr = np.frombuffer(raw, dtype=np.uint8).reshape(n, 90, 160).astype(np.int16)
    diff = np.abs(np.diff(fr, axis=0)).mean(axis=(1, 2))  # n-1 values
    near = diff < 0.5
    # runs of near-dup (frame indices: diff[i] compares frames i,i+1)
    runs = []
    i = 0
    while i < len(near):
        if near[i]:
            j = i
            while j < len(near) and near[j]:
                j += 1
            runs.append((i, j - i))  # start diff index, length in diffs
            i = j
        else:
            i += 1
    # word windows in frame space (24fps)
    wins = [(round(s * 24), round(e * 24)) for _, _, s, e in LINES]
    def in_words(diff_idx):
        # diff idx i covers frames i..i+1; frame i+1 time = (i+1)/24
        f = diff_idx + 1
        return any(a <= f < b for a, b in wins)
    word_runs = [(s, l) for s, l in runs if any(in_words(s + k) for k in range(l))]
    print(f"== {path}")
    print(f"frames: {n}  mean diff: {diff.mean():.3f}  "
          f"exact-dup frames (diff==0): {int((diff == 0).sum())}")
    print(f"longest near-dup run overall: {max((l for _, l in runs), default=0)}f")
    print(f"longest near-dup run during words: "
          f"{max((l for _, l in word_runs), default=0)}f  (gate <24f)")
    big = [(s, l) for s, l in runs if l >= 12]
    print(f"runs >=12f: {len(big)}")
    for s, l in big[:40]:
        print(f"  diff@{s} len {l}f  t={s/24:.2f}-{ (s+l)/24:.2f}s "
              f"{'WORDS' if any(in_words(s+k) for k in range(l)) else 'gap/hold'}")
    return {"frames": n, "mean": float(diff.mean()),
            "max_run": max((l for _, l in runs), default=0),
            "max_word_run": max((l for _, l in word_runs), default=0),
            "exact_dup": int((diff == 0).sum()),
            "big_runs": [(s, l) for s, l in big]}

if __name__ == "__main__":
    for p in sys.argv[1:]:
        audit(p)
