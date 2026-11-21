#!/usr/bin/env python3
"""MV-5 lyrics redo — build the merged word grid (v2).

The old grid's words and lines are semi-independent structures (the word
list is NOT the concatenation of line texts — label lines I09/L56b break
cumulative slicing, and line spans bleed into the next line's first word).
So the merge does NOT use old words as anchors at all. Instead, for each
line, the NEW (arbitrated) text is aligned directly against the ASR word
sequence in the line's time window:
  - primary time source: P1 (turbo, suppression ON) for Verse/Bridge;
    STEM (vocal-only decode) for Intro/Chorus/Final when --stem is given.
  - repeats P1 dropped: NOP times.
  - unmatched new words: positional fallback to the nearest free ASR word.
New text per line (arbitration across OLD/NOP/P1/P2/GEM/sheet):
  L48  "So I did it, not yet"      (all 4 ASR sources: did it, not didn't)
  L52  "Like none of it was last"   (NOP+P2+GEM: last; delivered .ass already "last")
  L81  "And the bass moves slow"    (NOP+P1+P2+GEM: moves)
  L45  "Ice, ice, ice cup sweating" (all ASR: repeated ice; count via --ice)
  L102 "Let it drift, let it go"    (--drift rip|drift; stem decides)
  L73a/c "I'm falling"              (--falling yes|no; stem decides)
  I09  "ta-da, ta-da, ta-da, ta-da, ta-da, ta-da" (NOP x6)
  L107 DROPPED (no words 187.5-193.5 in P1/P2/NOP)
  L56b DROPPED (held note, no words 120.02-121.26 in any pass)
  Tail L108-L110: RESTRUCTURED from P1 (PROVISIONAL — the final stem
  arbitrates the pair count: P1 hears 7x 'Easy now', P2 hears 4 + echo).
  Intro 'it's time to spend': NOT ADDED — NOP hallucination; the stem hears
  only the 'comes' tail to 17.52, then silence to the ta-da at ~18.7.
  L45 ice count: 3 (NOP+P1+P2+GEM all hear 3x 'ice').
Usage: merge_grid.py [--stem words_stem.json] [--drift rip|drift]
       [--falling yes|no] [--itstime yes|no] [--ice N]
       [--sections S,...] [--out grid_merged.json]
NOTE: --tail/--itstime/--held are accepted for compatibility but the tail is
always the P1 provisional (build_tail_lines) until a --tail stem path is
added; --itstime is ignored (the stem settled it: no such line).
"""
import argparse, difflib, json, re, sys
from collections import Counter

PROJ = "/home/hatch/workspace/wubutv-network/musicvideo/MV-5_easy-now-easy-now"
ap = argparse.ArgumentParser()
ap.add_argument("--stem", default=None)
ap.add_argument("--drift", default="drift", choices=["drift", "rip"])
ap.add_argument("--falling", default="yes", choices=["yes", "no"])
ap.add_argument("--itstime", default="no", choices=["yes", "no"])
ap.add_argument("--ice", type=int, default=3)
ap.add_argument("--held", default="Easy")
ap.add_argument("--tail", default="stem", choices=["stem", "old"])
ap.add_argument("--sections", default=None)
ap.add_argument("--out", default="grid_merged.json")
args = ap.parse_args()

def norm(w):
    return re.sub(r"[^a-z0-9']", "", w.lower())

def load_words(path):
    d = json.load(open(path))
    if "words" in d:
        return d["words"]
    return [w for s in d.get("segments", []) for w in s.get("words", [])]

old = json.load(open(PROJ + "/SONG_WORDS.json"))
old_lines = old["lines"]
nop = load_words(PROJ + "/work/song_transcript_noprompt.json")
p1 = load_words(PROJ + "/work/lyrics-redo/words_full_v3turbo.json")
stem = load_words(args.stem) if args.stem else []

