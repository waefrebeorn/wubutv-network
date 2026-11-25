#!/usr/bin/env python3
"""JOINT GATE measurement on work/joined.mp4 + joint-frame harvest."""
import subprocess, json, os
import numpy as np
from PIL import Image

E2 = '/home/hatch/workspace/wubutv-network/new-era/episodes/E2_SHOW-4_the-count'
joined = f'{E2}/work/joined.mp4'
qc = f'{E2}/work/qc'
os.makedirs(qc, exist_ok=True)
os.makedirs(f'{E2}/panels', exist_ok=True)

# full MAE series at 320x180 gray
out = subprocess.run(['ffmpeg','-v','error','-i',joined,'-vf',
                      'scale=320:180,format=gray','-f','rawvideo','-'],
                     capture_output=True).stdout
fs = 320*180
nf = len(out)//fs
fr = np.frombuffer(out[:nf*fs], dtype=np.uint8).reshape(nf,180,320).astype(np.float32)
mae = np.abs(np.diff(fr, axis=0)).mean(axis=(1,2))  # mae[i] = |f[i+1]-f[i]|
print(f'frames decoded: {nf}, mae series: {len(mae)}')

# baseline: adjacent MAE sampled every 24f inside units, excluding 12f at edges
samples = []
for u in range(6):
    base = u*240
    for f in range(base+12, base+228, 24):
        samples.append(mae[f])
baseline95 = float(np.percentile(samples, 95))
print(f'baseline 95th pct: {baseline95:.2f} (n={len(samples)})')

results = {}
for j in range(1, 6):
    cut = j*240
    seam = float(mae[cut-1])
    head = float(np.mean(mae[cut:cut+12]))
    verdict = 'PASS' if seam <= 58 else ('CONDITIONAL' if seam <= 75 else 'FAIL')
    results[f'J{j}'] = {'cut_frame': cut, 'seam_mae': round(seam,2),
                        'band': verdict, 'downstream_head_motion_0_0.5s': round(head,2),
                        'head_motion_ok': bool(head >= 8)}
    print(f'J{j} cut@{cut}: seam MAE {seam:.2f} -> {verdict}; downstream head motion {head:.2f}')

# seam frames + strips (full res)
for j in range(1, 6):
    cut = j*240
    for tag, f in [('a', cut-1), ('b', cut)]:
        subprocess.run(['ffmpeg','-v','error','-i',joined,'-vf',
                        f'select=eq(n\\,{f})','-frames:v','1',
                        f'{qc}/joint{j}_seam{tag}.jpg'], check=True)
    # strip: frames cut-6..cut+5 as 160x90 thumbs in a row
    thumbs = []
    raw = subprocess.run(['ffmpeg','-v','error','-i',joined,'-vf',
                          f"select='between(n\\,{cut-6}\\,{cut+5})',scale=160:90,format=rgb24",
                          '-vsync','0','-f','rawvideo','-'], capture_output=True).stdout
    tfs = 160*90*3
    for i in range(len(raw)//tfs):
        thumbs.append(Image.fromarray(
            np.frombuffer(raw[i*tfs:(i+1)*tfs], dtype=np.uint8).reshape(90,160,3)))
    if thumbs:
        strip = Image.new('RGB', (160*len(thumbs), 90))
        for i, t in enumerate(thumbs):
            strip.paste(t, (i*160, 0))
        strip.save(f'{qc}/joint{j}_strip.jpg')
    print(f'J{j} artefacts written')

# joint frames from segments at frame 228 (J4)
import hashlib
for u in range(1, 6):
    seg = f'{E2}/work/segments/seg_U{u}.mp4'
    dst = f'{E2}/panels/PNL-JOINT-U{u}.png'
    subprocess.run(['ffmpeg','-v','error','-i',seg,'-vf','select=eq(n\\,228)',
                    '-frames:v','1', dst], check=True)
    md5 = hashlib.md5(open(dst,'rb').read()).hexdigest()
    print(f'PNL-JOINT-U{u}.png md5 {md5} (seg_U{u} frame 228)')

print(json.dumps(results, indent=1))
