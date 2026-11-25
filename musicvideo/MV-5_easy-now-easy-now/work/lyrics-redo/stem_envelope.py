#!/usr/bin/env python3
"""MV-5 lyrics redo — vocal-stem RMS activity envelope for disputed spans.

Reads the assembled stem wav (44.1k stereo), computes 25ms RMS per channel
(mean), and prints the activity in the disputed windows so the question
"is anything sung here?" is answered from the separated vocal, not the mix:
  - 17.0-18.6s  "it's time to spend" (NOP only) or silence?
  - 187.5-193.5s  L107 artifact span: silence?
  - 197.5-200.5s  tail gap: "We ride" or silence?
  - 140.5-148.7s  "I'm falling" tags: vocal bursts present?
  - 102.4-103.8s  L45 "Ice" count: how many "ice" bursts?
  - 181.6-182.8s  L102 "drift" vs "rip" (activity only; word from stem decode)
Prints 100ms-bin RMS (max) per window with a sung/silent call at 0.02.
Usage: stem_envelope.py <stem_wav>
"""
import sys
import numpy as np
from scipy.io import wavfile

sr, data = wavfile.read(sys.argv[1])
assert sr == 44100
x = data.astype(np.float32) / 32768.0
if x.ndim == 2:
    x = x.mean(axis=1)
# 25ms RMS
win = int(0.025 * sr)
n = len(x) // win
rms = np.sqrt((x[:n * win].reshape(n, win) ** 2).mean(axis=1))
t = np.arange(n) * 0.025

WINDOWS = [
    ("it's-time-to-spend?", 17.0, 18.6),
    ("L107 artifact span", 187.0, 194.5),
    ("tail gap 197.5-200.5", 197.0, 201.0),
    ("I'm-falling tags", 140.0, 149.0),
    ("L45 ice count", 102.0, 104.0),
    ("L102 drift/rip", 181.0, 183.5),
    ("ta-da vocalise", 18.4, 22.0),
    ("closing Easy 193.5-197.5", 193.0, 198.0),
    # Chorus-1 hook windows (provisional grid: NOP hears 'Easy now' here,
    # the stem transcription hears NOTHING — is the hook sung or not?)
    ("C1 L17 hook", 57.5, 59.3),
    ("C1 L19 hook", 60.0, 61.6),
    ("C1 L21 hook", 62.3, 63.9),
    ("C1 L23 hook", 64.6, 66.2),
    ("C1 L25 hook", 66.8, 68.4),
    ("C1 L27 hook", 69.1, 70.6),
    ("C1 L29 hook", 71.1, 73.1),
    ("C1 L31 hook", 73.8, 75.2),
    ("C1 L33-L36 tags", 76.6, 86.4),
]
for label, t0, t1 in WINDOWS:
    print(f"--- {label} ({t0}-{t1}s) ---")
    i0, i1 = int(t0 / 0.025), int(t1 / 0.025)
    # 100ms bins: max RMS in each 4x25ms block
    bins = []
    for b in range(i0, i1, 4):
        seg = rms[b:b + 4]
        if len(seg):
            bins.append(f"{b*0.025:6.2f}:{seg.max():.3f}{'*' if seg.max() > 0.02 else ' '}")
    print("  " + " ".join(bins))
