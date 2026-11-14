#!/usr/bin/env python3
r"""kinetic_ass.py — per-word kinetic type for WuBuTV music videos.

Takes a words JSON in the SONG_WORDS.json shape ({"words":[{word,start,end,
line?,...}]} or a bare list of the same) and emits an .ass subtitle file with
per-word kinetic moves, for burning over generated footage in POST with
ffmpeg (ass filter). Type is NEVER generated inside clips — this is the type
layer, composited at assembly.

Presets:
  SLAM      each word alone, center lower-third, scales 300%->100% on onset
  CASCADE   line builds word by word; each word flies in (\move) from
            alternating left/right into its slot in the line
  HIGHLIGHT full line shown dim for its whole span; the active word pops in
            CADMIUM at 112% over its slot
  STACK     words stack one per row, building the line downward
  MIXED     cycle SLAM->CASCADE->HIGHLIGHT->STACK per line (showcase/proofs)

Also emits an optional graphic accent layer (--accents, default on): a thin
palette bar that slides in under each line (ASS \p1 drawing + \move).

WuBu palette (ASS colors are &HBBGGRR):
  COBALT #1B3FD1  VERMILION #E23A1B  CADMIUM #FFC61E
  BONE   #F4EEDC  INK       #141414  FOREST  #1E4D33

Usage:
  python3 kinetic_ass.py --words SONG_WORDS.json --preset HIGHLIGHT \
      --out kinetic.ass [--start 0 --end 10] [--no-accents]
Plain python3, stdlib only.
"""
import argparse, json, sys

PALETTE = {  # name -> (hexRGB, ass &HBBGGRR)
    "COBALT":    ("1B3FD1", "&HD13F1B"),
    "VERMILION": ("E23A1B", "&H1B3AE2"),
    "CADMIUM":   ("FFC61E", "&H1EC6FF"),
    "BONE":      ("F4EEDC", "&HDCEEF4"),
    "INK":       ("141414", "&H141414"),
    "FOREST":    ("1E4D33", "&H334D1E"),
}
ACCENT_CYCLE = ["CADMIUM", "VERMILION", "COBALT", "FOREST"]
PRESETS = ["SLAM", "CASCADE", "HIGHLIGHT", "STACK", "MIXED"]

