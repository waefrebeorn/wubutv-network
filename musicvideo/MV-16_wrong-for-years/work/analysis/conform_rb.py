#!/usr/bin/env python3
"""MV-16 REBUILD conform: per-scene chunk warps from the NEW performed
grid (86 lines, correct take) + take ASR. Adapted from conform.py
(first build) — same machinery, new tables:
- SHIP: S22 -> s22_t3, S28 -> s28_t3 (re-fired for the new BR/OUT
  content); all other ship takes unchanged (same line texts, re-timed).
- SKIP: take words before the slot's first group (S10: the (oh-oh)
  vocalise the new grid doesn't carry; S13: the NSM x2 chant — the new
  POST slot is WFY x2 only, the skipped chant fills the head pocket;
  S23: the (yeah) before 'And I'm still going').
- S11 / S28: custom chunk maps (data-driven from word times).
- S14: room-line span capped at word end + 0.10 and LAST_CAP 8.70 on
  the (yeah) shout — same treatment the first build gave this take.
Output: work/segments/S##.mp4 (silent, 1280x720, 24fps, exact frames)
+ work/segments/conform_log.json."""
import json, subprocess, sys, os

ROOT = os.path.expanduser('~/workspace/wubutv-network/musicvideo/MV-16_wrong-for-years')
FPS = 24
SHIP = {
 'S01':'s01_t3','S02':'s02_t1','S03':'s03_t1','S04':'s04_t2','S05':'s05_t3',
 'S06':'s06_t2','S07':'s07_t2','S08':'s08_t2','S09':'s09_t1','S10':'s10_t1',
 'S11':'s11_t1','S12':'s12_t2','S13':'s13_t1','S14':'s14_t2','S15':'s15_t2',
 'S16':'s16_t2','S17':'s17_t2','S18':'s18_t1','S19':'s19_t2','S20':'s20_t1',
 'S21':'s21_t2','S22':'s22_t3','S23':'s23_t2','S24':'s24_t1','S25':'s25_t1',
 'S26':'s26_t1','S27':'s27_t2','S28':'s28_t3'}
EXPECT_LINES = {'S01':3,'S02':3,'S03':3,'S04':3,'S05':3,'S06':2,'S07':4,
 'S08':4,'S09':3,'S10':3,'S11':3,'S12':3,'S13':2,'S14':3,'S15':4,'S16':2,
 'S17':4,'S18':3,'S19':3,'S20':3,'S21':3,'S22':5,'S23':1,'S24':3,'S25':3,
 'S26':3,'S27':3,'S28':4}
SKIP = {'S10': 2, 'S13': 6, 'S23': 1}
REORDER = {'S03','S20','S26'}   # take groups [WFY][AISG][WFY] -> song [0,2,1]
HEAD_TRIM = {'S04': 0.30}       # skip closed-mouth head pose (take property)
LAST_CAP = {'S14': 8.70}        # cap (yeah) shout source end (take property)
SPAN_END_CAP = {'S14': {1: 0.10}}  # group idx -> source end = word end + this

grid = json.load(open(f'{ROOT}/work/analysis/grid_lines.json'))
smap = json.load(open(f'{ROOT}/work/analysis/scene_map.json'))['scenes']
ONLY = os.environ.get('MV16_ONLY')
if ONLY:
    keep = set(ONLY.split(','))
    smap = [s for s in smap if s['sc'] in keep]

def dur(path):
    return float(subprocess.check_output(['ffprobe','-v','error','-show_entries',
        'format=duration','-of','csv=p=0', path]).decode().strip())

def wc(text):
    return len(text.replace('—',' ').split())

