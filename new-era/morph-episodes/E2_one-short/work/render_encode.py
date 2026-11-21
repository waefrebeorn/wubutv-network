#!/usr/bin/env python3
"""ONE SHORT E2 — board graphics renderer + master encode (one pass).
Full-frame RGBA rendered in PIL frame-by-frame into ffmpeg's stdin; ffmpeg
overlays it on work/joined.mp4, burns the ~ WuBu ~ bug, applies the loudness
pass, encodes. Deterministic (G8). CRF via RENDER_CRF env (18 master,
23 differential). Loudness gain via GAIN_DB env (measured on joined first).

Board state chain (keyed to MEASURED speech, see GATE_LOG):
  CLAIMED 24 flips at 0.30 (the U1 slam; Hale's line @0.00-3.96)
  COUNTED 12 flips at 18.08 (end of U2 Champion claim, "certify my
  five." ends 18.44; board follows the U2 tail GAP-1 cliff)
  COUNTED 18 flips at 24.38 (U3 count "18." lands; holds to U3 tail)
  settle COUNTED 23 | CLAIMED 24 at 47.58 (U5 verdict "23's chairs."
  ends 49.28; settle pulse at the stamp, before the last word lands)
  TAKES 22 | KEPT 1 at 55.78 (U6, on "chair two," the kept chair
  named in the begun office count)
No question card in E2 (that was E1's device). Foam decals: NONE —
the generator rendered the foam X (U5/U6) and the foam 4 (U6, from
behind in profile) in-scene; no post decal was needed (see GATE_LOG).
"""
import subprocess, math, sys, os
from PIL import Image, ImageDraw, ImageFont

EP = '/home/hatch/workspace/wubutv-network/new-era/morph-episodes/E2_one-short'
NOTO = '/usr/share/fonts/truetype/noto'
F_SANS_BLACK = ImageFont.truetype(f'{NOTO}/NotoSans-Black.ttf', 34)
F_SANS_BOLD_LBL = ImageFont.truetype(f'{NOTO}/NotoSans-Bold.ttf', 12)
F_MARKER = ImageFont.truetype(f'{NOTO}/NotoSans-Bold.ttf', 22)

INK = (16, 16, 20)
BONE = (237, 230, 218)
LIT = (245, 242, 234)
DIM = (120, 116, 108)
FOREST = (31, 107, 58)

W, H = 1280, 720
CHIP_W, CHIP_H, CHIP_Y = 196, 64, 632
COUNTED_X, CLAIMED_X, MARK_X = 28, 264, 232

# state entries: (t, counted_label, counted_val, claimed_label, claimed_val)
STATES = [
    (0.00, 'COUNTED', None, 'CLAIMED', None),
    (0.30, 'COUNTED', None, 'CLAIMED', 24),
    (18.08, 'COUNTED', 12, 'CLAIMED', 24),
    (24.38, 'COUNTED', 18, 'CLAIMED', 24),
    (47.58, 'COUNTED', 23, 'CLAIMED', 24),
    (55.78, 'TAKES', 22, 'KEPT', 1),
]
PULSES = [0.30, 18.08, 24.38, 47.58, 55.78]

def state_at(t):
    cur = STATES[0]
    for s in STATES:
        if t >= s[0]:
            cur = s
    return cur

def pulse_amt(t):
    amt = 0.0
    for pt in PULSES:
        if pt <= t < pt + 0.21:
            amt = max(amt, math.sin(math.pi * (t - pt) / 0.21))
    return amt

def chip(img, x, label, value, pulse):
    d = ImageDraw.Draw(img, 'RGBA')
    d.rounded_rectangle([x, CHIP_Y, x + CHIP_W, CHIP_Y + CHIP_H], 10,
                        fill=INK + (238,), outline=FOREST + (255,), width=2)
    d.text((x + 12, CHIP_Y + 6), label, font=F_SANS_BOLD_LBL, fill=BONE + (230,))
    txt = '––' if value is None else str(value)
    col = DIM if value is None else LIT
    bb = d.textbbox((0, 0), txt, font=F_SANS_BLACK)
    tw = bb[2] - bb[0]
    d.text((x + (CHIP_W - tw) / 2 - bb[0], CHIP_Y + 22), txt,
           font=F_SANS_BLACK, fill=col + (255,))
    if pulse > 0:
        d.rounded_rectangle([x, CHIP_Y, x + CHIP_W, CHIP_Y + CHIP_H], 10,
                            fill=(255, 255, 255, int(55 * pulse)))

_cache = {}
def frame(t):
    _, cl_lbl, c, cr_lbl, cl = state_at(t)
    p = pulse_amt(t)
    key = (cl_lbl, c, cr_lbl, cl, round(p, 2))
    if key in _cache:
        return _cache[key]
    img = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    chip(img, COUNTED_X, cl_lbl, c, p)
    chip(img, CLAIMED_X, cr_lbl, cl, p)
    if c is not None and cl is not None:
        d = ImageDraw.Draw(img, 'RGBA')
        marker = '=' if c == cl else '≠'
        bb = d.textbbox((0, 0), marker, font=F_MARKER)
        d.text((MARK_X + (24 - (bb[2] - bb[0])) / 2 - bb[0], CHIP_Y + 20),
               marker, font=F_MARKER, fill=FOREST + (255,))
    b = img.tobytes()
    if len(_cache) < 400:
        _cache[key] = b
    return b

def main():
    out_path = sys.argv[1]
    gain = os.environ.get('GAIN_DB', '0.0')
    bug = ("drawtext=fontfile=/usr/share/fonts/truetype/noto/NotoSerif-Bold.ttf:"
           "text='~ WuBu ~':fontsize=25:fontcolor=0xC9A227:"
           "shadowcolor=black@0.6:shadowx=1:shadowy=1:x=w-tw-20:y=h-th-16")
    cmd = ['ffmpeg', '-v', 'error', '-i', f'{EP}/work/joined.mp4',
           '-f', 'rawvideo', '-pix_fmt', 'rgba', '-s', f'{W}x{H}', '-r', '24', '-i', '-',
           '-filter_complex', f'[0:v][1:v]overlay=0:0:format=auto,{bug},format=yuv420p',
           '-af', f'volume={gain}dB,alimiter=limit=0.84',
           '-c:v', 'libx264', '-crf', os.environ.get('RENDER_CRF', '18'),
           '-preset', 'medium',
           '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart',
           '-frames:v', '1440', out_path]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for f in range(1440):
        proc.stdin.write(frame(f / 24))
    proc.stdin.close()
    rc = proc.wait()
    print('ffmpeg rc:', rc)

if __name__ == '__main__':
    main()
