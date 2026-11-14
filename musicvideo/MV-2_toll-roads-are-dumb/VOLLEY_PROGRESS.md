# MV-2 volley progress

Track: MV-2 "Toll Roads Are Dumb" (THE VOICE), 268.01s, 27 scenes.
Volley cap: at most 6 videos per user message. Volleys fire only on the
user's short message (or tap) — never from a cron job.

## Volley 1 — FIRED 2026-11-01 (user message "Fire volley 1")

- Fired scenes: S01, S02, S03, S04, S05, S06 (t1 takes, see TAKE_HISTORY.md).
- Active takes: mv2_s01_t1 … mv2_s06_t1 (all 1280x720, 10.000s).
- Flagged scenes: S03 (TEXT — legible STOP signs), S05 (TEXT —
  legible STOP signs). Reroll axis for both: text.
- Style note: volley 1 renders PHOTOREALISTIC live-action, not the flat
  cartoon style the vehicles specify. Volley 2 (below) renders flat
  cartoon. The two volleys do not match; see "Style break" below.

## Volley 2 — FIRED 2026-11-01 (user message "Fire volley 2, keep the flags")

- Fired scenes: S07, S08, S09, S10, S11, S12 (t1 takes, see TAKE_HISTORY.md).
- Active takes: mv2_s07_t1 … mv2_s12_t1 (all 1280x720, 24fps, 10.000s).
- Flagged scenes: S11 (TEXT — partial painted road letters bottom-right
  of the 3s frame). Reroll axis: text.
- Style: volley 2 renders FLAT CARTOON illustration (flat fills, ink
  outline) — the vehicle style axis hit, unlike volley 1.

## Style break (open decision)

- Volley 1 (photoreal) and volley 2 (flat cartoon) will visibly clash at
  the 60s joint unless volley 1 is re-fired with the strengthened flat
  style wording used for volley 2. A flat re-fire of volley 1 (6 videos,
  one user message) would also give S03/S05 a clean shot at the text gate.
- Standing flags: S03, S05 (volley 1 TEXT), S11 (volley 2 TEXT) — all
  awaiting a reroll call. S03/S05 rerolls were deferred by the user's
  "keep the flags" choice on volley 2.

## Volley 3 — FIRED 2026-11-01 (user message "Fire volley 3")

- Fired scenes: S13, S14, S15, S16, S17, S18 (t1 takes, see TAKE_HISTORY.md).
- Active takes: mv2_s13_t1 … mv2_s18_t1 (all 1280x720, 24fps, 10.000s).
- Flagged scenes: S15 (TEXT — five legible STOP signs), S17 (TEXT —
  "THE VOICE" lettering on gantry signs, confirmed across 3s/6s/8s frames).
  Reroll axis for both: text.
- Style: flat cartoon throughout, matching volley 2.

## Style break (open decision)

- Volley 1 (photoreal) and volleys 2–3 (flat cartoon) will visibly clash
  at the 60s joint unless volley 1 is re-fired with the strengthened flat
  style wording used for volleys 2–3. A flat re-fire of volley 1 (6 videos,
  one user message) would also give S03/S05 a clean shot at the text gate.
- Standing flags: S03, S05 (volley 1 TEXT), S11 (volley 2 TEXT), S15, S17
  (volley 3 TEXT) — all awaiting a reroll call. S03/S05 rerolls were
  deferred by the user's "keep the flags" choice on volley 2.

## Volley 4 — FIRED 2026-11-01 (user message "Fire volley 4")

- Fired scenes: S19, S20, S21, S22, S23, S24 (t1 takes, see TAKE_HISTORY.md).
- Active takes: mv2_s19_t1 … mv2_s24_t1 (all 1280x720, 24fps, 10.000s).
- Flagged scenes: none. All six pass frame-check; no legible text in any
  3s frame. Standing flags unchanged: S03, S05, S11, S15, S17.
- Style: flat cartoon throughout, matching volleys 2–3.

## Style break (open decision)

- Volley 1 (photoreal) and volleys 2–4 (flat cartoon) will visibly clash
  at the 60s joint unless volley 1 is re-fired with the strengthened flat
  style wording used for volleys 2–4. A flat re-fire of volley 1 (6 videos,
  one user message) would also give S03/S05 a clean shot at the text gate.
- Standing flags: S03, S05 (volley 1 TEXT), S11 (volley 2 TEXT), S15, S17
  (volley 3 TEXT) — all awaiting a reroll call. S03/S05 rerolls were
  deferred by the user's "keep the flags" choice on volley 2.

## Volley 5 — FIRED 2026-11-01 (user message "Fire volley 5")

- Fired scenes: S25, S26, S27 (t1 takes, see TAKE_HISTORY.md). S26's
  first fire call hit a tool-loading error and was retried cleanly in
  the same message — no extra video spent.
- Active takes: mv2_s25_t1 … mv2_s27_t1 (all 1280x720, 24fps, 10.000s).
- Flagged scenes: none. All three pass frame-check; no legible text in
  any 3s frame. Standing flags unchanged: S03, S05, S11, S15, S17.
- Style: flat cartoon throughout, matching volleys 2–4.
- ALL 27 SCENES NOW FIRED (S01–S27 t1 takes).

## Style break (open decision)

- Volley 1 (photoreal) and volleys 2–5 (flat cartoon) will visibly clash
  at the 60s joint unless volley 1 is re-fired with the strengthened flat
  style wording used for volleys 2–5. A flat re-fire of volley 1 (6 videos,
  one user message) would also give S03/S05 a clean shot at the text gate.
- Standing flags: S03, S05 (volley 1 TEXT), S11 (volley 2 TEXT), S15, S17
  (volley 3 TEXT) — all awaiting a reroll call. S03/S05 rerolls were
  deferred by the user's "keep the flags" choice on volley 2.

## Volley 1 flat re-fire — FIRED 2026-11-01 (user message "Re-fire volley 1 in flat style")

- Fired scenes: S01–S06 t2 takes from v2 vehicles (same scene specs,
  STYLE replaced with the strengthened flat wording, blank-panel sentence
  added to TEXT). Vehicles at mv2_s0N_vehicle_v2.txt.
- Active takes: mv2_s01_t2 … mv2_s06_t2 (all 1280x720, 24fps, 10.000s).
- STYLE BREAK CLOSED: the full 27-scene set is now flat cartoon on
  t2 (S01–S06) + t1 (S07–S27).
- Text flags now: S02 (t2 "TOLL" panel), S04 marginal (t2 single "1"
  glyph), S11, S15, S17. S03 + S05 flags CLEARED by the re-fire.
- Trade-off on record: S02/S04 t1 takes are text-clean but photoreal
  (style break if used); t2 takes are flat but text-flagged. Assembly
  take choice is the user's call.

## Scenes still to fire

- None. Next decisions: assemble the full video from current takes,
  or reroll S02 + S04 on the text axis first.
- Awaiting: user decision.

## Kickstand state (read by mv-kickstand-watch / mv-kickstand-nag)

- last_volley_delivered: 2026-11-01 (volley 1 flat re-fire, S01–S06 t2).
- last_alert: none.
- assembled: 2026-11-01 — full 27-scene cut assembled with cheap lip-sync
  time-tween; masters delivered in chat (16:9 + 9:16, 268.01s). Project
  is DELIVERED, not waiting on the user.

