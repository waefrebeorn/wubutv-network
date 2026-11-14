#!/usr/bin/env python3
"""Episode fire-prompt builder — Q3 run 2026-10-14 14:45 EDT (#137/#138/#139).
Replicates the proven 1245 builder: strip the header line, strip the
Source paragraph + Production note paragraph (same block in the 0215 file),
strip citation parens/fragments, strip '(premise NN)' metadata parens AND
bare 'Premise NN staged.' fragments, strip LORE bits, strengthen bug lock,
wordmark-plate rider where relevant, fail-loud read-back grep.
"""
import re, pathlib

SLATE = pathlib.Path.home() / "workspace/wubutv-network/slate"

def extract(fname, num):
    txt = (SLATE / fname).read_text()
    m = re.search(rf"^## === #{num}\b.*?^Hand-painted(.*?)$(?=\n^## === #\d+|\Z)", txt, re.S | re.M)
    if not m:
        raise SystemExit(f"FAILED: stage #{num} not found in {fname}")
    return ("Hand-painted" + m.group(1)).strip()

def build(stage, num):
    # 1. Source paragraph through the Production note (same block, ends at blank line)
    stage = re.sub(r"(?:^|\n)Source:.*?(?=\n\n)", "", stage, count=1, flags=re.S)
    # 2. citation parens/fragments
    stage = re.sub(r"\s*\((?:B|AD|NE|N|O|L|PA|S|M|A)-\d[\d/]*\)", "", stage)
    stage = re.sub(r",\s*(?:B|AD|NE|N|O|L|PA|S|M|A)-\d[\d/]*(?=\s*\))", "", stage)
    stage = re.sub(r"\s*[—–-]\s*(?:B|AD)-\d[\d/]*(?=\s*\))", "", stage)
    stage = re.sub(r"\s+per\s+(?:B|AD|S)-\d[\d/]*", "", stage)
    stage = re.sub(r"\s*\([^()]*named in SUBJECTS[^()]*\)", "", stage)
    # 3. (premise NN) metadata parens + bare 'Premise NN staged.' fragments
    stage = re.sub(r"\s*\(premise\s+\d+\)", "", stage)
    stage = re.sub(r"\s*[Pp]remise\s+\d+\s+staged\.?", "", stage)
    # 4. LORE bits
    stage = re.sub(r"\s*\(named here only,? strip at fire\)", "", stage)
    # 5. bug lock strengthen
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
    if re.search(r"(?:B|AD|NE|N|O|L|PA|S|M|A)-\d[\d/]*|\(premise\s+\d+\)", stage):
        bad.append("citation-token survivor")
    if re.search(r"[Pp]remise\s+\d+", stage):
        bad.append("'Premise NN' survivor")
    if "Production note:" in stage:
        bad.append("Production note survivor")
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

jobs = [
    ("FIRE_E137_2026-10-14_1445.txt", 137),
    ("FIRE_E138_2026-10-14_1445.txt", 138),
    ("FIRE_E139_2026-10-14_1445.txt", 139),
]
for out, num in jobs:
    stage = extract("PREPRO_2026-10-14_0215.md", num)
    stage = build(stage, num)
    fail_loud(stage, num)
    (SLATE / out).write_text(stage + "\n")
    print(f"OK #{num}: {out} ({len(stage)} chars)")
