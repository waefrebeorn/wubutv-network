#!/usr/bin/env python3
"""Build v2 correction vehicles for the bumper factory 1915 EDT run:
- B-1278 v2: named single-axis VOICE-TIMING correction (v1 early-onset, B-1083-v1 signature)
- B-1279 v2: named single-axis WORDMARK correction (v1 doubled trailing tilde at 9.5s, new drift class)
Verbatim v1 body preserved; correction header prepended; zero citation tokens."""
import hashlib, pathlib, re

SLATE = pathlib.Path.home() / "workspace/wubutv-network/slate"

B1278_CORR = (
    "NAMED SINGLE-AXIS CORRECTION (VOICE-TIMING): the prior take of this exact shape voiced the directed line EARLY "
    "— the mouth verified OPEN at 7.0s/7.25s with loud voice-grade audio at 6.75s/7.0s/7.25s, all before the 7.5s cutoff "
    "(the early-onset signature), while the mouth was CLOSED at 8.0s/8.25s with no voiced utterance anywhere in the 7.5-8.75s "
    "window. In THIS take the mouth MUST be fully CLOSED through 7.4s — no voice-grade sound before 7.5s, ever; the directed "
    "line \"The tack is kept.\" voiced ONCE in-window: the line's FIRST SOUND lands AT 7.5s or LATER, never before 7.5s; "
    "the mouth opens ONCE at ~8s, on the lens; the utterance COMPLETE BY 8.75s. This axis HELD or the take fails.\n\n"
)

B1279_CORR = (
    "NAMED SINGLE-AXIS CORRECTION (WORDMARK): the prior take of this exact shape rendered the hoodie wordmark's TRAILING "
    "TILDE DOUBLED at 9.5s (\"~WuBu~~\" — seven glyphs on clear black fabric, crop-zoom verified; the double-tilde form is "
    "forbidden, a new drift class alongside the dash class). In THIS take the wordmark MUST read ~WuBu~ — exactly SIX glyphs: "
    "tilde, W, u, B, u, tilde, the trailing tilde present exactly ONCE, never doubled, never as a V, never as a dash, never as "
    "a bar — in EVERY frame of the take, including the 9.5s verdict frame. This axis HELD or the take fails.\n\n"
)

for v1name, v2name, corr in [
    ("fire_b1278_20261019_1915_v1.txt", "fire_b1278_20261019_1915_v2.txt", B1278_CORR),
    ("fire_b1279_20261019_1915_v1.txt", "fire_b1279_20261019_1915_v2.txt", B1279_CORR),
]:
    v1 = (SLATE / v1name).read_text()
    v2 = corr + v1
    (SLATE / v2name).write_text(v2)
    md5 = hashlib.md5(v2.encode()).hexdigest()
    non_grammar = [b for b in set(re.findall(r"\[[^\]]{1,20}\]", v2)) if not re.match(r"^\[\d", b)]
    assert not non_grammar, f"unexpected bracket tokens in {v2name}: {non_grammar}"
    print(f"{v2name}: {len(v2)} chars, md5 {md5}")
print("v2 vehicles built")
