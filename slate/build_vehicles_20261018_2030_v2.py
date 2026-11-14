#!/usr/bin/env python3
"""Build v2 named-correction vehicles for the 2030 bumper factory run.
B-1236: named SCENE correction (v1 rendered a print shop — total scene miss).
B-1242: named single-axis COUNT correction (v1 rendered a fourth bucket)."""
import hashlib, os

SLATE = os.path.expanduser("~/workspace/wubutv-network/slate")

CORR_1236 = (
    "CORRECTION — the first take of this draft rendered a PRINT SHOP: a printing press, "
    "printed sheets, printed paper. That is the wrong scene and it fails. This take is THE "
    "CUSTOMS SHED, and only the customs shed: one plain wooden CRATE, one plain stick of "
    "CHALK, one plain customs SEAL — NO printing press anywhere, NO printed sheets, NO "
    "printed paper, NO press machinery of any kind. The three beats are exactly: the crate "
    "OPENED at 2s (his hands opening the crate), the mark PAID chalked on the crate at 4-6s "
    "(his hand chalking), the customs seal PRESSED on the crate at 9s. The 9.5s verdict is "
    "the sealed chalked crate with his hands at his sides — never a printed sheet. "
    "Everything else in the draft below holds verbatim.\n\n"
)

CORR_1242 = (
    "CORRECTION — the first take of this draft rendered FOUR buckets at 8s/9.5s. That "
    "breaks the draft's hard rule 'exactly THREE buckets in every frame' and the NEGATIVE "
    "'no fourth bucket'. This take has EXACTLY THREE leather buckets in every frame from 0s "
    "to 10s — the three named buckets MILL, FORD, ASH, one name per bucket — NO fourth "
    "bucket, ever, in any frame, at any timestamp. Three doorsteps, three buckets, one per "
    "doorstep; the 9.5s verdict is exactly three full buckets standing in the dark with his "
    "hands at his sides — never four. Everything else in the draft below holds verbatim.\n\n"
)

def build(num, corr):
    v1 = open(os.path.join(SLATE, f"fire_{num}_20261018_2030_v1.txt")).read()
    body = corr + v1
    out = os.path.join(SLATE, f"fire_{num}_20261018_2030_v2.txt")
    open(out, "w").write(body)
    print(f"{num} v2: {out} md5 {hashlib.md5(body.encode()).hexdigest()} ({len(body)} chars)")

build("b1236", CORR_1236)
build("b1242", CORR_1242)
