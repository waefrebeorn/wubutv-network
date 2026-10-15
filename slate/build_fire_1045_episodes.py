#!/usr/bin/env python3
"""Episode fire-prompt builder — Q3 run 2026-10-14 10:45 EDT (#131/#132/#133).
Replicates the proven 1845 builder: strip the full header line, strip the
Source paragraph (incl. inline Production note), strip citation
parens/fragments, strip '(premise NN)' metadata parens, strip '(named here
only, strip at fire)' LORE bits, strengthen bug lock (B-648), wordmark-plate
rider (AD-65) where relevant, fail-loud read-back grep.
"""
import re, pathlib

SLATE = pathlib.Path.home() / "workspace/wubutv-network/slate"

def extract(fname, num):
    txt = (SLATE / fname).read_text()
    m = re.search(rf"^## === #{num}\b.*?\n(.*?)(?=^## === #\d+|\Z)", txt, re.S | re.M)
    if not m:
        raise SystemExit(f"FAILED: stage #{num} not found in {fname}")
    return m.group(1).strip()

def build(stage, num):
    stage = re.sub(r"(?:^|\n)Source:.*?(?=\n\n)", "", stage, count=1, flags=re.S)
    stage = re.sub(r"\s*\((?:B|AD|NE|N|O|L|PA|S|M|A)-\d[\d/]*\)", "", stage)
    stage = re.sub(r",\s*(?:B|AD|NE|N|O|L|PA|S|M|A)-\d[\d/]*(?=\s*\))", "", stage)
    stage = re.sub(r"\s*[—–-]\s*(?:B|AD)-\d[\d/]*(?=\s*\))", "", stage)
    stage = re.sub(r"\s+per\s+(?:B|AD|S)-\d[\d/]*", "", stage)
    stage = re.sub(r"\s*\([^()]*named in SUBJECTS[^()]*\)", "", stage)
    stage = re.sub(r"\s*\(premise\s+\d+\)", "", stage)
    stage = re.sub(r"\s*\(named here only,? strip at fire\)", "", stage)
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
        bad.append("citationtoken survivor")
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
    ("e131_fireprompt.txt", 131),
    ("e132_fireprompt.txt", 132),
    ("e133_fireprompt.txt", 133),
]
for out, num in jobs:
    stage = extract("PREPRO_2026-10-14_0115.md", num)
    stage = build(stage, num)
    fail_loud(stage, num)
    (SLATE / out).write_text(stage + "\n")
    head = stage[:120].replace("\n", " ")
    print(f"OK #{num}: {out} ({len(stage)} chars)")
    print(f"   head: {head}")
