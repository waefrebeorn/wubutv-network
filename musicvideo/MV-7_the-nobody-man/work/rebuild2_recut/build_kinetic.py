#!/usr/bin/env python3
"""Kinetic words JSON for rebuild-2: performed (sheet) lyric text on measured
SONG timings. Non-chant: sheet words paired to song word starts in the line
window (proportional fallback on count mismatch, except 3 hand-mapped lines).
Chant: word times synthesized from the take-slice proportions — the same rep
anchors the picture warp uses (SONG chant stamps are garbled)."""
import json, sys, os

BASE = "/home/hatch/workspace/wubutv-network/musicvideo/MV-7_the-nobody-man"
RC = f"{BASE}/work/rebuild2_recut"
sys.path.insert(0, RC)
from plan_data import T, NORM

SONG = json.load(open(f"{BASE}/SONG_WORDS.json"))["words"]
anchors = {r["ref"]: r for r in json.load(open(f"{RC}/anchors.json"))["lines"]}
SUNG_END_OVERRIDE = {"I2c": 18.74}

# hand-mapped (sheet word -> song time) for count-mismatch lines
HAND = {
    "V1.5": [("Made", 29.76), ("a", 29.92), ("joke", 30.08), ("at", 30.52),
             ("a", 30.68), ("quarter", 30.84), ("past", 30.98), ("eight", 31.30)],
    "B.6": [("I'm", 137.02), ("the", 138.18), ("joke", 138.34), ("that", 138.88),
            ("lasts", 139.46), ("and", 139.95), ("lasts", 140.44)],
    "FC.10": [("Yeah,", 168.16), ("I", 168.90), ("turn", 169.66), ("the", 169.92),
              ("small", 170.10), ("things", 170.60), ("grand", 171.20)],
}

out = []
lid = 0

def emit(pairs, line_end):
    """pairs: [(text, start)] -> word events with end = next start / line_end."""
    global lid
    lid += 1
    for i, (tok, s) in enumerate(pairs):
        e = pairs[i + 1][1] if i + 1 < len(pairs) else line_end
        out.append({"word": tok, "start": round(s, 3),
                    "end": round(max(e, s + 0.15), 3), "line": lid})

# ---- non-chant T lines ----
for ref, lyric, a, b, _unit in T:
    if ref in HAND:
        emit(HAND[ref], b)
        continue
    toks = lyric.split()
    sw = [w for w in SONG if a - 0.01 <= w["start"] < b - 0.01]
    if len(sw) == len(toks):
        emit([(t, w["start"]) for t, w in zip(toks, sw)], b)
    elif sw:
        t0, t1 = sw[0]["start"], b
        step = (t1 - t0) / len(toks)
        emit([(t, t0 + i * step) for i, t in enumerate(toks)], b)
    else:
        step = (b - a) / len(toks)
        emit([(t, a + i * step) for i, t in enumerate(toks)], b)

# ---- chant lines: synthesized from slice proportions ----
CHANT_REFS = ["I1a", "I1b", "I1c", "I1d", "I2a", "I2b", "I2c",
              "C1.Ta", "C1.Tb", "C1.Tc", "C1.Td",
              "FC.Ta", "FC.Tb", "FC.Tc", "FC.Td"]
for ref in CHANT_REFS:
    rec = anchors[ref]
    sl = rec["slice"]
    a = rec["a"]
    if not sl:  # STRUCT chant line (C1.Tb): performed "Nobody man", even split
        emit([("Nobody", a), ("man", a + (rec["b"] - a) / 2)], rec["b"])
        continue
    song_end = SUNG_END_OVERRIDE.get(ref, rec["b"])
    t_start, t_end = sl[0]["s"], sl[-1]["e"]
    span_t = max(0.05, t_end - t_start)
    pairs = []
    for w in sl:
        txt = NORM.get(w["w"].lower().strip(",.?!"), w["w"])
        if w is sl[0]:
            txt = txt[0].upper() + txt[1:]
        pairs.append((txt, a + (w["s"] - t_start) / span_t * (song_end - a)))
    emit(pairs, rec["b"])

out.sort(key=lambda w: w["start"])
# re-number lines in time order
remap = {}
for w in out:
    if w["line"] not in remap:
        remap[w["line"]] = len(remap) + 1
    w["line"] = remap[w["line"]]
json.dump(out, open(f"{RC}/kinetic_words.json", "w"), indent=1)
print("kinetic words:", len(out), "lines:", len(remap))