def ts(t):
    t = max(0.0, t)
    h = int(t // 3600); m = int((t % 3600) // 60); s = t % 60
    return f"{h}:{m:02d}:{s:05.2f}"

def load_words(path):
    d = json.load(open(path))
    words = d["words"] if isinstance(d, dict) else d
    out = []
    for w in words:
        out.append({"word": str(w["word"]), "start": float(w["start"]),
                    "end": float(w["end"]), "line": w.get("line")})
    out.sort(key=lambda w: w["start"])
    return out

def group_lines(words):
    """Group by the 'line' field when present, else split on >0.7s gaps."""
    lines, cur, last_end = [], [], None
    for w in words:
        new = False
        if cur:
            if w["line"] is not None and cur[-1]["line"] is not None:
                new = w["line"] != cur[-1]["line"]
            elif last_end is not None and w["start"] - last_end > 0.7:
                new = True
        if new:
            lines.append(cur); cur = []
        cur.append(w); last_end = w["end"]
    if cur: lines.append(cur)
    return lines

class Ass:
    def __init__(self, width, height, font, fontsize):
        self.W, self.H, self.font, self.fs = width, height, font, fontsize
        self.events = []
    def add(self, layer, start, end, style, text):
        if end <= start: end = start + 0.05
        self.events.append(
            f"Dialogue: {layer},{ts(start)},{ts(end)},{style},,0,0,0,,{text}")
    def header(self):
        B = PALETTE["BONE"][1]; I = PALETTE["INK"][1]; C = PALETTE["CADMIUM"][1]
        return f"""[Script Info]
Title: WuBuTV kinetic type (kinetic_ass.py)
ScriptType: v4.00+
PlayResX: {self.W}
PlayResY: {self.H}
WrapStyle: 2

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Bone,{self.font},{self.fs},{B},{B},{I},&H96000000,-1,0,0,0,100,100,0,0,1,4,0,5,10,10,10,1
Style: Cadmium,{self.font},{self.fs},{C},{C},{I},&H96000000,-1,0,0,0,100,100,0,0,1,4,0,5,10,10,10,1
Style: Dim,{self.font},{self.fs},&H64DCEEF4,&H64DCEEF4,{I},&H96000000,-1,0,0,0,100,100,0,0,1,4,0,5,10,10,10,1
Style: Draw,{self.font},{self.fs},{B},{B},{I},&H00000000,0,0,0,0,100,100,0,0,1,0,0,7,0,0,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

def char_w(fs):  # rough advance width of one char at fontsize (bold sans)
    return fs * 0.52

def line_slots(line, fs):
    """Return (total_width, [(word, x_left), ...]) for a centered line."""
    widths = [len(w["word"]) * char_w(fs) for w in line]
    space = char_w(fs)
    total = sum(widths) + space * (len(line) - 1)
    return total, widths, space

def emit_line(a, line, preset, li, accents, next_start=None):
    fs = a.fs
    cx, base_y = a.W // 2, int(a.H * 0.80)
    lstart = line[0]["start"]
    lend = max(w["end"] for w in line) + 0.45
    if next_start is not None:  # never bleed into the next line's window
        lend = min(lend, next_start - 0.02)
    total, widths, space = line_slots(line, fs)
    x0 = cx - total / 2
    slots, x = [], x0
    for w, wd in zip(line, widths):
        slots.append(x); x += wd + space

    if accents:  # graphic accent layer: palette bar slides in under the line
        col = PALETTE[ACCENT_CYCLE[li % len(ACCENT_CYCLE)]][1]
        bw = max(120, int(total))
        bar = (f"{{\\an7\\1c{col}\\bord0\\shad0"
               f"\\move({cx-bw//2-260},{base_y+34},{cx-bw//2},{base_y+34},0,220)"
               f"\\p1}}m 0 0 l {bw} 0 l {bw} 7 l 0 7{{\\p0}}")
        a.add(0, lstart, lend, "Draw", bar)

    if preset == "SLAM":
        for i, w in enumerate(line):
            # Last word: tail is w["end"] + 0.4, but NEVER bleed into the
            # next line's window — lend is already capped at next_start-0.02.
            # (2026-11-09 MV-9: the uncapped tail put the previous line's last
            # word at full opacity over the next line's opening words for
            # 0.37-0.40s at 6 back-to-back boundaries, e.g. "goty" at 145.99s.)
            nxt = line[i + 1]["start"] if i + 1 < len(line) else min(w["end"] + 0.4, lend)
            txt = (f"{{\\an5\\pos({cx},{base_y})\\fscx300\\fscy300\\alpha&HFF&"
                   f"\\t(0,60,\\fscx300\\fscy300\\alpha&H00&)"
                   f"\\t(60,150,\\fscx100\\fscy100)\\fad(0,90)}}{w['word']}")
            a.add(2, w["start"], nxt, "Cadmium" if i % 2 else "Bone", txt)

    elif preset == "CASCADE":
        for i, (w, sx, wd) in enumerate(zip(line, slots, widths)):
            from_x = int(sx - 420) if i % 2 == 0 else int(sx + wd + 420)
            txt = (f"{{\\an4\\move({from_x},{base_y},{int(sx)},{base_y},0,200)"
                   f"\\fad(60,0)}}{w['word']}")
            a.add(2, w["start"], lend, "Bone", txt)

    elif preset == "HIGHLIGHT":
        # Per-word events at computed slots for BOTH layers: a single
        # full-line string is laid out with real font metrics, so overlay
        # x-positions estimated from char widths drift off the dim copy.
        # Same-estimate per-word slots keep the CADMIUM pop exactly on top.
        for w, sx in zip(line, slots):
            a.add(1, lstart, lend, "Dim",
                  f"{{\\an4\\pos({int(sx)},{base_y})\\fad(120,150)}}{w['word']}")
        for w, sx in zip(line, slots):
            txt = (f"{{\\an4\\pos({int(sx)},{base_y})\\fscx112\\fscy112"
                   f"\\t(0,90,\\fscx100\\fscy100)}}{w['word']}")
            a.add(2, w["start"], min(w["end"] + 0.12, lend), "Cadmium", txt)

    elif preset == "STACK":
        for i, w in enumerate(line):
            y = int(a.H * 0.52) + i * int(fs * 1.25)
            txt = (f"{{\\an5\\pos({cx},{y})\\fscx40\\fscy40"
                   f"\\t(0,130,\\fscx100\\fscy100)\\fad(0,120)}}{w['word']}")
            a.add(2, w["start"], lend, "Cadmium" if i == len(line) - 1 else "Bone", txt)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--words", required=True)
    ap.add_argument("--preset", default="HIGHLIGHT", choices=PRESETS)
    ap.add_argument("--out", required=True)
    ap.add_argument("--start", type=float, default=0.0)
    ap.add_argument("--end", type=float, default=1e9)
    ap.add_argument("--width", type=int, default=1280)
    ap.add_argument("--height", type=int, default=720)
    ap.add_argument("--font", default="Noto Sans")
    ap.add_argument("--fontsize", type=int, default=54)
    ap.add_argument("--no-accents", action="store_true")
    args = ap.parse_args()

    words = [w for w in load_words(args.words)
             if args.start <= w["start"] < args.end]
    if not words:
        sys.exit("no words in window")
    lines = group_lines(words)
    a = Ass(args.width, args.height, args.font, args.fontsize)
    cycle = ["SLAM", "CASCADE", "HIGHLIGHT", "STACK"]
    for li, line in enumerate(lines):
        preset = cycle[li % 4] if args.preset == "MIXED" else args.preset
        nxt = lines[li + 1][0]["start"] if li + 1 < len(lines) else None
        emit_line(a, line, preset, li, not args.no_accents, nxt)
    with open(args.out, "w") as f:
        f.write(a.header())
        f.write("\n".join(a.events) + "\n")
    print(f"{args.out}: {len(lines)} lines, {len(words)} words, "
          f"{len(a.events)} events, preset={args.preset}")

if __name__ == "__main__":
    main()
