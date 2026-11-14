#!/usr/bin/env python3
"""Build fire vehicles for the 2026-10-18 2200 bumper factory run.

Extracts the GENERATION PROMPT bodies for the 0315 provisionals B-1917
("The Glasshouse") and B-1919 ("The Mash") from PREPRO_2026-10-18_0315.md,
stripping the Source: and Production note: lines, the header, and any
B-digit/parenthetical citation tokens. Writes zero-citation fire vehicles.
"""
import hashlib, re, sys

SRC = "/home/hatch/workspace/wubutv-network/slate/PREPRO_2026-10-18_0315.md"
OUTDIR = "/home/hatch/workspace/wubutv-network/slate"

TARGETS = {
    "B-1917": "fire_b1245_20261018_2200_v1.txt",
    "B-1919": "fire_b1246_20261018_2200_v1.txt",
}

text = open(SRC).read()

def extract(prov):
    # capture from the header line to the next blank-"---" separator
    m = re.search(r"## === " + re.escape(prov) + r" \(provisional\).*?\n(.*?)\n---",
                  text, re.S)
    if not m:
        raise SystemExit("draft %s not found" % prov)
    body = m.group(1).strip()
    lines = []
    skip = True
    for ln in body.splitlines():
        s = ln.strip()
        if skip:
            # drop everything until the first prompt-style paragraph;
            # skip blank lines, the Source: line, the Production note: line
            if not s:
                continue
            if s.startswith("Source:") or s.startswith("Production note:"):
                continue
            if s.startswith("Hand-painted"):
                skip = False
            else:
                continue
        lines.append(ln)
    body = "\n".join(lines).strip()
    # excise B-digit tokens and parenthetical citation tokens (10S-F103 class)
    body = re.sub(r"\bB-\d+\b", "", body)
    body = re.sub(r"\([0-9A-Z]+-[0-9A-Z]+\)", "", body)
    body = re.sub(r"[ \t]{2,}", " ", body)
    return body

for prov, fname in TARGETS.items():
    body = extract(prov)
    assert "Source:" not in body and "Production note:" not in body, prov
    assert "B-1917" not in body and "B-1919" not in body, prov
    assert re.search(r"\([0-9A-Z]+-[0-9A-Z]+\)", body) is None, prov
    path = OUTDIR + "/" + fname
    open(path, "w").write(body + "\n")
    print(fname, hashlib.md5(open(path, "rb").read()).hexdigest(), len(body))
