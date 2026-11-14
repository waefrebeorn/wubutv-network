#!/usr/bin/env python3
"""Build v6 captions (ASS) from measured song word times.

Form: line block + per-word highlight. Each word gets one event showing its
FULL line, with the current word in yellow; events tile contiguously
([word_start-0.125, next_word_start-0.125)) so the block never overlaps the
next line and the highlight moves 3 frames early. Caption text = the
PERFORMED song words (SONG_WORDS_BASE tokens) with display cleanup:
  toe/tall/told -> toll, done -> dumb (hook "dumb"), flaselines -> fast lanes,
  plasers -> plazas, -old -> old, watchin' -> watching, weavein' -> weaving,
  comin' -> coming; overrides where mouth + sheet agree against a song-Whisper
  token: bricks, -> brakes, ; high. -> hot.
Zero-duration tokens: a run of >=2 consecutive zero-duration words is a
transcription echo (words 333-339, the S17 line repeated at 205.2) and is
EXCLUDED; an isolated zero-duration word (371 "the" at 228.6, inside GAP-D's
line) is FOLDED into the next word's highlight.
Line breaks: gaps > 0.9s plus forced breaks at sheet line boundaries with
small gaps (consumed sequentially, in occurrence order; an auto-break by gap
never consumes a forced entry).
"""
import json
import pathlib
import re

PROJ = pathlib.Path.home() / "workspace/wubutv-network/musicvideo/MV-2_toll-roads-are-dumb"
WORK = PROJ / "masters_work_v6"

MAP = {
    "toe": "toll", "tall": "toll", "told": "toll", "done": "dumb",
    "flaselines": "fast lanes", "plasers": "plazas", "-old": "old",
    "watchin": "watching", "weavein": "weaving", "comin": "coming",
    "bricks": "brakes", "high": "hot",
}
# (prev, next[, min_next_t0]), in occurrence order.
FORCED = [
    ("roll", "-old"), ("go", "cars"), ("smash", "ntsb"), ("map", "now"),
    ("by", "while"), ("by", "weavein"), ("all", "one"),
    ("comin", "express"), ("high", "speed"), ("caught", "they"),
    ("hit", "crashes"), ("mess", "lexus"), ("clear", "poor"),
    ("disappear", "stop"), ("bit", "but"), ("done", "fast"),
    ("dime", "but"), ("time", "one"), ("stuck", "somebody's"),
    ("done", "fast"), ("come", "pay"), ("roads", "toe"),
    ("done", "toe", 224.0), ("come", "toe"),
]


def strip_token(tok):
    m = re.match(r"^(.*?)([.,!?;:]*)$", tok)
    return m.group(1), m.group(2)


def cmp_form(tok):
    core, _ = strip_token(tok)
    return core.lower().strip("'")


def display(tok, line_start):
    core, punct = strip_token(tok)
    low = core.lower().strip("'")
    base = MAP.get(low, core)
    if low in MAP and core[:1].isupper() and line_start:
        base = base[:1].upper() + base[1:]
    elif not line_start and core[:1].isupper() and core[1:].islower():
        base = base[:1].lower() + base[1:]
    return base + punct


def esc(s):
    return s.replace("\\", "\\\\").replace("{", "\\{").replace("}", "\\}")


def fmt(t):
    t = max(0.0, t)
    h = int(t // 3600)
    m = int((t % 3600) // 60)
    s = t % 60
    return "%d:%02d:%05.2f" % (h, m, s)


def main():
    d = json.load(open(PROJ / "SONG_WORDS_BASE.json"))
    words = d["words"] if "words" in d else d
    words = sorted(words, key=lambda w: w["t0"])
    assert len(words) == 404
    # Preprocess zero-duration tokens.
    cap_words = []  # each: dict(t0, t1, word, prefix)
    excluded = []
    folded = []
    i = 0
    while i < len(words):
        w = words[i]
        if w["t1"] > w["t0"]:
            cap_words.append({"t0": w["t0"], "t1": w["t1"], "word": w["word"], "prefix": ""})
            i += 1
            continue
        # Zero-duration: find the run.
        j = i
        while j < len(words) and words[j]["t1"] <= words[j]["t0"]:
            j += 1
        run = words[i:j]
        if len(run) >= 2:
            excluded.extend(run)
        else:
            folded.append(run[0])
            # Fold into the next real word's prefix (applied at event build).
            nxt = words[j]
            cap_words.append({"t0": nxt["t0"], "t1": nxt["t1"], "word": nxt["word"],
                              "prefix": run[0]["word"] + " "})
            j += 1
        i = j
    print("excluded phantom tokens:", [(w["word"], w["t0"]) for w in excluded])
    print("folded tokens:", [(w["word"], w["t0"]) for w in folded])
    print("caption words:", len(cap_words))
    # Group into lines.
    lines = []
    cur = [cap_words[0]]
    fi = 0
    for a, b in zip(cap_words, cap_words[1:]):
        gap = b["t0"] - a["t1"]
        forced = False
        if fi < len(FORCED):
            entry = FORCED[fi]
            ok = (cmp_form(a["word"]), cmp_form(b["word"])) == (entry[0], entry[1])
            if ok and len(entry) > 2 and b["t0"] < entry[2]:
                ok = False
            if ok and gap <= 0.9:
                forced = True
        if gap > 0.9 or forced:
            lines.append(cur)
            cur = [b]
            if forced:
                fi += 1
        else:
            cur.append(b)
    lines.append(cur)
    assert fi == len(FORCED), "forced breaks consumed %d/%d" % (fi, len(FORCED))
    print("caption lines:", len(lines))
    for l in lines:
        txt = " ".join((w["prefix"] + display(w["word"], w is l[0])) for w in l)
        print(f"  {l[0]['t0']:7.2f}-{l[-1]['t1']:7.2f} ({len(l):2d}w) {txt}")
    # Events: one per caption word; text = full line, current word yellow.
    # A folded prefix highlights jointly with its word.
    events = []
    flat = [(w, li, wi) for li, l in enumerate(lines) for wi, w in enumerate(l)]
    for idx, (w, li, wi) in enumerate(flat):
        line = lines[li]
        parts = []
        for j, lw in enumerate(line):
            t = esc((lw["prefix"] if j == wi else "") + display(lw["word"], j == 0))
            if j == wi:
                t = "{\\1c&H0000FFFF&}" + t + "{\\1c&H00FFFFFF&}"
            parts.append(t)
        text = " ".join(parts)
        start = w["t0"] - 0.125
        if idx + 1 < len(flat):
            end = flat[idx + 1][0]["t0"] - 0.125
        else:
            end = w["t1"] + 0.3
        assert end > start, (w, start, end)
        events.append((start, end, text))
    for (s1, e1, _), (s2, e2, _) in zip(events, events[1:]):
        assert abs(e1 - s2) < 0.001, (e1, s2)
    header = """[Script Info]
ScriptType: v4.00+
PlayResX: 1280
PlayResY: 720
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: V6Line,DejaVu Sans,30,&H00FFFFFF,&H00FFFFFF,&H80000000,&H80000000,-1,0,0,0,100,100,0,0,3,2,0,2,60,60,36,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    body = "".join(
        "Dialogue: 0,%s,%s,V6Line,,0,0,0,,%s\n" % (fmt(s), fmt(e), t)
        for (s, e, t) in events)
    (WORK / "captions.ass").write_text(header + body)
    print("events:", len(events), "->", WORK / "captions.ass")


if __name__ == "__main__":
    main()
