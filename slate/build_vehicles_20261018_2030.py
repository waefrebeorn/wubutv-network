#!/usr/bin/env python3
"""Build fire vehicles for the 2030 bumper factory run.
Verbatim PREPRO fire-section extracts: Production note stripped, citation
tokens excised, zero citations. Scans for subject-word slips per the
Q1-CROSS-DRAFT-SLIP datum."""
import re, hashlib, sys, os

SLATE = os.path.expanduser("~/workspace/wubutv-network/slate")

SPECS = {
    "b1236": ("PREPRO_2026-10-18_0215.md", '## === B-1910 (provisional)',
              ['crate', 'chalk', 'seal', 'customs', 'paid', 'duty']),
    "b1242": ("PREPRO_2026-10-18_0315.md", '## === B-1911 (provisional)',
              ['bucket', 'doorstep', 'mill', 'ford', 'ash', 'sunset', 'dusk', 'dark']),
    "b1243": ("PREPRO_2026-10-18_0315.md", '## === B-1912 (provisional)',
              ['lift', 'car', 'panel', 'button', 'door', 'floor', 'fourteen', 'unnumbered']),
}

# citation-token scrub: parenthetical (10S-F###), (B-### ...), (S-### ...), (N-### ...)
CIT_RE = re.compile(r"\s*\((?:10S-F\d+|B-\d+[^)]*|S-\d+[^)]*|N-\d+[^)]*|AD-\d+[^)]*|E\d+[^)]*)\)")

def build(key, src, marker, subject_words):
    text = open(os.path.join(SLATE, src)).read()
    i = text.index(marker)
    # fire section starts at "Hand-painted 2D cartoon" after the production note
    j = text.index("Hand-painted 2D cartoon", i)
    k = text.index("\n---\n", j)
    body = text[j:k].strip()
    body = CIT_RE.sub("", body)
    body = re.sub(r"\s{2,}", " ", body)
    # slip scan: flag foreign subject words in the fire section
    foreign = {"crate": ["cloth", "fold", "fulling", "slate"],
               "bucket": ["cloth", "slate", "crate", "fulling"],
               "lift": ["bucket", "cloth", "slate", "crate", "chalk"]}
    key0 = "crate" if key == "b1236" else ("bucket" if key == "b1242" else "lift")
    hits = [w for w in foreign[key0] if re.search(rf"\b{w}\w*", body, re.I)]
    if hits:
        print(f"SLIP-WARNING {key}: foreign words {hits}", file=sys.stderr)
    # sanity: the draft's own subject words must appear
    missing = [w for w in subject_words if w.lower() not in body.lower()]
    if missing:
        print(f"MISSING-WARNING {key}: {missing}", file=sys.stderr)
    out = os.path.join(SLATE, f"fire_{key}_20261018_2030_v1.txt")
    open(out, "w").write(body + "\n")
    md5 = hashlib.md5(body.encode()).hexdigest()
    print(f"{key}: {out} md5 {md5} ({len(body)} chars)")

for key, (src, marker, words) in SPECS.items():
    build(key, src, marker, words)
