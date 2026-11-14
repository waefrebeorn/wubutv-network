#!/usr/bin/env python3
"""Build v2 named-correction vehicles for the 2026-10-18 23:15 EDT bumper run.
Correction block promoted to FIRST load-bearing position (AD-290 B-766 lesson);
v1's exact failures named explicitly; all held axes re-asserted in the block.
FIRE-VEHICLE TRANSCRIPTION-SLIP: never hand-assemble — script-built only."""
import hashlib, re

def build(v1_path, v2_path, correction):
    with open(v1_path) as f:
        v1 = f.read().rstrip("\n")
    assert v1.startswith("Hand-painted 2D cartoon"), "v1 vehicle malformed"
    text = correction.strip() + "\n\n" + v1
    assert not re.search(r"\[[0-9]+\]|\[citation", text), "citation token found"
    with open(v2_path, "w") as f:
        f.write(text)
    md5 = hashlib.md5(text.encode()).hexdigest()
    print(f"{v2_path}: {len(text)} bytes, md5 {md5}")

# B-1236 v2: named two-axis VOICE-TIMING + BUG correction
build(
    "/home/hatch/workspace/wubutv-network/slate/fire_b1236_20261018_2315_v1.txt",
    "/home/hatch/workspace/wubutv-network/slate/fire_b1236_20261018_2315_v2.txt",
    """CORRECTION — the first take of this draft failed on two axes, and this take fixes both. (1) VOICE-TIMING: v1 rendered a loud voice-grade event spanning 6.75s-7.75s (peaking -6.6 dBFS at 7.0s) with the mouth verified OPEN at 7.0s — the line sounding BEFORE the 7.5s cutoff, the B-1083 early-voice break. This take: his mouth is CLOSED and motionless from 0s through 7.5s — no voice event and no mouth opening before 7.5s, ever; the directed line's FIRST SOUND lands AT 7.5s or LATER; exactly ONE mouth opening in the entire take, at ~8s, for the one directed line "The tide is hired."; the mouth closed again by 8.75s and staying closed through 10s. (2) BUG: v1's corner bug flickered — at 7.0s line one rendered "WuBu ~" with the leading tilde and space missing, while other frames held "~ WuBu ~". This take: the bug's line one reads "~ WuBu ~" — tilde, space, W-u-B-u, space, tilde, the leading tilde present and legible — in EVERY frame, all 240 frames identical, fully opaque from frame 0, fixed at the bottom-right corner, never flickering, never changing. The voice-timing lock and the bug lock hold alongside every other lock in the draft below, which holds verbatim.""",
)

# B-1247 v2: named two-axis WORDMARK + VERDICT correction
build(
    "/home/hatch/workspace/wubutv-network/slate/fire_b1247_20261018_2315_v1.txt",
    "/home/hatch/workspace/wubutv-network/slate/fire_b1247_20261018_2315_v2.txt",
    """CORRECTION — the first take of this draft failed on two axes, and this take fixes both. (1) WORDMARK: v1 rendered the hoodie wordmark as "~WuBu" — the TRAILING tilde missing, five glyphs — on the 8s and 9.5s frames, failing the wordmark hard gate. This take: the hoodie wordmark reads exactly "~WuBu~" — six glyphs total, tilde, W, u, B, u, tilde, BOTH tildes single, wavy, fully rendered, yellow/gold, on bare black fabric — in EVERY frame, on the 0.5s, 8s, and 9.5s front-facing frames, no missing tilde ever, no single-sided wordmark ever. (2) VERDICT: v1 left the boat sitting in the slip on its carriage at 9.5s — the draft's NEGATIVE bans any boat in the slip at 9.5s, and the empty slip is the verdict. This take: at 9.5s the boat is GONE, the slip EMPTY, the doors open, his hands at his sides — the empty slip is the verdict; the boat run out and away is the proof, staged as the 4s-6s run-out with the crew's hands ONLY on the carriage. The wordmark lock and the verdict lock hold alongside every other lock in the draft below, which holds verbatim.""",
)

print("done — v2 correction vehicles on disk, fire verbatim")
