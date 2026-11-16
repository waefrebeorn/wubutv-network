#!/usr/bin/env python3
"""Method C graphic layer for HOLD ON E1 — see GFX_CARDS.md.
Device 1: Cull Clock overlay — 1440 RGBA frames at 1280x720/24fps.
Device 2: three chalk picture inserts (rendered as frame sequences
          the assembly cuts in, picture-only, take audio continuous):
  INS-U1 (31f): left-edge docket lines 1-9 faint; fresh BR— draws on.
  INS-U5 (48f): struck line nine + BR— beside it, full composition.
  INS-U6 (36f): wall state + fresh PAID. ASK HIS HAND. draws on.
Deterministic: all jitter from fixed seeds.
Usage: render_gfx.py <clock_outdir> <inserts_outdir>
"""
import math, os, random, sys
from PIL import Image, ImageDraw, ImageFont

CLOCK_OUT = sys.argv[1]
INS_OUT = sys.argv[2]
os.makedirs(CLOCK_OUT, exist_ok=True)
os.makedirs(INS_OUT, exist_ok=True)

W, H = 1280, 720
EP = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
WALL = Image.open(os.path.join(EP, "panels", "PNL-WALL-closeup-16x9.png")).convert("RGB")

BONE = (238, 234, 222)
CADMIUM = (255, 207, 63)
CHALK = (232, 228, 218)

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

# ---------------------------------------------------------------- clock
SS = 3
CX, CY, RAD, STROKE = 1194, 86, 56, 9
NSEG = 30
rng = random.Random(20261116)
SEG_JIT = [(rng.uniform(-0.9, 0.9), rng.uniform(-1.6, 1.6), rng.randint(205, 255))
           for _ in range(NSEG)]

def chalk_arc(draw, cx, cy, r, a0, a1, width, color):
    steps = max(2, int(abs(a1 - a0) / 4))
    pts = []
    for i in range(steps + 1):
        a = math.radians(a0 + (a1 - a0) * i / steps)
        rr = r + 0.7 * math.sin(a * 7.0 + r)
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    draw.line(pts, fill=color, width=width, joint="curve")

