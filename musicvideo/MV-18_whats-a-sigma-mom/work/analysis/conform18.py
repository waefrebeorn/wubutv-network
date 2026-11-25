#!/usr/bin/env python3
"""MV-18 conform: explicit chunk spec from take-ASR QC (see
TAKE_HISTORY.md). Each chunk: (take, src0, src1, tgt0, tgt1) —
phrase-level smooth warp (setpts), exact frames per scene.
Output: work/segments/S##.mp4 + conform_log.json
Total must equal 3782 frames (157.61s song at 24fps)."""
import json, subprocess, os, hashlib, sys

ROOT = os.path.expanduser('~/workspace/wubutv-network/musicvideo/MV-18_whats-a-sigma-mom')
FPS = 24
C = {
 'S01': [('s01_t1', 0.00, 6.60, 0.00, 6.60)],
 'S02': [('s02_t1', 0.00, 6.40, 6.60, 13.00)],
 'S03': [('s03_t1', 1.22, 2.82, 13.00, 15.58), ('s03_t1', 2.82, 3.42, 15.58, 16.18)],
 'S04': [('s04i_t1', 1.00, 3.58, 16.18, 18.76)],
 'S05': [('s05_t1', 0.00, 6.40, 18.76, 24.64)],
 'S06': [('s06_t1', 0.00, 5.30, 24.64, 27.56)],
 'S07': [('s07_t1', 0.00, 4.02, 27.56, 30.66)],
 'S08': [('s08_t2', 0.00, 5.40, 30.66, 33.64)],
 'S09': [('s09_t1', 0.00, 3.62, 33.64, 36.88)],
 'S10': [('s10_t1', 1.00, 4.08, 36.88, 40.14), ('s10_t1', 5.00, 8.24, 40.14, 44.20)],
 'S11': [('s11_t2', 0.00, 6.20, 44.20, 50.40)],
 'S12': [('s12_t1', 0.00, 6.90, 50.40, 56.72)],
 'S13': [('s13_t1', 0.00, 1.64, 56.72, 58.28), ('s13_t1', 1.64, 2.02, 58.28, 58.44), ('s13_t1', 2.02, 3.60, 58.44, 59.90)],
 'S14': [('s14i_t1', 1.20, 4.02, 59.90, 62.72)],
 'S15': [('s15_t1', 0.00, 7.54, 62.72, 69.20)],
 'S16': [('s16_t1', 0.00, 1.44, 69.20, 70.10), ('s16_t1', 1.44, 2.20, 70.10, 70.24), ('s16_t1', 2.20, 3.44, 70.24, 71.06), ('s16_t1', 3.44, 4.33, 71.06, 71.95)],
 'S17': [('s17_t1', 0.00, 3.11, 71.95, 75.06)],
 'S18': [('s18_t1', 0.00, 3.36, 75.06, 77.80)],
 'S19': [('s19_t2', 0.00, 1.92, 77.80, 78.80), ('s19_t2', 2.42, 4.40, 78.80, 80.76)],
 'S20': [('s20_t1', 0.00, 3.22, 80.76, 83.70)],
 'S21': [('s21_t1', 0.00, 3.82, 83.70, 87.52)],
 'S22': [('s31_t1', 6.90, 10.00, 87.52, 92.16), ('s28_t1', 2.00, 3.86, 92.16, 94.02)],
 'S23': [('s23_t1', 0.00, 6.36, 94.02, 100.38)],
 'S24': [('s24_t1', 0.86, 6.70, 100.38, 104.76), ('s24_t1', 6.70, 9.22, 104.76, 107.28)],
 'S25': [('s25_t1', 0.00, 2.50, 107.28, 110.18)],
 'S26': [('s26i_t2', 0.50, 2.94, 110.18, 112.62)],
 'S27': [('s27_t1', 0.00, 7.32, 112.62, 118.64)],
 'S28': [('s28_t2', 0.64, 3.88, 118.64, 120.30)],
 'S29': [('s29_t1', 0.00, 2.60, 120.30, 121.74), ('s29_t1', 4.72, 7.34, 121.74, 123.60), ('s29_t1', 7.34, 8.54, 123.60, 124.80)],
 'S30': [('s30_t2', 0.00, 4.56, 124.80, 130.78)],
 'S31': [('s31_t1', 0.00, 6.30, 130.78, 137.12), ('s31_t1', 6.30, 6.90, 137.12, 137.72)],
 'S32': [('s32_t1', 0.00, 1.48, 137.72, 138.70), ('s32_t1', 1.48, 2.04, 138.70, 139.18), ('s32_t1', 2.04, 3.34, 139.18, 140.30)],
 'S33': [('s33i_t1', 1.00, 3.76, 140.30, 143.06)],
 'S34': [('s34_t1', 0.00, 6.88, 143.06, 150.60)],
 'S35': [('s35_t1', 0.00, 2.56, 150.60, 152.78)],
 'S36': [('s36_t1', 0.00, 1.66, 152.78, 154.58), ('s36_t1', 1.66, 2.42, 154.58, 155.20), ('s36_t1', 2.42, 4.83, 155.20, 157.61)],
}
# exact frames per scene: round(span*24) with -1 trims on S01/S15/S24/S31/S34
# so the total is exactly 3782.
FRAMES = {'S01': 157, 'S02': 154, 'S03': 76, 'S04': 62, 'S05': 141, 'S06': 70,
          'S07': 74, 'S08': 72, 'S09': 78, 'S10': 176, 'S11': 149, 'S12': 152,
          'S13': 76, 'S14': 68, 'S15': 155, 'S16': 66, 'S17': 75, 'S18': 66,
          'S19': 71, 'S20': 71, 'S21': 92, 'S22': 156, 'S23': 153, 'S24': 165,
          'S25': 70, 'S26': 59, 'S27': 144, 'S28': 40, 'S29': 108, 'S30': 144,
          'S31': 166, 'S32': 62, 'S33': 66, 'S34': 180, 'S35': 52, 'S36': 116}
ZOOM = {'S35'}   # slow push-in lifts the near-frozen locked ECU over the motion floor (MV-17 precedent)
CROP = {'S32', 'S33'}  # 1152x768 (3:2) returns — centre-crop to 16:9

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
only = os.environ.get('MV18_ONLY')
for sid in sorted(C):
    if only and sid not in only.split(','):
        continue
    want = FRAMES[sid]
    chunks = C[sid]
    parts = []
    made = 0
    for i, (take, s0, s1, t0, t1) in enumerate(chunks):
        tp = f'{ROOT}/takes/mv18_{take}.mp4'
        td = dur(tp)
        s1c = min(s1, td)
        n = want - made if i == len(chunks) - 1 else round((t1 - t0) * FPS)
        made += n
        speed = (s1c - s0) / (n / FPS)
        out = f'{ROOT}/work/chunks/{sid}_c{i}.mp4'
        if sid in ZOOM:
            scale = "scale=1344:756,crop=1280:720:x='min(64,n*0.6)':y='min(36,n*0.34)'"
        elif sid in CROP:
            scale = 'scale=1280:720:force_original_aspect_ratio=increase,crop=1280:720'
        else:
            scale = 'scale=1280:720:force_original_aspect_ratio=disable'
        vf = (f'setpts=(PTS-STARTPTS)/{speed:.5f},fps={FPS},'
              f'tpad=stop_mode=clone:stop_duration=0.25,trim=end_frame={n},setpts=PTS-STARTPTS,'
              + scale + ',format=yuv420p')
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
assert total == 3782, f'total {total} != 3782'
json.dump(log, open(f'{ROOT}/work/segments/conform_log.json', 'w'), indent=1)