CHORUS_SECTIONS = {"Intro", "Chorus 1", "Chorus 2", "Final Chorus"}
# L01 "Bare feet": P1's intro timestamps jitter (Bare 20.88 vs NOP/old 22.00);
# the old grid's L01 words ARE the NOP pass (verified exact). Use NOP.
PRIMARY_OVERRIDE = {"L01": "nop"}
# The stem is primary for a chorus section ONLY if it actually covers that
# section's time range (a partial stem file — e.g. intro-only — must NOT
# displace P1 for the uncovered choruses; they fall back to P1+NOP).
def stem_covered_sections(stem_words, lines):
    cov = set()
    if not stem_words:
        return cov
    for L in lines:
        if any(L["start"] - 1.0 <= w["start"] < L["end"] + 1.0 for w in stem_words):
            cov.add(L["section"])
    return cov
STEM_COVERED = stem_covered_sections(stem, old_lines)

# Full-text overrides (line id -> new display text)
TEXT_OVERRIDE = {
    "L48": "So I did it, not yet",
    "L52": "Like none of it was last",
    "L81": "And the bass moves slow",
    "L102": f"Let it {args.drift}, let it go",
    "I09": "ta-da, ta-da, ta-da, ta-da, ta-da, ta-da",
    "L90": "No, no, no",
}
if args.falling == "no":
    for lid in ("L73a", "L73c"):
        TEXT_OVERRIDE[lid] = "Just two small sparks"
# L45 ice count
TEXT_OVERRIDE["L45"] = " ".join(["Ice"] + ["ice"] * (args.ice - 1) + ["cup", "sweating"])

def words_in(ws, t0, t1):
    return [w for w in ws if t0 <= w["start"] < t1]

def align(text_words, asr_words):
    """difflib align; returns {text_idx: asr_word} for equal pairs."""
    a = [norm(w) for w in text_words]
    b = [norm(w["word"]) for w in asr_words]
    sm = difflib.SequenceMatcher(a=a, b=b, autojunk=False)
    out = {}
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            for k in range(i2 - i1):
                out[i1 + k] = asr_words[j1 + k]
    return out

sections = set(args.sections.split(",")) if args.sections else None
new_lines, new_words, report = [], [], []
dropped = []
used_asr = set()  # ids of ASR words already assigned — no word is used twice
# Old words per line (span assignment, gap words to the next line) — used ONLY
# as POS anchors (the old grid's word times are the prior for unmatched words).
old_by_line = {}
for w in old["words"]:
    for L in old_lines:
        if L["start"] <= w["start"] < L["end"]:
            old_by_line.setdefault(L["id"], []).append(w)
            break
    else:
        nxt = [L for L in old_lines if L["start"] > w["start"]]
        if nxt:
            old_by_line.setdefault(nxt[0]["id"], []).append(w)

def build_tail_lines(p1_words):
    """PROVISIONAL tail (final stem arbitrates): P1 hears 7x 'Easy now'
    (193.48-197.52) then 2x 'Till the morning comes' (200.48-202.68,
    203.34-204.90). P2 hears 4 pairs + an echo continuation to 201.20, so
    the pair COUNT is uncertain (P1 may over-split: pairs at 195.50/195.74
    are 0.24s apart). Rendered as one chant line (the closing chant is a
    single 4s phrase) + 2 Till lines; the stem will correct the count.
    The old L108 'We ride' is WRONG; the old L109 span straddles the gap.
    """
    tw = [w for w in p1_words if 193.0 <= w["start"] < 206.0]
    # split at the first 'Till'
    ti = next((i for i, w in enumerate(tw) if w["word"].strip().lower().startswith("till")), len(tw))
    chant, rest = tw[:ti], tw[ti:]
    # split the Till run at the second 'Till'
    tj = next((i for i in range(1, len(rest)) if rest[i]["word"].strip().lower().startswith("till")), len(rest))
    till1, till2 = rest[:tj], rest[tj:]
    def mkwords(ws, chant_fmt=False):
        out = []
        for i, w in enumerate(ws):
            txt = w["word"].strip().strip(",")
            if chant_fmt:
                txt = txt.capitalize() if i == 0 else txt.lower()
                if i % 2 == 1 and i < len(ws) - 1:
                    txt += ","
            out.append({"word": txt, "start": round(w["start"], 3),
                        "end": round(w["end"], 3), "src": "P1-TAIL"})
        return out
    lines, words = [], []
    cw = mkwords(chant, chant_fmt=True)
    # The last chant word's end is a segment-boundary artefact (P1's final
    # 'now' inherits the 3s gap to the next segment); cap the line end.
    chant_end = round(cw[-1]["start"] + 0.5, 3)
    lines.append({"id": "L108", "section": "Final Chorus",
                  "text": " ".join(w["word"] for w in cw),
                  "start": cw[0]["start"], "end": chant_end})
    words += cw
    for lid, ws in (("L109", till1), ("L110", till2)):
        if not ws:
            continue
        lw = mkwords(ws)
        # display 'Till' capitalised
        lw[0]["word"] = "Till"
        lines.append({"id": lid, "section": "Final Chorus",
                      "text": " ".join(w["word"] for w in lw),
                      "start": lw[0]["start"], "end": lw[-1]["end"]})
        words += lw
    return lines, words

