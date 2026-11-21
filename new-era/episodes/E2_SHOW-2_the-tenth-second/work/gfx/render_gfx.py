#!/usr/bin/env python3
"""Method C graphic layer for E2 SHOW-2 — one deterministic PIL sequence.
Devices: GFX-1 Cull Clock (segmented ring, snaps full on joint frames),
GFX-2 Chalk Tally (serial count, one mark per unit of the show's run),
GFX-3 The Stamp (one firing, U6 handover). See GFX_CARDS.md.
Usage: render_gfx.py <outdir> <stamp_local_frame_in_U6>
Renders 1440 RGBA frames at 1280x720, 24fps, as f%04d.png.
Deterministic: all jitter from fixed seeds.
"""
import math, os, random, sys
from PIL import Image, ImageDraw, ImageFont

OUT = sys.argv[1]
STAMP_LOCAL = int(sys.argv[2]) if len(sys.argv) > 2 else 224
os.makedirs(OUT, exist_ok=True)

W, H = 1280, 720
SS = 3  # supersample for chalk edges
BONE = (238, 234, 222, 255)
CADMIUM = (255, 207, 63, 255)
INK = (16, 16, 18, 255)

CX, CY, RAD, STROKE = 1194, 86, 56, 9
NSEG = 30

FONT_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
if not os.path.exists(FONT_BOLD):
    FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

rng = random.Random(20261115)
SEG_JIT = [(rng.uniform(-0.9, 0.9), rng.uniform(-1.6, 1.6), rng.randint(205, 255))
           for _ in range(NSEG)]

def chalk_arc(draw, cx, cy, r, a0, a1, width, color):
    """Arc with slight radial wobble: drawn as short chord segments."""
    steps = max(2, int(abs(a1 - a0) / 4))
    pts = []
    for i in range(steps + 1):
        a = math.radians(a0 + (a1 - a0) * i / steps)
        rr = r + 0.7 * math.sin(a * 7.0 + r)
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    draw.line(pts, fill=color, width=width, joint="curve")

