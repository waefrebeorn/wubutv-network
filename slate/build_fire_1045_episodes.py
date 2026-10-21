#!/usr/bin/env python3
"""Episode fire-prompt builder — Q3 run 2026-10-20 10:45 EDT (#214/#215/#216).
Follows the 0845 proven format: header + production note, then the stage body
verbatim minus its own leading Production-note paragraph (the note moves to the
header). No citation stripping — stage tokens (B-45)/(S-16)/(B-26) ride verbatim
per the 0845 vehicles. fail-loud on structural faults."""
import re, hashlib, pathlib

SLATE = pathlib.Path.home() / "workspace/wubutv-network/slate"
SRC = "PREPRO_2026-10-20_0915.md"

HEADERS = {
    214: '## === #214 — PA-79 "THE TARE" (PUBLIC ACCESS) : VOICE STAGE ===',
    215: '## === #215 — L-77 "THE PAPER THAT DARKENS" (LABS) : VOICE STAGE ===',
    216: '## === #216 — S-52 "THE CHALK" (SATIRE) : VOICE STAGE ===',
}
NOTES = {
    214: 'Production note: bank [READY] (IDEAS_BANK.md line 12952, FIFO) — condensed to the single 10s beat. UNC is the weighbridge keeper — identity lock applies. Lore: TARE AND TRETT. Lineage flagged vs shipped #213 L-76 "The Sifters" (the subtraction vs the sorting). Series PA-79 verified free (grep-zero vs EPISODE_LEDGER.md + notes/COMMERCIALS.md); title "The Tare" clean (bank source item, expected intake); line "The sack doesn\'t count." grep-zero. Stage #506 (provisional -> PA-79) in slate/PREPRO_2026-10-20_0915.md; claim in CLAIM_2026-10-20_1045_episodes.json.',
    215: 'Production note: bank [READY] (IDEAS_BANK.md line 12953, FIFO) — condensed to the single 10s beat. NO-LINE — the strip is the verdict. UNC and the standard — identity lock applies. Lore: THE STANDARD CANDLE. Lineage flagged vs shipped B-1235 "The Gas Gauge" (the purity vs the pressure). Series L-77 verified free; title "The Paper That Darkens" grep-zero. Stage #507 (provisional -> L-77) in slate/PREPRO_2026-10-20_0915.md; claim in CLAIM_2026-10-20_1045_episodes.json.',
    216: 'Production note: bank [READY] (IDEAS_BANK.md line 12954, FIFO) — condensed to the single 10s beat. UNC is the warden — irony in the WORDS, face straight (Satire UNC does administration). MEME-F165 stages here. Lore: THE CHALKED TIME. Lineage flagged vs shipped #62 N-45 "The Chalk Search" (the enforcement chalking vs the ruling ident — adjudicated distinct). Series S-52 verified free; title "The Chalk" adjudicated distinct vs "The Chalk Search"; line "This is a search." grep-zero. Stage #508 (provisional -> S-52) in slate/PREPRO_2026-10-20_0915.md; claim in CLAIM_2026-10-20_0845_episodes.json.'.replace("0845", "1045"),
}
PROV = {214: 506, 215: 507, 216: 508}

txt = (SLATE / SRC).read_text()
vehicles = {}
for num in (214, 215, 216):
    p = PROV[num]
    m = re.search(rf"^## === #{p} \(provisional\).*?\n(.*?)(?=^## === #\d+ \(provisional\)|\Z)", txt, re.S | re.M)
    if not m:
        raise SystemExit(f"FAILED: stage #{p} not found in {SRC}")
    body = m.group(1).strip()
    # strip the body's own leading Production-note paragraph (moves to header)
    body2 = re.sub(r"^Production note:.*?\n\n", "", body, count=1, flags=re.S)
    if body2 == body:
        raise SystemExit(f"FAILED #{num}: body Production-note paragraph not found/stripped")
    if re.search(r"(?:^|\n)Source:", body2):
        raise SystemExit(f"FAILED #{num}: Source: survivor in body")
    if "EXACTLY TWO lines of plain WHITE text" not in body2:
        raise SystemExit(f"FAILED #{num}: bug paragraph missing")
    vehicle = HEADERS[num] + "\n\n" + NOTES[num] + "\n\n" + body2 + "\n"
    vehicles[num] = vehicle

man = {}
for num, v in vehicles.items():
    out = SLATE / f"fire_e{num}_20261020_1045_v1.txt"
    out.write_text(v)
    man[f"e{num}"] = {"file": str(out), "md5": hashlib.md5(v.encode()).hexdigest(), "bytes": len(v)}
    print(num, out.name, man[f"e{num}"]["md5"], len(v))
(SLATE / "vehicles_20261020_1045.json").write_text(__import__("json").dumps(man, indent=2))
print("BUILD OK — 3 vehicles")