## S02 + S04 t3 TEXT-AXIS rerolls — FIRED 2026-11-01
- Fired scenes: S02, S04 t3 takes from v3 vehicles (no-signage / no-gantry wording).
- Active takes: S02 t3 (md5 1d743a76460f7eac6d79b265752a42a6), S04 t3 (md5 3f1aae2e3be515bc78d45bb0b3034bbd). Both PASS text QC at 3s/6s/8s.
- Text flags now: S11, S15, S17 only (no reroll ordered for these — assembling with them flagged and disclosed).
- Next: lip-sync assembly of the full 27-scene cut.

## Assembly + delivery — DONE 2026-11-01

- Cheap lip-sync time-tween assembly ran clean (exit 0): per-scene
  generated-audio peaks paired to Suno onsets (`LIPSYNC_REPORT.json`),
  Suno track sole master audio, subtitle track, ~ WuBu ~ corner bug.
- Masters: `masters/mv2_toll_roads_are_dumb_16x9.mp4` (1280x720,
  md5 00368e7626185343ad7a66dc2ae28a8d) and
  `masters/mv2_toll_roads_are_dumb_9x16.mp4` (720x1280,
  md5 f8277f868df8554cb77360f5a6a1e1cf), both 268.010s.
  Ledger: `MUSIC_VIDEO_LEDGER.md`. Delivered in chat as attachments;
  announced to #wubu-mv-6a90e1. Flags S11/S15/S17 disclosed at delivery.
  Note 2026-11-06: both v1 master files were deleted with the user's
  approval (see CLEANUP_2026-11-06.md); the md5s above remain the
  delivery record.

## MV-2 v2 redo — Volley 1 performance-window re-fires — QC 2026-11-01
- Fired: S05 t3, S07 t2, S09 t2, S12 t2, S13 t2, S20 t2 (all 1280x720, 24fps, 10.000s).
- QC PASS (KEEP): S05 t3, S07 t2, S09 t2, S13 t2, S20 t2 — each >=2/3 samples face-to-camera with a visible open-mouth vocal passage, zero legible text.
- QC FAIL (REJECT): S12 t2 — gantry "TOLL" sign legible at 2s, "TOL" partial at 5s/8s. Text-axis reroll (t3, no overhead sign) still owed.
- Next: volley 2 (S11, S15, S17, S25, S27) + S12 t3, then re-plan the cut on LYRIC_TIMELINE.md.

## MV-2 v2 redo — Volley 2 + S12 t3 — FIRED 2026-11-01 under rebuilt pipeline
- Fired: S11 t2, S15 t2, S17 t2, S25 t2, S27 t2 (v2 performance-window vehicles) + S12 t3 (v3 text-axis vehicle: bare gantry frame, no sign panel at all). Vehicles at mv2_s11_vehicle_v2.txt, mv2_s15_vehicle_v2.txt, mv2_s17_vehicle_v2.txt, mv2_s25_vehicle_v2.txt, mv2_s27_vehicle_v2.txt, mv2_s12_vehicle_v3.txt.
- Pipeline basis: aggregated research (musicvideo/notes/SLOPCANNON_AGGREGATED_RESEARCH_2026-11-01.md) + rebuilt skill (references/performance-window.md; peak-tween removed from assemble.md).
- QC PENDING on /tmp/mv2_refire2/ frames (2s/5s/8s, majority rule + zero-text gate). Do not mark active until QC passes.

## MV-2 v2 redo — Volley 2 + S12 t3 — QC 2026-11-01
- QC PASS (KEEP) all six: S11 t2 (widened sample: to-camera vocal 1–4s, turn after), S15 t2, S17 t2, S25 t2, S27 t2, S12 t3 (text axis fixed, blank panel only).
- All 11 re-fired scenes now have a QC-passed take. Next: re-plan the cut on LYRIC_TIMELINE.md (S26 decision included), then assemble v2 under the rebuilt engine.

## MV-2 v2 redo — S26 re-plan restage — FIRED + QC 2026-11-01
- Fired: S26 t2 from mv2_s26_vehicle_v2.txt (staging axis: sing to camera first, silhouette after the vocal). 1 video on the user's "make the best music video" message (cap 6, 1 used).
- QC PASS (KEEP, widened sample 1s–8s): to-camera open-mouth singing 1s/2s, face-to-camera 3s, turn 4s, back silhouette 5s/6s/8s; text-clean throughout. S26 t1 retired from the cut (kept on disk).
- Re-plan DECIDED: 27 scenes on the true-timeline grid (see CUTLIST_V2.md). S26 window 248.01–258.01 contains vocal, hence the re-fire. All 27 scenes now have a QC-passed v2 take. Next: assemble v2.

## MV-2 v5 volley — FIRED + QC 2026-11-02
- Fired: S08 t2, S04 t5, S14 t2, S19 t2, S11 t3, S02 t4 (all 1280x720, 24fps, 10.000s).
- QC PASS (KEEP): all six — S08 t2, S14 t2, S19 t2, S11 t3, S02 t4 clean; S04 t5 partial-head KEEP (single clean "Weave"; song 74/75 covered by weave-hold warp, disclosed).
- Active v5 takes: S01 t4, S02 t4, S03 t2, S04 t5, S05 t4, S06 t2, S07 t2, S08 t2, S09 t2, S10 t1, S11 t3, S12 t3, S13 t2, S14 t2, S15 t2, S16 t1, S17 t2, S18 t1, S19 t2, S20 t2, S21 t2, S22 t1, S23 t1, S24 t1, S25 t2, S26 t2, S27 t2. Scenes still to fire: None. Next: v5 assembly on WORD_MATCH_V5.json.

## MV-2 v6 volley 1 — FIRED + QC 2026-11-02 (user message "fix all to fit within 10 sec and use proper cuts and triple devils advocate then fire volley")

- Fired (6 = cap for this user message, vehicles mv2_s*_vehicle_v6.txt verbatim):
  S13 t3 md5 eb13c86ef130a5b794ca134e744371ab,
  S23 t2 md5 61625845d79ab312b2c497ebfb82034f,
  S05 t5 md5 7bc84d871df04fb0430df8151978c7cc,
  S10 t2 md5 cf8562e58c5d14c32fc390ff57658982,
  S16 t2 md5 15e3180669a70e1f50c0c4061d8fafc4,
  S08 t3 md5 8ec7ecc9cb50d9b3cbd94f17a5031838.
  All 1280x720, 24fps, 10.000s. Transcription: TAKE_WORDS_V6_VOLLEY1.json
  (faster-whisper base, word timestamps, av-bypass via ffmpeg wav decode;
  prompt-grounded match to each scene's own BEAT line only, with the
  known Whisper mishear tall=toll applied — see below).
