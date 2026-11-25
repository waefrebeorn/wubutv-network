#!/usr/bin/env python3
"""Per-line F0 analysis of the MV-5 vocal stem -> singer evidence.

For every grid line: autocorrelation F0 track on the separated vocal
stem, per-0.25s medians, line median F0, voiced fraction, register
classification. Two voices are expected: a low register (CAT, the
crooner 'THE VOICE') and a high register (GIRL). Lines whose 0.25s
medians alternate between registers are flagged ALT (duet/alternation).
Output: singer_f0.json next to this script's qc dir + stdout table.
"""
import json
import sys

import numpy as np
from scipy.io import wavfile

QC = "/home/hatch/workspace/wubutv-network/musicvideo/MV-5_easy-now-easy-now/work/rebuild-v6/qc"
GRID = "/home/hatch/workspace/wubutv-network/musicvideo/MV-5_easy-now-easy-now/work/lyrics-redo/grid_merged.json"

sr, data = wavfile.read(f"{QC}/track_vocals.wav")
if data.ndim > 1:
    data = data.mean(axis=1)
x = data.astype(np.float64)
if np.max(np.abs(x)) > 0:
    x = x / np.max(np.abs(x))

WIN = int(0.05 * sr)          # 50 ms analysis window
HOP = int(0.025 * sr)         # 25 ms hop
FMIN, FMAX = 65, 420          # Hz search range
LAGMIN, LAGMAX = int(sr / FMAX), int(sr / FMIN)


def f0_track(t0, t1):
    """Return list of (t, f0 or None, rms) per hop in [t0, t1]."""
    out = []
    a = int(t0 * sr)
    b = int(t1 * sr)
    for s in range(a, max(a, b - WIN), HOP):
        seg = x[s:s + WIN]
        rms = float(np.sqrt(np.mean(seg ** 2))) if len(seg) else 0.0
        seg = seg - seg.mean()
        ac = np.correlate(seg, seg, "full")[len(seg) - 1:]
        if ac[0] <= 0:
            out.append((s / sr, None, rms))
            continue
        ac = ac / ac[0]
        seg_ac = ac[LAGMIN:LAGMAX]
        if len(seg_ac) == 0:
            out.append((s / sr, None, rms))
            continue
        lag = int(np.argmax(seg_ac)) + LAGMIN
        # periodicity strength = peak height; voiced if strong + loud
        if seg_ac.max() < 0.45 or rms < 0.02:
            out.append((s / sr, None, rms))
        else:
            out.append((s / sr, sr / lag, rms))
    return out


grid = json.load(open(GRID))
lines = grid["lines"] if isinstance(grid, dict) and "lines" in grid else grid

results = []
for ln in lines:
    t0, t1 = float(ln["start"]), float(ln["end"])
    tr = f0_track(t0, t1)
    # bucket into 0.25 s medians
    buckets = {}
    for t, f, r in tr:
        if f:
            buckets.setdefault(round((t - t0) / 0.25), []).append(f)
    meds = [float(np.median(v)) for k, v in sorted(buckets.items()) if v]
    allf = [f for _, f, _ in tr if f]
    voiced = len(allf) / max(1, len(tr))
    med = float(np.median(allf)) if allf else None
    results.append({
        "id": ln["id"], "start": t0, "end": t1, "text": ln["text"],
        "median_f0": med, "voiced_frac": round(voiced, 2),
        "bucket_medians": [round(m, 1) for m in meds],
    })

json.dump(results, open(f"{QC}/singer_f0.json", "w"), indent=1)
for r in results:
    print(f"{r['id']:>5} {r['start']:7.2f} medF0="
          f"{('%6.1f' % r['median_f0']) if r['median_f0'] else '   ---'}"
          f" voiced={r['voiced_frac']:.2f} buckets={r['bucket_medians']}"
          f"  {r['text'][:44]}")