def build_intro_lines(stem_words):
    """Rebuild the intro from the STEM decode (vocal-only, the arbiter).

    The old intro line spans are wrong by up to 4s (I06/I07/I08 overlap and
    misplace the second 'Till the morning comes'). The stem hears:
      I01 Easy now, easy now   (1.40-3.72)   I02 We ride, we ride (3.84-5.76)
      I03 Easy now, easy now   (6.34-7.56)   I04 Till the morning comes (8.04-10.04)
      I05 Easy now, easy now   (10.60-12.72)
      I06 We ride — NOT SUNG (P1+P2+stem all lack it; only NOP/base hallucinates it)
      I07 Easy now — NOT SUNG (stem hears 'until the morning' from 12.72)
      I08 Till the morning comes (12.72-17.52, drawn out; stem hears 'until')
      I09 ta-da x6 — the stem transcriber skips the wordless vocalise; times
          are the 25ms-RMS envelope burst onsets of the vocal stem:
          18.70, 19.15, 19.58, 19.98, 20.30, 20.88 (6 bursts, cf. NOP 6x).
    The stem's first 24 words are the intro (I01-I05 + I08); the last 4 are
    L01 'Bare feet on the boardwalk' (Verse 1, NOP override in the main loop).
    """
    sw = stem_words
    if len(sw) < 24:
        raise SystemExit(f"intro stem has {len(sw)} words, need >=24")
    specs = [
        ("I01", "Easy now, easy now", sw[0:4]),
        ("I02", "We ride, we ride", sw[4:8]),
        ("I03", "Easy now, easy now", sw[8:12]),
        ("I04", "Till the morning comes", sw[12:16]),
        ("I05", "Easy now, easy now", sw[16:20]),
        ("I08", "Till the morning comes", sw[20:24]),
    ]
    out_lines, out_words = [], []
    for lid, text, ws in specs:
        disp = text.split()
        # I08: the stem hears 'until' for the drawn-out 'Till' — display 'Till'
        # (sheet + NOP + P1/P2 all say Till).
        if lid == "I08":
            disp = ["Till", "the", "morning", "comes"]
        lw = []
        for i, w in enumerate(ws):
            lw.append({"word": disp[i], "start": round(w["start"], 3),
                       "end": round(w["end"], 3), "src": "STEM"})
        out_lines.append({"id": lid, "section": "Intro", "text": text,
                          "start": lw[0]["start"], "end": lw[-1]["end"]})
        out_words += lw
    # I09 ta-da x6 from the stem envelope onsets
    onsets = [18.70, 19.15, 19.58, 19.98, 20.30, 20.88]
    lw = []
    for k, t in enumerate(onsets):
        e = onsets[k + 1] if k + 1 < len(onsets) else 21.40
        lw.append({"word": "ta-da," if k < 5 else "ta-da", "start": t, "end": round(e, 3),
                   "src": "STEM-ENV"})
    out_lines.append({"id": "I09", "section": "Intro",
                      "text": "ta-da, ta-da, ta-da, ta-da, ta-da, ta-da",
                      "start": lw[0]["start"], "end": lw[-1]["end"]})
    out_words += lw
    return out_lines, out_words
