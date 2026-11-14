#!/usr/bin/env python3
"""Audio identity: decoded master audio vs track.mp3.
Decode both to 16k mono f32 via ffmpeg pipe, cross-correlate for lag,
report correlation at lag 0 and best lag.
"""
import subprocess, sys
import numpy as np
def decode(path, sr=16000):
    raw = subprocess.run(['ffmpeg','-v','error','-i',path,'-ac','1','-ar',str(sr),
                          '-f','s16le','-'], capture_output=True).stdout
    return np.frombuffer(raw, dtype=np.int16).astype(np.float32)/32768.0
a = decode(sys.argv[1])   # master
b = decode(sys.argv[2])   # track.mp3
n = min(len(a), len(b))
a, b = a[:n], b[:n]
print(f'samples compared: {n} ({n/16000:.3f}s)')
# lag via cross-correlation on a 30s slice (fast)
sl = slice(16000*30, 16000*60)
x, y = a[sl], b[sl]
x = x - x.mean(); y = y - y.mean()
cc = np.correlate(x, y, mode='full')
lags = np.arange(-len(x)+1, len(x))
best = lags[np.argmax(cc)]
print(f'best lag (30-60s slice): {best} samples = {best/16000:.4f}s')
def corr(u, v):
    u = u-u.mean(); v = v-v.mean()
    return float(np.dot(u, v)/ (np.linalg.norm(u)*np.linalg.norm(v)))
print(f'correlation at lag 0 (full): {corr(a, b):.6f}')
# max abs sample diff
print(f'max |diff| lag0: {np.max(np.abs(a-b)):.4f}  mean |diff|: {np.mean(np.abs(a-b)):.6f}')