- QC by line ratio (song / take vocal, grey zone 0.60-0.80 / 1.25-1.60
  re-measured before a miss call, per V6_10S_CUT_PLAN.md):
  - S10 t2: RATIO IN BAND 0.97x (take vocal 3.86-7.14 = 3.28s,
    song 3.18s) BUT FRAME-QC FAILS: 2s/5s/8s all show three-quarter
    face looking sideways, mouth closed, never an open singing
    mouth in the vocal passage, and road text "NEAR" legible in
    all three frames (text gate fail). Ratio alone is not a QC
    pass. NOT a candidate; reroll axis facing + text.
  - S16 t2: RATIO IN BAND 0.94x (take vocal 2.22-5.44 = 3.22s,
    song 3.02s) BUT TEXT GATE FAILS: "STOP" legible on booth
    signs in 2s/5s/8s (plus faint road STOP). 5s frame itself
    is good (face-to-camera, open mouth, coin in hand), 2s coin
    close-up is the designed pre-vocal, 8s is post-vocal rest —
    but zero-text is a hard gate, so NOT a candidate as-is;
    reroll axis text (or a text-clean re-read of this take
    if the STOP signs are judged background-only — recorded
    here as a fail, not hidden).
  - S08 t3: GREY 0.61x (take vocal 0.00-7.56 = 7.56s, song 4.62s).
    Held delivery overshot; first-word onset at 0.00 is Whisper-edge
    suspect — re-measure before a firm miss call. Does NOT replace
    S08 t2 yet.
  - S13 t3: CLEAR MISS 0.42x (take vocal 0.00-3.64 = 3.64s, song 1.52s;
    Whisper "tall roads are dumb" = toll, mishear-corrected).
    Improved from t2 5.10s / 0.30x (29% faster) but still far from
    band — pacing moved it directionally, not 3.4x, exactly as the
    devil's-advocate pass predicted. NOT a candidate; needs
    split/restage, not another pacing rewrite.
  - S23 t2: CLEAR MISS 0.31x (take vocal 0.00-4.48 = 4.48s, song 1.38s;
    "tall" = toll). Slower than t1 3.74s / 0.37x despite the brisk
    prompt — selection variance swamps the pacing word. NOT a
    candidate.
  - S05 t5: CLEAR MISS 0.41x (take vocal ~5.28-10.00 = 4.72s, song
    1.92s; Whisper "towroads / are / dummed", slurred chorus, last
    word runs to take end). No improvement on t4 0.44x. NOT a
    candidate; chorus-line staging needs restage, not pacing.
- Motion/frame QC: frames at 2s/5s/8s extracted to qc_frames_v6v1/
  and read: S10 fails facing + text (see above), S16 fails text
  (see above), S08 5s passes (face-to-camera, open mouth, blank
  panels, ticket in hand mid-vocal), S13 5s is post-vocal hold
  (mouth closed expected — ratio already disqualifies it).
  Motion gate across whole vocals still applies before any take
  enters a cut — no take enters the v6 cut on ratio alone, and
  volley 1 yields ZERO clean candidates on full QC (2 ratio-pass
  takes both fail other gates).
- Scenes still to fire for v6: S06a + S06b (split vehicles written,
  V6_10S_CUT_PLAN.md section 4, first two slots of volley 2),
  grey/clear-miss restages for S13/S23/S05/S08, and fresh takes for
  every v5-reused occurrence (no-reuse rule). v6 is NOT assembled
  yet — volley 1 alone does not finish it. Next: user's "fire next
  volley" message (cap 6 again).

- Motion gate (0.5s-sampled frame diff, grayscale mean abs diff, 160x90):
  S10 vocal 3.86-7.14: diffs 23.6, 17.4, 17.5, 1.6, 0.49 — near-frozen
  tail during the vocal, matching the closed-mouth frames. MOTION FAIL.
  S16 vocal 2.22-5.44: diffs 36.5-15.0, continuous strong motion.
  MOTION PASS (text is its only fail). S08 vocal 0.00-7.56: diffs
  1.1-10.9, motion present with slow patches, no zero run.
  S13 vocal 0.00-3.64: diffs 1.5-11.4, motion present.
  Net: motion does not rescue S10, and does not condemn S16/S08
  on motion alone.

## MV-2 v6 volley 2 — FIRED + QC 2026-11-03 (user tap "Fire volley 2")

- Fired (6 = cap): S06a t1 md5 9fae8a9815ee60173b69f5db2cdcb570, S06b t1 md5 dbb5ef11a6d7349868563f37b4232c4e, S10 t3 md5 beef89c7adcfc360c2dbc5ec2965da5f, S16 t3 md5 47acafdf6537532649618345c3fcfbde, S13 t4 md5 23a353fb0aea1d006b4514b112c5e487, S23 t3 md5 9f3c6b4aaa8835922626bb4694d79690. All 1280x720, 24fps, 10.000s. Transcription: TAKE_WORDS_V6_VOLLEY2.json; frames in qc_frames_v6v2/.
- QC: S06b t1 CANDIDATE (ratio 0.97x, motion pass, text-clean 2s/5s/8s) — first clean v6 take. S06a t1 ratio 0.95x + motion pass BUT TEXT FAIL ("TOLL" signs) — not a candidate, text reroll owed. S10 t3 ratio 0.61x GREY (held), facing + text FIXED, motion patchy — not a candidate, delivery/selection take owed. S16 t3 ratio 0.83x BUT TEXT FAIL again (gantry "THE") — second denied v6 reroll, RETIRED, fresh staging owed. S13 t4 ratio 0.36x CLEAR MISS, text/facing clean — second denied v6 reroll, RETIRED, fresh staging owed. S23 t3 ratio 0.57x (0.66x on re-measured 1.60s song span, still grey) + TEXT FAIL ("TOLL LANE") — second denied v6 reroll, RETIRED, fresh staging owed.
- Scenes still to fire for v6: S06a t2 (text), S10 tighter take, S16/S13/S23 fresh stagings, S05 restage, S08 restage, fresh takes for v5-reused occurrences. v6 is NOT assembled yet — volley 2 yields 1 clean candidate. Next: user's "fire next volley" message (cap 6 again).

## MV-2 v6 volley 3 — FIRED + QC 2026-11-03 (user tap "Fire volley 3")

- Fired (6 = cap): S06a t2 md5 e39dc87cf28fb9f5e60cf5f1546c228d, S10 t4 md5 0527fb2723a78e12ca020a5d1ee9d3cc, S16 t4 md5 9b772e4cbeb0f106f6f73f07938afa45, S13 t5 md5 6ad6e3b163ed0e4b4172c1ba58367f2a, S23 t4 md5 224777466655a5a6e54c7d9504e9ea8a, S05 t6 md5 a82b554fdb82cdae768184e522559c68. All 1280x720, 24fps, 10.000s. Transcription: TAKE_WORDS_V6_VOLLEY3.json; frames in qc_frames_v6v3/.
- QC: S06a t2 CANDIDATE (ratio 0.89x, motion pass 4.9-13.6, text-clean 2s/5s/8s, face-to-camera open mouth mid-vocal, blank ticket) — second clean v6 take, S06 split now fully covered. S16 t4 CANDIDATE, borderline (ratio 0.80x on rounding, 3.02/3.78; motion pass, low but continuous 1.3-3.7, no zero run; text-clean empty stage, face-to-camera open mouth at 2s) — sits exactly on the lower band edge, disclosed as borderline. S10 t4 GREY 0.78x (take vocal 0.00-4.10 vs song 3.18s; 0.12s from band), facing + text clean (2s face-to-camera open mouth, blank panels), motion patchy (1.0 dips, no zero run) — HELD grey, not a candidate; tighter/selection take still owed. S23 t4 GREY on re-measure (0.55x on base 1.38s, 0.63x on re-measured 1.60s; vocal 0.00-2.52), text FIXED (fog only, no signage), facing pass, motion pass — HELD grey, fresh-staging selection take owed. S13 t5 CLEAR MISS 0.32x (vocal 0.00-4.70, "toll" held 2.46s; frames/text clean, pocket square red nit) — fresh staging did NOT compress; third staging family to fail on this 4-word hook. S05 t6 CLEAR MISS 0.54x (vocal 0.00-3.64 vs song 1.98s; frames/text clean) — single-line restage did NOT compress.
- Pattern now firm: the 4-word chorus hook "toll roads are dumb" is delivered at ~0.9-1.2s/word by the generator across pacing, staging, fresh-staging, and single-line vehicles (S13: t3 0.42x, t4 0.36x, t5 0.32x; S05: t5 0.41x, t6 0.54x; S23 improving only to grey). Next structural idea for volley 4, not yet tried: a delivery-MODE change (spoken/shouted chant instead of sung sustain) on one hook first, plus S08 restage and fresh takes for v5-reused occurrences. Do NOT re-fire volleys 1-3.
- Scenes still to fire for v6: S08 restage, S10/S23 grey selection takes, S13/S05 hook structural attempt, fresh takes for v5-reused occurrences. v6 clean coverage now: S06a t2, S06b t1, S16 t4 (borderline). v6 is NOT assembled yet.

