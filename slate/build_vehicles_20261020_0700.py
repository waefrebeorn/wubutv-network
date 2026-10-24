#!/usr/bin/env python3
"""Build fire vehicles for bumper factory 0700 run: B-1282 (0415 B-2218), B-1283 (0415 B-2219)."""
import re

PREPRO = "/home/hatch/workspace/wubutv-network/slate/PREPRO_2026-10-19_0415.md"
TARGETS = {
    "B-1282": ("B-2218", "THE CUTTING FLAG", "THE DRY STONE WALL"),
    "B-1283": ("B-2219", "THE DRY STONE WALL", "THE SMOKEHOUSE DOOR"),
}

text = open(PREPRO, encoding="utf-8").read()

for bnum, (prov, title, next_title) in TARGETS.items():
    hdr = "## === " + prov + ' (provisional) \u2014 "' + title + '" : GENERATION PROMPT ==='
    i = text.find(hdr)
    assert i != -1, prov + " header not found"
    rest = text[i + len(hdr):]
    m = re.search(r"\n---\n", rest)
    assert m, prov + ": no section delimiter found"
    body = rest[:m.start()].strip() + "\n"
    out = "/home/hatch/workspace/wubutv-network/slate/fire_" + bnum.lower() + "_20261020_0700_v1.txt"
    size = len(body.encode("utf-8"))
    assert 4500 <= size <= 9000, bnum + ": size " + str(size) + " out of band"
    assert next_title not in body, bnum + ": swallowed next section"
    assert "## ===" not in body, bnum + ": contains a section header"
    assert "2020" not in body and "3010" not in body and "3011" not in body, bnum + ": citation token present"
    body = re.sub(r"(?im)^.*production note.*$\n?", "", body)
    assert body.startswith("Source:"), bnum + ": body does not start with Source:"
    open(out, "w", encoding="utf-8").write(body)
    print(out + ": " + str(size) + " bytes OK")

print("BUILD OK")
