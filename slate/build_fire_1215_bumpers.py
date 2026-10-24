#!/usr/bin/env python3
"""Fire-prompt builder — Q2 run 2026-10-14 12:15 EDT (B-867 freed->B-873 draft, B-874, B-875 FIFO).
Strip rules carried over from build_fire_0715_bumpers.py + fire-file strip hygiene lessons:
- strip Source paragraph (anchored on Production note:)
- strip citation-style parens, "named in" parens, "named here only" parens, premise-NN parens,
  em-dash self-reference clauses
- strip full LORE clause and MOTIF clause from CANON
- strengthen corner bug paragraph
Plus the standing three-clause fire-time strip on every fire:
  (1) tight-tilde re-anchor, (2) bug-spacing re-anchor, (3) no-quote-marks/no-apostrophes.
"""
import re, pathlib

SLATE = pathlib.Path.home() / "workspace/wubutv-network/slate"

def extract(fname, num):
    txt = (SLATE / fname).read_text()
    start_pat = r"## === B-%d —" % num
    m = re.search(start_pat + r"(.*?)(?=\n## === )", txt, re.S)
    if not m:
        raise SystemExit(f"FAILED: B-{num} section not found in {fname}")
    return m.group(1).strip()

def build(stage, num):
    # 0. strip stray header residue (": GENERATION PROMPT ===" or " TITLE : GENERATION PROMPT ===")
    stage = re.sub(r"^.*?: GENERATION PROMPT ===\s*", "", stage, count=1)
    # 1. strip Source paragraph through the line before Production note:
    stage = re.sub(r"(?:^|\n)Source:.*?(?=\nProduction note:)", "", stage, count=1, flags=re.S)
    # 1b. strip the Production note paragraph itself (metadata, never fireable)
    stage = re.sub(r"(?:^|\n)Production note:.*?(?=\n\n)", "", stage, count=1, flags=re.S)
    # 2. strip citation-style parens ((B-87), (AD-65), ...)
    stage = re.sub(r"\s*\((?:B|AD|NE|N|O|L|PA|S|M|A)-\d[^)]*\)", "", stage)
    # 2b. strip premise-NN parens ((premise 78) class — L-17 datum)
    stage = re.sub(r"\s*\(premise \d+[^)]*\)", "", stage)
    # 3. strip "(named in ...)" parentheticals of ANY trailing content
    stage = re.sub(r"\s*\(named in [^)]*\)", "", stage)
    # 3b. strip any parenthetical containing "named here only"
    stage = re.sub(r"\s*\([^)]*named here only[^)]*\)", "", stage)
    # 3c. strip em-dash self-reference clauses
    stage = re.sub(r"\s*—\s*named in [^.]*\.", "", stage)
    # 4. strip full LORE clause from CANON
    stage = re.sub(r"\s*LORE\s*—[^.]*\.", "", stage)
    # 5. strip full MOTIF clause
    stage = re.sub(r"\s*MOTIF\s*—[^.]*\.", "", stage)
    # 6. strengthen corner bug paragraph
    stage = re.sub(
        r"Corner bug: two lines of plain WHITE text",
        "Corner bug: EXACTLY TWO lines of plain WHITE text",
        stage,
    )
    # 7. wordmark-plate rider on UNC stages
    if "hoodie" in stage and "no yellow rectangle" not in stage:
        stage = re.sub(
            r"(no badge around the wordmark)",
            r"\1, no background plate behind the wordmark, no yellow rectangle, no patch, no box behind the letters",
            stage,
        )
    # 8. THREE-CLAUSE FIRE-TIME STRIP: tight-tilde + bug-spacing re-anchor + no-quote-marks/no-apostrophes
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
    return stage

def fail_loud(stage, num):
    bad = []
    if re.search(r"(?:^|\n)Source:", stage):
        bad.append("Source: survivor")
    if re.search(r"(?:^|\n)Production note:", stage):
        bad.append("Production-note survivor")
    if re.search(r"\((?:B|AD|NE|N|O|L|PA|S|M|A)-\d[^)]*\)", stage):
        bad.append("citation-token survivor")
    if re.search(r"\(premise \d", stage):
        bad.append("premise-paren survivor")
    if "LORE —" in stage:
        bad.append("LORE survivor")
    if "MOTIF —" in stage:
        bad.append("MOTIF survivor")
    if "(named in " in stage:
        bad.append("named-in survivor")
    if "named here only" in stage:
        bad.append("named-here-only survivor")
    if re.search(r"—\s*named in", stage):
        bad.append("em-dash self-ref survivor")
    if "GENERATION PROMPT ===" in stage:
        bad.append("header residue survivor")
    if "EXACTLY TWO lines of plain WHITE text" not in stage:
        bad.append("bug paragraph not strengthened")
    if "WITH SPACES" not in stage:
        bad.append("bug-spacing re-anchor missing")
    if "no quote marks around the bug" not in stage:
        bad.append("no-quotes clause missing")
    if "no missing tilde" not in stage:
        bad.append("tight-tilde clause missing")
    if bad:
        raise SystemExit(f"FAILED fire prompt #{num}: " + "; ".join(bad))

# (draft_num_in_file, fire_as_num, slug)
specs = [
    (873, 867, "b867_the_ticket_window"),
    (874, 874, "b874_the_whistle"),
    (875, 875, "b875_the_platform_board"),
]

for draft_num, fire_num, slug in specs:
    raw = extract("PREPRO_2026-10-14_0715.md", draft_num)
    stage = build(raw, fire_num)
    fail_loud(stage, fire_num)
    out = SLATE / f"fire_b{fire_num}_20261014_1215.txt"
    out.write_text("10 seconds, 16:9 landscape, 1280x720. " + stage + "\n")
    print(f"wrote {out} ({len(stage)} chars)")
