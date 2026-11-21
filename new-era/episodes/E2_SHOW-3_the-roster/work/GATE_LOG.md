# GATE_LOG — SHOW-3 'THE ROSTER', E2 "The Pass, Done Properly"

Production: v2 stack (Panel Workflow Spec v2 + Joint Gate + Method C + BLAM Gate).
Script: SCRIPT.md (locked). Format target: 6×10s units, ONE 16:9 master 1280×720, 24fps, 1440f, CRF 18, AAC, faststart, "~ WuBu ~" corner bug.

## Winning vehicle formula (measured across this build)
Single PEAK panel as the only image anchor + dialogue LAST in the text entry + brisk/no-gap pacing + the final two speeches merged into one prompt block when the cliff is a lone name. Two-image journeys truncated dialogue (U1 t1–t5: 3 speeches max). A pronunciation hint fixed a recurring mispronunciation ("Conceded", U4). Lone-name cliffs spoken by an IN-SCENE voice land (U3 "Hale.", U4 "Keeper."); a lone UNFAMILIAR name from a DISEMBODIED voice never landed (U2 "Okonkwo.", 7 fires).

## U1 — envelope / WREN (Keeper + UNC) — SHIPS: takes/U1_t8.mp4
- Fires: t1,t2 (two-image journey) dialogue FAIL; t3,t4,t5 dialogue FAIL (3 speeches); t6 4 speeches, 4th compressed; t7 speaker labels leaked into speech; U1A (5s test) duration steering ignored, 2 speeches late; **t8 PASS**.
- Dialogue (t8, ASR): all 5 speeches, words exact — 1.84 "Read it again, UNC. From Wren." / 4.18 "Your envelope stayed sealed, Keeper." / 5.96 "I never broke that seal myself." / 7.56 "Wren, as written, keeper, Vasquez." (speeches 4+5 delivered as one continuous final speech; every scripted word present, in order; cliff word VASQUEZ is the last word, ends 9.84s).
- Wordmark: PASS — zoom reads exactly "~ WuBu ~" (5.0s, 7.5s, 9.5s).
- BLAM (take level): A1 t50 0.2 / t90 0.2 PASS · A2 0.0 PASS · A3 head −6.9 dB vs median (bar −6.0) MARGINAL — accent clause applies (envelope slap ≤0.5s, t50 0.2s); master carries a planted accent + loudness pass, re-measured at master · A4 5 vs 7 PASS · V1 11.47 PASS · V2 first bucket 14.14 PASS · E1 impact = envelope landing, frame 0–0.5s PASS.
- Flaws: Keeper reads ~60, full grey hair vs CHAR late-30s greying temples (recurs in every U1 candidate); the room resolves to a roster-board office, not the gothic stone room of the WORLD panel; the big WREN envelope becomes a small orange card by the tail (prop drift inside the take); frame 0 is the envelope already landing rather than the PEAK's mid-rotation pose (impact reads, accepted).
- Conform: work/seg1.mp4, 240f. Joint frame: panels/PNL-JOINT-U1.png (seg1 f228, md5 693d97d7b434473c8c9c75287df7b59f). Tail MAE settles from ~f196 (two-shot talking heads) — joint eye-check item "upstream tail settled" NOTED for J1.

## U2 — glass / VASQUEZ (Keeper + UNC, Dispatcher cliff) — SHIPS WITH TWO DISCLOSED DEVIATIONS: takes/U2_t3.mp4
- Fires: t1 speeches 1–3; t2 speeches 1–4 (ends 9.92s); t3 speeches 1–4 (ends 9.48s); t4 speeches 1,2,4; t5 speeches 1–3; t6 speeches 1–4 (Dispatcher appeared in doorway but did not speak; world broke to a fluorescent office); t7 (wordmark refire) wordmark CLEAN but speech 4 lost its leading "Vasquez."
- Dialogue (t3, ASR): speeches 1–4 words exact — "Why does her shift still run, UNC?" / "Spoken names stay kept. Erasure un-keeps, keeper." / "Then her shift never ends." / "Vasquez, kept still running, keeper."
- DEVIATION 1 (dialogue): the cliff word "Okonkwo." (Dispatcher, building speaker) is NOT spoken at U2's tail in ANY of 7 fires — systematic generator failure on a lone unfamiliar name from a disembodied/new voice (also failed twice with the Dispatcher visible in the doorway). Chain compensation: U3 opens on OKONKWO written on the entry card AND the Dispatcher's first U3 line speaks "Okonkwo." as its first word (landed, U3_t1 0.52s). The pass order and the written-name chain are intact; the U2 tail beat is silent.
- DEVIATION 2 (wordmark): t3's hoodie reads "~ W'uBu ~" — a small apostrophe-like tick after the W, consistent at 5.0s and 9.5s zooms. The one allowed refire (t7) fixed the wordmark but broke speech 4 (dropped "Vasquez."). No candidate passes both gates; t3 was shipped because the script-verbatim gate (a whole scripted name missing) outweighs a punctuation tick in the lettering. FLAGGED for the delivery decision.
- Visuals (t3): frame 0 = VASQUEZ huge on fogged glass (PEAK true); wide two-shot, both men flanking the glass door, VASQUEZ on the glass between them; palette warmer/redder than U1.
- Conform: work/seg2.mp4, 240f. Joint frame: panels/PNL-JOINT-U2.png (seg2 f228, md5 dfcc2630d009b35d4287d32e2b50632a).

