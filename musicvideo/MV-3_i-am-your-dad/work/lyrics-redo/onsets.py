#!/usr/bin/env python3
"""MV-3 lyrics redo: find dad-phrase onsets in a vocal-stem slice by RMS envelope.

The large-v3-turbo stem transcription goes silent after the first phrase
on pure-repeat slices (L26, L27-tail, L38) — the model itself suppresses
repeats even with no_repeat_ngram_size=0. But the MDX vocal stem is clean
isolated vocals, so the phrase onsets are measurable directly: each
"I am your dad" starts with a vowel burst ("I") after a gap. This script
computes a 25ms RMS envelope and reports rising-edge onsets (envelope
crosses 25% of the slice max after a dip below 10%), which are the phrase
starts. Usage: onsets.py <stem_wav> [min_gap_s] [threshold_frac].
"""
import sys
import numpy as np
from scipy.io import wavfile

def main():
    path = sys.argv[1]
    min_gap = float(sys.argv[2]) if len(sys.argv) > 2 else 0.8
    frac = float(sys.argv[3]) if len(sys.argv) > 3 else 0.25
    sr, data = wavfile.read(path)
    if data.ndim == 2:
        data = data.mean(axis=1)
    x = data.astype(np.float64) / max(1.0, np.abs(data).max())
    win = int(sr * 0.025)   # 25ms RMS window
    hop = int(sr * 0.010)   # 10ms hop
    n = 1 + max(0, (len(x) - win) // hop)
    env = np.empty(n)
    for i in range(n):
        seg = x[i * hop:i * hop + win]
        env[i] = np.sqrt(np.mean(seg ** 2))
    # smooth lightly (3-frame moving average)
    env = np.convolve(env, np.ones(3) / 3, mode="same")
    peak = env.max()
    hi, lo = peak * frac, peak * 0.10
    onsets = []
    armed = True
    for i in range(1, n):
        t = i * hop / sr
        if armed and env[i - 1] < hi <= env[i]:
            if not onsets or t - onsets[-1] >= min_gap:
                onsets.append(round(t, 2))
            armed = False
        elif env[i] < lo:
            armed = True
    print(f"{path}: sr={sr} peak_rms={peak:.4f} hi={hi:.4f}")
    print("onsets:", onsets)
    # also print a coarse envelope profile (0.25s bins) for eyeballing
    bins = []
    bw = int(sr * 0.25)
    for j in range(0, len(x), bw):
        seg = x[j:j + bw]
        bins.append(round(float(np.sqrt(np.mean(seg ** 2))) / peak, 2) if len(seg) else 0)
    print("env25 (0.25s bins, /peak):", bins)

if __name__ == "__main__":
    main()
