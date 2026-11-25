#!/usr/bin/env python3
"""MV-18 performed grid builder.

Aligns the ASR word stream (SONG_WORDS.json — timing authority) to the
hand-authored performed-line sequence (sheet text = text authority,
line COUNT from the measured performance, which differs from the
sheet: C1 sings the hook once before the first sigma, pre-choruses
sing each phrase once, C3's hooks are chopped) via difflib token
alignment, then assigns each line the span of its matched ASR words.
Outputs grid_lines.json + a review table on stdout.
"""
import json, re, difflib, pathlib

OUT = pathlib.Path(__file__).parent


HOOK = "I walked into the room and immediately forgot why"
NPC = "Like a confused NPC"
STAND = "Just standing here"
WANT = "What did I want"
BLANK = "Brain went blank"

# (section, text, kind)
HOOK = "The laundry is clean but it's still on the floor"
BASKET = "Living out the basket"
RAC = "Like a raccoon"
STILL = "Still on the floor"
CLEAN = "Clean is clean"
L = []
def V(sec, pairs):
    for t, k in pairs: L.append((sec, t, k))
CH = [(HOOK,"line"),(HOOK,"line"),(BASKET,"line"),(BASKET,"line"),(RAC,"line"),(HOOK,"line")]
PC = [(CLEAN,"line"),(CLEAN,"line"),("But it's still on the floor","line"),("But it's still on the floor","line")]
V("C1", CH)
V("V1", [("Washed it dried it folded nothing","line"),("Basket's full and I'm still wearing the same thing","line"),("Reached in for socks and pulled out a shirt","line"),("Now I'm just digging like it's my only source","line")])
V("PC1", PC)
V("C2", CH)
V("POST", [(STILL,"line"),(STILL,"line"),(RAC,"line"),(RAC,"line")])
V("V2", [("Week later and the basket's my dresser","line"),("Grabbing whatever's on top and calling it better","line"),("Pants are clean but they're wrinkled as hell","line"),("And I'm still not putting them away I can tell","line")])
V("PC2", PC)
V("C3", CH)
V("BR", [(STILL,"line"),(STILL,"line"),("I washed it","line"),("I dried it","line"),("And now I'm living out the basket","line")])
V("C4", CH)
V("OUT", [(STILL,"line"),(STILL,"line"),(RAC,"line")])

MISHEAR = {"checked": "check", "check": "check", "walked": "walked",
           "into": "into", "in": "into", "to": "to", "it": "it",
           "its": "it's", "immediately": "immediately"}

def norm(w):
    w = w.lower().strip(".,!?()'\"")
    w = w.replace("\u2019", "'").lstrip("-")
    if w in ("checked",): return "check"
    if w in ("in",) : return "into"
    return MISHEAR.get(w, w)


    w = w.lower().strip(".,!?()'\"")
    w = w.replace("’", "'").lstrip("-")
    return MISHEAR.get(w, w)

exp_words, exp_line_of = [], []
for li, (sec, text, kind) in enumerate(L):
    for w in text.replace("(", " ").replace(")", " ").replace("-", " ").split():
        exp_words.append(norm(w)); exp_line_of.append(li)

asr = json.load(open(OUT / "SONG_WORDS.json"))
# expand hyphenated ASR tokens ("what's-a-sigma?") into timed subwords
aw = []
for w in asr["words"]:
    parts = w["word"].replace("-", " ").split()
    if len(parts) > 1:
        for p in parts:
            aw.append({"word": p, "start": w["start"], "end": w["end"],
                       "prob": w["prob"]})
    else:
        aw.append(w)
asr_words = [norm(w["word"]) for w in aw]

sm = difflib.SequenceMatcher(a=exp_words, b=asr_words, autojunk=False)
emap = {}
for a0, b0, n in sm.get_matching_blocks():
    for k in range(n):
        emap[a0 + k] = b0 + k

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
# line's words while the next line got no span.
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
            nxt["matched"] = "split"
            for ai in range(cut, nxt["a_last"] + 1):
                assigned[ai] = nxt["n"]

# --- post-pass 2: EXTEND — chain over unassigned ASR words adjacent
# to the line's current end (garbled tails).
for ln in lines:
    if ln["a_last"] is None:
        continue
    j = ln["a_last"] + 1
    while j < len(aw) and j not in assigned and aw[j]["start"] - ln["end"] < 0.05:
        ln["a_last"] = j; ln["end"] = aw[j]["end"]; assigned[j] = ln["n"]
        ln["asr"] += " " + aw[j]["word"]; j += 1

for ln in lines:
    ln.pop("a_first"); ln.pop("a_last"); ln.pop("n_words")

# --- manual overrides (word-verified from the segment dump):
# L18: segment "What'sa-Sigma?" spans 70.82-71.88; alignment gave the
# hyphen-split head to L17. L44: performed line includes the stutter
# tail "i, i regret" running to 152.78 (segment 150.60-152.78).
OVERRIDES = {21: {"end": 75.08}, 22: {"start": 75.08}}
for n, ov in OVERRIDES.items():
    lines[n - 1].update(ov)
    lines[n - 1]["override"] = True

for ln in lines:
    s = f"{ln['start']:7.2f}" if ln["start"] is not None else "    -- "
    e = f"{ln['end']:7.2f}" if ln["end"] is not None else "    -- "
    print(f"L{ln['n']:02d} {ln['section']:4s} {s}-{e}  [{ln['matched']}] {ln['text']!r:55s} asr: {ln['asr']!r}")

json.dump(lines, open(OUT / "grid_lines.json", "w"), indent=1)
print(f"lines: {len(lines)}")
