#!/usr/bin/env python3
"""Q3 episode factory 2026-10-19 2245 EDT: build durable v1 fire vehicles
for #209/#210/#211 from PREPRO_2026-10-19_0215.md stages #341/#342/#343.
Body is copied VERBATIM from the stage (production-note paragraph replaced
with the run-time note)."""
import re, hashlib, json

PREPRO = "/home/hatch/workspace/wubutv-network/slate/PREPRO_2026-10-19_0215.md"
SLATE = "/home/hatch/workspace/wubutv-network/slate"

with open(PREPRO) as f:
    text = f.read()

# split into stage sections on header lines
parts = re.split(r'(?m)^## === #(\d+) \(provisional\)', text)
# parts[0] = preamble; then pairs of (num, header-rest + body)
stages = {}
for i in range(1, len(parts), 2):
    num = int(parts[i])
    body = parts[i + 1]
    stages[num] = body

specs = {
    341: {
        "ledger": 209, "series": "L-54", "title": "THE MEASURED DISH",
        "chan": "LABS",
        "note": ('bank production note intact (IDEAS_BANK.md line 9158) — hands-only; a dish measured at 2s; '
                 'fitted into its wire compartment at 4-6s; the rack of fitted dishes at 9.5s. Line ~8s: '
                 '"Measured first." LORE — THE MEASURED DISH: the chipped set protected — the wire compartments '
                 'fit first, because the dish was measured first. Lineage vs B-1043 "The Washed Mug" (the invention '
                 'behind the wash — flagged, distinct beat). Series L-54 verified free (grep-zero vs '
                 'EPISODE_LEDGER.md + notes/COMMERCIALS.md); title "The Measured Dish" grep-zero; line '
                 '"Measured first." grep-zero; ledger slot #209 (ledger tail #208). Stage #341 (provisional -> L-54) '
                 'in slate/PREPRO_2026-10-19_0215.md; claim in CLAIM_2026-10-19_2245_episodes.json.'),
    },
    342: {
        "ledger": 210, "series": "S-43", "title": "THE MILE-WIDE LOBBY",
        "chan": "SATIRE",
        "note": ('bank production note intact (IDEAS_BANK.md line 9159) — UNC crosses the empty lobby carrying '
                 'the plans at 2-6s; stands at the far desk at 9.5s. NO-LINE (the crossing is the pitch). LORE — '
                 'THE MILE-WIDE LOBBY: the lobby seemed a mile wide; the crossing was the pitch; the order was the '
                 'reward. Series S-43 verified free (grep-zero vs EPISODE_LEDGER.md + notes/COMMERCIALS.md); title '
                 '"The Mile-Wide Lobby" grep-zero; ledger slot #210 (ledger tail #208). Stage #342 (provisional -> '
                 'S-43) in slate/PREPRO_2026-10-19_0215.md; claim in CLAIM_2026-10-19_2245_episodes.json.'),
    },
    343: {
        "ledger": 211, "series": "N-111", "title": "THE BUCKET OF DISKS",
        "chan": "NEWS",
        "note": ('bank production note intact (IDEAS_BANK.md line 9160) — the Colonel reports the old system: a hand '
                 'takes a brass disk at 2s; tosses it into the bucket at 4-6s; the bucket of disks at 9.5s. '
                 'Line ~8s: "It counted nothing." LORE — THE TOSSED DISK: presence was recorded by brass disks '
                 'tossed in a bucket — no accurate record of when the man actually showed up. Lineage to #160 NE-18 '
                 '"The First In" (the prequel beat — the system before the clock — flagged, distinct). Colonel '
                 'register: irony in the WORDS, face straight. Series N-111 verified free (grep-zero vs '
                 'EPISODE_LEDGER.md + notes/COMMERCIALS.md); title "The Bucket of Disks" grep-zero; line '
                 '"It counted nothing." grep-zero; ledger slot #211 (ledger tail #208). Stage #343 (provisional -> '
                 'N-111) in slate/PREPRO_2026-10-19_0215.md; claim in CLAIM_2026-10-19_2245_episodes.json.'),
    },
}

out = {}
for prov, s in specs.items():
    body = stages[prov]
    # strip to end of section (cut at the "---" separator line)
    body = body.split("\n---\n")[0]
    # strip the header remainder (" — SERIES "TITLE" (CHAN) : VOICE STAGE ===\n\n")
    body = re.sub(r'^.*?VOICE STAGE ===\n\n', '', body, count=1, flags=re.S)
    body = body.strip("\n")
    # drop the original Production note paragraph (first paragraph of section)
    paras = re.split(r'\n\n', body, maxsplit=1)
    assert paras[0].strip().startswith("Production note:"), paras[0][:60]
    rest = paras[1].strip("\n")
    header = '## === #%d — %s "%s" (%s) : VOICE STAGE ===' % (s["ledger"], s["series"], s["title"], s["chan"])
    vehicle = header + "\n\nProduction note: " + s["note"] + "\n\n" + rest + "\n"
    path = "%s/fire_e%d_20261019_2245_v1.txt" % (SLATE, s["ledger"])
    with open(path, "w") as f:
        f.write(vehicle)
    md5 = hashlib.md5(vehicle.encode()).hexdigest()
    out[s["ledger"]] = {"path": path, "md5": md5, "series": s["series"]}
    print(s["ledger"], path, md5)

claim = {
    "run": "Q3 episode factory 2026-10-19 2245 EDT",
    "episodes": [
        {"ledger": 209, "stage": 341, "series": "L-54", "title": "The Measured Dish",
         "vehicle": "slate/fire_e209_20261019_2245_v1.txt", "md5": out[209]["md5"]},
        {"ledger": 210, "stage": 342, "series": "S-43", "title": "The Mile-Wide Lobby",
         "vehicle": "slate/fire_e210_20261019_2245_v1.txt", "md5": out[210]["md5"]},
        {"ledger": 211, "stage": 343, "series": "N-111", "title": "The Bucket of Disks",
         "vehicle": "slate/fire_e211_20261019_2245_v1.txt", "md5": out[211]["md5"]},
    ],
    "status": "STALL QUEUE — video budget outage window opened 2026-10-19 ~21:00 EDT persists; "
              "next run fires these three md5-verified vehicles IN ORDER (#209 FIRST) when the budget resets",
}
with open(SLATE + "/CLAIM_2026-10-19_2245_episodes.json", "w") as f:
    json.dump(claim, f, indent=2)
print("claim written")
