#!/usr/bin/env python3
"""Build Q3 episode-factory v1 fire vehicles for the 2026-10-20 14:45 EDT run.
Stall-queue build: ZERO fires attempted this run (budget outage, 4th wheel-wide
refusal ~14:28 EDT carries a hard-stop developer instruction; a 429 is a hard stop).
Verbatim PREPRO stage extracts with two strips:
  1. the "Production note:" paragraph (internal, never sent to the tool)
  2. bare parenthetical citation tokens ([A-Z]+-NNN+), e.g. (S-16) — the
     CITATION-TOKEN-LEAK class (10:45 Q3 run 2026-10-20): the generator can leak
     bare tokens into the frame as legible text. Prose mentions ("B-26 exposure
     lesson", "O-72 lesson") are kept per the prose-mention precedent.
"""
import re, hashlib, json, sys

SRC = "/home/hatch/workspace/wubutv-network/slate/PREPRO_2026-10-20_1115.md"
SLATE = "/home/hatch/workspace/wubutv-network/slate"

specs = [
    (220, "512", "L-79", "The Light Spot", 1),
    (221, "513", "O-147", "The Two Sowings", 0),
    (222, "514", "L-80", "The Chamois", 1),
]

text = open(SRC).read()

BARE_TOKEN = re.compile(r" \([A-Z]{1,3}-\d{2,4}\)")
vehicles = {}
for ledger, prov, series, title, expected_tokens in specs:
    m = re.search(
        rf"## === #{prov} \(provisional\) — .*?\n\n(Production note:.*?\n\n)(.*?)(?=\n---\n## === |\Z)",
        text, re.DOTALL)
    if not m:
        print(f"FATAL: stage #{prov} not found"); sys.exit(1)
    prod_note, body = m.group(1), m.group(2)
    assert "Production note:" in prod_note
    stripped, n = BARE_TOKEN.subn("", body)
    assert n == expected_tokens, f"#{prov}: token strip count {n} != expected {expected_tokens}"
    assert not BARE_TOKEN.search(stripped), f"#{prov}: token remains"
    assert "Production note" not in stripped
    vehicle = f"## === #{prov} (provisional) -> ledger #{ledger} — {series} \"{title}\" : VOICE STAGE ===\n\n" + stripped.strip() + "\n"
    path = f"{SLATE}/fire_e{ledger}_20261020_1445_v1.txt"
    open(path, "w").write(vehicle)
    vehicles[ledger] = {"provisional": prov, "series": series, "title": title,
                        "vehicle": path.split("/")[-1],
                        "md5": hashlib.md5(vehicle.encode()).hexdigest(),
                        "bytes": len(vehicle.encode())}
    print(ledger, prov, title, "->", path.split("/")[-1], vehicles[ledger]["md5"], vehicles[ledger]["bytes"])

claim = {
    "factory": "wubutv-episode-factory",
    "run": "2026-10-20 14:45 EDT",
    "claimed_numbers": [220, 221, 222],
    "provisionals": {str(v["provisional"]): k for k, v in vehicles.items()},
    "vehicles": vehicles,
    "status": "STALL QUEUE — video budget outage opened 2026-10-20 ~13:37 EDT persists; "
              "0/6 videos used, zero fires attempted (4th wheel-wide refusal ~14:28 EDT, "
              "hard-stop developer instruction; a 429 is a hard stop). "
              "Fire v1s verbatim sequentially at resume (#220 first).",
}
cp = f"{SLATE}/CLAIM_2026-10-20_1445_episodes.json"
json.dump(claim, open(cp, "w"), indent=2)
print("claim ->", cp)
