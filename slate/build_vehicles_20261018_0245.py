#!/usr/bin/env python3
"""Build script-built fire vehicles for the 2026-10-18 0245 bumper factory run.
Per the FIRE-VEHICLE TRANSCRIPTION-SLIP datum: fire from script-built vehicles,
never hand-pasted. Excision discipline: ALL B-<digits> tokens + all parenthetical
citation tokens ((10S-F103), (S-16)) stripped; Production note stripped."""
import re, hashlib, pathlib

slate = pathlib.Path.home() / "workspace/wubutv-network/slate"
pre = (slate / "PREPRO_2026-10-18_0115.md").read_text()
RUN = "20261018_0245"

def extract(prov, title):
    pat = re.compile(r"## === B-%d \(provisional\) — \"%s\" : GENERATION PROMPT ===\n" % (prov, title))
    m = pat.search(pre)
    assert m, f"section not found: B-{prov} {title}"
    start = m.start()
    end = pre.find("---\n\n", m.end())
    assert end > 0
    return pre[start:end]

def strip_production_note(text):
    # remove the "Production note:" paragraph (up to the blank line before Hand-painted)
    text, n = re.subn(r"Production note: .*?\n\n", "", text, flags=re.S, count=1)
    assert n == 1, "production note not stripped"
    return text

def excise(text):
    # (10S-F103), (S-16) parenthetical citation tokens
    text = re.sub(r"\s*\(10S-F103\)", "", text)
    text = re.sub(r"\s*\(S-16\)", "", text)
    # B-<digits> tokens: keep header but reword inline references
    text = text.replace("B-386's transmitter-hut station", "the transmitter-hut station")
    text = text.replace("(the B-588 rule — a legible docket is a text break)", "(a legible docket is a text break)")
    text = re.sub(r"\bB-\d+[a-zA-Z'’s]*", "", text)
    # rewrite header without the number token
    text = re.sub(r"## === B-\d+ \(provisional\) — ", "## === ", text)
    # collapse whitespace artifacts
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"  +", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    # verify zero citation tokens remain
    leftovers = re.findall(r"\bB-\d+|\(10S-|\(S-16\)", text)
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
    return fn

CORR_B1235 = """RECLAIM v2 — two named axes (verdict + voice-timing), built on the verbatim v1 extract:
AXIS 1 — VERDICT: at 9.5s the smoker is SET DOWN — it rests on the ground (or the hive stand), nowhere in his hands; the hive closed; his hands are at his sides, empty and still. The smoker leaves his hand at the 9s set-back and never returns to it; no smoker in hand at the verdict frame.
AXIS 2 — VOICE-TIMING: exactly ONE voice event in the entire take — the single directed line "The queen is home." — its FIRST SOUND lands AT 7.5s or LATER, never before 7.5s, ever; the utterance is COMPLETE BY 8.75s; his mouth stays fully CLOSED before 7.5s and fully CLOSED after 8.75s; no voice event, no harmonic tonal event, no mouth-open sound of any kind anywhere else in the take — no tonal event at 9.0s or anywhere past 8.75s, ever; the soft smoker-puff bed at 2s is the ONLY other directed sound.
All other blocks hold unchanged (SUBJECTS, TIMELINE, CAMERA, AUDIO beds, LOAD-BEARING DETAIL, TEXT allowlist none, the exactly-two-lines corner bug, CANON, NEGATIVE, the wordmark ~WuBu~ six glyphs both tildes, the frozen framing, the one smoke at 2s / one lift 4-6s / one set-back at 9s)."""

build(1893, "THE TUBE DOCKET", "1231", "v1")
build(1892, "THE APIARY CHECK", "1235", "v2", correction=CORR_B1235)
build(1894, "THE PIGEON LOFT", "1236", "v1")
print("OK")
