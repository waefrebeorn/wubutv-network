#!/usr/bin/env python3
"""Build the B-1269 v2 correction vehicle (named two-axis WORDMARK + VOICE correction).
Header names the exact v1 failures per the WORDMARK-CORRECTION-HEADER and VOICE-CORRECTION precedents;
v1 vehicle follows verbatim. No quoted forbidden tokens (B-1202). Zero citation tokens."""
import hashlib, re

V1 = "fire_b1269_20261019_0345_v1.txt"
vehicle = open(V1, encoding="utf-8").read()

HEADER = (
    'WORDMARK + VOICE CORRECTION - READ FIRST, THIS IS LOAD-BEARING: the previous take broke on two axes. '
    '(1) WORDMARK: the hoodie wordmark\'s trailing tilde rendered as a straight dash on the 4s tile - '
    'the six glyphs must read exactly tilde, W, u, B, u, tilde, with BOTH tildes as standalone wavy '
    'punctuation characters, never a dash, never doubled, never fused onto adjacent letters; '
    'the six wordmark glyphs sit DIRECTLY on the bare black fabric. '
    '(2) VOICE: the previous take never voiced the directed line at all - no voice-grade audio anywhere '
    'in the 7.5-8.75s window (the 8.0-8.75s bins measured -48 to -52 dBFS, digital silence) and the mouth '
    'was verified CLOSED at 8.0s (the mouth never opened for the line - the voice-missing class). '
    'This take MUST render the directed line "Every hook is empty." as one audible voiced utterance in the '
    '7.5-8.75s window: the mouth fully CLOSED through 7.4s - no open mouth and no voice-grade sound before '
    '7.5s, ever; his mouth opens ONCE, on the lens, at ~8s, and the single continuous utterance '
    '"Every hook is empty." is audible voiced speech - the line\'s FIRST SOUND lands AT 7.5s or LATER, '
    'never before 7.5s; the utterance COMPLETE BY 8.75s; no second utterance; no voice event before 7.5s, '
    'ever. Everything else identical to the prompt below.\n\n'
)

out_text = HEADER + vehicle
assert not re.search(r"\[\d+\]|\[cite", out_text), "citation token"
out = "fire_b1269_20261019_0345_v2.txt"
open(out, "w", encoding="utf-8").write(out_text)
print(f"{out}: {len(out_text)} bytes, md5 {hashlib.md5(out_text.encode()).hexdigest()}")
print("header check:", "WORDMARK + VOICE CORRECTION" in out_text, "| line check:", '"Every hook is empty."' in out_text)
print("OK")
