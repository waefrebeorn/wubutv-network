#!/usr/bin/env python3
"""Build durable fire vehicles for the 2026-10-20 11:45 EDT bumper factory run.
Extracts verbatim drafts, strips the Source line, strips ALL parenthetical
lesson tokens (B-45 etc. -- the 1045 Q3 CITATION-TOKEN-LEAK lesson), appends
the 0815 BUG anti-leak clause, restages B-2478's directed line ("It holds." is
owned by shipped B-290 + B-1101) to "The knot holds." (grep-zero). Prints md5s.
Firing must use the md5-verified files.
"""
import hashlib, re, sys

STAMP = "20261020_1145"
ANTI_LEAK = ("no meta-text describing the bug's spelling, "
             "no spelling-out of the tilde instruction as words.")
TOKEN_RE = re.compile(r"\s*\((?:B|AD|NE|N|O|L|PA|S|M|A|MEME)-\d+[^)]*\)")

CLAIMS = [
    ("/home/hatch/workspace/wubutv-network/slate/PREPRO_2026-10-20_0215.md",
     "B-1295", "B-2478", "The Tied Gate",
     ('"It holds."', '"The knot holds."')),
    ("/home/hatch/workspace/wubutv-network/slate/PREPRO_2026-10-20_0215.md",
     "B-1296", "B-2479", "The Rain Barrel",
     None),
    ("/home/hatch/workspace/wubutv-network/slate/PREPRO_2026-10-20_0215.md",
     "B-1297", "B-2482", "The Open Hatch",
     None),
]

for src, pool, prov, title, restage in CLAIMS:
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

    # strip the "Source:" line (zero citation tokens), keep everything else verbatim
    lines = section.split("\n")
    body_lines = [ln for ln in lines if not ln.startswith("Source:")]
    assert len(body_lines) < len(lines), f"Source line not stripped for {prov}"

    body = "\n".join(body_lines).strip()
    assert "NEGATIVE:" in body, f"NEGATIVE missing for {prov}"
    assert body.rstrip().endswith("no stinger."), f"bad NEGATIVE tail for {prov}"

    if restage:
        old, new = restage
        assert old in body, f"restage target {old} not found in {prov}"
        body = body.replace(old, new)

    # strip parenthetical lesson tokens (B-45 etc.) -- instruction prose stays
    stripped = TOKEN_RE.sub("", body)
    assert not re.search(r"\((?:B|AD|NE|N|O|L|PA|S|M|A|MEME)-\d+", stripped), \
        f"lesson token survived in {prov}"

    # append the 0815 BUG anti-leak clause into the NEGATIVE tail
    stripped = stripped.rstrip()
    assert stripped.endswith("no stinger.")
    stripped = stripped[:-len("no stinger.")] + "no stinger, " + ANTI_LEAK + "."

    # single-line vehicle (durable vehicle format of prior runs)
    vehicle = re.sub(r"\s*\n\s*", " ", stripped).strip()
    assert "Source:" not in vehicle, f"Source citation token in vehicle {prov}"
    assert "It holds." not in vehicle, f"old line leaked into {prov} vehicle"

    out = f"/home/hatch/workspace/wubutv-network/slate/fire_b{pool[2:]}_{STAMP}_v1.txt"
    open(out, "w").write(vehicle)
    md5 = hashlib.md5(vehicle.encode()).hexdigest()
    print(f"{prov} '{title}' -> {pool}: {out} md5={md5} bytes={len(vehicle)}")
