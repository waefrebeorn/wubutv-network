#!/usr/bin/env python3
"""Lyric asset-query generator for the Slopcannon asset-search stage.

Reads a verbatim lyrics file (one line per lyric line; optional [mm:ss]
timestamps and [Section] headers) and emits per-section search context plus
the four-rung query ladder from references/asset-search.md.

This is a keyword heuristic, not NLP: it surfaces frequent content words,
capitalised words (role/name candidates), and repeats (motif candidates).
The agent curates the output — it never fires queries blindly, and every
kept reference still passes the SLERM transform and the double/triple
adversarial passes before it reaches a scene plan.

Usage:
    python3 lyric_asset_queries.py lyrics.txt
    python3 lyric_asset_queries.py lyrics.txt -o ASSET_BOARD_DRAFT.md
"""

import argparse
import re
import sys
from collections import Counter

STOP = set("""
a an the and or but of to in on at for with by from as is are was were be been
being i you he she it we they me him her us them my your his its our their
this that these those there here what when where who whom how why not no yes
if then than so such just only also very too can could will would shall should
do does did done have has had am an it its it’s don’t can’t won’t
""".split())

# Small verb seed list: the agent expands this per track from the actual lines.
VERBS = set("""
keep count sell buy build watch wait stand sit leave come go take give hold
keep knock call answer ask tell ask sing dance run walk climb fall rise open
close hide seek find lose win pay owe read write sign erase file stack count
""".split())

TS = re.compile(r"^\s*\[?(\d{1,2}:\d{2})\]?\s*")
SECTION = re.compile(r"^\s*\[(verse|chorus|bridge|intro|outro|pre-chorus|hook|refrain)[^\]]*\]\s*$", re.I)
WORD = re.compile(r"[A-Za-z']+")


def parse(path):
    sections = []
    cur = {"name": "Untitled", "lines": []}
    sections.append(cur)
    with open(path, encoding="utf-8") as f:
        for raw in f:
            line = raw.strip()
            if not line:
                continue
            m = SECTION.match(line)
            if m:
                cur = {"name": m.group(1).capitalize(), "lines": []}
                sections.append(cur)
                continue
            t = TS.match(line)
            stamp = t.group(1) if t else ""
            text = TS.sub("", line) if t else line
            cur["lines"].append((stamp, text))
    return [s for s in sections if s["lines"]]


def analyse(lines):
    words, caps, verbs = [], [], []
    for _, text in lines:
        found = WORD.findall(text)
        for pos, w in enumerate(found):
            lw = w.lower().strip("'")
            if not lw or lw in STOP:
                continue
            # Crude singularisation so "counts"/"keeps" group with "count"/"keep".
            if lw.endswith("s") and len(lw) > 3:
                lw = lw[:-1]
            words.append(lw)
            # Skip sentence-initial words: they are capitalised by position,
            # not because they are a role or name.
            if pos > 0 and w[0].isupper():
                caps.append(w)
            if lw in VERBS:
                verbs.append(lw)
    freq = Counter(words)
    repeats = [w for w, c in freq.most_common() if c >= 2]
    return freq, repeats, sorted(set(caps)), sorted(set(verbs))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("lyrics")
    ap.add_argument("-o", "--out", default=None)
    args = ap.parse_args()
    sections = parse(args.lyrics)
    out = ["# Asset board draft (generated — agent curates before use)\n"]
    out.append("Source lyrics file: `%s`. Each section below is search context, "
               "not a plan. Run the four-rung ladder, keep max 3 references "
               "per scene, and put every kept row through the double/triple "
               "passes in references/asset-search.md.\n" % args.lyrics)
    for i, sec in enumerate(sections, 1):
        freq, repeats, caps, verbs = analyse(sec["lines"])
        top = [w for w, _ in freq.most_common(8)]
        # Motif anchor: first frequent word that is not an action verb
        # and not a generic filler noun.
        anchor = next((w for w in top if w not in VERBS and w not in
                       {"name", "one", "first", "thing", "way", "time", "day"}),
                      top[0] if top else "scene")
        out.append("## Section %d — %s\n" % (i, sec["name"]))
        for stamp, text in sec["lines"]:
            out.append("- %s %s" % (("[" + stamp + "] ") if stamp else "", text))
        out.append("\nSearch context:")
        out.append("- Top content words: %s" % (", ".join(top) or "—"))
        out.append("- Repeats (motif candidates): %s" % (", ".join(repeats) or "—"))
        out.append("- Capitalised (role/name candidates — archetype, never casting): %s" % (", ".join(caps) or "—"))
        out.append("- Action verbs: %s" % (", ".join(verbs) or "—"))
        out.append("\nQuery ladder (fill in the role/object from the lines above):")
        verb = verbs[0] if verbs else "waiting"
        out.append("1. ARCHETYPE: `<role from lines> archetype visual`")
        out.append("2. MOTIF: `%s music video visual`" % anchor)
        out.append("3. TROPE/MECHANIC: `%s music video technique` (e.g. match cut, one-take, doorway pass)" % verb)
        out.append("4. POP-CULTURE MECHANIC: `music video <same beat as these lines> technique` — record mechanic + source page only")
        out.append("\nBoard row to complete: archetype | motif + image URLs | mechanic + WuBu-native translation | FIRST/LAST/NEW/TRANSITION | KEPT/DEMOTED/KILLED + reason\n")
    text = "\n".join(out)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(text)
    else:
        sys.stdout.write(text)


if __name__ == "__main__":
    main()