## U3 — card / OKONKWO (Dispatcher + Keeper) — SHIPS: takes/U3_t1.mp4 (first fire)
- Dialogue (ASR): all 5 speeches — 0.52 "Okonkwo. This entry bears your hand, Keeper." / 3.52 "I wrote nothing while gone, dispatcher." / 6.10 "Logged while you were gone, Keeper." (full-take ASR read "Keeperer"; amplified slice hand-check reads "Keeper." clean — PASS) / 7.72 "I never wrote that entry." / 9.16 "Hail!" = the cliff "Hale." — homophone (Hale is pronounced exactly as "hail"); PASS by hand-check, written HALE appears on the palm in U4.
- F-004 FIRED in-scene. Rack clock visible behind the Keeper (motif present).
- Visuals: frame 0 = PEAK replica (card up, OKONKWO legible); Dispatcher and Keeper both on-CHAR; warm palette consistent with U2.
- Conform: work/seg3.mp4, 240f. Joint frame: panels/PNL-JOINT-U3.png (seg3 f228, md5 4d62e7d575e3e4c2f504d62b49735fda).

## U4 — palm / HALE (Keeper + UNC) — SHIPS: takes/U4_t5.mp4
- Fires: t1 speeches 1–2 + fragment; t2 speeches 1–4 but "Conceded" misdelivered ("Conceased", confirmed on amplified slice) and cliff missing; t3 speeches 1–4, "Conceded"→"Conceited", cliff missing; t4 speeches 1–3, "Concede"; **t5 PASS** (pronunciation hint + merged final block).
- Dialogue (t5, ASR): all 5 speeches, words exact — 0.0 "Look, UNC. Hale crossed my palm." / 2.6 "Hale's roster entry, your hand, tonight." / 5.42 "Conceded, UNC, one answer out of order." / 7.58 "Hale, an answer owed, keeper." / 9.56 "Keeper." (cliff, KEEPER spoken by UNC — the OWES beat F-017 born in dialogue).
- Wordmark: PASS — "~ WuBu ~" exact at 5.0s and 9.5s.
- Visuals: frame 0 = PEAK replica (palm, HALE legible); two-shot across the desk, roster boards behind.
- Conform: work/seg4.mp4, 240f. Joint frame: panels/PNL-JOINT-U4.png (seg4 f228, md5 11a4b52b9321ec182c655bcd7b8486ad).

