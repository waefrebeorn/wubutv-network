#!/usr/bin/env python3
"""Build fire vehicles for the 2026-10-18 23:15 EDT bumper factory run.
Verbatim extracts of the 0415 provisional prompts (Production note stripped,
zero citation tokens). Never hand-assemble a fired prompt — fire the on-disk
vehicle bytes verbatim (FIRE-VEHICLE TRANSCRIPTION-SLIP datum)."""
import hashlib, re, sys

PREPRO = "/home/hatch/workspace/wubutv-network/slate/PREPRO_2026-10-18_0415.md"

def extract(line_no):
    with open(PREPRO) as f:
        lines = f.readlines()
    text = lines[line_no - 1].rstrip("\n")
    assert text.startswith("Hand-painted 2D cartoon"), f"line {line_no} not the prompt: {text[:60]!r}"
    return text

def write_vehicle(path, text):
    # zero citation tokens
    assert not re.search(r"\[[0-9]+\]|\[citation", text), "citation token found"
    with open(path, "w") as f:
        f.write(text)
    md5 = hashlib.md5(text.encode()).hexdigest()
    print(f"{path}: {len(text)} bytes, md5 {md5}")
    return md5

jobs = {
    # file line of the single-line prompt, per verified layout
    "/home/hatch/workspace/wubutv-network/slate/fire_b1236_20261018_2315_v1.txt": 42,  # 0415 B-1925 THE TIDE MILL
    "/home/hatch/workspace/wubutv-network/slate/fire_b1247_20261018_2315_v1.txt": 52,  # 0415 B-1926 THE LIFEBOAT HOUSE
}
for path, lineno in jobs.items():
    write_vehicle(path, extract(lineno))
print("done — vehicles on disk, fire verbatim")
