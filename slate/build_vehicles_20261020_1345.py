#!/usr/bin/env python3
"""Build v1 generation vehicles for the 13:45 factory run:
B-1304 = 0315 B-2498 "The Served Rope" (last 0315 provisional),
B-1305 = 1315 B-2607 "The Master Key" (bank-FIFO),
B-1306 = 1315 B-2608 "The Checked Coat" (fresh original).
Verbatim PREPRO extracts, Source line stripped, zero citation tokens,
0815 BUG anti-leak clause on every vehicle.
"""
import hashlib, re

SLATE = "/home/hatch/workspace/wubutv-network/slate"

ANTI_LEAK = (
    " BUG-CLASS INSTRUCTION-SET HYGIENE: the generated take carries only the scene "
    "itself — no production-slate overlays, no version tokens, no number tokens, no "
    "meta-text describing the bug's spelling, no spelling-out of the tilde instruction "
    "as words; the corner bug renders as plain text only."
)

# named-lesson phrases that escaped the letter-digit strip on earlier runs
NAMED_LESSON = re.compile(r"(digit lesson|zoom-crop lesson|action-occlusion lesson)", re.I)

def extract(prepro_file, prov):
    text = open(prepro_file).read()
    m = re.search(rf"## === {prov} \(provisional\) — [^\n]*\n\n(.*?)\n\n---\n",
                  text, re.S)
    assert m, f"section {prov} not found in {prepro_file}"
    body = m.group(1)
    # drop the Source:/Setting:/Lore:/Action beats:/Line intro line
    body = re.sub(r"^Source:.*?\n\n", "", body, count=1, flags=re.S)
    # strip parenthetical lesson citation tokens of any letter class: (B-45), (S-16),
    # (B-79: ...), (O-72 ...) — 1045 Q3 CITATION-TOKEN-LEAK + 1315 colon-class hardening
    body = re.sub(r"\([A-Za-z]-\d+[^)]*\)", "", body)
    return body.strip()

SPECS = [
    ("0315", "B-2498", "fire_b1304_20261020_1345_v1.txt"),
    ("1315", "B-2607", "fire_b1305_20261020_1345_v1.txt"),
    ("1315", "B-2608", "fire_b1306_20261020_1345_v1.txt"),
]

for tag, prov, fname in SPECS:
    body = extract(f"{SLATE}/PREPRO_2026-10-20_{tag}.md", prov)
    if not body.endswith(ANTI_LEAK.strip()):
        body += ANTI_LEAK
    leaks = re.findall(r"\([A-Za-z]-\d+[^)]*\)", body)
    assert not leaks, f"citation tokens leaked in {prov}: {leaks}"
    assert not NAMED_LESSON.search(body), f"named-lesson phrase in {prov}"
    assert f" {prov} " not in body and f"({prov})" not in body, f"number token in {prov}"
    p = f"{SLATE}/{fname}"
    open(p, "w").write(body)
    print(fname, hashlib.md5(open(p, "rb").read()).hexdigest(), len(body), "bytes")
