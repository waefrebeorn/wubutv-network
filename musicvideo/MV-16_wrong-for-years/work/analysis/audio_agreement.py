#!/usr/bin/env python3
"""MV-16 REBUILD gate: master-vs-track audio agreement.
Decodes both audios to 16 kHz mono float PCM and computes Pearson
correlation overall and per 5 s window (min reported). The master
audio must be the song itself, sample-aligned: any edit, offset or
wrong take collapses the correlation.
Usage: audio_agreement.py <master.mp4> <track.mp3>"""
import subprocess, sys
import numpy as np

def decode(path):
    raw = subprocess.check_output(['ffmpeg', '-v', 'error', '-i', path,
        '-ac', '1', '-ar', '16000', '-f', 'f32le', '-'])
    return np.frombuffer(raw, dtype=np.float32)

a = decode(sys.argv[1])   # master
b = decode(sys.argv[2])   # track
n = min(len(a), len(b))
a, b = a[:n], b[:n]
def corr(x, y):
    x = x - x.mean(); y = y - y.mean()
    d = np.sqrt((x * x).sum() * (y * y).sum())
    return float((x * y).sum() / d) if d > 0 else 0.0
overall = corr(a, b)
win = 5 * 16000
mins = []
for i in range(0, n - win + 1, win):
    mins.append(corr(a[i:i + win], b[i:i + win]))
print(f'samples={n} dur={n / 16000:.3f}s overall_corr={overall:.5f}')
print(f'windows={len(mins)} min_window_corr={min(mins):.5f} '
      f'mean_window_corr={float(np.mean(mins)):.5f}')
print('worst windows:', [f'{i * 5}s:{c:.4f}' for i, c in
      sorted(enumerate(mins), key=lambda t: t[1])[:3]])