## MV-2 v6 volley 4 — FIRED + QC 2026-11-03 (user tap "Fire volley 4")

- Fired (6 = cap): S08 t4 md5 e8fff7534422faf2d7752717f13cadc6, S10 t5 md5 164fcc8eaa5a04160524f34a3258e10b, S23 t5 md5 6a2d34f87954c664be31efef8675841c, S13 t6 md5 45761afbfc2cbc25f46534cb5425b252, S05 t7 md5 f2f81dacd684df63ab2cfd1afb4a3485, R1 t1 md5 869014bfa2980025d5e3f97bb45e9316. All 1280x720, 24fps, 10.000s. Transcription: TAKE_WORDS_V6_VOLLEY4.json; frames in qc_frames_v6v4/.
- QC: R1 t1 ratio 1.07x IN BAND + motion pass BUT TEXT FAIL ("STOP" booth signs at 2s/5s/8s) — plaza setting strikes again, structure-free restage owed; NOT a candidate. S08 t4 GREY 1.43x high side (vocal 1.64-4.86 = 3.22s vs song 4.62s — the brisk-delivery reroll overshot fast), text clean (blank panels, blank ticket), motion pass — HELD grey. S10 t5 GREY 0.74x (vocal 0.00-4.28 vs song 3.18s), facing + text clean (2s/5s face-to-camera, blank panels, 8s post-vocal head turn + shrug as designed), motion pass — HELD grey; t4 (0.78x) remains the closer S10 grey. S23 t5 GREY on re-measure (Whisper "told roads are dumb" 0.00-2.54 — "told" is the same one-phoneme mishear class as tall=toll; 0.54x on base 1.38s, 0.63x on re-measured 1.60s), fog only TEXT CLEAN, 2s open mouth mid-vocal, motion pass strong — HELD grey. S13 t6 CLEAR MISS 0.27x (vocal 0.00-5.58, "are" held 2.16s) — the delivery-MODE experiment FAILED: the generator sang the line sustained anyway, ignoring the spoken-chant instruction; frames/text clean (empty room, open mouth at 2s/5s) but the mode change did not compress. S05 t7 CLEAR MISS 0.36x (vocal 0.00-5.46, "are" held 2.00s) — same chant failure, text clean.
- Pattern now conclusive: delivery-mode words are NOT honored by the generator for this hook — sung sustain is the default regardless of chant/spoken instruction, across five vehicle families and now a mode change. The hook's floor is ~0.9s/word in generated delivery; the song slot is ~0.4s/word. Next ideas, none yet tried: (a) accept the best grey hooks at assembly with the warp band honored (no — warp outside 0.80-1.25 is banned by the v6 rule, so greys stay held, not warped in); (b) a fundamentally different delivery vehicle — e.g. the line split across two shots, or a non-sung visual beat carrying the hook while the track's own vocal carries the words (assembly-level, needs user call); (c) more selection takes on the grey scenes (S08/S10/S23 greys are all within 0.25 of the band and selection variance has moved takes before).
- Scenes still to fire for v6: R1 structure-free restage, S08/S10/S23 grey selection takes, S13/S05 hook (no untried prompt axis left in the current family — needs a new structural idea or a user call on the grey-hook question), remaining v5-reused repeats (R2/R3/R4/R5/R6/R8/R11). v6 clean coverage UNCHANGED: S06a t2, S06b t1, S16 t4 (borderline). v6 is NOT assembled yet. Do NOT re-fire volleys 1-4.

## MV-2 v6 volley 5 — FIRED + QC 2026-11-03 (user tap "Fire volley 5")

- Fired (6 = cap): R1 t2 md5 81823e2efff9485109888d4b42933d7d, S08 t5 md5 d0b420963db52f80d118f96b829d7886, S10 t6 md5 1b51ae3a2805259213b09d6bfa6b783f, S23 t6 md5 28b73f65850df8cb71986d6630ebf69c, R2 t1 md5 32e2ab3263db61c524ac97c047534aa7, R3 t1 md5 362e228752c06ca979ac9344b88ffa94. All 1280x720, 24fps, 10.000s. Transcription: TAKE_WORDS_V6_VOLLEY5.json; frames in qc_frames_v6v5/.
- QC: S10 t6 CANDIDATE (ratio 0.90x in band, vocal 0.00-3.54 vs song 3.18s; motion pass strong 3.7-22.5; 2s face-to-camera open mouth mid-vocal, blank panels, plain arrows, blank ticket — TEXT CLEAN, face matches THE VOICE) — S10 finally covered after four v6 takes. R2 t1 CANDIDATE (line present 0.00-4.38 as "we've been slamming the danger roads" — the matcher scored 0/7 only because my beat string split "we've" into "we have"; ratio 1.21x in band vs song 5.28s; motion pass; open-road TEXT CLEAN, face matches, ticket in hand) — first repeat covered. R1 t2 ratio 1.07x in band ("paid to go faster, the rest of us slow" 0.00-5.96 — "paid" is the same one-phoneme mishear class), motion pass, open-road TEXT CLEAN — BUT CHARACTER FAIL: the singer renders as a different person (darker skin, different face) from THE VOICE, so it cannot cut as the same performer — NOT a candidate; character-consistency is a gate for a single-performer video. S08 t5 MISS: the line is sung TWICE (1.08-3.44 and 3.44-6.38); first span ratio 1.96x (too fast, above even grey) and the repeat makes it unusable as a single-line take; face also looks off. S23 t6 GREY 0.62x on re-measured span (vocal 0.00-2.58 exact, 0.53x on base 1.38s) — HELD grey, plus character drift (different face, gold chain not in the outfit spec). R3 t1 CLEAR MISS 0.56x (vocal 0.00-3.88 vs song 2.16s — just 0.04 below the grey floor), face + text clean.
- v6 clean coverage now: S06a t2, S06b t1, S16 t4 (borderline), S10 t6, R2 t1. Still to fire: R1 (character-consistent restage), S08 (line-doubling fix — single delivery only), S23 grey selection (character watch), R3 (near-grey, one more selection take), remaining v5-reused repeats (R4/R5/R6/R8/R11), S13/S05 hook (no untried prompt axis — needs a new structural idea or a user call). v6 is NOT assembled yet. Do NOT re-fire volleys 1-5.

## MV-2 v6 volley 6 — FIRED + QC 2026-11-03 (user tap "Fire volley 6")

