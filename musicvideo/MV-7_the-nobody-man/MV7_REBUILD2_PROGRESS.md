# MV-7 REBUILD-2 — progress

- Start 2026-11-07 (coordinator run 1). Brief MV7_REBUILD2_BRIEF_2026-11-07.md + Slopcannon read in full. Otaku master REJECTED for timing — dead, never re-deliver. Flag already renamed *.rejected-timing.
- Method: song grid = SONG_WORDS.json (330 words) + LYRIC_TIMELINE.md; line ratio = song sung span / take sung span (first word onset to last word end); KEEP band 0.80–1.25, GREY 0.60–0.80 / 1.25–1.60 (needs forced re-measure + mouth check), MISS = clear miss / wrong words.
- CLEAR-MISS re-fire list from brief (15 units): U06 0.577 · U08 0.587 · U17 0.590 · U15 0.607 · U16 0.608 · U34t2 0.609 · U21 0.617 · U14 0.665 · U32 0.667 · U20 0.677 (also cover-only, no face) · U13 0.679 · U22 0.679 · U18 0.697 · U35t2 0.708 · U05 0.730.
- GREY (keep pool, re-measure): U02 1.263 · U37 1.290 · U36 1.232.
- KEEP pool (in band, need mouth-event anchoring at assembly): U01t2, U03, U04, U07, U09, U10, U11, U12, U19t2, U23, U24t2, U25, U26, U27, U31, U33 (truncates final word — bad-word rule), U38, U39t2, U40 (words garbled). Bridge U28–U30 montage by design.
- Song sung spans (SONG_WORDS, first onset→last end): V1.1 2.80s · V1.2 2.02s · V1.3 2.20s · V1.4 2.60s · PC1.1 2.28s · PC1.2 2.10s.

## Volley R2-1 (this run, 6 generations max — PACING axis, single-line splits)
Vehicles in rebuild2_vehicles/ (PRE+IMAGE+POST format mirroring otaku_vehicles/; era A still refs/otaku_eraA.webp; 5s request; lyric quoted 3x; brisk/quick wording; mouth closes after last word):
- R05a = U05 line V1.1 "I got a profile, got a pile" — target ~3.0s window
- R05b = U05 line V1.2 "Got a thousand posts in a folder file" — target ~2.0s window
- R06a = U06 line V1.3 "Old meme face and a busted grin" — target ~2.0s window
- R06b = U06 line V1.4 "Been here so long, I could sign back in" — target ~2.5s window
- R08a = U08 line PC1.1 "I kept clicking, kept sticking around" — target ~2.5s window
- R08b = U08 line PC1.2 "Little by little, I learned the sound" — target ~2.0s window
Status: FIRED + MEASURED (coordinator run 1 hit its 6-generation cap — STOPPED firing here).

## Volley R2-1 results (all takes in takes/rebuild2/, 1248x704/24fps; words = faster-whisper small on take audio, work/rebuild2_take_words/)
| Take | File md5 | Dur | Heard (exact lyric words?) | Take span | Song span | Ratio | Verdict |
|---|---|---|---|---|---|---|---|
| R05a (V1.1) | ef3221b9e4743932e6aff222d0368e4a | 10.0s (5s requested — return miss) | "I got a profile, got a pile" YES | 5.30s | 2.80s | 0.528 | MISS |
| R05b (V1.2) | 573a5acb33fe6b6c5bf426f69fb2e2c8 | 5.0s | "Got a thousand posts in a folder file" YES | 4.28s | 2.02s | 0.472 | MISS |
| R06a (V1.3) | 94aad1681d68895762765510ecfe2766 | 10.0s (5s requested — return miss) | "Old meme face and a busted grin" YES | 4.34s | 2.20s | 0.507 | MISS |
| R06b (V1.4) | 757fac04f5407c13c78d2699071222b2 | 5.0s | "Been here so long, I could sign back in" YES | 4.26s | 2.60s | 0.610 | GREY (low) |
| R08a (PC1.1) | 59369bbc80e96dea39411f33d621962d | 5.0s | "I kept clicking, kept sticking around" YES | 3.98s | 2.28s | 0.573 | MISS |
| R08b (PC1.2) | 7976a910d169ea8a39a71b69ffd81fdd | 5.0s | "Little by little, I learned the sound" YES | 3.52s | 2.10s | 0.597 | MISS (just under grey floor) |

- Identity/visual QC (sheets work/rebuild2_qc/R05A_sheet.jpg, R06A_sheet.jpg read at full res): otaku lock PASS (cadmium streak, round glasses, cobalt star hoodie, headphones at neck, star lamp, bright room, no readable text); mouths visibly open in sung tiles. R06A's 10s tail drifts to a head-down laugh after the line — trim to the front sung span if ever used.
- KEY FINDING for the follow-up coordinator: word accuracy is now perfect (6/6 exact lines, no repeats) but PACING barely moved vs the 2-line takes. The generator sings a single line in ~3.5–5.3s regardless of the brisk wording — this is the measured pace floor (~0.47–0.61 on these slots), not a prompt wording failure. Per brief rule 2 each of these lines has now had ONE failed pacing pull (the original 2-line take) + this single-line pull counts as the second axis change (split). Follow-up options, in brief order: (a) ONE more pacing pull per line on a new axis only if a genuinely different axis exists; otherwise (b) mark V1.1/V1.2/V1.3/PC1.1/PC1.2 STRUCTURAL and cover with beat-cut montage + kinetic words (bad-word rule), disclosed; R06b at GREY 0.610 may be rescued only via the grey-zone path (forced-alignment re-measure + mouth check) or a bounded warp-rescue per skill — never warp a MISS into place. Do NOT keep re-firing identical brisk vehicles.
- NO assembly this run: re-fires remain outstanding (below). NO master, NO flag, NO announce.

## Still owed after this run (for follow-up coordinator)
Single-line re-fires for: U17 (C1.Tc, C1.Td — "Nobody Man" x2), U15 (C1.8 — "Nobody Man, Nobody Man" single line as written), U16 (C1.Ta, C1.Tb), U34 (FC.5, FC.6), U21 (PC2.1, PC2.2), U14 (C1.7 single), U32 (FC.1, FC.2), U20 (V2.5, V2.6 — must show FACE this time), U13 (C1.5, C1.6), U22 (PC2.3 single), U18 (V2.1, V2.2), U35 (FC.7 single). Plus any R2-1 line that lands MISS/GREY-fail. Then: mouth-event re-anchoring of keep pool, re-cut, master gate at every line onset, house master masters/mv7_im_the_nobody_man_16x9_rebuild2.mp4 + 50MB copy, MV7_REBUILD2_NOTES.md, flag, commit, announce. DO NOT assemble until all re-fires are covered or marked STRUCTURAL per brief rule 2.

---

## Coordinator run 2 (2026-11-07) — Volley R2-2 + PART B warp-rescue test

### Volley R2-2 (6 generations — cap hit, stopped)
NEW delivery axes (not run 1's brisk wording): chant lines (U14/U15/U16) = quick punchy STACCATO stadium chant, clipped percussive syllables; PC2 lines (U21) = RAPID CLIPPED, almost spoken-fast. Vehicles in rebuild2_vehicles/mv7r2_r{14,15,16a,16b,21a,21b}_vehicle.txt (PRE/POST mirrored from the units' original otaku vehicles; era A still for U14–U16, era B for U21; lyric quoted 3x; 5s requests — all 6 returned exactly 5.0s, 1248x704/24fps). Takes in takes/rebuild2/mv7r2_r*_t1.mp4; words in work/rebuild2_take_words/R{14,15,16A,16B,21A,21B}.json; sheets in work/rebuild2_qc/.

