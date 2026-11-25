#!/usr/bin/env python3
"""MV-17 performed grid builder.

Aligns the ASR word stream (SONG_WORDS.json — timing authority) to the
hand-authored performed-line sequence (sheet text = text authority,
plus measured performed extras) via difflib token alignment, then
assigns each line the span of its matched ASR words.
Outputs grid_lines.json + a review table on stdout.
"""
import json, re, difflib, pathlib

OUT = pathlib.Path(__file__).parent

# (section, text, kind) kind: line | adlib (performed ad-lib on the sheet)
L = []
def V(sec, pairs):
    for t, k in pairs: L.append((sec, t, k))
def chorus(sec):
    for t in ["Why does the refrigerator light go off when I close the door",
              "Why does the refrigerator light go off when I close the door",
              "I checked twice, I checked twice",
              "And it's never on",
              "Why does the refrigerator light go off when I close the door"]:
        L.append((sec, t, "line"))

V("V1", [("Opened it slow and the light was already there", "line"),
         ("Closed it fast and I swear I heard it shut off", "line"),
         ("Now I'm sitting on the floor with the door cracked open", "line"),
         ("Waiting for proof that it only works when I'm looking", "line")])
V("PC1", [("I checked, I checked", "line"), ("It was off, it was off", "line")])
# Choruses are PERFORMED chopped (measured from ASR segments): one full
# hook line, short hook fragments, then a full hook reprise.
V("C1", [("Why does the refrigerator light go off when I close the door", "line"),
         ("Why does it go off", "frag"),
         ("Why does that go off when I close the door", "frag"),
         ("I check twice", "frag"),
         ("I check once", "frag"),
         ("And it's never on", "line"),
         ("Why does the refrigerator light go off when I close the door", "line")])
V("V2", [("Set up my phone and recorded the whole thing", "line"),
         ("Played it back and the light only comes on when I open", "line"),
         ("Someone's turning it off the second I walk away", "line"),
         ("And I'm starting to think it's not just the fridge anymore", "line")])
V("PC2", [("I checked, I checked", "line"), ("It was off, it was off", "line")])
V("C2", [("Why does the refrigerator light go off when I close the door", "line"),
         ("Why does it go off", "frag"),
         ("I check twice, I check once", "frag"),
         ("And it's never on", "line"),
         ("Why does the refrigerator light go off when I close the door", "line")])
V("BR", [("I checked twice, I checked twice", "line"),
         ("It was never on, it was never on", "line"),
         ("When I close the door", "line")])
V("C3", [("Why does the refrigerator light go off when I close the door", "line"),
         ("Why does the refrigerator light go off when I close the door", "line"),
         ("I check twice, I check twice", "frag"),
         ("And it's never on", "line"),
         ("Why does the refrigerator light go off when I close the door", "line")])
V("OUT", [("Never on, never on", "line"),
          ("When I close the door", "line")])

MISHEAR = {"frige": "fridge", "refridgerator": "refrigerator", "lite": "light", "run": "on", "closed": "close"}
def norm(w):
    w = w.lower().strip(".,!?()'")
    w = w.replace("’", "'").lstrip("-")
    return MISHEAR.get(w, w)

exp_words, exp_line_of = [], []
for li, (sec, text, kind) in enumerate(L):
    for w in text.replace("(", " ").replace(")", " ").replace("-", " ").split():
        exp_words.append(norm(w)); exp_line_of.append(li)

asr = json.load(open(OUT / "SONG_WORDS.json"))
aw = asr["words"]
asr_words = [norm(w["word"]) for w in aw]

sm = difflib.SequenceMatcher(a=exp_words, b=asr_words, autojunk=False)
# map: for each expected word index -> asr index (from matching blocks)
emap = {}
for a0, b0, n in sm.get_matching_blocks():
    for k in range(n):
        emap[a0 + k] = b0 + k

