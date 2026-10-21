#!/usr/bin/env python3
"""Build durable fire vehicles for the 2026-10-20 18:45 EDT bumper-factory stall run.
Mirrors the 1830 build conventions (verbatim **SUBJECTS**-header extracts through
NEGATIVE, hardened citation-token strip, native anti-underline-bar stack, 0815 BUG
anti-leak clause). Zero fires — outage queue only.
Claimed numbers (fresh pool, max banked B-1360; B-1300 reserved):
  B-1361 <- 1715 B-2665 "The Night Sweeper"     (line "The city was here.")
  B-1362 <- 1715 B-2666 "The Blinking Row"      (line "All accounted for.")
  B-1363 <- 1815 B-2667 "The Unhooked Speaker"  (line "The post is the audience.")
Beat-gate at claim (this run): titles + lines grep-zero vs BUMPERS.md + IDEAS_BANK.md
+ all live 10-20 PREPROs + live claims (source PREPRO + bank intake record only).
Lineage DISTINCT per bell-family (carried in the claim record, stripped from vehicles):
  B-2665 vs drafted B-1532 "The Broom Walk" (the PILE vs the PATH — flagged)
  B-2666 vs shipped B-21 "The Blink" (the ROW vs the EYE — flagged)
  B-2667 vs shipped B-1289 "The Hooked Speaker" (the POST-hang vs the WINDOW-hook — flagged)
"""
import re, hashlib, sys

SLATE = "/home/hatch/workspace/wubutv-network/slate"
PREPRO_1715 = f"{SLATE}/PREPRO_2026-10-20_1715.md"
PREPRO_1815 = f"{SLATE}/PREPRO_2026-10-20_1815.md"

BUG_CLAUSE = ("\n\n---. BUG-CLASS INSTRUCTION-SET HYGIENE: the generated take carries only the scene itself "
              "— no production-slate overlays, no version tokens, no number tokens, no meta-text describing "
              "the bug's spelling, no spelling-out of the tilde instruction as words; the corner bug renders "
              "as plain text only.")

DRAFTS = {
    "B-1361": (PREPRO_1715, "B-2665", "fire_b1361_20261020_1845_v1.txt"),
    "B-1362": (PREPRO_1715, "B-2666", "fire_b1362_20261020_1845_v1.txt"),
    "B-1363": (PREPRO_1815, "B-2667", "fire_b1363_20261020_1845_v1.txt"),
}

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
    # bare tokens: kill unwrapped B-NNN / X-NNN refs (lineage carried in the claim record)
    vehicle = re.sub(r"\b[A-Z]{1,4}-\d+\b", "", vehicle)
    # clean the grammatical wreckage a bare-token strip leaves behind
    vehicle = re.sub(r"from\s+'s\b", "from the", vehicle)
    # lineage-only adjudication sentences are factory meta-text, not scene direction
    vehicle = re.sub(r";?\s*[Ll]ineage vs[^.]*?— flagged[^.]*\)?\.?", "", vehicle)
    vehicle = re.sub(r"\s*[Ll]ineage vs[^.]*?flagged\s*\([^)]*\)\.", "", vehicle)
    # collapse any doubled spaces / empty parens left behind
    vehicle = re.sub(r"\(\s*\)", "", vehicle)
    vehicle = re.sub(r"[ \t]{2,}", " ", vehicle)
    return vehicle

def assert_vehicle(v, num):
    hits = v.count("ABSOLUTELY NO BAR, LINE, OR STRIPE")
    assert hits >= 2, f"{num}: bar-stack hits {hits} < 2"
    assert "no underline bar" in v.lower(), f"{num}: missing underline-bar NEGATIVE"
    leftover = re.findall(r"\b[A-Z]{1,4}-\d+\b|\([A-Z]+-\d+", v)
    assert not leftover, f"{num}: citation tokens leaked: {leftover}"
    assert BUG_CLAUSE.strip() in v, f"{num}: anti-leak clause missing"
    assert "~ WuBu ~" in v, f"{num}: wordmark missing"

for num, (prepro, prov, fname) in DRAFTS.items():
    vehicle = strip_citation_tokens(extract(prepro, prov)) + BUG_CLAUSE
    assert_vehicle(vehicle, num)
    path = f"{SLATE}/{fname}"
    open(path, "w").write(vehicle)
    md5 = hashlib.md5(vehicle.encode()).hexdigest()
    print(f"{num} ({prov}): {fname} md5 {md5} ({len(vehicle)} bytes)")
print("ALL VEHICLES OK — zero citation tokens, bar stack >=2, anti-leak clause present")