| Take | File md5 | Dur | Heard (exact lyric words?) | Take span | Song span | Ratio | Verdict |
|---|---|---|---|---|---|---|---|
| R14 (U14 · C1.7) | 458bebbc0d34804c287e916236643d86 | 5.0s | "I'm the nobody man." YES | 2.88s | 2.26s | 0.785 | GREY (high) |
| R15 (U15 · C1.8) | 80073d064f37ae34984f95c431d83090 | 5.0s | "Nobody man, nobody man." YES | 3.56s | 4.08s | 1.146 | KEEP |
| R16A (U16 · C1.Ta) | c71a7e3e85bc2460ce3c772c85774e0e | 5.0s | "Nobody man." YES | 3.56s | 2.05s [inferred split] | 0.576 | MISS |
| R16B (U16 · C1.Tb) | 32b159f7087ad242701fa05326f85d82 | 5.0s | "Nobody man." YES | 3.52s | 2.05s [inferred split] | 0.582 | MISS + VISUAL FLAG |
| R21A (U21 · PC2.1) | 93731b6170fc7be2178082268b0f6c37 | 5.0s | "I kept clicking, kept sticking around." YES | 3.66s | 2.82s | 0.770 | GREY |
| R21B (U21 · PC2.2) | 2d5b4aeb9c4c2a3a9a765ef9ae3d989f | 5.0s | "Little by little, I learned the sound." YES | 4.30s | 2.12s | 0.493 | MISS |

- Word accuracy 6/6 EXACT again — every take sings exactly its line, once, no repeats, no extras. The failure axis remains pace only.
- The staccato-chant axis DID move the chant lines: C1.7 0.665 (orig U14) → 0.785 GREY-high; **C1.8 0.607 → 1.146 KEEP — the first in-band re-fire of rebuild-2; R15 enters the keep pool** (mouth-event anchoring at assembly). Rapid-clipped moved PC2.1 to 0.770 GREY (PC1.1-class lines were 0.573–0.617 before).
- Still floored: single "Nobody Man" tag phrases (~3.5s each — R16A holds "man" 1.74s, R16B holds "nobody" 2.68s) and PC2.2 (R21B lingers on "Little" 0.00–1.52). BUT see Part B: R16A/R16B rescue speedups are 1.74x/1.72x — INSIDE the now-proven rescue envelope.
- Visual QC (sheets work/rebuild2_qc/R*_sheet.jpg): identity lock PASS on R14/R15/R16A/R21A/R21B (cadmium streak, round glasses, cobalt star hoodie, headphones at neck, star lamp, bright room, no readable text; era B room correct for R21A/R21B); mouths visibly open across sung tiles. **R16B VISUAL FLAG: my "quick excited nod" staging produced a head-bow — tiles 1–3 (~0–1.5s) show cat-ear headphones ON HIS HEAD and head bowed down laughing, mouth not visible for the head of the phrase; compliant from ~1.5s on. Do not use R16B's head span; gate decides if it is used at all.**

### PART B — warp-rescue test (NO generations; scratch renders in work/rebuild2_rescue/, script build_rescue.py)
Method: swing keyframes from the take's own transcription (word onsets) → song word onsets (SONG_WORDS.json), monotone-cubic (PCHIP) interpolation so speed varies smoothly (no per-word setpts steps), frames resampled onto the song grid, song excerpt muxed as audio. Mouth gate = crop grid at every song word onset + onset+1 frame (R06B_mouthgate.jpg / R08A_mouthgate.jpg; rows = words in order, left = onset frame, right = +1 frame).

