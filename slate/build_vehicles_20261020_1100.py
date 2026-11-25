#!/usr/bin/env python3
"""Build durable fire vehicles for the 2026-10-20 11:00 EDT bumper factory run.
Extracts verbatim 0115 B-2471/B-2472/B-2473 draft prompts, strips the Source line
(zero citation tokens), appends the 0815 BUG anti-leak clause, writes vehicles,
prints md5s. Firing must use the md5-verified files, not this script's output."""
import hashlib, re, sys

SRC = "/home/hatch/workspace/wubutv-network/slate/PREPRO_2026-10-20_0115.md"
STAMP = "20261020_1100"
ANTI_LEAK = ("no meta-text describing the bug's spelling, "
             "no spelling-out of the tilde instruction as words.")

CLAIMS = [
    ("B-1291", "B-2471", "The Numbered Shelf"),
    ("B-1292", "B-2472", "The Raised Blind"),
    ("B-1294", "B-2473", "The Emptied Pocket"),
]

text = open(SRC).read()

for pool, prov, title in CLAIMS:
    # extract section: header line through the next "\n---\n" delimiter
    start = text.find(f"## === {prov} (provisional)")
    if start < 0:
        print(f"FAIL: section {prov} not found", file=sys.stderr)
        sys.exit(1)
    end = text.find("\n---\n", start)
    section = text[start:end].strip()

    # expected header prefix check (guards delimiter-swallow bugs, per 0730 lesson)
    expected_head = f"## === {prov} (provisional) — \"{title}\" : GENERATION PROMPT ==="
    first_line = section.split("\n", 1)[0].strip()
    assert first_line == expected_head, f"header mismatch for {prov}: {first_line!r}"

    # strip the "Source:" line (zero citation tokens), keep everything else verbatim
    lines = section.split("\n")
    body_lines = [ln for ln in lines if not ln.startswith("Source:")]
    assert len(body_lines) < len(lines), f"Source line not stripped for {prov}"

    # sanity: prompt must carry the directed line and end its NEGATIVE with "no stinger."
    body = "\n".join(body_lines).strip()
    assert "NEGATIVE:" in body, f"NEGATIVE missing for {prov}"
    assert body.rstrip().endswith("no stinger."), f"unexpected NEGATIVE tail for {prov}: {body[-80:]!r}"

    # append the 0815 BUG anti-leak clause into the NEGATIVE tail
    body = body.rstrip()
    assert body.endswith("no stinger.")
    body = body[:-len("no stinger.")] + "no stinger, " + ANTI_LEAK + "."

    # single-line vehicle (matches the durable vehicle format of prior runs)
    vehicle = re.sub(r"\s*\n\s*", " ", body).strip()
    assert "Source" not in vehicle.split("NEGATIVE:")[0][:400] or "Source:" not in vehicle, \
        f"citation token leak in {prov}"
    assert "Source:" not in vehicle, f"Source citation token in vehicle {prov}"

    out = f"/home/hatch/workspace/wubutv-network/slate/fire_b{pool[2:]}_20261020_1100_v1.txt"
    open(out, "w").write(vehicle)
    md5 = hashlib.md5(vehicle.encode()).hexdigest()
    print(f"{prov} '{title}' -> {pool}: {out} md5={md5} bytes={len(vehicle)}")
