#!/usr/bin/env python3
"""Fire-prompt builder — Q2 run 2026-10-14 17:00 EDT (B-887 from 0815 FIFO, B-888/B-889 FIFO from 0915).
Strip stack carried from build_fire_1415_bumpers.py:
- positive-form overlay-law CORRECTION paragraph at the prompt HEAD (B-871/B-872 precedent)
- standing three-clause fire-time strip (tight-tilde hoodie / spaced bug / no quotes / no double-print)
- Source + Production note stripped, citation parens stripped, LORE/MOTIF stripped from CANON
"""
import re, pathlib

SLATE = pathlib.Path.home() / "workspace/wubutv-network/slate"

CORRECTION_HEAD = (
    "THE CORNER BUG LAW: the corner bug is exactly two lines of plain white text printed "
    "directly over the picture. Line one reads ~ WuBu ~ — tilde, space, W-u-B-u, space, tilde — "
    "with nothing before the first tilde and nothing after the last tilde: no quote marks, no "
    "apostrophes, no doubling, never quoted, the tildes bare at the line's ends. Line two reads "
    "WuBuTV in full, never TV alone. The bug is printed exactly once per line, bottom-right, "
    "every frame, fixed position, never animated, identical in all 240 frames. The hoodie's "
    "wordmark is separate and reads ~WuBu~ tight with no spaces — the hoodie's tight spacing "
    "never applies to the bug.\n\n"
)

def extract(fname, num):
    txt = (SLATE / fname).read_text()
    m = re.search(r"## === B-%d —(.*?)(?=\n## === )" % num, txt, re.S)
    if not m:
        raise SystemExit("FAILED: B-%d section not found in %s" % (num, fname))
    return m.group(1).strip()

def build(stage):
    stage = re.sub(r"^.*?: GENERATION PROMPT ===\s*", "", stage, count=1)
    stage = re.sub(r"(?:^|\n)Source:.*?(?=\nProduction note:|\n\n)", "", stage, count=1, flags=re.S)
    stage = re.sub(r"(?:^|\n)Production note:.*?(?=\n\n)", "", stage, count=1, flags=re.S)
    stage = re.sub(r"\s*\((?:B|AD|NE|N|O|L|PA|S|M|A)-\d[^)]*\)", "", stage)
    stage = re.sub(r"\s*\(premise \d+[^)]*\)", "", stage)
    stage = re.sub(r"\s*\(named in [^)]*\)", "", stage)
    stage = re.sub(r"\s*\([^)]*named here only[^)]*\)", "", stage)
    stage = re.sub(r"\s*—\s*named in [^.]*\.", "", stage)
    stage = re.sub(r"\s*LORE\s*—[^.]*\.", "", stage)
    stage = re.sub(r"\s*MOTIF\s*—[^.]*\.", "", stage)
    stage = re.sub(
        r"Corner bug: two lines of plain WHITE text",
        "Corner bug: EXACTLY TWO lines of plain WHITE text",
        stage,
    )
    if "hoodie" in stage and "no yellow rectangle" not in stage:
        stage = re.sub(
            r"(no badge around the wordmark)",
            r"\1, no background plate behind the wordmark, no yellow rectangle, no patch, no box behind the letters",
            stage,
        )
    strip = (" no missing tilde, no single-sided wordmark, no flickering tilde,"
             " the hoodie's line reads ~WuBu~ tight with both tildes,"
             " the corner bug's line one reads '~ WuBu ~' WITH SPACES — tilde, space, W-u-B-u, space, tilde"
             " — the hoodie's tight spacing never applies to the bug,"
             " no quote marks around the bug, no apostrophes around the bug,"
             " the bug printed exactly once per line, no double-print, no ghosting,")
    stage = re.sub(
        r"(NEGATIVE: no dissolves, no subtitles,)",
        r"\1" + strip,
        stage,
        count=1,
    )
    return CORRECTION_HEAD + stage

def fail_loud(stage, num):
    bad = []
    if re.search(r"(?:^|\n)Source:", stage):
        bad.append("Source: survivor")
    if re.search(r"(?:^|\n)Production note:", stage):
        bad.append("Production-note survivor")
    if re.search(r"\((?:B|AD|NE|N|O|L|PA|S|M|A)-\d[^)]*\)", stage):
        bad.append("citationtoken survivor")
    if re.search(r"\(premise \d+[^)]*\)", stage):
        bad.append("premise-paren survivor")
    if re.search(r"LORE\s*—", stage):
        bad.append("LORE survivor")
    if re.search(r"MOTIF\s*—", stage):
        bad.append("MOTIF survivor")
    if bad:
        raise SystemExit("B-%d FAIL-LOUD: %s" % (num, "; ".join(bad)))

jobs = [(887, "PREPRO_2026-10-14_0815.md"), (888, "PREPRO_2026-10-14_0915.md"), (889, "PREPRO_2026-10-14_0915.md")]
for num, fname in jobs:
    stage = extract(fname, num)
    fired = build(stage)
    fail_loud(fired, num)
    out = SLATE / ("fire_b%d_20261014_1700.txt" % num)
    out.write_text(fired)
    print("B-%d: %d chars -> %s" % (num, len(fired), out.name))
