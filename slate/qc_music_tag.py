#!/usr/bin/env python3
"""CEO order R1 (Era II, 2026-10-21): MUSIC_TAG gate.
A new master without a MUSIC_TAG row (bed id + sting id) in
music/tags.json fails QC. Usage: python3 qc_music_tag.py B-1294 E-101 AD-302
Exits 0 when every listed unit has a valid row, 1 otherwise.
"""
import json, os, sys

ROOT = os.path.expanduser("~/workspace/wubutv-network")
CH = ["NEWS", "ORIGINALS", "SATIRE", "LABS", "ARENA", "MEDIASCHOOL",
      "PUBLICACCESS", "PUPPET", "NETWORK"]
VALID = {"MV1-BED-" + c for c in CH} | {"MV1-STING-" + c for c in CH}
# Serial-bed lane (MUSIC_TAGS.md: "one bed per serial"; the serial bed
# replaces the channel bed for serial units). CEO7 segment spec for SERIAL-1
# issues bed=serial-1-orig, sting=orig (the ORIGINALS channel sting) verbatim;
# both are valid tag ids for serial units.
VALID |= {"serial-1-orig", "orig"}

tags = json.load(open(f"{ROOT}/music/tags.json"))
bad = []
for uid in sys.argv[1:]:
    row = tags.get(uid)
    if not isinstance(row, dict):
        bad.append(f"{uid}: no MUSIC_TAG row in music/tags.json")
        continue
    bed, sting = row.get("bed"), row.get("sting")
    if bed not in VALID:
        bad.append(f"{uid}: bad bed id {bed!r}")
    if sting not in VALID:
        bad.append(f"{uid}: bad sting id {sting!r}")
if bad:
    print("MUSIC_TAG QC FAIL:")
    for b in bad:
        print("  " + b)
    sys.exit(1)
print(f"MUSIC_TAG QC PASS: {len(sys.argv[1:])} unit(s)")
