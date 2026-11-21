#!/usr/bin/env python3
"""MV-18 ASS builder: kinetic per-word highlight captions on the
performed grid + ~ WuBu ~ bug. The caption layer also carries the
five montage-cover lines (L03, L15, L26-L28, L32, L42) whose sung
vehicles were refused — captions + performed vocal carry them.
Text/timing authority: performed grid (grid_lines.json + SONG_WORDS.json).
Adapted from the MV-17 builder (fridge-specific tallies/magnets dropped)."""
import json

ROOT = '/home/hatch/workspace/wubutv-network/musicvideo/MV-18_whats-a-sigma-mom'
grid = json.load(open(f'{ROOT}/work/analysis/grid_lines.json'))
words = json.load(open(f'{ROOT}/work/analysis/SONG_WORDS.json'))['words']

def ts(t):
    h = int(t // 3600); m = int((t % 3600) // 60); s = t % 60
    return f'{h}:{m:02d}:{s:05.2f}'

def clean(w):
    return w.strip('.,!?()').replace('{', '').replace('}', '')

HEADER = """[Script Info]
Title: MV-18 What's a Sigma? ~Mom — kinetic layer
ScriptType: v4.00+
PlayResX: 1280
PlayResY: 720
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Line,Arial,44,&H00FFFFFF,&H0000FFFF,&H00141414,&H64000000,-1,0,0,0,100,100,0,0,1,3,1,2,40,40,26,1
Style: Slam,Arial,58,&H00FFFFFF,&H0000FFFF,&H00141414,&H64000000,-1,0,0,0,100,100,0,0,1,4,2,2,40,40,30,1
Style: Bug,Arial,22,&H66FFFFFF,&H66FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,0,0,9,20,16,12,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
ev = []
ACC = r'{\c&H00FFFF&\b1}'
RST = r'{\c&HFFFFFF&\b1}'
SLAM = {1, 16, 29, 43}   # first hook of C1/C2/C3 + the final hook

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

# ---- bug ----
ev.append((0.0, 157.61, 'Bug', r'{\pos(1252,700)}~ WuBu ~'))

ev.sort(key=lambda x: x[0])
lines = [HEADER]
for (s, e, st, txt) in ev:
    if e - s < 0.04:
        continue
    lines.append(f'Dialogue: 0,{ts(s)},{ts(e)},{st},,0,0,0,,{txt}')
open(f'{ROOT}/work/mv18_kinetic.ass', 'w').write('\n'.join(lines) + '\n')
print('events:', len(lines) - 1)
