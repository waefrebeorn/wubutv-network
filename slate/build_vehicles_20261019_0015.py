#!/usr/bin/env python3
"""Build the B-1253 fire vehicle for the 2026-10-19 00:15 EDT bumper factory run.
Verbatim extract of the 0415 B-1933 provisional prompt (Production note stripped,
zero citation tokens). Never hand-assemble a fired prompt — fire the on-disk
vehicle bytes verbatim (FIRE-VEHICLE TRANSCRIPTION-SLIP datum)."""
import hashlib, re

PREPRO = "/home/hatch/workspace/wubutv-network/slate/PREPRO_2026-10-18_0415.md"

with open(PREPRO) as f:
    lines = f.readlines()
text = lines[122 - 1].rstrip("\n")  # 0415 B-1933 THE POWDER MAGAZINE
assert text.startswith("Hand-painted 2D cartoon"), f"line 122 not the prompt: {text[:60]!r}"
assert "iron door" in text, "wrong provisional extract"
assert not re.search(r"\[[0-9]+\]|\[citation", text), "citation token found"

path = "/home/hatch/workspace/wubutv-network/slate/fire_b1253_20261019_0015_v1.txt"
with open(path, "w") as f:
    f.write(text)
md5 = hashlib.md5(text.encode()).hexdigest()
print(f"{path}: {len(text)} bytes, md5 {md5}")
print("vehicle built")
