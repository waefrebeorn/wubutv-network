#!/usr/bin/env python3
"""MV-19 ASS builder: kinetic per-word highlight captions on the
performed grid + the "?" motif layer (POST-layer only, per
ASSET_BOARD: C1 one small, C2 two, BR one hovering, C3 one per
self on the desync, OUT one over the pair + one in the settle)
+ ~ WuBu ~ bug. Text/timing authority: performed grid
(grid_lines.json + SONG_WORDS.json). Adapted from MV-18's builder."""
import json

ROOT = '/home/hatch/workspace/wubutv-network/musicvideo/MV-19_confused-npc'
grid = json.load(open(f'{ROOT}/work/analysis/grid_lines.json'))
words = json.load(open(f'{ROOT}/work/analysis/SONG_WORDS.json'))['words']

def ts(t):
    h = int(t // 3600); m = int((t % 3600) // 60); s = t % 60
    return f'{h}:{m:02d}:{s:05.2f}'

def clean(w):
    return w.strip('.,!?()').replace('{', '').replace('}', '')

HEADER = """[Script Info]
Title: MV-19 Confused NPC — kinetic layer
ScriptType: v4.00+
PlayResX: 1280
PlayResY: 720
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Line,Arial,44,&H00FFFFFF,&H0000FFFF,&H00141414,&H64000000,-1,0,0,0,100,100,0,0,1,3,1,2,40,40,26,1
Style: Slam,Arial,58,&H00FFFFFF,&H0000FFFF,&H00141414,&H64000000,-1,0,0,0,100,100,0,0,1,4,2,2,40,40,30,1
Style: Qmark,Arial,72,&H001A7AFF,&H001A7AFF,&H00141414,&H00000000,-1,0,0,0,100,100,0,0,1,4,0,5,0,0,0,1
Style: Bug,Arial,22,&H66FFFFFF,&H66FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,0,0,9,20,16,12,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
ev = []
ACC = r'{\c&H00FFFF&\b1}'
RST = r'{\c&HFFFFFF&\b1}'
SLAM = {11, 29, 40, 45}   # first hook of C1/C2/C3 + the final full hook

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

# ---- "?" motif pops: (start, end, x, y, size) ----
Q = [
    (52.30, 53.00, 640, 150, 56),     # C1 close — one small
    (90.65, 91.18, 640, 150, 64),     # C2 — on the Spawn Pop plant
    (104.90, 105.68, 640, 150, 64),   # C2 — on the Skip Cut's last landing
    (107.45, 108.25, 640, 175, 72),   # BR — hovering in the dusk gap
    (125.55, 126.10, 330, 130, 72),   # C3 — one per self, on the desync
    (126.30, 126.85, 640, 130, 72),
    (127.05, 127.60, 950, 130, 72),
    (141.50, 142.40, 640, 140, 80),   # OUT — above both heads, the sway
    (145.60, 146.50, 640, 140, 88),   # OUT — the settle before the last line
]
for (s, e, x, y, size) in Q:
    ev.append((s, e, 'Qmark', rf'{{\pos({x},{y})\fs{size}\fad(50,110)}}?'))

# ---- bug ----
ev.append((0.0, 153.60, 'Bug', r'{\pos(1252,700)}~ WuBu ~'))

ev.sort(key=lambda x: x[0])
lines = [HEADER]
for (s, e, st, txt) in ev:
    if e - s < 0.04:
        continue
    lines.append(f'Dialogue: 0,{ts(s)},{ts(e)},{st},,0,0,0,,{txt}')
open(f'{ROOT}/work/mv19_kinetic.ass', 'w').write('\n'.join(lines) + '\n')
print('events:', len(lines) - 1)
