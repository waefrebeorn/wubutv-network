#!/usr/bin/env python3
"""Build durable v1 fire vehicles for the 2026-10-20 18:15 EDT bumper-factory stall run.

FIFO: 1715 batch B-2657/B-2658/B-2659 (B-2655/B-2656 consumed by the 1800 stall
claim; B-2660..B-2666 queued behind).
Claims: B-1355/B-1356/B-1357 (fresh pool numbers; max banked B-1354;
B-1300 reserved, B-1302..B-1354 banked-unshot by live stall claims).

Format (per the 1800 precedent, 1715 new-format drafts):
- verbatim **SUBJECTS**-header extracts through NEGATIVE (no Source paragraph
  exists in the new format)
- hardened citation-token strip: colon-class (B-45:) unwrapped via regex
  keeping the 6-tile QC prose; backstop kills any remaining (X-NNN...) form;
  bare-token strip kills unwrapped B-NNN refs
- UNC drafts (all three): native anti-underline-bar stack — full
  "ABSOLUTELY NO BAR, LINE, OR STRIPE of any kind beneath the six glyphs" in
  SUBJECTS + shortened "...beneath them" in LOAD-BEARING (>=2 ABSOLUTELY hits
  asserted) + "no underline bar" in NEGATIVE
- 0815 BUG anti-leak clause appended; zero citation tokens asserted
"""

import hashlib
import re
from pathlib import Path

SLATE = Path("/home/hatch/workspace/wubutv-network/slate")

# provisional -> (prepro file, format, pool number, slug)
JOBS = [
    ("B-2657", "PREPRO_2026-10-20_1715.md", "new", "B-1355", "the_unit_that_opens"),
    ("B-2658", "PREPRO_2026-10-20_1715.md", "new", "B-1356", "the_vending_machines_exact_change"),
    ("B-2659", "PREPRO_2026-10-20_1715.md", "new", "B-1357", "the_last_cone"),
]

BUG_CLAUSE = (
    "\n\n---. BUG-CLASS INSTRUCTION-SET HYGIENE: the generated take carries only "
    "the scene itself \u2014 no production-slate overlays, no version tokens, "
    "no number tokens, no meta-text describing the bug's spelling, no "
    "spelling-out of the tilde instruction as words; the corner bug renders "
    "as plain text only."
)

CITATION_ANY = re.compile(r"\([A-Za-z]-\d+[^)]*\)")
CITATION_COLON = re.compile(r"\(([A-Za-z]-\d+):\s*([^)]*)\)")
CITATION_BARE = re.compile(r",?\s*\bB-\d+\b")
BAR_ABSOLUTELY = "ABSOLUTELY NO BAR, LINE, OR STRIPE"


def extract(prov: str, prepro_name: str, fmt: str) -> str:
    text = (SLATE / prepro_name).read_text()
    start = text.index(f"## === {prov} (provisional)")
    nxt = re.search(r"\n## === |\n---\n", text[start + 10:])
    end = start + 10 + nxt.start() if nxt else len(text)
    block = text[start:end]
    lines = block.splitlines()
    if fmt == "old":
        body_start = next(
            i for i, ln in enumerate(lines) if ln.startswith("Hand-painted 2D cartoon")
        )
    else:
        body_start = next(i for i, ln in enumerate(lines) if ln.startswith("**SUBJECTS**:"))
    body = "\n".join(lines[body_start:]).rstrip() + "\n"
    return body


def strip_citations(body: str, prov: str):
    body = CITATION_COLON.sub(r"\2", body)
    leftover = CITATION_ANY.findall(body)
    body = CITATION_ANY.sub("", body)
    bare = CITATION_BARE.findall(body)
    body = CITATION_BARE.sub("", body)
    leftover.extend(b.strip(", ") for b in bare if b.strip(", "))
    return body, leftover


for prov, prepro_name, fmt, pool, slug in JOBS:
    body = extract(prov, prepro_name, fmt)
    assert "Source:" not in body, f"{prov}: Source leaked into vehicle"
    body, leftover = strip_citations(body, prov)
    assert not CITATION_ANY.search(body), f"{prov}: citation tokens remain"
    has_unc = "UNC \u2014 heavyset" in body or "UNC - heavyset" in body
    abs_hits = body.count(BAR_ABSOLUTELY)
    if has_unc:
        assert abs_hits >= 2, f"{prov}: UNC draft needs >=2 ABSOLUTELY hits, got {abs_hits}"
        assert "no underline bar" in body, f"{prov}: UNC draft lost the NEGATIVE bar wording"
    else:
        assert "no underline bar anywhere" in body, f"{prov}: no-figure bar wording lost"
        assert abs_hits == 0, f"{prov}: no-figure draft must not carry the stack"
    vehicle = body.rstrip("\n") + BUG_CLAUSE
    assert not CITATION_ANY.search(vehicle), f"{prov}: tokens in final vehicle"
    assert not CITATION_BARE.search(vehicle), f"{prov}: bare tokens in final vehicle"
    out = SLATE / f"fire_{pool.lower().replace('-', '')}_20261020_1815_v1.txt"
    out.write_text(vehicle)
    md5 = hashlib.md5(vehicle.encode()).hexdigest()
    print(f"{out.name}  md5={md5}  bytes={len(vehicle.encode())}  leftover_tokens={leftover}")

print("OK: 3 vehicles built, zero citation tokens asserted.")
