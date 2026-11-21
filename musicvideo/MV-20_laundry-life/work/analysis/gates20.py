#!/usr/bin/env python3
"""MV-20 master gates: frames (3888), SEI crf, faststart, AAC,
audio agreement vs track.mp4 audio, zero-still enumeration on the
pre-grain master (near-dup = mean abs diff < 1.0 at 96x54 gray;
FAIL on any run >= 24f). Adapted from MV-19 gates19.py."""
import subprocess, json, sys, re
import numpy as np

ROOT = '/home/hatch/workspace/wubutv-network/musicvideo/MV-20_laundry-life'
MASTER = sys.argv[1] if len(sys.argv) > 1 else f'{ROOT}/masters/mv20_laundry_life_16x9.mp4'
PREGRAIN = f'{ROOT}/work/master_pregrain.mp4'

def probe(p):
    r = subprocess.run(['ffprobe', '-v', 'error', '-show_entries',
                        'stream=codec_name,width,height,r_frame_rate,sample_rate,channels',
                        '-show_entries', 'format=duration', '-of', 'json', p],
                       capture_output=True, text=True)
    return json.loads(r.stdout)

def frames(p):
    return int(subprocess.check_output(['ffprobe', '-v', 'error', '-select_streams', 'v:0',
        '-count_frames', '-show_entries', 'stream=nb_read_frames', '-of', 'csv=p=0', p]).decode().strip())

info = probe(MASTER)
v = [s for s in info['streams'] if 'width' in s][0]
a = [s for s in info['streams'] if s['codec_name'] in ('aac', 'mp3')]
print(f"video: {v['codec_name']} {v['width']}x{v['height']} @{v['r_frame_rate']}")
print(f"audio: {[(s['codec_name'], s.get('sample_rate'), s.get('channels')) for s in a]}  duration: {float(info['format']['duration']):.3f}")
print(f"frames: {frames(MASTER)} (expect 3888)")

raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', MASTER, '-map', '0:v:0',
                      '-c:v', 'copy', '-f', 'h264', '-'],
                     capture_output=True).stdout[:4000000]
m = re.search(rb'crf=([0-9.]+)', raw)
print(f"SEI crf: {m.group(1).decode() if m else 'NOT FOUND'}")
head = open(MASTER, 'rb').read(200000)
print(f"faststart (moov before mdat): {head.find(b'moov') < head.find(b'mdat') and head.find(b'moov') >= 0}")

def pcm(p):
    r = subprocess.run(['ffmpeg', '-v', 'error', '-i', p, '-ac', '1', '-ar', '16000',
                        '-f', 'f32le', '-'], capture_output=True)
    return np.frombuffer(r.stdout, dtype=np.float32)

x = pcm(MASTER); y = pcm(f'{ROOT}/track.mp4')
n = min(len(x), len(y)); x, y = x[:n], y[:n]
def corr(a, b):
    a = a - a.mean(); b = b - b.mean()
    return float(a @ b / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-12))
g = corr(x, y)
print(f"audio agreement global: {g:.5f}")
worst = 1.0; worst_i = -1
for i in range(0, n - 160000, 160000):
    c = corr(x[i:i+160000], y[i:i+160000])
    if c < worst: worst, worst_i = c, i // 16000
print(f"audio agreement worst-10s: {worst:.5f} (window at {worst_i}s)")

W, H, FPS = 96, 54, 24
raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', PREGRAIN, '-vf',
                      f'fps={FPS},scale={W}:{H},format=gray', '-f', 'rawvideo', '-'],
                     capture_output=True).stdout
nf = len(raw) // (W * H)
fr = np.frombuffer(raw[:nf * W * H], dtype=np.uint8).reshape(nf, H, W).astype(np.int16)
d = np.abs(np.diff(fr, axis=0)).mean(axis=(1, 2))
near = d < 1.0
runs = []; run = 0; start = 0
for i, val in enumerate(near):
    if val and run == 0: start = i
    run = run + 1 if val else 0
    if not val and run > 0: runs.append((start, run))
    if i == len(near) - 1 and run > 0: runs.append((start, run))
    if not val: run = 0
big = [(s, l) for s, l in runs if l >= 12]
worst_run = max([l for _, l in runs], default=0)
print(f"zero-still: frames scanned {nf}, worst near-dup run {worst_run}f ({worst_run/24:.2f}s)")
for s, l in big:
    print(f"  run >= 12f: start frame {s} ({s/24:.2f}s), length {l}f ({l/24:.2f}s)")
print(f"zero-still verdict: {'FAIL' if worst_run >= 24 else 'PASS'} (bar: no run >= 24f)")
