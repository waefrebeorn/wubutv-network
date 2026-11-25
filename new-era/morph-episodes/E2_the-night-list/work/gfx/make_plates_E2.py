#!/usr/bin/env python3
"""THE NIGHT LIST E2 — deterministic writing plates (PIL).
All handwriting is drawn here, never generated. Adapted from E1's
make_plates.py; board-row detection reused. E2 states:
  open   — 11 names, KEEPER at the foot, unstruck
  struck — KEEPER struck through in vermilion (U1 tail / U2-U4)
  held   — ELIAS fresh in the foot slot over the struck ghost (U5)
  final  — held + KEEPER fresh, squeezed at the very foot (U6 freeze)
Plus: PEAK-U1 (strike mid-landing on KEEPER), the floor-rule house
sign, the HELD tag, and the ANCH-U1 board-roster fix.
"""
import random
import numpy as np
from PIL import Image, ImageDraw, ImageFont

EP = "/home/hatch/workspace/wubutv-network/new-era/morph-episodes/E2_the-night-list"
SERIF_B = "/usr/share/fonts/truetype/noto/NotoSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/noto/NotoSerif-Regular.ttf"
BONE = (233, 226, 206)
BONE_DIM = (198, 190, 168)
FRESH = (245, 240, 224)
VERMILION = (203, 52, 30)
INK = (38, 34, 30)

NAMES = ["ANNA", "MOSS", "JUNE", "COLE", "RUTH", "SOL", "LAURA",
         "EMMETT", "TESS", "HAROLD", "KEEPER"]
KEEPER_I = NAMES.index("KEEPER")

board = Image.open(f"{EP}/panels/PNL-PROP-board-blank.png").convert("RGB")
W, H = board.size

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
pitch = int(np.median(np.diff(lines)))
bands = []
prev = lines[0] - pitch
for ln in lines:
    bands.append((prev, ln)); prev = ln
print("bands:", bands, "pitch:", pitch)


def chalk_text(img, xy, text, size, color=BONE, seed=7, alpha=235, font_path=SERIF_B):
    rng = random.Random(seed)
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    font = ImageFont.truetype(font_path, size)
    x, y = xy
    for ch in text:
        d.text((x, y + rng.randint(-2, 2)), ch, font=font, fill=color + (alpha,))
        x += d.textlength(ch, font=font) + rng.randint(0, 3)
    a = np.asarray(layer)[:, :, 3].astype(np.int16)
    noise = np.random.RandomState(seed).rand(img.size[1], img.size[0])
    a[noise < 0.16] = (a[noise < 0.16] * 0.35).astype(np.int16)
    layer.putalpha(Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)))
    img.alpha_composite(layer)
    return x


def strike(img, band, frac=1.0, seed=3, dust=False):
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
    if dust:
        for _ in range(260):
            dx = x1 + rng.randint(-6, 46); dy = yc + rng.randint(-26, 26)
            r = rng.randint(1, 3)
            d.ellipse([dx, dy, dx + r, dy + r], fill=(226, 90, 60, rng.randint(60, 170)))
    a = np.asarray(layer)[:, :, 3].astype(np.int16)
    noise = np.random.RandomState(seed).rand(img.size[1], img.size[0])
    a[noise < 0.12] = (a[noise < 0.12] * 0.4).astype(np.int16)
    layer.putalpha(Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)))
    img.alpha_composite(layer)


