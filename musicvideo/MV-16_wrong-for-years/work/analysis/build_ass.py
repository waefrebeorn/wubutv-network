#!/usr/bin/env python3
"""MV-16 ASS builder: kinetic per-word highlight + SLAM lines + S13 word
chase (wall) + S26 worn graphics (tee) + SCREEN PiP states + ~ WuBu ~ bug.
Text/timing authority: performed grid (grid_lines.json + SONG_WORDS.json)."""
import json, re

ROOT = '/home/hatch/workspace/wubutv-network/musicvideo/MV-16_wrong-for-years'
grid = json.load(open(f'{ROOT}/work/analysis/grid_lines.json'))
words = json.load(open(f'{ROOT}/work/analysis/SONG_WORDS.json'))['words']

def ts(t):
    h = int(t // 3600); m = int((t % 3600) // 60); s = t % 60
    return f'{h}:{m:02d}:{s:05.2f}'

def clean(w):
    return w.strip('.,!?()').replace('{', '').replace('}', '')

HEADER = """[Script Info]
Title: MV-16 Wrong for Years — kinetic layer
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
SLAM_LINES = set()
for L in grid:
    if L['text'] == 'Wrong for years':
        SLAM_LINES.add(L['n'])
SLAM_LINES |= {81, 82, 85, 86}   # FC "Nobody stopped me" doubles

for li, L in enumerate(grid):
    n = L['n']
    nxt = grid[li + 1]['start'] if li + 1 < len(grid) else L['end'] + 0.3
    lw = [w for w in words if L['start'] - 0.05 <= w['start'] < nxt - 0.02]
    # DISPLAY text ALWAYS comes from the corrected grid line, never raw
    # ASR tokens (song ASR slips — "for"->"three", "switching sides"->
    # "swooning itch inside", "wrote"->"rode" — must not reach the screen).
    # ASR words supply timing only, mapped proportionally onto grid tokens.
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
        if n in (42, 43, 44, 45):      # S13 word chase on the blank wall
            txt = ' '.join(disp[:i + 1])
            ev.append((s, e, 'Chase', r'{\pos(70,110)}' + txt))
        elif 87 <= n <= 89:            # S26 worn graphics on the blank tee
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
def box(border='B0B0B0', fill='141414'):
    return rect(1000, 440, 1250, 600, fill) + r'{\p0} ' + rect(996, 436, 1254, 604, border, r'\alpha&HFF&')
# simpler: layered events — fill rect + 4 border rects
def box_events(s, e, border='B0B0B0', fill='141414', alpha=''):
    out = [(s, e, 'Draw', rect(1000, 440, 1250, 600, fill, alpha))]
    for (x0, y0, x1, y1) in [(996,436,1254,441),(996,599,1254,604),(996,436,1001,604),(1249,436,1254,604)]:
        out.append((s, e, 'Draw', rect(x0, y0, x1, y1, border, alpha)))
    return out
# install (S07): fade in via 3 alpha steps
for i, (s, a) in enumerate([(38.54, r'\alpha&HB0&'), (39.30, r'\alpha&H70&'), (40.06, '')]):
    e = 47.92 if i == 2 else [39.30, 40.06][i]
    ev += box_events(s, e, alpha=a)
# C1 tail + V1/PC: steady box, occasional glitch bars
ev += box_events(47.92, 54.10)
for s in [49.5, 51.0, 52.6]:
    ev.append((s, s + 0.18, 'Draw', rect(1010, 480, 1240, 492, 'B0B0B0')))
# C2 glitch: alternating bar sets every 0.8s
t = 54.10
k = 0
while t < 77.90:
    e = min(t + 0.8, 77.90)
    ev += box_events(t, e)
    y = 470 + (k % 3) * 40
    ev.append((t, e, 'Draw', rect(1010, y, 1240, y + 10, '8A8A8A')))
    t = e; k += 1
# POST pulse on the beat (0.4s grid, phase 0.208)
t = 77.90
while t < 86.66:
    e = min(t + 0.4, 86.66)
    ev += box_events(t, e, border='00E6FF')
    t = e
# V2/BR: dark box
ev += box_events(86.66, 132.24, fill='0A0A0A')
ev += box_events(132.24, 145.08, border='5A5A5A', fill='050505')
# FC gold equalizer: 5 bars, heights cycle per beat
import itertools
pats = [[30, 70, 110, 60, 90], [80, 120, 50, 100, 40], [110, 60, 90, 130, 70], [60, 100, 130, 45, 105]]
t = 145.08; k = 0
while t < 172.84:
    e = min(t + 0.4, 172.84)
    ev += box_events(t, e, border='00C8FF', fill='101010')
    for j, h in enumerate(pats[k % 4]):
        x = 1020 + j * 45
        ev.append((t, e, 'Draw', rect(x, 590 - h, x + 28, 590, '00C8FF')))
    t = e; k += 1
# OUT: fade out
for i, (s, a) in enumerate([(174.10, ''), (176.50, r'\alpha&H70&'), (179.00, r'\alpha&HB0&')]):
    e = [176.50, 179.00, 182.80][i]
    ev += box_events(s, e, alpha=a)

# bug
ev.append((0.0, 183.2, 'Bug', r'{\pos(1252,700)}~ WuBu ~'))

ev.sort(key=lambda x: x[0])
lines = [HEADER]
for (s, e, st, txt) in ev:
    if e - s < 0.04:
        continue
    lines.append(f'Dialogue: 0,{ts(s)},{ts(e)},{st},,0,0,0,,{txt}')
open(f'{ROOT}/work/mv16_kinetic.ass', 'w').write('\n'.join(lines) + '\n')
print('events:', len(lines) - 1)
