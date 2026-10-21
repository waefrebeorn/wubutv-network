#!/usr/bin/env python3
"""Bumper fire-prompt builder — Q2 run 2026-10-13 20:15 EDT (B-702/B-703/B-704).
Adapted from build_fire_1945_bumpers.py. The 1215 drafts run Source and
"Production note:" contiguous (no blank line), so the Source strip is
anchored on the Production-note line (the 1745 gotcha fix), not on \n\n.
Fire-time patch (generic): B-675/B-689 verdict-visibility rider on all three
line-takes — the 1215 drafts predate the corollary; each take's verdict
object gets "stays visible in every frame through 10s, in the line framing
and in the 9.5s verdict frame". Rider failure is B-676 disclose-class.
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
    # 0. strip stray header residue (": GENERATION PROMPT ===") left by section slicing
    stage = re.sub(r"^: GENERATION PROMPT ===\s*", "", stage, count=1)
    # 1. strip the Source paragraph: from "Source:" through the line before
    #    "Production note:" (1215 drafts run them contiguous — 1745 gotcha fix)
    stage = re.sub(r"(?:^|\n)Source:.*?(?=\nProduction note:)", "", stage, count=1, flags=re.S)
    # 2. strip citation-style parens ((B-87), (AD-65), (S-16), ...)
    #    [^)]* (not just [\d/]*) so tokens broken across a newline
    #    ("(B-212\nper-frame condition)") are caught too
    stage = re.sub(r"\s*\((?:B|AD|NE|N|O|L|PA|S|M|A)-\d[^)]*\)", "", stage)
    # 3. strip "(named in ...)" parentheticals of ANY trailing content (B-641)
    stage = re.sub(r"\s*\(named in [^)]*\)", "", stage)
    # 3b. strip any parenthetical containing "named here only"
    stage = re.sub(r"\s*\([^)]*named here only[^)]*\)", "", stage)
    # 3c. strip em-dash self-reference clauses (fire-file strip hygiene lesson)
    stage = re.sub(r"\s*—\s*named in [^.]*\.", "", stage)
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
    # 9. FIRE-TIME PATCH (all three): B-675/B-689 verdict-visibility rider.
    riders = {
        702: ("the placard standing", "8s"),
        703: ("the fader on the tape mark", "7s"),
        704: ("the coin in his hand and the return cup empty", "8s"),
    }
    obj, line_t = riders[num]
    rider = (f" CAMERA: {obj} stays visible in every frame"
             f" through 10s, in the line framing at {line_t} and in the 9.5s verdict frame.")
    if "in the 9.5s verdict frame" not in stage:
        stage = re.sub(
            r"(CAMERA: locked off (?:wide|medium), no push in, no pan, no cuts, no reframing\.)",
            r"\1" + rider,
            stage,
            count=1,
        )
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
    if "no VHS caption" not in stage:
        bad.append("VHS-caption NEGATIVE not present")
    if "in the 9.5s verdict frame" not in stage:
        bad.append("verdict-visibility rider missing")
    if bad:
        raise SystemExit(f"FAILED fire prompt #{num}: " + "; ".join(bad))

PREPRO = "PREPRO_2026-10-13_1215.md"
specs = {
    702: (PREPRO, r"^## === B-702 — THE FOLDED SIGN", r"^## === B-703 — THE DIMMER", "FIRE_B702_2026-10-13_2015.txt"),
    703: (PREPRO, r"^## === B-703 — THE DIMMER", r"^## === B-704 — THE REFUSED COIN", "FIRE_B703_2026-10-13_2015.txt"),
    704: (PREPRO, r"^## === B-704 — THE REFUSED COIN", r"^## === B-705 — THE THIRD DOOR", "FIRE_B704_2026-10-13_2015.txt"),
}

for num, (fname, start, end, out) in specs.items():
    stage = extract(fname, start, end)
    stage = build(stage, num)
    fail_loud(stage, num)
    (SLATE / out).write_text(stage + "\n")
    print(f"OK #{num}: {out} ({len(stage)} chars)")
