#!/usr/bin/env python3
"""Method C post graphics for THE LAST SEAT E2 (per SCRIPT.md — the only
graphic this episode): the "~ WuBu ~" corner bug (every frame). No
question card in E2 (script: post card "if used" — not used; the debt
declaration is the hanger). PIL-drawn; no generated text anywhere."""
from PIL import Image, ImageDraw, ImageFont

W, H = 1280, 720
SERIF_I = "/usr/share/fonts/truetype/noto/NotoSerif-SemiBoldItalic.ttf"
BONE = (237, 230, 218)

bug = Image.new("RGBA", (W, H), (0, 0, 0, 0))
d = ImageDraw.Draw(bug)
f = ImageFont.truetype(SERIF_I, 25)
txt = "~ WuBu ~"
tw = d.textlength(txt, font=f)
d.text((W - tw - 26, H - 44), txt, font=f, fill=BONE + (215,))
bug.save("work/gfx/bug.png")
print("bug ok")
