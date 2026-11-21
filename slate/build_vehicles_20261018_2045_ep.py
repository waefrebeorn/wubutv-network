#!/usr/bin/env python3
"""Build script-built fire vehicles for the 2026-10-18 2045 episode factory run.

Episode-factory convention (1845-run precedent): the stage is fired VERBATIM
from the PREPRO section bytes — header with provisional number intact,
production note intact, no token excision (1845's E192 fired with its
(B-26/B-588) tokens verbatim and shipped clean). Extraction is byte-exact
between the section header and the next "---" delimiter; md5 is printed and
must be verified before each fire.
Per the FIRE-VEHICLE TRANSCRIPTION-SLIP datum: fire from the on-disk vehicle
file's bytes verbatim, never from a hand transcription."""
import re, hashlib, pathlib

slate = pathlib.Path.home() / "workspace/wubutv-network/slate"
pre = (slate / "PREPRO_2026-10-18_2015.md").read_text()
RUN = "20261018_2045"

def extract(prov):
    pat = re.compile(r"## === #%d \(provisional\) — " % prov)
    m = pat.search(pre)
    assert m, f"section not found: #{prov}"
    start = m.start()
    delim = pre.find("\n---\n", m.end())
    assert delim > 0, f"no trailing delimiter for #{prov}"
    return pre[start:delim].rstrip() + "\n"

def build(prov, ledger, version, correction=None):
    body = extract(prov)
    if correction:
        body += "\n---\n\n" + correction + "\n"
    fn = slate / f"fire_e{ledger}_{RUN}_{version}.txt"
    fn.write_text(body)
    md5 = hashlib.md5(body.encode()).hexdigest()
    print(f"{fn.name}  md5={md5}  bytes={len(body.encode())}")
    return fn

build(311, "193", "v1")
build(312, "194", "v1")
build(313, "195", "v1")
print("OK")
