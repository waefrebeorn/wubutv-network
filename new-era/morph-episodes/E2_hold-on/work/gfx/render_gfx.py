#!/usr/bin/env python3
"""Method C graphic layer for HOLD ON E2 — see GFX_CARDS.md.
Device 1: THE BELL overlay (E1 Cull Clock device, same geometry) —
  1440 RGBA frames at 1280x720/24fps: segmented ring empties over
  exactly 10.0s per unit (1 segment / 8 frames), snaps full on every
  joint frame with a 3-frame settle pulse + cadmium ghost; U1 ignition
  draws on staggered frames 5-19, frame 0 carries no graphic.
Device 2: chalk picture inserts (frame sequences cut in picture-only,
  take audio continuous):
  INS-U1 (20f): names field weathered; fresh JUNE — ELI draws on.
    (20f not the card's ~31f: measured ASR gap between June's line end
    2.92s and the Watcher's line start 3.74s is 0.82s — the insert is
    fitted to the real gap, draw-on compressed to ~0.55s.)
  INS-U5 (48f): field + JUNE — ELI full; MARRIED draws on across it.
    Placed at the chalking beat under "Wall writes married" (the
    verdict line measures late in the take, 6.24-9.58s; window
    182-230 starts just after "Hold held." lands).
  INS-U6 (29f): MARRIED stands finished at 95%, field unchanged.
Deterministic: all jitter from fixed seeds.
Usage: render_gfx.py <bell_outdir> <inserts_outdir>
"""
import math, os, random, sys
from PIL import Image, ImageDraw, ImageFont

BELL_OUT = sys.argv[1]
INS_OUT = sys.argv[2]
os.makedirs(BELL_OUT, exist_ok=True)
os.makedirs(INS_OUT, exist_ok=True)

W, H = 1280, 720
EP = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
WALL = Image.open(os.path.join(EP, "panels", "PNL-WALL2-closeup-16x9.png")).convert("RGB")

BONE = (238, 234, 222)
CADMIUM = (255, 207, 63)
CHALK = (232, 228, 218)

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

# ---------------------------------------------------------------- bell
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

def draw_bell(base, unit, f):
    # Render only the ring's tile (1080,0)-(1280,200) at SS, then
    # composite: the full-frame SS render spent ~2.7s/frame on a
    # 3840x2160 layer that is transparent outside this tile.
    TX, TY, TW, TH = 1080, 0, 200, 200
    layer = Image.new("RGBA", (TW * SS, TH * SS), (0, 0, 0, 0))
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
        chalk_arc(d, (CX - TX) * SS, (CY - TY) * SS, (RAD + jr) * SS * scale,
                  a0, a1, max(2, int(STROKE * SS * scale)), c)
    if unit > 0 and f < 2:
        chalk_arc(d, (CX - TX) * SS, (CY - TY) * SS, RAD * SS * 1.13, -90, 270,
                  int(3 * SS), (255, 207, 63, 120))
    layer = layer.resize((TW, TH), Image.LANCZOS)
    base.alpha_composite(layer, (TX, TY))

for g in range(int(os.environ.get("BELL_START", "0")), 1440):
    unit, f = g // 240, g % 240
    frame = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw_bell(frame, unit, f)
    frame.save(os.path.join(BELL_OUT, f"f{g:04d}.png"))
print("bell frames done")

# ---------------------------------------------------------------- chalk
def chalk_text_layer(text, size, alpha, seed):
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

OLD = int(255 * 0.45)
FRESH = int(255 * 0.95)
FIELD1 = chalk_text_layer("BRUNO \u2014 ROSA", 52, OLD, seed=51)
FIELD2 = chalk_text_layer("PEACH \u2014 LIME", 52, OLD, seed=52)
FIELD3 = chalk_text_layer("H \u2014 M", 52, int(255 * 0.30), seed=53)
JUNE_ELI = chalk_text_layer("JUNE \u2014 ELI", 56, FRESH, seed=61)
MARRIED = chalk_text_layer("MARRIED", 76, FRESH, seed=62)

def field(frame):
    frame.alpha_composite(FIELD1, (150, 165))
    frame.alpha_composite(FIELD2, (150, 280))
    frame.alpha_composite(FIELD3, (760, 165))

def render_insert(name, nframes, draw_fn):
    outdir = os.path.join(INS_OUT, name)
    os.makedirs(outdir, exist_ok=True)
    for i in range(nframes):
        t = i / max(1, nframes - 1)
        frame = push_in(WALL, t).convert("RGBA")
        field(frame)
        draw_fn(frame, i, nframes)
        frame.convert("RGB").save(os.path.join(outdir, f"f{i:03d}.png"))
    print(name, "done", nframes)

def ins_u1(frame, i, n):
    # JUNE — ELI draws on over ~0.55s (13 frames) starting at frame 2
    frac = max(0.0, min(1.0, (i - 2) / 13.0))
    if frac > 0:
        frame.alpha_composite(reveal(JUNE_ELI, frac), (150, 395))

def ins_u5(frame, i, n):
    frame.alpha_composite(JUNE_ELI, (150, 395))
    # MARRIED draws on across the span over ~1.2s (28 frames) from frame 4
    frac = max(0.0, min(1.0, (i - 4) / 28.0))
    if frac > 0:
        frame.alpha_composite(reveal(MARRIED, frac), (330, 492))

def ins_u6(frame, i, n):
    frame.alpha_composite(JUNE_ELI, (150, 395))
    frame.alpha_composite(MARRIED, (330, 492))

render_insert("ins_u1", 20, ins_u1)
render_insert("ins_u5", 48, ins_u5)
render_insert("ins_u6", 29, ins_u6)
print("ALL GFX DONE")
