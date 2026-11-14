#!/usr/bin/env python3
"""MV-3 captions: line-block + per-word highlight (ASS), from performed words.

Source of truth: LYRIC_TIMELINE.md line table (performed text) + word
times from SONG_WORDS.json. Whisper mishears (game=dad, dogs=hooks,
see=say) are normalized by POSITION: the nth Whisper word in a line's
span displays the nth performed word. Karaoke stepping is used only
when the Whisper word count in the span equals the performed word
count, times are strictly increasing, and every duration > 0.05s;
otherwise the line gets a single sustained block event (no fabricated
timing). Dense mantra lines (L26/L34/L38/L40 pile-ups) are block-only
by this rule. Mantra blocks display the base phrase once, sustained.
"""
import json, os

PROJ = os.path.dirname(os.path.abspath(__file__))

# (line, performed text, start, end)
LINES = [
    ("L01", "Listen, all of you", 2.82, 9.00),
    ("L02", "You already know, I am your dad", 9.32, 18.34),
    ("L03", "I been here the whole time, kid, looking right at you", 32.16, 35.72),
    ("L04", "Old man on the corner, old man in the room", 36.56, 39.74),
    ("L05", "You walk by, you scroll by, you turn the radio on", 40.06, 44.26),
    ("L06", "And the voice in the speaker says the same thing all along", 44.26, 47.60),
    ("L07", "I raised you in the dark, I raised you in the light", 48.12, 50.96),
    ("L08", "I raised every face that is listening tonight", 51.76, 54.38),
    ("L09", "You don't have to like it, you don't have to stay, but the words keep coming and they won't go away", 55.14, 62.20),
    ("L10", "I am your dad, I am your dad, say it with me", 62.64, 67.90),
    ("L11", "I am your dad, you're hearing once, you're hearing twice, now it lives inside", 68.36, 75.48),
    ("L12", "I am your dad, I am your dad, don't fight the feeling, I am your dad", 76.28, 82.90),
    ("L13", "I am your dad, I am your dad", 82.92, 87.50),
    ("L14", "You got your real one maybe, or maybe you don't", 90.66, 97.70),
    ("L15", "Matter to me, the message is the point", 98.50, 99.76),
    ("L16", "I walk through the speakers, brass hits on the one and the three", 99.68, 108.92),
    ("L17", "You try to skip it, but you try to change the song, but the phrase comes back and it doesn't take long", 108.92, 115.90),
    ("L18", "Short words, easy words, the kind that sticks fast, I am your dad, and the song will last", 116.14, 123.40),
    ("L19", "I am your dad, I am your dad, say it with me", 123.74, 128.90),
    ("L20", "I am your dad, you're hearing once, you're hearing twice, now it lives inside", 129.46, 135.80),
    ("L21", "I am your dad, I am your dad, I am your dad, say it with me", 136.52, 143.80),
    ("L22", "I am your dad, you're hearing twice, now it lives inside", 143.76, 149.10),
    ("L23", "I am your dad, I am your dad, I am your dad", 150.30, 159.50),
    ("L24", "I am your dad, I am your dad", 160.70, 166.50),
    ("L25", "You can close your eyes, you can plug your ears, the words still bounce around inside your head", 168.76, 182.12),
    ("L26", "I am your dad", 183.06, 191.94),
    ("L27", "I am your dad, I am your dad, I am your dad, I am your dad", 195.24, 214.90),
    ("L28", "They study the hooks, they study the loops, they say simple words", 215.40, 220.64),
    ("L29", "Make the brain stay true, repeat the same, I make it easy to sing, and the mind can play it on its own string", 220.64, 230.00),
    ("L30", "I don't need a story, I don't need a name, just the one short claim that never changes", 230.52, 236.80),
    ("L31", "You wake up tomorrow and the first thing you hear is the old man saying it crystal clear", 238.24, 245.10),
    ("L32", "I am your dad, I am your dad, say it with me", 245.10, 250.70),
    ("L33", "I am your dad, you're hearing once, you're hearing twice, now it lives inside", 251.04, 258.32),
    ("L34", "I am your dad", 258.32, 287.80),
    ("L35", "I am your dad, I am your dad, just a low voice", 287.80, 296.00),
    ("L36", "I am your dad, I am your dad, I am your dad, I am your dad", 296.70, 308.56),
    ("L37", "All of you, every single one, I am your dad, you know it now", 309.88, 321.44),
    ("L38", "I am your dad", 322.08, 338.44),
    ("L39", "Say it back to me, I am your dad, say it to yourself", 338.55, 343.91),
    ("L40", "I am your dad", 344.55, 353.71),
]
MANTRA_BLOCK = {"L26", "L34", "L38", "L40"}

def ts(sec):
    h = int(sec // 3600); m = int((sec % 3600) // 60); s = sec % 60
    return f"{h}:{m:02d}:{s:05.2f}"

def ass_escape(t):
    return t.replace("\\", "\\\\").replace("{", "\\{").replace("}", "\\}")

def build(playres_x, playres_y, fontsize, margin_v, out_path):
    words = json.load(open(os.path.join(PROJ, "SONG_WORDS.json")))["words"]
    used = [False] * len(words)
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
        # tokenize keeping commas attached
        toks = text.split(" ")
        cand = []
        for i, (wt, ws, we) in enumerate(words):
            if not used[i] and ls - 0.05 <= ws < le:
                cand.append((i, wt, ws, we))
        ok = (len(cand) == len(toks) and lid not in MANTRA_BLOCK
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
            reason = "mantra-block" if lid in MANTRA_BLOCK else (
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
    build(720, 1280, 46, 140, os.path.join(PROJ, "captions_9x16.ass"))
