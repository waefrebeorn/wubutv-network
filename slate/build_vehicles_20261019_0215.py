#!/usr/bin/env python3
"""Build v1 fire vehicles for the 2026-10-19 02:15 EDT bumper-factory run.
Extracts the generation prompt (from 'Hand-painted 2D cartoon' to the end of
the NEGATIVE block) verbatim from the PREPRO drafts. Production note and
Source lines are stripped; zero citation tokens."""
import hashlib, re, sys

SLATE = "/home/hatch/workspace/wubutv-network/slate"
TS = "20261019_0215"

JOBS = [
    # (claimed number, prepro file, provisional number)
    ("b1258", "PREPRO_2026-10-18_0515.md", "B-1946"),  # The Brick Clamp
    ("b1259", "PREPRO_2026-10-18_0615.md", "B-1947"),  # The Bandstand
    ("b1260", "PREPRO_2026-10-18_0615.md", "B-1948"),  # The Milepost
]

def extract(path, prov):
    with open(f"{SLATE}/{path}") as f:
        text = f.read()
    pat = re.compile(r"^## === " + re.escape(prov) + r" \(provisional\).*?$", re.M)
    m = pat.search(text)
    if not m:
        raise SystemExit(f"heading not found: {prov} in {path}")
    start = m.start()
    nxt = text.find("\n## ===", start)
    section = text[start:nxt if nxt != -1 else len(text)]
    hp = section.find("Hand-painted 2D cartoon")
    if hp == -1:
        raise SystemExit(f"style line not found for {prov}")
    body = section[hp:].strip()
    body = re.split(r"\n---\s*$", body, maxsplit=1)[0].strip()
    if not body.endswith("no stinger."):
        raise SystemExit(f"{prov}: vehicle does not end with NEGATIVE block; ends: {body[-60:]!r}")
    if "Production note" in body or re.search(r"^Source:", body, re.M):
        raise SystemExit(f"{prov}: leak of Production note/Source line")
    # zero citation tokens: no B-number tokens inside the vehicle
    for tok in re.findall(r"\bB-\d+\b|\b10S-[A-Z]+\d*\b|\bMEME-[A-Z]+\d*\b", body):
        raise SystemExit(f"{prov}: citation token leaked: {tok}")
    return body

for num, prepro, prov in JOBS:
    body = extract(prepro, prov)
    out = f"{SLATE}/fire_{num}_{TS}_v1.txt"
    with open(out, "w") as f:
        f.write(body + "\n")
    md5 = hashlib.md5(body.encode()).hexdigest()
    print(f"{num} <- {prepro} {prov}: {out} md5 {md5} ({len(body)} chars)")
