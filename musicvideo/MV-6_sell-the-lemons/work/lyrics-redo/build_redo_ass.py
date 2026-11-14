#!/usr/bin/env python3
"""Build work/lyrics-redo/mv6_kinetic_redo.ass from new_word_grid.json.

Design (same as the old mv6.ass, words+times corrected):
  Caption layer: one event per grid caption line, style Caption (fs 40).
  Kinetic layer: per-word events via kinetic_ass.py's emit logic, adapted:
    * per-line font-size scaling: estimated line width capped at 1100px
      (MV-13 overflow fix). SLAM words display one at a time, so the cap
      applies to the longest single word (never binding); CASCADE and
      HIGHLIGHT show the whole line at once, so the cap applies to the
      full line width. Scaled lines get an inline {\\fsN} override and
      slots computed at the scaled size.
    * HIGHLIGHT Dim layer uses \\fad(0,150) — NO fade-in — so the first
      word is full-strength at the line's exact start frame (known nit).
    * SINGLE backslashes only in all overrides (MV-12 bug); verified after.
  Word times: mix backbone for clean lines (count-checked after GARBLE
  normalization); explicit per-word times in the grid for glued/garbled
  tokens; stem sources for the dense spans.
"""
import json, sys

ROOT = "/home/hatch/workspace/wubutv-network/musicvideo/MV-6_sell-the-lemons"
LR = ROOT + "/work/lyrics-redo"
OUT = LR + "/mv6_kinetic_redo.ass"

GARBLE = {
 "lemmons": "lemons", "lemongs": "lemons", "lomon": "lemons",
 "lemoons": "lemons", "level": "lemons", "lamons": "lemons",
 "levins": "lemons", "limons": "lemons", "lemon": "lemons",
 "levels": "lemons", "lewins": "lemons", "lebens": "lemons",
 "levens": "lemons", "elements": "lemons",
 "sellthe": "sell", "sellthen": "sell", "sellth": "sell",
 "bakon": "bacon", "bakone": "bacon", "baconhead": "bacon",
 "baconheads": "bacon", "breaking": "bacon", "silver": "sell",
 "heads": "head", "them": "the", "sale": "sell", "start": "stop",
 "multiply": "multipliers", "nerga": "never", "hot": "high",
 "up": "the", "stick": "sell",
}

PALETTE = {
    "COBALT": "&HD13F1B", "VERMILION": "&H1B3AE2", "CADMIUM": "&H1EC6FF",
    "BONE": "&HDCEEF4", "INK": "&H141414", "FOREST": "&H334D1E",
}
ACCENT_CYCLE = ["CADMIUM", "VERMILION", "COBALT", "FOREST"]
W, H, FONT, FS_KIN, FS_CAP = 1280, 720, "Noto Sans", 54, 40
WIDTH_CAP = 1100