for L in old_lines:
    lid, sec = L["id"], L["section"]
    if sections and sec not in sections:
        continue
    # Intro: rebuilt from the stem (see build_intro_lines); the old intro
    # spans are wrong by up to 4s, so the normal window alignment cannot work.
    # Without --stem, intro lines fall through to the normal P1/NOP path.
    if sec == "Intro" and args.stem:
        if lid == "I01":
            il, iw = build_intro_lines(stem)
            new_lines += il
            new_words += iw
            dropped.append(("I06", "NOT SUNG — P1+P2+stem all lack 'We ride' here; only NOP/base hallucinates it"))
            dropped.append(("I07", "NOT SUNG — stem hears 'until the morning comes' from 12.72; no 'Easy now' at 15.40"))
        continue
    if lid == "L107":
        dropped.append((lid, "artifact — no words 187.5-193.5 in P1/P2/NOP; line dropped"))
        continue
    if lid == "L56b":
        # "(held vocalise)" — no words sung 120.02-121.26 in any pass; the
        # 119.65 word is the tail of L56 'replays' ('-plays', NOP 'fly' /
        # P1 'play'). A held note, not a caption. Dropped.
        dropped.append((lid, "held note, no words 120.02-121.26 in P1/P2/NOP; dropped"))
        continue
    if lid in ("L108", "L109", "L110"):
        # Tail restructure (PROVISIONAL until the final stem lands — see
        # build_tail_lines): P1 hears 6x 'Easy now' (194.52-197.52, one per
        # ~0.5s) then 2x 'Till the morning comes' (200.48-202.68, 203.34-204.90).
        # The old L108 'We ride' is WRONG (no source hears it); the old L109
        # span (197.58-203.42) straddles the P1 gap (197.52-200.48) and the
        # first Till. P2's extra 'Easy now's at 198.82-201.20 are its echo
        # artifact (same failure as Chorus-1 'Is it now?') — P1's silence
        # there is the provisional reading; the final stem arbitrates.
        if lid == "L108":
            tl, tw = build_tail_lines(p1)
            new_lines += tl
            new_words += tw
        continue
    new_text = TEXT_OVERRIDE.get(lid, L["text"])
    text_words = [w.strip(",") for w in new_text.replace(",", " ,").split()]
    text_words = [w for w in text_words if w != ","]
    # keep punctuation attached to the word it follows for display
    disp = []
    for w in new_text.split():
        disp.append(w)
    text_words = [re.sub(r"[^A-Za-z0-9'\-]", "", w) for w in disp]
    t0, t1 = L["start"] - 1.0, L["end"] + 1.0
    if PRIMARY_OVERRIDE.get(lid) == "nop":
        primary = nop
    elif args.stem and sec in STEM_COVERED:
        primary = stem
    else:
        primary = p1
    prim = [w for w in words_in(primary, t0, t1) if id(w) not in used_asr]
    match = align(text_words, prim)
    nopw = [w for w in words_in(nop, t0, t1) if id(w) not in used_asr]
    match_nop = align(text_words, nopw)
    # Tiebreak when P1 and NOP both match the same text word but disagree:
    # prefer the one whose start falls INSIDE the old line span; if both do,
    # prefer P1; if they agree within 0.3s, P1. (Catches P1's intro jitter,
    # e.g. L01 "Bare feet": P1 20.88/21.76 vs NOP/old 22.00/22.22.)
    for i in list(match):
        if i in match_nop:
            a, b = match[i], match_nop[i]
            if abs(a["start"] - b["start"]) > 0.3:
                a_in = L["start"] <= a["start"] < L["end"]
                b_in = L["start"] <= b["start"] < L["end"]
                if b_in and not a_in:
                    del match[i]
                elif a_in and not b_in:
                    del match_nop[i]
                # both in or both out: keep P1 (match wins below)
    used = set(id(v) for v in match.values()) | set(id(v) for v in match_nop.values())
    # Reject cross-line leaks: a matched ASR word more than 0.5s outside the
    # old line span belongs to a neighbouring line (e.g. L02 "on" matching
    # P1's L01 "on"@22.64). Those words fall back to POS with old-word anchors.
    for i in list(match):
        if match[i]["start"] < L["start"] - 0.5 or match[i]["start"] > L["end"] + 0.5:
            report.append(f"{lid}: rejected cross-line P1 match '{disp[i]}'@{match[i]['start']:.2f}")
            del match[i]
    for i in list(match_nop):
        if match_nop[i]["start"] < L["start"] - 0.5 or match_nop[i]["start"] > L["end"] + 0.5:
            del match_nop[i]
    used = set(id(v) for v in match.values()) | set(id(v) for v in match_nop.values())
    prim_free = [w for w in prim if id(w) not in used]
    nop_free = [w for w in nopw if id(w) not in used]
    old_anchor = old_by_line.get(lid, [])
    line_out = []
    for i, dw in enumerate(disp):
        sw, src = None, None
        if i in match:
            sw, src = match[i], ("STEM" if primary is stem else ("NOP" if primary is nop else "P1"))
        elif i in match_nop:
            sw, src = match_nop[i], "NOP"
        else:
            pool = [w for w in prim_free + nop_free if id(w) not in used_asr]
            if pool:
                anchor = (old_anchor[i]["start"] if i < len(old_anchor)
                          else L["start"] + (L["end"] - L["start"]) * (i + 0.5) / max(len(disp), 1))
                sw = min(pool, key=lambda w: abs(w["start"] - anchor))
                if abs(sw["start"] - anchor) > 0.5:
                    # No ASR word is actually at this position (the word was
                    # misheard/absent in every pass) — the old time (NOP pass)
                    # is the best estimate. Do NOT drag the word to a distant
                    # neighbour's time (L04 "Said": P1 26.78 is a segment-
                    # boundary artefact; NOP/old 27.6 is the onset).
                    nt, ne = anchor, anchor + 0.3
                    line_out.append({"word": dw, "start": round(nt, 3), "end": round(ne, 3),
                                     "src": "OLD"})
                    continue
                src = "POS"
        if sw is None:
            anchor = (old_anchor[i]["start"] if i < len(old_anchor) else L["start"])
            report.append(f"{lid}: NO time for '{dw}' — old anchor {anchor:.2f} used")
            nt, ne = anchor, anchor + 0.3
            src = "OLD"
        else:
            nt, ne = sw["start"], sw["end"]
            used_asr.add(id(sw))
        line_out.append({"word": dw, "start": round(nt, 3), "end": round(ne, 3),
                         "src": src})
    new_lines.append({"id": lid, "section": sec, "text": new_text,
                      "start": line_out[0]["start"], "end": line_out[-1]["end"]})
    # monotonicity: word starts must not decrease within a line
    starts = [w["start"] for w in line_out]
    if any(b < a for a, b in zip(starts, starts[1:])):
        report.append(f"{lid}: NON-MONOTONIC times {[ (w['word'], w['start']) for w in line_out ]}")
    new_words += line_out

