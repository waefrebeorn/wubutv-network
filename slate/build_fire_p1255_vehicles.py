#!/usr/bin/env python3
"""Build Q4 fire vehicles for STATION piece 585 (chain p1255) from
slate/PREPRO_2026-11-08_2115.md, verbatim per the factory body.

2115-format parts carry: Logline, SHOT & CAMERA, SUBJECTS, ACTION,
Addressee/Want, Withhold/Spend, LIGHT, AUDIO, STYLE. The vehicle keeps
the scene fields in PREPRO order and drops the two meta fields
(Logline, Withhold/Spend) per the 553/554 precedent (WITHHELD FACT +
PRICE paragraphs stripped at fire time). Only the ** bold markers are
removed; all other bytes are verbatim from the draft.

Fail-loud gates: every part must carry exactly one LINE in the 7-9s
beat with <=9 words; no citation tokens (B-NNN / CRAFT-NNN / bare
#NNN) may survive into a vehicle.
"""
import hashlib, re, sys

PREPRO = "slate/PREPRO_2026-11-08_2115.md"
SLUG = "theessaythemillpondkeepsfornoreader"
CHAIN = "p1255"
FIELDS = ["SHOT & CAMERA", "SUBJECTS", "ACTION", "Addressee/Want",
          "LIGHT", "AUDIO", "STYLE"]
DROP = ["Logline", "Withhold/Spend"]

text = open(PREPRO).read()
vehicles = {}
for n in (1, 2, 3, 4):
    m = re.search(rf"### {CHAIN} PART {n} of 4\n(.*?)(?=\n### |\n## CHAIN|\Z)",
                  text, re.S)
    assert m, f"part {n} not found"
    block = m.group(1)
    # split into **Field:** ... paragraphs; a field runs until the next **Field:**
    parts = re.split(r"(?m)^\*\*([A-Za-z &/()\-]+):\*\*\s", block)
    # parts[0] is the lead (empty); then label, body, label, body, ...
    assert parts[0].strip() == "", f"part {n}: unexpected lead text {parts[0][:80]!r}"
    fields = {}
    labels = {}
    for i in range(1, len(parts), 2):
        norm = re.sub(r" \(.*\)$", "", parts[i])
        fields[norm] = parts[i + 1].rstrip("\n")
        labels[norm] = parts[i]
    for f in FIELDS:
        assert f in fields, f"part {n}: missing field {f}"
    for f in DROP:
        assert f in fields, f"part {n}: missing meta field {f} (drop-list drift?)"
    # LINE gate: exactly one quoted line in the 7-9s ACTION beat, <=9 words
    lines = re.findall(r'\(7\.0–9\.0s\) LINE — [^:]+: "([^"]+)"', fields["ACTION"])
    assert len(lines) == 1, f"part {n}: expected 1 line, got {lines}"
    words = lines[0].split()
    assert len(words) <= 9, f"part {n}: line has {len(words)} words: {lines[0]}"
    def render(f):
        body = fields[f].rstrip()
        # ACTION's beats start on the next line in the draft (header alone)
        sep = ":\n" if body.startswith("(") else ": "
        return f"{labels[f]}{sep}{body}\n"
    vehicle = "".join(render(f) for f in FIELDS)
    # citation-token gate
    bad = re.findall(r"B-\d+|CRAFT-\d+|(?<!\w)#\d+", vehicle)
    assert not bad, f"part {n}: citation tokens survive: {bad}"
    assert "**" not in vehicle, f"part {n}: bold markers survive"
    vehicles[n] = vehicle

for n, v in vehicles.items():
    path = f"slate/fire_station_p{n}_{SLUG}_v1.txt"
    open(path, "w").write(v)
    print(f"P{n} {path} md5={hashlib.md5(v.encode()).hexdigest()} "
          f"line=\"{re.findall(chr(34)+r'([^'+chr(34)+r']+)'+chr(34), v)[-1]}\"")
print("OK — 4 vehicles built verbatim (Logline + Withhold/Spend dropped).")
