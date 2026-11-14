#!/usr/bin/env python3
"""MV-16 REBUILD ASS builder: kinetic per-word highlight + SLAM lines +
S13 word chase (wall) + S26 worn graphics (tee) + SCREEN PiP states +
~ WuBu ~ bug. Adapted from build_ass.py: all timings re-derived from
the NEW grid (grid_lines.json) + NEW scene_map.json. SLAM = every
'Wrong for years' line (the new FC has no NSM doubles to slam).
Text/timing authority: performed grid (grid_lines.json + SONG_WORDS.json)."""
import json

ROOT = '/home/hatch/workspace/wubutv-network/musicvideo/MV-16_wrong-for-years'
grid = json.load(open(f'{ROOT}/work/analysis/grid_lines.json'))
words = json.load(open(f'{ROOT}/work/analysis/SONG_WORDS.json'))['words']
smap = {s['sc']: s for s in json.load(open(f'{ROOT}/work/analysis/scene_map.json'))['scenes']}
TOTAL = json.load(open(f'{ROOT}/work/analysis/scene_map.json'))['total']

def ts(t):
    h = int(t // 3600); m = int((t % 3600) // 60); s = t % 60
    return f'{h}:{m:02d}:{s:05.2f}'

def clean(w):
    return w.strip('.,!?()').replace('{', '').replace('}', '')

def lines_in(sid):
    s = smap[sid]
    return [L['n'] for L in grid if s['start'] - 0.01 <= L['start'] < s['end'] - 0.01]

CHASE = {L['n'] for L in grid if L['section'] == 'POST'}       # S13 wall
TEE = set(lines_in('S26'))                                     # worn graphics
SLAM_LINES = {L['n'] for L in grid if L['text'] == 'Wrong for years'}

HEADER = """[Script Info]
Title: MV-16 Wrong for Years — kinetic layer (REBUILD, correct take)
ScriptType: v4.00+
PlayResX: 1280
PlayResY: 720
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Line,Arial,44,&H00FFFFFF,&H0000FFFF,&H00141414,&H64000000,-1,0,0,0,100,100,0,0,1,3,1,2,40,40,26,1
Style: Slam,Arial,58,&H00FFFFFF,&H0000FFFF,&H00141414,&H64000000,-1,0,0,0,100,100,0,0,1,4,2,2,40,40,30,1
Style: Chase,Arial,40,&H0000E6FF,&H0000E6FF,&H00141414,&H00000000,-1,0,0,0,100,100,0,0,1,2,0,7,0,0,0,1
Style: Tee,Arial,30,&H002E1A1A,&H002E1A1A,&H00FFFFFF,&H00000000,-1,0,0,0,100,100,0,0,1,1,0,5,0,0,0,1
Style: Bug,Arial,22,&H66FFFFFF,&H66FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,0,0,9,20,16,12,1
Style: Draw,Arial,20,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,0,0,7,0,0,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
ev = []
ACC = r'{\c&H00FFFF&\b1}'
RST = r'{\c&HFFFFFF&\b1}'

for li, L in enumerate(grid):
    n = L['n']
    nxt = grid[li + 1]['start'] if li + 1 < len(grid) else L['end'] + 0.3
    lw = [w for w in words if L['start'] - 0.05 <= w['start'] < nxt - 0.02]
    # DISPLAY text ALWAYS from the grid line, never raw ASR (see
    # build_ass.py note). ASR supplies timing only, mapped proportionally.
    disp = [clean(t) for t in L['text'].replace('—', ' ').split()]
    if lw:
        A, G = len(lw), len(disp)
        bounds = [lw[min(A - 1, (j * A) // G)]['start'] for j in range(G)] + [L['end']]
    else:
        step = (L['end'] - L['start']) / max(1, len(disp))
        bounds = [L['start'] + j * step for j in range(len(disp))] + [L['end']]
    style = 'Slam' if n in SLAM_LINES else 'Line'
    for i in range(len(disp)):
        s = bounds[i]; e = bounds[i + 1]
        if n in CHASE:      # S13 word chase on the blank wall
            txt = ' '.join(disp[:i + 1])
            ev.append((s, e, 'Chase', r'{\pos(70,110)}' + txt))
        elif n in TEE:      # S26 worn graphics on the blank tee
            tacc = r'{\c&H0000FF&\b1}'
            parts = [tacc + d + r'{\c&H2E1A1A&\b1}' if j == i else d for j, d in enumerate(disp)]
            ev.append((s, e, 'Tee', r'{\pos(650,520)}' + ' '.join(parts)))
        else:
            parts = [ACC + d + RST if j == i else d for j, d in enumerate(disp)]
            ev.append((s, e, style, ' '.join(parts)))

# ---- SCREEN PiP (lower-right box x1000-1250, y440-600) ----
def rect(x0, y0, x1, y1, colour, alpha=''):
    return (r'{\p1\c&H' + colour + '&' + alpha + r'\pos(0,0)}' +
            f'm {x0} {y0} l {x1} {y0} l {x1} {y1} l {x0} {y1}')
def box_events(s, e, border='B0B0B0', fill='141414', alpha=''):
    out = [(s, e, 'Draw', rect(1000, 440, 1250, 600, fill, alpha))]
    for (x0, y0, x1, y1) in [(996,436,1254,441),(996,599,1254,604),(996,436,1001,604),(1249,436,1254,604)]:
        out.append((s, e, 'Draw', rect(x0, y0, x1, y1, border, alpha)))
    return out

S07, S09, S13, S14, S22, S24, S28 = (smap[k] for k in
    ('S07','S09','S13','S14','S22','S24','S28'))
s07_lines_end = max(L['end'] for L in grid
                    if S07['start'] - 0.01 <= L['start'] < S07['end'] - 0.01)
# install (S07): fade in via 3 alpha steps
t0 = S07['start']
for i, (s, a) in enumerate([(t0, r'\alpha&HB0&'), (t0 + 0.76, r'\alpha&H70&'), (t0 + 1.52, '')]):
    e = s07_lines_end if i == 2 else [t0 + 0.76, t0 + 1.52][i]
    ev += box_events(s, e, alpha=a)
# S07 tail + PC1: steady box, occasional glitch bars
ev += box_events(s07_lines_end, smap['S08']['end'])
for s in [s07_lines_end + 1.6, s07_lines_end + 3.1, s07_lines_end + 4.7]:
    ev.append((s, s + 0.18, 'Draw', rect(1010, 480, 1240, 492, 'B0B0B0')))
# C2 glitch: alternating bar sets every 0.8s
t = S09['start']; k = 0
while t < S13['start']:
    e = min(t + 0.8, S13['start'])
    ev += box_events(t, e)
    y = 470 + (k % 3) * 40
    ev.append((t, e, 'Draw', rect(1010, y, 1240, y + 10, '8A8A8A')))
    t = e; k += 1
# POST pulse on the beat (0.4s steps)
t = S13['start']
while t < S14['start']:
    e = min(t + 0.4, S14['start'])
    ev += box_events(t, e, border='00E6FF')
    t = e
# V2..C3: dark box; BR: darker/off
ev += box_events(S14['start'], S22['start'], fill='0A0A0A')
ev += box_events(S22['start'], S24['start'], border='5A5A5A', fill='050505')
# FC gold equalizer: 5 bars, heights cycle per beat
pats = [[30, 70, 110, 60, 90], [80, 120, 50, 100, 40], [110, 60, 90, 130, 70], [60, 100, 130, 45, 105]]
t = S24['start']; k = 0
while t < S28['start']:
    e = min(t + 0.4, S28['start'])
    ev += box_events(t, e, border='00C8FF', fill='101010')
    for j, h in enumerate(pats[k % 4]):
        x = 1020 + j * 45
        ev.append((t, e, 'Draw', rect(x, 590 - h, x + 28, 590, '00C8FF')))
    t = e; k += 1
# OUT: fade out
o = S28['start']
for i, (s, a) in enumerate([(o, ''), (o + 2.77, r'\alpha&H70&'), (o + 5.77, r'\alpha&HB0&')]):
    e = [o + 2.77, o + 5.77, S28['end']][i]
    ev += box_events(s, e, alpha=a)
# bug
ev.append((0.0, TOTAL, 'Bug', r'{\pos(1252,700)}~ WuBu ~'))

ev.sort(key=lambda x: x[0])
lines = [HEADER]
for (s, e, st, txt) in ev:
    if e - s < 0.04:
        continue
    lines.append(f'Dialogue: 0,{ts(s)},{ts(e)},{st},,0,0,0,,{txt}')
open(f'{ROOT}/work/mv16_kinetic.ass', 'w').write('\n'.join(lines) + '\n')
print('events:', len(lines) - 1, '| slam lines:', sorted(SLAM_LINES),
      '| chase:', sorted(CHASE), '| tee:', sorted(TEE))