# Repair pass: enforce strictly-increasing word starts within each line.
# Two failure modes, repaired differently:
#  (a) OUTLIER: a word far ahead of its predecessor AND past its successor
#      (e.g. L34 'just'@81.8 stole L35's 'Just'; its neighbours are 79.64 /
#      79.96). Replace it with the old-grid anchor (the NOP prior) if that
#      sits between its neighbours, else the neighbours' midpoint. Do NOT
#      touch the words after it — they were right.
#  (b) SMALL SWAP: a word <= its predecessor by a small amount (e.g. L31
#      'now,'@73.98 vs 'Easy'@74.04, 0.06s). Nudge it to the old anchor if
#      monotonic, else prev+0.05s.
# The earlier version repaired (b) by pushing LATER words forward, which
# cascaded L34's correct words into L35's span — that is the bug this
# version fixes.
wi = 0
for L in new_lines:
    n = len(L["text"].split())
    ws = new_words[wi:wi + n]
    oa = old_by_line.get(L["id"], [])
    def anchor_ok(k, t):
        lo = ws[k - 1]["start"] if k > 0 else -1e9
        hi = ws[k + 1]["start"] if k + 1 < len(ws) else 1e9
        return lo < t < hi
    # (a) outliers first
    for k in range(1, len(ws) - 1):
        if ws[k]["start"] > ws[k + 1]["start"] and ws[k]["start"] - ws[k - 1]["start"] > 0.5:
            anchor = oa[k]["start"] if k < len(oa) else None
            if anchor is not None and anchor_ok(k, anchor):
                nt = anchor
            else:
                nt = round((ws[k - 1]["start"] + ws[k + 1]["start"]) / 2, 3)
            report.append(f"{L['id']}: repaired outlier '{ws[k]['word']}' "
                          f"{ws[k]['start']:.2f} -> {nt:.2f}")
            ws[k]["start"] = nt
            ws[k]["src"] = ws[k]["src"] + "+FIX"
            if ws[k]["end"] <= ws[k]["start"]:
                ws[k]["end"] = round(ws[k]["start"] + 0.3, 3)
    # (b) small swaps
    for k in range(1, len(ws)):
        if ws[k]["start"] <= ws[k - 1]["start"]:
            anchor = oa[k]["start"] if k < len(oa) else None
            if anchor is not None and anchor_ok(k, anchor):
                nt = anchor
            else:
                nt = round(ws[k - 1]["start"] + 0.05, 3)
            report.append(f"{L['id']}: repaired out-of-order '{ws[k]['word']}' "
                          f"{ws[k]['start']:.2f} -> {nt:.2f}")
            ws[k]["start"] = nt
            ws[k]["src"] = ws[k]["src"] + "+FIX"
            if ws[k]["end"] <= ws[k]["start"]:
                ws[k]["end"] = round(ws[k]["start"] + 0.3, 3)
    L["start"] = ws[0]["start"]
    L["end"] = ws[-1]["end"]
    wi += n

