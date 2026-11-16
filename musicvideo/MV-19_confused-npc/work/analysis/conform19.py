#!/usr/bin/env python3
"""MV-19 conform: explicit chunk spec authored from take-ASR word
times vs song word times (see TAKE_HISTORY.md + SCENE_PLAN.md).
Each chunk: (take, src0, src1, tgt0, tgt1) — phrase-level smooth
warp (setpts), exact frames per scene. Chunks tile each scene's
target span in order; src may jump (skip-cuts / word-level
reassembly — all disclosed in GATE_LOG.md).
Output: work/segments/S##.mp4 + conform_log.json
Total must equal 3686 frames (153.600s song at 24fps, MV-18 method:
round(span*24) per scene, S36 absorbs -1)."""
import json, subprocess, os, hashlib, sys

ROOT = os.path.expanduser('~/workspace/wubutv-network/musicvideo/MV-19_confused-npc')
FPS = 24
C = {
 # head = post-line settle borrowed (mouth closed, verified frame)
 'S01': [('s01_t1', 2.50, 5.00, 0.00, 1.98), ('s01_t1', 0.00, 2.40, 1.98, 3.90)],
 'S02': [('s02_t1', 0.00, 2.82, 3.90, 7.08), ('s02_t1', 2.82, 5.10, 7.08, 8.60)],
 'S03': [('s03_t2', 0.00, 4.35, 8.60, 12.82)],
 'S04': [('s04_t1', 0.00, 4.95, 12.82, 17.28)],
 'S05': [('s05_t1', 0.00, 4.55, 17.28, 21.88)],
 'S06': [('s06_t1', 0.00, 4.60, 21.88, 26.62)],
 'S07': [('s07_t1', 0.00, 1.49, 26.62, 28.49), ('s07_t1', 1.49, 3.13, 28.49, 29.46),
         ('s07_t1', 3.13, 4.60, 29.46, 31.52)],
 # head trimmed to the last pats; phrase split at word level (2.16x/2.03x disclosed)
 'S08': [('s08_t1', 1.55, 3.10, 31.52, 32.94), ('s08_t1', 3.10, 4.44, 32.94, 33.56),
         ('s08_t1', 4.44, 5.70, 33.56, 34.18)],
 'S09': [('s09_t2', 0.00, 5.45, 34.18, 38.66)],
 'S10': [('s10_t1', 0.00, 4.75, 38.66, 43.12)],
 'S11': [('s11_t2', 0.00, 1.79, 43.12, 44.32), ('s11_t2', 1.79, 4.30, 44.32, 46.98)],
 'S12': [('s12_t1', 0.00, 7.00, 46.98, 53.00)],
 # head at 0.55x (disclosed, wordless daylight flood)
 'S13': [('s13_t1', 0.00, 1.76, 53.00, 56.20), ('s13_t1', 1.76, 3.85, 56.20, 57.68)],
 # tail-borrow stare + press beat + word-split line
 'S13B': [('s13b_t1', 2.95, 5.00, 57.68, 60.30), ('s13b_t1', 0.80, 1.72, 60.30, 61.20),
          ('s13b_t1', 0.00, 0.80, 61.20, 61.85), ('s13b_t1', 1.72, 2.45, 61.85, 62.40)],
 # word-level reassembly: tail-borrow head, words exact, freeze fills
 # the gap, rotate snap in the tail (all disclosed)
 'S14': [('s14_t1', 8.20, 10.00, 62.40, 63.70), ('s14_t1', 0.00, 0.55, 63.70, 64.30),
         ('s14_t1', 2.40, 3.20, 64.30, 64.90), ('s14_t1', 0.55, 2.40, 64.90, 67.30),
         ('s14_t1', 3.20, 3.84, 67.30, 68.56), ('s14_t1', 3.84, 4.40, 68.56, 69.16),
         ('s14_t1', 7.36, 8.08, 69.16, 69.76), ('s14_t1', 4.40, 5.85, 69.76, 70.48)],
 # action gaps cut (door swing / kneel / stare / door walk) — words at <=1.85x
 'S15': [('s15_t2', 0.00, 0.60, 70.48, 71.08), ('s15_t2', 1.90, 2.55, 71.08, 71.66)],
 'S16': [('s16_t1', 0.00, 0.50, 71.66, 71.96), ('s16_t1', 1.46, 2.26, 71.96, 72.46),
         ('s16_t1', 2.26, 2.90, 72.46, 72.84)],
 'S17': [('s17_t1', 1.02, 1.50, 72.84, 73.12), ('s17_t1', 1.50, 2.22, 73.12, 73.62),
         ('s17_t1', 2.22, 2.90, 73.62, 73.99)],
 'S18': [('s18_t1', 0.00, 0.50, 73.99, 74.28), ('s18_t1', 0.94, 1.45, 74.28, 74.56),
         ('s18_t1', 1.52, 1.90, 74.56, 74.78), ('s18_t1', 1.90, 2.45, 74.78, 75.08)],
 'S19': [('s19_t2', 0.00, 2.45, 75.08, 76.38)],
 # shrug-rise gap cut (emote snap)
 'S19B': [('s19b_t1', 0.00, 0.62, 76.38, 76.92), ('s19b_t1', 2.68, 3.70, 76.92, 77.50)],
 'S20': [('s20_t1', 1.06, 5.45, 77.50, 79.82)],
 'S21': [('s21_t1', 0.00, 2.16, 79.82, 81.07), ('s21_t1', 2.38, 3.20, 81.07, 81.60),
         ('s21_t1', 3.70, 4.35, 81.60, 82.06), ('s21_t1', 4.60, 6.55, 82.06, 84.10)],
 'S22': [('s22_t1', 3.15, 4.72, 84.10, 85.34), ('s22_t1', 4.72, 7.25, 85.34, 86.80)],
 'S23': [('s23_t3', 0.00, 6.95, 86.80, 91.18)],
 'S24': [('s24_t1', 0.00, 4.65, 91.18, 95.68)],
 'S25': [('s25_t1', 0.00, 2.35, 95.68, 96.90)],
 'S25B': [('s25b_t1', 0.00, 0.62, 96.90, 97.25), ('s25b_t1', 1.46, 2.05, 97.25, 97.68),
          ('s25b_t1', 2.12, 2.75, 97.68, 98.02)],
 'S26': [('s26_t1', 0.00, 2.40, 98.02, 99.60)],
 # skip-cut fragments (landings live in the dropped gaps)
 'S27': [('s27_t1', 0.00, 2.16, 99.60, 101.52), ('s27_t1', 2.16, 4.10, 101.52, 102.84),
         ('s27_t1', 5.58, 6.10, 102.84, 103.52), ('s27_t1', 6.10, 7.70, 103.52, 105.68)],
 'S28': [('s28_t1', 0.00, 2.30, 105.68, 107.38), ('s28_t1', 2.30, 2.76, 107.38, 108.28),
         ('s28_t1', 2.76, 4.80, 108.28, 109.42)],
 'S28B': [('s28b_t1', 0.00, 0.48, 109.42, 109.68), ('s28b_t1', 1.50, 2.10, 109.68, 110.02),
          ('s28b_t1', 2.10, 2.56, 110.02, 110.42)],
 'S29': [('s29_t1', 0.00, 2.20, 110.42, 112.92), ('s29_t1', 2.20, 4.60, 112.92, 115.14)],
 'S30': [('s30_t1', 6.35, 7.65, 115.14, 116.16), ('s30_t1', 0.00, 4.62, 116.16, 119.38),
         ('s30_t1', 4.62, 6.35, 119.38, 120.92)],
 'S31': [('s31_t5', 0.00, 6.40, 120.92, 125.42)],
 'S32': [('s32_t1', 0.00, 2.05, 125.42, 126.65), ('s32_t1', 3.14, 3.62, 126.65, 127.02),
         ('s32_t1', 4.02, 4.52, 127.02, 127.40), ('s32_t1', 4.56, 5.02, 127.40, 127.74)],
 'S33': [('s33_t1', 0.00, 2.30, 127.74, 129.30)],
 'S34': [('s34_t2', 0.00, 1.86, 129.30, 131.24), ('s34_t2', 1.86, 4.45, 131.24, 132.56),
         ('s34_t2', 5.46, 6.04, 132.56, 133.20), ('s34_t2', 6.04, 7.72, 133.20, 135.18)],
 'S35': [('s35_t1', 0.55, 3.52, 135.18, 137.98), ('s35_t1', 3.52, 5.65, 137.98, 139.60),
         ('s35_t1', 5.65, 9.70, 139.60, 144.18)],
 # head at 0.41x (disclosed sub-floor, wordless settle, zoomed);
 # tail zoomed door close
 'S36': [('s36_t1', 3.41, 4.60, 144.18, 147.06), ('s36_t1', 4.60, 7.10, 147.06, 149.26),
         ('s36_t1', 7.30, 10.00, 149.26, 153.60)],
}
FRAMES = {'S01': 94, 'S02': 113, 'S03': 101, 'S04': 107, 'S05': 110, 'S06': 114,
          'S07': 118, 'S08': 64, 'S09': 108, 'S10': 107, 'S11': 93, 'S12': 144,
          'S13': 112, 'S13B': 113, 'S14': 194, 'S15': 28, 'S16': 28, 'S17': 28,
          'S18': 26, 'S19': 31, 'S19B': 27, 'S20': 56, 'S21': 103, 'S22': 65,
          'S23': 105, 'S24': 108, 'S25': 29, 'S25B': 27, 'S26': 38, 'S27': 146,
          'S28': 90, 'S28B': 24, 'S29': 113, 'S30': 139, 'S31': 108, 'S32': 56,
          'S33': 37, 'S34': 141, 'S35': 216, 'S36': 225}
