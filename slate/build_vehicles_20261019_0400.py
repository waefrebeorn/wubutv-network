#!/usr/bin/env python3
"""Build fire vehicles for the 2026-10-19 04:00 EDT Q2 bumper factory run.
Verbatim extracts from PREPRO_2026-10-19_0215.md (B-2197, B-2198) and
PREPRO_2026-10-19_0315.md (B-2199), Production note stripped,
zero citation tokens. Mapping: 0215 B-2197 -> B-1269, 0215 B-2198 -> B-1271,
0315 B-2199 -> B-1273."""
import hashlib, re

JOBS = [
    ("PREPRO_2026-10-19_0215.md", "B-2197", "b1269"),
    ("PREPRO_2026-10-19_0215.md", "B-2198", "b1271"),
    ("PREPRO_2026-10-19_0315.md", "B-2199", "b1273"),
]

for src, prov, slot in JOBS:
    text = open(src, encoding="utf-8").read()
    sections = re.split(r"(?m)^## === (B-\d+) \(provisional\)", text)
    bodies = {}
    for i in range(1, len(sections), 2):
        bodies[sections[i]] = sections[i + 1]
    body = bodies.get(prov)
    assert body is not None, f"missing provisional {prov} in {src}"
    start = body.index("Hand-painted 2D cartoon")
    end = body.index("no voiceover, no music, no stinger.") + len("no voiceover, no music, no stinger.")
    vehicle = body[start:end].strip() + "\n"
    assert not re.search(r"\[\d+\]|\[cite", vehicle), f"citation token in {prov}"
    assert "Production note" not in vehicle, f"production note leaked in {prov}"
    out = f"fire_{slot}_20261019_0400_v1.txt"
    open(out, "w", encoding="utf-8").write(vehicle)
    md5 = hashlib.md5(vehicle.encode()).hexdigest()
    print(f"{out}: {len(vehicle)} bytes, md5 {md5}, starts={vehicle[:40]!r}")
print("OK")
