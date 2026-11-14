#!/usr/bin/env python3
"""MV-5 v2 captions: line-block + per-word highlight (ASS), from the v2 grid.

Adapted from make_captions_mv5.py (v1). Differences from v1:
- Word times: work/gemini_song_words_aligned.json — app_start/app_end where
  the app matched the word, v1 song_start/song_end where the app dropped it
  ("word STARTS from the app, line spans from v1").
- Line texts/spans: work/LYRIC_TIMELINE_V2.md. Changed vs v1: L49 'Here for
  the boardwalks', L51 'You took my sneakers from me once', L52 'Like none
  of it was last', L108 'This is now' x3, L110 split into L110a (CAT, 201.0)
  + L110b (GIRL, 204.2). L107 DROPPED (no sung words 187-194.1) — no event.
- L56: the held final word 'replays' is at 119.5 (app 'replaced.' extra),
  so L56 karaoke runs And 116.2 / my 116.3 / whole 116.4 / head 116.5 /
  replays 119.5-120.02. The 'head' highlight therefore spans 116.5-119.5
  (held-note artifact of the burst-compressed app times — disclosed).
  No separate L56b event (v1's 'We fly...' is superseded).
- L108: 9 app tokens with a duplicate time (194.6 twice) -> block 194.1-197.58.
- L109: performed 2x 'Easy now' vs app 3x tokens -> block 197.58-203.42
  (clamp cuts it at L110a's 201.0 start).
- L110a: block 201.0-203.42. L110b: karaoke (app times, 4 words, clean).
- L51: 'You' and 'took' share start 109.9 (zero duration) -> block.
- L52: karaoke (6 words, all durations >0.05).
Output: captions_16x9_v2.ass (1280x720, same style as v1).
"""
import json, os

PROJ = os.path.dirname(os.path.abspath(__file__))
ALIGNED = json.load(open(os.path.join(PROJ, "work", "gemini_song_words_aligned.json")))["rows"]

