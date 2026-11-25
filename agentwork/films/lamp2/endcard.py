#!/usr/bin/env python3
"""End card for THE LAMP: black ground, gold ~ WuBu ~, small credit. 2 s at 24 fps."""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 854, 480
FPS = 24
SECS = 2.0
FONT = "/opt/data/shitpost-box/fonts/Anton-Regular.ttf"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "endcard", "f_%04d.png")

GOLD = (242, 196, 140)


def ease(t):
    return t * t * (3 - 2 * t)


def frame(i, n):
    img = Image.new("RGB", (W, H), (5, 6, 9))
    d = ImageDraw.Draw(img)
    t = i / max(1, n - 1)

    # faint warm pool behind the mark so the black is not dead
    pool = Image.new("L", (W, H), 0)
    pd = ImageDraw.Draw(pool)
    r = int(W * (0.30 + 0.05 * ease(t)))
    pd.ellipse([W // 2 - r, H // 2 - r // 2, W // 2 + r, H // 2 + r // 2],
               fill=int(26 + 18 * ease(t)))
    pool = pool.filter(ImageFilter.GaussianBlur(60))
    img = Image.composite(Image.new("RGB", (W, H), (40, 30, 22)), img, pool)
    d = ImageDraw.Draw(img)

    f_big = ImageFont.truetype(FONT, 84)
    f_small = ImageFont.truetype(FONT, 20)

    mark = "~ WuBu ~"
    bb = d.textbbox((0, 0), mark, font=f_big)
    mw, mh = bb[2] - bb[0], bb[3] - bb[1]
    x = (W - mw) // 2
    y = H // 2 - mh // 2 - 26

    # the mark lands: slide up 18 px and fade in over the first 0.45 s
    p = min(1.0, t / 0.45)
    y += int((1 - ease(p)) * 18)
    alpha = int(255 * p)
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ld = ImageDraw.Draw(layer)
    ld.text((x, y), mark, font=f_big, fill=GOLD + (alpha,))
    img = Image.alpha_composite(img.convert("RGBA"), layer)

    # credit line fades a beat later
    q = min(1.0, max(0.0, (t - 0.3) / 0.5))
    if q > 0:
        line = "wuBu3D  ·  854x480  ·  Piqua, Ohio"
        bb2 = d.textbbox((0, 0), line, font=f_small)
        lx = (W - (bb2[2] - bb2[0])) // 2
        ly = y + mh + 34
        l2 = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(l2).text((lx, ly), line, font=f_small,
                                fill=(154, 147, 132, int(235 * q)))
        img = Image.alpha_composite(img, l2)

    a = np.asarray(img.convert("RGB"), dtype=np.float32) / 255.0
    # grain, so the black matches the film's texture
    rng = np.random.default_rng(7 + i)
    a += rng.normal(0, 0.012, a.shape).astype(np.float32)
    return (np.clip(a, 0, 1) * 255).astype(np.uint8)


def main():
    os.makedirs(os.path.join(HERE, "endcard"), exist_ok=True)
    n = int(SECS * FPS)
    for i in range(n):
        Image.fromarray(frame(i, n)).save(OUT % i, compress_level=1)
    print("endcard frames:", n)


if __name__ == "__main__":
    main()
