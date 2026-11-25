#!/usr/bin/env python3
"""E2 SHOW-5 graphics — Class P (PIL) renderers, Method C devices.
- THE SEAT MAP (invariant, §2.5a): 9x6 seat-glyph grid on an ink card; one lit
  seat in BONE. Pilot = position 1 (retrospective baseline); E2 = position 2
  (moved exactly one). Position numbering is row-major from top-left.
- THE TWO TICKETS (§2.5c): two bone ticket stubs; printed seat number = episode
  number (2). One stub of the pair tears itself per episode — E2 renders the
  pair intact and the pair with stub B torn (switched in the encode at ~2.2s).
- The `~ WuBu ~` bug: gold, bottom-right station furniture (not an event).
Outputs RGBA PNGs into work/gfx/.
"""
import os
from PIL import Image, ImageDraw, ImageFilter, ImageFont

OUT = os.path.expanduser(
    "~/workspace/wubutv-network/new-era/episodes/E2_SHOW-5_the-last-seat/work/gfx")
os.makedirs(OUT, exist_ok=True)

BONE = (233, 221, 193)
BONE_DIM = (150, 138, 112)
INK = (12, 11, 14)
GOLD = (216, 178, 90)
PAPER = (228, 216, 184)
PAPER_INK = (52, 44, 34)

def font(size, bold=False):
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    for base in ("/usr/share/fonts/truetype/dejavu/", "/usr/share/fonts/"):
        p = os.path.join(base, name)
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

# ---------------- THE SEAT MAP ----------------
def seat_map(position=2, cols=9, rows=6, scale=4):
    cw, ch = 34 * scale, 30 * scale          # cell
    pad = 14 * scale
    W = cols * cw + pad * 2
    H = rows * ch + pad * 2 + 12 * scale      # headroom for a stage line
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([0, 0, W - 1, H - 1], radius=10 * scale,
                        fill=INK + (205,), outline=BONE_DIM + (255,),
                        width=max(2, scale))
    # stage line at top
    sy = pad // 2 + 2 * scale
    d.line([pad, sy, W - pad, sy], fill=BONE_DIM + (255,), width=max(2, scale))
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    for r in range(rows):
        for c in range(cols):
            idx = r * cols + c + 1
            x0 = pad + c * cw + 5 * scale
            y0 = pad + 8 * scale + r * ch + 3 * scale
            x1 = pad + (c + 1) * cw - 5 * scale
            y1 = pad + 8 * scale + (r + 1) * ch - 3 * scale
            if idx == position:
                gd.rounded_rectangle([x0 - 3 * scale, y0 - 3 * scale,
                                      x1 + 3 * scale, y1 + 3 * scale],
                                     radius=6 * scale, fill=BONE + (160,))
                d.rounded_rectangle([x0, y0, x1, y1], radius=5 * scale,
                                    fill=BONE + (255,))
            else:
                d.rounded_rectangle([x0, y0, x1, y1], radius=5 * scale,
                                    outline=(96, 88, 76, 255),
                                    width=max(2, scale))
    glow = glow.filter(ImageFilter.GaussianBlur(6 * scale))
    img = Image.alpha_composite(glow, img)
    img = img.resize((W // scale, H // scale), Image.LANCZOS)
    img.save(os.path.join(OUT, f"seatmap_pos{position}.png"))
    print("seatmap", img.size)

# ---------------- THE TWO TICKETS ----------------
def stub(d, x, y, w, h, number):
    d.rounded_rectangle([x, y, x + w, y + h], radius=8, fill=PAPER + (255,),
                        outline=PAPER_INK + (255,), width=2)
    # perforation
    px = x + int(w * 0.68)
    for yy in range(y + 6, y + h - 4, 9):
        d.line([px, yy, px, yy + 4], fill=PAPER_INK + (255,), width=2)
    d.text((x + 14, y + 10), "SEAT", font=font(17, bold=True),
           fill=PAPER_INK + (255,))
    d.text((x + 14, y + 30), str(number), font=font(34, bold=True),
           fill=PAPER_INK + (255,))
    d.text((px + 10, y + h // 2 - 10), str(number), font=font(20, bold=True),
           fill=PAPER_INK + (255,))

def tickets(number=2):
    W, H = 360, 240
    # intact pair
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    stub(d, 8, 18, 200, 92, number)
    stub(d, 8, 126, 200, 92, number)
    img.save(os.path.join(OUT, "tickets_intact.png"))
    # torn pair: stub B's end piece separated, rotated, offset
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    stub(d, 8, 18, 200, 92, number)
    stub(d, 8, 126, 200, 92, number)
    img.save(os.path.join(OUT, "_tickets_base.png"))
    # cut the torn end from stub B and re-paste rotated
    base = Image.open(os.path.join(OUT, "_tickets_base.png"))
    piece = base.crop((144, 126, 208, 218)).rotate(-14, expand=True,
                                                  resample=Image.BICUBIC)
    d = ImageDraw.Draw(base)
    d.rectangle([144, 126, 208, 218], fill=(0, 0, 0, 0))
    # jagged tear edge on the remaining stub
    for yy in range(128, 216, 6):
        d.polygon([(144, yy), (150, yy + 3), (144, yy + 6)],
                  fill=PAPER + (255,))
    base.alpha_composite(piece, (168, 148))
    base.save(os.path.join(OUT, "tickets_torn.png"))
    os.unlink(os.path.join(OUT, "_tickets_base.png"))
    print("tickets", base.size)

# ---------------- THE BUG ----------------
def bug():
    t = "~ WuBu ~"
    f = font(30, bold=True)
    tmp = ImageDraw.Draw(Image.new("RGBA", (10, 10)))
    box = tmp.textbbox((0, 0), t, font=f)
    W, H = box[2] - box[0] + 16, box[3] - box[1] + 12
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.text((8 - box[0], 6 - box[1]), t, font=f, fill=GOLD + (235,),
           stroke_width=2, stroke_fill=(0, 0, 0, 160))
    img.save(os.path.join(OUT, "bug_wubu.png"))
    print("bug", img.size)

if __name__ == "__main__":
    seat_map(position=2)
    tickets(number=2)
    bug()
