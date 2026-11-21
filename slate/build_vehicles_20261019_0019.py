#!/usr/bin/env python3
"""Build fire vehicles for the 2026-10-19 00:19 EDT commercial run: AD-301, AD-302."""
import hashlib, pathlib

SLATE = pathlib.Path("/home/hatch/workspace/wubutv-network/slate")

STYLE = ("Hand-painted 2D cartoon, thick black outlines, flat comic palette, 1970s public-access "
"broadcast, VHS chroma bleed, scanlines. STYLE IS LOAD-BEARING: painted timber, painted fabric, "
"thick black outlines on every edge \u2014 never photorealistic, never photographic shading, never camera grain. "
"MOTION IS LOAD-BEARING: this is NOT a still \u2014 the {beat} at 4s-6s MUST render as visible motion "
"and a visible state change; a take where the 0.5s and 9.5s {setup} match is a failed take.")

IDENTITY = ("The man (heavyset Black man, large rounded afro, thick mustache/goatee, BLACK hoodie "
"with the wordmark ~WuBu~ in YELLOW/GOLD letters spelled fully and exactly with tildes in every frame \u2014 "
"exactly SIX glyphs total: tilde, W, u, B, u, tilde \u2014 the six glyphs on ONE STRAIGHT HORIZONTAL BASELINE, "
"the leading tilde sitting ON the line at the left of the W at the same height as the trailing tilde, never "
"floating above the cap line, never detached; the trailing tilde present exactly ONCE, never doubled, the ~~ "
"double-tilde form forbidden, no dotted tilde, no dot-tilde, no macron, no bar, no umlaut, no diacritic on any "
"letter of the wordmark, the two u letters plain u with no dots, no diaeresis, no umlaut, never \u00fc; the two "
"tildes render fully even when he leans in \u2014 posture never removes a tilde; the hoodie bare black fabric, "
"no patch, no plate, no rectangle behind the letters; bare eyes, no glasses, no eyewear of any kind; EXACTLY "
"ONE man in every frame \u2014 no second figure, no second hero body, no background extra carrying his face). "
"He never reacts; deadpan throughout.")

BUG = ("Corner bug: EXACTLY TWO lines of plain WHITE text printed directly over the picture, no background, "
"no plaque, no panel, no shape, no outline, no white box, no white chip, no dark letters, no television shape, "
"no antennae, never red, never orange, never yellow, never gold, never pink, no words spelling corner, no word "
"bug rendered \u2014 line one \"~ WuBu ~\" with exactly one tilde on each side, never doubled, nothing before "
"the first tilde, nothing after the last tilde, the bug's line one spelled WITH SPACES \u2014 tilde, space, "
"W-u-B-u, space, tilde; line two \"WuBuTV\" in full, never \"TV\" alone; bottom-right, never at the top, never "
"at the left, every frame, fully opaque from frame 0, fixed position, never animated, identical in all 240 frames. "
"The bug is legal ONLY at the frame's bottom-right corner \u2014 name BOTH the backing (none) and the placement "
"(bottom-right corner).")

NEG_BASE = ("NEGATIVE: no dissolves, no subtitles, no watermark other than the two-line overlay, no boxed bug, "
"no chip-style bug, no dark-on-white bug, no background plate behind the bug, no words spelling corner, no word "
"bug, no VHS caption, no third line under the bug, no invented text, no dark letters, no television shape, no "
"antennae, never red, never orange, never yellow, never gold, never pink, no letter-shaped noise, no grain "
"lettering, no block lettering, {prop_lettering}, no second {prop1}, no second {prop2}, no second {prop3}, "
"no second man, no second figure, no second hero body, no quote marks, no apostrophes, no production-slate "
"overlays, no day stamps, no time stamps, no REC indicators, no corner timecodes, no overlay graphics of any kind, "
"no version tokens, no number tokens, no citation-style text, no missing tilde, no single-sided wordmark, "
"no flickering tilde, no floating tilde, no tilde above the cap line, no doubled tilde, no ~~ anywhere, "
"no dotted tilde, no dot-tilde, no dotted u, no umlaut u, no diacritic on any letter of the wordmark, the two u "
"letters plain u with no dots, no diaeresis, no umlaut, never \u00fc, no yellow plate behind the wordmark letters, "
"no dark letters forming the wordmark, no wordmark on the {prop_surfaces}, no WuBu text on any surface but the "
"hoodie and the corner bug, no voice event outside the ~8s line, no second utterance, no open mouth outside the "
"line, no photorealism, no photographic shading, no camera grain, no cloth mask, no licensed cartoon characters, "
"no franchise faces, no animal mascots, no real people, no real logos, no voiceover, no music, no stinger.")

