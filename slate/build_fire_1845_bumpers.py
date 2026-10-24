#!/usr/bin/env python3
"""Bumper fire-prompt builder — Q2 run 2026-10-14 18:45 EDT (B-896/B-897/B-898).
CORNER BUG LAW head + 0915 FIRE-READY drafts with the standing strip:
Source paragraph gone, Production note gone, citation tokens gone,
LORE/MOTIF clauses gone, (named in ...) gone."""
import re, pathlib

SLATE = pathlib.Path.home() / "workspace/wubutv-network/slate"

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
    txt = (SLATE / "PREPRO_2026-10-14_0915.md").read_text()
    start = rf"^## === B-{num} \u2014"
    m = re.search(start + r"(.*?)(?=" + next_hdr + r")", txt, re.S | re.M)
    if not m:
        raise SystemExit(f"FAILED: section B-{num} not found")
    return m.group(1).strip()

def build(stage, num):
    # 0. strip stray header residue (" THE BREAK ROOM MUG : GENERATION PROMPT ===")
    stage = re.sub(r"^[^:]*: GENERATION PROMPT ===\s*", "", stage, count=1)
    # 1. strip the Source paragraph (anchored at start, through the blank line)
    stage = re.sub(r"^Source:.*?(?=\n\n)", "", stage, count=1, flags=re.S)
    # 2. strip the Production note paragraph
    stage = re.sub(r"\nProduction note:.*?(?=\n\n)", "", stage, count=1, flags=re.S)
    # 3. strip citation-style parens ((B-87), (AD-65), (S-16), (M-1), ...)
    stage = re.sub(r"\s*\((?:B|AD|NE|N|O|L|PA|S|M|A)-\d[\d/]*\)", "", stage)
    # 4. strip "(named in ...)" parentheticals
    stage = re.sub(r"\s*\(named in [^)]*\)", "", stage)
    # 5. strip full LORE clause from CANON
    stage = re.sub(r"\s*LORE\s*\u2014[^.]*\.", "", stage)
    # 6. strip full MOTIF clause
    stage = re.sub(r"\s*MOTIF\s*\u2014[^.]*\.", "", stage)
    stage = stage.strip()
    return stage

def fail_loud(stage, num):
    bad = []
    if re.search(r"(?:^|\n)Source:", stage):
        bad.append("Source: survivor")
    if re.search(r"\nProduction note:", stage):
        bad.append("Production note: survivor")
    if re.search(r"\((?:B|AD|NE|N|O|L|PA|S|M|A)-\d[\d/]*\)", stage):
        bad.append("citation-token survivor")
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
    896: (r"^## === B-897 \u2014", "fire_b896_20261014_1845.txt"),
    897: (r"^## === B-898 \u2014", "fire_b897_20261014_1845.txt"),
    898: (r"^## === B-899 \u2014", "fire_b898_20261014_1845.txt"),
}

for num, (next_hdr, out) in specs.items():
    stage = extract(num, next_hdr)
    stage = build(stage, num)
    fail_loud(stage, num)
    full = CORNER_BUG_LAW + "\n\n" + stage + "\n"
    (SLATE / out).write_text(full)
    print(f"OK #{num}: {out} ({len(full)} chars)")
