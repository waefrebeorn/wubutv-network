#!/usr/bin/env python3
"""Bumper fire-prompt builder — Q2 run 2026-10-15 01:00 EDT (B-954/B-955/B-956).
Minimal CORNER BUG LAW head (B-934 leak datum: no spell-out language in the
head — the draft's own bug paragraph holds the full form) + the standing
strip: Source gone, Production note gone, citation tokens gone (incl. bare
#NNN), LORE/MOTIF clauses gone, (named in ...) gone. fail_loud before writing.
Claims: B-954 <- 2315 B-1030 'The Lowered Flag'; B-955 <- 2315 B-1031
'The Stitch'; B-956 <- 0015 B-1032 'The Stored Winter'."""
import re, pathlib

SLATE = pathlib.Path.home() / "workspace/wubutv-network/slate"

MINIMAL_BUG_HEAD = (
    "THE CORNER BUG LAW: line one reads ~ WuBu ~ and line two reads WuBuTV "
    "\u2014 exactly two lines, never three, no other text anywhere near the bug. "
    "The hoodie's wordmark is separate and reads ~WuBu~ tight with no spaces "
    "\u2014 the hoodie's tight spacing never applies to the bug."
)

def extract(src, prov, next_hdr):
    txt = src.read_text()
    start = rf"^## === B-{prov} \u2014"
    m = re.search(start + r"(.*?)(?=" + next_hdr + r")", txt, re.S | re.M)
    if not m:
        raise SystemExit(f"FAILED: section B-{prov} not found in {src.name}")
    return m.group(1).strip()

def build(stage):
    stage = re.sub(r"^[^:]*: GENERATION PROMPT ===\s*", "", stage, count=1)
    stage = re.sub(r"^Source:.*?(?=\n\n)", "", stage, count=1, flags=re.S)
    stage = re.sub(r"\nProduction note:.*?(?=\n\n)", "", stage, count=1, flags=re.S)
    stage = re.sub(r"\s*\((?:B|AD|NE|N|O|L|PA|S|M|A)-\d[\d/]*\)", "", stage)
    stage = re.sub(r"\s*\([^)]*\b(?:B|AD|NE|N|O|L|PA|S|M|A)-\d[\d/]*[^)]*\)", "", stage)
    stage = re.sub(r"\s*\(named in [^)]*\)", "", stage)
    stage = re.sub(r"#\d{3}", "", stage)
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
    if re.search(r"\b(?:B|AD|NE|N|O|L|PA|S|M|A)-\d[\d/]*\b", stage):
        bad.append("letter-prefixed-token survivor")
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
    if bad:
        raise SystemExit(f"FAILED fire prompt #{num}: " + "; ".join(bad))

specs = [
    (954, SLATE / "PREPRO_2026-10-14_2315.md", 1030, r"^## === B-1031 \u2014",
     "fire_b954_20261015_0100.txt"),
    (955, SLATE / "PREPRO_2026-10-14_2315.md", 1031, r"^## === #267 \u2014",
     "fire_b955_20261015_0100.txt"),
    (956, SLATE / "PREPRO_2026-10-15_0015.md", 1032, r"^## === B-1033 \u2014",
     "fire_b956_20261015_0100.txt"),
]

for num, src, prov, next_hdr, out in specs:
    stage = extract(src, prov, next_hdr)
    stage = build(stage)
    fail_loud(stage, num)
    full = MINIMAL_BUG_HEAD + "\n\n" + stage + "\n"
    (SLATE / out).write_text(full)
    print(f"OK #{num}: {out} ({len(full)} chars)")
