#!/usr/bin/env python3
"""PIL chalk plates for HOLD ON E3 PART 2 assembly (BRIEF_PART2 plate spec).

Wall stack on U1-U5 and U6 stage 1:
  PEACH (small, fresh, higher up) — H-1 paid in the background
  MARTA — OWES THE RENT (the docket line, fresh docket hand)
  weathered Part 1 residue below: the struck
  SHE HELD MY TIN. MY COINS ARE GONE. + HANDS OPEN. COINS LOOSE.
U6 stage 2: the MARTA line struck through + MARTA PAID. beneath it.
U6 freeze: stage 2 + SHOULD LAURA WRITE THE WATCHER'S NAME?
across the lower wall field.
White chalk, docket hand (Liberation Serif + chalk erosion).
Also renders the house corner bug (~ WuBu ~, gold serif, bottom-right).

Plate origins are per-unit and get tuned at assembly against each
accepted take's wall field (placement-check frames first, as in
Part 1). The defaults below mirror Part 1's spread.
"""
import random

from PIL import Image, ImageDraw, ImageFilter, ImageFont

random.seed(20261123)
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SERIF_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
W, H = 1280, 720
CHALK = (238, 238, 232)
WEATHERED = (196, 196, 188)

DOCKET = "MARTA — OWES THE RENT"
PAID = "MARTA PAID."
PEACH = "PEACH"
P1_DOCKET = "SHE HELD MY TIN. MY COINS ARE GONE."
P1_TRUE = "HANDS OPEN. COINS LOOSE."
QUESTION = "SHOULD LAURA WRITE THE WATCHER'S NAME?"


def chalk_line(line, origin, size, color=CHALK, alpha=235, strike=False):
    """One hand-chalked line on a transparent W x H layer, eroded."""
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    font = ImageFont.truetype(SERIF, size)
    x0, y0 = origin
    x = x0
    for ch in line:
        d.text((x, y0 + random.uniform(-1.2, 1.2)), ch,
               font=font, fill=color + (alpha,))
        x += d.textlength(ch, font=font)
    if strike:
        w_line = x - x0
        yc = y0 + size * 0.52
        pts = []
        for t in range(0, int(w_line) + 1, 14):
            pts.append((x0 - 6 + t, yc + random.uniform(-2.5, 2.5)))
        d.line(pts, fill=color + (max(120, alpha - 20),),
               width=max(3, size // 7))
    layer = layer.rotate(random.uniform(-0.35, 0.35),
                         center=(x0 + 200, y0 + size / 2),
                         resample=Image.BICUBIC)
    return layer


def erode(img, speckles):
    px = img.load()
    for _ in range(speckles):
        x = random.randrange(W)
        y = random.randrange(H)
        r, g, b, a = px[x, y]
        if a > 0:
            px[x, y] = (r, g, b, max(0, a - random.randrange(60, 200)))
    return img.filter(ImageFilter.GaussianBlur(0.55))


def stack(origin, size, stage=1, question=False):
    """The Part 2 wall stack at a given origin/size. stage 2 = struck
    docket + MARTA PAID. beneath. question adds the freeze line."""
    x0, y0 = origin
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    # PEACH: small and fresh, higher up
    img.alpha_composite(chalk_line(PEACH, (x0 + int(size * 0.4), y0),
                                   max(16, int(size * 0.62))))
    dy = int(size * 1.55)
    # the docket line (struck at stage 2)
    img.alpha_composite(chalk_line(DOCKET, (x0, y0 + dy), size,
                                   strike=(stage == 2)))
    dy += int(size * 1.35)
    if stage == 2:
        img.alpha_composite(chalk_line(PAID, (x0, y0 + dy), size))
        dy += int(size * 1.35)
    # weathered Part 1 residue: struck docket + true line, dimmer
    img.alpha_composite(chalk_line(P1_DOCKET, (x0, y0 + dy),
                                   max(15, int(size * 0.58)),
                                   color=WEATHERED, alpha=120,
                                   strike=True))
    dy += int(size * 0.95)
    img.alpha_composite(chalk_line(P1_TRUE, (x0, y0 + dy),
                                   max(15, int(size * 0.58)),
                                   color=WEATHERED, alpha=120))
    if question:
        qsize = max(18, int(size * 0.8))
        qw = ImageDraw.Draw(Image.new("RGBA", (W, H))).textlength(
            QUESTION, font=ImageFont.truetype(SERIF, qsize))
        img.alpha_composite(chalk_line(
            QUESTION, (int((W - qw) / 2), H - int(size * 3.4)), qsize))
    return erode(img, 26000)


def main():
    out = "/home/hatch/workspace/wubutv-network/new-era/morph-episodes/E3_hold-on/work/assembly_part2"
    plates = {
        "plate_U1.png": stack((350, 26), 30),
        "plate_U2.png": stack((185, 120), 26),
        "plate_U3.png": stack((330, 20), 30),
        "plate_U4.png": stack((240, 26), 30),
        "plate_U5.png": stack((24, 16), 26),
        "plate_U6a.png": stack((56, 10), 22),
        "plate_U6b.png": stack((430, 10), 22, stage=2),
        "plate_U6freeze.png": stack((430, 10), 22, stage=2, question=True),
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
