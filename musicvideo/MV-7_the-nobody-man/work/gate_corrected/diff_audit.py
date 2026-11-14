#!/usr/bin/env python3
"""Frame-diff audit on the master: motion + judder + near-dup runs.
Reads 160x90 gray rawvideo via ffmpeg pipe, computes mean abs diff per
consecutive frame pair. Reports vocal mean diff, near-dup runs (>=24f),
and the largest diff spikes with whether each sits on a segment boundary.
"""
import json, subprocess, sys
import numpy as np
MASTER = sys.argv[1]
W, H = 160, 90
proc = subprocess.Popen(['ffmpeg','-v','error','-i',MASTER,'-vf','scale=160:90',
                         '-f','rawvideo','-pix_fmt','gray','-'], stdout=subprocess.PIPE)
frames = []
while True:
    raw = proc.stdout.read(W*H)
    if len(raw) < W*H:
        break
    frames.append(np.frombuffer(raw, dtype=np.uint8).astype(np.float32))
proc.wait()
n = len(frames)
print('frames decoded:', n)
diffs = np.array([np.mean(np.abs(frames[i+1]-frames[i])) for i in range(n-1)])
np.save('work/gate_corrected/frame_diffs.npy', diffs)
cut = json.load(open('work/correction/cutlist_corrected.json'))
bounds = set()
for s in cut['segments']:
    bounds.add(round(s['song_start']*24))
    bounds.add(round(s['song_end']*24))
# vocal spans: everything except GAP/plate/fade? Use all frames minus fade tail.
vocal = diffs[:round(183.24*24)]
print(f'vocal mean diff: {vocal.mean():.3f} (fail if <0.5)')
print(f'overall mean diff: {diffs.mean():.3f}  median: {np.median(diffs):.3f}')
# near-dup runs: diff < 0.5
runs = []
i = 0
while i < len(diffs):
    if diffs[i] < 0.5:
        j = i
        while j < len(diffs) and diffs[j] < 0.5:
            j += 1
        runs.append((i, j-1, j-i))
        i = j
    else:
        i += 1
long_runs = [r for r in runs if r[2] >= 24]
print('near-dup runs >=24f (FAIL if any during vocal):', long_runs if long_runs else 'none')
print('near-dup runs >=12f:', [r for r in runs if r[2] >= 12])
# biggest spikes: in-phrase step check
order = np.argsort(diffs)[::-1][:25]
print('top diff spikes (frame, t, diff, on-boundary?):')
for idx in sorted(order):
    t = idx/24
    onb = any(abs(idx-b) <= 1 for b in bounds)
    print(f'  f{idx} t={t:.2f} diff={diffs[idx]:.1f} boundary={onb}')
