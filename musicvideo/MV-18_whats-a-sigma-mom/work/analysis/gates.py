#!/usr/bin/env python3
"""MV-17 master gates: frames, SEI crf, faststart, AAC, audio agreement,
zero-still enumeration (on the pre-grain master), per-section motion."""
import subprocess, json, sys, re
import numpy as np

ROOT = '/home/hatch/workspace/wubutv-network/musicvideo/MV-17_fridge-light-mystery'
MASTER = sys.argv[1] if len(sys.argv) > 1 else f'{ROOT}/masters/mv17_fridge_light_mystery_16x9.mp4'
PREGRAIN = f'{ROOT}/work/master_pregrain.mp4'

def probe(p):
    r = subprocess.run(['ffprobe', '-v', 'error', '-show_entries',
                        'stream=codec_name,width,height,r_frame_rate',
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
print(f"audio: {[s['codec_name'] for s in a]}  duration: {float(info['format']['duration']):.3f}")
print(f"frames: {frames(MASTER)} (expect 3908)")

raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', MASTER, '-vf', 'select=eq(n\\,10)',
                      '-frames:v', '1', '-c:v', 'copy', '-f', 'h264', '-'],
                     capture_output=True).stdout
m = re.search(rb'crf=([0-9.]+)', raw)
print(f"SEI crf: {m.group(1).decode() if m else 'NOT FOUND'}")
head = open(MASTER, 'rb').read(200000)
print(f"faststart (moov before mdat): {head.find(b'moov') < head.find(b'mdat') and head.find(b'moov') >= 0}")

def pcm(p):
    r = subprocess.run(['ffmpeg', '-v', 'error', '-i', p, '-ac', '1', '-ar', '16000',
                        '-f', 'f32le', '-'], capture_output=True)
    return np.frombuffer(r.stdout, dtype=np.float32)

x = pcm(MASTER); y = pcm(f'{ROOT}/track.mp3')
n = min(len(x), len(y)); x, y = x[:n], y[:n]
def corr(a, b):
    a = a - a.mean(); b = b - b.mean()
    return float(a @ b / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-12))
print(f"audio agreement global: {corr(x, y):.5f}")
worst = 1.0
for i in range(0, n - 160000, 160000):
    worst = min(worst, corr(x[i:i+160000], y[i:i+160000]))
print(f"audio agreement worst-10s: {worst:.5f}")

# zero-still enumeration on PRE-GRAIN master: near-dup runs at 96x54 gray
W, H, FPS = 96, 54, 24
raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', PREGRAIN, '-vf',
                      f'fps={FPS},scale={W}:{H},format=gray', '-f', 'rawvideo', '-'],
                     capture_output=True).stdout
nf = len(raw) // (W * H)
fr = np.frombuffer(raw[:nf * W * H], dtype=np.uint8).reshape(nf, H, W).astype(np.int16)
d = np.abs(np.diff(fr, axis=0)).mean(axis=(1, 2))
runs = []
run = 0
for i, val in enumerate(d):
    if val < 1.0:
        run += 1
    else:
        if run >= 2: runs.append((i - run, run + 1))
        run = 0
if run >= 2: runs.append((len(d) - run, run + 1))
print(f"pregrain frames: {nf}; near-dup runs >=2f: {len(runs)}; longest: {max([r[1] for r in runs], default=0)}")
for s, L in runs[:20]:
    print(f"  run at {s/FPS:.2f}s len {L}f")
# master motion audit: worst near-dup run >=24f anywhere + during vocal spans
grid = json.load(open(f'{ROOT}/work/analysis/grid_lines.json'))
def worst_run(a, b):
    seg = d[int(a*FPS):int(b*FPS)]
    w = r = 0
    for val in seg:
        r = r + 1 if val < 1.0 else 0
        w = max(w, r)
    return w
print(f"master worst near-dup run overall: {worst_run(0, nf/FPS)}f")
bad = [(L['n'], worst_run(L['start'], L['end'])) for L in grid]
bad = [(n, w) for n, w in bad if w >= 24]
print(f"lines with >=24f near-dup run during words: {bad if bad else 'none'}")
