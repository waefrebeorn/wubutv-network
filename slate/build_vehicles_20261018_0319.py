#!/usr/bin/env python3
"""Build script-built fire vehicles for the 2026-10-18 0319 commercial factory run.
Claim-time drafts per the AD-64/65/66 precedent: sponsor invented claim-time,
verb-grep TRUE zero-hit vs all tables + IDEAS_BANK (word-boundary), beat-gated,
retired-shape check clean. Fire from these vehicles verbatim
(FIRE-VEHICLE TRANSCRIPTION-SLIP datum). Production note stripped at build;
citation tokens zero by construction."""
import hashlib, pathlib, re

slate = pathlib.Path.home() / "workspace/wubutv-network/slate"
RUN = "20261018_0319"

HEADER = """10-second 16:9 commercial, 1280x720, exactly 10.0 seconds, flat hand-painted 2D cartoon grade (STYLE IS LOAD-BEARING: every surface painted, no photorealism, no photographic texture anywhere). Locked-off camera, identical framing at 0.5s and 9.5s (240-frame camera lock; no push-in, no reframe, no approach staging, never a close-up)."""

CHARACTER = """CHARACTER (identity lock): UNC — heavyset Black man, large rounded afro, mustache/goatee, BLACK hoodie. On the chest, the exact yellow/gold wordmark `~WuBu~` — six glyphs: tilde, W, u, B, u, tilde; the two u letters plain u with no dots, no diaeresis, no umlaut, never ü. Plain fabric, no other lettering. BARE FABRIC — no yellow panel, no yellow box, no yellow rectangle, no patch, no plate behind the letters, the black fabric uninterrupted around every glyph. BARE EYES, no glasses, no spectacles, no eyewear. He never reacts; deadpan throughout. (TILDE AND POSTURE LOCK: both tildes always present and fully rendered even when he bends or leans — posture never removes a tilde, never profile-turned into invisibility; his hands stay clear of the chest panel at every point; his torso never turns; his head never drops over the wordmark.)"""

BUG = """CORNER BUG (every frame): EXACTLY TWO lines of plain WHITE text, bottom-right, painted directly on the scene itself: line one `~ WuBu ~`, line two `WuBuTV` — and NOTHING beneath them. Never yellow, never gold, never boxed, never on a backing panel, never on a chip, never on a black box, never on any rectangle or plaque; the bug letters sit directly on the background scene with the scene visible around every glyph."""

AD276 = f"""AD-276 "Skived" v1 — The Skiver's Edge Leather Works.

{HEADER}

{CHARACTER}

{BUG}

SET: the leather bench — one flat leather strap with one thick square edge, one skiving knife with a plain wooden handle, one cutting mat under the strap. Exactly ONE strap, ONE knife, ONE mat, the same single props throughout. TEXT ALLOWLIST: NONE — the strap plain and unlettered, the knife handle plain wood and unlettered, the mat unlettered, the bench bare, the walls bare; any framed pictures on the walls render as wordless abstract washes with no readable letters, no signage anywhere, no readable marks of any kind. The whole set is wordless.

BEAT (10s, setup/turn/tag):
- 0-4s (setup): the strap flat on the mat, its thick square edge toward camera at 0.5s; the skiving knife lying beside it. Frame 1 is on the strap's edge (OBJECT FIRST). He stands beside the bench facing camera, mouth closed.
- 4-6s (beat): he draws the skiving knife along the strap's edge — the blade shaving a thin curled strip of leather from the edge, the curl lifting as it cuts. Knife, edge, and his hands in continuous motion across the whole 4-6s window, never a frozen take. The work stays at bench level, BELOW the chest panel; his torso never turns; his head never drops over the wordmark.
- 6-8s (turn): the edge feathered thin; he sets the knife down on the bench, stands motionless facing camera, mouth closed, hands empty at his sides.
- 8s (tag): NO-LINE — mouth closed every frame; the tagline lives in the verdict still, never rendered text.
- 9.5s (verdict): the strap's edge tapered to a paper-thin feather edge along its whole length, the curled leather shaving lying beside the strap on the mat, the knife set down, his hands empty at his sides, eyes on the lens, mouth closed.

NEGATIVE: no photorealism, no third bug line, no boxed bug, NO BLACK BOX behind the bug, NO backing panel or plaque or chip behind the bug, no spelled-out wordmark descriptions as on-screen text, no yellow or gold bug letters, no real logos, no brands, no timecode/REC/production overlays, no day stamps, no corner timecodes, no overlay graphics of any kind, the two u letters never rendered with dots or umlaut, no hand or prop occlusion of the chest wordmark at any point, no second strap, no second knife, no second shaving, no awl, no edge paint, no readable letters anywhere on set, no lettered knife handle, no open mouth at any point, no WuBu text on any background surface, no lamp.

AUDIO: native diegetic audio only, never dubbed. Quiet beds only: the knife draw ~4.5s, the knife set-down ~6.5s — all under -25 dBFS. No voiced utterance anywhere; mouth closed every frame. True peak must stay under -1 dB.

PRODUCTION NOTE: the beat reads in the feathered edge, not in text; the thick square edge at 0.5s vs the paper-thin feather taper at 9.5s is the whole commercial. Identity continuity: the strap on the mat at 0.5s is the SAME strap with the feathered edge at 9.5s; the knife beside the strap at 0.5s is the SAME knife set down at 9.5s.
"""

