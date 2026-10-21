#!/usr/bin/env python3
"""Build durable fire vehicles for the 2026-10-20 12:00 EDT bumper factory run.
Extracts verbatim drafts, strips the Source line, strips ALL parenthetical
lesson tokens (the 1045 Q3 CITATION-TOKEN-LEAK lesson), appends the 0815 BUG
anti-leak clause. Prints md5s. Firing must use the md5-verified files.
Claims: B-1295 <- 0215 B-2483 "The Dialed Number" (freed pool number);
B-1296 <- 0215 B-2485 "The Weighed Load" (freed pool number);
B-1298 <- 0215 B-2486 "The Rung Mop" (fresh pool number, max shipped B-1297).
0215 B-2484 "The Returned Coin" struck at claim (title owned by shipped B-466).
"""
import hashlib, re, sys

STAMP = "20261020_1200"
ANTI_LEAK = ("no meta-text describing the bug's spelling, "
             "no spelling-out of the tilde instruction as words.")
TOKEN_RE = re.compile(r"\s*\((?:B|AD|NE|N|O|L|PA|S|M|A|MEME)-\d+[^)]*\)")

CLAIMS = [
    ("/home/hatch/workspace/wubutv-network/slate/PREPRO_2026-10-20_0215.md",
     "B-1295", "B-2483", "The Dialed Number"),
    ("/home/hatch/workspace/wubutv-network/slate/PREPRO_2026-10-20_0215.md",
     "B-1296", "B-2485", "The Weighed Load"),
    ("/home/hatch/workspace/wubutv-network/slate/PREPRO_2026-10-20_0215.md",
     "B-1298", "B-2486", "The Rung Mop"),
]

for src, pool, prov, title in CLAIMS:
    text = open(src).read()
    start = text.find(f"## === {prov} (provisional)")
    if start < 0:
        print(f"FAIL: section {prov} not found in {src}", file=sys.stderr)
        sys.exit(1)
    end = text.find("\n---\n", start)
    section = text[start:end].strip()

    expected_head = f'## === {prov} (provisional) — "{title}" : GENERATION PROMPT ==='
    first_line = section.split("\n", 1)[0].strip()
    assert first_line == expected_head, f"header mismatch for {prov}: {first_line!r}"

    lines = section.split("\n")
    body_lines = [ln for ln in lines if not ln.startswith("Source:")]
    assert len(body_lines) < len(lines), f"Source line not stripped for {prov}"

    body = "\n".join(body_lines).strip()
    assert "NEGATIVE:" in body, f"NEGATIVE missing for {prov}"
    assert body.rstrip().endswith("no stinger."), f"bad NEGATIVE tail for {prov}"

    stripped = TOKEN_RE.sub("", body)
    assert not re.search(r"\((?:B|AD|NE|N|O|L|PA|S|M|A|MEME)-\d+", stripped), \
        f"lesson token survived in {prov}"

    stripped = stripped.rstrip()
    assert stripped.endswith("no stinger.")
    stripped = stripped[:-len("no stinger.")] + "no stinger, " + ANTI_LEAK + "."

    vehicle = re.sub(r"\s*\n\s*", " ", stripped).strip()
    assert "Source:" not in vehicle, f"Source citation token in vehicle {prov}"

    out = f"/home/hatch/workspace/wubutv-network/slate/fire_b{pool[2:]}_{STAMP}_v1.txt"
    open(out, "w").write(vehicle)
    md5 = hashlib.md5(vehicle.encode()).hexdigest()
    print(f"{prov} '{title}' -> {pool}: {out} md5={md5} bytes={len(vehicle)}")
