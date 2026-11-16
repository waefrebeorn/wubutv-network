#!/usr/bin/env python3
"""MV-4 lyrics redo: build the new kinetic .ass from the large-v3-turbo grid.

Input: work/lyrics-redo/song_transcript_large.json (new words)
       make_captions_mv4.LINES (57 sheet lines — the song's structure)
       work/lyrics-redo/text_overrides.json (optional: {lid: performed text}
         for lines where the performed words genuinely differ from the sheet;
         absent = sheet text stands)
Method:
- Align the new ASR word sequence to the sheet's full token sequence
  (difflib, in order); assign each ASR word to a line. Line start = first
  assigned word's start; line end = last assigned word's end.
- Caption text = sheet text (or override). Karaoke stepping per word when
  the assigned ASR word count equals the caption token count, times strictly
  increasing, every duration > 0.05s; else a single block event.
- Per-line font-size scaling (MV-13 kinetic-overflow fix): estimated width =
  len(text) * 0.52 * 44 * 1.06 (the 1.06 is the sans-width underestimate
  correction from the MV-13 width trap); if > 1100px, fs scales down so the
  estimate caps at 1100px. Applied as {\\fsN} on every event of the line.
- SINGLE backslashes only (MV-12 double-backslash bug): overrides are
  {\\1c&H1EC6FF&}, {\\r}, {\\fsN} — verify 0 lines contain '\\\\'.
- Style identical to the delivered captions: DejaVu Sans 44, white +
  cadmium highlight, bottom-center, MarginV 40.
"""
import difflib
import json
import os
import re
import sys

PROJ = "/home/hatch/workspace/wubutv-network/musicvideo/MV-4_this-time-its-real"
sys.path.insert(0, PROJ)
from make_captions_mv4 import LINES  # noqa: E402

NEW = json.load(open(f"{PROJ}/work/lyrics-redo/song_transcript_large.json"))["words"]
OVERRIDES = {}
ov_path = f"{PROJ}/work/lyrics-redo/text_overrides.json"
if os.path.exists(ov_path):
    OVERRIDES = json.load(open(ov_path))


def norm(w):
    # Strip apostrophes too: sheet "Futurama's" and ASR "Futuramas" are the
    # same word (the apostrophe is punctuation, not a phoneme). Without this
    # the chorus lines lose their first word and fall to block-only.
    return re.sub(r"[^a-z0-9']", "", w.lower()).replace("'", "")


# Canonical ASR spellings -> sheet tokens. Every entry is unambiguous on
# this track (the Suno lyric video confirms the sheet word in each case):
# the singer says "Futurama's" (ASR spells it Futuramma's/Futuramah's),
# "twenty-thirteen"/"fourteen"/"twenty-seven" (ASR writes digits),
# "everyone" (ASR guesses "everybody" at p=0.0 on the soft repeats).
ASR_ALIASES = {
    "futurammas": "futuramas",
    "futuramahs": "futuramas",
    "2013": "twentythirteen",
    "14": "fourteen",
    "27": "twentyseven",
    "everybody": "everyone",
    # L47's second "done" is heard as "gone" at p=0.0 (old grid: "done"
    # p=0.991 at the same time; video says "done"). No real "gone" in the
    # song, so the alias is unambiguous here.
    "gone": "done",
}


def canon(w):
    return ASR_ALIASES.get(norm(w), norm(w))