AD277 = f"""AD-277 "Calendered" v1 — The Iron Roll Paperworks.

{HEADER}

{CHARACTER}

{BUG}

SET: the calender room — a bench-top calender machine with two polished iron rolls and one crank handle, one matte sheet of paper, one wooden feed table before the rolls and one outfeed table behind them. Exactly ONE machine, ONE sheet, the same single props throughout. TEXT ALLOWLIST: NONE — the machine's nameplate blank with no words, the rolls bare polished iron, the sheet plain and unlettered, the tables bare, the walls bare; any framed pictures on the walls render as wordless abstract washes with no readable letters, no signage anywhere, no readable marks of any kind. The whole set is wordless.

BEAT (10s, setup/turn/tag):
- 0-4s (setup): the matte sheet flat on the feed table before the roll nip at 0.5s, its leading edge at the rolls. Frame 1 is on the sheet (OBJECT FIRST). He stands beside the machine facing camera, mouth closed.
- 4-6s (beat): he feeds the sheet between the two polished iron rolls and turns the crank — the sheet drawn through the roll nip, emerging glazed on the outfeed side. Rolls, sheet, crank, and his hands in continuous motion across the whole 4-6s window, never a frozen take. The work stays at bench level, BELOW the chest panel; his torso never turns; his head never drops over the wordmark.
- 6-8s (turn): the crank at rest; he lifts the sheet from the outfeed table and holds it to the light, the glazed sheen catching the light. He stands motionless, mouth closed, holding the sheet at two corners.
- 8s (tag): NO-LINE — mouth closed every frame; the tagline lives in the verdict still, never rendered text.
- 9.5s (verdict): the glazed sheet held up to the light with its sheen visible, the rolls still, the crank at rest, his eyes on the lens, mouth closed.

NEGATIVE: no photorealism, no third bug line, no boxed bug, NO BLACK BOX behind the bug, NO backing panel or plaque or chip behind the bug, no spelled-out wordmark descriptions as on-screen text, no yellow or gold bug letters, no real logos, no brands, no timecode/REC/production overlays, no day stamps, no corner timecodes, no overlay graphics of any kind, the two u letters never rendered with dots or umlaut, no hand or prop occlusion of the chest wordmark at any point, no second sheet, no second crank, no nameplate lettering, no readable letters anywhere on set, no open mouth at any point, no WuBu text on any background surface, no lamp.

AUDIO: native diegetic audio only, never dubbed. Quiet beds only: the crank turns ~4.5-5.5s, the sheet lift ~6.5s — all under -25 dBFS. No voiced utterance anywhere; mouth closed every frame. True peak must stay under -1 dB.

PRODUCTION NOTE: the beat reads in the sheen, not in text; the matte sheet at 0.5s vs the glazed sheet catching the light at 9.5s is the whole commercial. Identity continuity: the sheet on the feed table at 0.5s is the SAME sheet held to the light at 9.5s; the still rolls at 0.5s are the SAME rolls that drew the sheet through at 9.5s.
"""

def strip_production_note(text):
    text, n = re.subn(r"PRODUCTION NOTE: .*", "", text, flags=re.S, count=1)
    text = text.rstrip() + "\n"
    assert n == 1, "production note not stripped"
    return text

for ad, text in [("276", AD276), ("277", AD277)]:
    body = strip_production_note(text)
    body = body.rstrip() + "\n"
    assert "PRODUCTION NOTE" not in body
    fn = slate / f"fire_ad{ad}_{RUN}_v1.txt"
    fn.write_text(body)
    md5 = hashlib.md5(body.encode()).hexdigest()
    print(f"{fn.name}  md5={md5}  bytes={len(body.encode())}")
print("OK")
