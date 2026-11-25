#!/usr/bin/env python3
"""MV-17 ASS builder: kinetic per-word highlight + count tallies (S07/S19)
+ fridge-magnet OFF letters (S08) + ~ WuBu ~ bug.
Text/timing authority: performed grid (grid_lines.json + SONG_WORDS.json)."""
import json

ROOT = '/home/hatch/workspace/wubutv-network/musicvideo/MV-17_fridge-light-mystery'
grid = json.load(open(f'{ROOT}/work/analysis/grid_lines.json'))
words = json.load(open(f'{ROOT}/work/analysis/SONG_WORDS.json'))['words']

def ts(t):
    h = int(t // 3600); m = int((t % 3600) // 60); s = t % 60
    return f'{h}:{m:02d}:{s:05.2f}'

def clean(w):
    return w.strip('.,!?()').replace('{', '').replace('}', '')

HEADER = """[Script Info]
Title: MV-17 Fridge Light Mystery — kinetic layer
ScriptType: v4.00+
PlayResX: 1280
PlayResY: 720
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Line,Arial,44,&H00FFFFFF,&H0000FFFF,&H00141414,&H64000000,-1,0,0,0,100,100,0,0,1,3,1,2,40,40,26,1
Style: Slam,Arial,58,&H00FFFFFF,&H0000FFFF,&H00141414,&H64000000,-1,0,0,0,100,100,0,0,1,4,2,2,40,40,30,1
Style: Magnet,Arial,54,&H00FFFFFF,&H00FFFFFF,&H00141414,&H00000000,-1,0,0,0,100,100,0,0,1,3,0,7,0,0,0,1
Style: Bug,Arial,22,&H66FFFFFF,&H66FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,0,0,9,20,16,12,1
Style: Draw,Arial,20,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,0,0,7,0,0,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
ev = []
ACC = r'{\c&H00FFFF&\b1}'
RST = r'{\c&HFFFFFF&\b1}'
SLAM = {7, 20, 28, 32}   # first hook of C1/C2/C3 + the final hook

for li, L in enumerate(grid):
    n = L['n']
    nxt = grid[li + 1]['start'] if li + 1 < len(grid) else L['end'] + 0.3
    lw = [w for w in words if L['start'] - 0.05 <= w['start'] < nxt - 0.02]
    disp = [clean(t) for t in L['text'].replace('—', ' ').split()]
    if lw:
        A, G = len(lw), len(disp)
        bounds = [lw[min(A - 1, (j * A) // G)]['start'] for j in range(G)] + [L['end']]
    else:
        step = (L['end'] - L['start']) / max(1, len(disp))
        bounds = [L['start'] + j * step for j in range(len(disp))] + [L['end']]
    style = 'Slam' if n in SLAM else 'Line'
    # captions lead the audio by 3 frames (0.125s)
    for i in range(len(disp)):
        s = max(0.0, bounds[i] - 0.125); e = bounds[i + 1] - 0.125
        parts = [ACC + d + RST if j == i else d for j, d in enumerate(disp)]
        ev.append((s, e, style, ' '.join(parts)))

def slash(x, y=150):
    return (r'{\p1\c&HFFFFFF&\pos(0,0)}' +
            f'm {x} {y} l {x + 7} {y} l {x + 19} {y + 34} l {x + 12} {y + 34}')

def line_words(n):
    L = grid[n - 1]
    nxt = grid[n]['start'] if n < len(grid) else L['end'] + 0.3
    return L, [w for w in words if L['start'] - 0.05 <= w['start'] < nxt - 0.02]

# ---- tallies: S07 / L05 — one slash per sung "checked", persists ----
L5, w5 = line_words(5)
chk5 = [w for w in w5 if w['word'].lower().startswith('checked')]
for i, w in enumerate(chk5[:2]):
    ev.append((w['start'], 33.72, 'Draw', slash(1010 + i * 35)))
# ---- tallies: S19 / L18 — the count grows: slashes 3 and 4 ----
L18, w18 = line_words(18)
chk18 = [w for w in w18 if w['word'].lower().startswith('checked')]
for i, w in enumerate(chk18[:2]):
    ev.append((w['start'], L18['end'] + 0.3, 'Draw', slash(1010 + (i + 2) * 35)))
# ---- magnets: S08 / L06 — OFF lands on the door per sung "off" ----
L6, w6 = line_words(6)
offs = [w for w in w6 if w['word'].lower().startswith('off')]
MAG = r'{\c&H0000FF&}O{\c&H00FF00&}F{\c&HFF0000&}F'
for i, w in enumerate(offs[:2]):
    x = 860 + i * 150
    mv = '{\\move(' + str(x) + ',190,' + str(x) + ',300,0,180)}'
    ev.append((w['start'], 33.72, 'Magnet', mv + MAG))
# ---- bug ----
ev.append((0.0, 162.816, 'Bug', r'{\pos(1252,700)}~ WuBu ~'))

ev.sort(key=lambda x: x[0])
lines = [HEADER]
for (s, e, st, txt) in ev:
    if e - s < 0.04:
        continue
    lines.append(f'Dialogue: 0,{ts(s)},{ts(e)},{st},,0,0,0,,{txt}')
open(f'{ROOT}/work/mv17_kinetic.ass', 'w').write('\n'.join(lines) + '\n')
print('events:', len(lines) - 1)
