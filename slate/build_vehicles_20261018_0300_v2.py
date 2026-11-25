#!/usr/bin/env python3
"""Build v2 correction vehicles for the 2026-10-18 0300 bumper factory run.
B-1235 v2: named WORDMARK correction (v1 rendered 'ĩWuBũ' diacritics, not '~WuBu~').
B-1236 v2: named VOICE-TIMING correction (v1 mouth never opened; no voice event)."""
import hashlib, pathlib

slate = pathlib.Path.home() / "workspace/wubutv-network/slate"
RUN = "20261018_0300"

CORR_B1235_WORDMARK = """V2 — NAMED WORDMARK CORRECTION (v1 rendered the wordmark as 'ĩWuBũ' — the tildes fused as diacritic marks over i/u letters — vs the drafted '~WuBu~'; WORDMARK HARD GATE failed on v1):

The hoodie wordmark MUST read as exactly SIX SEPARATE, STANDALONE GLYPHS: [1] a tilde '~' as an independent wavy horizontal line, [2] capital W, [3] lowercase u, [4] capital B, [5] lowercase u, [6] a tilde '~' as an independent wavy horizontal line. The two tildes are PUNCTUATION CHARACTERS printed on the black fabric — they are NOT accent marks, NOT diacritics, NOT breve marks, NOT attached to any letter, NOT floating above any letter. There is visible bare black fabric between the first tilde and the W, and between the final u and the last tilde. The letters themselves are plain: W, u, B, u — no marks on them, no dotted letters, no diacritics on any letter. Yellow/gold letters on bare black fabric, no patch, no plate, no rectangle behind the letters. The wordmark reads '~WuBu~' — tilde, W, u, B, u, tilde — in every frame he faces the lens.

All other blocks hold unchanged (SUBJECTS, TIMELINE, CAMERA, AUDIO, LOAD-BEARING DETAIL, TEXT allowlist none, the exactly-two-lines corner bug, CANON, NEGATIVE, the frozen framing, the walk 2-4s / stop 6s / needle steady 9.5s, the one directed line "The gas is rising." with first sound AT 7.5s or later and complete by 8.75s)."""

CORR_B1236_VOICE = """V2 — NAMED VOICE-TIMING CORRECTION (v1 never opened his mouth for the directed line — mouth verified CLOSED at 7.5s and 8s; no harmonic voice event rendered; VOICE failed on v1):

At [8s], his mouth OPENS ONCE, ON the lens, and he speaks the single directed line "The lamp is fed." — one opening, one breath, one continuous utterance. The line's FIRST SOUND lands AT 7.5s or LATER, never before 7.5s, ever. The utterance is COMPLETE BY 8.75s — no voice event after 8.75s, ever. His mouth is fully CLOSED and motionless before 7.5s and fully CLOSED after 8.75s. Exactly ONE voice event in the entire take — the single spoken line — the ONLY voice; no second utterance, no vocalization except the one directed line. The soft oil-pour bed at 4s and the soft trim-snip bed at 6s are the ONLY other directed sounds (non-speech).

All other blocks hold unchanged (SUBJECTS, TIMELINE, CAMERA, LOAD-BEARING DETAIL, TEXT allowlist none, the exactly-two-lines corner bug, CANON, NEGATIVE, the wordmark ~WuBu~ six glyphs both tildes standalone, the frozen framing, the fill at 4s / trim at 6s / light at 7s / lit lamp + hands at sides at 9.5s)."""

def build_v2(claimed, v1file, correction):
    v1 = (slate / v1file).read_text().rstrip() + "\n"
    body = v1 + "\n---\n\n" + correction + "\n"
    fn = slate / f"fire_b{claimed}_{RUN}_v2_correction.txt"
    fn.write_text(body)
    md5 = hashlib.md5(body.encode()).hexdigest()
    print(f"{fn.name}  md5={md5}  bytes={len(body.encode())}")
    return md5

md5_1235v2 = build_v2("1235", "fire_b1235_20261018_0300_v1.txt", CORR_B1235_WORDMARK)
md5_1236v2 = build_v2("1236", "fire_b1236_20261018_0300_v1.txt", CORR_B1236_VOICE)
print("OK", md5_1235v2, md5_1236v2)
