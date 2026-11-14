#!/usr/bin/env python3
"""Bumper fire-prompt builder — Q2 run 2026-10-14 19:30 EDT (B-902/B-903/B-904).
CORNER BUG LAW head + 1015 FIRE-READY drafts with the standing strip:
Source paragraph gone, Production note gone, citation tokens gone
(incl. bare #NNN per the fire-builder gap datum), LORE/MOTIF clauses gone,
(named in ...) gone. Retitles (claim-time, ledger-side only):
B-902 "The Inverted Mug" (from "THE BREAKROOM MUG" — collision w/ shipped B-896),
B-903 "The Released Doors" (from "THE ELEVATOR HOLD" — retired B-867 shape title)."""
import re, pathlib

SLATE = pathlib.Path.home() / "workspace/wubutv-network/slate"
SRC = SLATE / "PREPRO_2026-10-14_1015.md"

CORNER_BUG_LAW = (
    "THE CORNER BUG LAW: the corner bug is exactly two lines of plain white "
    "text printed directly over the picture. Line one reads ~ WuBu ~ \u2014 tilde, space, "
    "W-u-B-u, space, tilde \u2014 with nothing before the first tilde and nothing after the "
    "last tilde: no quote marks, no apostrophes, no doubling, never quoted, the tildes "
    "bare at the line's ends. Line two reads WuBuTV in full, never TV alone. The bug is "
    "printed exactly once per line, bottom-right, every frame, fixed position, never "
    "animated, identical in all 240 frames. The hoodie's wordmark is separate and reads "
    "~WuBu~ tight with no spaces \u2014 the hoodie's tight spacing never applies to the bug."
)

def extract(num, next_hdr):
    txt = SRC.read_text()
    start = rf"^## === B-{num} \u2014"
    m = re.search(start + r"(.*?)(?=" + next_hdr + r")", txt, re.S | re.M)
    if not m:
        raise SystemExit(f"FAILED: section B-{num} not found")
    return m.group(1).strip()

def build(stage):
    stage = re.sub(r"^[^:]*: GENERATION PROMPT ===\s*", "", stage, count=1)
    stage = re.sub(r"^Source:.*?(?=\n\n)", "", stage, count=1, flags=re.S)
    stage = re.sub(r"\nProduction note:.*?(?=\n\n)", "", stage, count=1, flags=re.S)
    stage = re.sub(r"\s*\((?:B|AD|NE|N|O|L|PA|S|M|A)-\d[\d/]*\)", "", stage)
    stage = re.sub(r"\s*\(named in [^)]*\)", "", stage)
    stage = re.sub(r"#\d{3}", "", stage)  # bare citation tokens (fire-builder gap datum)
    stage = re.sub(r"\s*LORE\s*\u2014[^.]*\.", "", stage)
    stage = re.sub(r"\s*MOTIF\s*\u2014[^.]*\.", "", stage)
    return stage.strip()

def fail_loud(stage, num):
    bad = []
    if re.search(r"(?:^|\n)Source:", stage):
        bad.append("Source: survivor")
    if re.search(r"\nProduction note:", stage):
        bad.append("Production note: survivor")
    if re.search(r"\((?:B|AD|NE|N|O|L|PA|S|M|A)-\d[\d/]*\)", stage):
        bad.append("citation-token survivor")
    if re.search(r"#\d{3}", stage):
        bad.append("bare-#NNN survivor")
    if "LORE \u2014" in stage:
        bad.append("LORE survivor")
    if "MOTIF \u2014" in stage:
        bad.append("MOTIF survivor")
    if "(named in " in stage:
        bad.append("named-in survivor")
    if "GENERATION PROMPT ===" in stage:
        bad.append("header residue survivor")
    if "no quote marks, no apostrophes" not in stage:
        bad.append("no-quote-marks strip missing")
    if bad:
        raise SystemExit(f"FAILED fire prompt #{num}: " + "; ".join(bad))

specs = {
    902: (r"^## === B-903 \u2014", "fire_b902_20261014_1930.txt"),
    903: (r"^## === B-904 \u2014", "fire_b903_20261014_1930.txt"),
    904: (r"^## === B-905 \u2014", "fire_b904_20261014_1930.txt"),
}

for num, (next_hdr, out) in specs.items():
    stage = extract(num, next_hdr)
    stage = build(stage)
    fail_loud(stage, num)
    full = CORNER_BUG_LAW + "\n\n" + stage + "\n"
    (SLATE / out).write_text(full)
    print(f"OK #{num}: {out} ({len(full)} chars)")
