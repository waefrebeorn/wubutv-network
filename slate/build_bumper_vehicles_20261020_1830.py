#!/usr/bin/env python3
"""Build durable fire vehicles for the 2026-10-20 18:30 EDT bumper-factory stall run.
Mirrors the 1815 build conventions (verbatim **SUBJECTS**-header extracts through
NEGATIVE, hardened citation-token strip, native anti-underline-bar stack, 0815 BUG
anti-leak clause). Zero fires — outage queue only.
Claimed numbers (fresh pool, max banked B-1357; B-1300 reserved):
  B-1358 <- 1715 B-2662 "The Pallet's Edge"  (line "Out it goes.")
  B-1359 <- 1715 B-2663 "The Second Mug"    (line "One for each.")
  B-1360 <- 1715 B-2664 "The Floor Held"     (line "Nobody's in a hurry.")
STRUCK at claim (annotated in the 1715 PREPRO, never re-claim):
  1715 B-2660 "The Antenna's Turn" — duplicate of shipped B-801 "The Antenna Turn"
    (mast-turn beat, "the turn is the verdict"; B-801 shipped 2026-10-14).
  1715 B-2661 "The Filed Footage" — duplicate of shipped B-389 "The Empty Slot"
    (basement-archive slot + one object placed 4-6s, "the filing is the verdict").
"""
import re, hashlib, sys

PREPRO = "/home/hatch/workspace/wubutv-network/slate/PREPRO_2026-10-20_1715.md"
SLATE = "/home/hatch/workspace/wubutv-network/slate"

BUG_CLAUSE = ("\n\n---. BUG-CLASS INSTRUCTION-SET HYGIENE: the generated take carries only the scene itself "
              "— no production-slate overlays, no version tokens, no number tokens, no meta-text describing "
              "the bug's spelling, no spelling-out of the tilde instruction as words; the corner bug renders "
              "as plain text only.")

DRAFTS = {
    "B-1358": ("B-2662", "fire_b1358_20261020_1830_v1.txt"),
    "B-1359": ("B-2663", "fire_b1359_20261020_1830_v1.txt"),
    "B-1360": ("B-2664", "fire_b1360_20261020_1830_v1.txt"),
}

text = open(PREPRO).read()

def extract(prov):
    m = re.search(r"## === " + re.escape(prov) + r" \(provisional\).*?\n(.*?)(?=\n---\n## === |\Z)",
                  text, re.S)
    if not m:
        raise SystemExit(f"section {prov} not found")
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
    vehicle = re.sub(r"[ \t]{2,}", " ", vehicle)
    # lineage parentheticals that only carry claim-time adjudication ("flagged") are
    # factory meta-text, not scene direction: drop them outright
    vehicle = re.sub(r";?\s*lineage vs[^.]*— flagged\)?", "", vehicle)
    vehicle = re.sub(r"\(the sanctioned repeat form[^)]*\)",
                     "(the sanctioned repeat form)", vehicle)
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

for num, (prov, fname) in DRAFTS.items():
    vehicle = strip_citation_tokens(extract(prov)) + BUG_CLAUSE
    assert_vehicle(vehicle, num)
    path = f"{SLATE}/{fname}"
    open(path, "w").write(vehicle)
    md5 = hashlib.md5(vehicle.encode()).hexdigest()
    print(f"{num} ({prov}): {fname} md5 {md5} ({len(vehicle)} bytes)")
print("ALL VEHICLES OK — zero citation tokens, bar stack >=2, anti-leak clause present")
