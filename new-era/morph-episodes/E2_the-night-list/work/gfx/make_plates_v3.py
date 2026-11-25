#!/usr/bin/env python3
"""THE NIGHT LIST E2 — board plates, REPAIR ROUND v3.

Rebuilt on the revised script's roster so the pictured count
and the spoken count are the SAME count (DECISION_LOG R3-4):
eleven rows — nine lodgers + PETER in the tenth row + KEEPER
at the foot. States follow the spoken chain exactly:
  open   : 11 names standing (PETER row 10, KEEPER foot)
  struck : KEEPER struck through in vermilion (U1) -> 10 standing
  grant  : PETER struck fresh + ELIAS written fresh in his
           place (U5) -> still 10 standing
  held   : the grant state, strikes settled (U6 freeze)
  final  : held + KEEPER written fresh at the very foot (U6)
           -> 11 standing, 10 beds
Geometry reuses make_plates_E2.py's board (E1 board look).
"""
from PIL import Image, ImageDraw, ImageFont
import random

EP = "/home/hatch/workspace/wubutv-network/new-era/morph-episodes/E2_the-night-list"
PANELS = EP + "/panels"
SERIF = "/usr/share/fonts/truetype/noto/NotoSerif-Regular.ttf"
SERIF_B = "/usr/share/fonts/truetype/noto/NotoSerif-Bold.ttf"
CHALK = (238, 232, 214)
VERMILION = (226, 62, 32)

ROSTER = ["ANNA", "MOSS", "JUNE", "COLE", "RUTH", "SOL",
          "LAURA", "EMMETT", "TESS", "PETER", "KEEPER"]
IDX_PETER = 9
IDX_KEEPER = 10


def chalk_text(d, xy, s, size=44, jitter=5, fill=CHALK, bold=True, seed=0):
    rnd = random.Random(seed)
    f = ImageFont.truetype(SERIF_B if bold else SERIF, size)
    x, y = xy
    for ch in s:
        d.text((x + rnd.randint(-1, 1), y + rnd.randint(-jitter, jitter)),
               ch, font=f, fill=fill + (235,))
        x += d.textlength(ch, font=f) + 3


def strike(d, x0, x1, y, seed=0, w=7, alpha=235):
    rnd = random.Random(seed)
    for k in range(2):
        yy = y + rnd.randint(-3, 3) + k * 5
        pts = [(x, yy + rnd.randint(-4, 4)) for x in range(x0, x1, 26)]
        d.line(pts, fill=VERMILION + (alpha,), width=w)


def draw_board(path, state):
    """state in {open, struck, grant, held, final}"""
    img = Image.open(PANELS + "/PNL-PROP-board-blank.png").convert("RGBA")
    ov = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    x0, y0, dy = 470, 96, 62
    for i, name in enumerate(ROSTER):
        y = y0 + i * dy
        if state in ("grant", "held", "final") and i == IDX_PETER:
            # PETER chalked, struck through fresh; ELIAS written
            # fresh in his place, slightly high in the slot.
            chalk_text(d, (x0, y), "PETER", seed=100 + i)
            w = d.textlength("PETER", font=ImageFont.truetype(SERIF_B, 44))
            fresh = state == "grant"
            strike(d, x0 - 12, int(x0 + w + 14), y + 29, seed=55,
                   w=8 if fresh else 6, alpha=245 if fresh else 215)
            chalk_text(d, (x0 + 4, y - 31), "ELIAS", size=40, seed=300 + i)
            continue
        chalk_text(d, (x0, y), name, seed=100 + i)
        if i == IDX_KEEPER and state in ("struck", "grant", "held", "final"):
            w = d.textlength(name, font=ImageFont.truetype(SERIF_B, 44))
            settled = state in ("held", "final")
            strike(d, x0 - 12, int(x0 + w + 14), y + 24, seed=7,
                   w=6 if settled else 8, alpha=215 if settled else 245)
    if state == "final":
        foot_y = y0 + IDX_KEEPER * dy
        chalk_text(d, (x0, foot_y + 118), "KEEPER", seed=999)
    img.alpha_composite(ov)
    img.convert("RGB").save(path, quality=92)
    print("plate:", path, state)


if __name__ == "__main__":
    out = EP + "/work/gfx"
    for st in ("open", "struck", "grant", "held", "final"):
        draw_board(f"{out}/board_v3_{st}.png", st)
