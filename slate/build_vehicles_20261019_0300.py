#!/usr/bin/env python3
"""Build v1 fire vehicles for the 0300 bumper-factory run: 0615 B-1956..B-1958 -> B-1266..B-1268."""
import re, hashlib

SRC = "slate/PREPRO_2026-10-18_0615.md"
text = open(SRC).read()

JOBS = [
    ("B-1956", "b1266"),
    ("B-1957", "b1267"),
    ("B-1958", "b1268"),
]

for prov, slug in JOBS:
    m = re.search(r"^## === " + re.escape(prov) + r" \(provisional\).*?\n(.*?)^---$",
                  text, re.M | re.S)
    assert m, f"section not found for {prov}"
    body = m.group(1).strip()
    # Strip Source paragraph and Production note paragraph; vehicle starts at the style paragraph.
    idx = body.find("Hand-painted 2D cartoon")
    assert idx > 0, f"prompt start not found for {prov}"
    vehicle = body[idx:].strip()
    # Zero-citation-token guard: no B-number tokens, no form tokens inside the vehicle.
    assert not re.search(r"\bB-\d{1,4}\b", vehicle), f"citation B-token in {prov} vehicle"
    for tok in ("v1", "v2", "Q1", "Q2", "FIRE-READY"):
        assert tok not in vehicle.split(), f"form token {tok} in {prov} vehicle"
    out = f"slate/fire_{slug}_20261019_0300_v1.txt"
    open(out, "w").write(vehicle + "\n")
    md5 = hashlib.md5(open(out, "rb").read()).hexdigest()
    print(f"{out}: {len(vehicle)} chars, md5 {md5}")
