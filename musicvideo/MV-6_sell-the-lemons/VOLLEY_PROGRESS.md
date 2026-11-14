# MV-6 VOLLEY PROGRESS

## Volley 1 — CHORUS-HOOK TEST (2026-11-06, coordinator run) — DONE, 4 fired
- S05 HOOK t1: **KEEP** (ratio 1.11 in band; look holds) · S01 t1: REJECT (G2 "BACON" banner) → t2: **KEEP-WITH-FLAG** (duplicate background Bacon 2–5s; use 0–2s + 5–10s) · S06 t1: **KEEP-WITH-FLAG** (montage, use 0–6s; "$" glyph minor).
- Hook verdict: **LOOK HOLDS** — identity, world, and mouth performance all pass on the first pull. Plan proceeds as written in MV_PREPRO_MV-6.md.
- No master assembled, no DELIVERED flag, no commit, no IRC (parent reviews).

## Owed volleys (parent fires)
- V2: S02 (intro singing) + S03 (V1 L1–L4) + S04 (V1 L5–L8) — all ref_bacon_closeup, no-lettering clause in every vehicle.
- V3: S07 (V2 L1–L3) + S08 (V2 L4–L6, Joe entrance, Joe mouth closed/still) + S09 (V2 L7–L8).
- V4: S10 (C2 hook — fresh take, own occurrence) + S11 (C2 montage).
- V5: S12 (bridge montage volley material, beat cuts) + S13 (bridge sustained chant).
- V6: S14 (V3 L1–L4, World 2) + S15 (V3 L5–L8).
- V7: S16 (final-chorus PEAK hook, ref_money_mountain_portal) + S17 (peak montage) + S18 (outro rhyme).
- Optional refinement: one small-model/Gemini pass over song 0–30s to upgrade the [inferred] intro/V1 head times before assembly.

## Volley 2 — INTRO + VERSE 1 (2026-11-06, volley-coordinator run) — 3 fired, QC done
- S02 t1: **KEEP** (ratio 0.96, all gates pass) · S03 t1: **REJECT G4** (profile from ~6s, L4 sung sideways; reroll owed — staging axis, vehicle v2 written) · S04 t1: **REJECT G4** (bends down from ~5s, L7–L8 face-down; reroll owed — staging axis, vehicle v2 written).
- Lesson: action beats invade the vocal window at the take midpoint (see TAKE_HISTORY volley-2 lesson). All remaining verse vehicles are now action-free.

## Volley 3 — VERSE 2 + JOE (2026-11-06, volley-coordinator run) — 3 fired, QC done
- S07 t1: **REJECT G2** (readable "Depot District" signage; performance itself was perfect, ratio 1.04) — reroll owed, TEXT axis, vehicle v2 written · S08 t1: **REJECT G2 + duplicate + G4-tail** (signage "…mon depot"; second small Joe in the doorway; Bacon turns to the portal for the L6 tail; Joe himself passes every gate) — reroll owed, vehicle v2 written · S09 t1: **KEEP** (ratio 0.81, all gates pass, strongest motion floor of the build).

## COORDINATOR STATUS — generation cap reached for this run (6/6 videos: V2 + V3)
All remaining vehicles are WRITTEN and fire-ready. Owed queue for the next continuation run, in plan order:
- Rerolls: S03 v2 (staging) · S04 v2 (staging) · S07 v2 (text) · S08 v2 (text + restage) — 4 videos.
- V4: S10 (C2 hook, vehicle hardened vs signage) + S11 (C2 montage) — 2 videos.
- V5: S12 (bridge machine montage) + S13 (bridge sustained chant) — 2 videos. (Optional extra plate if the parent wants it: a P3 Bacon-dancing insert for the bridge's "dancing" line — no vehicle written; S12's machine plate + S13 carry the bridge as planned.)
- V6: S14 (V3 L1–L4, World 2, vehicle hardened) + S15 (V3 L5–L8, vehicle rewritten action-free) — 2 videos.
- V7: S16 (peak hook) + S17 (peak montage) + S18 (outro rhyme, set-down confined to final second) — 3 videos.
Total owed: 13 generations. Current KEEPs: S01 t2 (flagged windows), S02 t1, S05 t1, S06 t1 (flagged trim), S09 t1.

