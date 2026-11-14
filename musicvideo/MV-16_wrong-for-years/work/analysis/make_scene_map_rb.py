#!/usr/bin/env python3
"""MV-16 REBUILD scene map (correct take, 198.016s).
Same derivation as the first build's scene_map: scene windows tile the
song; a boundary sits at the midpoint of the gap between the previous
scene's last grid line end and the next scene's first grid line start.
EXCEPTION (mirrors the first build's POST->V2 pocket assignment): the
93.88-95.36 breath pocket before V2 goes to S13's tail, so S14 starts
exactly at L40's onset (95.36) — s14_t2's head IS the Mic onset and
cannot fill a head pocket.
Scene->line assignment is by performed content (see MV16_PROGRESS
REBUILD section): identical line texts to the first build except S22
(BR is now WFYx3+NSMx2) and S28 (OUT is now NSM/NSM/WFY/(yeah))."""
import json, pathlib
A = pathlib.Path(__file__).parent
grid = json.load(open(A / 'grid_lines.json'))
by_n = {L['n']: L for L in grid}
ASSIGN = {  # scene -> (first line n, last line n, section)
 'S01': (1, 3, 'C1'), 'S02': (4, 6, 'C1'), 'S03': (7, 9, 'C1'),
 'S04': (10, 12, 'C1'), 'S05': (13, 15, 'V1'), 'S06': (16, 17, 'V1'),
 'S07': (18, 21, 'V1'), 'S08': (22, 25, 'PC1'), 'S09': (26, 28, 'C2'),
 'S10': (29, 31, 'C2'), 'S11': (32, 34, 'C2'), 'S12': (35, 37, 'C2'),
 'S13': (38, 39, 'POST'), 'S14': (40, 42, 'V2'), 'S15': (43, 46, 'V2'),
 'S16': (47, 48, 'V2'), 'S17': (49, 52, 'PC2'), 'S18': (53, 55, 'C3'),
 'S19': (56, 58, 'C3'), 'S20': (59, 61, 'C3'), 'S21': (62, 64, 'C3'),
 'S22': (65, 69, 'BR'), 'S23': (70, 70, 'BR'), 'S24': (71, 73, 'FC'),
 'S25': (74, 76, 'FC'), 'S26': (77, 79, 'FC'), 'S27': (80, 82, 'FC'),
 'S28': (83, 86, 'OUT')}
TOTAL = 198.10   # per-scene frame rounding loses ~2f; outro tail absorbs it
                 # (segments sum to 4752f = 198.000s vs track 198.016s)
scenes = []
prev_end = None
for i in range(1, 29):
    sid = f'S{i:02d}'
    a, b, sec = ASSIGN[sid]
    first, last = by_n[a], by_n[b]
    if i == 1:
        start = 0.0
    elif sid == 'S14':
        start = first['start']            # pocket exception (see header)
    else:
        start = round((prev_end + first['start']) / 2, 2)
    scenes.append({'sc': sid, 'section': sec, 'start': start,
                   'lines': [a, b]})
    prev_end = last['end']
for i, s in enumerate(scenes):
    s['end'] = scenes[i + 1]['start'] if i + 1 < len(scenes) else TOTAL
    s['first_line_start'] = by_n[s['lines'][0]]['start']
    s['last_line_end'] = by_n[s['lines'][1]]['end']
out = {'fps': 24, 'total': TOTAL, 'scenes': [
    {'sc': s['sc'], 'section': s['section'], 'start': s['start'],
     'end': s['end']} for s in scenes]}
json.dump(out, open(A / 'scene_map.json', 'w'), indent=1)
tot = 0
for s in scenes:
    nf = round((s['end'] - s['start']) * 24)
    tot += nf
    print(f"{s['sc']} {s['section']:4s} {s['start']:7.2f}-{s['end']:7.2f} "
          f"lines {s['lines'][0]}-{s['lines'][1]} ({nf}f)")
print('TOTAL frames', tot, '=', tot / 24, 's')
