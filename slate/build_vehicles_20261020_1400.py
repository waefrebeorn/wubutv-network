#!/usr/bin/env python3
"""Build v1 generation vehicles for the 14:00 factory run:
B-1307 = 1315 B-2609 "The Tagged Shirt" (fresh original, dry cleaner),
B-1308 = 1315 B-2610 "The Pestle" (fresh original, apothecary),
B-1309 = 1315 B-2611 "The Unseen Marvel" (fresh original, sideshow tent).
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

NAMED_LESSON = re.compile(
    r"(digit lesson|zoom-crop lesson|action-occlusion lesson|COPYPASTA)", re.I
)

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
    # strip the bare B-141: citation prefix (keep the instruction prose after it)
    body = re.sub(r"\bB-141:\s*", "", body)
    # strip the named-lesson COPYPASTA parenthetical (instruction already in prose)
    body = re.sub(r"\(per the COPYPASTA[^)]*\)", "", body)
    # collapse the double spaces the strips leave behind
    body = re.sub(r" {2,}", " ", body)
    body = re.sub(r" \)", ")", body)
    return body.strip()

SPECS = [
    ("1315", "B-2609", "fire_b1307_20261020_1400_v1.txt"),
    ("1315", "B-2610", "fire_b1308_20261020_1400_v1.txt"),
    ("1315", "B-2611", "fire_b1309_20261020_1400_v1.txt"),
]

for tag, prov, fname in SPECS:
    body = extract(f"{SLATE}/PREPRO_2026-10-20_{tag}.md", prov)
    if not body.endswith(ANTI_LEAK.strip()):
        body += ANTI_LEAK
    leaks = re.findall(r"\([A-Za-z]-\d+[^)]*\)", body)
    assert not leaks, f"citation tokens leaked in {prov}: {leaks}"
    bare = re.findall(r"\b[A-Z]-\d+\b", body)
    assert not bare, f"bare number tokens leaked in {prov}: {bare}"
    assert not NAMED_LESSON.search(body), f"named-lesson phrase in {prov}"
    assert f" {prov} " not in body and f"({prov})" not in body, f"number token in {prov}"
    p = f"{SLATE}/{fname}"
    open(p, "w").write(body)
    print(fname, hashlib.md5(open(p, "rb").read()).hexdigest(), len(body), "bytes")
