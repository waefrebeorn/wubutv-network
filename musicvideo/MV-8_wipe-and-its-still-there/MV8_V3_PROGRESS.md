# MV-8 v3 — REBUILD PROGRESS (montage-first rebuild)

Verdict (user playback, 2026-11-09 ~02:52 EST): v2 REJECTED — bad
montage timing, bad lipsync timing, halted moments; v2 centered a
singing character against the told order (no singing character —
cartoon events, montage of lyrics); reused footage; song timing/vibes
not used properly. **v3 ordered same night: no singing character as
the spine, cartoon events + montage of lyrics, singer clips only as
properly-timewarped montage inserts, ZERO reused footage, fire more
cannon, use the song, find better detection methods daily.**
Parent delivers; coordinator does NOT write any *_DELIVERED.flag and
does NOT commit.

Governing plan: `work/rebuild/SCENE_PLAN_v3.md` (montage-first, 17
scenes, 4493f). Song facts unchanged (SONG_WORDS_v2.json,
LYRIC_TIMELINE_v2.md, CRESCENDO_MAP_v2.md, beat_grid_v2.json;
123.05 BPM, 368 beats, first beat 5.968s, true peak 159.435s =
frame 3826). v2 assets are REFERENCE ONLY — never cut a v2 take into
v3 as scene footage. Singer inserts: 6 named v2 takes, each used
once, warp-verified by eye on the warped render (see plan § Inserts).

## Stage 1 — Replan (2026-11-09 ~03:0x EST)

