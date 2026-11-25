#!/usr/bin/env python3
"""Build fire vehicles for the 0815 bumper factory run. Verbatim extracts,
Source line stripped, zero citation tokens. Asserts byte-size band + next-title
leak-zero per the 2026-10-20 MISSING-DELIMITER lesson."""
import re, hashlib, sys

SLATE = "/home/hatch/workspace/wubutv-network/slate/"

JOBS = [
    # (out_vehicle, prepro_file, section_marker, next_section_title_for_leak_check)
    ("fire_b1275_20261020_0815_v1.txt", "PREPRO_2026-10-19_0515.md",
     '## === B-2228 (provisional) — "THE SCULLERY"',
     '## === B-2229 (provisional) — "THE TIDE GAUGE HUT"'),
    ("fire_b1287_20261020_0815_v1.txt", "PREPRO_2026-10-19_0515.md",
     '## === B-2229 (provisional) — "THE TIDE GAUGE HUT"',
     '## === B-2230 (provisional) — "THE OIL STORE"'),
    ("fire_b1288_20261020_0815_v1.txt", "PREPRO_2026-10-19_0515.md",
     '## === B-2230 (provisional) — "THE OIL STORE"',
     '## === B-2231 (provisional) — "THE SAW PIT"'),
]

for out, prepro, marker, next_title in JOBS:
    text = open(SLATE + prepro, encoding="utf-8").read()
    m = re.search(re.escape(marker) + r"[^\n]*\n(.*?)\n---\n", text, re.S)
    if not m:
        print(f"FAIL: section not found or unterminated: {marker}"); sys.exit(1)
    body = m.group(1)
    body = re.sub(r"^Source:.*\n\n?", "", body, count=1, flags=re.M)
    body = body.strip() + "\n"
    if re.search(r"\[[a-f0-9]{8,}\]|【\d+†", body):
        print(f"FAIL: citation token in {out}"); sys.exit(1)
    if next_title.split("—")[0].strip() in body:
        print(f"FAIL: next-section leak in {out}"); sys.exit(1)
    n = len(body.encode("utf-8"))
    if not (4500 <= n <= 8000):
        print(f"FAIL: byte-size {n} out of band for {out}"); sys.exit(1)
    open(SLATE + out, "w", encoding="utf-8").write(body)
    md5 = hashlib.md5(body.encode("utf-8")).hexdigest()
    print(f"OK {out} bytes={n} md5={md5}")

print("ALL VEHICLES BUILT")
