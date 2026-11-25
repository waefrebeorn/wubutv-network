#!/usr/bin/env python3
"""Build fire vehicles for the 2026-10-18 2245 bumper factory run.

Extracts GENERATION PROMPT bodies:
  0315 B-1922 ("The Maltings")      -> B-1236 (freed pool number)
  0415 B-1923 ("The Telegram Boy")  -> B-1247 (fresh pool number)
  0415 B-1924 ("The Quarry Face")   -> B-1248 (fresh pool number)
Strips Source: / Production note: lines + header; excises B-digit and
citation tokens. Zero-citation fire vehicles.
"""
import hashlib, re

OUTDIR = "/home/hatch/workspace/wubutv-network/slate"

TARGETS = {
    ("/home/hatch/workspace/wubutv-network/slate/PREPRO_2026-10-18_0315.md", "B-1922"): "fire_b1236_20261018_2245_v1.txt",
    ("/home/hatch/workspace/wubutv-network/slate/PREPRO_2026-10-18_0415.md", "B-1923"): "fire_b1247_20261018_2245_v1.txt",
    ("/home/hatch/workspace/wubutv-network/slate/PREPRO_2026-10-18_0415.md", "B-1924"): "fire_b1248_20261018_2245_v1.txt",
}

def extract(src, prov):
    text = open(src).read()
    m = re.search(r"## === " + re.escape(prov) + r" \(provisional\).*?\n(.*?)\n---",
                  text, re.S)
    if not m:
        raise SystemExit("draft %s not found in %s" % (prov, src))
    body = m.group(1).strip()
    lines = []
    skip = True
    for ln in body.splitlines():
        s = ln.strip()
        if skip:
            if not s:
                continue
            if s.startswith("Source:") or s.startswith("Production note:"):
                continue
            if s.startswith("Hand-painted"):
                skip = False
            else:
                continue
        lines.append(ln)
    body = "\n".join(lines).strip()
    body = re.sub(r"\bB-\d+\b", "", body)
    body = re.sub(r"\([0-9A-Z]+-[0-9A-Z]+\)", "", body)
    body = re.sub(r"[ \t]{2,}", " ", body)
    return body

for (src, prov), fname in TARGETS.items():
    body = extract(src, prov)
    assert "Source:" not in body and "Production note:" not in body, prov
    assert re.search(r"\bB-\d+\b", body) is None, prov
    assert re.search(r"\([0-9A-Z]+-[0-9A-Z]+\)", body) is None, prov
    path = OUTDIR + "/" + fname
    open(path, "w").write(body + "\n")
    print(fname, hashlib.md5(open(path, "rb").read()).hexdigest(), len(body))
