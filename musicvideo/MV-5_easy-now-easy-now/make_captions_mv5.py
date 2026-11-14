#!/usr/bin/env python3
"""MV-5 captions: line-block + per-word highlight (ASS), from performed words.

Adapted from MV-4 make_captions_mv4.py. Source of truth: LYRIC_TIMELINE.md
line table (performed text) + word times from SONG_WORDS.json. Words are
selected by their line id (SONG_WORDS.json carries one), not by a time
window — several lines' word times jitter outside the line-table window
(L56 words start 115.74 vs line 116.00; I09 first "ta-da" at 18.40 vs
line 18.64). Karaoke stepping only when the Whisper word count equals the
performed word count, times are strictly increasing, and every duration >
0.05s; otherwise the line gets a single sustained block event.
Display-text exceptions: I09 "Ta-da, ta-da, ta-da, ta-da, ta-da, ta-da"
(6x, matches the take); L56b "We fly..." (per LYRIC_TIMELINE, "'We fly'
heard"); L90 "No, no, no".
"""
import json, os

PROJ = os.path.dirname(os.path.abspath(__file__))

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
    ("L49", "Kids with a boombox", 107.52, 108.72),
    ("L50", "Cutting through the crowd", 108.72, 109.74),
    ("L51", "You took my sleeve and spun me once", 109.74, 110.70),
    ("L52", "Like none of it was loud", 110.70, 111.90),
    ("L53", "Slow down, take your time", 111.90, 113.78),
    ("L54", "Let the hard week fade", 113.78, 114.94),
    ("L55", "One small look from you", 114.94, 116.00),
    ("L56", "And my whole head replays", 116.00, 118.28),
    ("L56b", "We fly\u2026", 119.30, 120.02),
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
    ("L107", "Easy now, easy now", 190.42, 194.72),
    ("L108", "We ride, we ride", 194.72, 197.58),
    ("L109", "Easy now, easy now", 197.58, 203.42),
    ("L110", "Till the morning comes", 203.42, 205.58),
]
BLOCK_ONLY = {"L56b"}

def ts(sec):
    h = int(sec // 3600); m = int((sec % 3600) // 60); s = sec % 60
    return f"{h}:{m:02d}:{s:05.2f}"

def ass_escape(t):
    return t.replace("\\", "\\\\").replace("{", "\\{").replace("}", "\\}")

def build(playres_x, playres_y, fontsize, margin_v, out_path):
    words = json.load(open(os.path.join(PROJ, "SONG_WORDS.json")))["words"]
    by_line = {}
    for w in words:
        by_line.setdefault(w["line"], []).append(w)
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
        cand = [(w["word"], w["start"], w["end"]) for w in by_line.get(lid, [])]
        cand.sort(key=lambda c: c[1])
        ok = (len(cand) == len(toks) and lid not in BLOCK_ONLY
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
                f"count whisper={len(cand)} perf={len(toks)}")
            report.append((lid, "block:" + reason, len(toks)))
    out = [header]
    # Clamp: no two events may overlap (Whisper word times jitter across
    # line boundaries, e.g. a line's last word ends after the next line's
    # first word starts). Sort by start, cut each event's end at the next
    # event's start, drop events that collapse to zero length.
    events.sort(key=lambda e: (e[0], e[1]))
    fixed = []
    for i, (s, e, t) in enumerate(events):
        if i + 1 < len(events):
            e = min(e, events[i + 1][0])
        if e > s:
            fixed.append((s, e, t))
    n_dropped = len(events) - len(fixed)
    for s, e, t in fixed:
        out.append(f"Dialogue: 0,{ts(s)},{ts(e)},Cap,,0,0,0,,{t}")
    open(out_path, "w").write("\n".join(out) + "\n")
    for lid, mode, n in report:
        print(f"{lid}: {mode} ({n} words)")
    print(f"events: {len(fixed)} (dropped {n_dropped} zero-length) -> {out_path}")

if __name__ == "__main__":
    build(1280, 720, 44, 40, os.path.join(PROJ, "captions_16x9.ass"))
