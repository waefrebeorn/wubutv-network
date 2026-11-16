#!/usr/bin/env python3
"""Fire-prompt builder — Q2 run 2026-10-14 07:15 EDT (B-814 by number, B-833 by number, B-839 FIFO).
Strip rules carried over from build_fire_2015_bumpers.py + fire-file strip hygiene lessons:
- strip Source paragraph (anchored on Production note:)
- strip citation-style parens, "(named in ...)" multi-clause parens, "named here only" parens,
  em-dash self-reference clauses
- strip full LORE clause and MOTIF clause from CANON
- strengthen corner bug paragraph
Plus the standing three-clause fire-time strip on every fire:
  (1) tight-tilde re-anchor, (2) bug-spacing re-anchor, (3) no-quote-marks/no-apostrophes.
Plus named-failure strengthens:
- B-814: 47-absence strengthen (verdict-inversion datum) baked into first fire.
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
    # 2. strip citation-style parens ((B-87), (AD-65), ...)
    stage = re.sub(r"\s*\((?:B|AD|NE|N|O|L|PA|S|M|A)-\d[^)]*\)", "", stage)
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
    # 8. bug-spacing re-anchor: upgrade B-814's old-form bug paragraph to the full WITH-SPACES form
    if num == 814:
        old_bug = ('line one "~ WuBu ~" with exactly one tilde on each side, never doubled, '
                   'line two "WuBuTV" in full, never "TV" alone;')
        new_bug = ('line one "~ WuBu ~" with exactly one tilde on each side, never doubled, '
                   'the bug\'s line one spelled WITH SPACES — tilde, space, W-u-B-u, space, tilde — '
                   'the hoodie\'s tight ~WuBu~ spacing never applies to the bug; '
                   'line two "WuBuTV" in full, never "TV" alone;')
        if old_bug not in stage:
            raise SystemExit("FAILED B-814: old-form bug paragraph not found for upgrade")
        stage = stage.replace(old_bug, new_bug)
    # 9. THREE-CLAUSE FIRE-TIME STRIP: tight-tilde + bug-spacing re-anchor + no-quote-marks/no-apostrophes
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
    # 10. B-814 named 47-absence strengthen (verdict-inversion datum): the rack holds no 47, named hard
    if num == 814:
        strengthen = (" The verdict is the missing number: at 9.5s the ticket reads '47' glyph-exact in his hand"
                      " and the rack's tags are checked closely — every tag readable, none reading '47',"
                      " no 47 anywhere on the rack, the absence is the verdict.")
        stage = re.sub(r"(SILENT-FRAME GAMBLE:[^.]*\.)", r"\1" + strengthen, stage, count=1)
    # 11. B-839: wordmark gate already disclosed in draft (silhouette); no change needed
    return stage

def fail_loud(stage, num):
    bad = []
    if re.search(r"(?:^|\n)Source:", stage):
        bad.append("Source: survivor")
    if re.search(r"\((?:B|AD|NE|N|O|L|PA|S|M|A)-\d[^)]*\)", stage):
        bad.append("citation-token survivor")
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
    if num == 814 and "no 47 anywhere on the rack" not in stage:
        bad.append("47-absence strengthen missing")
    if bad:
        raise SystemExit(f"FAILED fire prompt #{num}: " + "; ".join(bad))

specs = {
    814: ("PREPRO_2026-10-14_0215.md", "b814-the-ticket-47"),
    833: ("PREPRO_2026-10-14_0415.md", "b833-the-first-anchor"),
    839: ("PREPRO_2026-10-14_0415.md", "b839-the-dish-field"),
}

for num, (fname, slug) in specs.items():
    raw = extract(fname, num)
    stage = build(raw, num)
    fail_loud(stage, num)
    out = SLATE / f"fire_b{num}_20261014_0715.txt"
    out.write_text("10 seconds, 16:9 landscape, 1280x720. " + stage + "\n")
    print(f"wrote {out} ({len(stage)} chars)")
