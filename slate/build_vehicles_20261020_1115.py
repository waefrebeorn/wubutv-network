#!/usr/bin/env python3
"""Build durable fire vehicles for the 2026-10-20 11:15 EDT bumper factory run.
Extracts verbatim drafts, strips the Source line, strips ALL parenthetical
lesson tokens (B-45 etc. -- the 1045 Q3 CITATION-TOKEN-LEAK lesson: the
generator rendered "(B-45)" as a physical sign; instruction prose stays, only
the parenthetical token goes), appends the 0815 BUG anti-leak clause, writes
vehicles, prints md5s. Firing must use the md5-verified files.
"""
import hashlib, re, sys

STAMP = "20261020_1115"
ANTI_LEAK = ("no meta-text describing the bug's spelling, "
             "no spelling-out of the tilde instruction as words.")
TOKEN_RE = re.compile(r"\s*\((?:B|AD|NE|N|O|L|PA|S|M|A|MEME)-\d+[^)]*\)")

CLAIMS = [
    ("/home/hatch/workspace/wubutv-network/slate/PREPRO_2026-10-20_0115.md",
     "B-1291", "B-2474", "The Grounded Mast"),
    ("/home/hatch/workspace/wubutv-network/slate/PREPRO_2026-10-20_0215.md",
     "B-1295", "B-2475", "The Marked Bay"),
    ("/home/hatch/workspace/wubutv-network/slate/PREPRO_2026-10-20_0215.md",
     "B-1296", "B-2477", "The Salted Step"),
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

    # strip the "Source:" line (zero citation tokens), keep everything else verbatim
    lines = section.split("\n")
    body_lines = [ln for ln in lines if not ln.startswith("Source:")]
    assert len(body_lines) < len(lines), f"Source line not stripped for {prov}"

    body = "\n".join(body_lines).strip()
    assert "NEGATIVE:" in body, f"NEGATIVE missing for {prov}"
    assert body.rstrip().endswith("no stinger."), f"bad NEGATIVE tail for {prov}"

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

    out = f"/home/hatch/workspace/wubutv-network/slate/fire_b{pool[2:]}_{STAMP}_v1.txt"
    open(out, "w").write(vehicle)
    md5 = hashlib.md5(vehicle.encode()).hexdigest()
    print(f"{prov} '{title}' -> {pool}: {out} md5={md5} bytes={len(vehicle)}")
