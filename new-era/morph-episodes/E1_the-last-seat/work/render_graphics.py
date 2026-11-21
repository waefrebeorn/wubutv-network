#!/usr/bin/env python3
"""Method C post graphics for THE LAST SEAT E1 (per SCRIPT.md — the only
graphics this episode): the "~ WuBu ~" corner bug (every frame) and the
QUESTION card at the U6 freeze. PIL-drawn; no generated text anywhere."""
from PIL import Image, ImageDraw, ImageFont

W, H = 1280, 720
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_I = "/usr/share/fonts/truetype/noto/NotoSerif-SemiBoldItalic.ttf"
BONE = (237, 230, 218)
GOLD = (201, 162, 75)

# --- corner bug, bottom-right, small (wordmark law: post-only in this show)
bug = Image.new("RGBA", (W, H), (0, 0, 0, 0))
d = ImageDraw.Draw(bug)
f = ImageFont.truetype(SERIF_I, 25)
txt = "~ WuBu ~"
tw = d.textlength(txt, font=f)
d.text((W - tw - 26, H - 44), txt, font=f, fill=BONE + (215,))
bug.save("work/gfx/bug.png")
print("bug ok")

# --- the QUESTION card (lands on the U6 freeze, GAP 3's carrier)
card = Image.new("RGBA", (W, H), (0, 0, 0, 0))
d = ImageDraw.Draw(card)
# soft dark backing for legibility over the frozen frame
d.rounded_rectangle([240, 268, 1040, 452], radius=18, fill=(0, 0, 0, 110))
f1 = ImageFont.truetype(SERIF, 44)
lines = ["WHO IS THE WOMAN", "IN SEAT ONE?"]
y = 296
for ln in lines:
    tw = d.textlength(ln, font=f1)
    d.text(((W - tw) / 2, y), ln, font=f1, fill=BONE + (255,))
    y += 58
# thin gold rule under the text — the lamp's colour, the show's one device
d.line([490, y + 8, 790, y + 8], fill=GOLD + (255,), width=3)
card.save("work/gfx/question_card.png")
print("question card ok")
