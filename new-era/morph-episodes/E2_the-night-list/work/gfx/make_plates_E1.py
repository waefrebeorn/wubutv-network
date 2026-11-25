#!/usr/bin/env python3
"""THE NIGHT LIST E1 — deterministic writing plates (PIL).
All handwriting for the episode is drawn here, never generated.
Board rows are detected from the blank board panel's chalk lines.
"""
import random
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

EP = "/home/hatch/workspace/wubutv-network/new-era/morph-episodes/E1_the-night-list"
SERIF_B = "/usr/share/fonts/truetype/noto/NotoSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/noto/NotoSerif-Regular.ttf"
BONE = (233, 226, 206)
BONE_DIM = (198, 190, 168)
VERMILION = (203, 52, 30)
INK = (38, 34, 30)

NAMES = ["ANNA", "MOSS", "JUNE", "COLE", "RUTH", "SOL", "LAURA",
         "EMMETT", "TESS", "HAROLD", "KEEPER"]
SOL_I = NAMES.index("SOL")

board = Image.open(f"{EP}/panels/PNL-PROP-board-blank.png").convert("RGB")
W, H = board.size

# --- detect chalk row lines: bright horizontal runs in the left third
g = np.asarray(board.convert("L"), dtype=np.float32)
strip = g[:, int(W * 0.3):int(W * 0.7)].mean(axis=1)
lines = []
in_line = False
for y in range(H):
    if strip[y] > 95 and not in_line:
        start = y; in_line = True
    elif strip[y] <= 95 and in_line:
        lines.append((start + y) // 2); in_line = False
print("detected lines:", lines)
assert len(lines) >= 11, f"need >=11 lines, got {len(lines)}"
lines = lines[:11]
# row band i sits ABOVE line i for i in 0..9? Names sit between lines:
# bands: (lines[i-1], lines[i]) with a virtual top at lines[0]-pitch
pitch = int(np.median(np.diff(lines)))
bands = []
prev = lines[0] - pitch
for ln in lines:
    bands.append((prev, ln)); prev = ln
print("bands:", bands)


def chalk_text(img, xy, text, size, color=BONE, seed=7, alpha=235, font_path=SERIF_B):
    """Draw chalk-like text: per-letter jitter + erosion noise."""
    rng = random.Random(seed)
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    font = ImageFont.truetype(font_path, size)
    x, y = xy
    for ch in text:
        d.text((x, y + rng.randint(-2, 2)), ch, font=font,
               fill=color + (alpha,))
        x += d.textlength(ch, font=font) + rng.randint(0, 3)
    # chalk erosion: knock out sparse noise
    a = np.asarray(layer)[:, :, 3].astype(np.int16)
    noise = np.random.RandomState(seed).rand(H, W)
    a[noise < 0.16] = (a[noise < 0.16] * 0.35).astype(np.int16)
    layer.putalpha(Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)))
    img.alpha_composite(layer)
    return x


def strike(img, band, frac=1.0, seed=3, dust=False):
    """Vermilion strike stroke across the band's name zone."""
    y0, y1 = band
    yc = (y0 + y1) // 2
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    x0 = int(W * 0.055)
    x1 = x0 + int((W * 0.30 - x0) * frac)
    rng = random.Random(seed)
    for t in range(7):
        yy = yc + rng.randint(-4, 4)
        d.line([(x0, yy + rng.randint(-2, 2)), (x1, yy + rng.randint(-3, 3))],
               fill=VERMILION + (215,), width=5)
    if dust:  # chalk-dust burst at the stroke tip
        for _ in range(260):
            dx = x1 + rng.randint(-6, 46); dy = yc + rng.randint(-26, 26)
            r = rng.randint(1, 3)
            d.ellipse([dx, dy, dx + r, dy + r], fill=(226, 90, 60, rng.randint(60, 170)))
    a = np.asarray(layer)[:, :, 3].astype(np.int16)
    noise = np.random.RandomState(seed).rand(H, W)
    a[noise < 0.12] = (a[noise < 0.12] * 0.4).astype(np.int16)
    layer.putalpha(Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)))
    img.alpha_composite(layer)


def draw_board(struck: bool, fresh_sol: bool = False):
    img = board.convert("RGBA")
    size = int(pitch * 0.52)
    for i, name in enumerate(NAMES):
        y0, y1 = bands[i]
        col = BONE if i % 2 == 0 else BONE_DIM
        alpha = 225
        if i == SOL_I and fresh_sol:
            col, alpha = (245, 240, 224), 250
        chalk_text(img, (int(W * 0.06), y0 + (pitch - size) // 2 - 4),
                   name, size, color=col, seed=11 + i, alpha=alpha)
    if struck:
        strike(img, bands[SOL_I], frac=1.0)
    return img


# State A: SOL struck (U1 tail state / U2 / U5 start)
stateA = draw_board(struck=True)
stateA.convert("RGB").save(f"{EP}/work/gfx/board_stateA.png")

# State B: SOL restored, fresh bright (U6)
stateB = draw_board(struck=False, fresh_sol=True)
stateB.convert("RGB").save(f"{EP}/work/gfx/board_stateB.png")

# PEAK-U1: tight 16:9 window on the SOL row, strike MID-LANDING (65%)
img = board.convert("RGBA")
size = int(pitch * 0.52)
for i, name in enumerate(NAMES):
    y0, y1 = bands[i]
    col = BONE if i % 2 == 0 else BONE_DIM
    chalk_text(img, (int(W * 0.06), y0 + (pitch - size) // 2 - 4),
               name, size, color=col, seed=11 + i, alpha=225)
strike(img, bands[SOL_I], frac=0.65, dust=True)
sol_c = (bands[SOL_I][0] + bands[SOL_I][1]) // 2
cw = 1500; ch = int(cw * 9 / 16)
x0 = int(W * 0.02); y0 = max(0, sol_c - ch // 2)
peak1 = img.convert("RGB").crop((x0, y0, x0 + cw, y0 + ch)).resize((2048, 1152))
peak1.save(f"{EP}/panels/PNL-PEAK-U1.png")
print("plates done")