def draw_clock(base, unit, f):
    """unit 0-based, f = local frame 0..239."""
    layer = Image.new("RGBA", (W * SS, H * SS), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    t = f / 24.0
    # segments remaining: full at t=0, empty at t=10 (one per 8 frames)
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
            # ignition: segments draw on staggered over frames 5..19
            start = 5 + (i % 15)
            if f < start:
                continue
            alpha = int(alpha * min(1.0, (f - start + 1) / 4.0))
        c = (col[0], col[1], col[2], alpha)
        chalk_arc(d, CX * SS, CY * SS, (RAD + jr) * SS * scale,
                  a0, a1, max(2, int(STROKE * SS * scale)), c)
    if unit > 0 and f < 2:
        # snap flash: one cadmium ring ghost on the joint frame
        chalk_arc(d, CX * SS, CY * SS, RAD * SS * 1.13, -90, 270,
                  int(3 * SS), (255, 207, 63, 120))
    layer = layer.resize((W, H), Image.LANCZOS)
    base.alpha_composite(layer)

# ---- chalk tally -------------------------------------------------------
TALLY_X, TALLY_Y = 1086, 176
MARK_W, MARK_H, GATE_GAP = 7, 22, 12

def draw_mark(d, x, y, frac, seed):
    """One tally stroke (vertical) with chalk jitter; frac = draw-on 0..1."""
    r = random.Random(seed)
    ln = MARK_H * frac
    x0 = x + r.uniform(-0.8, 0.8)
    d.line([(x0, y), (x0 + r.uniform(-1.2, 1.2), y + ln)],
           fill=(238, 234, 222, 235), width=3)

def draw_gate_diag(d, x, y, frac, seed):
    r = random.Random(seed)
    x1, y1 = x - 2, y + MARK_H - 2
    x0, y0 = x + 4 * MARK_W + 2, y + 2
    ex = x0 + (x1 - x0) * frac
    ey = y0 + (y1 - y0) * frac
    d.line([(x0, y0), (ex, ey)], fill=(238, 234, 222, 235), width=3)

def draw_tally(base, unit, f):
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    # marks banked before this unit: pilot 6 + previous E2 units
    banked = 6 + unit
    # this unit's mark draws on: U1 with ignition (f 5..19), else f 5..16
    if unit == 0:
        frac = max(0.0, min(1.0, (f - 5) / 14.0))
    else:
        frac = max(0.0, min(1.0, (f - 5) / 11.0))
    total_slots = banked + 1  # including the drawing one
    for n in range(1, total_slots + 1):
        gate = (n - 1) // 5
        pos = (n - 1) % 5
        gx = TALLY_X + gate * (4 * MARK_W + GATE_GAP + 14)
        is_current = (n == total_slots)
        if pos < 4:
            fr = frac if is_current else 1.0
            if fr > 0:
                draw_mark(d, gx + pos * MARK_W, TALLY_Y, fr, 900 + n)
        else:
            fr = frac if is_current else 1.0
            if fr > 0:
                draw_gate_diag(d, gx, TALLY_Y, fr, 900 + n)
    base.alpha_composite(layer)

# ---- the stamp ---------------------------------------------------------
def make_stamp():
    sw, sh = 470, 196
    img = Image.new("RGBA", (sw, sh), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    r = random.Random(423)
    # ink texture: jittered double border
    for inset, wdt in [(6, 5), (18, 2)]:
        pts = []
        for (x, y) in [(inset, inset), (sw - inset, inset), (sw - inset, sh - inset), (inset, sh - inset), (inset, inset)]:
            pts.append((x + r.uniform(-1.5, 1.5), y + r.uniform(-1.5, 1.5)))
        d.line(pts, fill=(255, 207, 63, 245), width=wdt, joint="curve")
    f1 = ImageFont.truetype(FONT_BOLD, 64)
    f2 = ImageFont.truetype(FONT_BOLD, 40)
    d.text((sw / 2, 62), "CULL 423", font=f1, anchor="mm", fill=(255, 207, 63, 250))
    d.text((sw / 2, 138), "TO THE COURIER", font=f2, anchor="mm", fill=(255, 207, 63, 240))
    # speckle knock-out for ink wear
    px = img.load()
    for _ in range(2600):
        x, y = r.randrange(sw), r.randrange(sh)
        if px[x, y][3] > 0 and r.random() < 0.5:
            px[x, y] = (255, 207, 63, int(px[x, y][3] * 0.55))
    return img

STAMP = make_stamp()
STAMP_CENTRE = (306, 606)

def ease_out_back(x):
    c = 1.70158
    return 1 + (c + 1) * (x - 1) ** 3 + c * (x - 1) ** 2

def draw_stamp(base, g):
    start = 5 * 240 + STAMP_LOCAL
    if g < start:
        return
    k = g - start
    if k < 8:
        s = 1.35 - 0.35 * ease_out_back(k / 8.0)
        rot = -12 + 2.0 * (1 - ease_out_back(k / 8.0))
    else:
        s, rot = 1.0, -12.0
    st = STAMP.resize((int(STAMP.width * s), int(STAMP.height * s)), Image.LANCZOS)
    st = st.rotate(rot, resample=Image.BICUBIC, expand=True)
    base.alpha_composite(st, (int(STAMP_CENTRE[0] - st.width / 2),
                              int(STAMP_CENTRE[1] - st.height / 2)))

for g in range(1440):
    unit, f = divmod(g, 240)
    frame = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw_clock(frame, unit, f)
    draw_tally(frame, unit, f)
    draw_stamp(frame, g)
    frame.save(os.path.join(OUT, f"f{g:04d}.png"))
    if g % 240 == 0:
        print("unit", unit + 1, "done", flush=True)
print("rendered 1440 frames")
