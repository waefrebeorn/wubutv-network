#!/usr/bin/env python3
"""MV-5 lyrics redo — arbitrate disputed WORD CONTENT across all sources.

Sources: OLD grid (SONG_WORDS.json), NOPROMPT base pass,
P1 (turbo, repeat suppression ON), P2 (turbo, suppression OFF),
GEMINI aligned rows (work/gemini_song_words_aligned.json: app_word).
For each disputed span, print what each source hears.
"""
import json

PROJ = "/home/hatch/workspace/wubutv-network/musicvideo/MV-5_easy-now-easy-now"

def load_words(path, key=None):
    d = json.load(open(path))
    if key:
        return d[key]
    if "words" in d:
        return d["words"]
    ws = []
    for s in d.get("segments", []):
        ws += s.get("words", [])
    return ws

old = load_words(PROJ + "/SONG_WORDS.json")
nop = load_words(PROJ + "/work/song_transcript_noprompt.json")
p1 = load_words(PROJ + "/work/lyrics-redo/words_full_v3turbo.json")
p2 = load_words(PROJ + "/work/lyrics-redo/words_full_v3turbo_norepeat.json")
gem = json.load(open(PROJ + "/work/gemini_song_words_aligned.json"))["rows"]

def span_words(ws, t0, t1):
    return " ".join(w["word"].strip() for w in ws if t0 <= w["start"] < t1)

def gem_span(t0, t1):
    rs = [r for r in gem if r.get("app_start") is not None and t0 <= r["app_start"] < t1]
    if not rs:
        rs = [r for r in gem if r.get("song_start") is not None and t0 <= r["song_start"] < t1]
        return " ".join(r.get("song_word", "") for r in rs) + "  (song-side)"
    return " ".join(r.get("app_word", "") for r in rs)

SPANS = [
    ("L02 Salt on my skin", 23.42, 24.60),
    ("L09 Backpack half-zipped", 38.48, 40.44),
    ("L14 hard week fade", 49.60, 51.46),
    ("L16 replays", 52.80, 56.50),
    ("L33-36 I gotta go there tags", 76.80, 85.20),
    ("L45 Ice cup sweating", 102.40, 103.80),
    ("L48 So I didn't, not yet", 106.42, 107.52),
    ("L52 Like none of it was loud", 110.70, 111.90),
    ("L73a/c I'm falling tags", 140.52, 148.70),
    ("L78 Hand in my hand", 153.58, 154.42),
    ("L81 bass move slow", 156.70, 158.06),
    ("L83 We don't fold in", 159.10, 160.24),
    ("L87 Same worn-in shoes", 163.58, 164.90),
    ("L90 No, no, no ad-lib", 167.50, 169.16),
    ("L100 Keep it loose, keep it low", 179.30, 180.50),
    ("L102 Let it drift", 181.56, 182.78),
    ("L106 Just two small sparks", 186.46, 188.04),
    ("L107 span (artifact?)", 187.0, 194.5),
    ("L108-110 tail", 194.52, 205.58),
    ("I09 ta-da vocalise", 18.64, 22.00),
]
for label, t0, t1 in SPANS:
    print(f"--- {label} ({t0}-{t1}s) ---")
    print(f"  OLD : {span_words(old, t0, t1)}")
    print(f"  NOP : {span_words(nop, t0, t1)}")
    print(f"  P1  : {span_words(p1, t0, t1)}")
    print(f"  P2  : {span_words(p2, t0, t1)}")
    print(f"  GEM : {gem_span(t0, t1)}")
