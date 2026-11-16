#!/usr/bin/env python3
"""Build v2 correction vehicles for AD-301 (voice-timing) and AD-302 (verdict staging)."""
import hashlib, pathlib

SLATE = pathlib.Path("/home/hatch/workspace/wubutv-network/slate")

CORR_301 = """CORRECTION (v1 was REJECTED on voice-timing \u2014 this block is first load-bearing priority and overrides any conflicting impulse): v1 rendered a VOICED event at 7.10-7.15s on a verified OPEN mouth \u2014 BEFORE the 7.5s floor \u2014 and the line's voicing ran to ~9.05s \u2014 PAST the 8.75s ceiling \u2014 as two separate voiced episodes. v2 MUST hold ALL of the following: no voice event and no mouth opening before 7.5s, ever; the mouth stays CLOSED from 0s to 7.5s; the line's first mouth-synced sound lands no earlier than 7.5s; exactly ONE mouth opening for the line, and it opens no earlier than 7.5s; the utterance is complete by 8.75s; the mouth is CLOSED from 8.75s to 10s; no second utterance, no second mouth opening, ever. Every other axis is HELD from v1: ONE smocking at 4-6s with visible motion and a visible gathered state change; the hoop, the fabric panel, and the needle are the same single props in every frame \u2014 exactly ONE hoop, ONE panel, ONE needle, never on his person except in his working hand during the 4-6s beat; flat hand-painted 2D cartoon with thick black outlines, never photorealistic, never photographic shading; the evenly gathered panel in the hoop is the 9.5s verdict, the needle laid on the bench beside the hoop, his hands empty at his sides; the wordmark ~WuBu~ glyph-exact \u2014 six glyphs on one straight horizontal baseline, both tildes single \u2014 on every front-facing frame; the corner bug EXACTLY TWO lines of plain WHITE text (\u201c~ WuBu ~\u201d over \u201cWuBuTV\u201d) bottom-right every frame; TEXT allowlist = none; the camera framing FROZEN from 0s to 10s.

"""

CORR_302 = """CORRECTION (v1 was REJECTED on verdict staging \u2014 this block is first load-bearing priority and overrides any conflicting impulse): v1 rendered the hasp hardware as a PHANTOM ON THE MAN'S HOODIE at 8s/9.5s (iron hasp plate and staple drawn on his torso below the wordmark) and parked his body IN FRONT of the chest at 9.5s, so the chest's hasp was unverifiable. v2 MUST hold ALL of the following: the hasp, the staple, and the pin exist ONLY on the wooden chest \u2014 never on his person, never on his hoodie, never on his torso, never floating, never detached from the chest; at 8s and 9.5s he faces the lens from BESIDE the chest \u2014 his body offset to the left of frame, the chest's front (the closed hasp over the staple, the seated pin) fully visible to the right of him, never behind his torso, never occluded by his body; his hands at his sides, empty, at 8s and 9.5s. Every other axis is HELD from v1: ONE fastening at 4-6s with visible motion (the hasp swung closed over the staple, the pin dropped through in one steady sequence); exactly ONE voice event at ~8s = \u201cIt holds fast.\u201d \u2014 first mouth-synced sound no earlier than 7.5s, utterance complete by 8.75s, exactly ONE mouth opening, mouth closed before and after; flat hand-painted 2D cartoon with thick black outlines, never photorealistic, never photographic shading; the wordmark ~WuBu~ glyph-exact \u2014 six glyphs on one straight horizontal baseline, both tildes single \u2014 on every front-facing frame; the corner bug EXACTLY TWO lines of plain WHITE text (\u201c~ WuBu ~\u201d over \u201cWuBuTV\u201d) bottom-right every frame; TEXT allowlist = none; the camera framing FROZEN from 0s to 10s.

"""

for num, corr in [("301", CORR_301), ("302", CORR_302)]:
    v1 = SLATE / f"fire_ad{num}_20261019_0019_v1.txt"
    text = v1.read_text()
    lines = text.split("\n")
    # Insert CORRECTION after the header line (## === ...) and the blank line
    assert lines[0].startswith("## ==="), f"unexpected header in {v1}"
    v2 = lines[0] + "\n\n" + corr + "\n".join(lines[1:]).lstrip("\n")
    out = SLATE / f"fire_ad{num}_20261019_0019_v2.txt"
    out.write_text(v2)
    md5 = hashlib.md5(v2.encode()).hexdigest()
    print(f"fire_ad{num}_20261019_0019_v2.txt: {len(v2)} chars, md5 {md5}")
    assert "\u3010" not in v2 and "\u3011" not in v2, "citation token leaked"
print("zero citation tokens verified")
