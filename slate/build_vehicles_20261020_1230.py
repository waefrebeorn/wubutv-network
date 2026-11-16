#!/usr/bin/env python3
"""Build Q2 bumper factory vehicles for the 2026-10-20 12:30 EDT run.
B-1295 (freed pool, B-814 precedent; never the retired "The Dialed Number" draft) <- 0315 B-2489 "The Watered Seed" (FIFO)
B-1300 (fresh pool, max shipped B-1299) <- 0315 B-2490 "The Shuttered Booth" (FIFO)
B-1301 (fresh pool, max shipped B-1299) <- 0315 B-2491 "The Shelved Jar" (FIFO)
Convention: verbatim PREPRO extract, Source line stripped, parenthetical
B-NNN lesson citation tokens stripped incl. extended forms like "(B-79: ...)"
(1045 Q3 CITATION-TOKEN-LEAK lesson + 1215 SELF-INFLICTED lesson), 0815 BUG
anti-leak clause appended, single-line TEXT-ONLY vehicle."""
import re, hashlib

PREPRO = "/home/hatch/workspace/wubutv-network/slate/PREPRO_2026-10-20_0315.md"
OUTDIR = "/home/hatch/workspace/wubutv-network/slate"
LEAK_CLAUSE = "no meta-text describing the bug's spelling, no spelling-out of the tilde instruction as words."

text = open(PREPRO).read()
jobs = {
    "b1295": ("B-2489", "fire_b1295_20261020_1230_v1.txt"),
    "b1300": ("B-2490", "fire_b1300_20261020_1230_v1.txt"),
    "b1301": ("B-2491", "fire_b1301_20261020_1230_v1.txt"),
}

for pool, (prov, fname) in jobs.items():
    start = text.index(f"## === {prov} (provisional)")
    seg = text[start:]
    end_markers = [m.start() for m in re.finditer(r"\n## === B-", seg)]
    end = min([e for e in end_markers if e > 10], default=len(seg))
    section = seg[:end].strip()
    section = re.sub(r"\n---+\s*$", "", section).strip()
    lines = section.split("\n")
    header = lines[0]
    body_lines = [l for l in lines[1:] if not l.startswith("Source:")]
    body = " ".join(l.strip() for l in body_lines if l.strip())
    body = re.sub(r"\s+", " ", body)
    # strip ANY parenthetical containing a B-NNN token (bare "(B-45)" or
    # extended "(B-79: the prop...)" / "(B-85 zoom-crop)"), instruction prose kept
    toks = re.findall(r"\([^()]*B-\d+[^()]*\)", body)
    body = re.sub(r"\s*\([^()]*B-\d+[^()]*\)", "", body)
    if not body.rstrip().endswith(LEAK_CLAUSE):
        body = body.rstrip().rstrip(".") + ", " + LEAK_CLAUSE.rstrip(".") + "."
    vehicle = (header + " " + body).strip()
    # hard checks
    assert "(B-" not in vehicle, f"citation token leak in {fname}"
    assert "O-72" not in vehicle and "digit lesson" not in vehicle.lower(), f"lesson token in {fname}"
    assert "no meta-text describing the bug's spelling" in vehicle, f"missing anti-leak in {fname}"
    assert "PREPRO_2026-10-20_0315" not in vehicle, f"source citation in {fname}"
    assert "never re-claim" not in vehicle, f"PREPRO annotation leak in {fname}"
    md5 = hashlib.md5(vehicle.encode()).hexdigest()
    open(f"{OUTDIR}/{fname}", "w").write(vehicle)
    print(f"{fname}: md5={md5} bytes={len(vehicle)} stripped_tokens={toks}")
print("OK")