## Volley 4 + REROLLS (2026-11-06, coordinator #3) — firing
- **S03 v2 reconciliation (before firing):** the v2 vehicle's line assignment already matches the corrected LYRIC_TIMELINE (L1–L4 = 19.86–32.9, span **13.0s**) — content unchanged. Two adjustments made to the vehicle text: (1) the pre-vocal pop-in/shrug beat (0.0–0.5s) is REMOVED and the performance window widened to the full clip (0.0–10.0s) so the sung span stretches toward the 13.0s song span; (2) relaxed/unhurried pacing language added ("spreading the lines evenly across the whole clip"). Expected line ratio ≈ 13.0 ÷ ~10 ≈ **1.30 — grey zone** (generation band 0.80–1.25); grey-zone protocol applies at QC (re-measure + ear check, not auto-reject), and per-word assembly warp caps (slowdown ≤2x) cover 1.30 comfortably. The staging fix (button untouched, locked facing) is unchanged.
- Batch order: S03 v2 · S04 v2 · S07 v2 · S08 v2 · S10 (C2 hook, fresh) · S11 (C2 montage). **BATCH DONE — verdicts (full rows in TAKE_HISTORY.md):**
  - S03 t2: **KEEP-WITH-FLAG** — staging fixed (facing locked, button untouched); ratio **1.38 GREY** vs the corrected 13.04s span (per-line L1+L2 1.27 · L3 1.31 · L4 ≈2.38, the tightest interval — assembly adjudicates L4 against word-level song times). Frame rule pass.
  - S04 t2: **KEEP** — bend fixed; ratio **1.19 in band**; all gates pass.
  - S07 t2: **KEEP** — text fixed (panel wall blank at full-res); ratio **0.99 in band**; flag: hair renders shorter/tighter + blue panel-light cast.
  - S08 t2: **REJECT — G2 SAME-AXIS double reject** (v1 shopfront signage → v2 lemon-crate print "FRES…/LEMO…"). Everything else passed (ratio 1.07; Joe perfect; one-scale and facing both fixed). **No third attempt fired — parent's call.** A v3 must keep crates out of frame entirely.
  - S10 t1: **KEEP-WITH-FLAG** — fresh C2 hook, content complete once; ratio **≈0.92 in band** (L3-end estimate flagged in TAKE_HISTORY); flag: camera drifts/pushes instead of locked (facing + mouth pass).
  - S11: **NOT GENERATED** — tool-side integrity error on the call; not retried per run instructions. **Parent: re-fire S11 in a later run** (C2 L5–L8 montage still owed).
- Current KEEPs: S01 t2 (flagged windows) · S02 t1 · S03 t2 (flagged grey) · S04 t2 · S05 t1 · S06 t1 (flagged trim) · S07 t2 (flagged texture) · S09 t1 · S10 t1 (flagged drift).
- Still owed after this run: S08 resolution (parent) · S11 re-fire (parent) · V5 = S12 + S13 · V6 = S14 + S15 · V7 = S16 + S17 + S18.

## ⚠ REFINEMENT RESULT — the head timeline was WRONG; plan slots S01–S03 shift (parent re-map needed)
The owed 0–30s refinement RAN and overturned the stage-1 inferred times (full detail in AUDIO_NOTES_MV6.md + LYRIC_TIMELINE.md, both updated; evidence work/head30_small_words.json). Small (unprompted + prompted) and tiny (unprompted) agree: **singing starts at 2.72s** — intro hook line 2.72–5.32, "Sell the lemons" at 6.88–8.34 / 9.92–11.60 / 15.70–18.00, Verse 1 = **19.86–44.2** (not 20.7). Consequences:
- S01's slot (0.0–14.5) is NOT wordless: it carries the intro hook line + hook phrases #1–#2. S01 t2 (mouth closed throughout) cannot be the slot's singing coverage — it remains the opening visual / clicks cover only.
- S02's take sings exactly the intro-hook content ("Bacon head on the stand. Sell the lemons, sell the lemons.") — its natural song home is now **2.72–11.60**, not 14.5–20.7 (phrase-level ratios there: hook line 2.6s song ÷ 2.3s take ≈ 1.13; the parent's assembly call).
- S03's span becomes L1–L4 = 19.86–32.9 (13.0s); the v2 reroll vehicle's content is unchanged, its ratio will be measured against 13.0s.
- S04 and everything from Chorus 1 onward are base-measured and unchanged.

## Volley 5 + S08 v3 (2026-11-06, coordinator #4) — firing
- S08 t3: **KEEP** — v3 empty-yard redesign fixed G2 after the same-axis double reject (ratio 1.10 in band; Joe perfect; facing locked). S08 is resolved, NOT structural.
- S11 re-fire: **FAILED AGAIN — same tool-side integrity_check_failed on the verbatim call** (second consecutive). Not retried per rule. Still owed; parent decides the route.
- S12 t1: **KEEP** — bridge machine-line plate (motion mean diff 9.966, G2 clean at full-res, no faces/speech as specced).
- S13 t1: **REJECT** — only 3 of 4 chants (completeness) + frame-rule fail in the vocal window (32f near-dup run). G2/G1/G4 pass. Reroll owed (parent).
- S14 t1: **KEEP-WITH-FLAG** — World 2 singing, all 4 lines complete, G2 clean; ratio 1.30 grey.
- S15 t1: **REJECT** — L8 tail truncated at the clip edge (completeness) + G2 (readable "12" numeral + pseudo-text stall placards at full-res). Action-free staging itself passed. Reroll owed (parent).

