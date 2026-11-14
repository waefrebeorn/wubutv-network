#!/usr/bin/env python3
"""Build v2 correction vehicles for the 2026-10-20 11:15 EDT bumper factory run.
- B-1295 v2: named single-axis CAMERA correction (v1 denied B-168: mid-take reframe).
- B-1296 v2: named single-axis VOICE-TIMING correction (v1 denied onset ~7.0s, B-1083-v1).
Each derived from the md5-verified v1 vehicle by targeted replacement; asserts the
old string occurs exactly once; prints md5s. Zero citation tokens preserved."""
import hashlib, sys

STAMP = "20261020_1115"

def build(pool, prov, old_new_pairs):
    src = f"/home/hatch/workspace/wubutv-network/slate/fire_b{pool}_{STAMP}_v1.txt"
    v1 = open(src).read()
    v2 = v1
    for old, new in old_new_pairs:
        assert v2.count(old) == 1, f"old string not unique in {pool}: {old[:60]!r}"
        v2 = v2.replace(old, new)
    # citation-token hygiene preserved
    assert "Source:" not in v2
    import re
    assert not re.search(r"\((?:B|AD|NE|N|O|L|PA|S|M|A|MEME)-\d+", v2), "token leak"
    out = f"/home/hatch/workspace/wubutv-network/slate/fire_b{pool}_{STAMP}_v2.txt"
    open(out, "w").write(v2)
    print(f"{prov} -> B-{pool} v2: {out} md5={hashlib.md5(v2.encode()).hexdigest()}")

# B-1295 "The Marked Bay" v2: named CAMERA correction
build("1295", "B-2475", [(
    "CAMERA: FROZEN \u2014 no push, no pan, no cuts, no reframing; 9.5s framing identical to 0.5s.",
    "CAMERA: the framing is FROZEN and IDENTICAL in every frame \u2014 the same locked-off WIDE framing on the bay from 0s to 10s, the 9.5s framing identical to the 0.5s framing; absolutely no push in, no zoom, no pan, no tilt, no cuts, no reframing, no progressive tightening at any time; he stays at the cart and never walks toward the lens; the bay, the cart, and the lot hold the same screen positions in every frame from 0s to 10s."
), (
    "no photorealism, no photographic shading, no camera grain,",
    "no photorealism, no photographic shading, no camera grain, no camera move, no reframing, no cuts,"
)])

# B-1296 "The Salted Step" v2: named VOICE-TIMING correction
build("1296", "B-2477", [(
    '[8s] his mouth opens ONCE, on the lens: "First frost." \u2014 one opening, one breath, one continuous utterance; the line\'s FIRST SOUND lands AT 7.5s or LATER, never before 7.5s; the utterance COMPLETE BY 8.75s.',
    '[8s] his mouth opens ONCE, on the lens: "First frost." \u2014 one opening, one breath, one continuous utterance; the mouth stays fully CLOSED and STILL through 7.4s \u2014 no parting, no opening, no mouth movement of any kind before 7.5s, ever; the line\'s FIRST SOUND lands AT 7.5s or LATER, never before 7.5s; the utterance COMPLETE BY 8.75s \u2014 the mouth fully CLOSED by 8.75s; the mouth moves ONLY for this one utterance in the entire take.'
), (
    "no open mouth before 7.5s, no open mouth after 8.75s,",
    "no mouth movement of any kind before 7.5s, no open mouth after 8.75s, ever,"
)])
print("v2 vehicles built.")
