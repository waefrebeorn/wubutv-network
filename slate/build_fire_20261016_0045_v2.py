#!/usr/bin/env python3
"""Build v2 re-fire prompts for the 00:45 run: B-1022 v2, B-1023 v2."""
import pathlib

slate_dir = pathlib.Path.home() / "workspace/wubutv-network/slate"

# ---- B-1022 v2: named two-axis CORRECTION (voice + count)
v1_1022 = (slate_dir / "fire_b1022_20261016_0045.txt").read_text()
corr_1022 = (
    "\n\nCORRECTION — the v1 fire rendered two named failures; this re-fire corrects both, "
    "named verbatim. (1) VOICE: v1 rendered undrafted voice-grade speech-band events at "
    "7.0-7.5s (peaking -15.94 dB) with no directed sound before 7.5s, rendered the directed "
    "8s line \"Clear.\" weak at -17.54 dB, and rendered hot undrafted voice-grade events at "
    "9.0-9.25s (peaking -6.61 dB) after the cutoff. v2: the line \"Clear.\" is LOUD AND "
    "VISIBLE at 8s — UNC's mouth visibly OPEN at 8s, exactly ONE mouth opening, one audible "
    "voice event 8.0-8.5s for \"Clear.\", the take's loudest voice event; the ONLY voice in "
    "the take; no voice event and no mouth opening before 7.5s, ever; no voice event and no "
    "mouth opening after 8.75s, ever. (2) COUNT: v1 rendered TWO leaves on the grate at "
    "0.5s against the load-bearing \"exactly one grate, one leaf, one clearing, never two\". "
    "v2: exactly ONE leaf lying on the grate at 0.5s — one leaf, one clearing, never two; "
    "the leaf in his hand at 5s is that same one leaf; the grate bare at 9.5s.\n"
)
v2_1022 = v1_1022.rstrip() + "\n" + corr_1022
assert "TWO leaves" in v2_1022 and "LOUD AND VISIBLE" in v2_1022
(slate_dir / "fire_b1022_20261016_0045_v2.txt").write_text(v2_1022)
print(f"wrote fire_b1022_20261016_0045_v2.txt: {len(v2_1022)} chars")

# ---- B-1023 v2: named three-axis CORRECTION (style + voice + text), B-997 form
v1_1023 = (slate_dir / "fire_b1023_20261016_0045.txt").read_text()
corr_1023 = (
    "\n\nCORRECTION — the v1 fire rendered three named failures; this re-fire corrects all "
    "three, named verbatim. (1) STYLE: v1 rendered photorealistic skin shading, photographic "
    "water reflections, and realistic wood grain with no black outlines — B-981 class against "
    "the explicit STYLE IS LOAD-BEARING lock. v2: STYLE IS LOAD-BEARING — painted skin, "
    "painted fabric, painted wood, painted water, painted stone, thick black outlines on "
    "every edge, flat comic palette — never photorealistic, never photographic shading, "
    "never camera grain; hand-painted 2D cartoon throughout, every frame. (2) VOICE: v1 "
    "rendered undrafted voice-grade speech-band events at 6.75-7.0s (peaking -12.47 dB) with "
    "no directed sound before 7.5s, and voice continuing past the cutoff to 9.25s (-15.33 "
    "dB). v2: the line \"The tide is due.\" is LOUD AND VISIBLE at 8s — UNC's mouth visibly "
    "OPEN at 8s, exactly ONE mouth opening, one audible voice event 8.0-8.5s, the take's "
    "loudest voice event; the ONLY voice in the take; no voice event and no mouth opening "
    "before 7.5s, ever; no voice event and no mouth opening after 8.75s, ever. (3) TEXT: v1 "
    "rendered letter-formed building signs in the background against TEXT allowlist NONE. "
    "v2: the background buildings are bare and unlettered — no signs, no lettering, no "
    "letter-forms anywhere in the frame; the board blank and unlettered; the post bare; the "
    "pier bare; no text anywhere except the hoodie wordmark and the two-line corner bug.\n"
)
v2_1023 = v1_1023.rstrip() + "\n" + corr_1023
assert "B-981 class" in v2_1023 and "LOUD AND VISIBLE" in v2_1023 and "letter-formed" in v2_1023
(slate_dir / "fire_b1023_20261016_0045_v2.txt").write_text(v2_1023)
print(f"wrote fire_b1023_20261016_0045_v2.txt: {len(v2_1023)} chars")

for name, needles in [
    ("fire_b1022_20261016_0045_v2.txt",
     ["claimed as B-1022", "CORRECTION — the v1 fire", "TWO leaves", "after 8.75s, ever",
      "LORE — THE CLEARED GRATE:"]),
    ("fire_b1023_20261016_0045_v2.txt",
     ["claimed as B-1023", "CORRECTION — the v1 fire", "B-981 class", "after 8.75s, ever",
      "LORE — THE TIDE TABLE:"]),
]:
    txt = (slate_dir / name).read_text()
    for n in needles:
        assert n in txt, f"{name}: missing {n!r}"
    print(f"verified {name}")
print("BUILD OK")
