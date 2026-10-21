#!/usr/bin/env python3
"""Build script-built fire vehicles for the 2026-10-18 0330 bumper factory run.
Per the FIRE-VEHICLE TRANSCRIPTION-SLIP datum: fire from script-built vehicles,
never hand-pasted. Excision discipline: ALL B-<digits> tokens + all parenthetical
citation tokens stripped; Production note stripped. B-1238's vehicle is the
durable on-disk reclaim vehicle (fire_b1238_20261018_0315_v1.txt) — NOT rebuilt.
Claim: B-1236 <- 0215 B-1901 "THE LIME KILN"; B-1238 <- 0215 B-1900 "THE SAW PIT"
(reclaim, on-disk vehicle); B-1239 <- 0215 B-1903 "THE OAST HOUSE" (B-1902 skipped
at claim — subject collision with shipped B-1066 "The Pressed Cider")."""
import re, hashlib, pathlib

slate = pathlib.Path.home() / "workspace/wubutv-network/slate"
pre0215 = (slate / "PREPRO_2026-10-18_0215.md").read_text()
RUN = "20261018_0330"

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
    text = re.sub(r"\s*\(10S-F103\)", "", text)
    text = re.sub(r"\s*\(S-16\)", "", text)
    text = re.sub(r"\bB-\d+[a-zA-Z'’s:]*", "", text)
    text = re.sub(r"## === B-\d+ \(provisional\) — ", "## === ", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
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
    (pre0215, 1901, "THE LIME KILN", 1236),
    (pre0215, 1903, "THE OAST HOUSE", 1239),
]
for pre, prov, title, claimed in JOBS:
    build(pre, prov, title, claimed, "v1")
print("OK")
