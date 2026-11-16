#!/usr/bin/env python3
"""Build the v2 named BUG correction vehicle for B-1255 (The Groyne).
v1 rendered a forbidden THIRD line under the corner bug: the literal text
'tilde space W u B u space tilde'. The correction names that exact string and
re-asserts the exact two-line bug. Zero citation tokens."""
import hashlib

SLATE = "/home/hatch/workspace/wubutv-network/slate"

CORRECTION = """CORRECTION — the first take of this draft rendered a forbidden THIRD line of text under the corner bug: the literal words "tilde space W u B u space tilde". That third line is banned and it fails. This take has EXACTLY TWO lines in the corner bug and nothing else: line one "~ WuBu ~" (tilde, space, W-u-B-u, space, tilde), line two "WuBuTV" — bottom-right, plain white text printed directly over the picture, fully opaque from frame 0, identical in all 240 frames. NO third line, NO descriptive text about the bug, NO words spelling out the bug's spelling, NO meta-text. Everything else in the draft below holds verbatim.

"""

with open(f"{SLATE}/fire_b1255_20261019_0145_v1.txt") as f:
    v1 = f.read()

body = CORRECTION + v1
# strengthen the NEGATIVE's no-third-line ban explicitly
body = body.replace(
    "no third line under the bug,",
    "no third line under the bug, no descriptive text about the bug's spelling,",
    1,
)

out = f"{SLATE}/fire_b1255_20261019_0145_v2.txt"
with open(out, "w") as f:
    f.write(body)
md5 = hashlib.md5(body.encode()).hexdigest()
print(f"b1255 v2: {out} md5 {md5} ({len(body)} chars)")
# zero citation tokens check
import re
toks = re.findall(r"\bB-\d+\b|\b10S-[A-Z]+\d*\b|\bMEME-[A-Z]+\d*\b", body)
if toks:
    raise SystemExit(f"citation token leaked: {toks}")
print("zero citation tokens confirmed")
