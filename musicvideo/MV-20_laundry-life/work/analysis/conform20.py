#!/usr/bin/env python3
"""MV-20 conform: phrase-level smooth warp from take-ASR word times
vs song word times (grid_lines.json). Chunks tile each scene span:
head gap / lines / inter-line gaps / tail. Gap chunks use the take's
own between-material when present; when the take gap is longer than
the song gap a natural-speed sub-window is used; when absent, a
mouth-closed tail sub-window is borrowed (disclosed, MV-19 method).
Overrides: S19 line starts at the descent (1.70s) so the mouth lands
on the onset; S26 src capped at 4.66 (repeat "floor" excluded; head
borrows the sustain tail); S27 raccoon line uses performance 2;
S30 single wordless chunk. Output work/segments + conform_log.json.
Total must equal 3888 frames (162.000s x 24); S30 absorbs -1."""
import json, subprocess, os, hashlib, sys, re

ROOT = os.path.expanduser('~/workspace/wubutv-network/musicvideo/MV-20_laundry-life')
FPS = 24
ANA = f'{ROOT}/work/analysis'
grid = {L['n']: L for L in json.load(open(f'{ANA}/grid_lines.json'))}

# sid: (start, end, take, [line numbers])
SCENES = [
 ('S01', 0.00, 4.50, 's01_t1', [1]), ('S02', 4.50, 10.18, 's02_t1', [2]),
 ('S03', 10.18, 16.00, 's03_t1', [3, 4, 5]), ('S04', 16.00, 22.98, 's04_t1', [6]),
 ('S05', 22.98, 28.44, 's05_t1', [7, 8]), ('S06', 28.44, 34.16, 's06_t1', [9, 10]),
 ('S07', 34.16, 36.40, 's07_t2', [11]), ('S07B', 36.40, 38.82, 's07b_t1', [12]),
 ('S08', 38.82, 43.90, 's08_t2', [13, 14]), ('S09', 43.90, 47.88, 's09_t1', [15]),
 ('S10', 47.88, 54.90, 's10_t1', [16]), ('S11', 54.90, 60.54, 's11_t1', [17, 18, 19]),
 ('S12', 60.54, 64.80, 's12_t1', [20]), ('S13', 64.80, 66.32, 's13_t2', [21]),
 ('S13B', 66.32, 67.72, 's13b_t1', [22]), ('S14', 67.72, 74.16, 's14_t1', [23, 24]),
 ('S15', 74.16, 80.90, 's15_t1', [25, 26]), ('S16', 80.90, 86.56, 's16_t1', [27, 28]),
 ('S17', 86.56, 88.74, 's17_t1', [29]), ('S17B', 88.74, 91.18, 's17b_t1', [30]),
 ('S18', 91.18, 92.88, 's18_t1', [31]), ('S18B', 92.88, 95.72, 's18b_t1', [32]),
 ('S19', 95.72, 100.86, 's19_t1', [33]), ('S20', 100.86, 106.70, 's20_t1', [34]),
 ('S21', 106.70, 112.16, 's21_t1', [35, 36, 37]), ('S22', 112.16, 117.26, 's22_t1', [38]),
 ('S23', 117.26, 122.54, 's23_t1', [39, 40, 41]), ('S24', 122.54, 126.66, 's24_t1', [42]),
 ('S25', 126.66, 131.08, 's25_t1', [43]), ('S26', 131.08, 136.74, 's26_t1', [44]),
 ('S27', 136.74, 142.28, 's27_t1', [45, 46]), ('S28', 142.28, 150.32, 's28_t1', [47]),
 ('S29', 150.32, 155.80, 's29_t2', [48, 49]), ('S30', 155.80, 162.00, 's30_t1', []),
]
FRAMES = {}
_tot = 0
for sid, a, b, *_ in SCENES:
    FRAMES[sid] = round((b - a) * FPS); _tot += FRAMES[sid]
FRAMES['S30'] -= (_tot - 3888)
assert sum(FRAMES.values()) == 3888, sum(FRAMES.values())
ZOOM = {'S05', 'S23', 'S30'}
SRC_CAP = {'s26_t1': 4.66}

