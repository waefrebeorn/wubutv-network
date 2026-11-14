#!/usr/bin/env python3
"""Build fire vehicles for the 2026-10-19 03:30 EDT Q2 bumper factory run.
Verbatim extracts from PREPRO_2026-10-19_0215.md, Production note stripped,
zero citation tokens. Mapping: 0215 B-2189 -> B-1266, B-2190 -> B-1269, B-2191 -> B-1270."""
import hashlib, re, sys

SRC = "PREPRO_2026-10-19_0215.md"
MAP = {"B-2189": "b1266", "B-2190": "b1269", "B-2191": "b1270"}

text = open(SRC, encoding="utf-8").read()
sections = re.split(r"(?m)^## === (B-\d+) \(provisional\)", text)
# sections: [pre, id1, body1, id2, body2, ...]
bodies = {}
for i in range(1, len(sections), 2):
    bodies[sections[i]] = sections[i + 1]

for prov, slot in MAP.items():
    body = bodies.get(prov)
    assert body is not None, f"missing provisional {prov}"
    start = body.index("Hand-painted 2D cartoon")
    end = body.index("no voiceover, no music, no stinger.") + len("no voiceover, no music, no stinger.")
    vehicle = body[start:end].strip() + "\n"
    assert "[" not in vehicle.replace("~ WuBu ~", "").replace("[", "") or True  # placeholder no-op
    # zero citation tokens: reject bracket citations like [1], [cite], etc.
    assert not re.search(r"\[\d+\]|\[cite", vehicle), f"citation token in {prov}"
    # Production note must be gone
    assert "Production note" not in vehicle, f"production note leaked in {prov}"
    assert "provisional" not in vehicle[:80], f"header leaked in {prov}"
    out = f"fire_{slot}_20261019_0330_v1.txt"
    open(out, "w", encoding="utf-8").write(vehicle)
    md5 = hashlib.md5(vehicle.encode()).hexdigest()
    print(f"{out}: {len(vehicle)} bytes, md5 {md5}, starts={vehicle[:40]!r}")
print("OK")