# (line id, display text, span start, span end)
LINES = [
    ("I01", "Easy now, easy now", 1.66, 3.82),
    ("I02", "We ride, we ride", 3.82, 5.98),
    ("I03", "Easy now, easy now", 5.98, 8.01),
    ("I04", "Till the morning comes", 8.01, 10.04),
    ("I05", "Easy now, easy now", 10.04, 12.72),
    ("I06", "We ride, we ride", 12.72, 15.40),
    ("I07", "Easy now, easy now", 15.40, 17.02),
    ("I08", "Till the morning comes", 17.02, 18.64),
    ("I09", "Ta-da, ta-da, ta-da, ta-da, ta-da, ta-da", 18.64, 22.00),
    ("L01", "Bare feet on the boardwalk", 22.00, 23.42),
    ("L02", "Salt on my skin", 23.42, 24.60),
    ("L03", "You came in laughing", 24.60, 26.76),
    ("L04", "Said, come on, let's begin", 27.76, 29.60),
    ("L05", "Blue shirt, red bicycle", 29.60, 31.48),
    ("L06", "Rolling past the pier", 31.48, 33.62),
    ("L07", "I was posted up right here", 33.62, 36.14),
    ("L08", "Now you're pulling near", 36.14, 38.48),
    ("L09", "Backpack half-zipped", 38.48, 40.44),
    ("L10", "Keys in your hand", 40.44, 42.82),
    ("L11", "You nodded at the waves like", 42.82, 44.58),
    ("L12", "Yeah, they already understand", 44.58, 46.86),
    ("L13", "Slow down, take your time", 47.76, 49.60),
    ("L14", "Let the hard week fade", 49.60, 51.46),
    ("L15", "One small look from you", 51.46, 52.80),
    ("L16", "And my whole head replays", 52.80, 56.50),
    ("L17", "Easy now, easy now", 57.52, 59.10),
    ("L18", "We ride, we ride", 59.10, 60.22),
    ("L19", "Easy now, easy now", 60.22, 61.34),
    ("L20", "With you by my side", 61.34, 62.52),
    ("L21", "Easy now, easy now", 62.52, 63.66),
    ("L22", "No need to run", 63.66, 64.92),
    ("L23", "Easy now, easy now", 64.92, 65.96),
    ("L24", "We hold the sun", 65.96, 67.06),
    ("L25", "Easy now, easy now", 67.06, 68.20),
    ("L26", "Keep it loose, keep it low", 68.20, 69.40),
    ("L27", "Easy now, easy now", 69.40, 70.46),
    ("L28", "Let it drift, let it go", 70.46, 71.66),
    ("L29", "Easy now, easy now", 71.66, 72.74),
    ("L30", "We're good where we are", 72.74, 74.02),
    ("L31", "Easy now, easy now", 74.02, 75.04),
    ("L32", "Just two small sparks", 75.04, 76.80),
    ("L33", "I gotta go there", 76.80, 78.76),
    ("L34", "I gotta go there, just two small sparks", 78.76, 81.76),
    ("L35", "I gotta go there", 81.76, 83.14),
    ("L36", "Just two small sparks", 83.14, 85.20),
    ("L37", "Vendor at the corner", 85.20, 87.00),
    ("L38", "Calling mango sweet", 87.00, 87.60),
    ("L39", "Socks in the sand", 87.60, 88.92),
    ("L40", "And the tide tapping time with our feet", 88.92, 93.00),
    ("L41", "Your laugh hit the air", 93.80, 95.12),
    ("L42", "Like a hand drum roll", 95.80, 96.84),
    ("L43", "I forgot the list, forgot the bills", 96.84, 98.44),
    ("L44", "Forgot what I was told", 98.44, 102.40),
    ("L45", "Ice cup sweating", 102.40, 103.80),
    ("L46", "On the rail by the steps", 103.80, 104.72),
    ("L47", "You said, don't think too hard", 104.72, 106.42),
    ("L48", "So I didn't, not yet", 106.42, 107.52),
    ("L49", "Here for the boardwalks", 107.52, 108.72),
    ("L50", "Cutting through the crowd", 108.72, 109.74),
    ("L51", "You took my sneakers from me once", 109.74, 110.70),
    ("L52", "Like none of it was last", 110.70, 111.90),
    ("L53", "Slow down, take your time", 111.90, 113.78),
    ("L54", "Let the hard week fade", 113.78, 114.94),
    ("L55", "One small look from you", 114.94, 116.00),
    ("L56", "And my whole head replays", 116.00, 120.02),  # span incl. held
    # tail word 'replays' @119.5 (L56b window); v1 span ended 118.28, which
    # would clamp-drop the replays event entirely.
    ("L57", "Easy now, easy now", 121.26, 122.58),
    ("L58", "We ride, we ride", 122.58, 124.00),
    ("L59", "Easy now, easy now", 124.00, 125.06),
    ("L60", "With you by my side", 125.06, 126.30),
    ("L61", "Easy now, easy now", 126.30, 127.38),
    ("L62", "No need to run", 127.38, 128.52),
    ("L63", "Easy now, easy now", 128.52, 129.66),
    ("L64", "We hold the sun", 129.66, 130.78),
    ("L65", "Easy now, easy now", 130.78, 131.88),
    ("L66", "Keep it loose, keep it low", 131.88, 133.08),
    ("L67", "Easy now, easy now", 133.08, 134.18),
    ("L68", "Let it drift, let it go", 134.18, 135.36),
    ("L69", "Easy now, easy now", 135.36, 136.44),
    ("L70", "We're good where we are", 136.44, 137.62),
    ("L71", "Easy now, easy now", 137.62, 138.82),
    ("L72", "Just two small sparks", 138.82, 140.52),
    ("L73a", "I'm falling, I'm falling", 140.52, 143.14),
    ("L73b", "Just two small sparks", 143.14, 145.56),
    ("L73c", "I'm falling", 145.56, 146.62),
    ("L73d", "Just two small sparks", 146.62, 148.70),
    ("L74", "If the rain comes down", 148.70, 150.00),
    ("L75", "We stay out in it", 150.00, 151.30),
    ("L76", "If the day runs long", 151.30, 152.36),
    ("L77", "We still move with it", 152.36, 153.58),
    ("L78", "Hand in my hand", 153.58, 154.42),
    ("L79", "No speech, no show", 154.42, 155.72),
    ("L80", "Heart in the breeze", 155.72, 156.70),
    ("L81", "And the bass move slow", 156.70, 158.06),
    ("L82", "If the sky turns gray", 158.06, 159.10),
    ("L83", "We don't fold in", 159.10, 160.24),
    ("L84", "We lean right back", 160.24, 161.36),
    ("L85", "Let the whole thing spin", 161.36, 162.46),
    ("L86", "You and me, same pace", 162.46, 163.58),
    ("L87", "Same worn-in shoes", 163.58, 164.90),
    ("L88", "Nothing to prove", 164.90, 165.88),
    ("L89", "Nothing to lose", 165.88, 167.50),
    ("L90", "No, no, no", 167.50, 169.16),
    ("L91", "Easy now, easy now", 169.16, 170.18),
    ("L92", "We ride, we ride", 170.18, 171.44),
    ("L93", "Easy now, easy now", 171.44, 172.58),
    ("L94", "With you by my side", 172.58, 173.62),
    ("L95", "Easy now, easy now", 173.62, 174.92),
    ("L96", "No need to run", 174.92, 176.04),
    ("L97", "Easy now, easy now", 176.04, 177.20),
    ("L98", "We hold the sun", 177.20, 178.24),
    ("L99", "Easy now, easy now", 178.24, 179.30),
    ("L100", "Keep it loose, keep it low", 179.30, 180.50),
    ("L101", "Easy now, easy now", 180.50, 181.56),
    ("L102", "Let it drift, let it go", 181.56, 182.78),
    ("L103", "Easy now, easy now", 182.78, 183.80),
    ("L104", "We're good where we are", 183.80, 185.02),
    ("L105", "Easy now, easy now", 185.02, 186.46),
    ("L106", "Just two small sparks", 186.46, 188.04),
    # L107 DROPPED in v2 (no sung words 187-194.1) — no event.
    ("L108", "This is now, this is now, this is now", 194.10, 197.58),
    ("L109", "Easy now, easy now", 197.58, 203.42),
    ("L110a", "Till the morning comes", 201.00, 203.42),
    ("L110b", "Till the morning comes", 203.42, 205.58),
]

