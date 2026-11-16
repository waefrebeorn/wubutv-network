#!/usr/bin/env python3
"""Build fire vehicles for the 2026-10-19 04:45 EDT bumper factory run.
Verbatim extraction of the 0315 PREPRO generation prompts (citation-token-free),
Production-note/SOURCE strip pattern per the 0430 run. B-2206 -> B-1277, B-2207 -> B-1278."""
import hashlib, re

SRC = "/home/hatch/workspace/wubutv-network/slate/PREPRO_2026-10-19_0315.md"
OUT = {
    "B-2206": ("B-1277", "/home/hatch/workspace/wubutv-network/slate/fire_b1277_20261019_0445_v1.txt"),
    "B-2207": ("B-1278", "/home/hatch/workspace/wubutv-network/slate/fire_b1278_20261019_0445_v1.txt"),
}

text = open(SRC, encoding="utf-8").read()
# Sections are headed "## === B-NNNN (provisional) — "TITLE" : GENERATION PROMPT ==="
# and run to the next "## ===" heading or end-of-file.
heads = [m.start() for m in re.finditer(r"^## === B-\d+ \(provisional\)", text, re.M)]
heads.append(len(text))
built = {}
for i in range(len(heads) - 1):
    sec = text[heads[i]:heads[i + 1]]
    m = re.search(r"^## === (B-\d+) \(provisional\) — \"([^\"]+)\" : GENERATION PROMPT ===\s*\n", sec)
    if not m:
        continue
    prov, title = m.group(1), m.group(2)
    if prov not in OUT:
        continue
    body = sec[m.end():].strip()
    # Strip trailing "---" separators / source-footer cruft (keep only the prompt).
    body = re.sub(r"\n---\s*$", "", body).strip()
    # Zero citation tokens: strip the Source production-context block (Source: ... up to
    # the first blank line) — the generation prompt begins at "Hand-painted 2D cartoon".
    body = re.sub(r"^Source:.*?\n\n", "", body, flags=re.M | re.S).strip()
    # Scan for real citation tokens (bracket refs, parenthetical B-refs).
    # The NEGATIVE's "no citation-style text" phrase is intentional.
    assert not re.search(r"\[\d+\]|\[B-\d+\]|\(B-\d+\)|\[citation\]", body, re.I), f"citation token in {prov}"
    assert not re.search(r"^Source:", body, re.M), f"Source line leaked in {prov}"
    bnum, path = OUT[prov]
    open(path, "w", encoding="utf-8").write(body + "\n")
    md5 = hashlib.md5(body.encode()).hexdigest()
    built[prov] = (bnum, title, path, md5, len(body))
    print(f"{prov} '{title}' -> {bnum}: {path} md5={md5} chars={len(body)}")
    # sanity: the prompt must carry the load-bearing sections
    for sec_name in ["SUBJECTS:", "TIMELINE:", "CAMERA:", "AUDIO:", "LOAD-BEARING DETAIL:", "NEGATIVE:"]:
        assert sec_name in body, f"{prov} missing {sec_name}"
print("OK", built)
