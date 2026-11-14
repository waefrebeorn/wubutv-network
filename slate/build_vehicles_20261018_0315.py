#!/usr/bin/env python3
"""Build script-built fire vehicles for the 2026-10-18 0315 bumper factory run.
Per the FIRE-VEHICLE TRANSCRIPTION-SLIP datum: fire from script-built vehicles,
never hand-pasted. Excision discipline: ALL B-<digits> tokens + all parenthetical
citation tokens stripped; Production note stripped; B-1898's (10S-F103) excised;
B-1898's B-26 dressing parenthetical reworded (not a bare excision — keep the
crop-zoom-verified allowlist meaning).
Claim: B-1236 <- 0115 B-1898 "THE BOOK PRESS"; B-1237 <- 0215 B-1899 "THE WASH HOUSE";
B-1238 <- 0215 B-1900 "THE SAW PIT"."""
import re, hashlib, pathlib

slate = pathlib.Path.home() / "workspace/wubutv-network/slate"
pre0115 = (slate / "PREPRO_2026-10-18_0115.md").read_text()
pre0215 = (slate / "PREPRO_2026-10-18_0215.md").read_text()
RUN = "20261018_0315"

def extract(pre, prov, title):
    pat = re.compile(r"## === B-%d \(provisional\) — \"%s\" : GENERATION PROMPT ===\n" % (prov, title))
    m = pat.search(pre)
    assert m, f"section not found: B-{prov} {title}"
    start = m.start()
    end = pre.find("---\n\n", m.end())
    assert end > 0
    return pre[start:end]

def strip_production_note(text):
    text, n = re.subn(r"Production note: .*?\n\n", "", text, flags=re.S, count=1)
    assert n == 1, "production note not stripped"
    return text

def excise(text):
    # specific rewrites FIRST
    text = text.replace("(B-26 dressing, crop-zoom verified — no legible words anywhere, allowlist = none)",
                        "(crop-zoom verified — no legible words anywhere, allowlist = none)")
    # (10S-F103) parenthetical citation token
    text = re.sub(r"\s*\(10S-F103\)", "", text)
    # ALL remaining B-<digits> tokens, parenthetical or inline
    text = re.sub(r"\bB-\d+[a-zA-Z'’s:]*", "", text)
    # rewrite header without the number token
    text = re.sub(r"## === B-\d+ \(provisional\) — ", "## === ", text)
    # collapse whitespace artifacts
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    # verify zero citation tokens remain
    leftovers = re.findall(r"\bB-\d+|\(10S-|\(S-16\)", text)
    assert not leftovers, f"citation tokens remain: {leftovers}"
    return text

def build(pre, prov, title, claimed, version, correction=None):
    body = extract(pre, prov, title)
    body = strip_production_note(body)
    body = excise(body)
    body = body.rstrip() + "\n"
    if correction:
        body += "\n---\n\n" + correction + "\n"
    fn = slate / f"fire_b{claimed}_{RUN}_{version}.txt"
    fn.write_text(body)
    md5 = hashlib.md5(body.encode()).hexdigest()
    print(f"{fn.name}: {len(body)} chars, md5 {md5}")
    return md5

JOBS = [
    (pre0115, 1898, "THE BOOK PRESS", 1236),
    (pre0215, 1899, "THE WASH HOUSE", 1237),
    (pre0215, 1900, "THE SAW PIT", 1238),
]
for pre, prov, title, claimed in JOBS:
    build(pre, prov, title, claimed, "v1")
print("OK")
