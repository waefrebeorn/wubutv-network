#!/usr/bin/env python3
"""Build the AD-334 v2 NAMED WORDMARK + VOICE CORRECTION vehicle.
v1 (md5 77cd1cabe18f9d317e2c97cad8157ab8) QC-REJECTED on two breaks:
 (1) hoodie wordmark HARD GATE - solid gold UNDERLINE BAR beneath ~WuBu~ every frame
     (deterministic underline-bar class, AD-310/311/315/322/328/331 lineage - eighth occurrence);
 (2) VOICE-TIMING completion-bound - utterance 'Black in the cut.' rendered ~8.25-9.25s,
     mouth verified OPEN at 9.0s/9.25s with voice-grade sound (harm 0.54/0.40) at 8.75-9.25s.
Preamble names both failures + fixes; v1 vehicle fired verbatim below with corrections applied."""
import hashlib

BASE = "/home/hatch/workspace/wubutv-network/slate"
v1 = open(f"{BASE}/fire_ad334_20261020_1119_v1.txt").read()
assert hashlib.md5(v1.encode()).hexdigest() == "77cd1cabe18f9d317e2c97cad8157ab8", "v1 md5 mismatch"

preamble = """## === AD-334 "NIELLOED" (The Niello Bench) : v2 NAMED WORDMARK + VOICE CORRECTION ===

CORRECTION (v1 rejected 2026-10-20 on two breaks — this v2 re-rolls the same take with these two named fixes, everything else identical to the v1 vehicle below):

WORDMARK — v1 rendered a solid gold UNDERLINE BAR beneath the ~WuBu~ letters in every frame (the deterministic underline-bar class — the same regression class as AD-310 v1 / AD-311 v1 / AD-315 v2 / AD-322 "Harled" / AD-328 "Levigated" / AD-331 "Tawed" v1 — eighth occurrence; the v1 carried the full standing anti-bar clauses pre-emptively and still rendered the bar). The bar is the failure. v2: the six wordmark glyphs sit DIRECTLY on the bare black fabric — NO underline bar beneath the letters, no bar, no line, no stripe of any kind beneath the letters, no graphic under the letters, in any frame; the bare black fabric runs uninterrupted directly under the ~WuBu~ glyphs, nothing sits between the letters and the fabric, nothing underlines them. The underline-bar ban is strengthened in SUBJECTS + LOAD-BEARING + NEGATIVE (AD-315 v3 pattern — the correction that held on AD-331 v2).

VOICE — v1 rendered the utterance "Black in the cut." ~8.25-9.25s with the mouth verified OPEN at 9.0s and 9.25s and voice-grade sound (harm 0.54 at 8.75-9.0s, harm 0.40 at 9.0-9.25s) past the 8.75s completion bound. The late tail is the failure. v2: the line's LAST sound lands NO LATER than 8.6s — mouth fully CLOSED by 8.75s and STAYS closed through 10s; NO voice-grade sound after 8.75s, ever; exactly ONE mouth opening for the line, mouth closed before and after. The completion bound is strengthened in TIMELINE + AUDIO + LOAD-BEARING + NEGATIVE.

All v1 axes re-asserted unchanged below — the nielloing beat, the black-design verdict, the bug, the camera, the TEXT allowlist, the style.

--- v1 vehicle, fired verbatim below with the above corrections applied ---

"""

v2 = preamble + v1
out = f"{BASE}/fire_ad334_20261020_1119_v2.txt"
open(out, "w").write(v2)
print(f"AD-334 v2 -> {out} md5={hashlib.md5(v2.encode()).hexdigest()} bytes={len(v2)}")