def draw_names(img, skip_keeper=False, fresh_foot=None):
    size = int(pitch * 0.52)
    for i, name in enumerate(NAMES):
        if skip_keeper and i == KEEPER_I:
            continue
        y0, y1 = bands[i]
        col = BONE if i % 2 == 0 else BONE_DIM
        chalk_text(img, (int(W * 0.06), y0 + (pitch - size) // 2 - 4),
                   name, size, color=col, seed=11 + i, alpha=225)
    if fresh_foot:
        y0, y1 = bands[KEEPER_I]
        chalk_text(img, (int(W * 0.06), y0 + (pitch - size) // 2 - 4),
                   fresh_foot, size, color=FRESH, seed=41, alpha=250)


# --- open board (U1 reference / strike target state)
img = board.convert("RGBA")
draw_names(img)
img.convert("RGB").save(f"{EP}/work/gfx/board_E2_open.png")

# --- struck board (U2-U4 reference)
img = board.convert("RGBA")
draw_names(img)
strike(img, bands[KEEPER_I], frac=1.0)
img.convert("RGB").save(f"{EP}/work/gfx/board_E2_struck.png")

# --- held board (U5 tail / U6 reference): ELIAS fresh in the struck slot.
# The old strike survives only as a remnant TRAILING the new name — it
# never crosses ELIAS's letters (F-2: his name stands unstruck).
img = board.convert("RGBA")
draw_names(img, skip_keeper=True)
size = int(pitch * 0.52)
y0, y1 = bands[KEEPER_I]
yc = (y0 + y1) // 2
ex = chalk_text(img, (int(W * 0.06), y0 + (pitch - size) // 2 - 4),
                "ELIAS", size, color=FRESH, seed=41, alpha=250)
layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
d = ImageDraw.Draw(layer)
rng = random.Random(9)
for t in range(5):
    yy = yc + rng.randint(-3, 3)
    d.line([(ex + 14, yy), (int(W * 0.30), yy + rng.randint(-2, 2))],
           fill=VERMILION + (150,), width=4)
img.alpha_composite(layer)
img.convert("RGB").save(f"{EP}/work/gfx/board_E2_held.png")

# --- final board (U6 freeze): held + KEEPER squeezed fresh at the very foot
img = Image.open(f"{EP}/work/gfx/board_E2_held.png").convert("RGBA")
small = int(pitch * 0.40)
fy = lines[-1] + int(pitch * 0.18)
chalk_text(img, (int(W * 0.06), fy), "KEEPER", small, color=FRESH, seed=43, alpha=245)
img.convert("RGB").save(f"{EP}/work/gfx/board_E2_final.png")

# --- PEAK-U1: tight 16:9 window on the KEEPER row, strike MID-LANDING (65%)
img = board.convert("RGBA")
draw_names(img)
strike(img, bands[KEEPER_I], frac=0.65, dust=True)
kc = (bands[KEEPER_I][0] + bands[KEEPER_I][1]) // 2
cw = 1500; ch = int(cw * 9 / 16)
x0 = int(W * 0.02); y0 = max(0, min(H - ch, kc - ch // 2))
peak1 = img.convert("RGB").crop((x0, y0, x0 + cw, y0 + ch)).resize((2048, 1152))
peak1.save(f"{EP}/panels/PNL-PEAK-U1.png")

# --- floor-rule house sign (painted board, post-composited text + pictogram)
sign = Image.new("RGB", (1024, 640), (52, 42, 34))
d = ImageDraw.Draw(sign, "RGBA")
for x in range(0, 1024, 128):  # plank seams
    d.line([(x, 0), (x, 640)], fill=(30, 24, 19), width=4)
d.rectangle([14, 14, 1010, 626], outline=(190, 178, 150), width=5)
# pictogram: a figure lying dry on a floor line under a stair (bone paint)
d.line([(150, 470), (874, 470)], fill=BONE, width=7)                    # floor
for i in range(5):                                                      # stair
    sx = 560 + i * 62
    d.line([(sx, 470 - i * 44), (sx + 62, 470 - i * 44)], fill=BONE, width=6)
    d.line([(sx + 62, 470 - i * 44), (sx + 62, 470 - (i + 1) * 44)], fill=BONE, width=6)
d.ellipse([215, 408, 275, 468], outline=BONE, width=7)                  # head
d.line([(275, 448), (470, 448)], fill=BONE, width=9)                     # body
d.line([(470, 448), (520, 470)], fill=BONE, width=7)                     # legs
f1 = ImageFont.truetype(SERIF_B, 54)
f2 = ImageFont.truetype(SERIF_B, 44)
def ctext(y, text, font, fill):
    d.text((512 - d.textlength(text, font=font) / 2, y), text, font=font, fill=fill)
ctext(52, "STAYING AFTER REFUSAL", f1, BONE)
ctext(122, "EARNS DRY FLOOR", f1, BONE)
ctext(528, "NO BED · NO NAME", f2, (226, 90, 60))
sign.save(f"{EP}/work/gfx/sign_floor_rule.png")

# --- HELD tag (bone card, ink letters)
tag = Image.new("RGB", (512, 320), (226, 218, 196))
d = ImageDraw.Draw(tag)
d.rectangle([10, 10, 502, 310], outline=INK, width=5)
d.ellipse([226, 26, 286, 86], outline=INK, width=6)
ft = ImageFont.truetype(SERIF_B, 120)
d.text((256 - d.textlength("HELD", font=ft) / 2, 130), "HELD", font=ft, fill=INK)
tag.save(f"{EP}/work/gfx/held_tag.png")

# --- ANCH-U1 board fix: mute the wrong generator roster, warp the true one on
anch = Image.open(f"{EP}/panels/PNL-ANCH-U1.png").convert("RGB")
aw, ah = anch.size
# board quad (TL, TR, BR, BL) estimated from the panel
quad = [(58, 6), (462, 82), (455, 898), (46, 912)]
mask = Image.new("L", (aw, ah), 0)
md = ImageDraw.Draw(mask)
md.polygon(quad, fill=255)
dark = Image.new("RGB", (aw, ah), (24, 28, 30))
anch = Image.composite(dark, anch, mask.point(lambda v: int(v * 0.88)))
# render roster strip and perspective-warp it into the quad
strip_w, strip_h = 800, 1500
strip_img = Image.new("RGBA", (strip_w, strip_h), (0, 0, 0, 0))
sd = ImageDraw.Draw(strip_img)
fn = ImageFont.truetype(SERIF_B, 74)
for i, name in enumerate(NAMES):
    sd.text((46, 30 + i * 128), name, font=fn,
            fill=(BONE if i % 2 == 0 else BONE_DIM) + (215,))
# strike across KEEPER (bottom row) — the strike has landed by the wide
ky = 30 + KEEPER_I * 128 + 40
for t in range(6):
    sd.line([(40, ky + t * 2 - 4), (430, ky - t)], fill=VERMILION + (220,), width=6)

def find_coeffs(target, source):
    import numpy as np
    matrix = []
    for p1, p2 in zip(source, target):
        matrix.append([p1[0], p1[1], 1, 0, 0, 0, -p2[0] * p1[0], -p2[0] * p1[1]])
        matrix.append([0, 0, 0, p1[0], p1[1], 1, -p2[1] * p1[0], -p2[1] * p1[1]])
    A = np.matrix(matrix, dtype=float)
    B = np.array(target).reshape(8)
    res = np.linalg.solve(A, B)
    return np.array(res).reshape(8)

src = [(0, 0), (strip_w, 0), (strip_w, strip_h), (0, strip_h)]
coeffs = find_coeffs(quad, src)
warped = strip_img.transform((aw, ah), Image.PERSPECTIVE, coeffs, Image.BICUBIC)
anch.paste(warped, (0, 0), warped)
anch.save(f"{EP}/panels/PNL-ANCH-U1.png")
print("E2 plates done")
