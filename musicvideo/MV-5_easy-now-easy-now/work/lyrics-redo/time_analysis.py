#!/usr/bin/env python3
"""MV-5 lyrics redo — TIME analysis: per-word offsets old vs P1 vs noprompt.

For each old-grid word, find the same word (case-folded, punctuation-stripped)
in P1 and in noprompt within +-2.0s and report dt(P1-old), dt(NOP-old), dt(P1-NOP).
Group by section to find the systematic offset pattern.
"""
import json, re

PROJ = "/home/hatch/workspace/wubutv-network/musicvideo/MV-5_easy-now-easy-now"

def norm(w):
    return re.sub(r"[^a-z0-9']", "", w.lower())

def load_words(path):
    d = json.load(open(path))
    if "words" in d:
        return d["words"]
    ws = []
    for s in d.get("segments", []):
        ws += s.get("words", [])
    return ws

old = load_words(PROJ + "/SONG_WORDS.json")
nop = load_words(PROJ + "/work/song_transcript_noprompt.json")
p1 = load_words(PROJ + "/work/lyrics-redo/words_full_v3turbo.json")

def nearest(ws, word, t, win=2.0):
    best, bd = None, 1e9
    for w in ws:
        if norm(w["word"]) != norm(word):
            continue
        d = abs(w["start"] - t)
        if d < bd and d <= win:
            bd, best = d, w
    return best

SECTIONS = [
    ("Intro", 0, 22.0), ("Verse1", 22.0, 56.0), ("Chorus1", 56.0, 85.2),
    ("Verse2", 85.2, 120.6), ("Chorus2", 120.6, 148.7),
    ("Bridge", 148.7, 169.0), ("Final", 169.0, 206.4),
]
rows = []
for w in old:
    t = w["start"]
    a = nearest(p1, w["word"], t)
    b = nearest(nop, w["word"], t)
    if a is None and b is None:
        continue
    rows.append((t, w["word"],
                 (a["start"] - t) if a else None,
                 (b["start"] - t) if b else None,
                 ((a["start"] - b["start"]) if (a and b) else None)))
print(f"old words with a P1 or NOP match: {len(rows)} / {len(old)}")
for name, t0, t1 in SECTIONS:
    sub = [r for r in rows if t0 <= r[0] < t1]
    import statistics as st
    d1 = [r[2] for r in sub if r[2] is not None]
    d2 = [r[3] for r in sub if r[3] is not None]
    d3 = [r[4] for r in sub if r[4] is not None]
    def summ(v):
        return f"n={len(v)} med={st.median(v):+.3f} mean={st.mean(v):+.3f}" if v else "n=0"
    print(f"{name:9s} P1-old: {summ(d1)} | NOP-old: {summ(d2)} | P1-NOP: {summ(d3)}")
print()
# per-line median offset (P1-old) to find the one-word-early pattern
lines = json.load(open(PROJ + "/SONG_WORDS.json"))["lines"]
print("Per-line median dt(P1-old) (lines with >=3 matched words):")
for L in lines:
    lt = [r for r in rows if L["start"] <= r[0] < L["end"] and r[2] is not None]
    if len(lt) >= 3:
        import statistics as st
        print(f"  {L['id']:>4} {L['start']:6.2f}-{L['end']:6.2f}  med {st.median([r[2] for r in lt]):+.3f}  n={len(lt)}  {L['text'][:45]}")
