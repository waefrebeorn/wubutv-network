#!/usr/bin/env python3
"""Align a take's raw ASR words (take_asr.py output) to the expected line.
Usage: align_take.py <words.json> "<expected line>" <song_span_s>
Prints ratio/first/last + G7 word-set overlap; writes <words>.align.json"""
import json, re, sys, difflib
from pathlib import Path
wp, expected, span = sys.argv[1], sys.argv[2], float(sys.argv[3])
d = json.load(open(wp))
def norm(s): return re.sub(r"[^a-z0-9' ]", "", s.lower()).split()
exp = norm(expected)
asr = [(norm(w["w"]), w) for w in d["words"]]
asr = [(t[0], w) for t, w in asr if t[0]]
flat = [t for t, _ in asr]
best = (-1, 0, 0)
for i in range(len(flat)):
    for j in range(i + 1, len(flat) + 1):
        win = flat[i:j]
        sc = sum(max((difflib.SequenceMatcher(None, e, a).ratio() for a in win), default=0) for e in exp)
        ov = len(set(exp) & set(win)) / max(1, len(set(exp)))
        tot = sc + 2 * ov
        if tot > best[0]: best = (tot, i, j)
_, i, j = best
win_words = [w for _, w in asr[i:j]]
first = win_words[0]["start"]; last = win_words[-1]["end"]
overlap = len(set(exp) & set(flat)) / max(1, len(set(exp)))
out = {"expected": expected, "song_span": span, "take_first": first, "take_last": last,
       "line_ratio": round((last - first) / span, 3), "g7_overlap": round(overlap, 3),
       "asr_text": " ".join(flat)}
Path(wp.replace(".json", ".align.json")).write_text(json.dumps(out, indent=1))
print(f"{Path(wp).name}: ratio={out['line_ratio']} first={first} last={last} g7={out['g7_overlap']} asr={out['asr_text'][:70]!r}")