def draw_clock(base, unit, f):
    layer = Image.new("RGBA", (W * SS, H * SS), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    spent = min(NSEG, int(f // 8))
    pulse = 0.0
    if unit > 0 and f < 3:
        pulse = 0.07 * (1 - f / 3.0)
    scale = 1.0 + pulse
    for i in range(NSEG):
        if i < spent:
            continue
        ja, jr, ja_alpha = SEG_JIT[i]
        a0 = -90 + i * 12 + 1.6 + ja
        a1 = -90 + (i + 1) * 12 - 1.6 + ja
        col = CADMIUM if i == spent else BONE
        alpha = ja_alpha
        if unit == 0:
            start = 5 + (i % 15)
            if f < start:
                continue
            alpha = int(alpha * min(1.0, (f - start + 1) / 4.0))
        c = (col[0], col[1], col[2], alpha)
        chalk_arc(d, CX * SS, CY * SS, (RAD + jr) * SS * scale,
                  a0, a1, max(2, int(STROKE * SS * scale)), c)
    if unit > 0 and f < 2:
        chalk_arc(d, CX * SS, CY * SS, RAD * SS * 1.13, -90, 270,
                  int(3 * SS), (255, 207, 63, 120))
    layer = layer.resize((W, H), Image.LANCZOS)
    base.alpha_composite(layer)

for g in range(1440):
    unit, f = g // 240, g % 240
    frame = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw_clock(frame, unit, f)
    frame.save(os.path.join(CLOCK_OUT, f"f{g:04d}.png"))
print("clock frames done")

# ---------------------------------------------------------------- chalk
def chalk_text_layer(text, size, alpha, seed, strike=False):
    """Text on a transparent layer with seeded per-glyph jitter."""
    font = ImageFont.truetype(FONT, size)
    tmp = Image.new("RGBA", (10, 10))
    td = ImageDraw.Draw(tmp)
    bbox = td.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    layer = Image.new("RGBA", (tw + 16, th + 16), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    r = random.Random(seed)
    x = 8 - bbox[0]
    for ch in text:
        cw = d.textlength(ch, font=font)
        if ch != " ":
            jy = r.uniform(-1.6, 1.6)
            ja = max(0, min(255, alpha + r.randint(-22, 10)))
            d.text((x, 8 - bbox[1] + jy), ch, font=font,
                   fill=(CHALK[0], CHALK[1], CHALK[2], ja))
        x += cw
    if strike:
        y = 8 + th // 2 + r.randint(-2, 2)
        pts = [(2, y + r.uniform(-2, 2))]
        for px in range(12, tw + 12, 24):
            pts.append((px, y + r.uniform(-2.5, 2.5)))
        d.line(pts, fill=(CHALK[0], CHALK[1], CHALK[2], min(255, alpha + 15)), width=max(4, size // 9))
    return layer

def reveal(layer, frac):
    """Left-to-right draw-on: crop the layer at frac of its width."""
    if frac >= 1.0:
        return layer
    w = max(1, int(layer.width * frac))
    out = Image.new("RGBA", layer.size, (0, 0, 0, 0))
    out.alpha_composite(layer.crop((0, 0, w, layer.height)), (0, 0))
    return out

_SMALL = None
def push_in(base_img, t):
    """Slow push-in 1.00->1.06: crop window shrinks, resized to 1280x720."""
    global _SMALL
    if _SMALL is None:
        _SMALL = base_img.resize((1408, 792), Image.LANCZOS)
    sw, sh = _SMALL.size
    crop_w = int(sw / (1.0 + 0.06 * t))
    crop_h = int(crop_w * H / W)
    x0 = (sw - crop_w) // 2
    y0 = (sh - crop_h) // 2
    return _SMALL.crop((x0, y0, x0 + crop_w, y0 + crop_h)).resize((W, H), Image.LANCZOS)

def docket_edge():
    """The wall's older docket lines, numbered 1-9, faint (45%)."""
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    r = random.Random(77)
    font_n = ImageFont.truetype(FONT, 17)
    d = ImageDraw.Draw(layer)
    for i in range(9):
        y = 120 + i * 52
        a = int(255 * 0.45) + r.randint(-14, 8)
        d.text((46, y), str(i + 1), font=font_n, fill=(CHALK[0], CHALK[1], CHALK[2], a))
        ln = r.randint(90, 210)
        yy = y + 10 + r.uniform(-1.5, 1.5)
        d.line([(78, yy), (78 + ln, yy + r.uniform(-2, 2))],
               fill=(CHALK[0], CHALK[1], CHALK[2], a), width=3)
    return layer

EDGE = docket_edge()
BR = chalk_text_layer("BR\u2014", 58, int(255 * 0.95), seed=41)
LINE9 = chalk_text_layer("BRUNO OWES ME THREE MONTHS", 44, int(255 * 0.80), seed=42, strike=True)
PAID = chalk_text_layer("PAID. ASK HIS HAND.", 54, int(255 * 0.95), seed=43)

def render_insert(name, nframes, draw_fn):
    outdir = os.path.join(INS_OUT, name)
    os.makedirs(outdir, exist_ok=True)
    for i in range(nframes):
        t = i / max(1, nframes - 1)
        frame = push_in(WALL, t).convert("RGBA")
        frame.alpha_composite(EDGE, (0, 0))
        draw_fn(frame, i, nframes)
        frame.convert("RGB").save(os.path.join(outdir, f"f{i:03d}.png"))
    print(name, "done", nframes)

def ins_u1(frame, i, n):
    # BR— draws on over ~0.8s (19 frames) starting at frame 3
    frac = max(0.0, min(1.0, (i - 3) / 19.0))
    if frac > 0:
        frame.alpha_composite(reveal(BR, frac), (330, 300))

def ins_u5(frame, i, n):
    frame.alpha_composite(LINE9, (250, 215))
    frame.alpha_composite(BR, (330, 330))

def ins_u6(frame, i, n):
    frame.alpha_composite(LINE9, (250, 160))
    frame.alpha_composite(BR, (330, 262))
    # PAID draws on over ~1.0s (24 frames) starting at frame 4
    frac = max(0.0, min(1.0, (i - 4) / 24.0))
    if frac > 0:
        frame.alpha_composite(reveal(PAID, frac), (300, 400))

render_insert("ins_u1", 31, ins_u1)
render_insert("ins_u5", 48, ins_u5)
render_insert("ins_u6", 36, ins_u6)
print("ALL GFX DONE")
