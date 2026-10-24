#!/usr/bin/env python3
"""Build Q2 bumper factory vehicles for the 2026-10-20 12:15 EDT run.
B-1296 (freed pool, B-814 precedent) <- 0315 B-2487 "The Sorted Bin" (FIFO)
B-1299 (fresh pool, max shipped B-1298) <- 0315 B-2488 "The Cut Key" (FIFO)
Convention: verbatim PREPRO extract, Source line stripped, parenthetical
B-NNN lesson citation tokens stripped (1045 Q3 CITATION-TOKEN-LEAK lesson),
0815 BUG anti-leak clause appended, single-line TEXT-ONLY vehicle."""
import re, hashlib, sys

PREPRO = "/home/hatch/workspace/wubutv-network/slate/PREPRO_2026-10-20_0315.md"
OUTDIR = "/home/hatch/workspace/wubutv-network/slate"
LEAK_CLAUSE = "no meta-text describing the bug's spelling, no spelling-out of the tilde instruction as words."

text = open(PREPRO).read()
jobs = {
    "b1296": ("B-2487", "fire_b1296_20261020_1215_v1.txt"),
    "b1299": ("B-2488", "fire_b1299_20261020_1215_v1.txt"),
}

for pool, (prov, fname) in jobs.items():
    start = text.index(f"## === {prov} (provisional)")
    # section runs until the next '## === ' or a lone '---' terminator after the header
    seg = text[start:]
    end_markers = [m.start() for m in re.finditer(r"\n## === B-", seg)]
    end = min([e for e in end_markers if e > 10], default=len(seg))
    section = seg[:end].strip()
    # drop trailing '---' rule
    section = re.sub(r"\n---+\s*$", "", section).strip()
    # strip the "Source: ..." lead line
    lines = section.split("\n")
    header = lines[0]
    body_lines = [l for l in lines[1:] if not l.startswith("Source:")]
    body = " ".join(l.strip() for l in body_lines if l.strip())
    body = re.sub(r"\s+", " ", body)
    # strip parenthetical B-NNN citation tokens (1045 Q3 lesson)
    toks = re.findall(r"\(B-\d+\)", body)
    body = re.sub(r"\s*\(B-\d+\)", "", body)
    # append anti-leak clause to the NEGATIVE list (before final period)
    if not body.rstrip().endswith(LEAK_CLAUSE):
        body = body.rstrip().rstrip(".") + ", " + LEAK_CLAUSE.rstrip(".") + "."
    vehicle = (header + " " + body).strip()
    # hard checks
    assert "(B-" not in vehicle, f"citation token leak in {fname}"
    assert "no meta-text describing the bug's spelling" in vehicle, f"missing anti-leak in {fname}"
    assert "PREPRO_2026-10-20_0315" not in vehicle, f"source citation in {fname}"
    md5 = hashlib.md5(vehicle.encode()).hexdigest()
    open(f"{OUTDIR}/{fname}", "w").write(vehicle)
    print(f"{fname}: md5={md5} bytes={len(vehicle)} stripped_tokens={toks}")
print("OK")