- **R06B (V1.4, ratio 0.610 GREY) — overall speedup 1.638x. RESCUE PASS.** Mouth gate 9/9 words open or transitional at onset or +1 frame (8/9 open/transitional AT onset; "been" closed at exact onset, open at +1 — the take's frame 0 is a closed-smile lead-in). Motion: mean frame diff 3.89, max near-dup run 0f — no freezing, sheet frames clean, energy reads natural-brisk, NOT frantic/broken.
- **R08A (PC1.1, ratio 0.573 MISS) — overall speedup 1.746x. RESCUE PASS WITH TWO ANCHOR FIXES.** Mouth gate: kept / clicking / kept(2nd) / around OPEN at onset; clicking transitional at onset, open +1. Two exceptions, both anchoring artifacts, not warp failures: (1) "I" closed at onset AND +1 — the take opens on a held closed smile; its audio onset (0.00) leads the visible mouth, so assembly must re-anchor line heads on the VISIBLE mouth event (brief rule, MV-3 method); (2) "sticking" shares the previous word's mouth gesture — the song stamps squeeze kept→sticking onsets 0.02s apart (35.36/35.38), an ASR stamp artifact; merge such sub-0.1s stamp pairs into ONE anchor. Motion: mean diff 2.73, max near-dup run 1f — clean, NOT frantic/broken.
- Method caveat: raw PCHIP derivative spikes at cramped keyframes (instantaneous 8.8x / 26.7x) are interpolation artifacts; in the frame resample they cost at most a 1-frame jump and are invisible on the sheets. Assembly should use the interval-speed table + merged anchors rather than raw PCHIP through cramped stamps.
- **RECOMMENDATION: warp-rescue is VIABLE for the pace-floored cluster** — proven at 1.64x (R06B) and 1.75x (R08A) overall speedups with mouths landing open at onsets. Conditions: (a) line heads re-anchored on visible mouth events, (b) cramped song stamp pairs merged to single anchors, (c) master gate still decides every line. Disposition by required speedup: R06b 1.64x PROVEN · R08b 1.68x candidate (in envelope, untested on that take) · R16a 1.74x candidate · R16b 1.72x candidate BUT visual flag above · R08a 1.75x PROVEN-with-fixes · R05a 1.89x edge (at MV-5 v4's accepted 1.91x precedent, unproven) · R06a 1.97x / R21b 2.03x / R05b 2.12x BEYOND precedent — STRUCTURAL (beat-cut montage + kinetic words), disclosed. This supersedes run 1's "never warp a MISS into place" caution for the ≤1.75x envelope: the gate evidence, not the ratio alone, now carries the verdict — but ONLY inside the tested envelope and only with the two anchor fixes.

### Updated dispositions (all re-fired lines)
- KEEP pool additions: R15 (C1.8, 1.146). GREY path (forced re-measure + mouth check; warp need ≤1.30x): R14 (C1.7, 0.785), R21A (PC2.1, 0.770), plus brief greys U02 1.263 · U37 1.290 · U36 1.232 (unchanged, still owed).
- Rescue cluster (swing-warp at assembly, conditions above): R06b PROVEN · R08a PROVEN-with-fixes · R08b, R16a candidates · R16b candidate-with-visual-flag.
- STRUCTURAL (montage + kinetic, disclosed): V1.2 (R05b 2.12x) · V1.3 (R06a 1.97x) · PC2.2 (R21b 2.03x). Edge call left to assembly: V1.1 (R05a 1.89x) — rescue attempt permissible, master gate decides.
- NO assembly this run. NO master, NO flag, NO announce.

## Still owed after run 2 (for follow-up coordinator)
Single-line re-fires (14 takes ≈ 3 volleys at cap 6): U17 (C1.Tc, C1.Td), U34 (FC.5, FC.6), U32 (FC.1, FC.2), U20 (V2.5, V2.6 — must show FACE this time), U13 (C1.5, C1.6), U22 (PC2.3 single), U18 (V2.1, V2.2), U35 (FC.7 single). For chant/tag re-fires use the STACCATO axis (it moved C1.7/C1.8); do NOT add head-gesture business before the first word (R16B flag). Then: grey-zone forced re-measures (U02/U36/U37 + R14/R21A mouth checks), rescue renders for the candidate cluster, mouth-event re-anchoring of the full keep pool, re-cut, master gate at every line onset, house master + 50MB copy, MV7_REBUILD2_NOTES.md, flag, commit, announce. DO NOT assemble until all re-fires are covered or marked STRUCTURAL per brief rule 2.

---

## Coordinator run 3 (2026-11-07) — Volley R2-3

Axes per run-2 evidence: U13a/U13b/U17a/U17b = STACCATO chant; U22 = RAPID CLIPPED (run-2 PC2 axis); U35 (FC.7 hook line, chant-class like C1.7) = STACCATO. ALL vehicles carry the R16B fix: head up, face to camera, mouth visible from frame one, NO head-gesture/nod/bow business before or during the line, movement only after the last word. Vehicles in rebuild2_vehicles/mv7r2_r{13a,13b,17a,17b,22,35}_vehicle.txt (PRE/POST mirrored from the units' original otaku vehicles; era A still for U13/U17, era B for U22, era C for U35; lyric quoted 3x; 5s requests). Takes in takes/rebuild2/mv7r2_r*_t1.mp4; words in work/rebuild2_take_words/R{13A,13B,17A,17B,22,35}.json; sheets in work/rebuild2_qc/. Song spans from SONG_WORDS.json word times (first onset→last end): C1.5 2.38s · C1.6 1.86s · C1.Tc/Td 2.05s each [inferred split, same convention as run 2's Ta/Tb] · PC2.3 4.16s · FC.7 1.86s.

| Take | File md5 | Dur | Heard (exact lyric words?) | Take span | Song span | Ratio | Verdict |
|---|---|---|---|---|---|---|---|
| R13A (U13a · C1.5) | 87fd2a4a1200a31d7344e7b988e4bdb3 | 5.0s | "I got a thousand little sparks." YES | 2.26s | 2.38s | 1.053 | KEEP |
| R13B (U13b · C1.6) | 8106f08a7da85a1ed81b8628059238cf | 5.0s | "Flicking in the dark." YES | 1.62s | 1.86s | 1.148 | KEEP |
| R17A (U17a · C1.Tc) | 7668bdc27907b048a35613f82e6d5087 | 10.0s (5s requested — return miss) | "Nobody man." YES (once) | 2.36s (line only) | 2.05s | 0.869 | KEEP |
| R17B (U17b · C1.Td) | d260a6cfb80ef3f9a4d671e2617c2a3c | 10.0s (5s requested — return miss) | "Nobody man." YES (once) | 2.54s | 2.05s | 0.807 | KEEP (band edge) |
| R22 (U22 · PC2.3) | db67865ea1d278707f327c69efec2420 | 5.0s | "No one crowned me, no one had to." YES | 3.78s | 4.16s | 1.101 | KEEP |
| R35 (U35 · FC.7) | cdaf7e222c9b7373729872048891ff6d | 5.0s | "I'm the nobody man." YES | 3.50s | 1.86s | 0.531 | MISS |

- Word accuracy 6/6 EXACT again — every take sings exactly its line, once, no repeats of the line. Best volley of rebuild-2: 5 KEEP / 1 MISS.
- The staccato axis generalises beyond tags: sung-chant lines C1.5/C1.6 landed IN BAND at natural pace (1.053 / 1.148) — no warp needed. Rapid-clipped put the long PC2.3 (4.16s song span, the longest single line re-fired) in band at 1.101; the take's mid-line gap (me→No, 2.14→2.56) mirrors the song's own gap (97.14→97.58).
- R17A: 10s return; the line sits at 0.0–2.36s, then the take LAUGHS ("Heh. Hehehe…" at 4.32–8.50) for the tail — span measured on the line words only (run-1 R06A convention). Assembly trims to the front sung span; do not use the laughing tail.
- R17B: 10s return; line onset is LATE (first word 2.32s, span 2.32–4.86) — assembly trims the closed-mouth head; ratio is band-edge 0.807, mouth-event anchoring decides.
- R35 MISS detail: words exact but the take holds "I'm" for 1.82s (0.0–1.82) before finishing the phrase at 3.50s. Required rescue speedup 3.50/1.86 = 1.88x — the EDGE zone (same as R05a's 1.89x, at MV-5 v4's accepted 1.91x precedent, unproven on this take, and the front-loaded word distribution makes the swing warp uneven). Disposition: rescue candidate at the edge — assembly may attempt it, master gate decides; if the gate fails, FC.7 goes STRUCTURAL (montage + kinetic), disclosed.
- Visual QC (sheets work/rebuild2_qc/R{13A,13B,17A,17B,22,35}_sheet.jpg): identity lock PASS on all 6 (cadmium streak, round glasses, cobalt star hoodie, headphones at neck, star lamp, bright rooms; era B fuller room correct for R22, era C screen-wall kingdom correct for R35); mouths visibly open across sung tiles; NO head-bow on any take — the R16B failure did not recur; no readable text anywhere.
- NO assembly this run. NO master, NO flag, NO announce.

### Updated dispositions after run 3
- KEEP pool additions: R13A (C1.5, 1.053), R13B (C1.6, 1.148), R17A (C1.Tc, 0.869 — trim laughing tail), R17B (C1.Td, 0.807 — trim late head), R22 (PC2.3, 1.101). Join R15 (C1.8) + the brief's in-band pool.
- Rescue cluster additions: R35 (FC.7) at 1.88x EDGE (joins R05a at the edge; gate decides, else STRUCTURAL).
- Unchanged from run 2: GREY path R14 (0.785), R21A (0.770), U02/U36/U37 · rescue PROVEN R06b/R08a, candidates R08b/R16a/R16b(flagged) · STRUCTURAL V1.2, V1.3, PC2.2 · edge R05a.

## Still owed after run 3 (for follow-up coordinator)
Single-line re-fires (8 takes ≈ 2 volleys at cap 6): U18 (V2.1, V2.2), U20 (V2.5, V2.6 — must show FACE this time), U32 (FC.1, FC.2), U34 (FC.5, FC.6). Axes: sung lines RAPID CLIPPED or STACCATO per line class (both proven in-band this run); keep the no-head-business staging. Then: grey-zone forced re-measures (U02/U36/U37 + R14/R21A mouth checks), rescue renders for the candidate cluster (R08b, R16a, R16b-flagged, edge R05a/R35), mouth-event re-anchoring of the full keep pool, re-cut, master gate at every line onset, house master + 50MB copy, MV7_REBUILD2_NOTES.md, flag, commit, announce. DO NOT assemble until all re-fires are covered or marked STRUCTURAL per brief rule 2.

---

## Coordinator run 4 (2026-11-07) — Volley R2-4

Axes per task: U18a/U18b/U20a/U20b = RAPID CLIPPED (run-3 PC2.3 axis); U32a (FC.1, the hook chant "I'm The Nobody Man") = STACCATO; U32b (FC.2, sung answer line) = RAPID CLIPPED. ALL vehicles carry the no-head-business staging (head up, face to camera, mouth visible from frame one); U20 vehicles add an explicit face-lock (camera stays on his singing face the whole clip — no cutaway/back view/over-shoulder). Vehicles in rebuild2_vehicles/mv7r2_r{18a,18b,20a,20b,32a,32b}_vehicle.txt (PRE/POST mirrored from the units' original otaku vehicles; era B still for U18/U20, era C still for U32; lyric quoted 3x; 5s requests). Takes in takes/rebuild2/mv7r2_r*_t1.mp4 (1248x704/24fps); words in work/rebuild2_take_words/R{18A,18B,20A,20B,32A,32B}.json (faster-whisper small); sheets in work/rebuild2_qc/. Song spans from SONG_WORDS.json (first onset→last end): V2.1 2.54s · V2.2 2.08s · V2.5 2.32s · V2.6 2.26s · FC.1 2.12s · FC.2 2.40s.

| Take | File md5 | Dur | Heard (exact lyric words?) | Take span | Song span | Ratio | Verdict |
|---|---|---|---|---|---|---|---|
| R18A (U18a · V2.1) | 661ea255e5910402f8470206819e8229 | 5.0s | "I got drafts in the drawer like coins." YES | 2.72s | 2.54s | 0.934 | KEEP |
| R18B (U18b · V2.2) | 26b1bc2bcd65ced401d8acb7fa3e2c83 | 5.0s | "Half mad thoughts and a stack of joins." YES (see note) | 3.20s | 2.08s | 0.650 | GREY (low) |
| R20A (U20a · V2.5) | ba624287600ca368cba7347b56bef899 | 5.0s | "Everybody chasing that giant shout." YES | 3.10s | 2.32s | 0.748 | GREY |
| R20B (U20b · V2.6) | fa89ee305f64801ae8d3e3fbb6396147 | 5.0s | "I got a small flame I won't put out." YES | 3.18s | 2.26s | 0.711 | GREY |
| R32A (U32a · FC.1) | 5ac75d2215e07e69b28cbd65ba072377 | 10.0s (5s requested — return miss) | "I'm the the nobody man" — line words present + extra token (see note) | 4.68s | 2.12s | 0.453 | MISS → STRUCTURAL |
| R32B (U32b · FC.2) | 052e02066a39dc8a00a8a7d326470634 | 10.0s (5s requested — return miss) | "Still here. Still stand." YES (split delivery) | 5.88s | 2.40s | 0.408 | MISS → STRUCTURAL |

- Word coverage 6/6 lines — every take contains its line's actual words, once. Cumulative rebuild-2 word accuracy: 24/24 exact.
- **R18A is the volley's KEEP**: rapid-clipped lands V2.1 in band at natural pace (0.934), no warp needed beyond mouth-event anchoring.
- GREY cluster (grey path owed: forced re-measure + mouth check): R18B 0.650 (needed speedup 1.54x), R20A 0.748 (1.34x), R20B 0.711 (1.41x) — ALL THREE speedups sit INSIDE the run-2-proven ≤1.75x rescue envelope, so assembly has both the grey path and a proven rescue path for each. Where the pace went: R18B holds "Half" 0.0–0.90; R20A holds "Everybody" 0.0–1.42; R20B spreads evenly ~0.35s/word.
- R18B word note: Whisper tokenizes the take's "Half-mad" as "Half mad" and the song side as "half"+"-made"/"joints" — both are decode artifacts around the same performed line ("Half-mad thoughts and a stack of joins", timeline-adjudicated). The take sings the line.
- **U20 FACE CONFIRMED**: both R20A and R20B sheets show his face front-facing and singing in EVERY tile of the sung span — the original U20 no-face cover defect is fixed. Verse 2 is now fully covered (R18A KEEP + R18B/R20A/R20B GREY); nothing in V2 goes structural.
- R32A MISS detail: staccato did NOT move the final-chorus hook — the generator sang it grand and slow ("I'm" held 1.2s, a ~1.5s held "the" that Whisper splits into two tokens, the second at prob 0.415 — a stutter or a decoder split of the hold; either way the span is the span). Required speedup 4.68/2.12 = 2.21x — beyond the R05b structural line (2.12x). Minor staging drift: a thumbs-up enters ~4.0s, overlapping the tail of the held final word (mouth stays visible; not a head-bow). FC.1 has now had two pacing pulls (orig 2-line 0.667 + this single-line staccato) → **STRUCTURAL per brief rule 2: beat-cut montage + kinetic words, disclosed.** (The era-C thumbs-up tail could serve as montage texture.)
- R32B MISS detail: words exact but delivered as TWO separate phrases — "Still here" 0.0–2.38, a 2.14s silent gap, "Still stand" 4.52–5.88 — against the song's 0.24s internal gap. Full-span ratio 0.408; phrase-level ratios also floored (0.52 / 0.68). Required speedup 2.45x — beyond precedent. Two pacing pulls spent (orig + this) → **STRUCTURAL per brief rule 2: beat-cut montage + kinetic words, disclosed.**
- Visual QC (sheets work/rebuild2_qc/R{18A,18B,20A,20B,32A,32B}_sheet.jpg): identity lock PASS on all 6 (cadmium streak, round glasses, cobalt star hoodie, headphones at neck, star lamp; era B fuller room correct for R18/R20, era C screen-wall kingdom correct for R32); mouths visibly open across sung tiles; NO head-bow on any take; no readable text anywhere (screens abstract).
- NO assembly this run. NO master, NO flag, NO announce.

### Updated dispositions after run 4
- KEEP pool additions: R18A (V2.1, 0.934).
- GREY path additions (forced re-measure + mouth check owed; rescue speedups all ≤1.75x proven envelope): R18B (V2.2, 0.650, 1.54x), R20A (V2.5, 0.748, 1.34x), R20B (V2.6, 0.711, 1.41x). Join R14 (0.785), R21A (0.770), U02/U36/U37 on the grey path.
- STRUCTURAL additions (montage + kinetic, disclosed): FC.1 (R32A, 2.21x needed) · FC.2 (R32B, 2.45x needed). Join V1.2, V1.3, PC2.2. Edge calls unchanged: R05a (V1.1, 1.89x), R35 (FC.7, 1.88x) — rescue attempt permissible, master gate decides.
- Unchanged from run 3: KEEP R13A/R13B/R17A/R17B/R22/R15 + brief pool · rescue PROVEN R06b/R08a, candidates R08b/R16a/R16b(flagged).

## Still owed after run 4 (for follow-up coordinator)
Single-line re-fires (2 takes = 1 partial volley): U34 (FC.5, FC.6 — sung-chant lines; axes per run-3 evidence: STACCATO landed C1.5/C1.6 in band, RAPID CLIPPED also proven; keep no-head-business staging, era C still). Then: grey-zone forced re-measures + mouth checks (U02/U36/U37 brief greys + R14/R21A + new R18B/R20A/R20B), rescue renders for the candidate cluster (R08b, R16a, R16b-flagged, edge R05a/R35), mouth-event re-anchoring of the full keep pool, re-cut (STRUCTURAL lines now: V1.2, V1.3, PC2.2, FC.1, FC.2 — beat-cut montage + kinetic words, disclosed), master gate at every line onset, house master + 50MB copy, MV7_REBUILD2_NOTES.md, flag, commit, announce. DO NOT assemble until all re-fires are covered or marked STRUCTURAL per brief rule 2 — after U34 fires, every clear-miss unit from the brief is dispositioned.

---

## Coordinator run 5 (2026-11-07) — Volley R2-5 (final re-fires) + PART B grey re-measures + PART C rescue renders

### PART A — Volley R2-5 (2 generations — the last clear-miss units, U34)
Axis for BOTH lines: STACCATO chant — because the identical Chorus-1 lines landed IN BAND on staccato in run 3 (C1.5 via R13A 1.053, C1.6 via R13B 1.148); FC.5/FC.6 are the same words in the final chorus. Vehicles in rebuild2_vehicles/mv7r2_r{34a,34b}_vehicle.txt (era C still, lyric quoted 3x, no-head-business staging, 5s requests — both returned exactly 5.0s, 1248x704/24fps). Takes in takes/rebuild2/mv7r2_r*_t1.mp4; words in work/rebuild2_take_words/R34{A,B}.json; sheets in work/rebuild2_qc/. Song spans from SONG_WORDS.json (first onset→last end): FC.5 2.52s · FC.6 2.42s.
**MEASUREMENT WARNING (adjudicated): the first full-file Whisper pass on these two takes produced false word stamps (R34A words smeared 0.0–4.84s with a held "spots"; R34B 0.0–3.00s) that CONTRADICT the takes' RMS energy envelopes — both takes are silent for their first ~0.9s (RMS ≤0.018) and again after ~2.8s / ~2.2s. Per the standing adjudication rule (RMS + mouth frames over a single ASR pass), the spans below come from a re-transcription on audio trimmed to the first RMS energy onset (stamps offset back), cross-checked against the envelopes and the mouth-check grids (work/rebuild2_rescue/R34{A,B}_mouthcheck.jpg). The trimmed pass also hears the words exactly ("sparks", "Flicking" — no mishear normalization needed). The take-word JSONs on disk are the trimmed, adjudicated ones, with the note recorded in-file.**

| Take | File md5 | Dur | Heard (exact lyric words?) | Take span (adjudicated) | Song span | Ratio | Verdict |
|---|---|---|---|---|---|---|---|
| R34A (U34a · FC.5) | 8cc3ee4d4ea1d3fc937af8f83f727dfb | 5.0s | "I got a thousand little sparks" YES | 1.94s (0.85–2.79) | 2.52s | 1.299 | GREY (high) |
| R34B (U34b · FC.6) | 35e93fd36c4a5f2a8822f5c056ce3edd | 5.0s | "Flicking in the dark" YES | 1.24s (0.95–2.19) | 2.42s | 1.952 | MISS → STRUCTURAL |

- Word coverage 2/2 lines — cumulative rebuild-2 word accuracy 26/26 lines (every re-fired line's actual words present).
- The staccato axis OVERSHOT on both lines — after four volleys of takes singing too slow, these two sing too FAST. **R34A GREY 1.299**: the grey path is satisfied in-run (forced re-measure = the RMS-adjudicated trimmed transcription; mouth check = all 6 words open at onset AND +1 on the adjudicated onsets, R34A_mouthcheck.jpg) → **RESCUE at assembly: phrase-warp STRETCH 1.30x (0.77x speed, inside the 0.5x slow floor)**, master gate decides.
- **R34B MISS 1.952**: the take rattles FC.6 off in 1.24s against the song's 2.42s (its Chorus-1 twin R13B took 1.62s for the same words). Ratio is beyond the grey ceiling (1.60); the symmetric edge test also fails (required stretch 1.95x > 1.88x edge). FC.6 has had its pacing pulls (orig U34 unit + this single-line staccato) → **STRUCTURAL per brief rule 2: beat-cut montage + kinetic words, disclosed.** Fallback documented for assembly: the mouth check passes (words visibly articulated at the adjudicated onsets, R34B_mouthcheck.jpg) and a 1.95x stretch sits just inside the 2x slow cap — assembly may attempt it, master gate decides; expected smearing at that factor is why it is not the primary disposition.
- Both takes have ~0.9s of silent closed-smile lead-in before the line (assembly trims the head; the mouth-check grids confirm the visible mouth event coincides with the RMS onset, so no head-lag artifact on either).
- Visual QC (sheets work/rebuild2_qc/R34{A,B}_sheet.jpg): identity lock PASS on both (cadmium streak, round glasses, cobalt star hoodie, headphones at neck, star lamp, era C screen-wall kingdom; mouths visibly open across the sung tiles; NO head-bow; no readable text). Post-line tiles tilt into held smiles/laughs — tails only.
- After this volley EVERY clear-miss unit from the brief is dispositioned. NO assembly this run.

### PART B — Grey-zone forced re-measures + mouth checks (NO generations)
Method: take spans re-derived from per-word transcriptions (work/otaku_take_words/ for U-units, work/rebuild2_take_words/ for R-takes); song spans = SONG_WORDS.json first onset→last end (the runs 1–4 convention); mouth checks = crop grids at every take word onset + onset+1 frame (work/rebuild2_rescue/<unit>_mouthcheck.jpg, script make_mouth_sheets.py; rows = take words in order, left = onset, right = +1).
**Universal finding: in 7 of 8 grey takes the take-AUDIO onset of word 1 leads the VISIBLE mouth — word 1 sits on a closed smile at its audio onset (R20B is the exception, open from word 1). This is the R08A artifact, now confirmed across the whole grey cluster: assembly must re-anchor EVERY line head on the visible mouth event, not the audio onset.**

| Unit | Line | Take span | Song span | Re-measured ratio | Mouth check (onset / +1 per word) | Final disposition |
|---|---|---|---|---|---|---|
| U02 | I1c+I1d (intro chant ×2) | 3.92s | 4.95s window (merged chant stamps; words-convention unmeasurable) | 1.263 window; per-line inferred 1.38 / 1.56 | W1 "I'm" closed/closed (head lag); rest open/transitional throughout, rep-2 "I'm" wide open | RESCUE — phrase-warp STRETCH per phrase (1.38x / 1.56x = 0.72x / 0.64x speed, inside the 0.5x slow floor), head re-anchor |
| U36 | FC.8 "Nobody Man" | 3.36s | 2.34s | 0.696 (words convention — SUPERSEDES the audit's 1.232 window-convention figure: the song's words end at 162.36 and the take holds both words longer per word, nobody 1.76s vs song 1.30s, man 1.60s vs 1.04s) | W1 "Nobody" closed/closed at audio onset, opens into the hold; W2 "man" open/open | RESCUE — swing-warp 1.44x (inside ≤1.75x envelope), head re-anchor |
| U37 | FC.9 "I'm The Nobody Man" | 3.10s | 4.00s | 1.290 | W1 "I'm" closed/closed (head lag); "the" transitional; "nobody"/"man" open | RESCUE — phrase-warp STRETCH 1.29x (0.775x speed, inside slow floor), head re-anchor |
| R14 | C1.7 "I'm The Nobody Man" | 2.88s | 2.26s | 0.785 (unchanged) | W1 closed/closed (head lag); W2–W4 open | RESCUE — swing-warp 1.27x, head re-anchor |
| R21A | PC2.1 "I kept clicking, kept sticking around" | 3.66s | 2.82s | 0.770 (unchanged) | W1 closed/closed (head lag); kept/clicking/around open or transitional at onset or +1; "sticking" closed at onset, parting at +1 (shares gesture with "kept" — the cramped-stamp pair, merged-anchor fix applies) | RESCUE — swing-warp 1.30x, head re-anchor, merged anchors |
| R18B | V2.2 "Half-mad thoughts and a stack of joins" | 3.20s | 2.08s | 0.650 (unchanged) | W1 "Half" closed/closed (head lag); W2–W8 open/transitional throughout | RESCUE — swing-warp 1.54x (inside envelope), head re-anchor |
| R20A | V2.5 "Everybody chasing that giant shout" | 3.10s | 2.32s | 0.748 (unchanged) | W1 "Everybody" closed at onset, wide open at +1 (opens inside its 1.42s hold — head re-anchor consumes the hold); W2–W5 open/transitional at onset or +1 | RESCUE — swing-warp 1.34x, head re-anchor |
| R20B | V2.6 "I got a small flame I won't put out" | 3.18s | 2.26s | 0.711 (unchanged) | Cleanest of the cluster: all 9 words open/transitional at onset or +1 ("won't" shows correct pursed-lip articulation); NO head problem | RESCUE — swing-warp 1.41x, no head fix needed |

- Part B totals: 8 units measured, **8 RESCUE, 0 KEEP-AS-IS, 0 STRUCTURAL.** Every required speed sits inside the proven envelope (max 1.54x) or, for the two slow takes (U02/U37), the stretch sits inside the 0.5x slow floor. All eight ride on the master gate at assembly.

### PART C — Rescue renders for the candidate cluster (NO generations)
Method: work/rebuild2_rescue/build_rescue5.py — run-2 swing/PCHIP method PLUS the two run-2 anchor fixes implemented: (a) line heads re-anchored on VISIBLE mouth events via a mouth-interior detector (first frame scoring visible mouth interior replaces word 1's audio onset as the first keyframe); (b) sub-0.1s song stamp pairs merged to single anchors. Mouth gate = crop grid at every song word onset + onset+1 frame (work/rebuild2_rescue/<take>_mouthgate.jpg); PASS only if every word is open/transitional at onset or +1. Renders + reports in work/rebuild2_rescue/<take>_rescue.mp4 / _rescue_report.json.

| Take | Line | Speedup | Head re-anchor | Mouth gate | Motion (mean diff / max near-dup run) | Disposition |
|---|---|---|---|---|---|---|
| R08B | PC1.2 | 1.676x | none needed (frame 0 open) | **PASS 7/7** — "little"(1st) closed at onset, open at +1; all other words open at onset or +1 | 2.30 / 1f | **RESCUE-CONFIRMED** |
| R16A | C1.Ta | 1.737x | +0.875s (mouth interior first scored at frame 21) | **FAIL** — "nobody" wide open at onset/+1, but "man" CLOSED at onset and +1 and still closed through +6 frames (opens at +7f ≈ 0.29s late; verified on extracted frames 25/27/29/31) | 2.87 / 1f | NOT confirmed — assembly fallback: per-word mouth-event re-anchor of "man" (slack exists: take holds "man" 1.74s vs song ~1.02s), master gate decides; if it fails there, STRUCTURAL |
| R16B | C1.Tb | 1.717x | detector claimed +0.708s — FALSE POSITIVE on the bowed head | **FAIL** — word 1 "nobody": head bowed down, cat-ear headphones ON HEAD, mouth NOT VISIBLE at onset or +1 (the run-2 visual flag, decisive on the render); "man" open/open | 3.38 / 1f | **STRUCTURAL** (montage + kinetic) — cannot be trimmed past the flag: the flag covers the head of word 1 itself |
| R05A | V1.1 (EDGE) | 1.893x | detector claimed frame 0 — FALSE POSITIVE (gate grid shows the frame-0 closed smile) | **FAIL** — word 1 "I" closed at onset AND +1 (the R08A closed-smile lead-in); words 2–7 all open/transitional at onset or +1 ("profile" shows correct /p/ transitional at +1; "pile" closed at onset, open at +1) | 2.69 / 1f | **STRUCTURAL** per edge rule (V1.1) — failure is the line head ONLY; assembly fallback: true visible-mouth head re-anchor (mouth opens ~0.3s into the take's 1.5s held "I", slack exists), master gate decides |
| R35 | FC.7 (EDGE) | 1.882x | none (frame 0 scored open — gate grid overrides: it is a closed smile) | **FAIL** — word 1 "I'm" closed at onset AND +1 (same closed-smile lead-in); words 2–4 pass ("the" open, "nobody" open with rounded-lip shape, "man" open) | 5.67 / 1f | **STRUCTURAL** per edge rule (FC.7) — failure is the line head ONLY; same head re-anchor fallback as R05A (take holds "I'm" 1.82s, slack exists), master gate decides |

- Detector lesson (for the re-cut run): the mouth-interior detector false-positives on closed smiles (R05A frame 0, R35 frame 0) and on bowed heads (R16B). The GATE GRID is the verdict, never the detector score. Both edge takes failed on exactly one word — the line head — which is the known, assembly-fixable artifact; they are STRUCTURAL by the edge rule as rendered, with the re-anchor fallback documented for the re-cut.
- Motion is clean on all five renders (mean diff 2.30–5.67, max near-dup run 1f everywhere) — no warp in this cluster reads frantic or frozen; the failures are mouth-state failures, not motion failures.

### Updated cumulative dispositions after run 5
- KEEP pool: unchanged this run (no new in-band take). Pool = R18A, R13A, R13B, R17A (trim laughing tail), R17B (trim late head), R22, R15 + the brief's in-band pool (U01t2, U03, U04, U07, U09, U10, U11, U12, U19t2, U23, U24t2, U25, U26, U27, U31, U33 bad-word note, U38, U39t2, U40 garble note).
- RESCUE-CONFIRMED (gate-passed renders on disk): R06b (1.64x, run 2), R08a (1.75x, run 2, with anchor fixes), **R08b (1.68x, run 5)**.
- RESCUE at assembly (grey path — swing/phrase warp + head re-anchor, master gate decides): U02 (stretch 1.38x/1.56x per phrase), U36 (1.44x), U37 (stretch 1.29x), R14 (1.27x), R21A (1.30x), R18B (1.54x), R20A (1.34x), R20B (1.41x), **R34A (FC.5 — stretch 1.30x, mouth check already PASS)**. Conditional: R16a (C1.Ta) per-word re-anchor attempt; R05a (V1.1) / R35 (FC.7) / R34B (FC.6, stretch 1.95x) attempts despite STRUCTURAL disposition.
- STRUCTURAL (beat-cut montage + kinetic words, disclosed): V1.1 (R05a, edge gate-fail — head only), V1.2 (R05b), V1.3 (R06a), PC2.2 (R21b), C1.Tb (R16b, head-bow), FC.1 (R32a), FC.2 (R32b), FC.6 (R34b, 1.95x too fast), FC.7 (R35, edge gate-fail — head only). Conditional: C1.Ta (R16a) joins this list if the assembly re-anchor attempt fails the master gate.
- Bridge U28–U30 montage by design (unchanged). Every brief clear-miss unit is now dispositioned; generation for rebuild-2 is CLOSED (26 re-fire takes, word accuracy 26/26 lines).

## Still owed after run 5 (for the re-cut coordinator — assembly ONLY, no more generations)
1. Mouth-event re-anchoring of the full keep/rescue pool: measure each take's VISIBLE mouth events (line heads first — 7 of 8 grey takes + both edge takes carry the closed-smile head artifact; R16a's "man" needs a per-word re-anchor; R34A/R34B heads trim at their RMS onsets 0.85s/0.95s), shift/warp phrases so mouth events land on song word onsets. Use the interval-speed table + merged sub-0.1s anchors, NOT raw PCHIP through cramped stamps (run-2 caveat). Phrase-smooth warps only; no slow past 0.5x; speedups disclosed. Trims: R17A laughing tail (line 0.0–2.36s only), R17B late head (onset 2.32s), R06a tail if used as texture. MEASUREMENT CAUTION: Whisper DTW stamps on takes with silent lead-ins are unreliable (run 5 Part A) — adjudicate every take's span against its RMS envelope + mouth frames before warping.
2. Re-cut onto the song grid (SONG_WORDS.json + beat grid 103.36 BPM): KEEP pool at natural pace with mouth-event anchors; RESCUE-CONFIRMED renders (R06b/R08a/R08b) regenerated inside the assembly warp pipeline with the same keyframes; grey-path RESCUE units (U02/U36/U37/R14/R21A/R18B/R20A/R20B/R34A) swing/phrase-warped at the Part B speeds; STRUCTURAL spans (V1.1*, V1.2, V1.3, PC2.2, C1.Tb, FC.1, FC.2, FC.6*, FC.7*) as beat-cut montage + kinetic words (* = re-anchor/stretch attempt first, montage if the master gate fails; C1.Ta same conditional path); bridge U28–U30 beat-cut montage with U31 returning to his face for B.6; U33 final-word bad-word cut; U40 garble handled per brief notes.
3. Kinetic HIGHLIGHT layer rebuilt from SONG_WORDS.json (assembly layer in post, as before).
4. Master gate (brief rule 5, stricter): mouth state at EVERY sung line onset — open/transitional at onset or +1 frame, no +0.33s allowance; frame count exact 4493; SEI crf=18.0 read from the delivered file; AAC probe; motion during words. Any closed line onset = fix that unit before delivery.
5. Deliverables: masters/mv7_im_the_nobody_man_16x9_rebuild2.mp4 (house CRF 18) + _50mb chat copy (AAC copied untouched), MV7_REBUILD2_NOTES.md (with all STRUCTURAL + speedup disclosures), MV7_REBUILD2_DELIVERED.flag, commit (explicit paths only), announce via ~/workspace/freeq/announce.sh.

---

## Re-cut run (2026-11-07) — assembly ONLY, generation closed

- STARTED: re-cut coordinator live. Work order = "Still owed after run 5" items 1–5 below (mouth-event re-anchoring → re-cut → kinetic HIGHLIGHT → master gate → deliverables). Progress appended incrementally; encodes run detached.
- PLAN (re-cut coordinator): per-LINE swing assembly (not per-unit uniform warp). Anchors = take word onsets shifted by a per-line VISIBLE-mouth lag measured from mouth-crop openness curves + visually verified on head strips; PCHIP warp per line with merged sub-0.1s song anchors; gaps/tails filled at natural speed from the governing take; STRUCTURAL lines = beat-cut montage from their own takes + kinetic words. Dispositions applied exactly per "Updated cumulative dispositions after run 5": KEEP natural (R18A/R13A/R13B/R17A/R17B/R22/R15 + U01t2/U03/U04/U07/U09/U10/U11/U12/U19t2/U23/U24t2/U25/U26/U27/U31/U38/U39t2/U40), RESCUE-CONFIRMED regenerated in-pipeline (R06b/R08a/R08b), grey RESCUE at run-5 speeds (U02/U36/U37/R14/R21A/R18B/R20A/R20B/R34A), CONDITIONAL attempts (R16a per-word "man" re-anchor, R05a head, R35 head, R34B 1.95x stretch), STRUCTURAL montage (V1.2, V1.3, PC2.2, C1.Tb, FC.1, FC.2 + failed conditionals), bridge U28–U30 montage, U31 face for B.6, U33 final-word bad-word cut.
- CONTINUATION (re-cut coordinator #2): prior coordinator died on transport error after writing the PLAN + work/rebuild2_recut/plan_data.py (adopted as-is). This run: measure per-line visible-mouth lags (openness curves + head strips) -> render per-line segments to work/rebuild2_recut/seg/ -> concat -> master gate -> final encode + kinetic + AAC -> 50mb copy -> notes/flag/commit/announce. Progress appended after every step; encodes detached.
- MEASUREMENT (continuation run): anchors.json written (all 67 lines sliced, ZERO slice errors) + head strips read for all 56 sung lines. Detector verdicts split three ways: (a) lags visually confirmed (C1.7 0.792, C1.Ta 0.875, PC2.1 0.917, C2.7 0.708, B.6 0.583, V2.5 0.375, PC2.3 0.375, PC2.4/C2.3 0.292, V2.2 0.25, V2.1 0.167, C2.5 0.125, C1.1 0.292); (b) mouth genuinely open at audio onset, lag~0 correct (I1b, I1d, C1.4, C1.Td, C2.2, C2.4, C2.8 [detector None -> set 0], FC.4, FC.5, FC.6, FC.Tb, FC.Td, V2.6); (c) FALSE POSITIVES — closed smile at claimed frame-0 event, true opening later (I1a, I1c, I2a, I2c, V1.1, V1.5, FC.3, FC.7, FC.8, FC.9, FC.10, FC.Ta, FC.Tc + small-lag ~frame-3 openings C1.2/C1.3/C1.5/C1.8). Fix path: rise-based re-detection on the openness curves for group (c), then master gate at full-res crops adjudicates every line; failed segments re-anchored individually.

### Re-cut continuation — mouth-event adjudication (visual, dense strips)
Detector lags (measure.py + fix_lags v1) PROVEN unreliable: closed lips score
~0.024 baseline in the fixed patch; RISE events overshoot visible openings by
0.2-1.0s; the earlier background curve dump was corrupt (discarded). ALL head
lags re-measured BY EYE from full-res dense strips (every 2nd frame, face crop
x30-62%/y26-60%): strips in work/rebuild2_recut/strips/dense/.
anchors.json verified 100% consistent with plan_data ASSIGN + T windows + chant
table (0 mismatches) — slices/takes/windows are sound.
VISUAL LAG TABLE (event frame/24, in build_segments.py LAG_OVERRIDE):
I1a .583 | I1c .083 | I2a .417 | I2c .583 | V1.1 .750 (R05A COND head WORKS) |
V1.4 .250 | V1.5 .250 | V1.6 0 (open at onset) | PC1.1 .667 | PC1.2 .083 |
PC1.3 .417 | PC1.4 .250 | C1.2 0 (teeth-grin at onset; gate scrutiny) |
C1.3 .083 | C1.4 +.167 (mouth CLOSES at onset, reopens +4f — detector -0.068 was
the previous line's tail) | C1.5 .333 | C1.6 .250 | C1.8 .417 (detector .917
overshot) | C2.1 .333 | C2.6 0 (open at onset, full-res confirmed) |
C1.Ta per-word {Nobody .500, man .250} (man closes for /m/ at audio onset, opens
+6f; anchor the opening — run-5 fallback, visually grounded) |
FC.3 .500 | FC.5 0 (RMS slice) | FC.6 0 | FC.7 .583 (R35 COND head WORKS) |
FC.8 .750 | FC.9 .417 | FC.10 .167 | FC.Ta .500 | FC.Tc .500.
Batch-2 dense strips (C1.1/C1.7/V2.1/V2.2/V2.5/PC2.1/PC2.3/PC2.4/C2.3/C2.5/C2.7/
B.6/I1b/I1d/I2b/C2.2/C2.4/C2.8/FC.4/FC.Tb/FC.Td/C1.Tc/C1.Td/V2.3/V2.4) rendered
next; then build_segments.py runs all 67 lines + OUTRO.
Builder: per-line PCHIP swing, lag-shifted anchors, sub-0.1s merges, natural
head/tail fill, frame-exact tiling to 4493; FC.4 truncated final "man" ->
beat-cut montage from its song onset (bad-word rule, implemented).
Batch-2 dense verdicts (relative lags): C1.1 .167 | C1.7 .167 (detector .792
overshot 0.6s) | PC2.1 .417 | C2.7 .333 | B.6 .583 | V2.5 .333 | PC2.3 .417 |
PC2.4 .250 | C2.3 .333 | V2.2 .333 | V2.1 .167 | C2.5 .083 | second-line heads:
I1b/I1d/I2b/C2.2/C2.8/FC.Tb/FC.Td/C1.Td/V2.3/V2.4 all OPEN at onset (0) |
C2.4 +.167 (closes at onset, reopens +4f — same trap as C1.4) | FC.4 0 (open at
onset; later anchor would land the closed frame on it) | C1.Tc .333.
ALL 56 sung lines now carry eye-read lags in build_segments.py LAG_OVERRIDE.
Builder run next: 68 segments (67 lines + OUTRO), then concat + gate.

### Re-cut continuation (post-checkpoint, ~10:3x EST 2026-11-07)
- Segment build COMPLETE: 68 segments, total frames exactly 4493. Kinds: 39 KEEP / 13 RESCUE / 4 COND / 11 MONTAGE / 1 OUTRO.
- BUG FOUND + FIXED: C1.Tc anchors slice contained R17A's laughing tail (ASR words "Heh." 4.32s, "Hehehehehehe." 7.1–8.5s); first/last pairing warped the whole take incl. laughter into the line at uniform 4.315x. Slice trimmed to words 0–1 (Nobody 0.0–1.28, man! 1.28–2.36) per run-3 disposition; segment re-rendered selective (builder argv filter) → uniform 1.198x; manifest entry merged back (builder's selective mode rewrites the manifest with only the re-rendered entries — backed up + merged, totals re-verified 4493/68). Slice audit across all 67 lines: C1.Tc was the ONLY non-benign extra-words case (others: chant splits by design, half-mad / low-lit ASR splits, FC.Td word-2-only by design, STRUCT/MONTAGE empty by design).
- Speed extrema in build.log are analytic PCHIP derivative samples (1/deriv at fine tsamp) — spikes (e.g. PC2.1 314x) sit at compressed anchor pairs / lead-ins and are bounded by frame sampling in the render; sustained-slow risk is adjudicated by the gate's near-dup scan on the concat, not the derivative log.

### Re-cut continuation #2 (post-checkpoint, ~10:1x EST) — GATE v1 ADJUDICATED
- Gate sweep COMPLETE on candidate_v1 (all 10 sheets eye-read; grids are the verdict): 53/56 line onsets open/transitional at onset or +1. Passes at +1 only: I1c, I2b, PC1.2, C1.3, V2.5. C2.4 = weakest pass (transitional pout at onset, opening +1 onward, verified on seg frames 0-7). COND V1.1 PASS (parted at onset, wide at +1 — R05A head re-anchor WORKS, V1.1 stays sung). COND FC.7 PASS (parted at onset, wide at +1 — R35 head WORKS, FC.7 stays sung).
- FAIL 1 — C1.Ta (COND): candidate onset f1627 + f1628 both sealed closed smile; visible parting starts f1629, open f1630 (diag/cand_c1ta.jpg). Take R16A strip: parting at take f14-15 (0.583-0.625s), not f12. FIX ALREADY IN build_segments.py (pre-death edit, WORD_LAG_OVERRIDE C1.Ta word-0 lag 0.625) — segments were rendered BEFORE the edit (manifest still shows anchor 0.5). Re-render owed.
- FAIL 2 — FC.6 (COND): candidate onset f3730 through f3734 sealed/flat; parting ~f3735 (diag/cand_fc6.jpg). Take R34B strip: /f/ closure at the 0.95 RMS onset, visible opening at take f27 (1.125s). FIX ALREADY IN build_segments.py (WORD_LAG_OVERRIDE FC.6 {0: 0.167}). Re-render owed.
- FAIL 3 — B.6 TAIL FREEZE (motion gate): B.6 warp b=141.44 but segment window runs to FC.1 start 143.40 -> np.interp clamps to the take's last frame: 46-frame near-dup run, global f3395-3441 (gate_meta), visually confirmed frozen closed-smile frame across seg/B.6.mp4 local f107-153. Span 141.62-143.42 = ASR-heard pickup "to the one bright light" (sheet/kinetic show an instrumental gap; montage is legitimate under both readings). FIX: FC.4-style beat-cut montage tail from 141.62 from U31's own take (generalizing the builder's badword_montage mechanism) + keep the sung warp through "on" (141.44).
- Fixes queued: builder edit for B.6 tail montage; selective re-render C1.Ta + FC.6 + B.6 (manifest backed up to seg_manifest_v1_full.json first); re-concat candidate_v2; re-gate changed lines + full freeze scan.

### Re-cut continuation #2 — GATE v2 (candidate_v2) VERDICT
- Selective re-render done (C1.Ta 49f / B.6 154f / FC.6 58f); manifest merged back (68 entries, 4493f, contiguous; backups seg_manifest_v1_full.json + seg_manifest_pre_gatefix.json). candidate_v2.mp4 = concat copy, 4493f.
- C1.Ta FIXED: onset f1627 now parted/open, +1 wider — PASS (lag 0.625 word-0 anchor works; C1.Ta stays a SUNG take, no montage fallback needed).
- FC.6 FIXED: onset f3730 now open mid-articulation, +1 open — PASS (0.167 word-0 lag on the /f/ opening; FC.6 stays sung at the 1.95x stretch).
- B.6 tail FIXED: montage chunks moving (window mean diff 3.99, no >=24f run remains in 141.0-143.6).
- Full re-gate: total frames 4493 exact; longest near-dup run now 43f at global 426-469 = I2c held chant tail. ADJUDICATED PASS: seg/I2c.mp4 per-frame diffs 0.11-0.56, NEVER 0.00 (no identical-frame freeze; natural U04 tail, pose drifts visibly across 6f-spaced tiles) under the intro chant's held final "man" (sung end 18.74 per unit table) + post-line hold. Disclosed in NOTES.
- MASTER GATE: 56/56 line onsets open/transitional at onset or +1 frame. GATE CLOSED. Proceeding to final encode (kinetic composite + track.mp3 as AAC, CRF 18) + 50MB copy + notes/flag/commit/announce.

### Re-cut continuation #2 — DELIVERED (2026-11-07 ~10:3x EST)
- Final encode: candidate_v2 + rebuild2_kinetic.ass + track.mp3 (AAC 48kHz 192k) -> masters/mv7_im_the_nobody_man_16x9_rebuild2.mp4. VERIFIED from the delivered file: 4493 frames exact, 187.208s, x264 SEI crf=18.0, AAC stereo 48kHz, faststart, 79,561,001 B, md5 36176f04c349ad05e2f456e129392b80.
- Chat copy: masters/mv7_im_the_nobody_man_16x9_rebuild2_50mb.mp4 — 48,037,794 B (<=50,000,000), 4493f, AAC bit-identical to master (audio stream md5 b936ed73be63909db13d301cf5c88b29 both), md5 cc8b98adca40f45ea434d0541fcd1b66.
- MV7_REBUILD2_NOTES.md written (6 STRUCTURAL lines + bridge montage + FC.4 bad-word span + B.6 tail disclosed; all 4 COND attempts passed and stayed sung; every rescue speedup/stretch listed). MV7_REBUILD2_DELIVERED.flag created. REBUILD-2 COMPLETE — awaiting the user's playback verdict.
