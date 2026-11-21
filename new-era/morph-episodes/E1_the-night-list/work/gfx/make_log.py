#!/usr/bin/env python3
"""Log day-page plate: NOON / NIGHT columns warped onto the log's right page.
The noon entry is the episode's seen reveal — drawn here, never generated."""
import numpy as np
from PIL import Image, ImageDraw, ImageFont

EP = "/home/hatch/workspace/wubutv-network/new-era/morph-episodes/E1_the-night-list"
SERIF_B = "/usr/share/fonts/truetype/noto/NotoSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/noto/NotoSerif-Regular.ttf"
INK = (43, 38, 33, 235)
INK_SOFT = (60, 54, 47, 200)

log = Image.open(f"{EP}/panels/PNL-PROP-log-blank.png").convert("RGBA")
W, H = log.size

# flat page canvas (portrait)
PW, PH = 760, 980
page = Image.new("RGBA", (PW, PH), (0, 0, 0, 0))
d = ImageDraw.Draw(page)
fh = ImageFont.truetype(SERIF_B, 44)
fe = ImageFont.truetype(SERIF, 40)
fe_big = ImageFont.truetype(SERIF_B, 56)
mid = PW // 2
d.line([(mid, 30), (mid, PH - 40)], fill=(90, 84, 74, 160), width=3)
d.text((60, 36), "NOON", font=fh, fill=INK)
d.text((mid + 55, 36), "NIGHT", font=fh, fill=INK)
d.line([(30, 108), (PW - 30, 108)], fill=(90, 84, 74, 160), width=3)
# the noon entry — the reveal, drawn large enough to read at phone size
d.text((52, 150), "12:00", font=fe_big, fill=INK)
d.text((52, 235), "SOL struck", font=fe, fill=INK)
d.text((52, 295), "— U.", font=fe, fill=INK)
# two faint ruled rows lower down, empty (page breathes; night side stays blank)
for yy in (430, 520, 610):
    d.line([(40, yy), (PW - 40, yy)], fill=(120, 112, 100, 70), width=2)

# perspective-warp the flat page onto the log's right page quad
quad = [(985, 252), (1458, 205), (1618, 848), (1072, 908)]  # TL TR BR BL in log px
src = [(0, 0), (PW, 0), (PW, PH), (0, PH)]


def coeffs(dst, src):
    m = []
    for (x, y), (u, v) in zip(dst, src):
        m.append([x, y, 1, 0, 0, 0, -u * x, -u * y])
        m.append([0, 0, 0, x, y, 1, -v * x, -v * y])
    A = np.matrix(m, dtype=float)
    B = np.array([c for p in src for c in p], dtype=float)
    return np.array(np.linalg.solve(A, B)).reshape(8)


warped = page.transform((W, H), Image.PERSPECTIVE,
                        coeffs(quad, src), Image.BICUBIC)
# multiply-blend feel: darken page pixels where ink sits
log.alpha_composite(warped)
log.convert("RGB").save(f"{EP}/work/gfx/log_page.png")
print("log plate done")
