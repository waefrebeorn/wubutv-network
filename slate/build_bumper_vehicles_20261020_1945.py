#!/usr/bin/env python3
"""Build B-1373/B-1374/B-1375 v1 vehicles for the 2026-10-20 19:45 EDT stall-bank run.
1815-new-format verbatim **SUBJECTS**-through-NEGATIVE extracts (no draft header,
no Source paragraph); hardened citation-token strip; lineage-only adjudication
sentences dropped as factory meta-text; stranded-comma/empty-paren/double-space
collapse; native anti-underline-bar stack asserted >=2 on all three UNC drafts;
0815 BUG anti-leak clause appended; zero citation tokens asserted; size 2-8KB."""
import hashlib, re, sys

SLATE = "/home/hatch/workspace/wubutv-network/slate"

ANTILEAK = ("\n\n---. BUG-CLASS INSTRUCTION-SET HYGIENE: the generated take carries only "
            "the scene itself — no production-slate overlays, no version tokens, no number "
            "tokens, no meta-text describing the bug's spelling, no spelling-out of the "
            "tilde instruction as words; the corner bug renders as plain text only.")

SPECS = [
    ("B-1373", "PREPRO_2026-10-20_1815.md", "B-2677", "fire_b1373_20261020_1945_v1.txt"),
    ("B-1374", "PREPRO_2026-10-20_1815.md", "B-2678", "fire_b1374_20261020_1945_v1.txt"),
    ("B-1375", "PREPRO_2026-10-20_1915.md", "B-2679", "fire_b1375_20261020_1945_v1.txt"),
]

def extract(prepro, prov):
    text = open(f"{SLATE}/{prepro}", encoding="utf-8").read()
    # draft block: from its ## === header to the next ## === header (or EOF)
    m = re.search(r"^## === " + re.escape(prov) + r" .*?$", text, re.M)
    assert m, f"header for {prov} not found in {prepro}"
    start = m.end()
    nxt = re.search(r"^## ===", text[start:], re.M)
    block = text[start:start + nxt.start()] if nxt else text[start:]
    i = block.find("**SUBJECTS**:")
    assert i >= 0, f"SUBJECTS not found for {prov}"
    body = block[i:]
    # trim trailing separator --- / blank lines
    body = re.sub(r"\n---\s*$", "", body.strip()) + "\n"
    return body

def strip_tokens(body, tag):
    # 1. colon-class unwrap: (B-79: prose) -> prose
    body, n1 = re.subn(r"\(([A-Z]{1,4}-\d+):\s*([^()]*)\)", r"\2", body)
    # 2. backstop: kill any remaining (X-NNN...) parenthetical form
    body, n2 = re.subn(r"\([A-Z]{1,4}-\d+[^()]*\)", "", body)
    # 3. cf. cross-ref strip
    body, n3 = re.subn(r"\bcf\.\s*[A-Z]{1,4}-\d+", "", body)
    # 4. bare-token strip: unwrapped B-NNN refs
    body, n4 = re.subn(r"\b[A-Z]{1,4}-\d+\b", "", body)
    # 5. drop lineage-only adjudication sentences (factory meta-text)
    sents = re.split(r"(?<=[.!?])\s+", body)
    kept = [s for s in sents
            if not re.search(r"\bflagged\b|\badjudicated\b|\bper bell-family\b", s, re.I)]
    body = " ".join(kept)
    # 6. collapse stranded commas / empty parens / double spaces
    body = re.sub(r",\s*,", ",", body)
    body = re.sub(r"\(\s*\)", "", body)
    body = re.sub(r"[ \t]{2,}", " ", body)
    body = re.sub(r" \.", ".", body)
    assert not re.search(r"\b[A-Z]{1,4}-\d+\b", body), f"{tag}: citation token leaked"
    return body

def main():
    for num, prepro, prov, fname in SPECS:
        body = strip_tokens(extract(prepro, prov), num)
        # native anti-underline-bar stack >= 2 on UNC drafts
        bar = len(re.findall(r"(?i)no (?:underline )?bar|ABSOLUTELY NO BAR", body))
        assert bar >= 2, f"{num}: bar-stack only {bar}"
        body += ANTILEAK
        size = len(body.encode("utf-8"))
        assert 2000 <= size <= 8192, f"{num}: size {size} out of 2-8KB band"
        md5 = hashlib.md5(body.encode("utf-8")).hexdigest()
        with open(f"{SLATE}/{fname}", "w", encoding="utf-8") as f:
            f.write(body)
        print(f"{num} <- {prepro} {prov}: {fname} md5={md5} bytes={size} barstack={bar}")

if __name__ == "__main__":
    main()
