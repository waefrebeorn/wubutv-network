#!/usr/bin/env python3
"""Build v1 generation vehicles for the Q2 14:45 bumper-factory run (stall-queue banking):
B-1313 = 1415 B-2619 "The Bike Depot", B-1314 = 1415 B-2620 "The Shelter Sign",
B-1315 = 1415 B-2621 "The Darned Heel".
Verbatim PREPRO extracts, Source line stripped, zero citation tokens,
0815 BUG anti-leak clause on every vehicle, ANTI-UNDERLINE-BAR STACK adapted to
the 1415 format (strong clause in SUBJECTS + NEGATIVE only — exactly 2x per the
1430 double-application fix; the 1415 LOAD-BEARING "pre-emptive stack" reminder
stays as drafted and is NOT triple-strengthened) + the wordmark glyph gate in
LOAD-BEARING for the UNC draft.
No video fires this run (budget outage persists; the 14:28 hard-stop directive
forbids any further video request) — these are durable resume vehicles, banked
so the wheel fires hot the moment the budget resets.
"""
import hashlib, re

PREPRO = "/home/hatch/workspace/wubutv-network/slate/PREPRO_2026-10-20_1415.md"
SLATE = "/home/hatch/workspace/wubutv-network/slate"

ANTI_LEAK = (
    " BUG-CLASS INSTRUCTION-SET HYGIENE: the generated take carries only the scene "
    "itself — no production-slate overlays, no version tokens, no number tokens, no "
    "meta-text describing the bug's spelling, no spelling-out of the tilde instruction "
    "as words; the corner bug renders as plain text only."
)

def add_underline_stack_1415(body):
    # 1415 format: SUBJECTS has "no underline bar under the wordmark, ever;",
    # NEGATIVE has "no underline bar under the wordmark, no meta-text",
    # LOAD-BEARING has "no underline bar under the wordmark, ever (SUBJECTS +
    # LOAD-BEARING + NEGATIVE pre-emptive stack)." — the LOAD-BEARING reminder
    # must NOT receive the strong clause (triple-application; the 1430 fix
    # established exactly 2x: SUBJECTS + NEGATIVE). Target by following context.
    n0 = body.count("ABSOLUTELY NO BAR")
    # NEGATIVE first (bare-comma form, targeted by its unique follower)
    neg_old = "no underline bar under the wordmark, no meta-text"
    assert neg_old in body, "NEGATIVE underline clause not found"
    body = body.replace(
        neg_old,
        "no underline bar under the wordmark, ABSOLUTELY NO BAR, LINE, OR STRIPE "
        "of any kind beneath the six glyphs, the bare black fabric running "
        "uninterrupted directly under the ~WuBu~ glyphs, no meta-text")
    # SUBJECTS (", ever;" form, targeted by its unique follower)
    subj_old = "no underline bar under the wordmark, ever;"
    assert subj_old in body, "SUBJECTS underline clause not found"
    body = body.replace(
        subj_old,
        "no underline bar under the wordmark, ever \u2014 ABSOLUTELY NO BAR, LINE, OR STRIPE "
        "of any kind beneath the six glyphs; the bare black fabric runs uninterrupted "
        "directly under the ~WuBu~ glyphs;")
    # LOAD-BEARING reminder must survive untouched (no strong clause there)
    lb_reminder = ("no underline bar under the wordmark, ever (SUBJECTS + LOAD-BEARING "
                   "+ NEGATIVE pre-emptive stack)")
    assert lb_reminder in body, "LOAD-BEARING stack reminder changed or missing"
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

def extract(prov, underline_stack=False):
    text = open(PREPRO).read()
    m = re.search(rf"## === {prov} \(provisional\) \u2014 [^\n]*\n\n(.*?)\n\n---\n",
                  text, re.S)
    assert m, f"section {prov} not found"
    body = m.group(1)
    # drop the Source:/Setting:/Lore:/Action beats:/Line intro paragraph
    body = re.sub(r"^Source:.*?\n\n", "", body, count=1, flags=re.S)
    # strip parenthetical lesson citation tokens of any letter class: (B-45),
    # (B-79), (B-45: ...), (O-72 ...) — 1045 Q3 CITATION-TOKEN-LEAK lesson
    body = re.sub(r"\([A-Za-z]-\d+[^)]*\)", "", body)
    if underline_stack:
        body = add_underline_stack_1415(body)
    return body.strip()

SPECS = [
    # (provisional, claimed number, vehicle file, underline stack?)
    ("B-2619", "B-1313", "fire_b1313_20261020_1445_v1.txt", False),  # hands-only
    ("B-2620", "B-1314", "fire_b1314_20261020_1445_v1.txt", False),  # hands-only
    ("B-2621", "B-1315", "fire_b1315_20261020_1445_v1.txt", True),   # UNC draft
]

for prov, claimed, fname, stack in SPECS:
    body = extract(prov, stack)
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