# Normalise word ends: Whisper sometimes emits a zero-duration word
# (end == start, e.g. L105 'now'@186.34 POS). A zero end makes the line
# end degenerate and the .ass builder drops the word. Give it a 0.3s span.
for w in new_words:
    if w["end"] <= w["start"]:
        w["end"] = round(w["start"] + 0.3, 3)
wi = 0
for L in new_lines:
    n = len(L["text"].split())
    ws = new_words[wi:wi + n]
    L["start"] = ws[0]["start"]
    L["end"] = ws[-1]["end"]
    wi += n

# NOTE 2026-11-12 ~21:40 UTC: Python file writes are EPERM-blocked in this
# session (write() returns Operation not permitted for python and its
# children, while the shell and its direct children write fine). So an
# output path of '-' writes the JSON to stdout for the shell to redirect.
_payload = {"lines": new_lines, "words": new_words, "dropped": dropped,
            "report": report, "params": vars(args)}
if args.out == "-":
    json.dump(_payload, sys.stdout, indent=1)
    sys.stdout.flush()
    # Status lines go to stderr so stdout stays pure JSON.
    _out = sys.stderr
else:
    json.dump(_payload, open(args.out, "w"), indent=1)
    _out = sys.stdout
print(f"WROTE {args.out}: {len(new_lines)} lines, {len(new_words)} words", file=_out)
print(f"dropped: {dropped}", file=_out)
for r in report:
    print("  !", r, file=_out)
print("time sources:", Counter(w["src"] for w in new_words), file=_out)