log = []
os.makedirs(f'{ROOT}/work/segments', exist_ok=True)
total_frames = 0
for sc in smap:
    sid = sc['sc']; ws, we = sc['start'], sc['end']
    take = SHIP[sid]
    tpath = f'{ROOT}/takes/mv16_{take}.mp4'
    tdur = dur(tpath)
    words = json.load(open(f'{ROOT}/work/swing/mv16_{take}_words.json'))['words']
    lines = [L for L in grid if ws - 0.01 <= L['start'] < we - 0.01]
    assert len(lines) == EXPECT_LINES[sid], f'{sid}: {len(lines)} lines in window'
    base = SKIP.get(sid, 0)
    chunks = None
    leftover = 0
    if sid == 'S11':
        # take groups: [0:4] WFY+oh fused, [4:8] AISG, [8:11] clean WFY,
        # [11:15] AISG (unused). Song: WFY / WFY / AISG.
        G1, G2, G3 = words[0:4], words[4:8], words[8:11]
        assert G1[0]['w'].lower().startswith('wrong') and G3[0]['w'].lower().startswith('wrong')
        assert G2[0]['w'].lower() == 'and'
        L32, L33, L34 = lines
        chunks = [
            (G3[0]['start'], G3[-1]['end'] + 0.15, L32['start'], L33['start'], 'L32'),
            (G1[0]['start'], G1[-1]['end'] + 0.15, L33['start'], L34['start'], 'L33'),
            (G2[0]['start'], min(tdur, G2[-1]['end'] + 0.15), L34['start'], we, 'L34')]
        leftover = len(words) - 15
    elif sid == 'S28':
        # new take sings NSM / NSM / WFY; the song's (yeah) adlib (L86)
        # has no take words -> merged into L85's span, then a slow dawn
        # tail chunk covers the song tail (take's held pose, in motion).
        assert len(words) == 9
        L83, L84, L85, _L86 = lines
        wend = words[-1]['end']
        chunks = [
            (words[0]['start'], words[3]['start'], ws, L84['start'], 'L83'),
            (words[3]['start'], words[6]['start'], L84['start'], L85['start'], 'L84'),
            (words[6]['start'], wend + 0.30, L85['start'], 191.50, 'L85/86'),
            (wend + 0.30, tdur, 191.50, we, 'tail')]
    else:
        eff = [(L['start'], L['end'], wc(L['text']), f'L{L["n"]}') for L in lines]
        counts = [e[2] for e in eff]
        groups = []; idx = base
        if sid in REORDER:
            for a, b in [(0,3),(3,7),(7,10)]:
                groups.append(words[base+a:base+b])
            idx = base + 10
        else:
            for c in counts:
                g = words[idx:idx+c]
                assert len(g) == c, f'{sid}: word starve at {c}'
                groups.append(g); idx += c
        leftover = len(words) - idx
        spans = []
        for i, g in enumerate(groups):
            s0 = g[0]['start']
            s1 = groups[i+1][0]['start'] if i+1 < len(groups) else g[-1]['end']
            if sid in SPAN_END_CAP and i in SPAN_END_CAP[sid]:
                s1 = g[-1]['end'] + SPAN_END_CAP[sid][i]
            spans.append([s0, s1, g[-1]['end']])
        if sid in REORDER:
            spans = [spans[0], spans[2], spans[1]]
        chunks = []
        first_src = spans[0][0]
        pocket = eff[0][0] - ws
        if pocket > 0.10:
            if first_src > pocket + 0.05:
                hs = first_src - pocket
            else:
                hs = min(tdur - pocket, words[idx-1]['end'] + 0.30)
            chunks.append((hs, hs + pocket, ws, eff[0][0], 'head'))
        for i, (ls, le, _c, lab) in enumerate(eff):
            t0 = ls
            t1 = eff[i+1][0] if i+1 < len(eff) else we
            s0, s1, wend = spans[i]
            if i == len(eff)-1:
                cap = 0.85 if (we - le) > 0.3 else 0.15
                s1 = min(tdur, wend + cap)
                if sid in LAST_CAP:
                    s1 = min(s1, LAST_CAP[sid])
            words_end = min(wend + 0.30, s1)
            if s1 - words_end > 0.5 and t1 - (le + 0.25) > 0.2:
                chunks.append((s0, words_end, t0, le + 0.25, lab))
                chunks.append((words_end, s1, le + 0.25, t1, lab + '-gap'))
            else:
                chunks.append((s0, s1, t0, t1, lab))
        if sid in HEAD_TRIM and chunks:
            a, b, c, d, l = chunks[0]
            chunks[0] = (HEAD_TRIM[sid], b, c, d, l)
        out = []
        for (a, b, c, d, l) in chunks:
            if '-gap' not in l and l != 'head' and (b - a) / (d - c) < 0.45:
                wt = (b - a) / 0.62
                out.append((a, b, c, c + wt, l))
                out.append((tdur - 1.5, tdur, c + wt, d, l + '-hold'))
                print(f'{sid} {l}: HOLD-FILL applied (words -> {wt:.2f}s @0.62, hold fills rest)')
            else:
                out.append((a, b, c, d, l))
        chunks = out
    nframes = round((we - ws) * FPS)
    total_frames += nframes
    fc = []
    for i, (s0, s1, t0, t1, lab) in enumerate(chunks):
        src_d = s1 - s0; tgt_d = t1 - t0
        assert src_d > 0.05 and tgt_d > 0.05, f'{sid} {lab}: degenerate {src_d}/{tgt_d}'
        f = src_d / tgt_d
        log.append({'scene': sid, 'chunk': lab, 'src': [round(s0,2), round(s1,2)],
                    'tgt': [round(t0,2), round(t1,2)], 'factor': round(f,3),
                    'flag': bool(f > 2.2 or f < 0.5)})
        print(f'{sid} {lab}: src {s0:.2f}-{s1:.2f} -> tgt {t0:.2f}-{t1:.2f} factor {f:.2f}' +
              (' <<<' if (f > 2.2 or f < 0.5) else ''))
        fc.append(f'[0:v]trim=start={s0:.3f}:end={s1:.3f},setpts={tgt_d/src_d:.6f}*(PTS-STARTPTS),'
                  f'scale=1280:720,fps=24,setsar=1,format=yuv420p[v{i}]')
    filt = ';'.join(fc) + ';' + ''.join(f'[v{i}]' for i in range(len(chunks))) + \
           f'concat=n={len(chunks)}:v=1:a=0,trim=end_frame={nframes},setpts=N/(24*TB)[out]'
    out = f'{ROOT}/work/segments/{sid}.mp4'
    r = subprocess.run(['ffmpeg','-v','error','-i',tpath,'-filter_complex',filt,'-map','[out]',
           '-c:v','libx264','-crf','12','-preset','medium','-an', out, '-y'],
           capture_output=True, text=True)
    if r.returncode != 0:
        print('FFMPEG FAIL', sid, r.stderr[-800:]); sys.exit(1)
    nf = int(subprocess.check_output(['ffprobe','-v','error','-count_frames','-show_entries',
        'stream=nb_read_frames','-of','csv=p=0', out]).decode().strip())
    if nf < nframes:
        pad = nframes - nf
        tmp = out + '.pad.mp4'
        subprocess.run(['ffmpeg','-v','error','-i',out,'-vf',
            f'tpad=stop_mode=clone:stop_duration={pad/FPS:.3f},trim=end_frame={nframes},setpts=N/(24*TB)',
            '-c:v','libx264','-crf','12','-preset','medium','-an', tmp, '-y'], check=True)
        os.replace(tmp, out)
        log.append({'scene': sid, 'tpad_frames': pad})
        print(f'{sid}: TPAD {pad}f'); nf = nframes
    print(f'{sid}: {nf}f (target {nframes}) take={take} leftover_words={leftover}')
print('TOTAL FRAMES', total_frames)
json.dump(log, open(f'{ROOT}/work/segments/conform_log.json','w'), indent=1)
