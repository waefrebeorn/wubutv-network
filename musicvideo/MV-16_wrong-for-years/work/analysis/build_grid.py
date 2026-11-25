#!/usr/bin/env python3
"""MV-16 performed grid builder.

Aligns the ASR word stream (SONG_WORDS.json — timing authority) to the
hand-authored performed-line sequence (sheet text = text authority,
plus measured performed extras) via difflib token alignment, then
assigns each line the span of its matched ASR words.
Outputs grid_lines.json + a review table on stdout.
"""
import json, re, difflib, pathlib

OUT = pathlib.Path(__file__).parent

# (section, text, kind) kind: line | extra (performed extra not on sheet)
L = []
def chorus(sec, doubles=False):
    blk = [("I've been singing the wrong lyrics", "line"),
           ("For a decade", "line"),
           ("Nobody stopped me", "line"),
           ("I've been singing the wrong lyrics", "line"),
           ("For a decade", "line"),
           ("Nobody stopped me", "line")]
    if doubles:
        blk = [("I've been singing the wrong lyrics", "line"),
               ("For a decade", "line"),
               ("Nobody stopped me", "line"),
               ("Nobody stopped me", "extra-double"),
               ("I've been singing the wrong lyrics", "line"),
               ("For a decade", "line"),
               ("Nobody stopped me", "line"),
               ("Nobody stopped me", "extra-double")]
    blk += [("Wrong for years", "line"), ("Wrong for years", "line"),
            ("And I'm still going", "line"),
            ("I've been singing the wrong lyrics", "line"),
            ("For a decade", "line"),
            ("Nobody stopped me", "line")]
    for t, k in blk:
        L.append((sec, t, k))

chorus("C1")
L.append(("C1", "Hey! Hey!", "extra"))
for t in ["Belted the whole chorus in the car", "Like I wrote it", "(yeah)",
          "Friends in the back just nodded", "And let it ride", "(what)",
          "Now I'm at karaoke", "And the screen says different",
          "But I'm already locked in", "And I'm not switching sides"]:
    L.append(("V1", t, "adlib" if t.startswith("(") else "line"))
for t in ["I learned it wrong", "I learned it wrong", "And I kept it", "And I kept it"]:
    L.append(("PC1", t, "line"))
# C2 hand-authored: vocalise extras sit inside the chorus (measured)
for t, k in [("I've been singing the wrong lyrics", "line"), ("For a decade", "line"),
             ("Nobody stopped me", "line"), ("(oh-oh-oh)", "extra"),
             ("I've been singing the wrong lyrics", "line"), ("For a decade", "line"),
             ("Nobody stopped me", "line"), ("(oh-uh-oh)", "extra"),
             ("Wrong for years", "line"), ("Wrong for years", "line"),
             ("And I'm still going", "line"),
             ("I've been singing the wrong lyrics", "line"), ("For a decade", "line"),
             ("Nobody stopped me", "line")]:
    L.append(("C2", t, k))
for t in ["Nobody stopped me", "Nobody stopped me",
          "Wrong for years", "Wrong for years"]:
    L.append(("POST", t, "line"))
for t in ["Mic in my hand", "And the room starts to notice", "(yeah)",
          "But the wrong version hits harder", "So I'm staying", "(what)",
          "They can read the screen all they want", "I'm committed", "(uh)",
          "Ten years deep", "And I'm not rewriting it now"]:
    L.append(("V2", t, "adlib" if t.startswith("(") else "line"))
for t in ["I learned it wrong", "I learned it wrong", "And I kept it", "And I kept it"]:
    L.append(("PC2", t, "line"))
chorus("C3")
for t in ["Wrong for years", "Wrong for years", "Nobody stopped me",
          "Nobody stopped me", "(yeah)", "And I'm still going"]:
    L.append(("BR", t, "adlib" if t.startswith("(") else "line"))
chorus("FC", doubles=True)
for t in ["Nobody stopped me", "(oh)", "Nobody stopped me",
          "Wrong for years", "Wrong for years (yeah)"]:
    L.append(("OUT", t, "adlib" if t.startswith("(") else "line"))

MISHEAR = {"mike": "mic", "stops": "stopped", "stop": "stopped",
           "decay": "decade", "day": "decade", "seen": "been",
           "done": "been", "three": "for"}
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

# --- manual overrides (ear/word-verified):
# Bridge: the split pass + extension chained the '(no,)' pickup of
# L75 into L74's tail. The pickup belongs to L75.
OVERRIDES = {74: {"end": 135.58}, 75: {"start": 135.58}}
for n, ov in OVERRIDES.items():
    lines[n - 1].update(ov)
    lines[n - 1]["override"] = True

for ln in lines:
    s = f"{ln['start']:7.2f}" if ln["start"] is not None else "    -- "
    e = f"{ln['end']:7.2f}" if ln["end"] is not None else "    -- "
    print(f"L{ln['n']:02d} {ln['section']:4s} {s}-{e}  [{ln['matched']}] {ln['text']!r:55s} asr: {ln['asr']!r}")

json.dump(lines, open(OUT / "grid_lines.json", "w"), indent=1)
print(f"lines: {len(lines)}")