ZOOM = {'S06': 'g', 'S11': 'g', 'S21': 's', 'S23': 'g', 'S29': 'g', 'S33': 'g'}
ZOOM_CHUNKS = {'S36': {0, 2}}   # head + tail chunks only

def dur(p):
    return float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries',
        'format=duration', '-of', 'csv=p=0', p]).decode().strip())

def frames(p):
    return int(subprocess.check_output(['ffprobe', '-v', 'error', '-select_streams', 'v:0',
        '-count_frames', '-show_entries', 'stream=nb_read_frames', '-of', 'csv=p=0', p]).decode().strip())

def md5(p):
    return hashlib.md5(open(p, 'rb').read()).hexdigest()

def scale_for(sid, ci):
    z = ZOOM.get(sid) or ('g' if ci in ZOOM_CHUNKS.get(sid, set()) else None)
    if z == 'g':
        return "scale=1344:896,crop=1280:720:x='32+min(32,n*0.5)':y=88"
    if z == 's':
        return "scale=1536:1024,crop=1280:720:x='128+min(128,n*1.2)':y=152"
    return 'scale=1280:854,crop=1280:720:x=0:y=67'

os.makedirs(f'{ROOT}/work/segments', exist_ok=True)
os.makedirs(f'{ROOT}/work/chunks', exist_ok=True)
log = []
total = 0
only = os.environ.get('MV19_ONLY')
for sid in sorted(C):
    if only and sid not in only.split(','):
        continue
    want = FRAMES[sid]
    chunks = C[sid]
    parts = []
    made = 0
    for i, (take, s0, s1, t0, t1) in enumerate(chunks):
        tp = f'{ROOT}/takes/mv19_{take}.mp4'
        td = dur(tp)
        s1c = min(s1, td)
        n = want - made if i == len(chunks) - 1 else round((t1 - t0) * FPS)
        made += n
        speed = (s1c - s0) / (n / FPS)
        out = f'{ROOT}/work/chunks/{sid}_c{i}.mp4'
        vf = (f'setpts=(PTS-STARTPTS)/{speed:.5f},fps={FPS},'
              f'tpad=stop_mode=clone:stop_duration=0.25,trim=end_frame={n},setpts=PTS-STARTPTS,'
              + scale_for(sid, i) + ',format=yuv420p')
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
        print(f'{sid} c{i} {take} [{s0}-{s1c}] -> {n}f @ {speed:.3f}x', flush=True)
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
    print(f'{sid} segment OK: {got} frames, md5 {md5(seg)}', flush=True)
print(f'TOTAL segment frames: {total}')
assert total == 3686, f'total {total} != 3686'
json.dump(log, open(f'{ROOT}/work/segments/conform_log.json', 'w'), indent=1)