## U5 — ribbon / KEEPER (Laura + Keeper) — SHIPS: takes/U5_t4.mp4 (recovery session)
- Re-anchor unit (J7 / ROT-B): PEAK-U5 built fresh from PNL-JOINT-U4 + CHAR-LAURA + CHAR-KEEPER (md5 e7ef287a4b9d131634eb3b8c0084242d); fired single-anchor on the CHAR-derived PEAK (the proven dialogue formula; the identity refresh is baked into the PEAK itself).
- t1: speeches 1–3 exact (F-012 "What did you leave here, Keeper?" verbatim ✓), speeches 4–5 missing (slow pacing).
- t2 (fired 17:35 EST by the first coordinator, never evaluated; evaluated by the recovery): speeches 1–3 exact, speech 4 STARTS at 9.20s and is truncated by the 10s wall ("Didn't my hand…" — "stay, Laura?" cut), speech 5 + cliff WREN absent. Dialogue FAIL. Visuals clean (frame 0 = PEAK replica; identities hold throughout).
- t3 (recovery): speeches 1–4 complete (0.0–9.46s), speech 5 + cliff absent — the merged final block did not survive; the generator re-inserted a ~0.8s pause before speech 4 and ran out of take. Dialogue FAIL.
- t4 (recovery): the Keeper's final three beats folded into ONE unbroken quoted rush ("Didn't my hand stay, Laura? It wrote Okonkwo and Hale, Laura. Wren.") + an explicit NO-pauses-anywhere instruction. **PASS.**
- Dialogue (t4, ASR): all 5 speeches + cliff, words exact, in order — 0.00 "Keeper, looped on this ribbon." / 3.60 "Mine, Laura." / 4.80 "What did you leave here, Keeper?" (F-012 verbatim ✓) / 6.48 "Didn't my hand stay, Laura?" / 7.86 "It wrote Okonkwo and Hale, Laura." / 9.74 "Wren." (cliff, wrapping the pass). Two ASR artifacts cleared by amplified-slice hand-checks (the build's own method): full-take "Oconquo" (p=0.78) reads "Okonkwo" clean on the +14 dB slice (work/asr_u5t4_slices.log); the cliff reads "Ren" — Wren is pronounced /rɛn/, a homophone PASS on the U3 "Hail!"="Hale." precedent.
- Visuals (t4): frame 0 = PEAK replica (Laura + Keeper over the open roster, KEEPER ribbon legible); tail = tight two-shot, Laura holding her gaze on the Keeper (the scripted non-acceptance reaction), Keeper mid-speech at the cliff. Identities hold vs PEAK/CHAR throughout. No UNC in this unit → no wordmark read.
- Flaw (build-recurring, already disclosed at U1): the Keeper reads older than the CHAR late-30s greying temples.
- Conform: work/seg5.mp4, 240f. Joint frame: panels/PNL-JOINT-U5.png (seg5 f228, md5 4be92bde29bc70f82e8f5de0da591500). Tail scan (measure.py): median MAE 3.04; final-15% MAE below median (settled talking two-shot; the cliff word lands at 9.74s, so the final 12 f carry speech motion) — read at J5 on the master.

## U6 — verso / WREN wrap + LAURA entered (Keeper + UNC + Dispatcher) — SHIPS: takes/U6_t1.mp4 (first fire, recovery session)
- Chain call (J3b): slot 1 = PNL-JOINT-U5, slot 2 = derived PEAK-U6 (built by the recovery from PNL-JOINT-U5 + PNL-PROP-roster-page, md5 941b4856096fc71fc3d46fc910662bdf — the Keeper holding the roster page up to the lamp, all five names showing through reversed, WREN at top in visibly fresher ink, KEEPER circled; UNC at the left edge; the Dispatcher at her log).
- Dialogue (ASR): all 5 beats, words exact, in order — 1.00 "Lamp up, UNC." / 2.92 "Fresh ink retraces Wren." / 4.98 "Read it again, UNC. I'm listening." / 7.80 "Wren." (UNC, the pass completed) / 8.50 "Entering Laura, new name." (Dispatcher — the episode cliff, E2-P4 PLANTED). 18/18 words.
- DEVIATION (staging, disclosed): the scripted SILENCE BEAT is 2.5s; the take holds 1.02s of silence between "…listening." (ends 6.78s) and "Wren." (7.80s). The beat exists and reads (lamp held, no hand on the page) but is compressed to ~40% of spec. Shipped rather than refired: the full five-beat landing incl. the third-voice cliff is the rare event in this build (cf. U2's cliff, 0-for-7), and the deviation is duration of a pause, not a word. The "Wren." → Dispatcher gap is 0.14s (one ASR segment); voice attribution of "Wren." is not ASR-verifiable, and the Dispatcher's own delivery is confirmed visually at 9.5s (pen on log, mid-line). Nothing contradicts UNC speaking the wrap word.
- Wordmark: PASS — zoom at 5.0s reads exactly "~ WuBu ~" (blackletter face, glyphs exact: tilde W u B u tilde), UNC small/shadowed at the frame edge per the law. At 9.5s UNC's chest is out of frame (profile foreground), so the 5.0s read is the unit's only read.
- Visuals: frame 0 continues the U5 tail two-shot (chain opening true); by 5.0s the composition matches PEAK-U6 (page raised to the lamp, five names reversed through the sheet, Dispatcher at her log with pen in hand); the tail beat lands — Laura caught at the lamp's edge is not separately framed, but the Dispatcher ENTERING the name is on screen, writing, as she speaks the cliff. Identities hold vs CHAR (Dispatcher exact vs her sheet; UNC exact; Keeper build-consistent).
- Conform: work/seg6.mp4, 240f. Joint frame: panels/PNL-JOINT-U6.png (seg6 f228, md5 340ed1282eebbd790e4ab928b417a45c) — harvested for the calibration record; U6 is the terminal unit.

## Assembly + master verification (recovery session, 2026-11-15)
- ONE assembly pass: six segments (240f each) → concat demuxer →
  work/joined.mp4, probed BEFORE the master encode: **1440 video
  frames** (segment sum exact; container 60.13s = accumulated AAC
  priming, handled at the encode per the pilot finisher's method).
- Master encode (single uninterrupted pass): joined + "~ WuBu ~"
  corner bug (drawtext, Noto Sans Bold 22px, yellow-gold 0xFFD24A,
  bottom-right) + planted accent + loudness pass; video timeline
  regenerated (setpts=N/(24*TB)), audio trimmed to the picture
  window (atrim 0:60).
  - Planted accent (the U1 entry's prescription): a designed
    paper-slap transient at 0.30s, fused onto the source slap
    (source peak 0.325s / −0.8 dBFS in the joined decode) —
    bandpassed noise burst (500–4000 Hz, τ≈45ms) + 120 Hz thump +
    a decaying paper-settle tail (900–3000 Hz, τ≈160ms), peak
    −6.2 dBFS, work/accent.wav.
  - Loudness pass: +3 dB fixed gain + limiter (0.89) — master
    median −23.0 dBFS (joined was −25.9; the pilot masters sat at
    −29…−38, so this master is the hottest of the set, out of the
    basement the BLAM audit flagged).
- Master: masters/e2_show3_the-roster_16x9.mp4 — md5
  7001e7625173b39d9af92788f05264b4, 16,914,730 B. Probe: 1280×720,
  24fps, **1440 frames, video duration exactly 60.000s**, audio
  duration exactly 60.000s, x264 SEI crf=18.0 verified, AAC 48k
  mono, faststart (moov at byte 36, before mdat). ≤50 MB, so no
  separate chat copy — the house master is itself chat-sized.
- Eye pass (work/frames/MASTER_*.png): frame 0 = the sealed WREN
  envelope in the Keeper's hands over the closed roster (the
  script's first-second doctrine frame, legible sound-off); the
  name state is visible at every joint (see Joint Gate); the
  final frame holds on the Dispatcher writing the LAURA entry in
  her log, UNC in profile, the circled KEEPER page behind. Bug
  legible bottom-right throughout; no captions anywhere.

## BLAM GATE — measured on the finished master (measure.py)
- A1 onset: t50 0.3s / t90 0.3s — PASS (bars 0.5 / 1.5).
- A2 dead head: 0.0s — PASS (bar ≤0.2).
- A3 head level: numeric branch −8.1 dB (head −31.1 vs median
  −23.0; bar ≥ −6.0) — **PASS BY THE ACCENT CLAUSE**: a designed
  accent transient is placed at 0.30s ≤ 0.5s, locked to the
  envelope-landing impact frame, exactly the alternative the gate
  text allows and the remedy the U1 take entry prescribed. The
  numeric shortfall is disclosed, not hidden: five of the first
  ten 100ms windows are pre-speech room tone, which no
  proportionate single accent can lift to the median without
  becoming a sound effect in its own right.
- A4 crackle: head HF bursts 4 vs control 9 — PASS (bar ≤2×).
- V1 opening motion: 0–0.5s MAE 12.75 vs 3–10s baseline 1.12,
  ratio 11.38 — PASS (bar ≥0.6×).
- V2 no ramp: first bucket 14.06 ≥ 50% of strongest (16.07) —
  PASS.
- E1 impact ≤1.0s: the envelope landing (frame 0 hands/envelope
  already in motion; slap peak 0.325s with the planted accent on
  the same frame) — PASS.

## JOINT GATE — measured on the assembled master (§6; J16 calibration log)
Artefacts: work/qc/JOINT_J1..J5_strip.png (12-frame strips,
cut−6…cut+5). BASE (95th pct of in-unit adjacent-frame MAE,
sampled every 24f excl. 12f at unit edges) = **6.74**.
Class: all five JOINT (J5 is the J7 re-anchor's downstream side;
J4 is the re-anchor boundary itself).

| Joint | Seam MAE (bar ≤58) | Tail MAE (final 12f) | Head MAE (0–0.5s) | Eye 1–5 | Verdict |
|---|---|---|---|---|---|
| J1 U1→U2 | 21.10 PASS | 0.64 | 3.10 | ✓ (item 4: direction ✓, palette warms — carried from U2's entry) | PASS, item 6 conditional |
| J2 U2→U3 | 21.64 PASS | 0.37 | 0.88 | ✓ | PASS, item 6 conditional |
| J3 U3→U4 | 30.42 PASS | 2.50 | 1.44 | ✓ | PASS |
| J4 U4→U5 | 24.26 PASS | 0.25 | 2.06 | ✓ (item 5 read as the declared J7 re-anchor reframing) | PASS, item 6 conditional |
| J5 U5→U6 | 9.23 PASS | 1.24 | 4.23 | ✓ (item 3: the page-lift completes inside the 2s allowance) | PASS |

- Eye checklist detail: (1) identity holds at every seam vs the
  CHAR panels (Dispatcher and Laura exact; Keeper/UNC
  build-consistent); (2) wardrobe unchanged; (3) the name-chain
  carry is visible at every downstream head — VASQUEZ on the
  glass (J1), OKONKWO on the card (J2), HALE on the palm (J3),
  KEEPER on the ribbon (J4), the raised verso page (J5, completes
  ~2s in); (4) light direction consistent (lamp left/high)
  throughout; (5) shared-subject jump < ⅓ frame at J1/J2/J3/J5.
- **J1 open eye-check item RESOLVED:** "upstream tail settled" is
  CONFIRMED numerically — U1's final-12f MAE is 0.64 (two-shot
  talking heads at rest; the cliff word lands at 9.84s but the
  picture is settled). It is logged, not fixed: the seam itself
  measures 21.10 (PASS with 2.7× headroom) and the downstream
  head is alive (the condensation drip descends through U2's
  opening frames).
- **Item 6 (motion alive) — the episode's J16 calibration
  finding:** the PROPOSED downstream head-MAE floor (≥8) is met
  at NO joint (0.88–4.23), and three upstream tails are
  near-settled (0.25–0.64). BUT visible motion exists on both
  sides of every cut — speech mouths (J5 tail/head), the
  descending drip (J1 head), the card raise (J2 head), the
  Dispatcher's head-turn (J3 tail) and the opening palm (J3
  head) — nothing is a frozen frame, and this episode's own
  BASE (6.74) sits BELOW the proposed floor: the floor exceeds
  the 95th percentile of all in-unit motion this show generates,
  so no head this show could produce would pass it. Read as
  CONDITIONAL PASS on the visible-motion criterion, with the
  numeric shortfall recorded here as calibration data for the
  §6 re-basing (J16). The binding numeric bar (seam MAE ≤58)
  passes at every joint with 1.9–6.3× headroom.

## Flaws carried to delivery (complete list)
1. U2 DEVIATION 1: the cliff word "Okonkwo." is never spoken at
   U2's tail (0-for-7 fires, systematic); compensated in-scene —
   U3 opens on OKONKWO written on the card and spoken as its
   first word. The pass order and the written chain are intact.
2. U2 DEVIATION 2: U2's shipped take reads "~ W'uBu ~" (a tick
   after the W). The wordmark-clean refire dropped a scripted
   name; the script-verbatim gate was judged to outweigh the
   tick. FLAGGED for the delivery decision.
3. U6: the scripted 2.5s silence beat is held for 1.02s
   (measured). All 18 words verbatim; the beat reads but is
   compressed.
4. JOINT GATE item 6: proposed head-MAE floor (≥8) unmet at all
   five joints; tails near-settled at J1/J2/J4. Seam MAEs pass
   with headroom; visible motion present at every cut. Filed as
   J16 calibration data (episode BASE 6.74 < the floor itself).
5. BLAM A3 passes by the accent clause; the numeric branch
   reads −8.1 dB (bar −6.0), disclosed above.
6. Build-recurring: the Keeper reads older than his CHAR sheet
   (late-30s) in U1 and U5; U1's room resolves to a roster-board
   office rather than the WORLD panel's gothic stone; U1's big
   WREN envelope becomes a small orange card by its tail (prop
   drift inside the shipped take).