- Fired (6 = cap): R1 t3 md5 4e0d9a48594f65bed55337a40bdd2372, S08 t6 md5 59727b571681d6094a1fbcf826682598, S23 t7 md5 93f5bfd67c3c6bbab42b6af37b6e7672, R3 t2 md5 d871c3323b566202fc24017ab254bc08, R4 t1 md5 19158e204c190bd4fc9152e5a2d4d13c, R5 t1 md5 8cffc10e8c5263937d6f66a87113b8f5. All 1280x720, 24fps, 10.000s. Transcription: TAKE_WORDS_V6_VOLLEY6.json; frames in qc_frames_v6v6/.
- QC: R1 t3 CANDIDATE (ratio 1.09x in band, motion pass, text-clean open road, face matches — the t2 character failure fixed by selection on the same vehicle). S08 t6 ratio 1.07x in band + single delivery CONFIRMED (no second delivery in the transcript) BUT TEXT FAIL ("TOLL" booth signs at 2s/5s/8s) — plaza strikes again, structure-free restage owed. S23 t7 ratio 0.43x / 0.50x re-measured CLEAR MISS — face fixed, ratio not. R3 t2 ratio 0.44x CLEAR MISS, worse than t1's near-grey. R4 t1 ratio 0.59x (0.01 below grey) + CHARACTER FAIL (different person) — not a candidate on either gate. R5 t1 ratio 0.73x GREY HELD, face + text clean.
- v6 clean coverage now: S06a t2, S06b t1, S16 t4 (borderline), S10 t6, R2 t1, R1 t3. Still to fire: S08 structure-free restage, R3/R4/R5 selection takes, fresh takes for R6/R8/R11, S13/S05/S23 hook (no untried prompt axis — needs a new structural idea or a user call). v6 is NOT assembled yet. Do NOT re-fire volleys 1-6.

## MV-2 v6 volley 7 — FIRED + QC 2026-11-03 (user tap "Fire volley 7")

- Fired (6 = cap): S08 t7 md5 7cf29486002c2722052088b5c7a3dc67, R3 t3 md5 4b3a949c1ecfb87607c503105db13d83, R4 t2 md5 cfc623dc501fe1a36dce02b252583302, R5 t2 md5 1cce17e26c1d789fbd5c4ba3bb86da76, R6 t1 md5 a178526b4aa7e19e2c006a47d7969c80, R8 t1 md5 1f5bb38e275a920fc34397340987b837. All 1280x720, 24fps, 10.000s. Transcription: TAKE_WORDS_V6_VOLLEY7.json; frames in qc_frames_v6v7/.
- QC: R8 t1 CANDIDATE (ratio 0.96x in band, motion pass, text-clean, face matches). S08 t7 ratio 1.86x CLEAR MISS high side — structure-free fixed the text axis at last, but the delivery overshot fast; selection take on the same vehicle owed. R3 t3 ratio 0.43x CLEAR MISS, third wrong-way selection in a row. R4 t2 ratio 0.73x GREY HELD, character failure fixed. R5 t2 ratio 0.73x GREY HELD (identical to t1). R6 t1 ratio 0.60x GREY HELD exactly on the floor edge.
- v6 clean coverage now: S06a t2, S06b t1, S16 t4 (borderline), S10 t6, R2 t1, R1 t3, R8 t1. Still to fire: S08 selection, R3/R4/R5/R6 selection takes, R11 fresh take, S13/S05/S23 hook (no untried prompt axis — needs a new structural idea or a user call). v6 is NOT assembled yet. Do NOT re-fire volleys 1-7.

## MV-2 v6 volley 8 — FIRED + QC 2026-11-03 (user tap "Fire volley 8")

