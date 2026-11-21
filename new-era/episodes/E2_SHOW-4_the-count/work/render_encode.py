#!/usr/bin/env python3
"""THE COUNT E2 — Split Total graphics renderer + master encode (one pass).
Renders the furniture strip (760x144 RGBA) frame-by-frame into ffmpeg's stdin;
ffmpeg overlays it on work/joined.mp4, burns the ~ WuBu ~ bug, applies the
loudness pass, encodes CRF 18. Deterministic (G8): no randomness anywhere."""
import subprocess, math, sys, os
from PIL import Image, ImageDraw, ImageFont

E2 = '/home/hatch/workspace/wubutv-network/new-era/episodes/E2_SHOW-4_the-count'
NOTO = '/usr/share/fonts/truetype/noto'
F_SANS_BLACK = ImageFont.truetype(f'{NOTO}/NotoSans-Black.ttf', 34)
F_SANS_BOLD_LBL = ImageFont.truetype(f'{NOTO}/NotoSans-Bold.ttf', 12)
F_SERIF_BOLD = ImageFont.truetype(f'{NOTO}/NotoSerif-Bold.ttf', 32)
F_MARKER = ImageFont.truetype(f'{NOTO}/NotoSans-Bold.ttf', 22)
F_DIGIT_SANS = ImageFont.truetype(f'{NOTO}/NotoSans-Black.ttf', 30)
F_DIGIT_SERIF = ImageFont.truetype(f'{NOTO}/NotoSerif-Bold.ttf', 30)

INK = (16, 16, 20)
BONE = (237, 230, 218)
LIT = (245, 242, 234)
COBALT = (36, 86, 200)
FOREST = (31, 107, 58)

SW, SH = 760, 144
CHIP_W, CHIP_H, CHIP_Y = 196, 64, 56
BOARD_X, MARK_X, LEDG_X, TALLY_X = 28, 232, 264, 478

FLIPS = [(10.30, 'board', 1007), (13.05, 'board', 1008), (13.05, 'ledger', 1008),
         (22.90, 'board', 1009), (28.28, 'ledger', 1009),
         (40.70, 'board', 1011), (40.70, 'ledger', 1010), (52.00, 'board', 1012)]
SETTLE_T, SETTLE_D = 40.30, 0.40
PULSES = [(8.09, 'ledger'), (10.30, 'board'), (13.05, 'board'), (13.05, 'ledger'),
          (22.90, 'board'), (28.28, 'ledger'), (47.32, 'board'), (48.30, 'board'),
          (52.00, 'board'), (57.32, 'board')]
MIGRATIONS = [(2.95, 0.7, 'board', 'ledger', '6', F_DIGIT_SANS),
              (46.62, 0.7, 'ledger', 'board', '1', F_DIGIT_SERIF)]
STRADDLE_T, STRADDLE_D = 9.70, 0.60
TALLY_T = 33.88  # re-count event start

def state_at(t):
    b, l = 1006, 1007
    for ft, which, val in FLIPS:
        if t >= ft:
            if which == 'board': b = val
            else: l = val
    return b, l

def pulse_amt(t, chip):
    amt = 0.0
    for pt, pc in PULSES:
        if pc == chip and pt <= t < pt + 0.21:
            amt = max(amt, math.sin(math.pi * (t - pt) / 0.21))
    return amt

def chip(img, x, kind, value, pulse):
    d = ImageDraw.Draw(img, 'RGBA')
    if kind == 'board':
        fill, border, vcol, vfont, lbl = (16, 16, 20, 238), FOREST, LIT, F_SANS_BLACK, 'BOARD'
        lcol = BONE
    else:
        fill, border, vcol, vfont, lbl = (237, 230, 218, 242), FOREST, COBALT, F_SERIF_BOLD, 'LEDGER'
        lcol = INK
    d.rounded_rectangle([x, CHIP_Y, x + CHIP_W, CHIP_Y + CHIP_H], 10,
                        fill=fill, outline=border + (255,), width=2)
    d.text((x + 12, CHIP_Y + 6), lbl, font=F_SANS_BOLD_LBL, fill=lcol + (230,))
    txt = str(value)
    bb = d.textbbox((0, 0), txt, font=vfont)
    tw = bb[2] - bb[0]
    d.text((x + (CHIP_W - tw) / 2 - bb[0], CHIP_Y + 22), txt, font=vfont, fill=vcol + (255,))
    if pulse > 0:
        d.rounded_rectangle([x, CHIP_Y, x + CHIP_W, CHIP_Y + CHIP_H], 10,
                            fill=(255, 255, 255, int(55 * pulse)))

def draw_tally(img, t):
    d = ImageDraw.Draw(img, 'RGBA')
    x, y = TALLY_X, CHIP_Y
    d.rounded_rectangle([x, y, x + 64, y + CHIP_H], 10, fill=(16, 16, 20, 238),
                        outline=FOREST + (255,), width=2)
    for i in range(4):
        bx = x + 12 + i * 10
        d.line([bx, y + 14, bx, y + 46], fill=(245, 242, 234, 255), width=4)
    # diagonal: white before event, un-draws 33.88-34.18, cobalt serif after 34.28
    if t < TALLY_T:
        col, a = (245, 242, 234), 255
        d.line([x + 8, y + 48, x + 46, y + 12], fill=col + (a,), width=4)
    elif t < TALLY_T + 0.30:
        a = int(255 * (1 - (t - TALLY_T) / 0.30))
        d.line([x + 8, y + 48, x + 46, y + 12], fill=(245, 242, 234, a), width=4)
    elif t < TALLY_T + 0.50:
        pass  # the gap: the mark is gone
    elif t < TALLY_T + 0.80:
        p = (t - TALLY_T - 0.50) / 0.30
        ex = x + 8 + (x + 46 - (x + 8)) * p
        ey = y + 48 + (y + 12 - (y + 48)) * p
        d.line([x + 8, y + 48, ex, ey], fill=COBALT + (255,), width=5)
    else:
        d.line([x + 8, y + 48, x + 46, y + 12], fill=COBALT + (255,), width=5)

