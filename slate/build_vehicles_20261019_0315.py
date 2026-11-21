#!/usr/bin/env python3
"""Build v1 fire vehicles for the 0315 bumper factory run (zero citation tokens)."""
import hashlib, re, sys

SRC = "/home/hatch/workspace/wubutv-network/slate/PREPRO_2026-10-19_0215.md"
OUT = {
    "B-2187": ("/home/hatch/workspace/wubutv-network/slate/fire_b1267_20261019_0315_v1.txt", "1267", "THE PIN"),
    "B-2188": ("/home/hatch/workspace/wubutv-network/slate/fire_b1269_20261019_0315_v1.txt", "1269", "THE POINTED DOOR"),
}

text = open(SRC, encoding="utf-8").read()
lines = text.split("\n")

for prov, (outpath, bnum, title) in OUT.items():
    # find heading line for the provisional
    h = next(i for i, l in enumerate(lines) if prov in l and "GENERATION PROMPT" in l)
    # vehicle starts at the style line ("Hand-painted 2D cartoon")
    s = next(i for i in range(h, len(lines)) if lines[i].startswith("Hand-painted 2D cartoon"))
    # vehicle ends at the line before the next "---"
    e = next(i for i in range(s, len(lines)) if lines[i].strip() == "---")
    vehicle = "\n\n".join(l for l in lines[s:e] if l.strip())
    assert title in vehicle, f"title check failed for {prov}"
    assert "Production note" not in vehicle, f"production note not stripped for {prov}"
    assert not re.search(r"【[^】]*】|\[\d+\]", vehicle), f"citation token in {prov}"
    open(outpath, "w", encoding="utf-8").write(vehicle + "\n")
    md5 = hashlib.md5(vehicle.encode()).hexdigest()
    print(f"B-{bnum} <- {prov} '{title}': {outpath} md5={md5} bytes={len(vehicle)}")