# line span: first/last expected word with a match; extend over gaps by
# neighbour interpolation on the asr index axis.
lines = []
ew_start = 0
for li, (sec, text, kind) in enumerate(L):
    n = len(text.replace("(", " ").replace(")", " ").replace("-", " ").split())
    idxs = [emap[ew_start + k] for k in range(n) if (ew_start + k) in emap]
    if idxs:
        a_first, a_last = min(idxs), max(idxs)
        start = aw[a_first]["start"]; end = aw[a_last]["end"]
        asr_text = " ".join(w["word"] for w in aw[a_first:a_last + 1])
        matched = f"{len(idxs)}/{n}"
    else:
        start = end = None; asr_text = ""; matched = f"0/{n}"; a_first = a_last = None
    lines.append({"n": li + 1, "section": sec, "text": text, "kind": kind,
                  "start": start, "end": end, "matched": matched,
                  "asr": asr_text, "a_first": a_first, "a_last": a_last,
                  "n_words": n})
    ew_start += n

# --- post-pass 1: SPLIT — a line whose ASR range swallowed the next
# line's words while the next line got no span (bridge WFY x2 case).
assigned = {}
for ln in lines:
    if ln["a_first"] is not None:
        for ai in range(ln["a_first"], ln["a_last"] + 1):
            assigned[ai] = ln["n"]
for i, ln in enumerate(lines[:-1]):
    nxt = lines[i + 1]
    if ln["a_first"] is not None and nxt["a_first"] is None:
        rng = list(range(ln["a_first"], ln["a_last"] + 1))
        need = ln["n_words"] + nxt["n_words"]
        if len(rng) >= need:
            cut = ln["a_first"] + ln["n_words"]
            ln["a_last"] = cut - 1; ln["end"] = aw[cut - 1]["end"]
            ln["asr"] = " ".join(w["word"] for w in aw[ln["a_first"]:cut])
            nxt["a_first"] = cut; nxt["a_last"] = ln["a_first"] + len(rng) - 1
            nxt["start"] = aw[cut]["start"]; nxt["end"] = aw[nxt["a_last"]]["end"]
            nxt["asr"] = " ".join(w["word"] for w in aw[cut:nxt["a_last"] + 1])
            nxt["matched"] = f"split"
            for ai in range(cut, nxt["a_last"] + 1):
                assigned[ai] = nxt["n"]

# --- post-pass 2: EXTEND — chain over unassigned ASR words that start
# within 0.05s of the line's current end, inter-word gaps < 0.35s
# (garbled tails: 'switching sides' -> 'swooning itch inside').
for ln in lines:
    if ln["a_last"] is None:
        continue
    j = ln["a_last"] + 1
    while j < len(aw) and j not in assigned and aw[j]["start"] - ln["end"] < 0.05:
        ln["a_last"] = j; ln["end"] = aw[j]["end"]; assigned[j] = ln["n"]
        ln["asr"] += " " + aw[j]["word"]; j += 1

for ln in lines:
    ln.pop("a_first"); ln.pop("a_last"); ln.pop("n_words")

# --- manual overrides (ear/word-verified): none yet for MV-17.
OVERRIDES = {4: {"end": 24.92}, 5: {"start": 24.92}}  # PC1 pickup "and" (24.92-25.20, p=0.12) belongs to L05
for n, ov in OVERRIDES.items():
    lines[n - 1].update(ov)
    lines[n - 1]["override"] = True

for ln in lines:
    s = f"{ln['start']:7.2f}" if ln["start"] is not None else "    -- "
    e = f"{ln['end']:7.2f}" if ln["end"] is not None else "    -- "
    print(f"L{ln['n']:02d} {ln['section']:4s} {s}-{e}  [{ln['matched']}] {ln['text']!r:55s} asr: {ln['asr']!r}")

json.dump(lines, open(OUT / "grid_lines.json", "w"), indent=1)
print(f"lines: {len(lines)}")
