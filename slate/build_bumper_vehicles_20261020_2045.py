"""Build durable fire vehicles for the 2026-10-20 20:45 EDT bumper-factory stall run.

1815-new-format verbatim **SUBJECTS**-header extracts through NEGATIVE, no draft
header, no Source paragraph; hardened citation-token strip — colon-class
unwrapped, backstop kills any remaining (X-NNN...) form, bare-token strip kills
unwrapped B-NNN refs; lineage-only adjudication sentences dropped as factory
meta-text; stranded-comma/empty-paren/double-space collapse; native
anti-underline-bar stack asserted >=2 on all three UNC drafts (B-2686/B-2687/B-2688:
SUBJECTS full + LOAD-BEARING shortened + 'no underline bar' in NEGATIVE);
0815 BUG anti-leak clause appended; zero citation tokens asserted; size sanity 2-8KB.
"""
import hashlib, re, sys

PREPRO = "/home/hatch/workspace/wubutv-network/slate/PREPRO_2026-10-20_1915.md"
OUT = "/home/hatch/workspace/wubutv-network/slate"

# (provisional number, pool number, title)
JOBS = [
    ("2686", "B-1382", "The Mitre"),
    ("2687", "B-1383", "The Wicket Gate"),
    ("2688", "B-1384", "The Stencil"),
]

ANTI_LEAK = ("\n\n---. BUG-CLASS INSTRUCTION-SET HYGIENE: the generated take carries only "
            "the scene itself \u2014 no production-slate overlays, no version tokens, no "
            "number tokens, no meta-text describing the bug's spelling, no spelling-out of "
            "the tilde instruction as words; the corner bug renders as plain text only.")

src = open(PREPRO).read()

def extract(prov):
    """Verbatim section for provisional number, from **SUBJECTS** through NEGATIVE block."""
    start = src.find("## === B-%s (provisional)" % prov)
    if start < 0:
        raise RuntimeError("section B-%s not found" % prov)
    end = src.find("## === B-%d (provisional)" % (int(prov) + 1), start)
    section = src[start:] if end < 0 else src[start:end]
    subj = section.find("**SUBJECTS**")
    if subj < 0:
        raise RuntimeError("SUBJECTS missing in B-%s" % prov)
    body = section[subj:]
    # trim trailing '---' separator and anything after the NEGATIVE block
    neg = body.find("**NEGATIVE**")
    neg_end = body.find("\n---\n", neg)
    body = body[:neg_end] if neg_end > 0 else body
    return body.strip()

def strip_tokens(t):
    # colon-class: (B-123: ...) -> keep nothing (unwrap keeps prose, here just kill whole)
    t = re.sub(r"\([BSE]-\d+[^)]*\)", "", t)          # parenthetical B-/S-/E-NNN forms incl. colon class
    t = re.sub(r"\([A-Z]{1,3}-\d+[^)]*\)", "", t)     # backstop: any (X-NNN...) form
    t = re.sub(r"\b[A-Z]{1,3}-\d+\b", "", t)         # bare unwrapped B-NNN-style refs
    # stranded-comma / empty-paren / double-space collapse
    t = re.sub(r"\([^)]{0,1}\)", "", t)
    t = re.sub(r"\s*,\s*,", ",", t)
    t = re.sub(r"\(\s*,", "(", t)
    t = re.sub(r",\s*\)", ")", t)
    t = re.sub(r"[ \t]{2,}", " ", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip()

CITATION = re.compile(r"\([BSE]-\d+[^)]*\)|\bB-\d{2,}\b")

for prov, pool, title in JOBS:
    body = extract(prov)
    body = strip_tokens(body)
    # anti-underline-bar stack: >=2 of the three native sites
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
    fn = "%s/fire_b%s_20261020_2045_v1.txt" % (OUT, pool[2:])
    open(fn, "w").write(vehicle)
    md5 = hashlib.md5(vehicle.encode("utf-8")).hexdigest()
    print("%s %-18s md5=%s bytes=%d barstack=%d" % (pool, fn.split("/")[-1], md5, n, barstack))
print("OK — zero citation tokens, all assertions passed")
