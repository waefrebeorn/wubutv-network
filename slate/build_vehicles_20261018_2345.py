#!/usr/bin/env python3
"""Build fire vehicles for the 2026-10-18 23:45 EDT bumper factory run.
Verbatim extracts of the 0415 provisional prompts (Production note stripped,
zero citation tokens). Never hand-assemble a fired prompt — fire the on-disk
vehicle bytes verbatim (FIRE-VEHICLE TRANSCRIPTION-SLIP datum)."""
import hashlib, re

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
    "/home/hatch/workspace/wubutv-network/slate/fire_b1236_20261018_2345_v1.txt": 62,  # 0415 B-1927 THE SEMAPHORE TOWER
    "/home/hatch/workspace/wubutv-network/slate/fire_b1249_20261018_2345_v1.txt": 72,  # 0415 B-1928 THE COBBLER'S BENCH
    "/home/hatch/workspace/wubutv-network/slate/fire_b1250_20261018_2345_v1.txt": 82,  # 0415 B-1929 THE DAIRY
}

for path, line_no in jobs.items():
    write_vehicle(path, extract(line_no))
print("vehicles built")
