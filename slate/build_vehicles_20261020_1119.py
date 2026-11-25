#!/usr/bin/env python3
"""Build durable fire vehicles for the 2026-10-20 11:19 EDT commercial factory run.
AD-334 'Nielloed' + AD-335 'Dunnaged' — claim-time drafts per the AD-64/65/66 precedent.
Writes slate/fire_ad334_20261020_1119_v1.txt + slate/fire_ad335_20261020_1119_v1.txt,
prints md5s. Firing must use the md5-verified files, not this script's output."""
import hashlib, sys

STAMP = "20261020_1119"
BASE = "/home/hatch/workspace/wubutv-network/slate"

STYLE = ("Hand-painted 2D cartoon, thick black outlines, flat comic palette, 1970s public-access "
         "broadcast, VHS chroma bleed, scanlines. STYLE IS LOAD-BEARING: painted wood, painted metal, "
         "painted hide, thick black outlines on every edge \u2014 never photorealistic, never photographic "
         "shading, never camera grain. MOTION IS LOAD-BEARING: this is NOT a still \u2014 the {beat_noun} "
         "at 4s-6s MUST render as visible motion and a visible state change; a take where the 0.5s and "
         "9.5s {setting} match is a failed take.")

MAN = ("The man (heavyset Black man, large rounded afro, thick mustache/goatee, BLACK hoodie with the "
       "wordmark ~WuBu~ in YELLOW/GOLD letters spelled fully and exactly with tildes in every frame \u2014 "
       "exactly SIX glyphs total: tilde, W, u, B, u, tilde \u2014 the six glyphs on ONE STRAIGHT HORIZONTAL "
       "BASELINE, the leading tilde sitting ON the line at the left of the W at the same height as the "
       "trailing tilde, never floating above the cap line, never detached; the trailing tilde present "
       "exactly ONCE, never doubled, the ~~ double-tilde form forbidden, no dotted tilde, no dot-tilde, "
       "no macron, no bar, no umlaut, no diacritic on any letter of the wordmark, the two u letters plain "
       "u with no dots, no diaeresis, no umlaut, never \u00fc; the six wordmark glyphs sit DIRECTLY on the bare "
       "black fabric \u2014 no stroke, bar, line, stripe, plate, plaque, or graphic of any kind beneath or "
       "behind the letters, in any frame; the bare black fabric runs uninterrupted directly under the ~WuBu~ "
       "glyphs, nothing sits between the letters and the fabric, nothing underlines them; the hoodie bare "
       "black fabric, no patch, no plate, no rectangle behind the letters; THE WORDMARK IS ONLY THE SIX "
       "GLYPHS \u2014 beneath the six glyphs there is nothing but the bare black fabric itself, unbroken; no "
       "line, no bar, no stripe, no plate, no plaque, no patch, no underline of any kind sits beneath, "
       "behind, or touching any letter; a bar under the wordmark is a failed take; bare eyes, no glasses, "
       "no eyewear of any kind; EXACTLY ONE man in every frame \u2014 no second figure, no second hero body, "
       "no background extra carrying his face). He never reacts; deadpan throughout.")

BUG = ("Corner bug: EXACTLY TWO lines of plain WHITE text printed directly over the picture, no background, "
       "no plaque, no panel, no shape, no outline, no white box, no white chip, no dark letters, no "
       "television shape, no antennae, never red, never orange, never yellow, never gold, never pink, no "
       "words spelling corner, no word bug rendered, no meta-text describing the bug's spelling, no "
       "spelling-out of the tilde instruction as words, the doubled ~~ form forbidden in the bug, no third "
       "line under the bug \u2014 line one \"~ WuBu ~\" with exactly one tilde on each side, never doubled, "
       "nothing before the first tilde, nothing after the last tilde, the bug's line one spelled WITH SPACES "
       "\u2014 tilde, space, W-u-B-u, space, tilde; line two \"WuBuTV\" in full, never \"TV\" alone; bottom-right, "
       "never at the top, never at the left, every frame, fully opaque from frame 0, fixed position, never "
       "animated, identical in all 240 frames. The bug is legal ONLY at the frame's bottom-right corner \u2014 "
       "name BOTH the backing (none) and the placement (bottom-right corner).")

