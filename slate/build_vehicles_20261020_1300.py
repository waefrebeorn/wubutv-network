#!/usr/bin/env python3
"""Build v1 generation vehicles for the 13:00 factory run:
B-1295 = 0315 B-2492 "The Stacked Log", B-1301 = 0315 B-2493 "The Locked Wheel".
Verbatim PREPRO extracts, Source line stripped, zero citation tokens,
0815 BUG anti-leak clause on every vehicle.
"""
import hashlib, re

PREPRO = "/home/hatch/workspace/wubutv-network/slate/PREPRO_2026-10-20_0315.md"
SLATE = "/home/hatch/workspace/wubutv-network/slate"

ANTI_LEAK = (
    " BUG-CLASS INSTRUCTION-SET HYGIENE: the generated take carries only the scene "
    "itself — no production-slate overlays, no version tokens, no number tokens, no "
    "meta-text describing the bug's spelling, no spelling-out of the tilde instruction "
    "as words; the corner bug renders as plain text only."
)

def extract(prov):
    text = open(PREPRO).read()
    m = re.search(rf"## === {prov} \(provisional\) — [^\n]*\n\n(.*?)\n\n---\n",
                  text, re.S)
    assert m, f"section {prov} not found"
    body = m.group(1)
    # drop the Source:/Setting:/Lore:/Action beats:/Line intro line
    body = re.sub(r"^Source:.*?\n\n", "", body, count=1, flags=re.S)
    # strip parenthetical lesson citation tokens like (B-45), (S-16), (B-82) from instruction prose
    body = re.sub(r"\(B-\d+\)", "", body)
    body = re.sub(r"\(S-\d+\)", "", body)
    # strip any trailing whitespace junk
    return body.strip()

SPECS = [
    ("B-2492", "fire_b1295_20261020_1300_v1.txt"),
    ("B-2493", "fire_b1301_20261020_1300_v1.txt"),
]

for prov, fname in SPECS:
    body = extract(prov)
    if not body.endswith(ANTI_LEAK.strip()):
        body += ANTI_LEAK
    # leak check: no citation tokens remain
    leaks = re.findall(r"\([BS]-\d+\)", body)
    assert not leaks, f"citation tokens leaked in {prov}: {leaks}"
    assert f" {prov} " not in body and f"({prov})" not in body, f"number token in {prov}"
    p = f"{SLATE}/{fname}"
    open(p, "w").write(body)
    print(fname, hashlib.md5(open(p, "rb").read()).hexdigest(), len(body), "bytes")
