#!/usr/bin/env python3
"""WuBuTV ident: cards (intro / lockup / endcard) + cut plan.

Everything except the corpus montage is generated here at 1280x720 / 24 fps.
The wordmark is exact: "~ WuBu ~" in gold.
"""
import json
import math
import os

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE = "/opt/data/work/ident"
FONT = "/opt/data/shitpost-box/fonts/Anton-Regular.ttf"
W, H, FPS = 1280, 720, 24
GOLD = (242, 196, 140)
CREAM = (242, 232, 214)
DIM = (154, 147, 132)
BG = (5, 6, 9)

# ---------------------------------------------------------------- cut plan
# montage runs from 2.5 s; each entry = (bumper number, in-point, length in beats)
# one beat = 0.5 s. The stare (44) recurs: it is the brainwash anchor.
BEAT = 0.5
PLAN = [
    (49, 0.4, 2),   # test card, holds
    (11, 4.6, 1),   # static CRT tap
    (44, 1.0, 1),   # STARE
    (1, 0.6, 1),    # INF:0 title card
    (46, 3.6, 1),   # buzzer hit
    (48, 3.4, 1),   # wrist / clock
    (9, 0.6, 2),    # intermission marquee
    (39, 2.0, 1),   # Colonel composure
    (44, 3.0, 1),   # STARE (second)
    (8, 6.2, 2),    # PLEASE STAND BY placard
    (57, 0.8, 1),   # blank road map
    (40, 3.0, 1),   # eyes closed
    (12, 1.0, 2),   # brass plaque
    (34, 0.8, 1),   # news desk + globe
    (44, 5.0, 1),   # STARE (third)
    (56, 2.0, 1),   # weather map
    (25, 0.6, 1),   # curtain / stage
    (59, 3.0, 2),   # curtains closing
    (11, 6.6, 1),   # static
    (49, 1.2, 2),   # test card closes the loop
]

INTRO = 2.5
MONT = sum(l for _, _, l in PLAN) * BEAT          # 14.0 s
LOCKUP = 5.0
ENDCARD = 4.0
TOTAL = INTRO + MONT + LOCKUP + ENDCARD           # 25.5 s


def ease(t):
    return t * t * (3 - 2 * t)


def grain(a, seed, amt=0.012):
    rng = np.random.default_rng(seed)
    return a + rng.normal(0, amt, a.shape).astype(np.float32)


def to_u8(a):
    return (np.clip(a, 0, 1) * 255).astype(np.uint8)


def new_canvas():
    return np.zeros((H, W, 3), dtype=np.float32)


def add_radial(canvas, cx, cy, r, colour, strength, power=2.2):
    y0, y1 = max(0, cy - r), min(H, cy + r)
    x0, x1 = max(0, cx - r), min(W, cx + r)
    if y1 <= y0 or x1 <= x0:
        return
    yy, xx = np.mgrid[y0 - cy:y1 - cy, x0 - cx:x1 - cx].astype(np.float32)
    d2 = (xx * xx + yy * yy) / float(r * r)
    k = np.clip(1 - d2, 0, 1) ** power
    col = np.array(colour, dtype=np.float32) / 255.0
    canvas[y0:y1, x0:x1] += k[..., None] * col * strength


def font(sz):
    return ImageFont.truetype(FONT, sz)


def text_layer(lines, alpha=255, spacing=1.0):
    """lines: [(text, size, colour, dy)] centred; returns RGBA overlay."""
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    for txt, sz, col, dy in lines:
        f = font(sz)
        bb = d.textbbox((0, 0), txt, font=f)
        x = (W - (bb[2] - bb[0])) // 2
        d.text((x, dy), txt, font=f, fill=col + (alpha,))
    return ov


def wordmark(alpha=255, scale=1.0, dy=0):
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    f = font(int(118 * scale))
    d = ImageDraw.Draw(ov)
    mark = "~ WuBu ~"
    bb = d.textbbox((0, 0), mark, font=f)
    x = (W - (bb[2] - bb[0])) // 2
    y = H // 2 - (bb[3] - bb[1]) // 2 - 30 + dy
    d.text((x, y), mark, font=f, fill=GOLD + (alpha,))
    return ov


def ring(canvas, cx, cy, r, width, strength):
    r = int(r)
    width = max(1.5, float(width))
    cx, cy = int(cx), int(cy)
    if r < 2:
        return
    pad = int(r + width * 3)
    y0, y1 = max(0, cy - pad), min(H, cy + pad)
    x0, x1 = max(0, cx - pad), min(W, cx + pad)
    if y1 <= y0 or x1 <= x0:
        return
    yy, xx = np.mgrid[y0 - cy:y1 - cy, x0 - cx:x1 - cx].astype(np.float32)
    d = np.sqrt(xx * xx + yy * yy)
    k = np.exp(-((d - r) ** 2) / (2 * (width * 0.6) ** 2))
    canvas[y0:y1, x0:x1] += k[..., None] * np.array(GOLD, dtype=np.float32) / 255.0 * strength