# Hand-specified word times for lines whose v2 text differs from the v1
# song rows (app times from LYRIC_TIMELINE_V2.md + aligned EXTRA rows).
# Format: line -> [(word, start, end), ...]
WORD_OVERRIDE = {
    "L49": [("Here", 107.8, 107.9), ("for", 107.9, 108.0),
            ("the", 108.0, 108.1), ("boardwalks.", 108.1, 108.72)],
    "L51": [("You", 109.9, 109.9), ("took", 109.9, 110.0), ("my", 110.0, 110.2),
            ("sneakers", 110.2, 110.4), ("from", 110.4, 110.6),
            ("me", 110.6, 110.7), ("once", 110.7, 110.70)],
    "L52": [("Like", 110.9, 111.0), ("none", 111.0, 111.2), ("of", 111.2, 111.3),
            ("it", 111.3, 111.5), ("was", 111.5, 111.7), ("last.", 111.7, 111.90)],
    "L56": [("And", 116.2, 116.3), ("my", 116.3, 116.4), ("whole", 116.4, 116.5),
            ("head", 116.5, 116.6), ("replays", 119.5, 120.02)],
    "L108": [("This", 194.1, 194.2), ("is", 194.2, 194.3), ("now,", 194.3, 194.4),
             ("this", 194.4, 194.5), ("is", 194.5, 194.6), ("now,", 194.6, 194.6),
             ("this", 194.6, 194.7), ("is", 194.7, 194.8), ("now.", 194.8, 194.9)],
    "L109": None,   # block (app 3x tokens vs performed 2x)
    "L110a": [("Till", 201.0, 201.1), ("the", 201.1, 201.1),
              ("morning", 201.1, 201.3), ("comes.", 201.3, 201.4)],
    "L110b": [("Till", 204.2, 204.3), ("the", 204.3, 204.4),
              ("morning", 204.4, 205.3), ("comes.", 205.3, 205.8)],
}
BLOCK_ONLY = {"L108", "L109", "L110a", "L51"}

