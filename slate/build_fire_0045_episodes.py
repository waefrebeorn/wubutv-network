#!/usr/bin/env python3
"""Episode fire-prompt builder — Q3 run 2026-10-14 00:45 EDT (#116/#117/#118).
Adapted from build_fire_2045_episodes.py.
"""
import re, pathlib

SLATE = pathlib.Path.home() / "workspace/wubutv-network/slate"
CIT = r"(?:B|AD|NE|N|O|L|PA|S|M|A)"

def extract(fname, start_pat, end_pat):
    txt = (SLATE / fname).read_text()
    m = re.search(start_pat + r"(.*?)(?=" + end_pat + r")", txt, re.S | re.M)
    if not m:
        raise SystemExit(f"FAILED: section {start_pat!r} not found in {fname}")
    return m.group(1).strip()

def build(stage, num):
    # 1. strip Source paragraph (incl. inline Production note), through next blank line
    stage = re.sub(r"(?:^|\n)Source:.*?(?=\n\n)", "", stage, count=1, flags=re.S)
    # 1b. strip trailing "Production note:" paragraph (meta-guidance: QC
    # instructions, citation tokens, bank notes — never part of the fire prompt)
    stage = re.sub(r"\n+Production note:.*$", "", stage, count=1, flags=re.S)
    # 2. strip citation-style parens, multiline-safe: (B-212\nper-frame condition)
    stage = re.sub(r"\s*\(" + CIT + r"-\d[^)]*\)", "", stage)
    # 2b. strip citation fragments inside descriptive parens: (, B-58), (— B-112)
    stage = re.sub(r",\s*" + CIT + r"-\d[\d/]*(?=\s*\))", "", stage)
    stage = re.sub(r"\s*[—–-]\s*" + CIT + r"-\d[\d/]*(?=\s*\))", "", stage)
    # 2b2. strip parens where the citation token has trailing text before the
    # close: "(describe-it-as-a-dark-lens, B-28 risk neutralized)"
    stage = re.sub(r"\s*\([^()]*,\s*" + CIT + r"-\d[^()]*\)", "", stage)
    # 2c. metadata parens the citation regex misses
    stage = re.sub(r"\s*\(PA-3 stamp lesson\)", "", stage)
    # 2e. bare "per TOKEN" citations + "named in SUBJECTS" parens
    stage = re.sub(r"\s+per\s+" + CIT + r"-\d[\d/]*", "", stage)
    stage = re.sub(r"\s*\([^()]*named in SUBJECTS[^()]*\)", "", stage)
    # 2f. catch-all: any remaining paren whose text contains a citation token
    # (e.g. "(the B-651 count grammar: ...)", "(S-16)", "(the B-707 causal-anchor
    # rule: ...)") — all meta-references per the B-528 lesson, never fire-prompt text
    stage = re.sub(r"\s*\([^()]*" + CIT + r"-\d[\d/]*[^()]*\)", "", stage)
    stage = re.sub(r"\s*\(named here only,? strip at fire\)", "", stage)
    # 4. strengthen corner-bug lock (B-648) + VHS-caption NEGATIVE
    if "Corner bug: two lines of plain WHITE text" in stage:
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
    if re.search(CIT + r"-\d", stage):
        bad.append("citation-token survivor")
    if "named in SUBJECTS" in stage:
        bad.append("'named in SUBJECTS' survivor")
    if "named here only" in stage:
        bad.append("LORE survivor")
    if "EXACTLY TWO lines of plain WHITE text" not in stage:
        bad.append("bug paragraph not strengthened")
    if "no VHS caption" not in stage:
        bad.append("VHS-caption NEGATIVE not present")
    if bad:
        raise SystemExit(f"FAILED fire prompt #{num}: " + "; ".join(bad))

specs = {
    116: ("PREPRO_2026-10-13_2315.md",
          r'^## === #116 — O-61 "THE CORNERSTONE" \(ORIGINALS\) : VOICE STAGE ===',
          r'^## === #117 — O-62 "THE CHARACTER" \(ORIGINALS\) : VOICE STAGE ===',
          "FIRE_E116_2026-10-14_0045.txt"),
    117: ("PREPRO_2026-10-13_2315.md",
          r'^## === #117 — O-62 "THE CHARACTER" \(ORIGINALS\) : VOICE STAGE ===',
          r'^## === #118 — NE-10 "THE ALIGNMENT" \(NETWORK\) : VOICE STAGE ===',
          "FIRE_E117_2026-10-14_0045.txt"),
    118: ("PREPRO_2026-10-13_2315.md",
          r'^## === #118 — NE-10 "THE ALIGNMENT" \(NETWORK\) : VOICE STAGE ===',
          r"^## Bank flips \(this run\)",
          "FIRE_E118_2026-10-14_0045.txt"),
}

for num, (fname, start, end, out) in specs.items():
    stage = extract(fname, start, end)
    stage = build(stage, num)
    fail_loud(stage, num)
    (SLATE / out).write_text(stage + "\n")
    print(f"OK #{num}: {out} ({len(stage)} chars)")
