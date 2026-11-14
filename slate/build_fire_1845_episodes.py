#!/usr/bin/env python3
"""Episode fire-prompt builder — Q3 run 2026-10-13 18:45 EDT (#107/#108/#109).
Persists the builder in the repo per the fire-builder hygiene lesson.
Replicates the proven 16:45 builder, plus:
- B-641 rule: strip ANY parenthetical containing "named in SUBJECTS".
- Strip "(PA-3 stamp lesson)" metadata paren (not caught by citation regex).
- Strip citation fragments inside descriptive parens (", B-58", " — B-112", ", M-1").
Steps per stage: strip Source paragraph (incl. inline Production note, per the
16:45 convention that shipped #104-106), strip citation parens, strip
'(named here only, strip at fire)' LORE bits (lore paragraph text kept, per the
16:45 convention), strengthen bug lock (B-648) + wordmark-plate rider (AD-65),
then fail-loud read-back grep.
"""
import re, pathlib

SLATE = pathlib.Path.home() / "workspace/wubutv-network/slate"

def extract(fname, start_pat, end_pat):
    txt = (SLATE / fname).read_text()
    m = re.search(start_pat + r"(.*?)(?=" + end_pat + r")", txt, re.S | re.M)
    if not m:
        raise SystemExit(f"FAILED: section {start_pat!r} not found in {fname}")
    return m.group(1).strip()

def build(stage, num):
    # 1. strip Source paragraph (anchored at string start or newline), through
    #    the next blank line — 0715 drafts run Source into the inline
    #    "Production note:" (same paragraph), so both go together, 16:45-style.
    stage = re.sub(r"(?:^|\n)Source:.*?(?=\n\n)", "", stage, count=1, flags=re.S)
    # 2. strip citation-style parens like (B-87), (B-462), (B-125/126/127)
    stage = re.sub(r"\s*\((?:B|AD|NE|N|O|L|PA|S|M|A)-\d[\d/]*\)", "", stage)
    # 2b. strip citation fragments inside descriptive parens
    stage = re.sub(r",\s*(?:B|AD|NE|N|O|L|PA|S|M|A)-\d[\d/]*(?=\s*\))", "", stage)
    stage = re.sub(r"\s*[—–-]\s*(?:B|AD)-\d[\d/]*(?=\s*\))", "", stage)
    # 2c. strip metadata parens the citation regex misses
    stage = re.sub(r"\s*\(PA-3 stamp lesson\)", "", stage)
    # 2e. strip bare "per TOKEN" citations (not parenthesized)
    stage = re.sub(r"\s+per\s+(?:B|AD|S)-\d[\d/]*", "", stage)
    stage = re.sub(r"\s*\([^()]*named in SUBJECTS[^()]*\)", "", stage)
    # 3. strip '(named here only, strip at fire)' LORE bits
    stage = re.sub(r"\s*\(named here only,? strip at fire\)", "", stage)
    # 4. strengthen corner-bug lock: EXACTLY TWO lines (B-648)
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
    # 5. wordmark-plate rider on UNC stages (AD-65)
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
    return stage

def fail_loud(stage, num):
    bad = []
    if re.search(r"(?:^|\n)Source:", stage):
        bad.append("Source: survivor")
    if re.search(r"(?:B|AD|NE|N|O|L|PA|S|M|A)-\d[\d/]*", stage):
        bad.append("citation-token survivor")
    if "named in SUBJECTS" in stage:
        bad.append("'named in SUBJECTS' survivor")
    if "named here only" in stage:
        bad.append("LORE survivor")
    if "(PA-3" in stage:
        bad.append("PA-3 paren survivor")
    if "EXACTLY TWO lines of plain WHITE text" not in stage:
        bad.append("bug paragraph not strengthened")
    if "no VHS caption" not in stage:
        bad.append("VHS-caption NEGATIVE not present")
    if bad:
        raise SystemExit(f"FAILED fire prompt #{num}: " + "; ".join(bad))

specs = {
    107: ("PREPRO_2026-10-13_0715.md",
          r"^## #107 \(N-59\)", r"^## #108 \(O-45\)",
          "FIRE_E107_2026-10-13_1845.txt"),
    108: ("PREPRO_2026-10-13_0715.md",
          r"^## #108 \(O-45\)", r"^## #109 \(A-17\)",
          "FIRE_E108_2026-10-13_1845.txt"),
    109: ("PREPRO_2026-10-13_0715.md",
          r"^## #109 \(A-17\)", r"^## #110 \(S-17\)",
          "FIRE_E109_2026-10-13_1845.txt"),
}

for num, (fname, start, end, out) in specs.items():
    stage = extract(fname, start, end)
    stage = build(stage, num)
    fail_loud(stage, num)
    (SLATE / out).write_text(stage + "\n")
    head = stage[:200].replace("\n", " ")
    print(f"OK #{num}: {out} ({len(stage)} chars)")
    print(f"   head: {head}")