VOICE = ("[8s] he faces the lens deadpan, hands at his sides, and says exactly one line: \"{line}\" \u2014 "
         "the line's first mouth-synced sound lands no earlier than 7.5s, the utterance COMPLETE BY 8.75s \u2014 "
         "mouth fully CLOSED by 8.75s and STAYS closed through 10s; exactly ONE mouth opening for the line, "
         "mouth closed before and after; NO voice-grade sound after 8.75s, ever.")

CAMERA = ("CAMERA: the framing is FROZEN \u2014 the same locked-off medium framing in every frame from 0s to "
          "10s, no push in at any time, no pan, no cuts, no reframing, no progressive tightening; the 9.5s "
          "framing identical to the 0.5s framing; the man, the {hero_list} fully visible in every frame "
          "including the 9.5s verdict frame.")

ADS = [
    {
        "num": "AD-334", "title": "NIELLOED", "sponsor": "The Niello Bench",
        "line": "Black in the cut.", "beat_noun": "nielloing", "setting": "bench",
        "hero_list": "bench, and the silver piece",
        "prod_note": ("FRESH NUMBER. Claim-time draft per the AD-64/65/66 precedent. Hero verb "
            "\"niello\"/\"nielloed\" TRUE zero-hit repo-wide (word-boundary, case-insensitive md+txt sweep "
            "over slate/ideas/assembly/network/notes: 0 matches); title \"Nielloed\" zero-hit; sponsor "
            "\"The Niello Bench\" invented claim-time, zero-hit; directed line \"Black in the cut.\" zero-hit "
            "repo-wide. Title-read clean (felloed/waulked precedent). HOMONYM GUARD (standing rule): niello "
            "= the black sulfur-alloy paste rubbed into engraved silver \u2014 no other sense named or rendered. "
            "Beat-gated per B-625: zero inlay/engraving/silver commercial beats in the 333-row shipped ledger; "
            "no retired niello shape. Fire-time TILDE AND POSTURE LOCK + anti-umlaut clause + "
            "bare-fabric-ground clause + AD-315 v3 anti-underline-bar clause baked pre-emptively (standing "
            "rule); B-1275 BUG anti-leak clause baked (\"no meta-text describing the bug's spelling\"); AD-330 "
            "BUG doubled-tilde clause baked (\"the doubled ~~ form forbidden in the bug\"). Discards at claim: "
            "\"inlaid\" (known word), \"engraved\" (engrave-family), \"damascened\" (long), \"champleved\" (long)."),
        "subjects": ("SUBJECTS: the niello bench \u2014 one silver piece (a plain silver disc, its face engraved "
            "with one simple line design, the engraved lines EMPTY and bright at 0.5s, the silver unlettered); "
            "one niello pad (a small felt pad charged with black niello paste, unlettered); one bench (a plain "
            "wooden workbench, unlettered). This is NIELLOING \u2014 rubbing the black niello paste into the "
            "engraved lines and wiping the surface clean so the black design stands in the silver: one rubbing, "
            "one wipe, the black lines standing \u2014 never ink, never paint, never enamel, never a printed "
            "decal, never a second piece, never a second pad. The bench, the piece, the pad exist ONLY at the "
            "bench \u2014 never on his person, never on his hoodie, never on his torso, never floating. "
            + MAN + " He stands square to the lens at the bench from 0s, the piece before him, the pad at hand."),
        "timeline": ("TIMELINE: [0s-10s] Locked off medium on the man, the bench, the silver piece. OBJECT-FIRST "
            "opening: frame 1 lands on the silver piece with its empty engraved lines before the man. [0s-3s] the "
            "piece engraved-but-unfilled, the black lines absent, the charged pad beside it \u2014 setup. [4s-6s] "
            "ONE nielloing \u2014 he rubs the black niello paste into the engraved lines with the pad in one "
            "continuous rubbing, then wipes the surface clean with one pass, the black design standing crisp in "
            "the silver, never a frozen take; his hands staged at the bench through the sequence; the work stays "
            "at chest height and below, arms only, chest square, torso never turns, head never drops over the "
            "wordmark. [6s-8s] the piece with its black design standing, his hands at his sides. "
            + VOICE.format(line="Black in the cut.") + " [9.5s] the piece before him with the black design crisp "
            "in the silver, his hands empty at his sides, him facing the lens deadpan, mouth CLOSED \u2014 the "
            "inlaid black lines are the verdict; the nielloing beds at 4s-6s (soft pad rubs, the wipe pass, "
            "non-speech \u2014 directed sound), the ONE voice event at ~8s (the ONLY speech in the take, ever)."),
        "audio": ("AUDIO: quiet room tone 0s-10s; the nielloing beds at 4s-6s (soft pad rubs, the wipe pass, "
            "non-speech \u2014 directed sound); exactly ONE voice event at ~8s = \"Black in the cut.\" (the ONLY "
            "vocalization in the take, ever). No music, no audience, no SFX not listed here."),
        "loadbearing": ("LOAD-BEARING DETAIL: the engraved lines empty and bright at 0.5s; the nielloing in motion "
            "at 4-6s (the black paste rubbed into the lines, the surface wiped clean, the black design standing); "
            "the black design crisp in the silver at 9.5s; the wordmark ~WuBu~ glyph-exact \u2014 six glyphs on one "
            "straight horizontal baseline, both tildes single, the two u letters plain u with no dots, no diaeresis, "
            "no umlaut, NO underline bar beneath the letters, NO stripe or plate behind them, the six glyphs "
            "sitting DIRECTLY on the bare black fabric with bare fabric between each glyph and nothing else \u2014 "
            "on the 0.5s and 9.5s front-facing full-res frames; exactly ONE mouth opening synced to the ONE voice "
            "event at ~8s (onset no earlier than 7.5s, complete by 8.75s, mouth fully closed by 8.75s and staying "
            "closed), mouth closed in every other frame; at 9.5s the black-lined piece \u2014 the inlaid black lines "
            "are the verdict."),
        "gamble": ("SILENT-FRAME GAMBLE: empty engraved lines at 0.5s, black design standing at 9.5s \u2014 the "
            "nielloing reads with the sound off."),
        "text": ("TEXT: allowlist = none \u2014 the silver plain and unlettered, the pad unlettered, the bench "
            "unlettered, the walls bare and unlettered. The silver piece is a TEXT MAGNET \u2014 described as plain "
            "and unlettered in SUBJECTS + TEXT + NEGATIVE. Any bench dressing renders as wordless wood and metal, "
            "never lettering, never script (the wordless-wood clause, baked in by default)."),
        "canon": ("CANON: the man rubs the black into the cuts, wipes the face clean, says the line deadpan \u2014 "
            "black in the cut. LORE \u2014 THE NIELLO BENCH: the dark stays where the cut tells it."),
        "negative_extra": ("no ink, no paint, no enamel, no printed decal, no second silver piece, no second pad, "
            "no lettering on the silver, no numerals on the silver, no hallmarks, "),
    },
    {
        "num": "AD-335", "title": "DUNNAGED", "sponsor": "The Dunnage Bed",
        "line": "Bedded, not bruised.", "beat_noun": "dunnaging", "setting": "hold",
        "hero_list": "hold floor, the crate, and the dunnage timbers",
        "prod_note": ("FRESH NUMBER. Claim-time draft per the AD-64/65/66 precedent. Hero verb "
            "\"dunnage\"/\"dunnaged\" TRUE zero-hit repo-wide (word-boundary, case-insensitive md+txt sweep "
            "over slate/ideas/assembly/network/notes: 0 matches); title \"Dunnaged\" zero-hit; sponsor "
            "\"The Dunnage Bed\" invented claim-time, zero-hit; directed line \"Bedded, not bruised.\" zero-hit "
            "repo-wide. Title-read clean (felloed/waulked precedent). HOMONYM GUARD (standing rule): dunnage = "
            "rough protective bedding/bracing timbers laid under and around cargo in the hold \u2014 never packing "
            "peanuts, never filler, never straw. Beat-gated per B-625 vs AD-172 \"Lashed Down\" (rope thrown over "
            "a tarped load, verdict = taut lashed rope \u2014 flagged overlap per the B-903 verb-difference "
            "precedent), vs AD-66 \"Covered for the Night\" (drape tarp over freight), vs AD-195 \"Stowed\" (stow "
            "parcels): the DUNNAGE TIMBERS are the hero \u2014 laying/bedding vs throwing/securing vs draping vs "
            "stowing; the verdict is the crate riding braced on its dunnage bed. Retired-shape check clean. "
            "Fire-time TILDE AND POSTURE LOCK + anti-umlaut clause + bare-fabric-ground clause + AD-315 v3 "
            "anti-underline-bar clause baked pre-emptively (standing rule); B-1275 BUG anti-leak clause baked "
            "(\"no meta-text describing the bug's spelling\"); AD-330 BUG doubled-tilde clause baked (\"the doubled "
            "~~ form forbidden in the bug\"). Discards at claim: \"braced\" (brace-family), \"shored\" (known phrase), "
            "\"cribbed\" (reads as cheated), \"stowed\" (AD-195 shipped), \"lashed\" (AD-172 shipped)."),
        "subjects": ("SUBJECTS: the hold \u2014 one wooden crate (a plain wooden shipping crate, unlettered, sitting "
            "bare on the hold planks at 0.5s); dunnage timbers (six rough plain wooden timbers, unlettered, stacked "
            "beside the crate at 0.5s \u2014 THE HERO OBJECT); the hold floor (bare wooden planks, unlettered). This "
            "is DUNNAGING \u2014 laying the rough timbers as a protective bed under the crate and bracing them "
            "around its sides so the cargo never touches the hull: one laying, the crate settled onto its timber "
            "bed, the sides braced \u2014 never packing peanuts, never filler, never straw, never a pallet jack, "
            "never a second crate. The timbers, the crate, the planks exist ONLY in the hold \u2014 never on his "
            "person, never on his hoodie, never on his torso, never floating. "
            + MAN + " He stands square to the lens in the hold from 0s, the crate before him, the timbers at hand."),
        "timeline": ("TIMELINE: [0s-10s] Locked off medium on the man, the hold floor, the crate, the timbers. "
            "OBJECT-FIRST opening: frame 1 lands on the bare hold planks and the unprotected crate before the man. "
            "[0s-3s] the crate sitting bare on the planks, the six dunnage timbers stacked beside it \u2014 setup. "
            "[4s-6s] ONE dunnaging \u2014 he lays the timbers as a bed on the planks, tips the crate onto its timber "
            "bed, and braces timbers around its sides, the crate settling onto the dunnage, never a frozen take; "
            "his hands staged in the hold through the sequence; the work stays at waist height and below, arms only, "
            "chest square, torso never turns, head never drops over the wordmark. [6s-8s] the crate riding on its "
            "dunnage bed, braced all around, his hands at his sides. "
            + VOICE.format(line="Bedded, not bruised.") + " [9.5s] the crate on its timber bed, braced all around, "
            "his hands empty at his sides, him facing the lens deadpan, mouth CLOSED \u2014 the bedded crate is the "
            "verdict; the dunnaging beds at 4s-6s (timber knocks, the crate settle, non-speech \u2014 directed sound), "
            "the ONE voice event at ~8s (the ONLY speech in the take, ever)."),
        "audio": ("AUDIO: quiet room tone 0s-10s; the dunnaging beds at 4s-6s (timber knocks, the crate settle, "
            "non-speech \u2014 directed sound); exactly ONE voice event at ~8s = \"Bedded, not bruised.\" (the ONLY "
            "vocalization in the take, ever). No music, no audience, no SFX not listed here."),
        "loadbearing": ("LOAD-BEARING DETAIL: the crate bare on the planks with six timbers stacked beside it at "
            "0.5s; the dunnaging in motion at 4-6s (the timbers laid as a bed, the crate tipped onto it, the sides "
            "braced); the crate riding on its dunnage bed, braced all around, at 9.5s; the wordmark ~WuBu~ "
            "glyph-exact \u2014 six glyphs on one straight horizontal baseline, both tildes single, the two u letters "
            "plain u with no dots, no diaeresis, no umlaut, NO underline bar beneath the letters, NO stripe or plate "
            "behind them, the six glyphs sitting DIRECTLY on the bare black fabric with bare fabric between each "
            "glyph and nothing else \u2014 on the 0.5s and 9.5s front-facing full-res frames; exactly ONE mouth "
            "opening synced to the ONE voice event at ~8s (onset no earlier than 7.5s, complete by 8.75s, mouth "
            "fully closed by 8.75s and staying closed), mouth closed in every other frame; at 9.5s the bedded crate "
            "\u2014 the bedded crate is the verdict."),
        "gamble": ("SILENT-FRAME GAMBLE: bare crate on bare planks at 0.5s, crate riding its timber bed at 9.5s \u2014 "
            "the dunnaging reads with the sound off."),
        "text": ("TEXT: allowlist = none \u2014 the timbers plain wood and unlettered, the crate unlettered, the hold "
            "planks and walls bare and unlettered. The crate is a TEXT MAGNET \u2014 described as plain and unlettered "
            "in SUBJECTS + TEXT + NEGATIVE. Any hold dressing renders as wordless wood, never lettering, never "
            "script, never stencils (the wordless-wood clause, baked in by default)."),
        "canon": ("CANON: the man lays the timber bed, settles the crate onto it, braces the sides, says the line "
            "deadpan \u2014 bedded, not bruised. LORE \u2014 THE DUNNAGE BED: the cargo never touches the hull."),
        "negative_extra": ("no packing peanuts, no filler, no straw, no excelsior, no pallet jack, no forklift, "
            "no second crate, no stencils on the crate, no shipping labels, no lettering on the timbers, "),
    },
]

