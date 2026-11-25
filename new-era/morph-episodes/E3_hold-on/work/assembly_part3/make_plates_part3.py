#!/usr/bin/env python3
"""PIL chalk plates for HOLD ON E3 PART 3 assembly (BRIEF_PART3 plate spec).

Wall states (all chalk is POST layer; takes are generated blank):
- U1 pre-scrape:  Part 2's freeze question SHOULD LAURA WRITE THE
  WATCHER'S NAME? + a row of YES tallies beneath it.
- U1 post-scrape: the question remains; the tallies are GONE
  (a smear band where they were).
- U2-U5 morning stack: THE STREET SAID NO (fresh, the Watcher's
  chalk) + MARTA PAID. continuity + weathered residue (Part 2's
  struck MARTA — OWES THE RENT beneath it; Part 1 residue below).
- U6: the morning stack + WATCHER — OWES THE STREET A TRUE WALL
  large in Laura's true-line hand (switched on as she writes).
White chalk, docket hand (Liberation Serif + chalk erosion).
Also renders the house corner bug (~ WuBu ~, gold serif,
bottom-right) — same as Part 2.

Plate origins are per-unit defaults; tune at assembly against
each accepted take's wall field (preview composites first).
"""
import random

from PIL import Image, ImageDraw, ImageFilter, ImageFont

random.seed(20261124)
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SERIF_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
W, H = 1280, 720
CHALK = (238, 238, 232)
WEATHERED = (196, 196, 188)

QUESTION = "SHOULD LAURA WRITE THE WATCHER'S NAME?"
LIES = "THE STREET SAID NO"
PAID = "MARTA PAID."
P2_DOCKET = "MARTA — OWES THE RENT"
P1_DOCKET = "SHE HELD MY TIN. MY COINS ARE GONE."
P1_TRUE = "HANDS OPEN. COINS LOOSE."
TRUE_LINE = "WATCHER — OWES THE STREET A TRUE WALL"


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


def tallies(origin, size, count=14):
    """A row of YES tally marks (groups of five) under the question."""
    x0, y0 = origin
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    x = x0
    h = int(size * 1.15)
    for i in range(count):
        if i % 5 == 4:
            # diagonal gate stroke across the group of four
            gx = x - int(size * 0.62) * 4 - int(size * 0.3)
            d.line([(gx, y0 + h), (x - int(size * 0.2), y0 - 2)],
                   fill=CHALK + (225,), width=max(3, size // 6))
        else:
            d.line([(x, y0), (x + random.uniform(-1.5, 1.5), y0 + h)],
                   fill=CHALK + (230,), width=max(3, size // 6))
        x += int(size * 0.62)
        if i % 5 == 4:
            x += int(size * 0.5)
    return layer


def smear(origin, width, size):
    """A horizontal chalk-smear band: the tallies after the sleeve."""
    x0, y0 = origin
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    for _ in range(260):
        y = y0 + random.gauss(size * 0.55, size * 0.22)
        x = x0 + random.uniform(0, width)
        ln = random.uniform(18, 90)
        d.line([(x, y), (x + ln, y + random.uniform(-2, 2))],
               fill=CHALK + (random.randrange(18, 60),),
               width=random.randrange(2, 6))
    return layer.filter(ImageFilter.GaussianBlur(1.1))


def u1_plate(origin, size, scraped):
    """U1 wall: the freeze question; tallies before the scrape,
    smear after it."""
    x0, y0 = origin
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    img.alpha_composite(chalk_line(QUESTION, (x0, y0),
                                   max(17, int(size * 0.78))))
    ty = y0 + int(size * 1.5)
    if scraped:
        tw = int(size * 0.62) * 14 + int(size * 1.5)
        img.alpha_composite(smear((x0 + 4, ty), tw, size))
    else:
        img.alpha_composite(tallies((x0 + 6, ty), size))
    return erode(img, 20000)


def morning_stack(origin, size, true_line=False, true_origin=None):
    """U2 onward: THE STREET SAID NO fresh on top; MARTA PAID.
    continuity; weathered struck Part 2 docket + Part 1 residue."""
    x0, y0 = origin
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    img.alpha_composite(chalk_line(LIES, (x0, y0), size))
    dy = int(size * 1.5)
    img.alpha_composite(chalk_line(PAID, (x0, y0 + dy),
                                   max(16, int(size * 0.66))))
    dy += int(size * 1.15)
    img.alpha_composite(chalk_line(P2_DOCKET, (x0, y0 + dy),
                                   max(15, int(size * 0.58)),
                                   color=WEATHERED, alpha=120,
                                   strike=True))
    dy += int(size * 0.95)
    img.alpha_composite(chalk_line(P1_DOCKET, (x0, y0 + dy),
                                   max(15, int(size * 0.55)),
                                   color=WEATHERED, alpha=105,
                                   strike=True))
    dy += int(size * 0.9)
    img.alpha_composite(chalk_line(P1_TRUE, (x0, y0 + dy),
                                   max(15, int(size * 0.55)),
                                   color=WEATHERED, alpha=105))
    if true_line:
        to = true_origin if true_origin else (x0, y0 - int(size * 1.9))
        img.alpha_composite(chalk_line(TRUE_LINE, to, int(size * 1.18)))
    return erode(img, 26000)


def main():
    out = "/home/hatch/workspace/wubutv-network/new-era/morph-episodes/E3_hold-on/work/assembly_part3"
    plates = {
        # U1: flat wall face below the hanging board (tuned on pv_U1a)
        "plate_U1a.png": u1_plate((270, 168), 26, scraped=False),
        "plate_U1b.png": u1_plate((270, 168), 26, scraped=True),
        # U3-U5 morning stacks (U2 tuned by the successor on U2_t2)
        "plate_U3.png": morning_stack((450, 36), 24),
        "plate_U4.png": morning_stack((300, 26), 22),
        "plate_U5.png": morning_stack((440, 56), 22),
        # U6: stack low/center; the true line large on the upper-left
        # wall where her chalk moves (tuned on pv_U6b — never on a face)
        "plate_U6a.png": morning_stack((430, 300), 22),
        "plate_U6b.png": morning_stack((430, 300), 22, true_line=True,
                                       true_origin=(16, 54)),
        # U2: tuned by session 8 on U2_t2's wall field (corner brick
        # face between the door and the hanging board; preview-checked
        # at 0.5/2.5/5.0/7.5/9.5s — on brick throughout, never on a
        # face; rendered standalone in session 8 so the session-6
        # plates above keep their exact random sequence)
        "plate_U2.png": morning_stack((352, 64), 24),
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
