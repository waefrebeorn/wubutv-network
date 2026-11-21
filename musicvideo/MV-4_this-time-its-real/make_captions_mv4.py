#!/usr/bin/env python3
"""MV-4 captions: line-block + per-word highlight (ASS), from performed words.

Adapted from MV-3 make_captions_mv3.py. Source of truth: LYRIC_TIMELINE.md
line table (performed text) + word times from SONG_WORDS.json. Karaoke
stepping only when the Whisper word count in the span equals the performed
word count, times are strictly increasing, and every duration > 0.05s;
otherwise the line gets a single sustained block event. L57 (soft repeat,
one long held line) is block-only. L29 ("No" dropped by Whisper) is
block-only by the count rule.
"""
import json, os

PROJ = os.path.dirname(os.path.abspath(__file__))

LINES = [
    ("L01", "They said it was over back in '03,", 0.00, 4.00),
    ("L02", "Then they said it again in twenty-thirteen.", 4.00, 7.70),
    ("L03", "Hulu hit rewind and we all leaned in,", 7.70, 11.70),
    ("L04", "Fourteen seasons later, we're still on the screen.", 11.70, 15.32),
    ("L05", "\"Final Ending: The Last Conclusion,\"", 16.00, 18.66),
    ("L06", "That's the label on the last file.", 19.76, 23.34),
    ("L07", "Matt said, \"we're not done yet,\"", 23.34, 26.44),
    ("L08", "But the streamer closed the door in style.", 26.44, 30.54),
    ("L09", "Futurama's finished, Futurama's finished,", 32.36, 35.42),
    ("L10", "For real this time, no more reruns in the dark.", 35.42, 39.72),
    ("L11", "Futurama's finished, Futurama's finished,", 39.72, 42.72),
    ("L12", "No fresh episodes, that's the hard part.", 42.72, 46.88),
    ("L13", "Good news, everyone\u2014 the ride is done,", 46.88, 50.26),
    ("L14", "Good news, everyone\u2014 the ship won't run.", 50.26, 54.20),
    ("L15", "Futurama's finished, Futurama's finished,", 54.20, 57.94),
    ("L16", "For real this time, no more reruns in the dark.", 57.94, 63.04),
    ("L17", "Three more specials lined up in twenty-seven,", 64.82, 68.70),
    ("L18", "Christmas first, then two more after.", 68.70, 72.04),
    ("L19", "But a whole new season?", 72.80, 74.74),
    ("L20", "Not on the board.", 74.74, 76.28),
    ("L21", "They sealed it up and walked out after.", 76.28, 79.52),
    ("L22", "We've seen this loop from Fox to cable,", 79.52, 83.22),
    ("L23", "Then streaming gave it one more round.", 83.22, 86.96),
    ("L24", "But this song's about the day they mean it,", 86.96, 90.74),
    ("L25", "When the last new line never comes down.", 90.74, 95.40),
    ("L26", "Futurama's finished, Futurama's finished,", 95.40, 99.24),
    ("L27", "For real this time, no more reruns in the dark.", 99.24, 103.36),
    ("L28", "Futurama's finished, Futurama's finished,", 103.36, 106.38),
    ("L29", "No fresh episodes, that's the hard part.", 106.62, 110.34),
    ("L30", "Good news, everyone\u2014 the ride is done,", 110.34, 113.88),
    ("L31", "Good news, everyone\u2014 the ship won't run.", 113.88, 117.96),
    ("L32", "Futurama's finished, Futurama's finished,", 117.96, 121.64),
    ("L33", "For real this time, no more reruns in the dark.", 121.64, 126.44),
    ("L34", "They always joke before the ending,", 126.44, 130.18),
    ("L35", "Like they can talk the credits back.", 130.46, 133.82),
    ("L36", "\"We'll rise again,\" he keeps on saying,", 133.82, 137.52),
    ("L37", "But the paperwork says otherwise.", 137.52, 140.56),
    ("L38", "You can binge the old ones on your couch,", 140.56, 144.64),
    ("L39", "Quote every line like muscle memory,", 144.64, 147.86),
    ("L40", "But the new ones stopped at the doorstep,", 148.40, 151.96),
    ("L41", "And the hallway stays empty.", 151.96, 155.16),
    ("L42", "Futurama's finished, Futurama's finished,", 158.76, 162.64),
    ("L43", "For real this time, no more reruns in the dark.", 162.64, 166.54),
    ("L44", "Futurama's finished, Futurama's finished,", 166.54, 169.72),
    ("L45", "No fresh episodes, that's the hard part.", 169.72, 173.90),
    ("L46", "Good news, everyone (good news, everyone),", 173.90, 177.12),
    ("L47", "The ride is done (the ride is done),", 177.12, 181.24),
    ("L48", "Good news, everyone (good news, everyone),", 181.24, 184.52),
    ("L49", "No more coming on.", 184.52, 187.46),
    ("L50", "Futurama's finished\u2026", 188.24, 190.22),
    ("L51", "Futurama's finished\u2026", 190.40, 194.06),
    ("L52", "For real this time\u2026", 194.06, 198.38),
    ("L53", "No more coming on.", 198.38, 204.72),
    ("L54", "No more coming on\u2026 No more coming on\u2026", 205.09, 210.75),
    ("L55", "Good news, everyone. Good news, everyone.", 211.75, 216.73),
    ("L56", "For real this time.", 217.75, 220.77),
    ("L57", "Good news, everyone. / For real this time. (repeat, soft)", 220.77, 238.03),
]
BLOCK_ONLY = {"L57"}

def ts(sec):
    h = int(sec // 3600); m = int((sec % 3600) // 60); s = sec % 60
    return f"{h}:{m:02d}:{s:05.2f}"

def ass_escape(t):
    return t.replace("\\", "\\\\").replace("{", "\\{").replace("}", "\\}")

def build(playres_x, playres_y, fontsize, margin_v, out_path):
    words = json.load(open(os.path.join(PROJ, "SONG_WORDS.json")))["words"]
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
    used = [False] * len(words)
    for lid, text, ls, le in LINES:
        toks = text.split(" ")
        cand = []
        for i, w in enumerate(words):
            if not used[i] and ls - 0.05 <= w["start"] < le:
                cand.append((i, w["word"], w["start"], w["end"]))
        ok = (len(cand) == len(toks) and lid not in BLOCK_ONLY
              and all(cand[k][2] < cand[k + 1][2] for k in range(len(cand) - 1))
              and all(c[3] - c[2] > 0.05 for c in cand))
        if ok:
            for c in cand:
                used[c[0]] = True
            for k, (i, wt, ws, we) in enumerate(cand):
                ev_start = ws
                ev_end = cand[k + 1][2] if k + 1 < len(cand) else le
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
    for s, e, t in events:
        out.append(f"Dialogue: 0,{ts(s)},{ts(e)},Cap,,0,0,0,,{t}")
    open(out_path, "w").write("\n".join(out) + "\n")
    for lid, mode, n in report:
        print(f"{lid}: {mode} ({n} words)")
    print(f"events: {len(events)} -> {out_path}")

if __name__ == "__main__":
    build(1280, 720, 44, 40, os.path.join(PROJ, "captions_16x9.ass"))
