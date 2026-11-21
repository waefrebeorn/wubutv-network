#!/usr/bin/env python3
"""MV-16 conform v2: per-scene chunk warps from performed grid + take ASR.
All mappings grounded in the real grid dump (97 lines) + disk ASR JSONs.
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
 'S21':'s21_t2','S22':'s22_t2','S23':'s23_t2','S24':'s24_t1','S25':'s25_t1',
 'S26':'s26_t1','S27':'s27_t2','S28':'s28_t2'}
# scenes whose take delivers lines in rotated order: content groups by word
# index [0:3]=WFY [3:7]=still [7:10]=WFY, assigned to song lines [0,2,1]
REORDER = {'S03','S20','S26'}
COUNT_OVERRIDES = {'S10': [2,6,3,3]}          # (oh-oh-oh) = 2 take words
# merges: scene -> list of (grid line indexes grouped, take word count);
# grouped target starts at the first line's start
MERGES = {
 'S15': [(0,6),(1,3),(2,8),(3,2)],           # L51 '(what)' omitted by take -> merged into L52 span, count = L52's 8
 'S16': [(0,3),(1,6)],                        # L54 '(uh)' omitted -> merged into L55, count = L55's 3; then L56 count 6
 'S28': [(0,3),(1,3),(2,3),(3,3)],            # L94 '(oh)' omitted -> merged into L95 (4 eff. lines from 5)
}
MERGE_LINES = {'S15': [0,1,(2,3),4], 'S16': [(0,1),2], 'S28': [0,(1,2),3,4]}
# S11 fully custom: (src0, src1, grid line idx) in song order
S11_CHUNKS = [(1.10,2.64,0),(4.62,7.44,1),(0.00,2.64,2),(2.64,4.62,3)]

grid = json.load(open(f'{ROOT}/work/analysis/grid_lines.json'))
smap = json.load(open(f'{ROOT}/work/analysis/scene_map.json'))['scenes']
ONLY = os.environ.get('MV16_ONLY')
if ONLY:
    keep = set(ONLY.split(','))
    smap = [s for s in smap if s['sc'] in keep]
FORCE_SPLIT = {'S14': ('L47', 4.72, 89.79)}   # scene -> (label, src split, tgt split)
LAST_CAP = {'S14': 8.70}                       # cap last chunk source end (ASR over-long shout word)
HEAD_TRIM = {'S04': 0.30}                      # scene -> first chunk source start (skip closed-mouth head pose so the hook onset lands on an open mouth)

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
    assert lines, f'{sid}: no grid lines'
    if sid == 'S04':
        lines = lines[:3]
    # effective lines: (start, end, count, label)
    if sid in MERGE_LINES:
        eff = []
        for spec, cnt in zip(MERGE_LINES[sid], [c for _, c in MERGES[sid]]):
            idxs = spec if isinstance(spec, tuple) else (spec,)
            eff.append((lines[idxs[0]]['start'], lines[idxs[-1]]['end'], cnt,
                        '/'.join(f'L{lines[i]["n"]}' for i in idxs)))
        counts = [e[2] for e in eff]
    else:
        eff = [(L['start'], L['end'], wc(L['text']), f'L{L["n"]}') for L in lines]
        if sid in COUNT_OVERRIDES:
            eff = [(s, e, c, lab) for (s, e, _o, lab), c in zip(eff, COUNT_OVERRIDES[sid])]
        counts = [e[2] for e in eff]
    # group take words
    groups = []; idx = 0
    if sid in REORDER:
        for a, b in [(0,3),(3,7),(7,10)]:
            groups.append(words[a:b])
        idx = 10
    elif sid == 'S11':
        groups = None
    else:
        for c in counts:
            g = words[idx:idx+c]; assert len(g) == c, f'{sid}: word starve at {c}'
            groups.append(g); idx += c
    leftover = len(words) - idx if groups is not None else 0
    # source spans per effective line
    spans = []
    if groups is not None:
        for i, g in enumerate(groups):
            s0 = g[0]['start']
            s1 = groups[i+1][0]['start'] if i+1 < len(groups) else g[-1]['end']
            spans.append([s0, s1, g[-1]['end']])
        if sid in REORDER:
            spans = [spans[0], spans[2], spans[1]]
    # chunks: (src0, src1, tgt0, tgt1, label)
    chunks = []
    if sid == 'S11':
        for (s0, s1, li) in S11_CHUNKS:
            t0 = lines[li]['start']
            t1 = lines[li+1]['start'] if li+1 < len(lines) else we
            chunks.append((s0, s1, t0, t1, f'L{lines[li]["n"]}'))
    else:
        first_src = spans[0][0]
        pocket = eff[0][0] - ws
        if pocket > 0.02:
            if first_src > pocket + 0.05:
                hs = first_src - pocket
            else:
                hs = {'S03': 8.40}.get(sid, min(tdur - pocket, words[idx-1]['end'] + 0.30))
            chunks.append((hs, hs + pocket, ws, eff[0][0], 'head'))
        for i, (ls, le, _c, lab) in enumerate(eff):
            t0 = ls
            t1 = eff[i+1][0] if i+1 < len(eff) else we
            if sid == 'S04' and i == len(eff)-1:
                t1 = 24.88
            s0, s1, wend = spans[i]
            if i == len(eff)-1 and sid != 'S04':
                cap = 0.85 if (we - le) > 0.3 else 0.15
                s1 = min(tdur, wend + cap)
                if sid in LAST_CAP:
                    s1 = min(s1, LAST_CAP[sid])
            # words/gap sub-chunk split: compress the take's dead air harder
            words_end = min(wend + 0.30, s1)
            if s1 - words_end > 0.5 and t1 - (le + 0.25) > 0.2:
                chunks.append((s0, words_end, t0, le + 0.25, lab))
                chunks.append((words_end, s1, le + 0.25, t1, lab + '-gap'))
            else:
                chunks.append((s0, s1, t0, t1, lab))
        if sid == 'S04':
            chunks.append((6.80, 9.30, 24.88, we, 'HEY-shout'))
    # post-process: head trim + S13 tail source + forced split (S14 L47) + hold-fill for sub-0.45 word chunks
    if sid == 'S13':
        out = []
        for (a, b, c, d, l) in chunks:
            if l == 'L45-gap':
                out.append((8.65, 10.04, c, d, l))  # post-chant sway at 0.79x, not the 0.31x crawl
                print('S13 L45-gap: tail source replaced with take post-chant sway [8.65-10.04]')
            else:
                out.append((a, b, c, d, l))
        chunks = out
    if sid in HEAD_TRIM and chunks:
        a, b, c, d, l = chunks[0]
        chunks[0] = (HEAD_TRIM[sid], b, c, d, l)
    if sid in FORCE_SPLIT:
        lab, ssp, tsp = FORCE_SPLIT[sid]
        out = []
        for (a, b, c, d, l) in chunks:
            if l == lab:
                out.append((a, ssp, c, tsp, l)); out.append((ssp, b, tsp, d, l + '-gap'))
            else:
                out.append((a, b, c, d, l))
        chunks = out
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
