#!/usr/bin/env python3
"""JOINT GATE measurement — ONE SHORT E1.
Usage: joint_gate.py <video> [label]
Seam MAE at the 5 cuts vs episode baseline; item-6 judged by the
distribution-relative rule (post-msg-470): downstream head-12 mean MAE must
be >= the episode's p25 of 12-frame head-motion windows AND the head window
must be IN-MOTION class (head mean >= baseline median), replacing the old
fixed >=8 floor that E2 logged as miscalibrated.
"""
import subprocess, sys
import numpy as np

path = sys.argv[1]
label = sys.argv[2] if len(sys.argv) > 2 else path

out = subprocess.run(['ffmpeg', '-v', 'error', '-i', path, '-vf',
                      'scale=320:180,format=gray', '-f', 'rawvideo', '-'],
                     capture_output=True).stdout
fs = 320 * 180
nf = len(out) // fs
fr = np.frombuffer(out[:nf * fs], dtype=np.uint8).reshape(nf, 180, 320).astype(np.float32)
mae = np.abs(np.diff(fr, axis=0)).mean(axis=(1, 2))
print(f'{label}: frames decoded: {nf}, mae series: {len(mae)}')

samples = []
for u in range(6):
    base = u * 240
    for f in range(base + 12, base + 228, 24):
        samples.append(mae[f])
baseline95 = float(np.percentile(samples, 95))
baseline_med = float(np.median(samples))
print(f'baseline 95th pct: {baseline95:.2f}  median: {baseline_med:.2f} (n={len(samples)})')

heads = []
for u in range(6):
    base = u * 240
    for off in range(0, 228, 24):
        heads.append(float(np.mean(mae[base + off:base + off + 12])))
p25 = float(np.percentile(heads, 25))
print(f'head-window p25: {p25:.2f}')

for j in range(1, 6):
    cut = j * 240
    seam = float(mae[cut - 1])
    head = float(np.mean(mae[cut:cut + 12]))
    band = 'PASS' if seam <= 58 else ('CONDITIONAL' if seam <= 75 else 'FAIL')
    item6 = 'PASS' if (head >= p25 and head >= baseline_med) else 'BELOW-RULE'
    print(f'J{j} cut@{cut}: seam MAE {seam:.2f} [{band}]  head-12 {head:.2f} '
          f'item6(dist-relative) {item6}')
