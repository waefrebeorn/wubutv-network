#!/usr/bin/env python3
"""render_countdown_proof.py — Family I proof: countdown / listicle.

Deterministic renderAt(t). A steady procedural base (H2 gradient drift)
carried by a graphics layer, per VISUAL_FORMS_TAXONOMY Family I1:

  * items land ON measured downbeats of the project's beat grid
    (one clock rule — work/beat_grid.json; counter increments ON the
    naming beat, never between items);
  * the giant number slams with a true back-out spring (code type —
    the G2 move ASS cannot express);
  * milestone label + palette accent bar per item; progress counter
    "n / 5" top-right ticks on each onset; counted chips accumulate
    along the bottom (the outgoing number shrinks INTO its chip);
  * a drawn lemon glyph pops on every increment;
  * #1 gets the finale: CADMIUM number, ring bursts, payoff subline.

All type/graphics are this post-layer code render — zero generated text.
Audio: source track slice only, muxed at encode time by the caller.

Usage:
  python3 render_countdown_proof.py --grid MV-6.../work/beat_grid.json \
      --window-start 44.489 --out-frames /tmp/count_frames
Then: ffmpeg -framerate 24 -i f%03d.png -i slice.m4a -c:v libx264 \
      -pix_fmt yuv420p -crf 18 -c:a copy countdown_proof_16x9.mp4
"""
import argparse, json, math, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS, DUR = 1280, 720, 24, 10.0
INK = (20, 20, 20); BONE = (244, 238, 220); CADMIUM = (255, 198, 30)
VERMILION = (226, 58, 27); COBALT = (27, 63, 209); FOREST = (30, 77, 51)
FONT_BOLD = "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf"
FONT_BLACK = "/usr/share/fonts/truetype/noto/NotoSans-Black.ttf"

ITEMS = [  # (number, milestone, accent) in reveal order
    (5, "ONE LEMON, ONE STAND", CADMIUM),
    (4, "THE JUICER DOUBLES THE TAKE", VERMILION),
    (3, "CRATES BY THE DOZEN", COBALT),
    (2, "LIME LABS OPENS ITS DOORS", FOREST),
    (1, "$1.243 OCTOVIGINTILLION", CADMIUM),
]
FINALE_SUB = "THE TOP OF THE MONEY TOWER"


def ease_out_back(u):
    c1, c3 = 1.70158, 2.70158
    return 1 + c3 * (u - 1) ** 3 + c1 * (u - 1) ** 2


def text_layer(text, font, fill):
    tmp = Image.new("RGBA", (10, 10))
    tw = ImageDraw.Draw(tmp).textlength(text, font=font)
    asc, desc = font.getmetrics()
    img = Image.new("RGBA", (int(tw) + 8, asc + desc + 8), (0, 0, 0, 0))
    ImageDraw.Draw(img).text((4, 2), text, font=font, fill=fill + (255,))
    return img


