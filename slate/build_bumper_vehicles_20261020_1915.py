#!/usr/bin/env python3
"""Build durable fire vehicles for the 2026-10-20 19:15 EDT bumper-factory stall run.
Mirrors the 1845/1900 build conventions (verbatim **SUBJECTS**-header extracts through
NEGATIVE, hardened citation-token strip, native anti-underline-bar stack on the UNC
drafts, 0815 BUG anti-leak clause). Zero fires — outage queue only.
Claimed numbers (fresh pool, max claimed B-1366; B-1300 reserved):
  B-1367 <- 1815 B-2671 "The Reset Crank"  (line "Back to zero.")
  B-1368 <- 1815 B-2672 "The Brass Weight" (line "It weighs true.")
  B-1369 <- 1815 B-2673 "The Muster Board" (line "All present.")
Beat-gate at claim (this run): titles + lines grep-zero vs BUMPERS.md + IDEAS_BANK.md
+ all live 10-20 PREPROs + live claims, with adjudications:
  "The Muster Board": IDEAS_BANK hit = "muster board" PROSE inside EPISODE draft
    "The Volunteer Roster" (different medium, title zero-hit exact) — non-conflict.
  "All present.": BUMPERS.md hits all = "bug strip all present" QC PROSE in old
    ledger rows — never a directed line — non-conflict.
  "The Reset Crank" / "Back to zero." / "The Brass Weight" / "It weighs true.":
    all grep-zero everywhere (1815 source PREPRO only).
Lineage DISTINCT per bell-family (carried in the claim record, stripped from vehicles):
  B-2671 vs shipped B-1235 "The Gas Gauge" (the CRANK vs the GAUGE — the zeroing vs
    the rising — flagged); vs [READY] "The Five Cents" (the CRANK vs the HAND-RESET
    — flagged)
  B-2672 vs [READY] "The Honest Bushel" (the WEIGHT vs the STRIKE — flagged)
  B-2673 vs [READY] "The Fire Mark" (the MUSTER vs the PLAQUE — the board vs the
    mark — flagged)
"""
import re, hashlib, sys

SLATE = "/home/hatch/workspace/wubutv-network/slate"
PREPRO_1815 = f"{SLATE}/PREPRO_2026-10-20_1815.md"

BUG_CLAUSE = ("\n\n---. BUG-CLASS INSTRUCTION-SET HYGIENE: the generated take carries only the scene itself "
              "— no production-slate overlays, no version tokens, no number tokens, no meta-text describing "
              "the bug's spelling, no spelling-out of the tilde instruction as words; the corner bug renders "
              "as plain text only.")

# (number, provisional, vehicle file, is_unc_draft)
DRAFTS = [
    ("B-1367", "B-2671", "fire_b1367_20261020_1915_v1.txt", True),
    ("B-1368", "B-2672", "fire_b1368_20261020_1915_v1.txt", True),
    ("B-1369", "B-2673", "fire_b1369_20261020_1915_v1.txt", True),
]

def extract(prepro, prov):
    text = open(prepro).read()
    m = re.search(r"## === " + re.escape(prov) + r" \(provisional\).*?\n(.*?)(?=\n---\n\s*## === |\Z)",
                  text, re.S)
    if not m:
        raise SystemExit(f"section {prov} not found in {prepro}")
    body = m.group(1)
    i = body.find("**SUBJECTS**:")
    if i < 0:
        raise SystemExit(f"SUBJECTS not found in {prov}")
    return body[i:].strip()

def strip_citation_tokens(vehicle):
    # colon-class: (B-79: ...) -> unwrap, keep the QC prose inside
    vehicle = re.sub(r"\((?:[A-Z]+-)?B-\d+\s*:\s*([^)]*)\)", r"(\1)", vehicle)
    # backstop: any remaining (X-NNN ...) parenthetical form
    vehicle = re.sub(r"\([A-Z]{1,4}-\d+[^)]*\)", "", vehicle)
    # cf. cross-refs (e.g. "cf. B-2669") are lineage tokens, not scene direction
    vehicle = re.sub(r"cf\.\s*", "", vehicle)
    # bare tokens: kill unwrapped B-NNN / X-NNN refs (lineage carried in the claim record)
    vehicle = re.sub(r"\b[A-Z]{1,4}-\d+\b", "", vehicle)
    # clean the grammatical wreckage a bare-token strip leaves behind
    vehicle = re.sub(r"from\s+'s\b", "from the", vehicle)
    # lineage-only adjudication sentences are factory meta-text, not scene direction
    vehicle = re.sub(r";?\s*[Ll]ineage vs[^.]*?— flagged[^.]*\)?\.?", "", vehicle)
    vehicle = re.sub(r"\s*[Ll]ineage vs[^.]*?flagged\s*\([^)]*\)\.", "", vehicle)
    # collapse any doubled spaces / empty parens / stranded commas left behind
    vehicle = re.sub(r",\s*\)", ")", vehicle)
    vehicle = re.sub(r"\(\s*\)", "", vehicle)
    vehicle = re.sub(r"[ \t]{2,}", " ", vehicle)
    return vehicle

def assert_vehicle(v, num, is_unc):
    if is_unc:
        hits = v.count("ABSOLUTELY NO BAR, LINE, OR STRIPE")
        assert hits >= 2, f"{num}: bar-stack hits {hits} < 2"
        assert "no underline bar" in v.lower(), f"{num}: missing underline-bar NEGATIVE"
    leftover = re.findall(r"\b[A-Z]{1,4}-\d+\b|\([A-Z]+-\d+", v)
    assert not leftover, f"{num}: citation tokens leaked: {leftover}"
    assert "cf." not in v, f"{num}: cf. cross-ref leaked"
    assert BUG_CLAUSE.strip() in v, f"{num}: anti-leak clause missing"
    assert "~ WuBu ~" in v, f"{num}: wordmark missing"
    assert 2000 < len(v) < 8000, f"{num}: suspect vehicle size {len(v)}"

for num, prov, fname, is_unc in DRAFTS:
    vehicle = strip_citation_tokens(extract(PREPRO_1815, prov)) + BUG_CLAUSE
    assert_vehicle(vehicle, num, is_unc)
    path = f"{SLATE}/{fname}"
    open(path, "w").write(vehicle)
    md5 = hashlib.md5(vehicle.encode()).hexdigest()
    print(f"{num} ({prov}): {fname} md5 {md5} ({len(vehicle)} bytes, unc={is_unc})")
print("ALL VEHICLES OK — zero citation tokens, anti-leak clause present")
