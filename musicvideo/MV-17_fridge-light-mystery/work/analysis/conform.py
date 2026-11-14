#!/usr/bin/env python3
"""MV-17 conform: explicit chunk spec from take-ASR QC.
Each chunk: (take, src0, src1, tgt0, tgt1) — phrase-level smooth warp
(setpts), exact frames per scene (last chunk absorbs rounding).
Output: work/segments/S##.mp4 + conform_log.json"""
import json, subprocess, os, hashlib, sys

ROOT = os.path.expanduser('~/workspace/wubutv-network/musicvideo/MV-17_fridge-light-mystery')
FPS = 24
C = {
 'S01': [('s01_t1', 0.50, 5.04, 0.00, 4.54)],
 'S02': [('s02_t2', 0.75, 3.75, 4.54, 7.54)],
 'S03': [('s03_t2', 0.00, 6.57, 7.54, 12.04), ('s03_t2', 6.57, 7.33, 12.04, 12.80)],
 'S04': [('s04_t1', 0.99, 5.00, 12.80, 16.60)],
 'S05': [('s05_t1', 0.57, 5.33, 16.60, 20.78)],
 'S06': [('s06_t2', 0.00, 4.97, 20.78, 24.92)],
 'S07': [('s07_t2', 0.00, 4.23, 24.92, 28.02)],
 'S08': [('s08_t1', 3.01, 6.93, 28.02, 32.76), ('s08_t1', 6.93, 7.89, 32.76, 33.72)],
 'S09': [('s09_t1', 0.00, 5.00, 33.72, 38.34)],
 'S10': [('s10_t2', 0.98, 5.00, 38.34, 42.36)],
 'S11': [('s11_t1', 0.00, 1.37, 42.36, 43.46), ('s11_t1', 2.75, 3.99, 43.46, 44.44)],
 'S12': [('s12_t1', 0.00, 3.52, 44.44, 46.64)],
 'S13': [('s13_t2', 0.00, 4.95, 46.64, 51.34)],
 'S14': [('s14_t1', 0.00, 6.68, 51.34, 58.02)],
 'S15': [('s15_t1', 0.00, 4.07, 58.02, 63.24)],
 'S16': [('s16_t1', 0.88, 5.00, 63.24, 67.36)],
 'S17': [('s17_t1', 0.00, 4.23, 67.36, 71.28)],
 'S18': [('s18_t1', 0.00, 3.85, 71.28, 75.38)],
 'S19': [('s19_t2', 0.00, 2.35, 75.38, 79.20)],
 'S20': [('s20_t1', 3.53, 9.95, 79.20, 84.50)],
 'S21': [('s21_t1', 0.00, 4.37, 84.50, 89.24)],
 'S22': [('s22_t1', 1.00, 7.16, 89.24, 95.40)],
 'S23': [('s23_t1', 0.00, 2.07, 95.40, 97.56)],
 'S24': [('s24_t1', 0.00, 5.35, 97.56, 102.38), ('s24_t1', 5.35, 7.73, 102.38, 104.76)],
 'S25': [('s25_t2', 0.00, 3.35, 104.76, 108.64)],
 'S26': [('s26_t1', 0.00, 4.05, 108.64, 113.08)],
 'S27': [('s25_t1', 2.00, 5.32, 113.08, 116.40), ('s27_t1', 0.00, 3.41, 116.40, 119.30)],
 'S28': [('s28_t1', 0.50, 8.28, 119.30, 127.08)],
 'S29': [('s29_t1', 0.00, 5.00, 127.08, 131.68)],
 'S30': [('s30_t1', 0.00, 4.51, 131.68, 135.90)],
 'S31': [('s31_t1', 0.43, 4.57, 135.90, 140.04)],
 'S32': [('s32_t1', 0.00, 6.91, 140.04, 144.70), ('s32_t1', 6.91, 9.95, 144.70, 148.68)],
 'S33': [('s33_t1', 2.49, 5.00, 148.68, 153.26)],
 'S34': [('s34_t1', 0.00, 3.19, 153.26, 157.66), ('s34_t1', 7.08, 9.95, 157.66, 162.816)],
}
ZOOM = {'S16', 'S19', 'S20'}  # slow push-in lifts near-frozen locked takes over the motion floor
smap = {s['sc']: s for s in json.load(open(f'{ROOT}/work/analysis/scene_map.json'))['scenes']}