## COORDINATOR #4 BATCH SUMMARY (2026-11-06)
- Fired 5 of 6 (S11's verbatim re-fire died pre-generation on the same tool-side integrity_check_failed — second consecutive; not retried, not rephrased).
- Verdicts: S08 t3 **KEEP** (G2 double-reject axis FIXED by the empty-yard redesign) · S12 t1 **KEEP** (bridge plate) · S14 t1 **KEEP-WITH-FLAG** (grey 1.30) · S13 t1 **REJECT** (3/4 chants + frame rule) · S15 t1 **REJECT** (L8 truncated + G2 signage).
- **Current KEEP pool: S01 t2 (flagged windows) · S02 t1 · S03 t2 (flagged grey) · S04 t2 · S05 t1 · S06 t1 (flagged trim) · S07 t2 (flagged texture) · S08 t3 · S09 t1 · S10 t1 (flagged drift) · S12 t1 · S14 t1 (flagged grey).**
- Still owed: S11 (parent route decision — two verbatim integrity failures) · S13 reroll (count + motion floor) · S15 reroll (signage-free orchard) · V7 = S16 + S17 + S18.
- No assembly, no DELIVERED flag, no commit, no IRC (parent reviews).

## Volley 6 — FINAL BATCH (2026-11-06, coordinator #5) — firing
- Batch (cap 6): S11 v2 (parent-written redesign, stand_wide ref) · S13 t2 reroll (v2 vehicle: motion floor added — juicer/conveyor continuous motion + chant bob/sway) · S15 t2 reroll (v2 vehicle: stalls/placards/numerals banned by name, brisk even pacing, L8 must land by 9.0s) · S16 (peak hook, portal + closeup + money_tower refs) · S17 (peak montage, money_tower + boardroom + tank_robots refs, Joe mouth closed/still) · S18 (outro rhyme, stand_wide + closeup refs). QC sheets in work/qc_v6/.
- **BATCH DONE — 6/6 fired, all landed, all QC'd (full rows in TAKE_HISTORY.md):**
  - S11 t1 (v2 vehicle): **KEEP-WITH-FLAG** — the redesign cleared the integrity wall on the first try; C2 montage SECURED (motion 10.321; flag: distant pseudo-glyph town signage, none readable).
  - S13 t2: **REJECT** — motion-floor fix WORKED (frame run 32f→0f) and G1/G2/G4 pass, but adjudicated audio = **3 of 4 chants again** (split-half + RMS confirm; seconds 8–9 silent). Count axis failed twice — parent's call.
  - S15 t2: **REJECT** — G2 FIXED (zero text/numerals) and L8's tail now lands, but adjudicated audio shows L8's head words "Sell the lemons," were never sung (all three passes omit them). L5–L7 complete + signage-free = clean salvage. Parent's call on L8.
  - S16 t1: **KEEP-WITH-FLAG** — PEAK hook complete, ratio ≈0.99 in band, all gates pass; flag: raster **1168×640** not 1280×720 (three-ref conditioning drag; ~1.10× upscale at assembly).
  - S17 t1: **KEEP** — peak montage; Joe rule PASS (both mouths closed/still at full-res, Joe identity exact); motion 9.742; minor note: one stray "Oh" in take audio 0–0.9s, no visible open mouth.
  - S18 t1: **REJECT** — only **2 of 3 chants** (RMS digital-silence at 2–3s discounts the prompted pass); pull-back rhyme + lemon set-down land, all other gates pass. Parent's call.
- **Current KEEP pool (15): S01 t2 (flagged windows) · S02 t1 · S03 t2 (flagged grey) · S04 t2 · S05 t1 · S06 t1 (flagged trim) · S07 t2 (flagged texture) · S08 t3 · S09 t1 · S10 t1 (flagged drift) · S11 t1 (flagged signage) · S12 t1 · S14 t1 (flagged grey) · S16 t1 (flagged resolution) · S17 t1.**
- **Generation is COMPLETE except three count-axis slots, all parent's call: S13 (3/4 chants ×2 takes) · S15 (L8 head missing; L5–L7 salvage clean) · S18 (2/3 chants).** Dominant remaining risk is enumerative (repeated-phrase counts / edge words), not staging, text, or motion — both fix packages this batch worked.
- No assembly, no DELIVERED flag, no commit, no IRC (parent reviews).
