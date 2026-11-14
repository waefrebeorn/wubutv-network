#!/usr/bin/env python3
"""Build script-built fire vehicles for the 2026-10-18 0300 bumper factory run.
Per the FIRE-VEHICLE TRANSCRIPTION-SLIP datum: fire from script-built vehicles,
never hand-pasted. Excision discipline: ALL B-<digits> tokens + all parenthetical
citation tokens stripped; Production note stripped; provenance parentheticals removed."""
import re, hashlib, pathlib

slate = pathlib.Path.home() / "workspace/wubutv-network/slate"
pre = (slate / "PREPRO_2026-10-18_0115.md").read_text()
RUN = "20261018_0300"

def extract(prov, title):
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
    # specific rewrites FIRST (before generic B-digit removal mangles them)
    text = text.replace("(the bunker's interior, not B-1082's pavement coal hole)",
                        "(the bunker's interior, not the pavement coal hole)")
    text = text.replace("(the 6s and 9.5s positions identical — the stop holds, B-137)",
                        "(the 6s and 9.5s positions identical — the stop holds)")
    # provenance / redundant rule-citation parentheticals removed entirely
    text = text.replace("(bank dry — the [READY] bumper shelf is EMPTY; the 1615 fallback rule)", "")
    text = text.replace(" (the O-72 digit lesson, B-588 class)", "")
    # (10S-F103), (S-16) parenthetical citation tokens
    text = re.sub(r"\s*\(10S-F103\)", "", text)
    text = re.sub(r"\s*\(S-16\)", "", text)
    # ALL remaining B-<digits> tokens, parenthetical or inline
    text = re.sub(r"\bB-\d+[a-zA-Z'’s:]*", "", text)
    # rewrite header without the number token
    text = re.sub(r"## === B-\d+ \(provisional\) — ", "## === ", text)
    # collapse whitespace artifacts
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"  +", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    # verify zero citation tokens remain
    leftovers = re.findall(r"\bB-\d+|\(10S-|\(S-16\)|\(the [A-Za-z-]+ (rule|lesson)", text)
    assert not leftovers, f"citation tokens remain: {leftovers}"
    return text

def build(prov, title, claimed, version, correction=None):
    body = extract(prov, title)
    body = strip_production_note(body)
    body = excise(body)
    body = body.rstrip() + "\n"
    if correction:
        body += "\n---\n\n" + correction + "\n"
    fn = slate / f"fire_b{claimed}_{RUN}_{version}.txt"
    fn.write_text(body)
    md5 = hashlib.md5(body.encode()).hexdigest()
    print(f"{fn.name}  md5={md5}  bytes={len(body.encode())}")
    return fn, md5

results = {}
results["1231"], md5_1231 = build(1895, "THE COAL SIFTER", "1231", "v1")
results["1235"], md5_1235 = build(1896, "THE GAS GAUGE", "1235", "v1")
results["1236"], md5_1236 = build(1897, "THE LAMP FILLER", "1236", "v1")
print("OK", md5_1231, md5_1235, md5_1236)
