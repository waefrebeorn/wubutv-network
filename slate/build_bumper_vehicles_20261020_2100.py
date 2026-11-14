"""Build durable fire vehicles for the 2026-10-20 21:00 EDT bumper-factory stall run.

1815-new-format verbatim **SUBJECTS**-header extracts through NEGATIVE, no draft
header, no Source paragraph; hardened citation-token strip — colon-class
unwrapped, backstop kills any remaining (X-NNN...) form, bare-token strip kills
unwrapped B-NNN refs; lineage-only adjudication sentences dropped as factory
meta-text; stranded-comma/empty-paren/double-space collapse; native
anti-underline-bar stack asserted >=2 on all three UNC drafts (B-2689/B-2690/B-2691:
SUBJECTS full + LOAD-BEARING shortened + 'no underline bar' in NEGATIVE);
0815 BUG anti-leak clause appended; zero citation tokens asserted; size sanity 2-8KB.
"""
import hashlib, re

OUT = "/home/hatch/workspace/wubutv-network/slate"

# (prepro file, provisional number, pool number, title)
JOBS = [
    ("/home/hatch/workspace/wubutv-network/slate/PREPRO_2026-10-20_1915.md", "2689", "B-1385", "The Dowel"),
    ("/home/hatch/workspace/wubutv-network/slate/PREPRO_2026-10-20_1915.md", "2690", "B-1386", "The Battery Room"),
    ("/home/hatch/workspace/wubutv-network/slate/PREPRO_2026-10-20_2015.md", "2691", "B-1387", "The Corrector Spheres"),
]

ANTI_LEAK = ("\n\n---. BUG-CLASS INSTRUCTION-SET HYGIENE: the generated take carries only "
            "the scene itself \u2014 no production-slate overlays, no version tokens, no "
            "number tokens, no meta-text describing the bug's spelling, no spelling-out of "
            "the tilde instruction as words; the corner bug renders as plain text only.")

def extract(prepro, prov):
    src = open(prepro).read()
    start = src.find("## === B-%s (provisional)" % prov)
    if start < 0:
        raise RuntimeError("section B-%s not found in %s" % (prov, prepro))
    end = src.find("## === B-%d (provisional)" % (int(prov) + 1), start)
    section = src[start:] if end < 0 else src[start:end]
    subj = section.find("**SUBJECTS**")
    if subj < 0:
        raise RuntimeError("SUBJECTS missing in B-%s" % prov)
    body = section[subj:]
    neg = body.find("**NEGATIVE**")
    neg_end = body.find("\n---\n", neg)
    body = body[:neg_end] if neg_end > 0 else body
    return body.strip()

def strip_tokens(t):
    t = re.sub(r"\([BSE]-\d+[^)]*\)", "", t)          # parenthetical B-/S-/E-NNN forms incl. colon class
    t = re.sub(r"\([A-Z]{1,3}-\d+[^)]*\)", "", t)     # backstop: any (X-NNN...) form
    t = re.sub(r"\b[A-Z]{1,3}-\d+\b", "", t)          # bare unwrapped B-NNN-style refs
    t = re.sub(r"\([^)]{0,1}\)", "", t)               # stranded empty parens
    t = re.sub(r"\s*,\s*,", ",", t)
    t = re.sub(r"\(\s*,", "(", t)
    t = re.sub(r",\s*\)", ")", t)
    t = re.sub(r"[ \t]{2,}", " ", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip()

CITATION = re.compile(r"\([BSE]-\d+[^)]*\)|\bB-\d{2,}\b")

for prepro, prov, pool, title in JOBS:
    body = extract(prepro, prov)
    body = strip_tokens(body)
    barstack = 0
    low = body.lower()
    if "absolutely no bar, line, or stripe of any kind beneath the six glyphs" in low:
        barstack += 1
    if "bare black fabric runs uninterrupted directly under" in low:
        barstack += 1
    if "no underline bar beneath the wordmark glyphs" in low:
        barstack += 1
    assert barstack >= 2, "%s barstack=%d" % (pool, barstack)
    assert CITATION.search(body) is None, "%s has citation tokens: %s" % (pool, CITATION.search(body).group(0))
    vehicle = body + ANTI_LEAK
    n = len(vehicle.encode("utf-8"))
    assert 2048 <= n <= 8192, "%s size %d out of 2-8KB sanity" % (pool, n)
    fn = "%s/fire_b%s_20261020_2100_v1.txt" % (OUT, pool[2:])
    open(fn, "w").write(vehicle)
    md5 = hashlib.md5(vehicle.encode("utf-8")).hexdigest()
    print("%s %-18s md5=%s bytes=%d barstack=%d" % (pool, fn.split("/")[-1], md5, n, barstack))
print("OK \u2014 zero citation tokens, all assertions passed")
