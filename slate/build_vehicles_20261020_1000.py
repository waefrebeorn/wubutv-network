#!/usr/bin/env python3
"""Build v1 fire vehicles for the 1000 bumper factory run (B-1275/B-1291).
Pattern: verbatim 0115 B-2463/B-2464 extracts, Source line stripped,
0815 BUG anti-leak clause appended to NEGATIVE; zero citation tokens."""
import hashlib, re, sys

PREPRO = "/home/hatch/workspace/wubutv-network/slate/PREPRO_2026-10-20_0115.md"
SLATE = "/home/hatch/workspace/wubutv-network/slate"

TARGETS = {
    "B-2463": "fire_b1275_20261020_1000_v1.txt",
    "B-2464": "fire_b1291_20261020_1000_v1.txt",
}

ANTI_LEAK = ", no meta-text describing the bug's spelling, no spelling-out of the tilde instruction as words."

text = open(PREPRO).read()
sections = re.split(r"(?m)^## === (B-\d+) \(provisional\)", text)
bodies = {sections[i]: sections[i+1] for i in range(1, len(sections), 2)}

for prov, fname in TARGETS.items():
    if prov not in bodies:
        print(f"MISSING SECTION {prov}"); sys.exit(1)
    body = bodies[prov]
    body = re.sub(r"(?m)^[^\n]*GENERATION PROMPT ===\n", "", body, count=1)
    if "RETIRED PERMANENTLY" in body or "STRUCK" in body.split("\n\n")[0]:
        print(f"{prov}: retirement/strike annotation present — abort"); sys.exit(1)
    body = re.sub(r"(?m)^Source:.*\n", "", body, count=1)
    body = re.split(r"(?m)^## === ", body, maxsplit=1)[0]
    if re.search(r"(?m)^## ===", body):
        print(f"{prov}: leaked section header — abort"); sys.exit(1)
    body = re.sub(r"\n*---\s*$", "", body).strip()
    if not body.startswith("Hand-painted 2D cartoon"):
        print(f"{prov}: unexpected body start: {body[:60]!r}"); sys.exit(1)
    if not body.endswith("no stinger."):
        print(f"{prov}: unexpected NEGATIVE tail: {body[-60:]!r}"); sys.exit(1)
    body = body[:-len("no stinger.")] + "no stinger" + ANTI_LEAK
    if "Source:" in body:
        print(f"{prov}: Source line survived — abort"); sys.exit(1)
    out = f"{SLATE}/{fname}"
    open(out, "w").write(body)
    md5 = hashlib.md5(body.encode()).hexdigest()
    print(f"{prov} -> {fname} md5={md5} bytes={len(body)}")
print("BUILD OK")