def ts(sec):
    h = int(sec // 3600)
    m = int((sec % 3600) // 60)
    s = sec % 60
    return f"{h}:{m:02d}:{s:05.2f}"


def ass_escape(t):
    return t.replace("\\", "\\\\").replace("{", "\\{").replace("}", "\\}")


def fs_for(text, base=44, cap=1100):
    est = len(text) * 0.52 * base * 1.06
    if est <= cap:
        return base
    return max(20, int(base * cap / est))


# Line-level decisions from the diff analysis (see LYRICS_REDO_NOTES.md):
# - Caption TEXT = sheet text throughout (Suno lyric video confirms all 57
#   lines; the new ASR's performed-vs-sheet diffs are slurs/garble, never a
#   confident different word). Times = new large-v3-turbo anchors.
# - L54: BLOCK-ONLY. The second repeat is sung too softly for any ASR pass
#   (full-clip hears a 5s garbage "off" p=0.001; the slice hears "No, no, no").
#   Karaoke would highlight wrong words. Span 204.04 (new first word) to
#   212.00 (slice decode's final "on" end, p=0.932).
# - L55: falls to BLOCK-ONLY automatically (7 ASR tokens vs 6 sheet tokens:
#   "every"+"one" split). Span from assigned words.
# - L57: SPECIAL CASE — the old 17.26s static block is the worst alignment
#   failure in the track (text sits through 10s of silence). The new grid
#   hears two distinct soft phrases; emit two blocks, one per phrase.
BLOCK_ONLY = {"L54"}
# L54 end capped at L55's first word (211.62) so the blocks abut instead of
# overlapping — the slice decode's final "on" rings to 212.00, but L55's
# "Good" starts at 211.62 and takes the screen.
BLOCK_SPAN_OVERRIDE = {"L54": (204.04, 211.62)}
L57_BLOCKS = [("Good news, everyone.", 230.56, 234.24),
              ("For real this time.", 234.24, 238.02)]
# Align ASR words to sheet lines, in order.
# Global difflib alignment first; then per-line validation against the old
# spans (within 3s). A line that fails is re-aligned LOCALLY inside
# [ls-1.5, le+1.5] — the global matcher jumps identical repeats (L55's
# second "everyone" matched L57's repeat 14s later).
def align(toks, words):
    """difflib sheet-tokens -> ASR words; returns {tok_idx: asr_idx}.
    Sheet tokens are normed; ASR words are canonicalised (aliases above)."""
    wseq = [canon(w["word"]) for w in words]
    sm = difflib.SequenceMatcher(a=toks, b=wseq, autojunk=False)
    m = {}
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            for k in range(i2 - i1):
                m[i1 + k] = j1 + k
    return m


sheet_toks = []
line_of_tok = []
for lid, text, ls, le in LINES:
    for t in text.split(" "):
        sheet_toks.append(norm(t))
        line_of_tok.append(lid)

global_map = align(sheet_toks, NEW)
tok_asr = [global_map.get(i) for i in range(len(sheet_toks))]

# per-line assigned ASR words (in order)
line_words = {lid: [] for lid, _, _, _ in LINES}
for ti, ai in enumerate(tok_asr):
    if ai is not None:
        line_words[line_of_tok[ti]].append(NEW[ai])

for lid, text, ls, le in LINES:
    if lid == "L57":
        continue
    assigned = line_words[lid]
    bad = True
    if assigned:
        nls, nle = assigned[0]["start"], assigned[-1]["end"]
        bad = abs(nls - ls) > 3.0 or abs(nle - le) > 3.0
    if bad:
        win = [w for w in NEW if ls - 1.5 <= w["start"] < le + 1.5]
        toks = [norm(t) for t in text.split(" ")]
        lm = align(toks, win)
        line_words[lid] = [win[ai] for ti, ai in sorted(lm.items())]
        assigned = line_words[lid]
        if assigned:
            nls, nle = assigned[0]["start"], assigned[-1]["end"]
            bad = abs(nls - ls) > 3.0 or abs(nle - le) > 3.0
        print(f"  {lid}: global alignment failed span check; local re-align -> "
              f"{nls:.2f}-{nle:.2f} ({len(assigned)} words) {'STILL BAD' if bad else 'ok'}")

header = """[Script Info]
ScriptType: v4.00+
PlayResX: 1280
PlayResY: 720
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,DejaVu Sans,44,&H00FFFFFF,&H001EC6FF,&H80000000,&H80000000,-1,0,0,0,100,100,0,0,1,3,0,2,40,40,40,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

events = []
report = []
for lid, text, ls, le in LINES:
    # End of the previous line's last event; a block's backward extension
    # never reaches back past it (stops L47/L48 double-claiming "gone").
    prev_ev_end = max([e for _, e, _ in events], default=0.0)
    text = OVERRIDES.get(lid, text)
    toks = text.split(" ")
    assigned = line_words[lid]
    fs = fs_for(text)
    fs_pre = f"{{\\fs{fs}}}" if fs != 44 else ""
    if lid == "L57":
        # Two per-phrase blocks; the 220.77-230.56 silence stays caption-free.
        for btext, bs, be in L57_BLOCKS:
            bfs = fs_for(btext)
            bpre = f"{{\\fs{bfs}}}" if bfs != 44 else ""
            events.append((bs, be, bpre + ass_escape(btext)))
        report.append((lid, "L57 split: 2 blocks (Good 230.56-234.24, For 234.24-238.02)", 7))
        continue
    if assigned:
        nls, nle = assigned[0]["start"], assigned[-1]["end"]
    else:
        nls, nle = ls, le
        report.append((lid, "NO-ASR-WORDS fell back to old span", len(toks)))
    if lid in BLOCK_SPAN_OVERRIDE:
        nls, nle = BLOCK_SPAN_OVERRIDE[lid]
    if lid in BLOCK_ONLY:
        events.append((nls, nle, fs_pre + ass_escape(text)))
        report.append((lid, f"BLOCK-ONLY (forced) fs={fs} {nls:.2f}-{nle:.2f}", len(toks)))
        continue
    ok = (len(assigned) == len(toks)
          and all(assigned[k]["start"] < assigned[k + 1]["start"] for k in range(len(assigned) - 1))
          and all(a["end"] - a["start"] > 0.05 for a in assigned))
    if ok:
        for k, a in enumerate(assigned):
            ev_start = a["start"]
            ev_end = assigned[k + 1]["start"] if k + 1 < len(assigned) else nle
            ev_end = min(ev_end, nle)
            parts = []
            for j, tok in enumerate(toks):
                if j == k:
                    parts.append("{\\1c&H1EC6FF&}" + ass_escape(tok) + "{\\r}")
                else:
                    parts.append(ass_escape(tok))
            events.append((ev_start, ev_end, fs_pre + " ".join(parts)))
        report.append((lid, f"karaoke fs={fs} {nls:.2f}-{nle:.2f}", len(toks)))
    else:
        # Block-only: span covers the line's sung words, including unassigned
        # words at the edges (L27's slurred "For" at 99.24 sits before the
        # first assigned word; L55's split "every"+"one" after the last).
        # Never cross into the neighbouring lines' assigned words.
        li = [l for l, _, _, _ in LINES].index(lid)
        next_start = float("inf")
        if li + 1 < len(LINES):
            nxt = line_words[LINES[li + 1][0]]
            if nxt:
                next_start = nxt[0]["start"]
        prev_end = prev_ev_end
        assigned_keys = {(w["start"], w["word"]) for ws in line_words.values() for w in ws}
        for w in NEW:
            if (max(ls - 1.5, prev_end) <= w["start"] < min(le + 1.5, next_start)
                    and (w["start"], w["word"]) not in assigned_keys):
                nls = min(nls, w["start"])
                nle = max(nle, w["end"])
        events.append((nls, nle, fs_pre + ass_escape(text)))
        reason = f"block: asr={len(assigned)} perf={len(toks)}"
        report.append((lid, f"{reason} fs={fs} {nls:.2f}-{nle:.2f}", len(toks)))

# Validation: every line's span must sit within 3s of the old line span
# (guards against a difflib repeat-misalignment jumping a line by a chorus).
for lid, text, ls, le in LINES:
    if lid == "L57":
        continue
    # check assigned words directly (guards against a difflib
    # repeat-misalignment jumping a line by a chorus).
    assigned = line_words[lid]
    if lid in BLOCK_SPAN_OVERRIDE:
        nls, nle = BLOCK_SPAN_OVERRIDE[lid]
    elif assigned:
        nls, nle = assigned[0]["start"], assigned[-1]["end"]
    else:
        continue
    if abs(nls - ls) > 3.0 or abs(nle - le) > 3.0:
        print(f"VALIDATION FAIL {lid}: new span {nls:.2f}-{nle:.2f} vs old {ls:.2f}-{le:.2f}")
        raise SystemExit(1)
print("span validation: all lines within 3s of old spans")

# Overlap check: events must be in time order and never overlap (overlapping
# same-layer events double-render the text). Abutting (start == prev end) is fine.
events.sort(key=lambda e: e[0])
overlaps = []
for (s0, e0, _), (s1, e1, _) in zip(events, events[1:]):
    if s1 < e0 - 0.001:
        overlaps.append((s0, e0, s1, e1))
if overlaps:
    print(f"OVERLAP FAIL: {len(overlaps)} overlapping event pairs")
    for o in overlaps[:10]:
        print("  ", o)
    raise SystemExit(1)
print(f"overlap check: {len(events)} events, no overlaps")

out = [header]
for s, e, t in events:
    out.append(f"Dialogue: 0,{ts(s)},{ts(e)},Cap,,0,0,0,,{t}")
out_path = f"{PROJ}/work/lyrics-redo/mv4_kinetic_redo.ass"
open(out_path, "w").write("\n".join(out) + "\n")

# verify: 0 double-backslash lines
bad = [l for l in open(out_path) if "\\\\" in l]
print(f"events: {len(events)} -> {out_path}")
print(f"double-backslash lines: {len(bad)}")
for lid, mode, n in report:
    print(f"{lid}: {mode} ({n} words)")
if bad:
    print("DOUBLE-BACKSLASH LINES FOUND — FIX BEFORE ENCODING")
    for l in bad[:5]:
        print("  ", l.rstrip())
