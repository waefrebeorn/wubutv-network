#!/usr/bin/env python3
"""Episode fire-prompt builder — Q3 run 2026-10-13 20:45 EDT (#110/#111/#112).
Adapted from build_fire_1845_episodes.py, plus:
- 2015 lesson: widen citation strip + fail_loud to `-\\d[^)]*` (multiline-safe).
- B-675 verdict-visibility rider on #111 (dark lens) and #112 (roadstud),
  since both verdict objects sit outside the line-time framing.
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

def build(stage, num, rider=None):
    # 1. strip Source paragraph (incl. inline Production note), through next blank line
    stage = re.sub(r"(?:^|\n)Source:.*?(?=\n\n)", "", stage, count=1, flags=re.S)
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
    # 3. strip '(named here only, strip at fire)' LORE bits
    stage = re.sub(r"\s*\(named here only,? strip at fire\)", "", stage)
    # 4. strengthen corner-bug lock (B-648) + VHS-caption NEGATIVE
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
    # 6. B-675 verdict-visibility rider (line-time framing keeps verdict in frame)
    if rider:
        stage = re.sub(
            r"(CAMERA: locked off medium(?:-low)?, no push in, no pan, no cuts, no reframing\.)",
            r"\1 " + rider,
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

RIDERS = {
    111: "The dark unlit indicator lens and the script stay visible in every frame through 10s, in the line framing at 8s and in the 9.5s verdict frame.",
    112: "The roadstud stays visible in every frame through 10s, in the line framing at 8s and in the 9.5s verdict frame.",
}

specs = {
    110: ("PREPRO_2026-10-13_0715.md",
          r"^## #110 \(S-17\)", r"^## #111 \(NE-8\)",
          "FIRE_E110_2026-10-13_2045.txt", None),
    111: ("PREPRO_2026-10-13_0715.md",
          r"^## #111 \(NE-8\)", r"\Z",
          "FIRE_E111_2026-10-13_2045.txt", RIDERS[111]),
    112: ("PREPRO_2026-10-13_0815.md",
          r"^## #112 \(O-46\)", r"^## #113 \(O-47\)",
          "FIRE_E112_2026-10-13_2045.txt", RIDERS[112]),
}

for num, (fname, start, end, out, rider) in specs.items():
    stage = extract(fname, start, end)
    stage = build(stage, num, rider)
    fail_loud(stage, num)
    (SLATE / out).write_text(stage + "\n")
    print(f"OK #{num}: {out} ({len(stage)} chars)")