# ---------------------------------------------------------------- intro
def intro_frame(i, n):
    c = new_canvas()
    t = i / n
    # static that resolves: noise fading as the mark lands
    rng = np.random.default_rng(1000 + i)
    noise = rng.random((H, W, 3)).astype(np.float32)
    noise_strength = max(0.0, 0.55 * (1 - t / 0.55))
    c += noise * noise_strength * 0.5
    add_radial(c, W // 2, H // 2, 300, GOLD, 0.045 * ease(min(1, t / 0.8)))

    # characters slam in on a 4-frame stagger
    chars = list("~ WuBu ~")
    img = Image.fromarray(to_u8(c)).convert("RGBA")
    stagger = 4
    for k, ch in enumerate(chars):
        if ch == " ":
            continue
        start = 2 + k * stagger
        if i < start:
            continue
        p = ease(min(1.0, (i - start) / 5.0))
        f = font(118)
        d = ImageDraw.Draw(img)
        full = "~ WuBu ~"
        bb = d.textbbox((0, 0), full, font=f)
        x0 = (W - (bb[2] - bb[0])) // 2
        # x offset of this char inside the full string
        pre = d.textbbox((0, 0), full[:k], font=f)
        x = x0 + (pre[2] - pre[0])
        y = H // 2 - (bb[3] - bb[1]) // 2 - 30
        y += int((1 - p) * -14)
        a = int(255 * p)
        d.text((x, y), ch, font=f, fill=GOLD + (a,))
    c = np.asarray(img.convert("RGB"), dtype=np.float32) / 255.0
    # a single scanline sweep across the intro
    sy = int(H * (t * 1.3 % 1.0))
    c[max(0, sy - 2):sy + 2] += 0.05
    return to_u8(grain(c, 77 + i, 0.02))


# ---------------------------------------------------------------- lockup
def lockup_frame(i, n):
    c = new_canvas()
    t = i / n
    # rings marching outward on the beat
    for k in range(4):
        ph = ((t * 2.0) + k * 0.25) % 1.0
        r = 60 + ph * 620
        ring(c, W // 2, H // 2 - 20, r, 2.0, 0.30 * (1 - ph) ** 1.5)
    add_radial(c, W // 2, H // 2 - 20, 300, GOLD, 0.030 + 0.012 * math.sin(t * math.pi * 4))

    # scanlines
    ys = (np.arange(H) % 4 == 0).astype(np.float32)[:, None, None]
    c *= (1 - ys * 0.06)

    img = Image.fromarray(to_u8(c)).convert("RGBA")
    pulse = 1.0 + 0.035 * math.sin(t * math.pi * 4)
    img = Image.alpha_composite(img, wordmark(255, pulse, 0))
    sub = text_layer([("YOU ARE WATCHING THE WUBU NETWORK", 26, DIM, H // 2 + 72)])
    # words appear in sequence
    q = min(1.0, max(0.0, (t - 0.30) / 0.50))
    if q > 0:
        sub = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        d = ImageDraw.Draw(sub)
        f = font(26)
        full = "YOU ARE WATCHING THE WUBU NETWORK"
        spacing = d.textbbox((0, 0), full, font=f)
        x = (W - (spacing[2] - spacing[0])) // 2
        d.text((x, H // 2 + 72), full, font=f, fill=DIM + (255,))
        wmask = Image.new("L", (W, H), 0)
        ImageDraw.Draw(wmask).rectangle(
            [0, 0, int((W + 20) * q), H], fill=255)
        sub.putalpha(Image.composite(sub.getchannel("A"), Image.new("L", (W, H), 0), wmask))
    img = Image.alpha_composite(img, sub)
    c = np.asarray(img.convert("RGB"), dtype=np.float32) / 255.0
    # vignette
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    v = 1 - 0.45 * (((xx - W / 2) ** 2 / (W / 2) ** 2 + (yy - H / 2) ** 2 / (H / 2) ** 2) ** 1.5)
    c *= np.clip(v, 0, 1)[..., None]
    return to_u8(grain(c, 300 + i, 0.015))


# ---------------------------------------------------------------- endcard
def end_frame(i, n):
    c = new_canvas()
    t = i / n
    add_radial(c, W // 2, H // 2, 480, GOLD, 0.035)
    img = Image.fromarray(to_u8(c)).convert("RGBA")
    fade = 1.0 if t < 0.72 else max(0.0, (1 - t) / 0.28)
    img = Image.alpha_composite(img, wordmark(int(255 * fade), 1.0, 0))
    lines = [("DAYTON, OHIO  ·  INF:0", 24, DIM, H // 2 + 66),
             ("the work is the receipt", 18, (110, 104, 94), H // 2 + 108)]
    img = Image.alpha_composite(img, text_layer(lines, int(230 * fade)))
    c = np.asarray(img.convert("RGB"), dtype=np.float32) / 255.0
    return to_u8(grain(c, 500 + i, 0.012))


def dump(name, fn, secs):
    out = os.path.join(HERE, name)
    os.makedirs(out, exist_ok=True)
    n = int(round(secs * FPS))
    for i in range(n):
        Image.fromarray(fn(i, n)).save(os.path.join(out, f"f_{i:04d}.png"), compress_level=1)
    print(name, n, "frames")


if __name__ == "__main__":
    dump("c_intro", intro_frame, INTRO)
    dump("c_lockup", lockup_frame, LOCKUP)
    dump("c_end", end_frame, ENDCARD)
    json.dump(dict(plan=PLAN, beat=BEAT, intro=INTRO, mont=MONT, lockup=LOCKUP,
                   end=ENDCARD, total=TOTAL, fps=FPS, w=W, h=H),
              open(os.path.join(HERE, "plan.json"), "w"), indent=1)
    print("total", TOTAL, "s")
