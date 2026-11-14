#!/usr/bin/env python3
"""Extract B-2216 (as B-1279) and B-2217 (as B-1282) verbatim from the 0415 PREPRO; strip any Production note lines; write durable fire vehicles."""
import re, hashlib

SRC = "PREPRO_2026-10-19_0415.md"
text = open(SRC).read()

def extract(prov):
    m = re.search(rf"^## === {prov} \(provisional\) — .*? : GENERATION PROMPT ===\n\n(.*?)\n---\n", text, re.S | re.M)
    assert m, f"section {prov} not found"
    body = m.group(1)
    body = re.sub(r"^.*?: GENERATION PROMPT ===\n\n", "", body, count=1)
    body = "\n".join(l for l in body.splitlines() if not l.startswith("Production note:"))
    body = body.strip() + "\n"
    assert "†" not in body and "【" not in body, "citation token leaked"
    return body

specs = {"B-2216": "fire_b1279_20261020_0645_v1.txt", "B-2217": "fire_b1282_20261020_0645_v1.txt"}
for prov, fn in specs.items():
    body = extract(prov)
    open(fn, "w").write(body)
    print(fn, hashlib.md5(body.encode()).hexdigest(), len(body))