def norm(w):
    w = w.lower().strip(".,!?()'\"").replace('\u2019', "'")
    if w == 'basketball': w = 'basket'
    if w.endswith("'s"): w = w[:-2]
    if w == 'baskets': w = 'basket'
    return w

def dur(p):
    return float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries',
        'format=duration', '-of', 'csv=p=0', p]).decode().strip())

def frames(p):
    return int(subprocess.check_output(['ffprobe', '-v', 'error', '-select_streams', 'v:0',
        '-count_frames', '-show_entries', 'stream=nb_read_frames', '-of', 'csv=p=0', p]).decode().strip())

def md5(p):
    return hashlib.md5(open(p, 'rb').read()).hexdigest()

def match_lines(take, line_nums):
    """Sequential greedy word match; returns {line_n: (src0, src1)}."""
    d = json.load(open(f'{ANA}/asr_mv20_{take}.json'))
    words = [(norm(w['w']), w['start'], w['end']) for w in d['words']]
    cap = SRC_CAP.get(take)
    if cap: words = [w for w in words if w[1] < cap]
    out, cur = {}, 0
    for ln in line_nums:
        want = [norm(x) for x in grid[ln]['text'].replace('-', ' ').split()]
        hits, j = [], cur
        for pw in want:
            k = j
            while k < len(words) and k < j + 4 and words[k][0] != pw:
                k += 1
            if k < len(words) and words[k][0] == pw:
                hits.append(k); j = k + 1
        if len(hits) >= max(1, len(want) // 2):
            out[ln] = (words[hits[0]][1], words[hits[-1]][2]); cur = hits[-1] + 1
        else:
            out[ln] = None
    # fallback: proportional split of the vocal span for unmatched lines
    spans = [v for v in out.values() if v]
    if spans:
        v0, v1 = spans[0][0], spans[-1][1]
        miss = [ln for ln in line_nums if out[ln] is None]
        for i, ln in enumerate(miss):
            f0 = (line_nums.index(ln)) / len(line_nums); f1 = (line_nums.index(ln) + 1) / len(line_nums)
            out[ln] = (v0 + (v1 - v0) * f0, v0 + (v1 - v0) * f1)
            print(f'  WARN {take} L{ln} fallback span {out[ln]}')
    return out, (words[-1][2] if words else 0.0)

def build_chunks(sid, a, b, take, line_nums, tdur):
    """Returns [(take, s0, s1, t0, t1, kind)] tiling [a, b]."""
    if sid == 'S30':
        return [(take, 0.0, 6.20, a, b, 'wordless')]
    spans, last_end = match_lines(take, line_nums)
    if sid == 'S27':  # perf 2 carries the raccoon line (ledgered)
        spans[46] = (6.50, 8.44)
    if sid == 'S19':  # start at the descent so the mouth lands on the onset
        s0, s1 = spans[33]; spans[33] = (max(0.0, s0 - 0.34), s1)
    tail_avail = (last_end, tdur)
    borrow_cur = [last_end]
    def borrow(tgt_dur):
        s0 = borrow_cur[0]; avail = tdur - s0
        use = min(avail, max(tgt_dur, 0.3))
        borrow_cur[0] = s0 + use
        return (s0, s0 + use)
    chunks, tcur = [], a
    lines = [(grid[ln]['start'], grid[ln]['end'], spans[ln]) for ln in line_nums]
    for i, (ls, le, (ts0, ts1)) in enumerate(lines):
        if ls - tcur >= 0.12:  # head / inter-line gap
            gd = ls - tcur
            prev_end = lines[i - 1][2][1] if i else 0.0
            navail = ts0 - prev_end
            if navail >= gd: src = (prev_end, prev_end + gd)
            elif navail >= 0.15: src = (prev_end, ts0)
            else: src = borrow(gd)
            chunks.append((take, src[0], src[1], tcur, ls, 'gap'))
        elif ls > tcur and i == 0:  # tiny head absorbed into the line chunk
            ts0 = max(0.0, ts0 - (ls - tcur) * ((ts1 - ts0) / max(le - ls, 0.01)))
            ls = tcur
        chunks.append((take, ts0, ts1, max(ls, tcur), le, 'line'))
        tcur = le
    if b - tcur >= 0.12:  # tail
        gd = b - tcur; s0 = lines[-1][2][1]; avail = tdur - s0
        src = (s0, s0 + gd) if avail >= gd else (s0, tdur)
        chunks.append((take, src[0], src[1], tcur, b, 'tail'))
    return chunks

def scale_for(sid):
    if sid in ZOOM:
        return ("scale=1344:756:force_original_aspect_ratio=increase,"
                "crop=1280:720:x='32+min(32,n*0.5)':y='18+min(18,n*0.25)',format=yuv420p")
    return 'scale=1280:720:force_original_aspect_ratio=increase,crop=1280:720,format=yuv420p'

os.makedirs(f'{ROOT}/work/segments', exist_ok=True)
os.makedirs(f'{ROOT}/work/chunks', exist_ok=True)
log, total = [], 0
only = os.environ.get('MV20_ONLY')
for sid, a, b, take, line_nums in SCENES:
    if only and sid not in only.split(','): continue
    tp = f'{ROOT}/takes/mv20_{take}.mp4'; tdur = dur(tp)
    want = FRAMES[sid]
    chunks = build_chunks(sid, a, b, take, line_nums, tdur)
    parts, made = [], 0
    for i, (tk, s0, s1, t0, t1, kind) in enumerate(chunks):
        s1 = min(s1, tdur)
        n = want - made if i == len(chunks) - 1 else round((t1 - t0) * FPS)
        made += n
        speed = (s1 - s0) / (n / FPS)
        out = f'{ROOT}/work/chunks/{sid}_c{i}.mp4'
        vf = (f'setpts=(PTS-STARTPTS)/{speed:.5f},fps={FPS},'
              f'tpad=stop_mode=clone:stop_duration=0.25,trim=end_frame={n},setpts=PTS-STARTPTS,'
              + scale_for(sid))
        r = subprocess.run(['ffmpeg', '-y', '-v', 'error', '-ss', f'{s0}', '-i', tp,
                            '-vf', vf, '-frames:v', str(n), '-an', '-c:v', 'libx264',
                            '-preset', 'medium', '-crf', '12', out], capture_output=True, text=True)
        if r.returncode != 0:
            print(f'{sid} chunk{i} FAILED: {r.stderr[-300:]}'); sys.exit(1)
        got = frames(out); assert got == n, f'{sid} chunk{i}: {got} != {n}'
        parts.append(out)
        log.append({'scene': sid, 'chunk': i, 'kind': kind, 'take': tk, 'src': [round(s0, 2), round(s1, 2)],
                    'tgt': [round(t0, 2), round(t1, 2)], 'speed': round(speed, 3), 'frames': n, 'md5': md5(out)})
        print(f'{sid} c{i} {kind} {tk} [{s0:.2f}-{s1:.2f}] -> {n}f @ {speed:.3f}x', flush=True)
    seg = f'{ROOT}/work/segments/{sid}.mp4'
    if len(parts) == 1: os.replace(parts[0], seg)
    else:
        lst = f'{ROOT}/work/chunks/{sid}_list.txt'
        open(lst, 'w').write(''.join(f"file '{p}'\n" for p in parts))
        subprocess.run(['ffmpeg', '-y', '-v', 'error', '-f', 'concat', '-safe', '0', '-i', lst,
                        '-c', 'copy', seg], check=True)
    got = frames(seg); assert got == want, f'{sid}: segment {got} != {want}'
    total += got
    print(f'{sid} segment OK: {got} frames, md5 {md5(seg)}', flush=True)
if not only:
    print(f'TOTAL segment frames: {total}'); assert total == 3888, total
    json.dump(log, open(f'{ROOT}/work/segments/conform_log.json', 'w'), indent=1)
