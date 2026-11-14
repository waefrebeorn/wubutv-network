#!/usr/bin/env python3
"""Extract B-2214 (as B-1279) and B-2215 (as B-1281) verbatim from the 0415 PREPRO; strip any Production note lines; write durable fire vehicles."""
import re, hashlib

SRC = "PREPRO_2026-10-19_0415.md"
text = open(SRC).read()

def extract(prov):
    m = re.search(rf"^## === {prov} \(provisional\) — .*? : GENERATION PROMPT ===\n\n(.*?)\n---\n", text, re.S | re.M)
    assert m, f"section {prov} not found"
    body = m.group(1)
    # strip the heading + blank line, strip any Production note lines
    body = re.sub(r"^.*?: GENERATION PROMPT ===\n\n", "", body, count=1)
    body = "\n".join(l for l in body.splitlines() if not l.startswith("Production note:"))
    body = body.strip() + "\n"
    assert "†" not in body and "【" not in body, "citation token leaked"
    return body

specs = {"B-2214": "fire_b1279_20261020_0615_v1.txt", "B-2215": "fire_b1281_20261020_0615_v1.txt"}
for prov, fn in specs.items():
    body = extract(prov)
    open(fn, "w").write(body)
    print(fn, hashlib.md5(body.encode()).hexdigest(), len(body))