def bezier(p0, p1, p2, t):
    return ((1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0],
            (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1])

def centre(kind):
    x = BOARD_X if kind == 'board' else LEDG_X
    return (x + CHIP_W / 2, CHIP_Y + CHIP_H / 2)

def frame(t):
    img = Image.new('RGBA', (SW, SH), (0, 0, 0, 0))
    b, l = state_at(t)
    if SETTLE_T <= t < SETTLE_T + SETTLE_D:
        # crossfade old state -> (1011, 1010) across the re-anchor joint
        p = (t - SETTLE_T) / SETTLE_D
        old = Image.new('RGBA', (SW, SH), (0, 0, 0, 0))
        chip(old, BOARD_X, 'board', b, 0); chip(old, LEDG_X, 'ledger', l, 0)
        new = Image.new('RGBA', (SW, SH), (0, 0, 0, 0))
        chip(new, BOARD_X, 'board', 1011, 0); chip(new, LEDG_X, 'ledger', 1010, 0)
        img = Image.blend(old, new, p)
        b, l = (1011, 1010) if p >= 0.5 else (b, l)
    else:
        chip(img, BOARD_X, 'board', b, pulse_amt(t, 'board'))
        chip(img, LEDG_X, 'ledger', l, pulse_amt(t, 'ledger'))
    d = ImageDraw.Draw(img, 'RGBA')
    marker = '=' if b == l else '≠'
    bb = d.textbbox((0, 0), marker, font=F_MARKER)
    d.text((MARK_X + (24 - (bb[2] - bb[0])) / 2 - bb[0], CHIP_Y + 20), marker,
           font=F_MARKER, fill=FOREST + (255,))
    if 30.0 <= t < 40.0:
        draw_tally(img, t)
        d = ImageDraw.Draw(img, 'RGBA')
    # migrations
    for mt, dur, src, dst, glyph, gfont in MIGRATIONS:
        if mt <= t < mt + dur:
            p = (t - mt) / dur
            pe = p * p * (3 - 2 * p)
            p0, p2 = centre(src), centre(dst)
            p1 = ((p0[0] + p2[0]) / 2, min(p0[1], p2[1]) - 36)
            x, y = bezier(p0, p1, p2, pe)
            a = int(255 * (math.sin(math.pi * p) ** 0.5))
            gb = d.textbbox((0, 0), glyph, font=gfont)
            gx, gy = x - (gb[2] - gb[0]) / 2 - gb[0], y - (gb[3] - gb[1]) / 2 - gb[1]
            d.text((gx + 1, gy + 1), glyph, font=gfont, fill=BONE + (a,))
            d.text((gx, gy), glyph, font=gfont, fill=FOREST + (a,))
    # straddle: the plate's 7 slides into the board chip across joint 1
    if STRADDLE_T <= t < STRADDLE_T + STRADDLE_D:
        p = (t - STRADDLE_T) / STRADDLE_D
        pe = p * p * (3 - 2 * p)
        x = (BOARD_X + CHIP_W + 44) + (BOARD_X + CHIP_W / 2 - (BOARD_X + CHIP_W + 44)) * pe
        y = CHIP_Y + CHIP_H / 2
        a = int(255 * (math.sin(math.pi * min(p * 1.15, 1.0)) ** 0.5))
        gb = d.textbbox((0, 0), '7', font=F_DIGIT_SANS)
        d.text((x - (gb[2] - gb[0]) / 2 - gb[0] + 1, y - (gb[3] - gb[1]) / 2 - gb[1] + 1),
               '7', font=F_DIGIT_SANS, fill=BONE + (a,))
        d.text((x - (gb[2] - gb[0]) / 2 - gb[0], y - (gb[3] - gb[1]) / 2 - gb[1]),
               '7', font=F_DIGIT_SANS, fill=FOREST + (a,))
    return img

def main():
    out_path = sys.argv[1] if len(sys.argv) > 1 else f'{E2}/masters/e2_show4_the-count_16x9.mp4'
    bug = ("drawtext=fontfile=/usr/share/fonts/truetype/noto/NotoSerif-Bold.ttf:"
           "text='~ WuBu ~':fontsize=25:fontcolor=0xC9A227:"
           "shadowcolor=black@0.6:shadowx=1:shadowy=1:x=w-tw-20:y=h-th-16")
    cmd = ['ffmpeg', '-v', 'error', '-i', f'{E2}/work/joined.mp4',
           '-f', 'rawvideo', '-pix_fmt', 'rgba', '-s', f'{SW}x{SH}', '-r', '24', '-i', '-',
           '-filter_complex', f'[0:v][1:v]overlay=0:576:format=auto,{bug},format=yuv420p',
           '-af', 'volume=-1.0dB,alimiter=limit=0.84',
           '-c:v', 'libx264', '-crf', os.environ.get('RENDER_CRF', '18'), '-preset', 'medium',
           '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', '-frames:v', '1440', out_path]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for f in range(1440):
        proc.stdin.write(frame(f / 24).tobytes())
    proc.stdin.close()
    rc = proc.wait()
    print('ffmpeg rc:', rc)

if __name__ == '__main__':
    main()