NEG_TAIL = ("NEGATIVE: no dissolves, no subtitles, no watermark other than the two-line overlay, no boxed bug, "
    "no chip-style bug, no dark-on-white bug, no background plate behind the bug, no words spelling corner, "
    "no word bug, no meta-text describing the bug's spelling, no spelling-out of the tilde instruction as words, "
    "no ~~ anywhere in the bug, no VHS caption, no third line under the bug, no invented text, no dark letters, "
    "no television shape, no antennae, never red, never orange, never yellow, never gold, never pink, "
    "no letter-shaped noise, no block lettering, {extra}"
    "no quote marks, no apostrophes, no production-slate overlays, no day stamps, no time stamps, no REC "
    "indicators, no corner timecodes, no overlay graphics of any kind, no version tokens, no number tokens, "
    "no citation-style text, no missing tilde, no single-sided wordmark, no flickering tilde, no floating tilde, "
    "no tilde above the cap line, no doubled tilde, no ~~ anywhere, no dotted tilde, no dot-tilde, no dotted u, "
    "no umlaut u, no diacritic on any letter of the wordmark, the two u letters plain u with no dots, no diaeresis, "
    "no umlaut, never \u00fc, no yellow plate behind the wordmark letters, no solid gold underline bar under the "
    "wordmark letters, no bar beneath the wordmark, no graphic under the wordmark letters, no dark letters forming "
    "the wordmark, no wordmark on the bench or the tools or the walls, no WuBu text on any surface but the hoodie "
    "and the corner bug, no voice event outside the ~8s line, no second utterance, no open mouth outside the line, "
    "no open mouth after 8.75s, no photorealism, no photographic shading, no camera grain, no cloth mask, "
    "no licensed cartoon characters, no franchise faces, no animal mascots, no real people, no real logos, "
    "no voiceover, no music, no stinger.")

