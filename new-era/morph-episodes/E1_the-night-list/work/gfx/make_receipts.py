#!/usr/bin/env python3
"""Mark the two receipt slips under UNC's hands on PEAK-U4 with 'BED 7' (post-drawn ink)."""
from PIL import Image, ImageDraw, ImageFont

EP = "/home/hatch/workspace/wubutv-network/new-era/morph-episodes/E1_the-night-list"
SERIF_B = "/usr/share/fonts/truetype/noto/NotoSerif-Bold.ttf"
INK = (43, 38, 33, 225)

img = Image.open(f"{EP}/panels/PNL-PEAK-U4.png").convert("RGBA")
# the two slips at his hands (right side of the desk row), panel coords 2048x1152
slips = [((1338, 906), -2.0), ((1358, 940), -1.0)]
for (x, y), ang in slips:
    tile = Image.new("RGBA", (150, 44), (0, 0, 0, 0))
    d = ImageDraw.Draw(tile)
    f = ImageFont.truetype(SERIF_B, 30)
    d.text((8, 5), "BED 7", font=f, fill=INK)
    tile = tile.rotate(ang, resample=Image.BICUBIC, expand=True)
    img.alpha_composite(tile, (x, y))
img.convert("RGB").save(f"{EP}/panels/PNL-PEAK-U4.png")
print("receipts marked")