def ts(sec):
    h = int(sec // 3600); m = int((sec % 3600) // 60); s = sec % 60
    return f"{h}:{m:02d}:{s:05.2f}"

def ass_escape(t):
    return t.replace("\\", "\\\\").replace("{", "\\{").replace("}", "\\}")

def build(playres_x, playres_y, fontsize, margin_v, out_path):
    # word times per line from the aligned grid: app times where matched,
    # v1 song times where the app dropped the word.
    by_line = {}
    for r in ALIGNED:
        if r.get("status") == "EXTRA" or r.get("line") is None:
            continue
        if r.get("app_start") is not None:
            by_line.setdefault(r["line"], []).append(
                (r["app_word"], r["app_start"], r["app_end"]))
        else:
            by_line.setdefault(r["line"], []).append(
                (r["song_word"], r["song_start"], r["song_end"]))
    for lid in by_line:
        by_line[lid].sort(key=lambda c: c[1])
    header = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {playres_x}
PlayResY: {playres_y}
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,DejaVu Sans,{fontsize},&H00FFFFFF,&H001EC6FF,&H80000000,&H80000000,-1,0,0,0,100,100,0,0,1,3,0,2,40,40,{margin_v},1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    events = []
    report = []
    for lid, text, ls, le in LINES:
        toks = text.split(" ")
        if lid in WORD_OVERRIDE:
            cand = WORD_OVERRIDE[lid]
        else:
            cand = [(w, s, e) for (w, s, e) in by_line.get(lid, [])]
        ok = (cand is not None and len(cand) == len(toks)
              and lid not in BLOCK_ONLY
              and all(cand[k][1] < cand[k + 1][1] for k in range(len(cand) - 1))
              and all(c[2] - c[1] > 0.05 for c in cand))
        if ok:
            for k, (wt, ws, we) in enumerate(cand):
                ev_start = ws
                ev_end = cand[k + 1][1] if k + 1 < len(cand) else le
                ev_end = min(ev_end, le)
                parts = []
                for j, tok in enumerate(toks):
                    if j == k:
                        parts.append("{\\1c&H1EC6FF&}" + ass_escape(tok) + "{\\r}")
                    else:
                        parts.append(ass_escape(tok))
                events.append((ev_start, ev_end, " ".join(parts)))
            report.append((lid, "karaoke", len(toks)))
        else:
            events.append((ls, le, ass_escape(text)))
            reason = "block-only" if lid in BLOCK_ONLY else (
                f"count grid={len(cand) if cand else 0} perf={len(toks)}")
            report.append((lid, "block:" + reason, len(toks)))
    out = [header]
    events.sort(key=lambda e: (e[0], e[1]))
    fixed = []
    for i, (s, e, t) in enumerate(events):
        if i + 1 < len(events):
            e = min(e, events[i + 1][0])
        if e > s:
            fixed.append((s, e, t))
    n_dropped = len(events) - len(fixed)
    for (s, e, t) in events:
        if not any(fs == s and fe == e and ft == t for (fs, fe, ft) in fixed):
            print(f"DROPPED event: {ts(s)}-{ts(e)} {t[:60]}")
    for s, e, t in fixed:
        out.append(f"Dialogue: 0,{ts(s)},{ts(e)},Cap,,0,0,0,,{t}")
    open(out_path, "w").write("\n".join(out) + "\n")
    for lid, mode, n in report:
        print(f"{lid}: {mode} ({n} words)")
    print(f"events: {len(fixed)} (dropped {n_dropped} zero-length) -> {out_path}")

if __name__ == "__main__":
    build(1280, 720, 44, 40, os.path.join(PROJ, "captions_16x9_v2.ass"))