for ad in ADS:
    num, title, sponsor = ad["num"], ad["title"], ad["sponsor"]
    sections = [
        f'## === {num} "{title}" ({sponsor}) : v1 ===',
        "",
        "Production note: " + ad["prod_note"],
        "",
        "---",
        "",
        STYLE.format(beat_noun=ad["beat_noun"], setting=ad["setting"]),
        "",
        "---",
        "",
        ad["subjects"],
        "",
        "---",
        "",
        ad["timeline"],
        "",
        "---",
        "",
        CAMERA.format(hero_list=ad["hero_list"]),
        "",
        "---",
        "",
        ad["audio"],
        "",
        "---",
        "",
        ad["loadbearing"],
        "",
        "---",
        "",
        ad["gamble"],
        "",
        "---",
        "",
        ad["text"],
        "",
        "---",
        "",
        BUG,
        "",
        "---",
        "",
        ad["canon"],
        "",
        "---",
        "",
        NEG_TAIL.format(extra=ad["negative_extra"]),
    ]
    vehicle = "\n".join(sections)
    # sanity checks
    assert "NEGATIVE:" in vehicle
    assert vehicle.rstrip().endswith("no stinger.")
    assert "Source:" not in vehicle
    assert ad["line"] in vehicle
    assert "~WuBu~" in vehicle
    out = f"{BASE}/fire_{num[3:].lower()}_{STAMP}_v1.txt".replace("ad", "ad", 1)
    out = f"{BASE}/fire_ad{num[3:]}_" + STAMP + "_v1.txt"
    open(out, "w").write(vehicle)
    md5 = hashlib.md5(vehicle.encode()).hexdigest()
    print(f"{num} '{title}' -> {out} md5={md5} bytes={len(vehicle)}")