CAMERA = ("CAMERA: the framing is FROZEN \u2014 the same locked-off medium framing in every frame from 0s to 10s, "
"no push in at any time, no pan, no cuts, no reframing, no progressive tightening; the 9.5s framing identical to "
"the 0.5s framing; the man, {props}, fully visible in every frame including the 9.5s verdict frame.")

ad301 = """## === AD-301 "SMOCKED" (The Smocking Hoop) : LINE STAGE ===

{style}

SUBJECTS: the stitching bench \u2014 one embroidery hoop (plain timber, unlettered) holding one fabric panel (natural undyed cloth, unlettered) on a workbench (bare timber, unlettered), one threaded needle (plain steel, unlettered) lying beside the hoop at 0.5s, the wall bare and unlettered behind. {identity} He stands at the bench from 0s, the needle in his hand. The smocking here is the TEXTILE trade \u2014 rows of gathering stitches worked across cloth \u2014 never a windmill, never a mill of any kind.

TIMELINE: [0s-10s] Locked off medium on the man, the hoop, the panel, the bench. OBJECT-FIRST opening: frame 1 lands on the hoop and its fabric panel. [0s-3s] the fabric panel flat and ungathered in the hoop, the threaded needle at rest in his hand \u2014 setup. [4s-6s] ONE smocking \u2014 he works rows of smocking stitches across the panel in one steady sequence, the needle passing in and out, the thread drawing the fabric into even gathers row by row \u2014 one smocking, continuous motion across 4s-6s, never a frozen take; his fingers staged ON the panel and the needle through every stitch; the stitching stays below the chest panel, arms only, chest square, torso never turns, head never drops over the wordmark. [6s-8s] the panel evenly gathered in the hoop \u2014 the gathers formed. [8s] he faces the lens deadpan, hands at his sides, and says exactly one line: "The gather holds." \u2014 the line's first mouth-synced sound lands no earlier than 7.5s, the utterance complete by 8.75s; exactly ONE mouth opening for the line, mouth closed before and after. [9.5s] the fabric panel evenly gathered in the hoop, the needle laid on the bench beside the hoop, his hands empty at his sides, him facing the lens deadpan \u2014 the gather is the verdict; stitching beds at 4s-6s (non-speech \u2014 directed sound), the needle set-down bed at ~7s (non-speech \u2014 directed sound), the ONE voice event at ~8s (the ONLY speech in the take, ever).

{camera}

AUDIO: quiet workroom tone 0s-10s; stitching beds at 4s-6s (non-speech \u2014 directed sound); the needle set-down bed at ~7s (non-speech \u2014 directed sound); exactly ONE voice event at ~8s = "The gather holds." (the ONLY vocalization in the take, ever). No music, no audience, no SFX not listed here.

LOAD-BEARING DETAIL: ONE smocking \u2014 flat ungathered panel at 0.5s, the stitching at 4-6s, the evenly gathered panel at 9.5s; the wordmark ~WuBu~ glyph-exact \u2014 six glyphs on one straight horizontal baseline, both tildes single, the two u letters plain u with no dots, no diaeresis, no umlaut \u2014 on the 0.5s and 9.5s front-facing full-res frames; exactly ONE mouth opening synced to the ONE voice event at ~8s (onset no earlier than 7.5s, complete by 8.75s), mouth closed in every other frame; at 9.5s the gathered panel in the hoop, the needle laid beside it, his hands at sides \u2014 the gather is the verdict.

SILENT-FRAME GAMBLE: a flat panel drawing itself into even gathered rows \u2014 the gathering reads with the sound off.

TEXT: allowlist = none \u2014 the hoop bare and unlettered, the fabric panel natural and unlettered, the needle plain and unlettered, the bench bare and unlettered, the wall bare and unlettered, no text anywhere in the frame. The hoop, the panel, and the needle are TEXT MAGNETS \u2014 described as bare and unlettered in SUBJECTS + TEXT + NEGATIVE. Any wall dressing renders as wordless boards, never lettering, never script (the wordless-wall clause, baked in by default).

{bug}

CANON: the man works rows of smocking stitches across the panel, lays the needle down, says the line deadpan \u2014 the gather holds. LORE \u2014 THE SMOCKING HOOP: the flat cloth becomes the gather, and the gather does not pull out.

{neg}
""".format(
    style=STYLE.format(beat="smocking", setup="panel"),
    identity=IDENTITY,
    camera=CAMERA.format(props="the hoop, the panel, and the bench"),
    bug=BUG,
    neg=NEG_BASE.format(prop_lettering="no hoop lettering, no panel lettering, no needle lettering, no bench lettering, no wall lettering",
                        prop1="hoop", prop2="fabric panel", prop3="needle",
                        prop_surfaces="hoop or the panel or the needle or the bench"),
)

