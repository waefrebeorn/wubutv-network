#!/usr/bin/env python3
"""MV-4 lyrics redo: diff new large-v3-turbo words vs old base-model grid.

Outputs work/lyrics-redo/word_diff.json + a printed per-line summary:
- word identity changes (old -> new) with times + new prob
- timing shifts for matched words (|dStart| > 0.10s)
- words present in one grid only
- per-line verdict vs the sheet (LINES table from make_captions_mv4.py)
"""
import difflib
import json
import re
import sys

PROJ = "/home/hatch/workspace/wubutv-network/musicvideo/MV-4_this-time-its-real"
sys.path.insert(0, PROJ)
from make_captions_mv4 import LINES  # noqa: E402  (line table + sheet text)

NEW = json.load(open(f"{PROJ}/work/lyrics-redo/song_transcript_large.json"))["words"]
OLD = json.load(open(f"{PROJ}/SONG_WORDS.json"))["words"]


def norm(w):
    return re.sub(r"[^a-z0-9']", "", w.lower())


new_seq = [norm(w["word"]) for w in NEW]
old_seq = [norm(w["word"]) for w in OLD]

sm = difflib.SequenceMatcher(a=old_seq, b=new_seq, autojunk=False)
ops = sm.get_opcodes()

diff = {"identity": [], "timing": [], "old_only": [], "new_only": []}
for tag, i1, i2, j1, j2 in ops:
    if tag == "equal":
        for k in range(i2 - i1):
            o, n = OLD[i1 + k], NEW[j1 + k]
            ds = round(n["start"] - o["start"], 2)
            if abs(ds) > 0.10:
                diff["timing"].append(
                    {"word": o["word"], "old_start": o["start"], "new_start": n["start"],
                     "d_start": ds, "new_prob": n["prob"]})
    elif tag == "replace":
        for k in range(max(i2 - i1, j2 - j1)):
            o = OLD[i1 + k] if i1 + k < i2 else None
            n = NEW[j1 + k] if j1 + k < j2 else None
            diff["identity"].append(
                {"old": o["word"] if o else None, "old_start": o["start"] if o else None,
                 "old_prob": o["prob"] if o else None,
                 "new": n["word"] if n else None, "new_start": n["start"] if n else None,
                 "new_prob": n["prob"] if n else None})
    elif tag == "delete":
        for k in range(i1, i2):
            diff["old_only"].append(
                {"word": OLD[k]["word"], "start": OLD[k]["start"], "prob": OLD[k]["prob"]})
    elif tag == "insert":
        for k in range(j1, j2):
            diff["new_only"].append(
                {"word": NEW[k]["word"], "start": NEW[k]["start"], "prob": NEW[k]["prob"]})

json.dump(diff, open(f"{PROJ}/work/lyrics-redo/word_diff.json", "w"), indent=1)
print(f"new words: {len(NEW)}  old words: {len(OLD)}")
print(f"identity changes: {len(diff['identity'])}")
for d in diff["identity"]:
    os_ = f"{d['old_start']:7.2f}" if d['old_start'] is not None else "    ---"
    print(f"  IDENTITY {os_}  old={d['old']!r} (p={d['old_prob']}) -> new={d['new']!r} (p={d['new_prob']})")
print(f"timing shifts >0.10s: {len(diff['timing'])}")
for d in diff["timing"]:
    print(f"  TIMING {d['old_start']:7.2f}  {d['word']!r} {d['old_start']:.2f} -> {d['new_start']:.2f} (d={d['d_start']:+.2f})")
print(f"old-only words: {len(diff['old_only'])}")
for d in diff["old_only"]:
    print(f"  OLD-ONLY {d['start']:7.2f}  {d['word']!r} (p={d['prob']})")
print(f"new-only words: {len(diff['new_only'])}")
for d in diff["new_only"]:
    print(f"  NEW-ONLY {d['start']:7.2f}  {d['word']!r} (p={d['prob']})")

# Per-line check: new words inside each sheet line span vs sheet tokens.
print("\nPER-LINE (sheet tokens vs new ASR words in span):")
for lid, text, ls, le in LINES:
    toks = [norm(t) for t in text.split(" ")]
    got = [w for w in NEW if ls - 0.05 <= w["start"] < le]
    got_seq = [norm(w["word"]) for w in got]
    sm2 = difflib.SequenceMatcher(a=toks, b=got_seq, autojunk=False)
    ratio = sm2.ratio()
    flag = "" if ratio >= 0.95 and len(got) == len(toks) else "  <-- CHECK"
    print(f"  {lid} {ls:7.2f}-{le:7.2f} sheet={len(toks)}w asr={len(got)}w ratio={ratio:.2f}{flag}")
    if ratio < 0.95 or len(got) != len(toks):
        print(f"      sheet: {' '.join(toks)}")
        print(f"      asr:   {' '.join(got_seq)}")