- SCENE_PLAN_v3.md written: same 17-scene tiling as v2 (4493f),
  all scenes CARTOON EVENT / MONTAGE; kinetic words in post on the
  song's word-onset grid; 28 fresh v3 takes planned across 5 volleys;
  6 singer inserts named (INS-1/2/4/5/6/7, ~27s ≈ 15% of the video);
  L18 + L22 on fresh montage (named v2 flaws, never warped singer
  takes); WIPE counter fixed (WIPE N at beat N−1 — beat 345 reads
  346, not 347); style lock CHANGED to flat bold 2D cartoon
  (v2's photoreal anchor was part of the look problem); O-A split
  re-applied with fresh takes; no-reuse audit mandated at assembly.
- TAKE_LEDGER_v3.md opened; DETECTION_GAPS_v3.md opened (4 gaps
  recorded for the daily detection-research job).

## Stage 2 — Stills v3 (DONE for volley 1 — 5/5 PASS)

- STILL_CHAIN_v3.md written: 16 stills G00–G15, flat bold 2D
  cartoon, briefs + QC notes. Volley-1 stills generated + eye-verified
  by the coordinator, all 2048x1152 16:9, canonical JPGs in
  work/rebuild/stills_v3/ with md5s in STILL_CHAIN_v3.md: G00
  (bathroom) PASS · G02 (porcelain city) PASS · G15 (five browns)
  PASS · G09 (plunger in clog) PASS · G14 (loop ring) PASS.
  Remaining stills G07, G08, G10–G13 are TODO for volley 4–5
  coordinators (briefs in STILL_CHAIN_v3.md); G01, G03, G04, G05
  landed in volley 2 (recovery run, 2026-11-09 ~04:0x EST), all PASS;
  G06 landed in volley 3 (recovery run, 2026-11-09 ~04:2x EST), PASS
  (md5 b6c5c524…, 2048x1152 — Champion in full TP armour + tall lanky
  adult Squire, quest map unrolling with glowing gold path). G07, G08,
  G10 landed in volley 4 (recovery run, 2026-11-09 ~04:5x EST), all PASS
  (md5s in STILL_CHAIN_v3.md). G11, G12, G13 landed in volley 5 (recovery
  run, 2026-11-09 ~05:1x EST), all PASS (md5s in STILL_CHAIN_v3.md).
  **Still chain COMPLETE: G00–G15, 16/16 PASS.**

## Stage 3 — Volley firing

- **V1 COMPLETE (this run): 5/6 KEEP + 1 REJECT.** IN-A_v3 KEEP ·
  H1-A_v3_city KEEP · H1-B_v3_browns KEEP (trim-in 1.0s — slow open)
  · H2-C_v3_clog KEEP (use 0–8s — tail is an exhausted hold) ·
  O-A_v3_approach KEEP **re-designated as the APEX-WINDOW take**
  (crest ~6.1s by eye, trim-in ≈2.67s, swirl mount correct) ·
  O-A_v3_apex REJECT (mount is a HORSE, not Sir Swirl — G1 fail at
  the video's biggest visual; crest ~4.6s was placeable, the mount
  was not). Full rows + md5s in TAKE_LEDGER_v3.md. Videos used this
  run: 6/6 (cap). Motion gates all PASS (longest frozen run 0–2f at
  native fps). Style note: flight takes read glossy-3D rather than
  flat-2D (anchor-pull) — disclosed, montage tolerates (C2), not a
  re-fire reason.
- **V2 COMPLETE (recovery run, 2026-11-09 ~03:4x–04:1x EST): 5/6 KEEP + 1
  REJECT.** O-A_v3_approach_c2 REJECT (horse mount AGAIN — second O-A horse
  substitution; approach role still open) · H1-A_v3_smears KEEP ·
  H1-B_v3_steps KEEP (use 0–8.5s) · I-A_v3_fibres KEEP · I-B_v3_river KEEP
  · V-0_v3_throne KEEP. Videos used this run: 6/6 (cap). Stills first:
  G01, G03, G04, G05 generated + eye-verified, all 2048x1152, canonical
  JPGs in work/rebuild/stills_v3/ (md5s in STILL_CHAIN_v3.md). QC: ffprobe
  (all 1248x704 24fps 10.000s h264+AAC) + motion audit (qc_v3_volley2.py;
  longest frozen run 0–1f, all PASS) + contact sheets eye-read + full-res
  text scan + RMS on all six + Whisper on the two takes with people (only
  "Thanks/Thank you for watching!" hallucinations — no lyric content).
  Full rows + md5s in TAKE_LEDGER_v3.md.
- **V3 COMPLETE (recovery run, 2026-11-09 ~04:2x–04:5x EST): 6/6 KEEP —
  first clean volley of v3.** O-A approach c3 KEEP (changed axis worked:
  swirl mount correct, 12fps strip shows climb only, no crest — the
  approach role is finally covered) · PH-A_v3_arming KEEP (trim, use
  2.5–4.6s) · I-A_v3_chocoriver KEEP · I-B_v3_gate KEEP ·
  H2-A_v3_departure KEEP · H2-A_v3_ribbon KEEP. Videos used this run:
  6/6 (cap). Stills first: G06 generated + eye-verified, PASS. Full rows
  + md5s in TAKE_LEDGER_v3.md.
- **V4 COMPLETE (recovery run, 2026-11-09 ~04:5x–05:1x EST): 6/6 KEEP —
  second clean volley of v3.** H2-B_v3_pupil KEEP (loose-prompt slot, F12
  glyph watch CLEAR — pupil reflections abstract rings/blobs only, no
  letters; use 0–7.5s) · H2-B_v3_canal KEEP · H2-C_v3_gate KEEP ·
  D-A_v3_duel KEEP (dismounts mid-take — assembly uses mounted opening /
  closing face-off) · D-B_v3_serpent KEEP (cleanest of the volley) ·
  FH-A_v3_flush KEEP. Videos used this run: 6/6 (cap). Stills first:
  G07, G08, G10 generated + eye-verified, all 2048x1152, canonical JPGs
  in work/rebuild/stills_v3/ (md5s in STILL_CHAIN_v3.md). QC: ffprobe
  (all 1248x704 24fps 10.000s h264+AAC) + motion audit (qc_v3_volley4.py;
  longest frozen run 0–2f — all PASS) + contact sheets eye-read +
  full-res text scan (all six f5s frames clean) + RMS on all six (−17.9
  to −28.4 dB) + Whisper on the three takes with people (H2-C gate:
  "Thanks for watching!" hallucination; D-A: generated dialogue "You
  won't get past me!"; FH-A: no words — none lyric content; generated
  audio is dropped at assembly). Full rows + md5s in TAKE_LEDGER_v3.md.
- **V5 COMPLETE (recovery run, 2026-11-09 ~05:1x–05:4x EST): 6/6 KEEP —
  third clean volley of v3.** FH-A_v3_paperstorm KEEP · FH-B_v3_pipeflight
  KEEP (Sir Swirl correct, no horse) · FH-B_v3_citizens KEEP ·
  O-B_v3_dam KEEP · O-B_v3_wave KEEP · O-C_v3_ghostwipe KEEP. Videos used
  this run: 6/6 (cap). Stills first: G11, G12, G13 generated + eye-verified,
  all 2048x1152, canonical JPGs in work/rebuild/stills_v3/ (md5s in
  STILL_CHAIN_v3.md). QC: ffprobe (all 10.000s 24fps h264+AAC) + motion
  audit (qc_v3_volley5.py; longest frozen run 0–1f — all PASS) + contact
  sheets eye-read + full-res text scan (all six f5s frames clean) + RMS on
  all six (−18.5 to −37.7 dB) + Whisper on all six (no lyric content
  anywhere; generated audio is dropped at assembly). Full rows + md5s in
  TAKE_LEDGER_v3.md. **ALL 17 SCENES NOW HAVE KEEP ROWS — volley work is
  DONE; assembly becomes owed.**
- **V5 OWED: NOTHING.** All 17 scenes have KEEP rows. Assembly v3 is owed
  (see Stage 4) — the revive detector / parent chains an assembly
  coordinator next; no further volley firing unless assembly finds a gap.

## Stage 4 — Assembly v3 (owed)

- Segments + kinetic layer v3 (WIPE counter fixed, kinetic words on
  SONG_WORDS_v2.json onsets). No-reuse audit BEFORE encoding (every
  take md5 use-count 1). Split-encode + capped-apad mux (proven v2
  path; NEVER bare apad — `apad=whole_dur=<dur> -t <dur>`).
- Master gates on the delivered master: audio agreement, motion
  audit, positional apex check (frame 3826 ±6f by eye), frame-exact
  4493f, CRF 18 SEI, AAC. House master + 50 MB chat copy. Report:
  md5s/sizes, gates, disclosed flaws, no-reuse audit result. No flag,
  no commit — parent delivers.

## Decisions / rulings log

- 2026-11-09 ~03:0x EST (coordinator): v2-take insert reconciliation
  — the user's "use some of the singer clips if you can timewarp
  them properly" explicitly blesses v2 takes as montage inserts;
  the zero-reuse law is read as banning v2 takes as SCENE footage
  and any double use. 6 inserts, each once, each warp-verified by
  eye, each with full montage coverage underneath. Parent may
  overrule (dropping an insert costs nothing).
- 2026-11-09 ~03:0x EST (coordinator): style lock changed to flat
  bold 2D cartoon — v2's photoreal anchor is judged part of the look
  problem (takes came out photoreal, not cartoon). Fresh still chain
  v3 in the cartoon style; F_HERO_TEST_v2 is NOT an anchor in v3.
- 2026-11-09 ~03:0x EST (coordinator): I-A L8 + FH-B L23/L24/L26
  stay montage (no inserts) — the brown chants are visualizer
  pulses, and FH-B's v2 ratios were edge/missing. Inserts total ~27s
  (~15%), all in-band or rescue-envelope.

- 2026-11-09 ~07:22 EST (parent): v3 DELIVERED. House master md5 ef48baee7ef9e5d8c4b50fbe5b24f8e5 (193,608,471 B, 4493f, crf 18, apex frame 3826 by eye). Chat copy md5 07ee1c9c9df93b3302850e7c1a54ad32 (43,459,184 B, AAC copied, faststart). MV8_V3_DELIVERED.flag written. Assembly coordinator c05ffc29 cancelled ~06:26 EST after building the master; parent finished delivery. Disclosed flaws: v2-insert style mismatch (~27s), three transient PCHIP dips, H2-A 3f freeze, D-A dismount, O-B yellow skin. Awaiting user's playback verdict.

## 2026-11-09 ~08:52 EST — USER VERDICT: MV8 ACCEPTED
v3 is the final cut. MV-8 CLOSED. Do not re-deliver v1, v2, or v3.
