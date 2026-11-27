#!/usr/bin/env python3
"""MV-29 karaoke captions. Adapted from MV-28's build_captions.py.
Text authority = lyrics_user_sheet.txt; timing authority =
SONG_WORDS.json. Slot selection is START-based (a word belongs to
the line whose span contains its start) so back-to-back lines do
not leak into each other. Segmentation is a small DP: atoms are
matched onto the sheet words by concatenation (hyphen splits like
white + collar merge), atoms under 0.05s are skippable decoder
junk (the doubled zero-duration echo tokens at 94.06), with three
documented tolerances, all ASR-side only (display text is always
the sheet):
 - plural-s: atom "lies" matches sheet "lie" (L13/L25);
 - atom "and" matches sheet "then" (L05/L17/L23/L41 — Whisper's
   word tokens hear "and" where segment ASR + sheet read "then");
 - MISHEAR relabels: toss->talks (L41), while->huang + hes->is
   (L43 "While he's gone" for "Huang is gone").
A line gets REAL word timings on a full segmentation, or on a
PREFIX segmentation when trailing atoms are backing echoes (L25).
Otherwise syllable-weight split across the line span.
Expected syllable-split fallbacks (disclosed in GATE_LOG):
L29 (song ASR hears a hook repeat; sheet line captioned),
L33-L38 (breakdown, ASR silent, display-derived spans),
L40 (ASR merged both final-chorus hooks into one stretched
"Room" token 145.64-150.60; L39 keeps real timings with the
sustain event clamped to its line end)."""
import json, os, re, sys
from functools import lru_cache

P = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SW = os.path.join(P, "work/swing")
SONG = json.load(open(os.path.join(P, "SONG_WORDS.json")))
HOOK = "Dario belongs in the rubber room"
TALKS = "Talks the doom then he takes the cash"
HUANG = "Huang is gone and the IPO flash"
LINES = [
 ("Rubber room", 0.00, 2.32),
 ("Yeah", 2.32, 2.92),
 (HOOK, 3.52, 6.30),
 (HOOK, 7.38, 10.08),
 (TALKS, 10.08, 13.28),
 (HOOK, 13.28, 16.98),
 (HUANG, 16.98, 20.88),
 (HOOK, 21.62, 24.78),
 ("Yeah!", 24.78, 25.28),
 ("Rubber, rubber room", 28.00, 29.70),
 ("Left the old team for the safety line", 32.80, 36.60),
 ("Half the jobs gone in a short short time", 36.60, 40.48),
 ("Law and finance, the white-collar fall", 40.48, 44.42),
 ("Huang said only they should do it all", 44.42, 47.82),
 ("Outrageous lie but the race stays hot", 47.82, 51.32),
 ("China chips and the nuclear talk", 52.24, 57.36),
 (HOOK, 58.76, 62.12),
 (HOOK, 62.12, 66.00),
 (TALKS, 66.00, 70.34),
 (HOOK, 70.34, 73.86),
 (HUANG, 73.86, 77.90),
 (HOOK, 77.90, 81.82),
 ("Hey!", 81.82, 82.28),
 ("Pentagon call and the deal went cold", 82.42, 84.28),
 ("No mass watch and the weapons hold", 84.28, 86.12),
 ("Then the board met and the Huang went down", 86.12, 88.16),
 ("Spy reports and the staff went round", 88.16, 90.02),
 ("Outrageous lie but the race stays hot", 90.02, 94.10),
 ("China chips and the nuclear talk", 94.10, 96.66),
 (HOOK, 102.08, 105.22),
 (HOOK, 105.22, 109.18),
 (TALKS, 109.18, 113.30),
 (HOOK, 114.10, 116.98),
 (HUANG, 116.98, 121.16),
 (HOOK, 123.40, 127.36),
 ("Rubber room", 127.36, 131.00),
 ("Huang is gone", 131.00, 133.00),
 ("Rubber room", 133.00, 135.00),
 ("Takes the cash", 135.00, 136.50),
 ("Talks the doom", 136.50, 138.00),
 ("IPO flash", 138.00, 142.86),
 (HOOK, 142.86, 147.00),
 (HOOK, 147.00, 150.60),
 (TALKS, 150.60, 154.58),
 (HOOK, 154.58, 158.22),
 (HUANG, 158.22, 162.18),
 (HOOK, 164.72, 168.56),
 ("Yeah", 168.56, 169.38),
 ("Rubber room", 169.38, 172.78),
 ("Rubber room", 172.90, 173.76),
 ("Rubber room", 173.76, 174.74),
 ("Rubber room", 174.74, 176.70),
 ("Rubber room", 176.88, 177.86),
 ("Rubber room", 177.86, 179.76),
 ("Rubber room", 183.08, 184.66),
]
def words(text): return [w for w in re.split(r"[\s,]+", text) if w]
def norm(w): return re.sub(r"[^a-z]", "", w.lower())
MISHEAR = {"toss": "talks", "while": "huang", "hes": "is"}
def atom_norm(w): return MISHEAR.get(norm(w), norm(w))
def syllables(w):
    w = re.sub(r"[^a-z]", "", w.lower())
    if not w: return 1
    n = len(re.findall(r"[aeiouy]+", w))
    if w.endswith("e") and n > 1 and not w.endswith(("le", "ee", "ye")): n -= 1
    return max(1, n)

