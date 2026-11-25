#!/usr/bin/env python3
"""Build v1 generation vehicles for the Q2 15:00 bumper-factory run (stall-queue banking):
B-1316 = 1315 B-2615 "The Noon Mark", B-1317 = 1315 B-2616 "The Brass Ring",
B-1318 = 1315 B-2617 "The Poured Cup".
Verbatim PREPRO extracts, Source paragraph stripped, zero citation tokens,
0815 BUG anti-leak clause on every vehicle, ANTI-UNDERLINE-BAR STACK adapted to
the 1315 format (strong clause in SUBJECTS + NEGATIVE only — exactly 2x per the
1430 double-application fix; the 1315 drafts carry no LOAD-BEARING pre-emptive
stack reminder, so nothing to preserve) + the wordmark glyph gate in
LOAD-BEARING for all three UNC drafts.
No video fires this run (budget outage persists; the 14:52 hard-stop directive
forbids any further video request) — these are durable resume vehicles, banked
so the wheel fires hot the moment the budget resets.
"""
import hashlib, re

PREPRO = "/home/hatch/workspace/wubutv-network/slate/PREPRO_2026-10-20_1315.md"
SLATE = "/home/hatch/workspace/wubutv-network/slate"

ANTI_LEAK = (
    " BUG-CLASS INSTRUCTION-SET HYGIENE: the generated take carries only the scene "
    "itself — no production-slate overlays, no version tokens, no number tokens, no "
    "meta-text describing the bug's spelling, no spelling-out of the tilde instruction "
    "as words; the corner bug renders as plain text only."
)

def add_underline_stack_1315(body):
    # 1315 format: SUBJECTS has "no underline bar under the wordmark, ever;",
    # NEGATIVE has "no underline bar under the wordmark, no meta-text describing
    # the bug's spelling". Strong clause exactly 2x (SUBJECTS + NEGATIVE), per the
    # 1430 double-application fix. No LOAD-BEARING stack reminder exists in the
    # 1315 drafts, so nothing to guard there.
    n0 = body.count("ABSOLUTELY NO BAR")
    # NEGATIVE first (bare-comma form)
    neg_old = "no underline bar under the wordmark, no meta-text"
    assert neg_old in body, "NEGATIVE underline clause not found"
    body = body.replace(
        neg_old,
        "no underline bar under the wordmark, ABSOLUTELY NO BAR, LINE, OR STRIPE "
        "of any kind beneath the six glyphs, the bare black fabric running "
        "uninterrupted directly under the ~WuBu~ glyphs, no meta-text")
    # SUBJECTS (", ever;" form)
    subj_old = "no underline bar under the wordmark, ever;"
    assert subj_old in body, "SUBJECTS underline clause not found"
    body = body.replace(
        subj_old,
        "no underline bar under the wordmark, ever \u2014 ABSOLUTELY NO BAR, LINE, OR STRIPE "
        "of any kind beneath the six glyphs; the bare black fabric runs uninterrupted "
        "directly under the ~WuBu~ glyphs;")
    # LOAD-BEARING gets the wordmark glyph gate if not already present
    if "LOAD-BEARING DETAIL:" in body and "glyph-exact" not in body:
        body = body.replace(
            "LOAD-BEARING DETAIL:",
            "LOAD-BEARING DETAIL: the hoodie wordmark `~ WuBu ~` glyph-exact in every tile "
            "where the chest is visible \u2014 six glyphs (tilde, W, u, B, u, tilde), yellow/gold, "
            "both tildes single and wavy, the bare black fabric uninterrupted directly "
            "under the glyphs;")
    n = body.count("ABSOLUTELY NO BAR")
    assert n - n0 == 2, f"underline stack applied {n - n0}x, expected 2"
    return body

def extract(prov):
    text = open(PREPRO).read()
    m = re.search(rf"## === {prov} \(provisional\) \u2014 [^\n]*\n\n(.*?)\n\n---\n",
                  text, re.S)
    assert m, f"section {prov} not found"
    body = m.group(1)
    # drop the Source:/Setting:/Lore:/Action beats:/Line intro paragraph
    body = re.sub(r"^Source:.*?\n\n", "", body, count=1, flags=re.S)
    # strip parenthetical lesson citation tokens of any letter class: (B-45),
    # (B-79), (B-45: ...), (O-72 ...), (B-85 zoom-crop) — 1045 Q3
    # CITATION-TOKEN-LEAK lesson, hardened [A-Za-z]-\d+ strip
    body = re.sub(r"\([A-Za-z]-\d+[^)]*\)", "", body)
    body = add_underline_stack_1315(body)
    return body.strip()

SPECS = [
    # (provisional, claimed number, vehicle file)
    ("B-2615", "B-1316", "fire_b1316_20261020_1500_v1.txt"),
    ("B-2616", "B-1317", "fire_b1317_20261020_1500_v1.txt"),
    ("B-2617", "B-1318", "fire_b1318_20261020_1500_v1.txt"),
]

for prov, claimed, fname in SPECS:
    body = extract(prov)
    if not body.endswith(ANTI_LEAK.strip()):
        body += ANTI_LEAK
    leaks = re.findall(r"\([A-Za-z]-\d+[^)]*\)", body)
    assert not leaks, f"citation tokens leaked in {prov}: {leaks}"
    for tok in (prov, claimed):
        assert f" {tok} " not in body and f"({tok})" not in body, \
            f"number token {tok} in {prov}"
    assert "Source:" not in body, f"Source line leaked in {prov}"
    p = f"{SLATE}/{fname}"
    open(p, "w").write(body)
    print(fname, hashlib.md5(open(p, "rb").read()).hexdigest(), len(body), "bytes")
