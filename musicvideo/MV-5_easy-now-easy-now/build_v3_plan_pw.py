#!/usr/bin/env python3
"""MV-5 v3 BUILD 3 plan — per-word swing-keyframe warping (user law 2026-11-06).

Starts from the build-2 plan (work/assembly_fit_mv5_v3.json) and replaces
uniform warps inside sung take-groups with piecewise per-word warps built
from measured word anchors. Anchor sources per scene (documented in
work/V3_ASSEMBLY_NOTES.md section 5):
  - pairs (work/gemini_takes.json, Gemini-app per-word, audit-adjudicated)
  - tool  (work/swing/*_swing.json, fresh dual-Whisper swing keyframes)
Caps: playback >= 0.5x per interval (setpts <= 2.0). Speedups free.
Knife-edge: an interval needing setpts >2.0 whose time deficit
(song_iv - 2*take_iv) is <= 0.11s is capped AT 2.0 and the deficit is
absorbed by the following interval (disclosed). Head/tail adjudication:
drop leading/trailing anchors whose edge interval is illegally slow
beyond knife-edge (word warps by neighbours); extend a take tail into
the take's unused frames where that legalizes a tail interval.
Groups that still cannot land legally keep their build-2 warps and are
flagged STRUCTURAL in the table.
"""
import json, subprocess, sys

P = '/home/hatch/workspace/wubutv-network/musicvideo/MV-5_easy-now-easy-now/'
plan = json.load(open(P + 'work/assembly_fit_mv5_v3.json'))
pairs = json.load(open(P + 'work/gemini_takes.json'))['scenes']
FPS = 24
KNIFE = 0.11  # seconds of deficit tolerated at the 2.0 cap

def take_dur(take):
    out = subprocess.run(['ffprobe', '-v', 'error', '-show_entries',
                          'format=duration', '-of', 'csv=p=0',
                          P + 'takes/' + take + '.mp4'],
                         capture_output=True, text=True).stdout.strip()
    return float(out)

DUR = {}
def dur(take):
    if take not in DUR: DUR[take] = take_dur(take)
    return DUR[take]

# ---------- anchor tables: (scene, take) -> [(take_t, song_t, word, src)]
ANCH = {}
def add(scene, take, rows):
    ANCH.setdefault((scene, take), []).extend(rows)

for sc, e in pairs.items():
    rows = [(w['take_start'], w['song_start_v2'], w['song_word'], 'pairs')
            for w in e['words']]
    add(sc, 'mv5_' + e['take'], rows)
# S01: tool keyframes (pairs' intro stamps are the noisy set; tool validated)
tool_s01 = json.load(open(P + 'work/swing/s01_t1_swing.json'))
ANCH[('S01', 'mv5_s01_t1')] = [(w['take_start'], w['song_start'], w['song_word'], 'tool')
                               for w in tool_s01['words'] if w['take_start'] is not None]
# S06 L12 on s06_t2: song stamps from pairs (t1 rows), take stamps from tool decode
l12_song = {w['song_word'].lower(): w['song_start_v2'] for w in pairs['S06']['words'] if w['line'] == 'L12'}
ANCH[('S06', 'mv5_s06_t2')] = [(0.0, l12_song['yeah'], 'Yeah', 'tool+pairs'),
                               (0.76, l12_song['they'], 'they', 'tool+pairs'),
                               (0.98, l12_song['already'], 'already', 'tool+pairs'),
                               (1.44, l12_song['understand'], 'understand', 'tool+pairs')]
# S07 L15 on s07_t2: tool keyframes (mandated table)
tool_t2 = json.load(open(P + 'work/swing/s07_t2_swing.json'))
ANCH[('S07', 'mv5_s07_t2')] = [(w['take_start'], w['song_start'], w['song_word'], 'tool')
                               for w in tool_t2['words'] if w['take_start'] is not None]
# S15 supplement: 'replays' (pairs dropped it; tool stamped the take time)
ANCH[('S15', 'mv5_s15_t1')].append((2.44, 116.32, 'replays', 'tool+pairs'))
# manual anchor drops (grid outliers, documented): S07 L16 'replays' pairs stamp
DROP = {('S07', 'mv5_s07_t1', 'replays')}
for k in list(ANCH):
    ANCH[k] = [r for r in ANCH[k] if (k[0], k[1], r[2].lower()) not in DROP]
    ANCH[k].sort()

