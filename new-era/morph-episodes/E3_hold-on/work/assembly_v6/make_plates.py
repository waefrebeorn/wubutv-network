#!/usr/bin/env python3
"""PIL chalk plates for HOLD ON E3 v6 assembly (BRIEF plate spec).
Docket line on U1-U5; U6 gets docket-only (stage 1) then the struck set
(stage 2). White chalk, docket hand (Liberation Serif caps + chalk erosion).
Also renders the house corner bug (~ WuBu ~, gold serif, bottom-right).
"""
import random

from PIL import Image, ImageDraw, ImageFilter, ImageFont

random.seed(20261119)
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SERIF_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
W, H = 1280, 720
CHALK = (238, 238, 232)

DOCKET = "SHE HELD MY TIN. MY COINS ARE GONE."
TRUE_LINE = "HANDS OPEN. COINS LOOSE."
TOMORROW = "TOMORROW: THE NAME HE WON'T WRITE."


def chalk_text(lines, origin, size, leading, strike_first=False):
    """Render lines of chalk text on a transparent W x H image."""
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    font = ImageFont.truetype(SERIF, size)
    x0, y0 = origin
    for i, line in enumerate(lines):
        layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        d = ImageDraw.Draw(layer)
        y = y0 + i * leading
        # per-letter placement with slight jitter for a hand-chalked feel
        x = x0
        for ch in line:
            d.text((x, y + random.uniform(-1.2, 1.2)), ch,
                   font=font, fill=CHALK + (235,))
            x += d.textlength(ch, font=font)
        if strike_first and i == 0:
            # one rough chalk stroke through the line
            w_line = x - x0
            yc = y + size * 0.52
            pts = []
            for t in range(0, int(w_line) + 1, 14):
                pts.append((x0 - 6 + t, yc + random.uniform(-2.5, 2.5)))
            d.line(pts, fill=CHALK + (215,), width=max(3, size // 7))
        layer = layer.rotate(random.uniform(-0.35, 0.35),
                             center=(x0 + 200, y + size / 2), resample=Image.BICUBIC)
        img.alpha_composite(layer)
    # chalk erosion: speckle the alpha, slight blur
    px = img.load()
    for _ in range(26000):
        x = random.randrange(W)
        y = random.randrange(H)
        r, g, b, a = px[x, y]
        if a > 0:
            px[x, y] = (r, g, b, max(0, a - random.randrange(60, 200)))
    return img.filter(ImageFilter.GaussianBlur(0.55))


def main():
    out = "/home/hatch/workspace/wubutv-network/new-era/morph-episodes/E3_hold-on/work/assembly_v6"
    plates = {
        "plate_U1.png": chalk_text([DOCKET], (350, 30), 30, 40),
        "plate_U2.png": chalk_text([DOCKET], (185, 130), 26, 36),
        "plate_U3.png": chalk_text([DOCKET], (330, 24), 30, 40),
        "plate_U4.png": chalk_text([DOCKET], (240, 30), 30, 40),
        "plate_U5.png": chalk_text([DOCKET], (24, 20), 26, 36),
        "plate_U6a.png": chalk_text([DOCKET], (56, 14), 22, 32),
        "plate_U6b.png": chalk_text([DOCKET, TRUE_LINE, TOMORROW],
                                    (560, 14), 22, 32, strike_first=True),
    }
    for name, im in plates.items():
        im.save(f"{out}/{name}")
        print("wrote", name)
    # corner bug: gold serif ~ WuBu ~, bottom-right, house style
    bug = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(bug)
    font = ImageFont.truetype(SERIF_BOLD, 30)
    txt = "~ WuBu ~"
    tw = d.textlength(txt, font=font)
    d.text((W - tw - 26, H - 52), txt, font=font, fill=(233, 178, 76, 242))
    bug.save(f"{out}/bug.png")
    print("wrote bug.png")


if __name__ == "__main__":
    main()