- Fired (6 = cap): S08 t8 md5 9eb642cefd3bdc934a63c8cba22d7a50, R4 t3 md5 446ab6b5ca033ea0eab07f17ee6fae62, R5 t3 md5 af42450ba79a6d88a8240160736275a5, R6 t2 md5 b40c7c57a06508c6fff020905e5e4531, R11 t1 md5 a48a5a14e060455d9a73a877424c6134, R3 t4 md5 a140ce5cba6be57f8c1ee91f8f0625b8. All 1280x720, 24fps, 10.000s. Transcription: TAKE_WORDS_V6_VOLLEY8.json; frames in qc_frames_v6v8/. R11 vehicle mv2_r11_vehicle_v6.txt written before firing (open-road R-template, "Yeah." at song 242.30-243.08).
- QC: R5 t3 CANDIDATE (ratio 0.88x in band, vocal frames 77/78 changed, face matches, text clean; disclosed nit: gold chain not in outfit spec). R3 t4 ratio 0.66x GREY HELD — first R3 take in grey (t1 0.56, t2 0.44, t3 0.43), vocal frames 72/79 changed, face + text clean. R6 t2 ratio 0.62x GREY HELD (up from t1's 0.60 edge), vocal frames 87/87 changed, face + text clean. R4 t3 ratio 0.53x CLEAR MISS (down from t2 grey 0.73), frames alive, face + text clean. R11 t1 ratio 0.40x CLEAR MISS (single "yeah" held 1.96s vs song 0.78s), face + text clean. S08 t8 ratio 2.18x CLEAR MISS high side (vocal 1.32-3.44, sung once) AND frame-poor during vocal (14/53 changed, 13-frame frozen run) — structure-free setting kept text clean but the take is fast AND still. S08 now has no take passing all gates: t6 ratio in band but plaza text fail + frame-poor vocal (49/104), t7/t8 structure-free but overshot fast.
- FRAME RECHECK (user rule 2026-11-03: more frames that actually change = good, fewer = bad): all 48 v6 takes audited at native 24fps (frame_audit_v6.py -> FRAME_AUDIT_V6.json) plus vocal-window audit (vocal_window_audit.py -> VOCAL_WINDOW_AUDIT.json: changed frames and longest near-duplicate run INSIDE the vocal span). Bar used: vocal changed fraction >=70% alive; any near-dup run >=24 frames (1s) during vocal = freeze flag. Finding: the old 0.5s-sample motion gate was too coarse — it passed takes that are frame-poor during words. S16 t4 DEMOTED under the frame rule: ratio 0.80 borderline, text clean, but only 27/92 vocal frames changed (29%, near-dup run 13) — a still singer on an empty stage, mouth moving but picture barely changing; NOT doable as-is. Frame-passing candidates now: S06a t2 (140/153), S06b t1 (139/139), S10 t6 (66/86), R2 t1 (105/106), R1 t3 (126/141), R8 t1 (144/145), R5 t3 (77/78). Frame-poor confirmed: S13 t6 vocal 32/135 with 58-frame near-dup run and 22-frame frozen run (the chant take was a held picture, not just slow); S10 t2 vocal near-dup run 34 (frozen tail confirmed); S05 t6 32/88, S05 t7 near-dup run 24, S10 t3/t4/t5 29-36% vocal changed, S08 t3/t4/t6/t8 all <=50% vocal changed. v5 in-band keep takes whole-take audited: S01 t4 (239/239), S04 t5 (239/239), S24 t1 (235/239), S03 t2 (205/239), S26 t2 (204/239) frame-alive; S02 t4 (115/239), S07 t2 (109/239), S11 t3 (104/239), S21 t2 (101/239) frame-poor by whole-take count and need vocal-window confirmation before assembly use.
- v6 clean coverage now (frame-passing only): S06a t2, S06b t1, S10 t6, R2 t1, R1 t3, R8 t1, R5 t3. Greys held with alive frames: R3 t4 0.66x, R4 t2 0.73x, R6 t2 0.62x. Still blocked: S16 (t4 frame-poor, t2 text fail — needs a text-clean AND frame-alive take), S08 (no take passes all gates), R11 (ratio miss), S13/S05/S23 hook (no in-band take; S23 t7 frame-alive 70/78 but ratio miss). v6 is NOT assembled yet. Do NOT re-fire volleys 1-8.

## MV-2 v6 volley 9 — FIRED + QC 2026-11-03 (user tap "Fire volley 9")

- Fired (6 = cap): S08 t9 md5 7db2503e55330e0b191415644e80f247, S16 t5 md5 cd4393bae0b8bdbf18268ca391ffccdd, R3 t5 md5 7feae2f652443413566554d112372133, R4 t4 md5 2f0bfbfbccae7701afb4d0daf4e8913a, R6 t3 md5 76bf9274a700c0c4e0a2191cc1efe754, R11 t2 md5 359da8591c7176123a37904929c51890. All 1280x720, 24fps, 10.000s. Transcription: TAKE_WORDS_V6_VOLLEY9.json; frames in qc_frames_v6v9/. New vehicles: mv2_s08_vehicle_v6r4.txt (steady pace + hand moves through the line), mv2_s16_vehicle_v6r2.txt (open road + push + hand rise through the line).
- QC: S08 t9 CANDIDATE (ratio 0.95x in band, line sung ONCE, face-to-camera open mouth, text clean; vocal frames: longest near-dup run 3 frames, vocal mean diff 1.92 — no freeze during words; disclosed nit: only 58/118 vocal frames changed, i.e. half-rate motion). S08 COVERED after nine v6 takes. S16 t5 ratio 0.50x CLEAR MISS (9-word line 0.00-6.06 vs song 3.02s) — restage fixed text AND frames (146/146 vocal frames changed, run 0) but delivery went slow; selection on v6r2 owed. R3 t5 ratio 0.52x CLEAR MISS (down from t4 grey 0.66), frames alive. R4 t4 ratio 0.69x grey on first span BUT repeat-tail defect: raw words show "done" sung twice (2.76-3.50 and 3.88-5.80) — the matcher second-delivery scan only flags full-line repeats, so this tail slipped past it; NOT a clean grey, single-delivery vehicle owed. R6 t3 ratio 0.50x CLEAR MISS (down from t2 grey 0.62), frames alive. R11 t2 DOUBLE-DELIVERY MISS: first "yeah" 0.00-0.78 ratio 1.00x in band, but "yeah" sung AGAIN at 3.48-4.18 — single-delivery vehicle owed (same fix class as S08 t5->t6).
- FRAME GATE REFINEMENT (from S08 t9 vs S16 t4): changed-fraction alone misranks — S08 t9 is 49% changed but mean diff 1.92 with max run 3 (moving, half-rate), while S16 t4 is 29% with mean 0.35 (essentially still). Gate now: FAIL if vocal near-dup run >=24 frames (1s) during vocal OR vocal mean diff <0.5; changed fraction is a quality note, not the gate. S16 t4 demotion stands (mean 0.35).
- v6 clean coverage now (frame-passing only): S06a t2, S06b t1, S10 t6, R2 t1, R1 t3, R8 t1, R5 t3, S08 t9. Greys held clean: R3 t4 0.66x, R6 t2 0.62x (R4 t4 grey disqualified by repeat tail). Still blocked: S16 (selection on v6r2 owed), R11 (single-delivery vehicle owed), R4 (single-delivery vehicle owed), R3/R6 (selections), S13/S05/S23 hook (no untried prompt axis). S22 identified as an uncovered main slot: line "Toll roads are done." song 222.44-224.64 = 2.20s, v5 take 0.58x miss — fresh v6 take owed. v6 is NOT assembled yet. Do NOT re-fire volleys 1-9.

## MV-2 v6 volley 10 — FIRED + QC 2026-11-03 (user tap "Fire volley 10")

- Fired (6 = cap): S16 t6 md5 fe67259117cd8f1ddcc5951f6d12835b, R11 t3 md5 23b9a5bb6805dffb8ae027425f7100c9, R4 t5 md5 b59e83a15ff3546c960b4c000c89b7fa, R3 t6 md5 774c6de04dd0e91a9c91e72c736706a6, R6 t4 md5 f45c2309fb656612d4f3f97f1e038c83, S22 t2 md5 ddb2a9b8de4038ba6f01b5ef7ed8cb20. All 1280x720, 24fps, 10.000s. Transcription: TAKE_WORDS_V6_VOLLEY10.json; frames in qc_frames_v6v10/; vocal-window audit in VOCAL_WINDOW_AUDIT.json (54 takes). New vehicles: mv2_r11_vehicle_v6r.txt (single-delivery), mv2_r4_vehicle_v6r.txt (single-delivery), mv2_s22_vehicle_v6.txt (fresh take, R-template open road; v6 numbering continues from v5 t1, so this is t2). Selections verbatim: mv2_s16_vehicle_v6r2.txt, mv2_r3_vehicle_v6.txt, mv2_r6_vehicle_v6.txt.
- QC: ZERO new candidates. R11 t3 GREY HELD, clean (vocal 0.00-1.00, ratio 0.78x, sung exactly once — the single-delivery vehicle WORKED, and this is the closest R11 grey yet; vocal frames 24/25 changed, run 1, mean 1.08; face matches, TEXT CLEAN; nit: pocket square blue). R6 t4 GREY HELD, clean (vocal 1.72-5.18, ratio 0.63x; vocal frames 75/85 changed, run 1, mean 1.77; face matches, TEXT CLEAN; nit: simpler flat render + pocket square blue, mic held in hand in frames). S16 t6 GREY 0.76x BUT REPEAT-DISQUALIFIED: first delivery 0.00-4.00 is in grey, but the raw word list shows the tail "for a dollar and a dime" sung AGAIN 5.52-8.04 — a partial-line repeat the full-line second-delivery scan misses (it only matches from the beat start, and the repeat starts mid-line). Vocal frames pass (96/97 changed, run 1, mean 1.61), face matches, TEXT CLEAN, but NOT a clean grey; single-delivery vehicle owed. R4 t5 CLEAR MISS 0.55x (vocal 0.00-4.40, exactly 4 words, no repeat — single-delivery fix worked, ratio went the wrong way from t4's 0.69x grey). R3 t6 CLEAR MISS 0.42x (vocal 0.00-5.20, "are" held 1.60s; down from t4 grey 0.66). S22 t2 CLEAR MISS 0.48x + REPEAT TAIL: vocal 0.00-4.56, but raw words show "done" again 4.56-6.08 — the R4 t4 defect class, in a fresh take; face matches, TEXT CLEAN, frames pass (109/110 changed, run 1, mean 1.33), nit: gold chain + CADMIUM square correct. All six frame-pass the vocal-window gate (near-dup runs 0-1, means 1.08-2.21).
- QC METHOD REFINEMENT (volley 10): the second-delivery scan must check for ANY beat-word subsequence recurring after the first delivery, not just a full-beat recurrence from the beat start — S16 t6's mid-line tail repeat and S22 t2's final-word repeat both slip past the full-line scan. Always read the raw word list; a take sings its line exactly once, no part of it a second time.
- v6 clean coverage UNCHANGED (frame-passing only): S06a t2, S06b t1, S10 t6, R2 t1, R1 t3, R8 t1, R5 t3, S08 t9. Clean greys held: R11 t3 0.78x (new), R6 t4 0.63x, R3 t4 0.66x, R4 t2 0.73x. Still blocked: S16 (single-delivery vehicle owed), S22 (single-delivery vehicle owed), R4/R3 (selection takes), S13/S05/S23 hook (no untried prompt axis). v6 is NOT assembled yet. Do NOT re-fire volleys 1-10.

## MV-2 v6 volley 11 — FIRED + QC 2026-11-03 (fired on user's "music video still not shipped" message; S16 t7 server-failed, not retried in-volley)

- Fired (5 landed + 1 failed): S22 t3 md5 e884bac5bfd64b8856b61d64cd3977d4, R4 t6 md5 690ef7e5c68711af43077f44b667eed0, R3 t7 md5 8bc87e3daec03273d1fab195b97e2e40, R11 t4 md5 8c2e82817131d5ee6b4ed59b67a73035, R6 t5 md5 f1f929ccade5fbd9716c3374359a40f2. All 1280x720, 24fps, 10.000s. Transcription: TAKE_WORDS_V6_VOLLEY11.json; frames in qc_frames_v6v11/; vocal-window audit in VOCAL_WINDOW_AUDIT.json (59 takes). S16 t7 produced NO video: takes/media-generation-mv2-s16-t7-1793696731.json records a server error (safety_service_unavailable, downstream 500, 0 attachments) and no mv2_s16_t7.mp4 exists; the firing subagent did not retry it within the volley. New single-delivery vehicles: mv2_s16_vehicle_v6r3.txt (unused — its take never generated), mv2_s22_vehicle_v6r.txt. Selections verbatim: mv2_r4_vehicle_v6r.txt, mv2_r3_vehicle_v6.txt, mv2_r11_vehicle_v6r.txt, mv2_r6_vehicle_v6.txt.
- QC: R11 t4 CANDIDATE (ratio 1.08x in band, "yeah" 0.00-0.72 sung exactly once, vocal frames 9/18 changed, near-dup run 1, mean 1.06 — frame gate PASS; face matches, TEXT CLEAN; nit: pocket square blue). R11 COVERED — first R11 candidate after t1 miss, t2 double-delivery, t3 grey. S22 t3 ratio 0.53x CLEAR MISS (repeat fixed vs t2: sung exactly once, second-delivery + subsequence scans empty; vocal frames 100/101 changed, run 1, mean 1.85; face matches, TEXT CLEAN; nit: blue suit + blue pocket square). R4 t6 ratio 0.56x CLEAR MISS (sung once; vocal frames 105/105 changed, run 0, mean 1.51; face + text clean; nit: pocket square blue). R3 t7 ratio 0.55x CLEAR MISS (sung once; vocal frames 89/94 changed, run 1, mean 1.39; face + text clean; nit: pocket square blue). R6 t5 ratio 0.54x CLEAR MISS (sung once; vocal frames 94/97 changed, run 1, mean 1.55; face + text clean; nit: pocket square orange).
- Pattern: all four "Toll roads are done" slots landed at 0.53-0.56x in volley 11 — selection on the same vehicles moved R3/R4/R6 DOWN from their held greys (R3 t4 0.66, R4 t2 0.73, R6 t4 0.63) instead of toward band, and S22's single-delivery fix cured its repeat tail without moving its ratio into band. Single-delivery wording is now confirmed working on all five landed takes (zero repeats, zero tails).
- v6 clean coverage now (frame-passing only): S06a t2, S06b t1, S10 t6, R2 t1, R1 t3, R8 t1, R5 t3, S08 t9, R11 t4. Clean greys held: R6 t4 0.63x, R3 t4 0.66x, R4 t2 0.73x (R11 t3 0.78x grey superseded by candidate t4). Still blocked: S16 (no take — server error, retry owed), S22/R4/R3/R6 "done" slots (ratios clustered ~0.55), S13/S05/S23 hook (no untried prompt axis). v6 is NOT assembled yet. Do NOT re-fire volleys 1-11.

## MV-2 v6 volley 12 — FIRED + QC 2026-11-03 (user tap "Fire volley 12"; firing completed ~06:06 EST, QC by parent)

- Fired (6 = cap, all landed, none owed): S16 t7 md5 cf675eaa451956107f170cec69fbc230, S22 t4 md5 2cc8337fdd3632a8885e4b1727891aee, R4 t7 md5 2a33c85e0c4e137a4e070a105de9230b, R3 t8 md5 114df823e8a0b6c175580749a4e96517, R6 t6 md5 af56400583a5c2bc9ec845db500efe7e, S23 t8 md5 3b997c4f6991bfabb4d66d0beb6c9ea7. All 1280x720, 24fps, 10.000s, 240 frames. Transcription: TAKE_WORDS_V6_VOLLEY12.json; frames in qc_frames_v6v12/; vocal-window audit in VOCAL_WINDOW_AUDIT.json (65 takes). Vehicles: S16 mv2_s16_vehicle_v6r3.txt (volley-11 pre-written single-delivery; the volley-11 server error did NOT recur); S22 mv2_s22_vehicle_v6r.txt (second and last attempt on this vehicle); R4 FRESH mv2_r4_vehicle_v6r2.txt (retirement check: v6r had two denied attempts t5 0.55x + t6 0.56x, not fired a third time; new axis: empty dark stage, seated on stool, locked-off MCU, ticket shown only after the last word); R3 FRESH mv2_r3_vehicle_v6r.txt (v6 far past two denied rerolls; new axis: bare interior room, window light, locked-off MCU, ticket held still through the line); R6 FRESH mv2_r6_vehicle_v6r.txt (v6 past two denied rerolls; new axis: roadside at dawn, turn-to-camera before the first word, locked-off MCU, no push-in); S23 mv2_s23_vehicle_v6fresh.txt reused verbatim (the t4/t5/t6 grey vehicle; t7 was a single miss, not two denied rerolls, so no fresh variant triggered; no chant/delivery-mode wording).
- QC: ZERO new candidates. S16 t7 GREY HELD 0.76x (9-word line 0.00-4.00; Whisper heard "tell" for "sell" — new one-phoneme mishear class, same precedent as tall=toll; sung exactly once, second-delivery + subsequence scans empty; vocal frames 96/97 changed, near-dup run 1, mean 1.01 — frame PASS; face matches, night road TEXT CLEAN, blank ticket; nit: pocket square blue). S22 t4 GREY HELD 1.29x high side (line recovered only by split-half recheck: full-clip Whisper returned 0 words on loud audio, but the 0-5s half decodes "TOWROADS ARE DONE" at 3.16-4.86 — toll+roads slur; second half empty, single delivery; vocal frames 23/43 changed, near-dup run 1, mean 1.47 — frame PASS; face matches, night road TEXT CLEAN, blank ticket; nit: pocket square blue). R4 t7 FRAME-GATE FAIL (ratio 0.72x grey on first span, but vocal near-dup run 62 frames >=24 AND vocal mean diff 0.20 <0.5 — frozen picture while the words play, exactly the v5 failure mode; strip frames near-identical at 2s/5s/8s; face matches, dark stage TEXT CLEAN, blank ticket; the fresh vehicle held the ratio band but froze the picture — NOT a clean grey, DISQUALIFIED). R3 t8 CLEAR MISS 0.44x (vocal 0.00-4.92, sung once; vocal mean 0.39 fails the frame gate too; face matches, bare room TEXT CLEAN, blank ticket; nit: pocket square blue) — fresh staging did NOT compress. R6 t6 CLEAR MISS 0.40x (vocal 0.00-5.42, sung once; vocal frames near-dup run 5, mean 1.87 — frame PASS; face matches, roadside dawn TEXT CLEAN, blank ticket; nit: pocket square red) — fresh staging did NOT compress. S23 t8 CLEAR MISS 0.55x (vocal 0.00-2.90, sung once; vocal frames near-dup run 1, mean 0.71 — frame PASS; face matches, fog stage TEXT CLEAN; nit: pocket square red) — DOWN from the same vehicle's held greys (t4/t5/t6 ~0.62-0.63x), the volley-11 pattern repeating: selection on the same vehicle moves "done"/hook slots down, not toward band.
- QC METHOD REFINEMENT (volley 12): a zero-word full-clip Whisper result is NOT a no-line verdict — S22 t4's full-clip decode blanked on loud audio while the 0-5s half decoded the line cleanly. Split-half recheck before calling any take lineless. New mishear class: tell=sell.
- v6 clean coverage UNCHANGED (frame-passing only): S06a t2, S06b t1, S10 t6, R2 t1, R1 t3, R8 t1, R5 t3, S08 t9, R11 t4. Clean greys held: S16 t7 0.76x (new), S22 t4 1.29x (new, high side), R6 t4 0.63x, R3 t4 0.66x, R4 t2 0.73x, plus S23 t4/t5/t6 ~0.62-0.63x. Still blocked: S16/S22 (greys held, not covered), R4/R3/R6 "done" slots (fresh vehicles failed: R4 froze, R3/R6 missed), S23 hook (t8 miss on the grey vehicle), S13/S05 hook (no untried prompt axis). v6 is NOT assembled yet. Do NOT re-fire volleys 1-12.


## MV-2 v6 volley 13 — FIRED + QC 2026-11-03 (standing refire authorization 2026-11-03 ~08:42 EST; no per-volley ask)

- Fired in two parts (6 takes total, all landed, none owed): FIRST firing agent died mid-run on a transport error (sqlx pool timeout) after landing S16 t8 md5 1671c4590bc69dae195932ac09415d19 and S22 t5 (raw file only, md5 a912f48dcb2b1a8dab3713d4996cfb4e; canonical takes/mv2_s22_t5.mp4 made by the parent in this write-up, md5 verified identical). REFIRE agent landed the 4 owed slots ~08:45 EST: R4 t8 md5 42a9f9f3af67924b0ceabebac72af8e5, R3 t9 md5 b99d03e3615693cddf7532a43f4d2abd, R6 t7 md5 f11608c0db2638c50c743b2b3482ab7b, S23 t9 md5 7cb456ca1464fd525a509ffbf296caff. All 1280x720, 24fps, 10.000s, 240 frames (parent md5 + ffprobe verified). Vehicles: S16 mv2_s16_vehicle_v6r3.txt (2nd attempt), S22 mv2_s22_vehicle_v6r2.txt (1st attempt, fresh staging), R4 mv2_r4_vehicle_v6r2.txt (2nd attempt), R3 mv2_r3_vehicle_v6r.txt (2nd attempt), R6 mv2_r6_vehicle_v6r.txt (2nd attempt), S23 mv2_s23_vehicle_v6fresh2.txt (1st attempt). Transcription: TAKE_WORDS_V6_VOLLEY13.json (S16/S22 rows from the recovered QC report — per-word timestamps lost with that agent's /tmp files, not reconstructed); refire transcription TAKE_WORDS_V6_VOLLEY13_REFIRE.json; frames qc_frames_v6v13_refire/ (refire takes only — the S16/S22 QC frames were /tmp and are lost); vocal-window audit VOCAL_WINDOW_AUDIT.json (69 takes).
- QC: ZERO new candidates. S16 t8 GREY HELD 0.60x boundary (9-word line, span 5.04s vs song 3.02s, unrounded 0.5992; sung exactly once, repeat scan empty; frame PASS 121/122 changed, run 1, mean 1.54; G1/G2/G4 PASS; nit: pocket square blue) — held per the R6 t1 0.60x boundary precedent. SLOWER than t7 (4.00s, 0.76x) on the same vehicle: selection moved down again. S22 t5 CLEAR MISS 0.44x (span 5.04s vs song 2.20s; "toll" alone held 2.66s; 4 words, sung exactly once — the t2 repeat tail is fixed; frame PASS 121/122 changed, mean 2.15; G1/G2/G4 PASS; nit: blue pocket square). R4 t8 FRAME-GATE FAIL, DISQUALIFIED (ratio 0.76x grey on first span, but vocal mean diff 0.42 <0.5, near-dup run 11; sung once; G1/G2/G4 PASS; nit: pocket square orange-red) — same fail as t7 on the same vehicle. R3 t9 FRAME-GATE FAIL, KNIFE-EDGE (ratio 0.94x IN BAND, vocal 0.18-2.48, sung once, G1/G2/G4 PASS, nit: pocket square blue; vocal mean diff 0.49919 <0.5 by 0.0008, near-dup run only 7, diffs spike to 2.24 — the picture visibly moves, but the gate is a hard line and the parent does NOT overrule it: NOT a candidate. The refire vocal json's rounded 0.50/PASS field is a rounding artifact, corrected to FAIL in this write-up). R6 t7 CLEAR MISS 0.43x (vocal 0.00-5.02, "toll" held 2.14s, sung once; frame PASS mean 0.81, run 1; G1/G2/G4 PASS; nit: pocket square orange-red). S23 t9 CLEAR MISS 0.37x (Whisper "robes" for "roads" — proposed new mishear class robes=roads, verdict independent of it; normalized span 0.00-4.32 vs song 1.60s, sung once as normalized; frame PASS mean 2.19, run 1, the most alive take of the four; G1/G2/G4 PASS; pocket square reads CADMIUM-gold here).
- RETIREMENTS (two-denied rule): R4 v6r2 RETIRED (t7 + t8 both frame-gate fails — the seated locked-off "completely still through the line" staging looks like the problem, not luck). R6 v6r RETIRED (t6 0.40x + t7 0.43x misses). R3 v6r RETIRED (t8 0.44x miss + t9 frame-gate fail). S23 v6fresh2 has ONE denied attempt banked (t9 0.37x); one more attempt allowed before retirement. S16 v6r3 has two attempts (t7 grey, t8 grey) — no third attempt on v6r3 without a fresh staging decision. S22 v6r2 has one denied attempt (t5 miss).
- v6 clean coverage UNCHANGED (frame-passing only): S06a t2, S06b t1, S10 t6, R2 t1, R1 t3, R8 t1, R5 t3, S08 t9, R11 t4. Clean greys held: S16 t7 0.76x, S16 t8 0.60x (new, boundary), S22 t4 1.29x, R6 t4 0.63x, R3 t4 0.66x, R4 t2 0.73x, S23 t4/t5/t6 ~0.62-0.63x. Still blocked: S16/S22 (greys/miss), R4/R3/R6 "done" slots (vehicles retired — fresh staging from scratch owed), S23 hook (v6fresh2 one attempt left), S13/S05 hook (no untried prompt axis — needs a new structural idea or a user call). v6 is NOT assembled yet. Do NOT re-fire volleys 1-13. Further firing follows the standing refire authorization AND the pending sung-timing method adjudication — the volley treadmill does not resume on the old method.
