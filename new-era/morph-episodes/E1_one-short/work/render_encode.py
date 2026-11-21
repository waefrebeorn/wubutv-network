#!/usr/bin/env python3
"""ONE SHORT E1 — board graphics renderer + master encode (one pass).
Full-frame RGBA rendered in PIL frame-by-frame into ffmpeg's stdin; ffmpeg
overlays it on work/joined.mp4, burns the ~ WuBu ~ bug, applies the loudness
pass, encodes. Deterministic (G8). CRF via RENDER_CRF env (18 master,
23 differential). Loudness gain via GAIN_DB env (measured on joined first).

Board state chain (keyed to MEASURED speech, see GATE_LOG):
  CLAIMED 31 flips at 0.30 (the U1 slam)
  COUNTED 20 flips at 18.94 (U2 cliff, "twenty." ends)
  COUNTED 30 flips at 29.00 (U3 tail, batch complete in silence)
  COUNTED blanks at 30.00 (U4 recount begins), flips back to 30 at 39.00
  settle pulse at 50.42 (U6, on "umbrella.")
Question card over the U6 freeze: fades in at 57.98, holds to 60.00.
"""
import subprocess, math, sys, os
from PIL import Image, ImageDraw, ImageFont

EP = '/home/hatch/workspace/wubutv-network/new-era/morph-episodes/E1_one-short'
NOTO = '/usr/share/fonts/truetype/noto'
F_SANS_BLACK = ImageFont.truetype(f'{NOTO}/NotoSans-Black.ttf', 34)
F_SANS_BOLD_LBL = ImageFont.truetype(f'{NOTO}/NotoSans-Bold.ttf', 12)
F_MARKER = ImageFont.truetype(f'{NOTO}/NotoSans-Bold.ttf', 22)
F_CARD = ImageFont.truetype(f'{NOTO}/NotoSerif-BoldItalic.ttf', 44)

INK = (16, 16, 20)
BONE = (237, 230, 218)
LIT = (245, 242, 234)
DIM = (120, 116, 108)
FOREST = (31, 107, 58)

W, H = 1280, 720
CHIP_W, CHIP_H, CHIP_Y = 196, 64, 632
COUNTED_X, CLAIMED_X, MARK_X = 28, 264, 232

FLIPS = [(0.30, 'claimed', 31), (18.94, 'counted', 20), (29.00, 'counted', 30),
         (30.00, 'counted', None), (39.00, 'counted', 30)]
PULSES = [0.30, 18.94, 29.00, 39.00, 50.42]
CARD_T0, CARD_T1 = 57.98, 58.23
CARD_TEXT = 'Then where does the one GO?'

def state_at(t):
    c, cl = None, None
    for ft, which, val in FLIPS:
        if t >= ft:
            if which == 'counted': c = val
            else: cl = val
    return c, cl

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

def draw_card(img, alpha):
    if alpha <= 0:
        return
    d = ImageDraw.Draw(img, 'RGBA')
    bb = d.textbbox((0, 0), CARD_TEXT, font=F_CARD)
    tw, th = bb[2] - bb[0], bb[3] - bb[1]
    cx, cy = W // 2, 478
    pad_x, pad_y = 40, 22
    box = [cx - tw / 2 - pad_x, cy - th / 2 - pad_y,
           cx + tw / 2 + pad_x, cy + th / 2 + pad_y]
    d.rounded_rectangle(box, 14, fill=INK + (int(225 * alpha),),
                        outline=FOREST + (int(255 * alpha),), width=2)
    d.text((cx - tw / 2 - bb[0], cy - th / 2 - bb[1]), CARD_TEXT,
           font=F_CARD, fill=BONE + (int(255 * alpha),))

_cache = {}
def frame(t):
    c, cl = state_at(t)
    p = pulse_amt(t)
    if t < CARD_T0:
        ca = 0.0
    elif t < CARD_T1:
        ca = (t - CARD_T0) / (CARD_T1 - CARD_T0)
    else:
        ca = 1.0
    key = (c, cl, round(p, 2), round(ca, 2))
    if key in _cache:
        return _cache[key]
    img = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    chip(img, COUNTED_X, 'COUNTED', c, p)
    chip(img, CLAIMED_X, 'CLAIMED', cl, p)
    if c is not None and cl is not None:
        d = ImageDraw.Draw(img, 'RGBA')
        marker = '=' if c == cl else '≠'
        bb = d.textbbox((0, 0), marker, font=F_MARKER)
        d.text((MARK_X + (24 - (bb[2] - bb[0])) / 2 - bb[0], CHIP_Y + 20),
               marker, font=F_MARKER, fill=FOREST + (255,))
    draw_card(img, ca)
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