ad302 = """## === AD-302 "HASPED" (The Hasp Works) : LINE STAGE ===

{style}

SUBJECTS: the hardware bench \u2014 one wooden chest (bare timber, unlettered) on a workbench (bare timber, unlettered), one hasp (plain iron, unlettered, OPEN at 0.5s) hinged to the chest's front, one staple (plain iron, unlettered) fixed below it, one loose pin (plain iron, unlettered) lying on the bench beside the chest at 0.5s, the wall bare and unlettered behind. {identity} He stands at the bench from 0s, his hand near the hasp.

TIMELINE: [0s-10s] Locked off medium on the man, the chest, the hasp, the bench. OBJECT-FIRST opening: frame 1 lands on the wooden chest and its open hasp. [0s-3s] the hasp open, hanging from its hinge, the staple bare below it, the pin lying on the bench \u2014 setup. [4s-6s] ONE fastening \u2014 he swings the hasp closed over the staple in one steady motion, seats it down, picks up the pin and drops it through the staple in one steady sequence \u2014 one fastening, continuous motion across 4s-6s, never a frozen take; his fingers staged ON the hasp and the pin through every move; the fastening stays at bench height below the chest panel, arms only, chest square, torso never turns, head never drops over the wordmark. [6s-8s] the hasp closed over the staple, the pin seated through it \u2014 the fastening formed. [8s] he faces the lens deadpan, hands at his sides, and says exactly one line: "It holds fast." \u2014 the line's first mouth-synced sound lands no earlier than 7.5s, the utterance complete by 8.75s; exactly ONE mouth opening for the line, mouth closed before and after. [9.5s] the hasp closed over the staple, the pin seated through the staple, the chest shut, his hand withdrawn, him facing the lens deadpan \u2014 the fastening is the verdict; the hasp-swing bed and the pin-drop bed at 4s-6s (non-speech \u2014 directed sound), the ONE voice event at ~8s (the ONLY speech in the take, ever).

{camera}

AUDIO: quiet workroom tone 0s-10s; the hasp-swing bed and the pin-drop bed at 4s-6s (non-speech \u2014 directed sound); exactly ONE voice event at ~8s = "It holds fast." (the ONLY vocalization in the take, ever). No music, no audience, no SFX not listed here.

LOAD-BEARING DETAIL: ONE fastening \u2014 hasp open at 0.5s, the closing and pinning at 4-6s, the hasp closed with the pin seated at 9.5s; the wordmark ~WuBu~ glyph-exact \u2014 six glyphs on one straight horizontal baseline, both tildes single, the two u letters plain u with no dots, no diaeresis, no umlaut \u2014 on the 0.5s and 9.5s front-facing full-res frames; exactly ONE mouth opening synced to the ONE voice event at ~8s (onset no earlier than 7.5s, complete by 8.75s), mouth closed in every other frame; at 9.5s the hasp closed, the pin seated, the chest shut, his hand withdrawn, hands at sides \u2014 the fastening is the verdict.

SILENT-FRAME GAMBLE: an open hasp swinging shut and a pin dropping through \u2014 the fastening reads with the sound off.

TEXT: allowlist = none \u2014 the hasp plain iron and unlettered, the staple plain and unlettered, the pin plain and unlettered, the chest bare timber and unlettered, the bench bare and unlettered, the wall bare and unlettered, no text anywhere in the frame. The hasp, the staple, the pin, and the chest are TEXT MAGNETS \u2014 described as bare and unlettered in SUBJECTS + TEXT + NEGATIVE. Any wall dressing renders as wordless boards, never lettering, never script (the wordless-wall clause, baked in by default).

{bug}

CANON: the man swings the hasp closed over the staple, drops the pin, says the line deadpan \u2014 it holds fast. LORE \u2014 THE HASP WORKS: the open chest becomes the shut chest, and the shut chest stays shut.

{neg}
""".format(
    style=STYLE.format(beat="fastening", setup="chest"),
    identity=IDENTITY,
    camera=CAMERA.format(props="the chest, the hasp, and the bench"),
    bug=BUG,
    neg=NEG_BASE.format(prop_lettering="no hasp lettering, no staple lettering, no pin lettering, no chest lettering, no bench lettering, no wall lettering",
                        prop1="hasp", prop2="staple", prop3="pin",
                        prop_surfaces="hasp or the staple or the pin or the chest"),
)

for name, text in [("fire_ad301_20261019_0019_v1.txt", ad301),
                   ("fire_ad302_20261019_0019_v1.txt", ad302)]:
    p = SLATE / name
    p.write_text(text)
    md5 = hashlib.md5(text.encode()).hexdigest()
    print(f"{name}: {len(text)} chars, md5 {md5}")
    assert "\u3010" not in text and "\u3011" not in text, "citation token leaked"
print("zero citation tokens verified")
