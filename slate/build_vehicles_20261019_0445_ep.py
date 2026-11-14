#!/usr/bin/env python3
"""Build script-built fire vehicles for the 2026-10-19 0445 episode factory run.

Episode-factory convention (per fire_e190/e191/e192_20261018_0445): the stage
is fired VERBATIM including the production note. Only the provisional-number
header token is rewritten ("## === #337 (provisional) — " -> "## === "),
because number tokens are banned by every stage's NEGATIVE block.
Verified at claim time: zero B-digit tokens in the three sections; header is
the only #NNN (provisional) token.
Per the FIRE-VEHICLE TRANSCRIPTION-SLIP datum: fire from the on-disk vehicle
file's bytes verbatim, never from a hand transcription."""
import re, hashlib, pathlib

slate = pathlib.Path.home() / "workspace/wubutv-network/slate"
pre = (slate / "PREPRO_2026-10-19_0115.md").read_text()
RUN = "20261019_0445"

def extract(prov):
    pat = re.compile(r"## === #%d \(provisional\) — " % prov)
    m = pat.search(pre)
    assert m, f"section not found: #{prov}"
    start = m.start()
    # section boundaries are "---\n" (the 0115 file's --- lines have one or two
    # trailing newlines); take the body up to the boundary line itself
    end = pre.find("\n---\n", m.end())
    if end < 0:
        end = len(pre)  # last section in the file has no trailing delimiter
    return pre[start:end]

def rewrite_header(text):
    # drop the provisional-number token from the header only
    text, n = re.subn(r"## === #\d+ \(provisional\) — ", "## === ", text, count=1)
    assert n == 1, "header rewrite failed"
    return text

def build(prov, ledger, version, correction=None):
    body = extract(prov)
    body = rewrite_header(body)
    # verify zero citation tokens remain
    leftovers = re.findall(r"\bB-\d+|#\d+ \(provisional\)|\([A-Z0-9-]*-[A-Z0-9]+\)", body)
    assert not leftovers, f"tokens remain: {leftovers}"
    body = body.rstrip() + "\n"
    if correction:
        body += "\n---\n\n" + correction + "\n"
    fn = slate / f"fire_e{ledger}_{RUN}_{version}.txt"
    fn.write_text(body)
    md5 = hashlib.md5(body.encode()).hexdigest()
    print(f"{fn.name}  md5={md5}  bytes={len(body.encode())}")
    return fn

build(337, "205", "v1")
build(338, "206", "v1")
build(339, "207", "v1")
print("OK")