def dur(p):
    return float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries',
        'format=duration', '-of', 'csv=p=0', p]).decode().strip())

def frames(p):
    return int(subprocess.check_output(['ffprobe', '-v', 'error', '-select_streams', 'v:0',
        '-count_frames', '-show_entries', 'stream=nb_read_frames', '-of', 'csv=p=0', p]).decode().strip())

def md5(p):
    return hashlib.md5(open(p, 'rb').read()).hexdigest()

os.makedirs(f'{ROOT}/work/segments', exist_ok=True)
os.makedirs(f'{ROOT}/work/chunks', exist_ok=True)
log = []
total = 0
only = os.environ.get('MV17_ONLY')
for sid in sorted(C):
    if only and sid not in only.split(','):
        continue
    sc = smap[sid]
    want = round((sc['end'] - sc['start']) * FPS) + {'S07': 1, 'S10': 1, 'S18': 1}.get(sid, 0)  # frame-bonus: total must equal round(162.816*24)=3908
    chunks = C[sid]
    parts = []
    made = 0
    for i, (take, s0, s1, t0, t1) in enumerate(chunks):
        tp = f'{ROOT}/takes/mv17_{take}.mp4'
        td = dur(tp)
        s1c = min(s1, td)
        n = want - made if i == len(chunks) - 1 else round((t1 - t0) * FPS)
        made += n
        speed = (s1c - s0) / (n / FPS)
        out = f'{ROOT}/work/chunks/{sid}_c{i}.mp4'
        scale = ('scale=1280:720:force_original_aspect_ratio=disable' if sid not in ZOOM
                 else "scale=1344:756,crop=1280:720:x='min(64,n*0.6)':y='min(36,n*0.34)'")
        vf = f'setpts=(PTS-STARTPTS)/{speed:.5f},fps={FPS},' + scale + ',format=yuv420p'
        r = subprocess.run(['ffmpeg', '-y', '-v', 'error', '-ss', f'{s0}', '-i', tp,
                            '-vf', vf, '-frames:v', str(n),
                            '-an', '-c:v', 'libx264', '-preset', 'medium', '-crf', '12', out],
                           capture_output=True, text=True)
        if r.returncode != 0:
            print(f'{sid} chunk{i} FAILED: {r.stderr[-300:]}'); sys.exit(1)
        got = frames(out)
        assert got == n, f'{sid} chunk{i}: {got} != {n}'
        parts.append(out)
        log.append({'scene': sid, 'chunk': i, 'take': take, 'src': [s0, s1c],
                    'tgt': [t0, t1], 'speed': round(speed, 3), 'frames': n, 'md5': md5(out)})
        print(f'{sid} c{i} {take} [{s0}-{s1c}] -> {n}f @ {speed:.3f}x')
    seg = f'{ROOT}/work/segments/{sid}.mp4'
    if len(parts) == 1:
        os.replace(parts[0], seg)
    else:
        lst = f'{ROOT}/work/chunks/{sid}_list.txt'
        open(lst, 'w').write(''.join(f"file '{p}'\n" for p in parts))
        subprocess.run(['ffmpeg', '-y', '-v', 'error', '-f', 'concat', '-safe', '0', '-i', lst,
                        '-c', 'copy', seg], check=True)
    got = frames(seg)
    assert got == want, f'{sid}: segment {got} != {want}'
    total += got
    print(f'{sid} segment OK: {got} frames, md5 {md5(seg)}')
print(f'TOTAL segment frames: {total}')
json.dump(log, open(f'{ROOT}/work/segments/conform_log.json', 'w'), indent=1)