SUNG = ('line', 'refrain', 'span', 'arrival', 'cover-L38', 'L39-grey',
        'L40-tail', 'tail-L106', 'no-need-to')
SKIP_SCENES = {'S03', 'S27'}   # vocalise / grid-contested — documented, keep v2
# groups whose only anchors are cross-complex misalignments (v1 refrain
# pairs) — per-word warping on them would damage the picture; keep v2.
SKIP_GROUPS = {('S17', 'mv5_s17_t1', 41)}

table = []          # human-readable per-group record
new_plan = {}
report = {'reworked': [], 'kept': [], 'caps': [], 'drops': [], 'flags': []}

for sc in plan['scenes']:
    pcs = plan['plan'][sc]
    if sc in SKIP_SCENES:
        new_plan[sc] = pcs
        report['kept'].append(f'{sc}: scene skipped (documented)')
        continue
    # group consecutive same-take pieces; freeze-leader is its own group
    groups = []
    for p in pcs:
        if (groups and groups[-1][0] == p['take'] and p['kind'] != 'freeze-leader'
                and groups[-1][1][0]['kind'] != 'freeze-leader'):
            groups[-1][1].append(p)
        else:
            groups.append([p['take'], [p]])
    out_pieces = []
    for take, gps in groups:
        gout = sum(g['out'] for g in gps)
        sung = any(g['kind'].startswith(SUNG) for g in gps)
        table_key = f'{sc}/{take}[{gps[0]["sf"]}-{gps[-1]["ef"]}]'
        if (sc, take, gps[0]['sf']) in SKIP_GROUPS:
            out_pieces.extend(gps)
            report['kept'].append(f'{table_key}: anchor misalignment (documented) — build-2 warps kept')
            continue
        if not sung or (sc, take) not in ANCH:
            out_pieces.extend(gps)
            if sung: report['kept'].append(f'{table_key}: no anchor table')
            continue
        sf, ef = gps[0]['sf'], gps[-1]['ef']
        d0, d1 = gps[0]['dst0'], gps[-1]['dst1']
        anch = [a for a in ANCH[(sc, take)]
                if sf / FPS < a[0] < ef / FPS and d0 < a[1] < d1]
        if not anch:
            out_pieces.extend(gps)
            report['kept'].append(f'{table_key}: no anchors inside span')
            continue
        pts = [(sf / FPS, d0, 'START', '')] + \
              [(a[0], a[1], a[2], a[3]) for a in anch] + \
              [(ef / FPS, d1, 'END', '')]
        # sanitize: strictly increasing take & song times (0.04s epsilon).
        # START/END are structural and never dropped — a conflicting
        # interior anchor is dropped instead (its word rides the interval).
        clean = [pts[0]]
        for p in pts[1:-1]:
            if p[0] - clean[-1][0] <= 0.04 or p[1] - clean[-1][1] <= 0.04:
                report['drops'].append(f'{table_key}: dropped anchor {p[2]} (zero/duplicate stamp)')
                continue
            clean.append(p)
        end = pts[-1]
        while len(clean) > 1 and (end[0] - clean[-1][0] <= 0.04 or end[1] - clean[-1][1] <= 0.04):
            report['drops'].append(f'{table_key}: dropped anchor {clean[-1][2]} (conflicts with span END)')
            clean.pop()
        clean.append(end)
        pts = clean
        # adjudicate edge intervals
        def ivs(pts):
            return [(pts[i + 1][0] - pts[i][0], pts[i + 1][1] - pts[i][1]) for i in range(len(pts) - 1)]
        ok = True
        guard = 0
        while ok and guard < 12:
            guard += 1
            iv = ivs(pts)
            pb = [t / s for t, s in iv]
            # middle intervals: cap if knife-edge, else fail the group
            bad_mid = [i for i in range(1, len(pb) - 1) if pb[i] < 0.5 and iv[i][1] - 2 * iv[i][0] > KNIFE]
            if bad_mid:
                ok = False; break
            # head
            if pb[0] < 0.5 and iv[0][1] - 2 * iv[0][0] > KNIFE:
                if len(pts) > 3:
                    report['drops'].append(f'{table_key}: dropped leading anchor {pts[1][2]} (illegal head interval)')
                    pts = [pts[0]] + pts[2:]; continue
                ok = False; break
            # tail
            if pb[-1] < 0.5 and iv[-1][1] - 2 * iv[-1][0] > KNIFE:
                # try tail extension into unused take frames
                need_take = iv[-1][1] / 2 * 1.02
                ext = (pts[-2][0] + need_take) - pts[-1][0]
                maxef = dur(take)
                if 0 < ext <= 1.0 and pts[-1][0] + ext <= maxef:
                    pts[-1] = (pts[-1][0] + ext, pts[-1][1], 'END+', '')
                    report['flags'].append(f'{table_key}: tail extended +{ext:.2f}s into take tail')
                    continue
                if len(pts) > 3:
                    report['drops'].append(f'{table_key}: dropped trailing anchor {pts[-2][2]} (illegal tail interval)')
                    pts = pts[:-2] + [pts[-1]]; continue
                ok = False; break
            break
        if not ok:
            out_pieces.extend(gps)
            report['kept'].append(f'{table_key}: STRUCTURAL — intervals cannot land legally; build-2 warps kept')
            report['flags'].append(f'{table_key}: STRUCTURAL (kept v2)')
            table.append(f'{table_key} KEPT-V2 (structural)')
            continue
        # emit sub-pieces with cumulative frame accounting
        iv = ivs(pts)
        capped = {}
        for i, (t, s) in enumerate(iv):
            if t / s < 0.5:
                capped[i] = s - 2 * t
                report['caps'].append(f'{table_key}: interval {pts[i][2]}->{pts[i+1][2]} capped at setpts 2.0 (deficit {s-2*t:.3f}s)')
        subs = []
        cum = 0
        rows = []
        for i, (t, s) in enumerate(iv):
            tf0 = round(pts[i][0] * FPS); tf1 = round(pts[i + 1][0] * FPS)
            if i in capped:
                o = 2 * (tf1 - tf0)
            elif i == len(iv) - 1:
                o = gout - cum
            else:
                o = round((pts[i + 1][1] - d0) * FPS) - cum
            if o <= 0:
                report['drops'].append(f'{table_key}: zero-frame interval at {pts[i][2]} merged')
                if subs:
                    subs[-1]['ef'] = tf1; subs[-1]['out'] += 0
                continue
            w = o / (tf1 - tf0)
            kbase = next((g['kind'].split('-')[0] for g in gps
                          if g['kind'].startswith(SUNG)), gps[0]['kind'].split('-')[0])
            subs.append({'kind': kbase + '-pw', 'take': take,
                         'sf': tf0, 'ef': tf1, 'warp': round(w, 4), 'out': o,
                         'dst0': round(d0 + cum / FPS, 3), 'dst1': round(d0 + (cum + o) / FPS, 3)})
            rows.append(f"    {pts[i][2]:>10s} take {pts[i][0]:5.2f}->{pts[i+1][0]:5.2f}  song {pts[i][1]:7.3f}->{pts[i+1][1]:7.3f}  playback {t/s:5.2f}x  setpts {w:5.3f}  out {o}f" + ('  CAPPED' if i in capped else ''))
            cum += o
        assert cum == gout, f'{table_key}: frame total {cum} != {gout}'
        out_pieces.extend(subs)
        report['reworked'].append(table_key)
        table.append(f'{table_key} REWORKED ({len(anch)} anchors, out {gout}f)\n' + '\n'.join(rows))
    new_plan[sc] = out_pieces

total = sum(p['out'] for sc in new_plan for p in new_plan[sc])
assert total == 4954, total
json.dump({'plan': new_plan, 'total_frames': total, 'bounds': plan['bounds'],
           'scenes': plan['scenes']}, open(P + 'work/assembly_fit_mv5_v3pw.json', 'w'), indent=1)
open(P + 'work/swing/PW_TABLE.md', 'w').write(
    '# BUILD 3 per-word swing table\n\n' + '\n'.join(table) +
    '\n\n## report\n' + json.dumps(report, indent=1))
print(json.dumps({k: (len(v) if isinstance(v, list) else v) for k, v in report.items()}, indent=1))
print('total frames', total)
for line in report['kept'] + report['flags']:
    print(' ', line)
