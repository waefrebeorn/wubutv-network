#!/usr/bin/env python3
"""Build v1 generation vehicles for the 14:30 factory run:
B-1310 = 1315 B-2612 "The Trued Wheel", B-1311 = 1315 B-2613 "The Wintered Boat",
B-1312 = 1315 B-2614 "The Sewn Signature".
Verbatim PREPRO extracts, Source line stripped, zero citation tokens,
0815 BUG anti-leak clause on every vehicle, ANTI-UNDERLINE-BAR STACK baked into
SUBJECTS + LOAD-BEARING + NEGATIVE for the two UNC drafts (1319 commercial lesson).
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

def add_underline_stack(body):
    # 1319 ANTI-UNDERLINE-BAR STACK: strengthen every "no underline bar" clause and
    # add the wordmark glyph gate to LOAD-BEARING for UNC drafts.
    # NEGATIVE first (bare comma form), then SUBJECTS (", ever" form) — the latter
    # contains the former as a substring, so order matters.
    n_before = body.count("ABSOLUTELY NO BAR")
    body = body.replace(
        "no underline bar under the wordmark,",
        "no underline bar under the wordmark, ABSOLUTELY NO BAR, LINE, OR STRIPE "
        "of any kind beneath the six glyphs, the bare black fabric running "
        "uninterrupted directly under the ~WuBu~ glyphs,")
    body = body.replace(
        "no underline bar under the wordmark, ABSOLUTELY NO BAR, LINE, OR STRIPE "
        "of any kind beneath the six glyphs, the bare black fabric running "
        "uninterrupted directly under the ~WuBu~ glyphs, ever",
        "no underline bar under the wordmark, ever — ABSOLUTELY NO BAR, LINE, OR STRIPE "
        "of any kind beneath the six glyphs; the bare black fabric runs uninterrupted "
        "directly under the ~WuBu~ glyphs")
    # LOAD-BEARING gets the glyph gate if not already present
    if "LOAD-BEARING DETAIL:" in body and "glyph-exact" not in body:
        body = body.replace(
            "LOAD-BEARING DETAIL:",
            "LOAD-BEARING DETAIL: the hoodie wordmark `~ WuBu ~` glyph-exact in every tile "
            "where the chest is visible — six glyphs (tilde, W, u, B, u, tilde), yellow/gold, "
            "both tildes single and wavy, the bare black fabric uninterrupted directly "
            "under the glyphs;")
    # sanity: exactly two ABSOLUTELY-NO-BAR clauses expected (SUBJECTS + NEGATIVE)
    n = body.count("ABSOLUTELY NO BAR")
    assert n == 2, f"underline stack applied {n}x, expected 2"
    return body

def extract(prov, underline_stack=False):
    text = open(PREPRO).read()
    m = re.search(rf"## === {prov} \(provisional\) — [^\n]*\n\n(.*?)\n\n---\n",
                  text, re.S)
    assert m, f"section {prov} not found"
    body = m.group(1)
    # drop the Source:/Setting:/Lore:/Action beats:/Line intro line
    body = re.sub(r"^Source:.*?\n\n", "", body, count=1, flags=re.S)
    # strip parenthetical lesson citation tokens of any letter class: (B-45), (S-16),
    # (B-79: ...), (O-72 ...) — 1045 Q3 CITATION-TOKEN-LEAK + 1215 O-72 lessons
    body = re.sub(r"\([A-Za-z]-\d+[^)]*\)", "", body)
    if underline_stack:
        body = add_underline_stack(body)
    return body.strip()

SPECS = [
    ("B-2612", "fire_b1310_20261020_1430_v1.txt", True),
    ("B-2613", "fire_b1311_20261020_1430_v1.txt", True),
    ("B-2614", "fire_b1312_20261020_1430_v1.txt", False),  # hands-only, no wordmark in frame
]

for prov, fname, stack in SPECS:
    body = extract(prov, stack)
    if not body.endswith(ANTI_LEAK.strip()):
        body += ANTI_LEAK
    leaks = re.findall(r"\([A-Za-z]-\d+[^)]*\)", body)
    assert not leaks, f"citation tokens leaked in {prov}: {leaks}"
    assert f" {prov} " not in body and f"({prov})" not in body, f"number token in {prov}"
    assert "Source:" not in body, f"Source line leaked in {prov}"
    p = f"{SLATE}/{fname}"
    open(p, "w").write(body)
    print(fname, hashlib.md5(open(p, "rb").read()).hexdigest(), len(body), "bytes")
