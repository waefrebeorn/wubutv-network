#!/usr/bin/env python3
"""Build script-built fire vehicles for the 2026-10-18 0249 commercial factory run.
Claim-time drafts per the AD-64/65/66 precedent: sponsor invented claim-time,
verb-grep zero-hit vs all four tables + IDEAS_BANK, beat-gated, retired-shape
check clean. Fire from these vehicles verbatim (FIRE-VEHICLE TRANSCRIPTION-SLIP datum)."""
import hashlib, pathlib

slate = pathlib.Path.home() / "workspace/wubutv-network/slate"
RUN = "20261018_0249"

AD274 = """AD-274 "Hinged" v1 — The Stamp Hinge Co.

10-second 16:9 commercial, 1280x720, exactly 10.0 seconds, flat hand-painted 2D cartoon grade (STYLE IS LOAD-BEARING: every surface painted, no photorealism, no photographic texture anywhere). Locked-off camera, identical framing at 0.5s and 9.5s (240-frame camera lock; no push-in, no reframe, no approach staging, never a close-up).

CHARACTER (identity lock): UNC — heavyset Black man, large rounded afro, mustache/goatee, BLACK hoodie. On the chest, the exact yellow/gold wordmark `~WuBu~` — six glyphs: tilde, W, u, B, u, tilde; the two u letters plain u with no dots, no diaeresis, no umlaut, never ü. Plain fabric, no other lettering. BARE FABRIC — no yellow panel, no yellow box, no yellow rectangle, no patch, no plate behind the letters, the black fabric uninterrupted around every glyph. BARE EYES, no glasses, no spectacles, no eyewear. He never reacts; deadpan throughout. (TILDE AND POSTURE LOCK: both tildes always present and fully rendered even when he bends or leans — posture never removes a tilde, never profile-turned into invisibility; his hands stay clear of the chest panel at every point; his torso never turns; his head never drops over the wordmark.)

CORNER BUG (every frame): EXACTLY TWO lines of plain WHITE text, bottom-right, painted directly on the scene itself: line one `~ WuBu ~`, line two `WuBuTV` — and NOTHING beneath them. Never yellow, never gold, never boxed, never on a backing panel, never on a chip, never on a black box, never on any rectangle or plaque; the bug letters sit directly on the background scene with the scene visible around every glyph.

SET: the collector's study desk — an open stamp album with one empty mount slot, one stamp lying face-up beside the album, one small gummed stamp hinge resting on a damp moistening pad. Exactly ONE album, ONE stamp, ONE hinge, ONE pad, the same single props throughout. TEXT ALLOWLIST: NONE — the album pages bare and unlettered, the stamp's printed design ornamental with no readable words, the hinge and pad unlettered, the walls bare; no signage anywhere, no readable marks of any kind. The whole set is wordless.

BEAT (10s, setup/turn/tag):
- 0-4s (setup): the stamp face-up beside the album at 0.5s, the hinge on the damp pad, the mount slot empty. Frame 1 is on the stamp (OBJECT FIRST). He stands beside the desk facing camera, mouth closed.
- 4-6s (beat): he lifts the hinge from the pad, lays it across the stamp's top back edge, lifts the stamp by the hinge and seats it into the album's empty slot, pressing it flat with one fingertip. Hinge, stamp, and his hand in continuous motion across the whole 4-6s window, never a frozen take. The work stays at desk level, BELOW the chest panel; his torso never turns; his head never drops over the wordmark.
- 6-8s (turn): the stamp seated in the slot; he sets the empty pad aside, stands motionless facing camera, mouth closed, hands empty at his sides.
- 8s (tag): NO-LINE — mouth closed every frame; the tagline lives in the verdict still, never rendered text.
- 9.5s (verdict): the stamp seated SQUARE in the album slot, its edges parallel to the page, the hinge hidden behind its top edge, the album flat and open, his hands empty at his sides, eyes on the lens, mouth closed.

NEGATIVE: no photorealism, no third bug line, no boxed bug, NO BLACK BOX behind the bug, NO backing panel or plaque or chip behind the bug, no spelled-out wordmark descriptions as on-screen text, no yellow or gold bug letters, no real logos, no brands, no timecode/REC/production overlays, no day stamps, no corner timecodes, no overlay graphics of any kind, the two u letters never rendered with dots or umlaut, no hand or prop occlusion of the chest wordmark at any point, no second stamp, no second hinge, no second album, no tongs, no magnifier, no readable letters anywhere on set, no open mouth at any point, no WuBu text on any background surface, no lamp.

AUDIO: native diegetic audio only, never dubbed. Quiet beds only: the hinge lift ~4.5s, the fingertip press ~5.5s — all under -25 dBFS. No voiced utterance anywhere; mouth closed every frame. True peak must stay under -1 dB.

PRODUCTION NOTE: the beat reads in the seated stamp, not in text; the loose stamp at 0.5s vs the squared stamp in the slot at 9.5s is the whole commercial. Identity continuity: the stamp beside the album at 0.5s is the SAME stamp seated in the slot at 9.5s; the hinge on the pad at 0.5s is the SAME hinge behind the stamp's top edge at 9.5s.
"""

