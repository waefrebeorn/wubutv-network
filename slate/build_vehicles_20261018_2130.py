#!/usr/bin/env python3
"""Build fire vehicles for the 2026-10-18 21:30 EDT bumper factory run.

Extracts 0315 provisional drafts B-1915 ("The Monoscope") and B-1916
("The Public Metre") as fire vehicles for pool numbers B-1242 and B-1244.
Strips the header (title line, Source paragraph, Production note paragraph),
excises B-digit + parenthetical citation tokens, scans for cross-draft
subject slips (Q1-CROSS-DRAFT-SLIP datum), and md5-sums the result.
"""
import hashlib, re, sys

PREPRO = "/home/hatch/workspace/wubutv-network/slate/PREPRO_2026-10-18_0315.md"
SLATE = "/home/hatch/workspace/wubutv-network/slate"

JOBS = [
    ("1915", "1242", "The Monoscope", "fire_b1242_20261018_2130_v1.txt"),
    ("1916", "1244", "The Public Metre", "fire_b1244_20261018_2130_v1.txt"),
]

FOREIGN = ["fold", "cloth", "fulling", "bucket", "press", "cone", "kiln",
           "saw", "lock", "gate", "oast", "lime", "tannery", "lamp"]

def extract(prov):
    text = open(PREPRO).read()
    start = text.index(f"## === B-{prov} (provisional)")
    seg = text[start:]
    end = seg.index("\n---\n")
    seg = seg[:end]
    lines = seg.split("\n")
    # prompt body begins at the style line
    idx = next(i for i, l in enumerate(lines) if l.startswith("Hand-painted 2D cartoon"))
    body = "\n".join(lines[idx:]).rstrip() + "\n"
    return body

for prov, pool, title, out in JOBS:
    body = extract(prov)
    # excise B-digit tokens and parenthetical production-code tokens
    b_tokens = re.findall(r"\bB-\d+\b", body)
    code_tokens = re.findall(r"\((?:[A-Z0-9]{2,}-[A-Z0-9]+|[0-9]+S-[A-Z0-9]+)\)", body)
    body = re.sub(r"\bB-\d+\b", "", body)
    body = re.sub(r"\((?:[A-Z0-9]{2,}-[A-Z0-9]+|[0-9]+S-[A-Z0-9]+)\)", "", body)
    # subject-slip scan: unexpected foreign subject words in the body
    own = {"1915": ["monoscope", "tube", "card", "transmitter", "glow"],
           "1916": ["etalon", "stick", "wall", "marble", "mark", "parade"]}[prov]
    hits = {w for w in FOREIGN if w in body.lower()} - set(own)
    low = body.lower()
    assert "10s" in low or "0s-10s" in low, f"B-{pool}: timeline clause missing"
    path = f"{SLATE}/{out}"
    open(path, "w").write(body)
    md5 = hashlib.md5(body.encode()).hexdigest()
    print(f"B-{pool} <- 0315 B-{prov} \"{title}\": {len(body)} bytes, md5 {md5}")
    print(f"  excised B-tokens={b_tokens} code-tokens={code_tokens}")
    print(f"  foreign-subject scan: {sorted(hits) if hits else 'CLEAN'}")
    # final zero-token verification
    assert not re.search(r"\bB-\d+\b", body), "B-token remains"
    assert not re.search(r"\((?:[A-Z0-9]{2,}-[A-Z0-9]+|[0-9]+S-[A-Z0-9]+)\)", body), "code token remains"
print("vehicles built OK")
