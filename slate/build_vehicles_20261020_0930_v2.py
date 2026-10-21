#!/usr/bin/env python3
"""Build named single-axis v2 correction vehicles for the 0930 run."""
import hashlib, sys

SLATE = "/home/hatch/workspace/wubutv-network/slate"

def load(n): return open(f"{SLATE}/fire_{n}_20261020_0930_v1.txt").read()
def save(n, text):
    out = f"{SLATE}/fire_{n}_20261020_0930_v2.txt"
    open(out, "w").write(text)
    print(f"{n} v2 md5={hashlib.md5(text.encode()).hexdigest()} bytes={len(text)}")

# ---- B-1275 v2: named VOICE-TIMING correction ----
t = load("b1275")
old_line = '[8s] his mouth opens ONCE, on the lens: "Clean hands." — one opening, one breath, one continuous utterance; the line\'s FIRST SOUND lands AT 7.5s or LATER, never before 7.5s; the utterance COMPLETE BY 8.75s.'
new_line = '[8s] his mouth opens ONCE, on the lens: "Clean hands." — one opening, one breath, one continuous utterance; his mouth stays fully CLOSED through 7.4s — no open mouth before 7.5s, ever; the line\'s FIRST SOUND lands AT 7.5s or LATER, never before 7.5s, never at 6s, never at 7s; the utterance COMPLETE BY 8.75s, the mouth fully CLOSED by 8.75s.'
assert old_line in t, "b1275 timeline anchor missing"
t = t.replace(old_line, new_line)
anchor = "no open mouth before 7.5s, no open mouth after 8.75s,"
assert anchor in t, "b1275 negative anchor missing"
t = t.replace(anchor, "no open mouth before 7.5s, no voice-grade sound before 7.5s, no open mouth after 8.75s,")
assert "no meta-text describing the bug's spelling" in t
save("b1275", t)

# ---- B-1289 v2: named TEXT correction ----
t = load("b1289")
old_subj = "SUBJECTS: the stairwell — one flight of stairs, one landing below at 0.5s; one ball in his hand at 0.5s."
new_subj = "SUBJECTS: the stairwell — one flight of stairs, one landing below at 0.5s; the walls completely BARE and unlettered — plain walls, no posters, no signs, no EXIT sign, no door placards, no lettering of any kind anywhere; one ball in his hand at 0.5s."
assert old_subj in t, "b1289 subjects anchor missing"
t = t.replace(old_subj, new_subj)
old_text = "TEXT: allowlist = the hoodie wordmark `~ WuBu ~` exactly — six glyphs (tilde, W, u, B, u, tilde), yellow/gold on bare black fabric, both tildes single, spelled WITH SPACES — and nothing else in-world; the stairs unnumbered (digits are the text risk), the walls bare."
new_text = "TEXT: allowlist = the hoodie wordmark `~ WuBu ~` exactly — six glyphs (tilde, W, u, B, u, tilde), yellow/gold on bare black fabric, both tildes single, spelled WITH SPACES — and nothing else in-world; the stairs unnumbered (digits are the text risk), the walls completely BARE — no posters, no signs, no EXIT sign, no door markings, no lettering of any kind."
assert old_text in t, "b1289 text anchor missing"
t = t.replace(old_text, new_text)
old_neg = "no floor numbers, no stair signage,"
assert old_neg in t, "b1289 negative anchor missing"
t = t.replace(old_neg, "no floor numbers, no stair signage, no posters, no signs, no EXIT sign, no wall lettering, no door placards, no letter-shaped noise,")
save("b1289", t)

# ---- B-1290 v2: named TEXT correction ----
t = load("b1290")
old_subj = "SUBJECTS: the seed cellar — one shelf of jars at 0.5s, one empty slot; one jar in the hands at 0.5s, unlabeled. Hands only — no face, no hero body in any frame."
new_subj = "SUBJECTS: the seed cellar — one shelf of jars at 0.5s with one EMPTY SLOT clearly visible; one jar in the hands at 0.5s, unlabeled; every other jar on the shelf UNLETTERED and untagged — no labels, no tags, no marks, no year tokens on any jar but the hero jar. Hands only — no face, no hero body in any frame."
assert old_subj in t, "b1290 subjects anchor missing"
t = t.replace(old_subj, new_subj)
old_4s = "[4s] ONE labeling — the hands write the year on the jar's tag — one labeling, never two; one soft pen bed at 4s (non-speech — directed sound)."
new_4s = "[4s] ONE labeling — the hands write \"1963\" on the hero jar's tag — the tag reads \"1963\", exactly four digits, glyph-exact — one labeling, never two; one soft pen bed at 4s (non-speech — directed sound)."
assert old_4s in t, "b1290 4s anchor missing"
t = t.replace(old_4s, new_4s)
old_text = "TEXT: allowlist = the jar's year token \"1963\" ONLY — glyph-exact, on the tag, nothing else; the other jars unlettered, the cellar bare."
new_text = "TEXT: allowlist = the hero jar's year token \"1963\" ONLY — exactly four digits, glyph-exact, on the hero tag, nothing else; every other jar on the shelf unlettered and untagged, the cellar bare."
assert old_text in t, "b1290 text anchor missing"
t = t.replace(old_text, new_text)
old_neg = "no second jar labeled, no second shelving, no second year token,"
assert old_neg in t, "b1290 negative anchor missing"
t = t.replace(old_neg, "no second jar labeled, no second shelving, no second year token, no \"1962\", no other year tokens, no labeled jars, no marked tags, no letter-shaped noise,")
save("b1290", t)

print("V2 BUILD OK")