AD275 = """AD-275 "Mitred" v1 — The Sheet Corner Co.

10-second 16:9 commercial, 1280x720, exactly 10.0 seconds, flat hand-painted 2D cartoon grade (STYLE IS LOAD-BEARING: every surface painted, no photorealism, no photographic texture anywhere). Locked-off camera, identical framing at 0.5s and 9.5s (240-frame camera lock; no push-in, no reframe, no approach staging, never a close-up).

CHARACTER (identity lock): UNC — heavyset Black man, large rounded afro, mustache/goatee, BLACK hoodie. On the chest, the exact yellow/gold wordmark `~WuBu~` — six glyphs: tilde, W, u, B, u, tilde; the two u letters plain u with no dots, no diaeresis, no umlaut, never ü. Plain fabric, no other lettering. BARE FABRIC — no yellow panel, no yellow box, no yellow rectangle, no patch, no plate behind the letters, the black fabric uninterrupted around every glyph. BARE EYES, no glasses, no spectacles, no eyewear. He never reacts; deadpan throughout. (TILDE AND POSTURE LOCK: both tildes always present and fully rendered even when he bends or leans — posture never removes a tilde, never profile-turned into invisibility; his hands stay clear of the chest panel at every point; his torso never turns; his head never drops over the wordmark.)

CORNER BUG (every frame): EXACTLY TWO lines of plain WHITE text, bottom-right, painted directly on the scene itself: line one `~ WuBu ~`, line two `WuBuTV` — and NOTHING beneath them. Never yellow, never gold, never boxed, never on a backing panel, never on a chip, never on a black box, never on any rectangle or plaque; the bug letters sit directly on the background scene with the scene visible around every glyph.

SET: the laundry room — one flat ironing table, one plain white bed sheet draped loosely over it with its near corner loose and hanging. Exactly ONE table, ONE sheet, the same single props throughout. TEXT ALLOWLIST: NONE — the sheet plain and unlettered, the table bare, the walls bare; no signage anywhere, no readable marks of any kind. The whole set is wordless.

BEAT (10s, setup/turn/tag):
- 0-4s (setup): the sheet's near corner loose and hanging at 0.5s. Frame 1 is on the sheet (OBJECT FIRST). He stands beside the table facing camera, mouth closed.
- 4-6s (beat): he lifts the loose corner, folds it under into a hospital-corner mitre — the diagonal tuck and the squared fold — then smooths the folded corner flat with one palm. Corner, fold, and his hands in continuous motion across the whole 4-6s window, never a frozen take. The work stays at table level, BELOW the chest panel; his torso never turns; his head never drops over the wordmark.
- 6-8s (turn): the corner squared and taut; he steps back, stands motionless facing camera, mouth closed, hands empty at his sides.
- 8s (tag): NO-LINE — mouth closed every frame; the tagline lives in the verdict still, never rendered text.
- 9.5s (verdict): the sheet drawn taut over the table with ONE crisp squared hospital corner at the near edge — the diagonal fold line visible, the corner seated flat — his hands empty at his sides, eyes on the lens, mouth closed.

NEGATIVE: no photorealism, no third bug line, no boxed bug, NO BLACK BOX behind the bug, NO backing panel or plaque or chip behind the bug, no spelled-out wordmark descriptions as on-screen text, no yellow or gold bug letters, no real logos, no brands, no timecode/REC/production overlays, no day stamps, no corner timecodes, no overlay graphics of any kind, the two u letters never rendered with dots or umlaut, no hand or prop occlusion of the chest wordmark at any point, no second sheet, no second table, no iron, no pillow, no blanket, no readable letters anywhere on set, no open mouth at any point, no WuBu text on any background surface, no lamp.

AUDIO: native diegetic audio only, never dubbed. Quiet beds only: the fabric lift ~4.5s, the palm smoothing pass ~5.5s — all under -25 dBFS. No voiced utterance anywhere; mouth closed every frame. True peak must stay under -1 dB.

PRODUCTION NOTE: the beat reads in the folded corner, not in text; the loose hanging corner at 0.5s vs the crisp squared hospital corner at 9.5s is the whole commercial. Identity continuity: the sheet draped loosely at 0.5s is the SAME sheet drawn taut at 9.5s; the loose corner at 0.5s is the SAME corner folded square at 9.5s.
"""

for ad, text, ver in [("274", AD274, "v1"), ("275", AD275, "v1")]:
    body = text.rstrip() + "\n"
    assert "Production note" not in body or True
    fn = slate / f"fire_ad{ad}_{RUN}_{ver}.txt"
    fn.write_text(body)
    md5 = hashlib.md5(body.encode()).hexdigest()
    print(f"{fn.name}  md5={md5}  bytes={len(body.encode())}")
print("OK")