def scale_alpha(layer, scale, alpha):
    if scale != 1.0:
        layer = layer.resize((max(1, int(layer.width * scale)),
                              max(1, int(layer.height * scale))), Image.LANCZOS)
    if alpha < 255:
        a = layer.getchannel("A").point(lambda v: v * alpha // 255)
        layer.putalpha(a)
    return layer


def paste_center(base, layer, cx, cy):
    base.alpha_composite(layer, (int(cx - layer.width / 2), int(cy - layer.height / 2)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--grid", required=True)
    ap.add_argument("--window-start", type=float, required=True)
    ap.add_argument("--out-frames", required=True)
    args = ap.parse_args()

    grid = json.load(open(args.grid))
    downbeats = [b["t"] - args.window_start for b in grid["beats"]
                 if b["is_downbeat"] and args.window_start <= b["t"] < args.window_start + DUR]
    onsets = downbeats[:5]
    assert len(onsets) == 5, f"need 5 downbeats in window, got {onsets}"
    beat_iv = grid["beat_interval_s_median"]

    f_num = ImageFont.truetype(FONT_BLACK, 330)
    f_num1 = ImageFont.truetype(FONT_BLACK, 380)
    f_label = ImageFont.truetype(FONT_BOLD, 46)
    f_sub = ImageFont.truetype(FONT_BOLD, 30)
    f_count = ImageFont.truetype(FONT_BLACK, 54)
    f_micro = ImageFont.truetype(FONT_BOLD, 19)
    f_title = ImageFont.truetype(FONT_BOLD, 34)
    f_chip = ImageFont.truetype(FONT_BLACK, 27)

    CX, CY = W // 2, 300  # stage centre for the number

    # pre-render per-item number + label layers
    item_layers = []
    for num, label, accent in ITEMS:
        nlay = text_layer(str(num), f_num1 if num == 1 else f_num,
                          CADMIUM if num == 1 else BONE)
        llay = text_layer(label, f_label, BONE)
        item_layers.append((nlay, llay))
    sub_layer = text_layer(FINALE_SUB, f_sub, VERMILION)
    chip_layers = {num: text_layer(str(num), f_chip, BONE) for num, _, _ in ITEMS}

    # glow sprites per accent colour
    glows = {}
    for _, _, accent in ITEMS:
        g = Image.new("RGBA", (760, 760), (0, 0, 0, 0))
        ImageDraw.Draw(g).ellipse([190, 190, 570, 570], fill=accent + (64,))
        glows[accent] = g.filter(ImageFilter.GaussianBlur(110))

    # base: INK + two slow diagonal panels (drawn per frame with drift)
    os.makedirs(args.out_frames, exist_ok=True)
    nframes = int(DUR * FPS)
    chip_y = 648
    chip_x0 = CX - (5 * 64 - 20) // 2  # 5 chips, 44px + 20 gap

    for f in range(nframes):
        t = f / FPS
        img = Image.new("RGBA", (W, H), INK + (255,))
        d = ImageDraw.Draw(img, "RGBA")
        # H2 procedural base: drifting diagonal panels
        drift = (t * 11) % 160
        d.polygon([(-260 + drift, 0), (240 + drift, 0), (-60 + drift, H), (-560 + drift, H)],
                  fill=COBALT + (26,))
        d.polygon([(W - 180 - drift, 0), (W + 320 - drift, 0), (W + 60 - drift, H), (W - 440 - drift, H)],
                  fill=FOREST + (22,))
        for gx in range(64, W, 64):  # faint dot grid, static = the "steady base"
            for gy in range(64, H, 64):
                d.ellipse([gx - 2, gy - 2, gx + 2, gy + 2], fill=BONE + (14,))

        # which item is active
        active = max(i for i, o in enumerate(onsets) if t >= o)
        num, label, accent = ITEMS[active]
        age = t - onsets[active]

        # glow behind stage, item colour
        paste_center(img, glows[accent], CX, CY)
        d = ImageDraw.Draw(img, "RGBA")

        # outgoing number shrinks into its chip during 0.30 s after an onset
        if active > 0 and age < 0.30:
            p = age / 0.30
            pnum, _, paccent = ITEMS[active - 1]
            layer = item_layers[active - 1][0]
            slot = active - 1
            tx = chip_x0 + slot * 64 + 22
            sc = 1.0 + (0.13 - 1.0) * (p * p * (3 - 2 * p))
            lay = scale_alpha(layer.copy(), sc, 255)
            paste_center(img, lay, CX + (tx - CX) * p, CY + (chip_y - CY) * p)

        # active number: slam spring, then (finale) a beat-rate pulse
        nlay = item_layers[active][0]
        if age < 0.34:
            u = age / 0.34
            sc = 2.6 + (1.0 - 2.6) * ease_out_back(u)
            alpha = min(255, int(255 * age / 0.06)) if age < 0.06 else 255
        else:
            sc, alpha = 1.0, 255
            if num == 1:
                sc = 1.0 + 0.018 * math.sin(2 * math.pi * (age / beat_iv))
        paste_center(img, scale_alpha(nlay.copy(), max(0.05, sc), alpha), CX, CY)
        d = ImageDraw.Draw(img, "RGBA")

        # accent bar + label (slide-up fade, from onset + 0.05)
        la = t - (onsets[active] + 0.05)
        if la >= 0:
            lp = min(1.0, la / 0.20)
            llay = item_layers[active][1]
            ly = 528 + int(14 * (1 - lp))
            paste_center(img, scale_alpha(llay.copy(), 1.0, int(255 * lp)), CX, ly)
            d = ImageDraw.Draw(img, "RGBA")
            bw = int(llay.width * min(1.0, la / 0.22))
            d.rectangle([CX - bw / 2, 560, CX + bw / 2, 568], fill=accent + (255,))
            if num == 1 and t > onsets[active] + 0.35:
                sp = min(1.0, (t - onsets[active] - 0.35) / 0.25)
                paste_center(img, scale_alpha(sub_layer.copy(), 1.0, int(255 * sp)), CX, 606)

        # finale ring bursts (onset, +0.08, +0.16; expand/fade 0.8 s)
        if num == 1:
            for k, delay in enumerate((0.0, 0.08, 0.16)):
                ra = age - delay
                if 0 <= ra < 0.8:
                    r = 120 + ra * 620
                    a = int(210 * (1 - ra / 0.8))
                    d.ellipse([CX - r, CY - r, CX + r, CY + r], outline=CADMIUM + (a,), width=5)

        # counted chips (completed items sit filled; current pops at onset)
        for slot, (cnum, _, caccent) in enumerate(ITEMS):
            if slot > active:
                break
            x = chip_x0 + slot * 64
            pop = 1.0
            cage = t - onsets[slot]
            if cage < 0.2:
                pop = 1 + 0.3 * (1 - cage / 0.2)
            cs = 44 * pop
            d.rounded_rectangle([x + 22 - cs / 2, chip_y - cs / 2, x + 22 + cs / 2, chip_y + cs / 2],
                                radius=9, outline=caccent, width=3,
                                fill=caccent + (46,) if slot < active else None)
            paste_center(img, chip_layers[cnum], x + 22, chip_y)

        # progress counter: ticks ON the item onset (n = items revealed)
        n = active + 1
        d.text((W - 46, 40), "MILESTONES", font=f_micro, fill=BONE + (150,), anchor="ra")
        d.text((W - 46, 62), f"{n} / 5", font=f_count, fill=BONE, anchor="ra")
        # title block
        d.text((44, 34), "SELL THE LEMONS", font=f_title, fill=BONE)
        d.text((46, 76), "COUNTDOWN", font=f_micro, fill=CADMIUM)
        tw = d.textlength("~ WuBu ~", font=f_micro)
        d.text((W - tw - 40, 40), "", font=f_micro)  # (bug sits bottom-right instead)
        d.text((W - 40, H - 44), "~ WuBu ~", font=ImageFont.truetype(FONT_BOLD, 24),
               fill=BONE + (190,), anchor="ra")

        # lemon glyph, bottom-left: bob per bar + pop on each onset
        bob = math.sin(2 * math.pi * t / (beat_iv * 4)) * 4
        pop = 1.0
        for o in onsets:
            if 0 <= t - o < 0.18:
                pop = 1 + 0.35 * (1 - (t - o) / 0.18)
        lx, ly = 84, chip_y + bob
        lw, lh = 62 * pop, 46 * pop
        d.ellipse([lx - lw / 2, ly - lh / 2, lx + lw / 2, ly + lh / 2], fill=CADMIUM)
        d.ellipse([lx - lw / 2 - 6, ly - 5, lx - lw / 2 + 5, ly + 5], fill=CADMIUM)
        d.ellipse([lx + lw / 2 - 5, ly - 5, lx + lw / 2 + 6, ly + 5], fill=CADMIUM)
        d.polygon([(lx + 12, ly - lh / 2), (lx + 30, ly - lh / 2 - 12), (lx + 16, ly - lh / 2 + 3)],
                  fill=FOREST)

        img.convert("RGB").save(os.path.join(args.out_frames, f"f{f:03d}.png"))
    print(f"rendered {nframes} frames; onsets={onsets}")


if __name__ == "__main__":
    main()
