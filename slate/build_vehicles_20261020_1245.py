#!/usr/bin/env python3
"""Build v1 fire vehicles for the 1245 Q3 episode factory run.
FIFO #217/#218/#219 <- provisional stages #509/#510/#511 in PREPRO_2026-10-20_1015.md.
Pattern: claim-time header + original production note + verification summary +
stage/claim provenance, then the verbatim prompt body (production note stripped,
Source line stripped, anti-leak clause already baked in at 1015). Zero citation tokens."""
import hashlib, re, sys

PREPRO = "/home/hatch/workspace/wubutv-network/slate/PREPRO_2026-10-20_1015.md"
SLATE = "/home/hatch/workspace/wubutv-network/slate"
CLAIM = "CLAIM_2026-10-20_1245_episodes.json"

# (ledger_num, provisional_stage, series, title, channel, bank_line)
TARGETS = [
    (217, "509", "NE-101", "THE HUNDRED FLIGHTS", "NETWORK",
     "bank production note condensed to the single 10s beat (IDEAS_BANK.md line 12955) — the doors shut-but-still at 4s; the first steps at 6s; the landing reached at 9.5s, the doors still closed behind — the climb is the verdict; mouth opens once at 8s; \"The stairs are running.\" UNC climbs — identity lock applies. Lore: THE 1945 OPERATORS' STRIKE. Lineage flagged vs shipped B-1229 \"The Car Call\" (the stairs vs the car — per bank note).",
     'Series NE-101 verified free; title "The Hundred Flights" grep-zero vs ledgers; line "The stairs are running." grep-zero.'),
    (218, "510", "PT-14", "THE NEVER-STOPS", "PUPPET THEATER",
     "bank production note condensed to the single 10s beat (IDEAS_BANK.md line 12956) — the loop gliding at 4s; the timed step at 6s; the ride continuing past the landing at 9.5s — the continuing ride is the verdict; mouth opens once at 8s; \"It doesn't wait.\" THE REGULAR boards — the compartments read as a loop, never separate cars. Lore: THE PATERNOSTER. Lineage flagged vs shipped B-1229 \"The Car Call\" (the loop vs the call — per bank note) + vs #509 same-run (the loop vs the stairs — per bank note).",
     'Series PT-14 verified free; title "The Never-Stops" grep-zero vs ledgers; line "It doesn\'t wait." grep-zero.'),
    (219, "511", "L-78", "THE DEVIATION CARD", "LABS",
     "bank production note condensed to the single 10s beat (IDEAS_BANK.md line 13063) — the swing at 4s; the card written at 6s; the corrected course held at 9.5s — the corrected course is the verdict; mouth opens once at 8s; \"The ship is corrected.\" THE ADJUSTER works — hands visible, the card is the load-bearing paper. Lore: THE DEVIATION CARD. Lineage flagged vs banked READY \"The South-Pointing Spoon\" (the correction vs the divination — per bank note).",
     'Series L-78 verified free; title "The Deviation Card" grep-zero vs ledgers; line "The ship is corrected." grep-zero.'),
]

text = open(PREPRO).read()
sections = re.split(r"(?m)^## === #(\d+) \(provisional\)", text)
# sections: [pre, num1, body1, num2, body2, ...]
bodies = {sections[i]: sections[i + 1] for i in range(1, len(sections), 2)}

results = []
for ledger, prov, series, title, channel, prodnote, verify in TARGETS:
    if prov not in bodies:
        print(f"MISSING SECTION #{prov}"); sys.exit(1)
    body = bodies[prov]
    if "RETIRED PERMANENTLY" in body or "STRUCK" in body.split("\n\n")[0]:
        print(f"#{prov}: retirement/strike annotation present — abort"); sys.exit(1)
    # split: body starts with the header-line remnant ("— SERIES ... ==="); drop it
    body = body.split("\n", 1)[1]
    # split: production note paragraph is the first paragraph; prompt body follows
    paras = body.strip().split("\n\n")
    if not paras[0].startswith("Production note:"):
        print(f"#{prov}: unexpected first paragraph: {paras[0][:60]!r}"); sys.exit(1)
    prompt_body = "\n\n".join(paras[1:])
    prompt_body = re.split(r"(?m)^## === ", prompt_body, maxsplit=1)[0]
    if re.search(r"(?m)^## ===", prompt_body):
        print(f"#{prov}: leaked section header — abort"); sys.exit(1)
    prompt_body = re.sub(r"\n*---\s*$", "", prompt_body).strip()
    if not prompt_body.startswith("Hand-painted 2D cartoon"):
        print(f"#{prov}: unexpected body start: {prompt_body[:60]!r}"); sys.exit(1)
    if not prompt_body.endswith("no stinger."):
        print(f"#{prov}: unexpected NEGATIVE tail: {prompt_body[-60:]!r}"); sys.exit(1)
    if "Source:" in prompt_body:
        print(f"#{prov}: Source line survived — abort"); sys.exit(1)
    if re.search(r"\(\d+[A-Z]-\w+\)", prompt_body):
        print(f"#{prov}: citation token present — abort"); sys.exit(1)
    if "no meta-text describing the bug's spelling" not in prompt_body:
        print(f"#{prov}: anti-leak clause missing — abort"); sys.exit(1)
    header = f"## === #{ledger} — {series} \"{title}\" ({channel}) : VOICE STAGE ===\n"
    note = (f"Production note: {prodnote} {verify} "
            f"Stage #{prov} (provisional -> {series}) in slate/PREPRO_2026-10-20_1015.md; "
            f"claim in {CLAIM}.\n")
    vehicle = header + "\n" + note + "\n" + prompt_body + "\n"
    fname = f"fire_e{ledger}_20261020_1245_v1.txt"
    out = f"{SLATE}/{fname}"
    open(out, "w").write(vehicle)
    md5 = hashlib.md5(vehicle.encode()).hexdigest()
    results.append((ledger, prov, series, title, fname, md5))
    print(f"#{ledger} <- #{prov} {series} -> {fname} md5={md5} bytes={len(vehicle)}")

print("BUILD OK")
for r in results:
    print("CLAIM-ROW", r)