def try_segment(atoms, targets, allow_leftover):
    A = [(atom_norm(w["word"]), w["start"], w["end"]) for w in atoms]
    T = list(targets)
    def matches(acc, t):
        return (acc == t or acc + "s" == t or acc == t + "s"
                or (acc == "and" and t == "then"))
    def cont(acc, t):
        return t.startswith(acc) or acc.startswith(t)
    sys.setrecursionlimit(10000)
    @lru_cache(maxsize=None)
    def go(i, j):
        if j == len(T):
            if allow_leftover: return ()
            if all(A[k][2] - A[k][1] < 0.05 for k in range(i, len(A))):
                return ()
            return None
        t = T[j]
        def walk(k, acc, st):
            if k >= len(A): return None
            dur = A[k][2] - A[k][1]
            if acc == "" and dur < 0.05:
                r = walk(k + 1, acc, st)
                if r is not None: return r
            nacc = acc + A[k][0]
            nst = A[k][1] if st is None else st
            if matches(nacc, t):
                rest = go(k + 1, j + 1)
                if rest is not None: return ((nst, A[k][2]),) + rest
            if cont(nacc, t):
                return walk(k + 1, nacc, nst)
            return None
        return walk(i, "", None)
    r = go(0, 0)
    return list(r) if r is not None else None

def ts_ass(t):
    h = int(t // 3600); m = int((t % 3600) // 60); s = t % 60
    return f"{h}:{m:02d}:{s:05.2f}"
def ts_srt(t):
    h = int(t // 3600); m = int((t % 3600) // 60); s = t % 60
    return f"{h:02d}:{m:02d}:{s:06.3f}".replace(".", ",")

events, srt, fallback = [], [], []
for li, (text, ls, le) in enumerate(LINES):
    ws = words(text)
    targets = [norm(w) for w in ws]
    atoms = [w for w in SONG if ls - 0.05 <= w["start"] < le - 0.05]
    spans = try_segment(atoms, targets, False) or try_segment(atoms, targets, True)
    if spans is None:
        fallback.append((li + 1, text, len(atoms), len(ws)))
        tot = sum(syllables(w) for w in ws); dur = le - ls; t = ls; spans = []
        for w in ws:
            d = dur * syllables(w) / tot; spans.append((t, t + d)); t += d
    for wi, w in enumerate(ws):
        a, b = spans[wi]
        b = min(b, le + 0.30)
        disp = " ".join(
            ("{\\1c&H0000FFFF&}" + x + "{\\1c&H00FFFFFF&}") if j == wi else x
            for j, x in enumerate(ws))
        events.append((a, max(b, a + 0.12), disp))
    nxt = LINES[li + 1][1] if li + 1 < len(LINES) else le + 1.0
    srt.append((ls, min(spans[-1][1] + 0.30, nxt), text))

hdr = """[Script Info]
ScriptType: v4.00+
PlayResX: 1280
PlayResY: 720
ScaledBorderAndShadow: yes
WrapStyle: 2

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: V6Line,DejaVu Sans,30,&H00FFFFFF,&H0000FFFF,&H00000000,&H96000000,-1,0,0,0,100,100,0,0,3,1,0,2,40,40,36,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
with open(os.path.join(SW, "captions_karaoke.ass"), "w") as f:
    f.write(hdr)
    for a, b, disp in events:
        f.write(f"Dialogue: 0,{ts_ass(a)},{ts_ass(b)},V6Line,,0,0,0,,{disp}\n")
with open(os.path.join(SW, "lyrics.srt"), "w") as f:
    for i, (a, b, text) in enumerate(srt, 1):
        f.write(f"{i}\n{ts_srt(a)} --> {ts_srt(b)}\n{text}\n\n")
print(f"lines: {len(LINES)}  word events: {len(events)}  srt cues: {len(srt)}")
for fb in fallback: print("FALLBACK (syllable split):", fb)