def ts(t):
    t = max(0.0, t)
    h = int(t // 3600); m = int((t % 3600) // 60); s = t % 60
    return f"{h}:{m:02d}:{s:05.2f}"


def norm(w):
    return GARBLE.get(w.lower().strip(".,!?'\"()…"), w.lower().strip(".,!?'\"()…"))


def load_words(path):
    d = json.load(open(path))
    return d["words"] if isinstance(d, dict) else d


def line_slots(words, fs):
    """(total_width, [word widths], space) for a centered line at fs."""
    cw = fs * 0.52
    widths = [len(w) * cw for w in words]
    total = sum(widths) + cw * (len(words) - 1)
    return total, widths, cw


def scaled_fs(words, preset):
    """Font size for a kinetic line: SLAM is one word at a time (cap the
    longest word); CASCADE/HIGHLIGHT show the whole line (cap the line)."""
    if preset == "SLAM":
        widest = max(len(w) for w in words)
        est = widest * FS_KIN * 0.52
    else:
        est, _, _ = line_slots(words, FS_KIN)
    if est <= WIDTH_CAP:
        return FS_KIN
    return max(20, int(FS_KIN * WIDTH_CAP / est))


def main():
    grid = json.load(open(LR + "/new_word_grid.json"))
    mix = load_words(LR + "/song_words_v3turbo.json")
    stems = {n: load_words(LR + f"/song_words_{n}_stem.json")
             for n in ["head", "c1tail", "bridge", "fc", "outro"]}

    # --- resolve kinetic word lists ---
    kin = []
    for k in grid["kinetic"]:
        if k["source"] == "explicit":
            words = [(w, float(s), float(e)) for w, s, e in k["words"]]
        else:
            src = mix if k["source"] == "mix" else stems[k["source"][5:]]
            a, b = k["start"], k["end"]
            # words whose START falls in [a-0.05, b): the next line's first
            # word starts exactly at b, so a strict < b keeps it out.
            cand = [w for w in src if a - 0.05 <= w["start"] < b]
            # canonical word list = the matching caption lines' words
            canon = []
            for c in grid["captions"]:
                if c["start"] >= a - 0.01 and c["end"] <= b + 0.35:
                    canon.extend(c["text"].replace("…", "").split())
            canon = [norm(c.strip(".,!?'\"")) for c in canon]
            # for merged SLAM lines the caption text may carry a trailing
            # comma/period; strip those for the count check
            got = [norm(w["word"]) for w in cand]
            if len(got) != len(canon):
                print(f"FAIL {k['id']}: {len(got)} source words {got} "
                      f"vs {len(canon)} canonical {canon}")
                sys.exit(1)
            for g, c in zip(got, canon):
                if g != c:
                    print(f"FAIL {k['id']}: source word {g!r} != canonical {c!r}")
                    sys.exit(1)
            words = [(canon[i], float(w["start"]), float(w["end"]))
                     for i, w in enumerate(cand)]
        # kinetic display is UPPERCASE (old design: SLAM/CASCADE/HIGHLIGHT
        # all caps; captions stay sentence-case)
        words = [(w[0].upper(), w[1], w[2]) for w in words]
        kin.append((k, words))

    # --- caption width audit (fs 40) ---
    for c in grid["captions"]:
        est, _, _ = line_slots(c["text"].split(), FS_CAP)
        if est > WIDTH_CAP:
            print(f"CAPTION OVERFLOW {c['id']}: {est:.0f}px {c['text']!r}")
            sys.exit(1)

    # --- emit ---
    events = []
    for c in grid["captions"]:
        events.append((1, c["start"], c["end"], "Caption", c["text"]))

    cx, base_y = W // 2, int(H * 0.80)
    # kinetic line start order = grid order; next_start = next kinetic line
    # (explicit lines carry no start/end keys: derive from their words)
    starts = [k.get("start", w[0][1]) for k, w in kin]
    for li, (k, words) in enumerate(kin):
        preset = k["preset"]
        wtexts = [w[0] for w in words]
        fs = scaled_fs(wtexts, preset)
        # \fs goes INSIDE the existing override braces — a nested {..}
        # would break libass parsing and print raw tags on screen (br4 bug).
        fs_tag = f"\\fs{fs}" if fs != FS_KIN else ""
        lstart = words[0][1]
        lend = max(w[2] for w in words) + 0.45
        nxt = starts[li + 1] if li + 1 < len(starts) else None
        if nxt is not None:
            lend = min(lend, nxt - 0.02)
        total, widths, space = line_slots(wtexts, fs)
        x0 = cx - total / 2
        slots, x = [], x0
        for wd in widths:
            slots.append(x); x += wd + space
        # accent bar
        col = PALETTE[ACCENT_CYCLE[li % len(ACCENT_CYCLE)]]
        bw = max(120, int(total))
        bar = (f"{{\\an7\\1c{col}\\bord0\\shad0"
               f"\\move({cx-bw//2-260},{base_y+34},{cx-bw//2},{base_y+34},0,220)"
               f"\\p1}}m 0 0 l {bw} 0 l {bw} 7 l 0 7{{\\p0}}")
        events.append((0, lstart, lend, "Draw", bar))
        if preset == "SLAM":
            for i, (wt, ws, we) in enumerate(words):
                nxt_w = words[i + 1][1] if i + 1 < len(words) else min(we + 0.4, lend)
                txt = (f"{{\\an5\\pos({cx},{base_y}){fs_tag}\\fscx300\\fscy300"
                       f"\\alpha&HFF&\\t(0,60,\\fscx300\\fscy300\\alpha&H00&)"
                       f"\\t(60,150,\\fscx100\\fscy100)\\fad(0,90)}}{wt}")
                events.append((2, ws, nxt_w, "Cadmium" if i % 2 else "Bone", txt))
        elif preset == "CASCADE":
            for i, ((wt, ws, we), sx, wd) in enumerate(zip(words, slots, widths)):
                from_x = int(sx - 420) if i % 2 == 0 else int(sx + wd + 420)
                txt = (f"{{\\an4\\move({from_x},{base_y},{int(sx)},{base_y},0,200)"
                       f"{fs_tag}\\fad(60,0)}}{wt}")
                events.append((2, ws, lend, "Bone", txt))
        elif preset == "HIGHLIGHT":
            for (wt, ws, we), sx in zip(words, slots):
                events.append((1, lstart, lend, "Dim",
                               f"{{\\an4\\pos({int(sx)},{base_y}){fs_tag}"
                               f"\\fad(0,150)}}{wt}"))
            for (wt, ws, we), sx in zip(words, slots):
                txt = (f"{{\\an4\\pos({int(sx)},{base_y}){fs_tag}\\fscx112\\fscy112"
                       f"\\t(0,90,\\fscx100\\fscy100)}}{wt}")
                events.append((2, ws, min(we + 0.12, lend), "Cadmium", txt))
        print(f"  {k['id']:8s} {preset:9s} fs={fs} {len(words)} words "
              f"est={total:.0f}px {lstart:.2f}-{lend:.2f}")

    events.sort(key=lambda e: (e[1], e[0]))
    header = f"""[Script Info]
Title: WuBuTV kinetic type — MV-6 lyrics redo (2026-11-12)
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 2

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Bone,{FONT},{FS_KIN},&HDCEEF4,&HDCEEF4,&H141414,&H96000000,-1,0,0,0,100,100,0,0,1,4,0,5,10,10,10,1
Style: Cadmium,{FONT},{FS_KIN},&H1EC6FF,&H1EC6FF,&H141414,&H96000000,-1,0,0,0,100,100,0,0,1,4,0,5,10,10,10,1
Style: Dim,{FONT},{FS_KIN},&H64DCEEF4,&H64DCEEF4,&H141414,&H96000000,-1,0,0,0,100,100,0,0,1,4,0,5,10,10,10,1
Style: Draw,{FONT},{FS_KIN},&HDCEEF4,&HDCEEF4,&H141414,&H00000000,0,0,0,0,100,100,0,0,1,0,0,7,0,0,0,1
Style: Caption,{FONT},{FS_CAP},&HDCEEF4,&HDCEEF4,&H141414,&H96000000,-1,0,0,0,100,100,0,0,1,3,0,2,10,10,24,1
[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    with open(OUT, "w") as f:
        f.write(header)
        for layer, s, e, style, text in events:
            if e <= s:
                e = s + 0.05
            f.write(f"Dialogue: {layer},{ts(s)},{ts(e)},{style},,0,0,0,,{text}\n")
    print(f"{OUT}: {len(grid['captions'])} captions, {len(kin)} kinetic lines, "
          f"{len(events)} events total")


if __name__ == "__main__":
    main()
