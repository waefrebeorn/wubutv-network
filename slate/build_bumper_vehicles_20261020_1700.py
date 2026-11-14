#!/usr/bin/env python3
"""Build durable v1 fire vehicles for the 2026-10-20 17:00 EDT bumper-factory stall run.

FIFO: 1515 batch B-2642 (the 1615 batch B-2643..B-2654 queues behind).
Claims: B-1340/B-1341/B-1342 (fresh pool numbers; max banked B-1339;
B-1300 reserved, B-1302..B-1339 banked-unshot by live stall claims).

Format (per the 1645 precedent):
- verbatim PREPRO GENERATION PROMPT extract, Source paragraph stripped
- hardened citation-token strip: colon-class (B-45: prose) unwrapped via regex
  keeping the 6-tile QC prose; backstop kills any remaining (X-NNN...) form;
  bare-token strip kills unwrapped B-NNN refs (the B-22 class)
- UNC drafts: native anti-underline-bar stack asserted verbatim exactly 2x
  (SUBJECTS + LOAD-BEARING), no strengthening pass
- hands-only drafts: NEGATIVE 'no underline bar anywhere' kept verbatim 1x
- 0815 BUG anti-leak clause appended; zero citation tokens asserted
"""

import hashlib
import re
from pathlib import Path

SLATE = Path("/home/hatch/workspace/wubutv-network/slate")

# provisional -> (prepro file, pool number, slug)
JOBS = [
    ("B-2642", "PREPRO_2026-10-20_1515.md", "B-1340", "the_walked_cloister"),
    ("B-2643", "PREPRO_2026-10-20_1615.md", "B-1341", "the_sub_cellarer"),
    ("B-2644", "PREPRO_2026-10-20_1615.md", "B-1342", "the_orb_on_the_machine"),
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
BAR_STACK = "ABSOLUTELY NO BAR, LINE, OR STRIPE of any kind beneath the six glyphs"


def extract(prov: str, prepro_name: str) -> str:
    text = (SLATE / prepro_name).read_text()
    start = text.index(f"## === {prov} (provisional)")
    nxt = re.search(r"\n## === ", text[start + 10:])
    end = start + 10 + nxt.start() if nxt else len(text)
    block = text[start:end]
    lines = block.splitlines()
    body_start = next(
        i for i, ln in enumerate(lines) if ln.startswith("Hand-painted 2D cartoon")
    )
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


for prov, prepro_name, pool, slug in JOBS:
    body = extract(prov, prepro_name)
    assert "Source:" not in body.split("\n")[0], f"{prov}: Source line leaked"
    body, leftover = strip_citations(body, prov)
    assert not CITATION_ANY.search(body), f"{prov}: citation tokens remain"
    stack_hits = body.count(BAR_STACK)
    hands_only = "Hands only" in body
    if hands_only:
        assert "no underline bar anywhere" in body, f"{prov}: hands-only bar wording lost"
        assert stack_hits == 0, f"{prov}: hands-only must not carry the 2x stack"
    else:
        assert stack_hits == 2, f"{prov}: UNC draft must carry exactly 2x stack, got {stack_hits}"
    vehicle = body.rstrip("\n") + BUG_CLAUSE
    assert not CITATION_ANY.search(vehicle), f"{prov}: tokens in final vehicle"
    assert not CITATION_BARE.search(vehicle), f"{prov}: bare tokens in final vehicle"
    out = SLATE / f"fire_{pool.lower().replace('-', '')}_20261020_1700_v1.txt"
    out.write_text(vehicle)
    md5 = hashlib.md5(vehicle.encode()).hexdigest()
    print(f"{out.name}  md5={md5}  bytes={len(vehicle.encode())}  leftover_tokens={leftover}")

print("OK: 3 vehicles built, zero citation tokens asserted.")
