#!/usr/bin/env python3
"""Build script-built fire vehicles for the 2026-10-18 0445 episode factory run.

Episode-factory convention (per fire_e184/e185/e186_20261018_0045): the stage
is fired VERBATIM including the production note. Only the provisional-number
header token is rewritten ("## === #263 (provisional) — " -> "## === "),
because number tokens are banned by every stage's NEGATIVE block.
The #263/#264/#265 sections carry zero B-digit / parenthetical citation tokens
(verified at claim time), so no excision pass is needed.
Per the FIRE-VEHICLE TRANSCRIPTION-SLIP datum: fire from the on-disk vehicle
file's bytes verbatim, never from a hand transcription."""
import re, hashlib, pathlib

slate = pathlib.Path.home() / "workspace/wubutv-network/slate"
pre = (slate / "PREPRO_2026-10-18_0415.md").read_text()
RUN = "20261018_0445"

def extract(prov):
    pat = re.compile(r"## === #%d \(provisional\) — " % prov)
    m = pat.search(pre)
    assert m, f"section not found: #{prov}"
    start = m.start()
    end = pre.find("---\n\n", m.end())
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

build(263, "190", "v1")
build(264, "191", "v1")
build(265, "192", "v1")
print("OK")
