#!/usr/bin/env python3
"""Build fire vehicles for the 2026-10-19 03:45 EDT Q2 bumper factory run.
Verbatim extracts from PREPRO_2026-10-19_0215.md, Production note stripped,
zero citation tokens. Mapping: 0215 B-2192 -> B-1269, B-2193 -> B-1271, B-2194 -> B-1272."""
import hashlib, re

SRC = "PREPRO_2026-10-19_0215.md"
MAP = {"B-2192": "b1269", "B-2193": "b1271", "B-2194": "b1272"}

text = open(SRC, encoding="utf-8").read()
sections = re.split(r"(?m)^## === (B-\d+) \(provisional\)", text)
bodies = {}
for i in range(1, len(sections), 2):
    bodies[sections[i]] = sections[i + 1]

for prov, slot in MAP.items():
    body = bodies.get(prov)
    assert body is not None, f"missing provisional {prov}"
    start = body.index("Hand-painted 2D cartoon")
    end = body.index("no voiceover, no music, no stinger.") + len("no voiceover, no music, no stinger.")
    vehicle = body[start:end].strip() + "\n"
    assert not re.search(r"\[\d+\]|\[cite", vehicle), f"citation token in {prov}"
    assert "Production note" not in vehicle, f"production note leaked in {prov}"
    out = f"fire_{slot}_20261019_0345_v1.txt"
    open(out, "w", encoding="utf-8").write(vehicle)
    md5 = hashlib.md5(vehicle.encode()).hexdigest()
    print(f"{out}: {len(vehicle)} bytes, md5 {md5}, starts={vehicle[:40]!r}")
print("OK")
