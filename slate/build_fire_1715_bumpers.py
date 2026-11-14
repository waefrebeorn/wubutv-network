#!/usr/bin/env python3
"""Bumper fire-prompt builder — Q2 run 2026-10-13 17:15 EDT (B-675/B-676/B-677).
Persists the builder in the repo per the fire-builder hygiene lesson.
Steps per draft: strip Source paragraph (anchored (?:^|\n)Source:),
strip citation-style parens ((B-87), (AD-65), (S-16), ...),
strip "(named in ...)" parentheticals,
strip full LORE and MOTIF clauses from CANON,
strengthen corner-bug lock (B-648 EXACTLY TWO lines; VHS-caption NEGATIVE),
AD-65 wordmark-plate rider on UNC stages,
then fail-loud read-back grep.
"""
import re, pathlib, sys

SLATE = pathlib.Path.home() / "workspace/wubutv-network/slate"

def extract(fname, start_pat, end_pat):
    txt = (SLATE / fname).read_text()
    m = re.search(start_pat + r"(.*?)(?=" + end_pat + r")", txt, re.S | re.M)
    if not m:
        raise SystemExit(f"FAILED: section {start_pat!r} not found in {fname}")
    return m.group(1).strip()

def build(stage, num):
    # 0. strip stray header residue (": GENERATION PROMPT ===") left by section slicing
    stage = re.sub(r"^: GENERATION PROMPT ===\s*", "", stage, count=1)
    stage = re.sub(r"(?:^|\n)Source:.*?(?=\n\n)", "", stage, count=1, flags=re.S)
    # 2. strip citation-style parens
    stage = re.sub(r"\s*\((?:B|AD|NE|N|O|L|PA|S|M|A)-\d[\d/]*\)", "", stage)
    # 3. strip "(named in ...)" parentheticals
    stage = re.sub(r"\s*\(named in [^)]*\)", "", stage)
    # 4. strip full LORE clause from CANON
    stage = re.sub(r"\s*LORE\s*—[^.]*\.", "", stage)
    # 5. strip full MOTIF clause
    stage = re.sub(r"\s*MOTIF\s*—[^.]*\.", "", stage)
    # 6. strengthen corner-bug lock: EXACTLY TWO lines (B-648)
    stage = re.sub(
        r"Corner bug: two lines of plain WHITE text",
        "Corner bug: EXACTLY TWO lines of plain WHITE text",
        stage,
    )
    if "no VHS caption" not in stage:
        stage = re.sub(
            r"(NEGATIVE: no dissolves, no subtitles,)",
            r"\1 no VHS caption, no third line under the bug,",
            stage,
        )
    # 7. wordmark-plate rider on UNC stages (AD-65)
    if "hoodie" in stage and "no yellow rectangle" not in stage:
        stage = re.sub(
            r"(no badge around the wordmark)",
            r"\1, no background plate behind the wordmark, no yellow rectangle, no patch, no box behind the letters",
            stage,
        )
    if "hoodie" in stage and "no dark letters on a yellow panel" not in stage:
        stage = re.sub(
            r"(NEGATIVE: no dissolves, no subtitles,)",
            r"\1 no dark letters on a yellow panel,",
            stage,
        )
    # 8. letters-themselves-on-fabric form lock (AD-65)
    if "hoodie" in stage and "the letters themselves are yellow/gold" not in stage:
        stage = re.sub(
            r"(yellow/gold letters —)",
            r"yellow/gold letters — the letters themselves are yellow/gold printed directly on the black fabric, a bare-fabric print —",
            stage,
        )
    return stage

def fail_loud(stage, num):
    bad = []
    if re.search(r"(?:^|\n)Source:", stage):
        bad.append("Source: survivor")
    if re.search(r"\((?:B|AD|NE|N|O|L|PA|S|M|A)-\d[\d/]*\)", stage):
        bad.append("citation-token survivor")
    if "LORE —" in stage:
        bad.append("LORE survivor")
    if "MOTIF —" in stage:
        bad.append("MOTIF survivor")
    if "(named in " in stage:
        bad.append("named-in survivor")
    if "GENERATION PROMPT ===" in stage:
        bad.append("header residue survivor")
    if "EXACTLY TWO lines of plain WHITE text" not in stage:
        bad.append("bug paragraph not strengthened")
    if "no VHS caption" not in stage:
        bad.append("VHS-caption NEGATIVE not present")
    if bad:
        raise SystemExit(f"FAILED fire prompt #{num}: " + "; ".join(bad))

PREPRO = "PREPRO_2026-10-13_1015.md"
specs = {
    675: (PREPRO, r"^## === B-675 — THE CEILING'S HOURS", r"^## === B-676 — THE SWEEPER'S LEAF", "FIRE_B675_2026-10-13_1715.txt"),
    676: (PREPRO, r"^## === B-676 — THE SWEEPER'S LEAF", r"^## === B-677 — THE FORGOTTEN CHOCK", "FIRE_B676_2026-10-13_1715.txt"),
    677: (PREPRO, r"^## === B-677 — THE FORGOTTEN CHOCK", r"^## === B-678 — THE STUCK FLOOR", "FIRE_B677_2026-10-13_1715.txt"),
}

for num, (fname, start, end, out) in specs.items():
    stage = extract(fname, start, end)
    stage = build(stage, num)
    fail_loud(stage, num)
    (SLATE / out).write_text(stage + "\n")
    print(f"OK #{num}: {out} ({len(stage)} chars)")
