#!/usr/bin/env python3
"""THE LAMP, second cut.

Painted plates + keyed silhouettes + 2.5D camera. No renderer, no primitives.
The turn is shown, not narrated: shots 4 and 5 carry it in silence.
"""
import argparse
import math
import os
import subprocess
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
PLATES = os.path.join(HERE, "plates")
CHARS = os.path.join(HERE, "chars")
FONT = "/opt/data/shitpost-box/fonts/Anton-Regular.ttf"
_FONT = None
_CAP_CACHE = {}

W, H = 854, 480
FPS = 24

# ---------------------------------------------------------------- shots
# (start_s, end_s, plate, camera drift, list of actors, caption, vo)
SHOTS = [
    dict(t=(0.0, 7.5), plate="s1_wide.png", drift=+1,
         actors=[dict(p="walk", x=(0.02, 0.46), by=0.735, h=0.30, glow=1.0)],
         cap=("Every night, the lamplighter", "walks the plain"), vo="vo_01"),
    dict(t=(7.5, 15.5), plate="s2_post.png", drift=-1,
         actors=[dict(p="offer", x=(0.60, 0.60), by=0.760, h=0.46, glow=1.0)],
         cap=("He lights every lamp", "he passes"), vo="vo_02"),
    dict(t=(15.5, 23.5), plate="s3_boulder.png", drift=+1,
         actors=[dict(p="walk", x=(0.60, 0.60), by=0.720, h=0.34, glow=1.0),
                 dict(p="sit", x=(0.31, 0.31), by=0.700, h=0.17, glow=0.0)],
         cap=("Tonight", "someone is waiting"), vo="vo_03"),
    dict(t=(23.5, 31.5), plate="s4_path.png", drift=-1,
         actors=[dict(p="offer", x=(0.28, 0.28), by=0.860, h=0.64, glow=1.0),
                 dict(p="sit", x=(0.74, 0.74), by=0.805, h=0.21, glow=0.0)],
         cap=None, vo=None),
    dict(t=(31.5, 39.5), plate="s5_afterglow.png", drift=+1,
         actors=[dict(p="stand_empty", x=(0.30, 0.30), by=0.745, h=0.31, glow=0.0),
                 dict(p="walk", x=(0.44, 0.82), by=0.722, h=(0.15, 0.21), glow=1.0, flip=True)],
         cap=None, vo=None),
    dict(t=(39.5, 46.5), plate="s6_far.png", drift=-1,
         actors=[dict(p="walk_empty", x=(0.52, 0.60), by=0.720, h=(0.20, 0.13), glow=0.0)],
         cap=("He walks home", "without it"), vo="vo_06"),
]

# lantern position inside the cut-out, as a fraction of its bounding box
LANTERN = {"walk": (0.17, 0.70), "offer": (0.86, 0.42), "walk_empty": (0.5, 0.6), "stand_empty": (0.5, 0.6)}


def cutout(name):
    """White background -> alpha. Tint to near-black with a cool lift so it sits in the plate."""
    im = Image.open(os.path.join(CHARS, name)).convert("RGB")
    a = np.asarray(im, dtype=np.float32) / 255.0
    lum = a.mean(axis=2)
    al = np.clip((1.0 - lum) * 5.0 - 0.25, 0.0, 1.0)
    al = (al > 0.45).astype(np.float32)
    al = np.asarray(Image.fromarray((al * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.8)),
                    dtype=np.float32) / 255.0
    ys, xs = np.where(al > 0.4)
    if len(xs) == 0:
        raise SystemExit(f"{name}: empty silhouette")
    box = (xs.min(), ys.min(), xs.max() + 1, ys.max() + 1)
    rgb = np.zeros((a.shape[0], a.shape[1], 3), dtype=np.float32)
    rgb[..., 0], rgb[..., 1], rgb[..., 2] = 0.016, 0.021, 0.034
    return rgb[box[1]:box[3], box[0]:box[2]], al[box[1]:box[3], box[0]:box[2]]


CACHE = {}
PLATE_CACHE = {}


