#!/usr/bin/env python3
"""Build v1 fire vehicles for the 0945 bumper factory run (B-1275/B-1289/B-1290).
Pattern: verbatim 0015 B-2460/B-2461/B-2462 extracts, Source line stripped,
0815 BUG anti-leak clause appended to NEGATIVE; zero citation tokens."""
import hashlib, re, sys

PREPRO = "/home/hatch/workspace/wubutv-network/slate/PREPRO_2026-10-20_0015.md"
SLATE = "/home/hatch/workspace/wubutv-network/slate"

TARGETS = {
    "B-2460": ("fire_b1275_20261020_0945_v1.txt", "b1275"),
    "B-2461": ("fire_b1289_20261020_0945_v1.txt", "b1289"),
    "B-2462": ("fire_b1290_20261020_0945_v1.txt", "b1290"),
}

ANTI_LEAK = ", no meta-text describing the bug's spelling, no spelling-out of the tilde instruction as words."

text = open(PREPRO).read()
sections = re.split(r"(?m)^## === (B-\d+) \(provisional\)", text)
# sections: [pre, id1, body1, id2, body2, ...]
bodies = {sections[i]: sections[i+1] for i in range(1, len(sections), 2)}

for prov, (fname, tag) in TARGETS.items():
    if prov not in bodies:
        print(f"MISSING SECTION {prov}"); sys.exit(1)
    body = bodies[prov]
    # strip the header tail line (" — \"The Stone Over\" : GENERATION PROMPT ===")
    body = re.sub(r"(?m)^[^\n]*GENERATION PROMPT ===\n", "", body, count=1)
    # sanity: section must not contain a retirement annotation
    if "RETIRED PERMANENTLY" in body:
        print(f"{prov} IS RETIRED — abort"); sys.exit(1)
    # strip the Source: line (first line after the header)
    body = re.sub(r"(?m)^Source:.*\n", "", body, count=1)
    # last bumper section runs into the episode headers — truncate at the next ## === line
    body = re.split(r"(?m)^## === ", body, maxsplit=1)[0]
    # sanity: no other section headers leaked in
    if re.search(r"(?m)^## ===", body):
        print(f"{prov}: leaked section header — abort"); sys.exit(1)
    # strip trailing section delimiter and whitespace
    body = re.sub(r"\n*---\s*$", "", body).strip()
    if not body.startswith("Hand-painted 2D cartoon"):
        print(f"{prov}: unexpected body start: {body[:60]!r}"); sys.exit(1)
    # append anti-leak clause: replace final period of NEGATIVE tail
    if not body.endswith("no stinger."):
        print(f"{prov}: unexpected NEGATIVE tail: {body[-60:]!r}"); sys.exit(1)
    body = body[:-len("no stinger.")] + "no stinger" + ANTI_LEAK
    # no citation tokens allowed
    if "Source:" in body:
        print(f"{prov}: Source line survived — abort"); sys.exit(1)
    out = f"{SLATE}/{fname}"
    open(out, "w").write(body)
    md5 = hashlib.md5(body.encode()).hexdigest()
    print(f"{prov} -> {fname} md5={md5} bytes={len(body)}")
print("BUILD OK")
