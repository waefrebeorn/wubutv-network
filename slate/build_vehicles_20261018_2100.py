import re, hashlib, pathlib
slate = pathlib.Path("/home/hatch/workspace/wubutv-network/slate")
pre = (slate/"PREPRO_2026-10-18_0315.md").read_text()
def extract(provisional, outname):
    # capture the section for the provisional number up to the trailing --- separator
    m = re.search(rf"## === {provisional} \(provisional\) — .*? : GENERATION PROMPT ===\n\n(.*?)\n\n---\n", pre, re.S)
    assert m, provisional
    body = m.group(1)
    # keep from the prompt start (drop Source: + Production note: paragraphs)
    i = body.find("Hand-painted 2D cartoon")
    assert i > 0, provisional
    prompt = body[i:].strip() + "\n"
    # provenance checks: no citation/version/number tokens
    for pat in (r"\(10S-[^)]*\)", r"\(B-\d+[^)]*\)", r"\(AD-\d+[^)]*\)", r"\(E-\d+[^)]*\)"):
        hits = re.findall(pat, prompt)
        assert not hits, (provisional, pat, hits[:3])
    assert "Production note:" not in prompt, provisional
    p = slate/outname
    p.write_text(prompt)
    print(outname, "md5", hashlib.md5(prompt.encode()).hexdigest(), "bytes", len(prompt))
extract("B-1913", "fire_b1242_20261018_2100_v1.txt")
extract("B-1914", "fire_b1244_20261018_2100_v1.txt")