def sprite(name, tw=None, th=None):
    key = (name, tw, th)
    if key in CACHE:
        return CACHE[key]
    base = (name, None, None)
    if base not in CACHE:
        CACHE[base] = cutout(name + ".png")
    rgb, al = CACHE[base]
    if tw is None:
        return rgb, al
    s_rgb = np.asarray(Image.fromarray((rgb * 255).astype(np.uint8)).resize((tw, th), Image.LANCZOS),
                       dtype=np.float32) / 255.0
    s_al = np.asarray(Image.fromarray((al * 255).astype(np.uint8)).resize((tw, th), Image.LANCZOS),
                      dtype=np.float32) / 255.0
    edge = np.asarray(Image.fromarray((s_al * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(3)),
                      dtype=np.float32) / 255.0
    edge = np.clip(edge - s_al, 0, 1) * s_al
    CACHE[key] = (s_rgb, s_al, edge)
    return CACHE[key]


def ease(t):
    return t * t * (3 - 2 * t)


def ease_io(t):
    return 0.5 - 0.5 * math.cos(math.pi * min(max(t, 0), 1))


def lerp(a, b, t):
    if isinstance(a, tuple):
        return tuple(lerp(a[i], b[i], t) for i in range(len(a)))
    return a + (b - a) * t


def place_actor(canvas, act, prog, frame_idx):
    base_rgb, _ = sprite(act["p"])
    h_frac = act["h"] if not isinstance(act["h"], tuple) else lerp(act["h"][0], act["h"][1], prog)
    th = max(8, int(h_frac * H))
    tw = max(4, int(th * base_rgb.shape[1] / base_rgb.shape[0]))
    s_rgb, s_al, edge = sprite(act["p"], tw, th)
    if act.get("flip"):
        s_rgb, s_al, edge = s_rgb[:, ::-1], s_al[:, ::-1], edge[:, ::-1]

    xfrac = act["x"] if not isinstance(act["x"], tuple) else lerp(act["x"][0], act["x"][1], ease(prog))
    px = int(xfrac * W) - tw // 2
    py = int(act["by"] * H) - th

    # contact shadow first: a figure without one floats
    ew, eh = int(tw * 1.05), max(8, int(th * 0.16))
    pad = max(4, int(th * 0.06))
    tile = Image.new("L", (ew + pad * 2, eh + pad * 2), 0)
    ImageDraw.Draw(tile).ellipse([pad, pad, pad + ew, pad + eh],
                                 fill=int(120 * (0.5 + 0.5 * h_frac)))
    tile = tile.filter(ImageFilter.GaussianBlur(max(2, int(th * 0.045))))
    ta = np.asarray(tile, dtype=np.float32) / 255.0
    sy = py + th - eh // 2 - pad
    sx = px + tw // 2 - (ew // 2 + pad)
    ty0, ty1 = max(0, sy), min(H, sy + ta.shape[0])
    tx0, tx1 = max(0, sx), min(W, sx + ta.shape[1])
    if ty1 > ty0 and tx1 > tx0:
        sub = ta[ty0 - sy:ty0 - sy + (ty1 - ty0), tx0 - sx:tx0 - sx + (tx1 - tx0)]
        canvas[ty0:ty1, tx0:tx1] *= (1.0 - sub[..., None] * 0.85)

    # silhouette, with a cool rim from the moon side
    rim = edge[..., None] * np.array([0.30, 0.38, 0.55], dtype=np.float32) * 0.55
    comp = s_rgb + rim

    y0, x0 = max(0, py), max(0, px)
    y1, x1 = min(H, py + th), min(W, px + tw)
    cy0, cx0 = y0 - py, x0 - px
    cy1, cx1 = cy0 + (y1 - y0), cx0 + (x1 - x0)
    if y1 <= y0 or x1 <= x0:
        return None
    a = s_al[cy0:cy1, cx0:cx1][..., None]
    canvas[y0:y1, x0:x1] = canvas[y0:y1, x0:x1] * (1 - a) + comp[cy0:cy1, cx0:cx1] * a

    # lantern: warm core, halo, and a pool of light on the ground
    if act.get("glow", 0) > 0:
        lx, ly = LANTERN[act["p"]]
        gx, gy = x0 + int(lx * tw), py + int(ly * th)
        flick = 0.86 + 0.14 * math.sin(frame_idx * 1.7 + 1.1) * math.cos(frame_idx * 0.53)
        g = act["glow"] * flick
        add_glow(canvas, gx, gy, int(th * 0.20), (1.00, 0.66, 0.30), 0.34 * g)
        add_glow(canvas, gx, gy, int(th * 0.07), (1.00, 0.84, 0.56), 0.90 * g)
        add_glow(canvas, gx, int(py + th), int(th * 0.26), (1.00, 0.60, 0.26), 0.09 * g, squash=0.30)
    return (px, py, tw, th)


_GLOW_CACHE = {}
PLATE_CACHE = {}


def add_glow(canvas, cx, cy, r, colour, strength, squash=1.0):
    if r < 2:
        return
    key = (r, round(squash, 2))
    k = _GLOW_CACHE.get(key)
    if k is None:
        yy, xx = np.mgrid[-r:r + 1, -r:r + 1].astype(np.float32)
        d2 = (xx * xx + (yy * yy) / (squash * squash)) / float(r * r)
        k = np.clip(1.0 - d2, 0, 1) ** 2.2
        _GLOW_CACHE[key] = k
    y0, y1 = max(0, cy - r), min(H, cy + r + 1)
    x0, x1 = max(0, cx - r), min(W, cx + r + 1)
    if y1 <= y0 or x1 <= x0:
        return
    ky0, kx0 = y0 - (cy - r), x0 - (cx - r)
    patch = k[ky0:ky0 + (y1 - y0), kx0:kx0 + (x1 - x0)]
    canvas[y0:y1, x0:x1] += patch[..., None] * np.array(colour, dtype=np.float32) * strength


def caption(canvas, lines):
    """Text is static inside a shot: draw the overlay once, composite it every frame."""
    if not lines:
        return
    key = tuple(lines)
    ov = _CAP_CACHE.get(key)
    if ov is None:
        img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        d = ImageDraw.Draw(img)
        global _FONT
        size = 30
        if _FONT is None:
            try:
                _FONT = ImageFont.truetype(FONT, size)
            except Exception:
                _FONT = ImageFont.load_default()
        total = len(lines) * int(size * 1.16)
        y = H - total - 26
        for line in lines:
            bbox = d.textbbox((0, 0), line, font=_FONT)
            x = (W - (bbox[2] - bbox[0])) // 2
            for dx, dy in ((-2, 0), (2, 0), (0, -2), (0, 2), (-1, 1), (1, -1)):
                d.text((x + dx, y + dy), line, font=_FONT, fill=(4, 5, 8, 235))
            d.text((x, y), line, font=_FONT, fill=(242, 232, 214, 255))
            y += int(size * 1.16)
        ov = np.asarray(img, dtype=np.float32) / 255.0
        _CAP_CACHE[key] = ov
    a = ov[..., 3:4]
    canvas[:] = canvas * (1 - a) + ov[..., :3] * a


def render_frame(shot_idx, f_global):
    sh = SHOTS[shot_idx]
    t0, t1 = sh["t"]
    n = max(1, int(round((t1 - t0) * FPS)))
    prog = min(1.0, max(0.0, (f_global - int(t0 * FPS)) / max(1, n)))

    if sh["plate"] not in PLATE_CACHE:
        PLATE_CACHE[sh["plate"]] = Image.open(os.path.join(PLATES, sh["plate"])).convert("RGB")
    plate = PLATE_CACHE[sh["plate"]]
    pw, ph = plate.size
    # camera: slow push-in, never locked off
    zoom = 1.0 + 0.075 * ease_io(prog)
    cw, chh = int(pw / zoom), int(ph / zoom)
    dx = sh["drift"] * 0.55
    cx = int((pw - cw) / 2 + dx * (pw - cw) * (prog - 0.5))
    cy = int((ph - chh) / 2)
    crop = plate.crop((cx, cy, cx + cw, cy + chh)).resize((W, H), Image.BICUBIC)
    canvas = np.asarray(crop, dtype=np.float32) / 255.0
    canvas *= 0.94  # a touch down, so the lantern is the brightest thing

    for act in sh["actors"]:
        place_actor(canvas, act, prog, f_global)

    canvas = canvas + canvas * canvas * 0.06          # gentle lift in the mids
    caption(canvas, sh.get("cap"))
    return (np.clip(canvas, 0, 1) * 255).astype(np.uint8)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--still", type=int, help="global frame number to write as a still")
    ap.add_argument("--all", action="store_true")
    a = ap.parse_args()

    os.makedirs(os.path.join(HERE, "frames"), exist_ok=True)
    total = int(SHOTS[-1]["t"][1] * FPS)

    if a.still is not None:
        f = a.still
        idx = next(i for i, s in enumerate(SHOTS) if int(s["t"][0] * FPS) <= f < int(s["t"][1] * FPS))
        img = render_frame(idx, f)
        out = os.path.join(HERE, f"still_{f:04d}.png")
        Image.fromarray(img).save(out)
        print("wrote", out, "shot", idx + 1)
        return

    if not a.all:
        print("nothing to do: pass --still N or --all")
        return

    done = 0
    for f in range(total):
        out = os.path.join(HERE, "frames", f"f_{f:04d}.png")
        if os.path.exists(out):
            done += 1
            continue
        idx = next(i for i, s in enumerate(SHOTS) if int(s["t"][0] * FPS) <= f < int(s["t"][1] * FPS))
        Image.fromarray(render_frame(idx, f)).save(out, compress_level=1)
        if f % 120 == 0:
            print(f"  {f}/{total}", flush=True)
    print("rendered", total, "frames")


if __name__ == "__main__":
    main()
