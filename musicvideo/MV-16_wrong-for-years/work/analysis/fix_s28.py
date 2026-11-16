#!/usr/bin/env python3
"""MV-16 REBUILD S28 tail fix. Motion probe on the first assembled
master showed the take's own motion dies at ~8.5s (held pose), so the
original tail chunk (src 5.54-10.00 at 0.68x) froze the master's last
~2.2s. Fix: tail-A uses only the live span (src 5.54-8.50 -> tgt
191.50-196.10, 0.64x: walk + dawn flood + pose strike); tail-B is a
slow push-in (zoompan 1.00->1.10 over 48f) on the take's held-pose
frame for the post-chant tail music (196.10-198.10, no words) — the
final frame rhymes with frame 0, in motion. Segment stays 321f.
Also rewrites S28's entries in work/segments/conform_log.json."""
import json, subprocess, sys, os

ROOT = os.path.expanduser('~/workspace/wubutv-network/musicvideo/MV-16_wrong-for-years')
FPS = 24
TAKE = f'{ROOT}/takes/mv16_s28_t3.mp4'
words = json.load(open(f'{ROOT}/work/swing/mv16_s28_t3_words.json'))['words']
assert len(words) == 9
tdur = float(subprocess.check_output(['ffprobe','-v','error','-show_entries',
    'format=duration','-of','csv=p=0', TAKE]).decode().strip())
wend = words[-1]['end']          # 5.24
pose_png = f'{ROOT}/work/qc/s28_pose.png'
subprocess.run(['ffmpeg','-v','error','-ss','8.75','-i',TAKE,'-frames:v','1',
                pose_png,'-y'], check=True)
# (src0, src1, tgt0, tgt1, label) for the four take-video chunks
CH = [
    (words[0]['start'], words[3]['start'], 184.73, 186.14, 'L83'),
    (words[3]['start'], words[6]['start'], 186.14, 189.28, 'L84'),
    (words[6]['start'], wend + 0.30,       189.28, 191.50, 'L85/86'),
    (wend + 0.30,       8.50,              191.50, 196.10, 'tail-A'),
]
fc = []
for i, (s0, s1, t0, t1, lab) in enumerate(CH):
    src_d, tgt_d = s1 - s0, t1 - t0
    print(f'S28 {lab}: src {s0:.2f}-{s1:.2f} -> tgt {t0:.2f}-{t1:.2f} factor {src_d/tgt_d:.2f}')
    fc.append(f'[0:v]trim=start={s0:.3f}:end={s1:.3f},setpts={tgt_d/src_d:.6f}*(PTS-STARTPTS),'
              f'scale=1280:720,fps=24,setsar=1,format=yuv420p[v{i}]')
fc.append("[1:v]zoompan=z='1+0.10*on/47':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
          ":d=48:s=1280x720:fps=24,setsar=1,format=yuv420p[v4]")
print('S28 tail-B: zoompan push-in 1.00->1.10 on pose frame -> tgt 196.10-198.10 (48f)')
filt = ';'.join(fc) + ';' + ''.join(f'[v{i}]' for i in range(5)) + \
       'concat=n=5:v=1:a=0,trim=end_frame=321,setpts=N/(24*TB)[out]'
out = f'{ROOT}/work/segments/S28.mp4'
r = subprocess.run(['ffmpeg','-v','error','-i',TAKE,'-i',pose_png,
        '-filter_complex',filt,'-map','[out]','-c:v','libx264','-crf','12',
        '-preset','medium','-an', out + '.tmp.mp4','-y'],
        capture_output=True, text=True)
if r.returncode != 0:
    print('FFMPEG FAIL', r.stderr[-800:]); sys.exit(1)
os.replace(out + '.tmp.mp4', out)
nf = int(subprocess.check_output(['ffprobe','-v','error','-count_frames','-show_entries',
    'stream=nb_read_frames','-of','csv=p=0', out]).decode().strip())
print(f'S28: {nf}f (target 321)')
assert nf == 321
# keep the conform log honest: replace S28 chunk entries
logp = f'{ROOT}/work/segments/conform_log.json'
log = [e for e in json.load(open(logp)) if e.get('scene') != 'S28']
for (s0, s1, t0, t1, lab) in CH:
    f = (s1 - s0) / (t1 - t0)
    log.append({'scene': 'S28', 'chunk': lab, 'src': [round(s0,2), round(s1,2)],
                'tgt': [round(t0,2), round(t1,2)], 'factor': round(f,3),
                'flag': bool(f > 2.2 or f < 0.5)})
log.append({'scene': 'S28', 'chunk': 'tail-B', 'src': 'pose frame @8.75 (zoompan)',
            'tgt': [196.10, 198.10], 'factor': None, 'flag': False,
            'note': 'push-in 1.00->1.10 replaces frozen held-pose tail (motion probe fix)'})
json.dump(log, open(logp,'w'), indent=1)
print('conform_log.json S28 entries updated')
