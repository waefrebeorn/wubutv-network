# MV-8 REBUILD — Progress (Stages 1–3 redo, NO video firing)

Governing brief: `MV8_REBUILD_BRIEF_2026-11-08.md`. v1 DELIVERED 2026-11-08 ~02:55 EST,
REJECTED ~02:56 EST (child subject / no lyric linking / bad timing). Remake: ADULTS only,
artsy journey, lilypad-learned visuals, lyric-linked, base music as timing, frame-exact 4493f.
Parent reviews the Stage 3 plan BEFORE any Stage 4 video firing. No chat delivery — parent delivers.

## Stage 1 — re-measure the song as a SUNG track (in progress)

- 2026-11-08 ~03:07 EST: read brief + Slopcannon + video-api-mastery + visual-mv-forms skills
  (all in full), v1 LYRIC_TIMELINE / SONG_WORDS / CRESCENDO_MAP / ASSET_BANK / SCENE_PLAN /
  STILL_CHAIN, wipe research report, @pixhell report, LILYPAD_ROTATION.md.
- Key v1 Stage 1 gap found: v1 `SONG_WORDS.json` (small, beam 1, no VAD) heard NOTHING before
  60.46s — the whole Hook 1 chant (5.97–34.40, 7+ lines) has NO word times, only inferred
  brackets. The tiny model corroborated Hook 1 phrases (8.0–10.46, 12.32–14.16) but was never
  used for word times. Stage 1 redo must recover Hook 1 word onsets.
- Transcription method: `work/rebuild/transcribe_v2.py` (fw-venv, 16 kHz wav input).
  - Pass B (small + sheet initial_prompt + VAD): COLLAPSED — 10 words only (VAD kills the
    music-bed vocal). Lesson: vad_filter=False on this track. Discarded.
  - Pass B2 (small + sheet initial_prompt, no VAD, beam 5): DONE ~03:18 EST —
  86 words, 6 segments. Recovered Hook 1 (L1 7.98–10.76, L2 11.78–14.58,
  Paper 15.34–18.74, Brown brown 20.94–23.14 weak, L3 23.14–26.52,
  L4 28.44–30.28, "Phantom residue stays" 31.70–34.36). Misses the Verse
  (take from v1); Hook 2 head misplaced; hears a line at 124.30–126.48
  (fills a v1 gap); replaces Paper 127.44–130.50 with a repeated hook line
  (v1's Paper has "back" p=1.00 — trust v1); zero-duration burst at 126.48
  (discard); "Turn it. Turn it. Brown brown." 157.72–159.46 almost certainly
  hallucination over the true-peak stabs.
- Pass A (medium, no prompt, no VAD, beam 5): DONE ~03:35 EST —
  154 words, 25 segments (`work/rebuild/SONG_WORDS_v2_medium.json`).
- **ADJUDICATION COMPLETE ~03:40 EST** (`work/rebuild/adjudicate_v2.py`,
  reproducible): canonical `work/rebuild/SONG_WORDS_v2.json` — 135 words,
  span 7.98–146.02. `work/rebuild/LYRIC_TIMELINE_v2.md` (26 lines L1–L26 +
  Drop shout; every divergence flagged) and `work/rebuild/CRESCENDO_MAP_v2.md`
  written. Headline findings: Hook 1 fully recovered (first word 7.98, NOT
  ~6.4); five-brown chants (22.08–24.74, 133.46–136.40); NEW Interlude Brown
  chant L8 36.90–41.84 (medium-only, sheet-supported); "Never clean"
  confirmed performed; performed "you're" variant in later hooks (medium
  p 0.87–0.99; "baby" ad-lib hypothesis DEAD — it was "there"); v1's "The
  water in this pipe" RETIRED (medium+sheet: "Endless wipe forever");
  L16 81.66–83.74 contested (v1 hook fragment wins over B2's sheet-echo
  "Brown brown", B2 probs ~0.00); Outro CONFIRMED instrumental — no lyric
  lines, sheet's Outro "Brown" is sheet-only; B2's "Turn it" discarded
  (zero-duration pile-up at 159.46). **Stage 1 DONE.**
- **Beat grid re-verified 2026-11-08 ~03:30 EST (`work/rebuild/beat_grid_v2.json`, VERIFIED):**
  true peak re-measured EXACTLY 159.435s / −2.16 dBFS; onset-autocorr tempo 123.05 BPM at
  lag 0.4876s (exact match); v1 grid 368 beats, first 5.968, median interval 0.4876s.
  Lyric onsets are NOT beat-locked (v1 words: median |dt| to nearest beat 0.133s, only
  44/112 within 0.10s) — lyric onsets are the primary cut grid in their own right, per brief.

## Stage 2 — adult asset bank + still chain F00–F21 (in progress)

- ASSET_BANK_v2.md written: adult-woman Champion (late 20s, tall/athletic, braid, defined
  cheekbones/jaw), adult Squire redesigned (tall lanky grown man, paper-white tabard — v1's
  small round TP-roll creature RETIRED: reads young), crowds adults-only, worlds/props
  carried from v1, lilypad techniques named (loose-prompt+curation, CRADLE SHOT, Critic loop,
  kinetic type, montage/collage, code-rendered counters, visualizer forms, songs-first).
- **F_HERO_TEST_v2: PASS first try** — `work/rebuild/stills/F_HERO_TEST_v2.jpg`
  (2048x1152, md5 b1081f96a4fbe6fcf7262258dabac087; snapshot
  c270cdb0-0dc7-4e79-b9f0-d15eb2ddef91:vcybnw). Eye-inspected: adult woman, unambiguous;
  mouth open mid-song facing camera; Sir Swirl + TP armour + yellow gloves + plunger +
  shield + cape all on-lock; porcelain palace city golden hour; no text, no children.
  Style reads glossy stylised 3D (slightly more render-real than v1's cartoon — accepted).
  This still is the identity anchor: pass FIRST in every Stage 4 call showing the Champion.
- Still chain F00–F21 delegated to 3 parallel subagents (A: F00–F06, B: F07–F14, C: F15–F21),
  each with the hero-test anchor + per-still specs; each writes its own notes file
  (`work/rebuild/still_notes_<agent>.md`); coordinator assembles STILL_CHAIN_v2.md after
  inspecting all 22 stills personally.
- **Coordinator eye-inspection COMPLETE 2026-11-08 ~03:27 EST — 20 PASS, F00
  PASS-with-wardrobe-note, F16 FAIL.** F00: adult woman, braid, tiled bathroom,
  frosted window — but short white tunic + bare legs on the toilet (re-fire:
  long white trousers). F16: FAIL — Champion reads youthful (round face, big
  wide eyes) + skimpy two-piece TP outfit (bare midriff/thighs); re-fire with
  hero-test adult face + full breastplate + long trousers/skirt. All others
  PASS (F01 sheet ECU; F02 vortex; F03 pipe cathedral; F04 pipe waterslide,
  adult citizens; F05 fibre hills; F06 riverbank rear view — attempt 1
  preserved as F06_attempt1_FAIL.jpg; F07 gate; F08 palace vista; F09 arming
  ring; F10 full armour + adult Squire; F11 first flight rear view; F12 eye,
  abstract neon bokeh, no readable glyphs; F13 pupil canal, neon abstract
  only; F14 night canal, hooded adult figures; F15 plunger-in-clog; F17 vortex
  duel, serpent has NO goggles; F18 serpent close, blurred yellow glove at edge
  harmless; F19 Colossus dam; F20 synchronised flush; F21 Ghost Wipe + adult
  Squire swooning). **Wardrobe variance noted (Stage 4 watch item):** armour
  kit varies between stills (full breastplate F10/F15 vs two-piece F16/F20 vs
  tunic F00/F06/F21) — restate full breastplate + skirt/trousers in every
  Stage 4 vehicle; two-piece is NOT the lock.
- **Re-fires spawned 2026-11-08 ~03:40 EST** (fresh fix agents): F00 → F00_v2.jpg
  (long white trousers); F16 → F16_v2.jpg (hero-test adult face + full
  breastplate + long trousers/skirt). **BOTH LANDED + COORDINATOR-VERIFIED
  ~03:50 EST (recovered from disk; agent handoffs still in transit).**
  F00_v2 md5 6e4709cfc98552721a70ddafd7c6b273 (2096x1184): adult woman, same
  bathroom composition, LONG WHITE TROUSERS, zero bare legs — PASS.
  F16_v2 md5 1f8cd39fcb98b3ca8a616631fd841140: adult face matching the hero
  test, full layered TP breastplate + long-sleeved tunic + full-length white
  trousers, no bare midriff/thighs (nit: small V of skin at collar) — PASS.
  Notes: `still_notes_F00_v2.md`, `still_notes_F16_v2.md`.
- **STILL_CHAIN_v2.md written** — 22/22 canonical stills PASS, all md5s
  verified against disk. Worker-PASS-overrides recorded (agent A marked F00
  PASS, agent C marked F16 PASS; coordinator inspection governs). Failed
  files retained as reference only (F00.jpg, F16.jpg,
  F06_attempt1_FAIL.jpg). **Stage 2 DONE.**

## Stage 3 — new 17-scene plan (WRITTEN, awaiting parent review)

- `work/rebuild/SCENE_PLAN_v2.md` written 2026-11-08 ~03:45 EST. 17 scenes
  tiling 0.00–187.20, frame counts summing to exactly 4493f (verified by
  addition in the doc). Scene spans re-derived from the adjudicated lyric
  onsets (v1's spans adjusted where lines straddle them: H1-A ends 22.08 at
  the Browns; H1-B ends 34.96 at L7's end; H2-A ends 81.08 at L15's end;
  D-B ends 120.06 at L20's onset; FH-A ends 133.46 at L23's onset).
- Every lyric line L1–L26 + the Drop shout linked to a scene; un-linkable:
  none. Flagged lines staged to work under either reading (L16 hook
  fragment + Brown-counter accent; L19 staged on the "never stops" tail;
  L26 "(Phantom wipe)" tag as a Ghost Wipe flicker before the core).
- **True-peak landing (hard requirement):** loop-the-loop apex ON frame 3826
  (159.435s), 322f into O-A; verification stated in the plan (extract frame
  3826 ± 12f from the assembled master; apex must be the local motion
  extreme within ±6f, else re-cut). v1 missed it by 11–12s — not repeated.
- Sung scenes are SINGING (performance-window, mouth-open on the line);
  instrumental scenes are JOURNEY with continuous motion. v1's designed-held-shot
  precedent is DEAD (D-B is the explicit motion-proof scene).
- Lilypad techniques named per scene (CRADLE SHOT: D-A + O-A; loose-prompt +
  strong curation slot: H2-B; Critic loop on visual slots; kinetic type;
  montage/collage; code-rendered WIPE counter; visualizer-form Brown pulses).
- Casting decision recorded in the plan: Champion = F_HERO_TEST_v2 adult
  woman (the voice made visible); Squire = tall lanky grown man (v1's small
  round creature retired); crowds adults-only.
- **Parent reviews casting, lyric coverage, true-peak landing BEFORE any
  Stage 4 firing.** Firing order in the plan (volley 1: H1-A + IN-A + D-B).

## Timing contract (standing)

- Master exactly 4493 frames / 187.200s. Cuts on lyric onsets + beat grid (123.05 BPM, to be
  re-verified). True peak 159.435s carries the biggest visual. No frozen-lead-in takes.
- Adults only, everywhere. No children in any frame, ever.

## Stage 4 — Volley 1 firing (parent-approved plan, 2026-11-08 ~05:36 EST)

- Parent reviewed SCENE_PLAN_v2.md and approved Stage 4. Firing coordinator spawned.
- Volley 1 (proof of look): H1-A c1 (10s, L1+L2) + H1-A c2 (5s, L3 + sheet prop) + IN-A (10s, F00_v2→F01) + D-B (10s, F17→F18, motion proof).
- Vehicles written to work/rebuild/vehicles/ (mv8_v2_h1a_c1/c2/ina/db_vehicle.txt) before firing, per Stage 4 discipline. Ledger: work/rebuild/TAKE_LEDGER.md.
- Ref read-back note (firing coordinator, before first call): F_HERO_TEST_v2 is photoreal while the world stills are glossy cartoon — vehicles state the cartoon style lock in text and the hero image is used as identity anchor only. Its outfit is the two-piece the plan bans; every vehicle restates full breastplate + long trousers. F00_v2 is cartoon + fully covered (long white trousers) — clean. F17/F18 clean as anchors.
- H1-A c1 fired first (chorus-hook test: SINGING proof gates the rest).

- H1-A c1 **KEEP** (2026-11-08 ~05:45 EST): takes/H1-A_v2_c1.mp4, md5 038bcb6e6f03f9ac54222541ea5d6f37, 10.000s, 1248x704. Sings L1+L2 complete, ratios 0.99/1.22, motion 26.7–44.9 diff throughout, mouth open at onsets. DISCLOSED: photoreal (anchor-faithful, not cartoon lock); bare thighs in opening wide shots (anchor's outfit; adult read unambiguous). Parent to rule on both.

- H1-A c2 **KEEP**: takes/H1-A_v2_c2.mp4, md5 ef285462f2da547050d3e449b8ccbde5, 5.000s. "PAPER COMES BACK DIRTY" complete; ratio 1.57 grey, rescue-envelope warp disclosed; mouth open at PAPER + DIRTY. Zigzag marker-stroke nit disclosed.
- IN-A **KEEP**: takes/IN-A_v2.mp4, md5 fb94bb1d56a64233241bd769b3041c65, 10.000s. Bathroom → vortex → sheet; motion strong in the used 0–6s window; tail hold outside scene span. Zigzag-stroke nit disclosed.
- D-B **KEEP**: takes/D-B_v2.mp4, md5 0f231211f5c0788d9e126a93ad189c56, 10.000s. Motion-proof scene delivers: push underway at frame 0, strongest motion of the volley. Serpent end-frame reads angry, not smug — disclosed.
- **VOLLEY 1 COMPLETE: 4/4 KEEP** (H1-A c1, H1-A c2, IN-A, D-B). Videos used this run: 4/6 (2 spare, unspent). Next volley owed (plan order): H1-B, I-A, I-B, V-0, PH-A, H2-A — parent chains the next coordinator.

## Stage 4 — Volley 2 firing (2026-11-08 ~05:47 EST)

- Firing coordinator spawned by parent ~05:47 EST (volley 1 was 4/4 KEEP; disk-verified, report never arrived).
- Volley 2 (journey order): H1-B, I-A, I-B, V-0, PH-A, H2-A — 6 videos, the run cap.
- Vehicles written to work/rebuild/vehicles/ (mv8_v2_h1b/ia/ib/v0/pha/h2a_vehicle.txt) before firing, per Stage 4 discipline. QC: ffprobe + faster-whisper-small transcription (fw-venv) + RMS envelope + 0.5s contact sheets, eye-read. QC tooling: work/rebuild/qc/qc_volley2.py.
- H1-B **KEEP**: takes/H1-B_v2.mp4, md5 9b4ecad69db38dccd21372ee7947154d, 10.000s. Six browns + one hook line + L7 complete; L4 0.92, L6 0.85, L5 → montage, L7 2.46 (mouth open at Phantom + stays; Phantom-hold interval exceeds warp caps — assembly montages or re-cuts). Motion 29.8–44.2.
- I-A **KEEP**: takes/I-A_v2.mp4, md5 07e217473b36c8d50c3204e744d18fd9, 10.000s. Six browns (one extra), L8 0.86, then journey tail. Motion 34.0–55.0.
- I-B **KEEP**: takes/I-B_v2.mp4, md5 0c1115afd36abbefb71e2a03ad60a09b, 10.000s. Journey, no words ("Thank you for watching!" is a Whisper hallucination, p=0.0). Pipe flight → gate → golden city. Motion 16.6–50.5.
- V-0 **KEEP**: takes/V-0_v2.mp4, md5 cd2e25fc04eff15551b04d6ae899af05, 5.000s. L9 1.43 (grey; "Toil Brown" hearing disclosed, leaning "toilet" mishear), L10 0.93. Throne-slam present ~2.9s. Motion 34.5–55.3.
- PH-A **KEEP**: takes/PH-A_v2.mp4, md5 386582de4de57abc521be5f99e2598ce, 5.000s. "Wipe, wipe again" complete; ratio 0.34 (~3x speedup, disclosed); quiet take vocal (max RMS 0.07), mouth-gated. Motion 32.3–47.8.
- H2-A **KEEP**: takes/H2-A_v2.mp4, md5 1a32c173ee5ecab6196c8df8e4a0840e, 10.000s. L12 0.84, L13 1.18; L14 MISSING → montage; L15 2.73, mouth not visible → montage or 2x-capped warp. Departure with adult Squire, Critic loop 8+. Motion 25.9–47.5.
- **VOLLEY 2 COMPLETE: 6/6 KEEP** (H1-B, I-A, I-B, V-0, PH-A, H2-A). Videos used this run: 6/6 (cap). Next volley owed (plan order): H2-B (loose-prompt slot, F12 glyph watch ACTIVE), H2-C, D-A, FH-A, FH-B, O-A (true-peak apex frame 3826 — fire early enough to re-fire if the apex misses) — parent chains the next coordinator.

## Stage 4 — Volley 3 firing (2026-11-08 ~06:47 EST, RE-FIRE ~06:53 EST)

- First volley-3 coordinator (66a6e089) spawned ~06:47 EST and died on a runtime transport error minutes later with ZERO disk footprint (no vehicles, no takes, no ledger rows; progress untouched since volley 2's 06:01 EST completion). Parent spawned a clean re-fire (2b63fd88) from the same brief.
- Volley 3 (plan order): H2-B (loose-prompt slot, F12 glyph watch ACTIVE), H2-C, D-A, FH-A, FH-B, O-A (true-peak apex frame 3826).
- Vehicles written to work/rebuild/vehicles/ (mv8_v2_h2b/h2c/da/fha/fhb/oa_vehicle.txt) before firing, per Stage 4 discipline. O-A fired FIRST (apex risk — re-fire slot kept open if the apex misses). QC: ffprobe + faster-whisper-small transcription (fw-venv) + RMS envelope + 0.5s contact sheets, eye-read. QC tooling: work/rebuild/qc/qc_volley2.py pattern (adapted per volley).
- O-A take 1 **REJECT — apex miss** (2026-11-08 ~07:0x EST): takes/O-A_v2.mp4, md5 78181f6dd006aebb08d4bef96031518a, 10.000s, 1248x704. Otherwise strong (motion min 24.3/mean 41.4, no words, no text, adult) BUT loop apex at ~2.0s into the take (second crest ~4.0s); assembly needs >=6.71s — no warp within the rules reaches frame 3826. Re-fire ordered with climb-first-seven-seconds vehicle (mv8_v2_oa_r2_vehicle.txt). Cost: the re-fire takes one of the volley's 6 video slots, so **D-A slips to volley 4** (with O-B + O-C; 3 scenes, 3 spare slots). Volley 3 fires: O-A re-fire, H2-B, H2-C, FH-A, FH-B.
- O-A take 2 (re-fire) **REJECT — apex miss, improved** (2026-11-08 ~07:1x EST): takes/O-A_v2_r2.mp4, md5 7a181682c95b6d2a0191f27331512637, 10.000s. Loop ring beautiful, dive clean, motion min 20.6/mean 45.3 — but the rider crests the ring top at ~5.5–6.0s, still short of >=6.71s (max 2x slow-down maps 5.75s → 157.5s, 1.9s early of 159.435s). LESSON: in both attempts the two-image morph pulls the F02 vortex in at ~7.0s and front-loads the loop. **Attempt-3 design (volley 4): single-anchor F11, NO F02 second image — prompt the loop top into the FINAL TWO SECONDS (~8s) with the dive implied; the apex must sit at ~7.9s in the take.** O-A is the only scene without a KEEP after volley 3.
- H2-B **KEEP**: takes/H2-B_v2.mp4, md5 ae6ac6992671a5285ee4354b49cd875a, 10.000s. Both lines complete (L16 0.96, L17 1.35 grey); mouth open at both onsets; F12 glyph watch CLEAR at full res (pupil frames 4.5s/5.0s: abstract highlight only, no letters). Motion 34.5–52.8.
- H2-C **KEEP**: takes/H2-C_v2.mp4, md5 69c2d596a0e1e5996739875645536347, 10.000s. L18 1.82 (edge, past rescue envelope, inside 2x floor) + L19 1.34; "Wife" = Wipe/Wife ASR confusion; mouth open at L18 onset, L19 tail-gated. DISCLOSED: L18 starts at take 0.0 — assembly covers the 2.52s scene lead from H2-B's tail, never holds the opening frame. Motion 16.9–57.8 (tail settle onto the gate).
- FH-A **KEEP**: takes/FH-A_v2.mp4, md5 d8feb2c833c915631cbcc0e3a96f2681, 10.000s. L20 1.16; L21 "there" MISSING (confirmed by full + trimmed re-transcription, no RMS burst) → montage; L22 core 2.07 (2x-capped warp). Mouth open at all three onsets. DISCLOSED: wardrobe variance (sleeveless TP-roll pauldrons, bare arms, collar V). Motion 28.2–54.7.
- FH-B **KEEP**: takes/FH-B_v2.mp4, md5 67f6f8fc5d43e0799799b6b4cc5fc2eb, 10.000s. Five browns + one hook line + "Endless wipe forever"; L25 MISSING → montage (same pattern as H1-B L5 / H2-A L14); Ghost-wipe flicker visible at 6.0s (tag delivered visually). Ratios L23 0.77, L24 1.73, L26 core 0.72. Motion 34.2–63.8.
- **VOLLEY 3 COMPLETE: 4/5 KEEP + 1 REJECT (O-A r2, apex miss) + 1 REJECT carried in (O-A take 1). Videos used this run: 6/6 (cap).** 14/17 scenes now have KEEP takes (IN-A, H1-A, H1-B, I-A, I-B, V-0, PH-A, H2-A, H2-B, H2-C, D-B, FH-A, FH-B + H1-A c2). Owed next — volley 4: D-A (slipped), O-B, O-C + O-A attempt 3 (single-anchor design above). Then assembly (frame-exact 4493f, CRF 18/AAC/faststart, ≤50 MB chat copy, frame-3826 apex gate).

## Stage 4 — Volley 4 firing (2026-11-08 ~15:0x EST)

- Firing coordinator spawned by parent ~15:00 EST. Volley 4 (plan order, apex risk first): O-A attempt 3 (single-anchor F11 design, banked from volley 3), D-A (slipped from volley 3), O-B, O-C. Cap 6 videos; 4 scenes = 4 generations, 2 spare slots for re-fires.
- Vehicles: work/rebuild/vehicles/mv8_v2_oa_r3_vehicle.txt (DRAFT finalized — single-anchor F11, NO F02, climb-first-seven-seconds, loop top final two seconds ~8s), mv8_v2_da_vehicle.txt (written volley 3, reviewed vs plan D-A: F16_v2→F17 cradle shot, serpent no goggles), mv8_v2_ob_vehicle.txt + mv8_v2_oc_vehicle.txt (DRAFTs finalized — reviewed vs plan: O-B F19→F20 loudest cluster + stab-run reveals; O-C F21→F00_v2 WIPE 001—CLEAN reset, final frame rhymes with F00). All anchors md5-verified against disk before firing.
- QC: ffprobe + faster-whisper-small transcription (fw-venv) + RMS envelope + 0.5s contact sheets, eye-read. Apex gate (O-A, take-level, before KEEP): crest frame must sit at >=6.71s in the take, target ~7.9s.
- O-A take 3 **REJECT — apex miss (improved, closest yet)** (2026-11-08 ~15:1x EST): takes/O-A_v2_r3.mp4, md5 5ad305b4095e9a81abad5437ef33d4ce, 10.000s. No words, motion min 32.1/mean 42.0. Climb 0–5s beautiful; rider crosses the ring crown at ~6.5s (tipping over by 6.75s) — short of the >=6.71s gate (2x maps to 159.0s, 0.435s early). Ring still front-loads (water wall enters ~2s despite "no ring yet" instruction). Attempt-4 design: NEW AXIS — temporal embargo (ring invisible until ~9s, crest ~9.5s); single-anchor F11 kept.
- O-A take 4 **REJECT — apex miss** (2026-11-08 ~15:2x EST): takes/O-A_v2_r4.mp4, md5 1c2aff6c97250bc930d742ce7bc4f643, 10.000s. No words, motion min 24.8/mean 41.1. Rider flies over the ring, crest ~6.25s (crown 6.0–6.5s, descending from ~6.5s) — short of the >=6.71s gate. The temporal-embargo axis FAILED: ring visible from ~2s despite the explicit embargo; the generator places the loop climax in the 55–65% window of any 10s take regardless of timing language. Four attempts (2.0 → 5.75 → 6.5 → 6.25s) — prompt-tuning has hit a ceiling. **O-A STOPS per brief; parent decides next** (split-scene apex-window take, code/Blender apex, or gate ruling). Best apex candidate remains take 3 (6.5s). Volley 4 continues: D-A, O-B, O-C.
- D-A **KEEP**: takes/D-A_v2.mp4, md5 44c889e24b8f67db376d44643ccea776, 10.000s. Cradle shot: gate → vortex → serpent face-off; motion min 40.7/mean 54.1; serpent NO goggles. DISCLOSED: take audio invents "Now, face me, Serpent!" 6.1–7.94s (instrumental scene, audio dropped at assembly); serpent enters ~5.5s, duel joined at the span's end, D-B continues it.
- O-B **KEEP** (recovery 2026-11-08 ~16:26 EST): takes/O-B_v2.mp4, md5 a0d7b077d996219ca4fbf77472d3a2ae, 10.000s. Dam → wave → city wash; motion min 22.4/mean 41.5. DISCLOSED: take audio invents "Let's clean this city!" 6.44–7.9s (instrumental scene, audio dropped at assembly). No text at full res. Recovery continues: O-C fire next.
- O-C **KEEP** (recovery 2026-11-08 ~16:30 EST): takes/O-C_v2.mp4, md5 015fa8595b03c7bb7ff560dbd4984704, 10.000s. Sheet + Squire → vortex → F00 bathroom rhyme; motion min 13.0/mean 35.7 (tail settle 9–10s outside the 7.20s span, assembly trims). DISCLOSED: "end of the video" transcription is a Whisper hallucination (I-B precedent); wardrobe variance — short sleeves, TP rolls on the back (FH-A/FH-B precedent). **VOLLEY 4 COMPLETE: 5/6 videos used (O-A r3, O-A r4, D-A, O-B, O-C); verdicts: D-A KEEP, O-B KEEP, O-C KEEP, O-A r3/r4 REJECT (apex miss — O-A STOPS per brief, parent decision pending). 16/17 scenes now have KEEP takes; O-A is the only scene without a KEEP.** Parent: verify + commit at the volley boundary; assembly is blocked only on the O-A decision.

## Stage 4 — O-A split (user decision 2026-11-08 ~18:49 EST: SPLIT THE APEX SCENE)

- Split coordinator spawned by parent ~18:51 EST. Vehicle: work/rebuild/vehicles/mv8_v2_oa_split_apex_vehicle.txt (NEW AXIS — apex-window / mid-climb start: rider already high at frame 0, ring already ahead; single-anchor F11 only, NO F02). 1 video used this run (cap 6).
- O-A split apex **KEEP**: takes/O-A_v2_split_apex.mp4, md5 176da2ac05bb4a5af24ae804badb62d0, 10.000s, 1248x704, 24fps, h264+AAC. Crest measured BY EYE at 5.50s (take frame 132; frame 130 still ascending, frame 134 already tipping over — apex bracketed ±2f). No words (transcription empty). Motion min 23.4/mean 41.0. Adult woman, matches anchor. No text, no child. DISCLOSED: mount wears goggles (O-B precedent); ring visible from ~0.5s (front-load persists) but the take is used only from 2.083s in.
- ASSEMBLY MATH (verified on a built 408f proxy, work/rebuild/qc/oasplit/assembly/oa_assembled_408f.mp4, md5 5bc2ccd2020ca546753d33a36550e4c2): approach = take 3 frames 0–143 (0–6.0s, pre-crest) warped 1.667x to 240f = 146.00–156.00 (split point 156.00s / frame 3744); apex = split-apex take frames 50–217 (2.083–9.083s) = 168f = 156.00–163.00; crest lands at in-window frame 82 = segment frame 322 = song frame 3826. Total 240f + 168f = 408f exactly. Positional apex verified by eye ON frame 3826 (offset 0f, ±2f).
- VERIFICATION CAVEAT (for the parent at assembly): the frame-diff-peak test as written in SCENE_PLAN_v2 does NOT show a local peak at 3826 — full-frame diffs rise monotonically 8.6→26 across segment frames 285–365 (peak seg 364, +42f); crown-crop diffs flat ~11 then rising from 320. The dive accelerates after the crest, so the diff peak sits structurally downstream of any loop crest. No re-cut attempted: no trim puts the diff peak on 3826 without moving the real apex off it. Parent ruling needed on the diff-peak proxy before the master gate.
- **17/17 scenes now have KEEP takes. O-A is closed at the take level; assembly is unblocked except for the diff-peak-proxy ruling above.** Next: assembly (frame-exact 4493f, CRF 18/AAC/faststart, ≤50 MB chat copy, frame-3826 apex gate) — parent chains. No MV8_V2_DELIVERED.flag exists yet. Do NOT commit (parent commits at the volley boundary).
- **PARENT VERIFICATION + RULING (2026-11-08 ~19:40 EST):** split coordinator's report never arrived as a handoff (stored record shows it completed ~19:03 EST); parent recovered from disk and verified independently — apex take md5 176da2ac05bb4a5af24ae804badb62d0 matches ledger, ffprobe 1248x704 24fps 10.000s h264+AAC; proxy oa_assembled_408f.mp4 md5 5bc2ccd2020ca546753d33a36550e4c2 matches; assembly math re-checked (take-3 frames 0–143 ×1.667 = 240f; apex frames 50–217 = 168f; 240+168 = 408f; crest in-window frame 82 = segment frame 322 = song frame 3826; O-A starts song frame 3504, 3504+322 = 3826 ✓); parent eye-read the proxy crest strip (segment frames 318–326) — rider crosses the crown at frame 322, ascending before, descending after, offset 0f ±2f. **RULING: the apex gate is SATISFIED on positional eye verification (within the ±6f tolerance). The frame-diff-peak proxy is RETIRED for dive-after-crest geometry — frame-diff magnitude measures post-crest acceleration, so its peak sits structurally downstream of any loop crest (here seg 364, +42f); chasing it would move the real apex off 3826. Assembly must NOT re-cut O-A to chase the diff peak. The master gate still verifies the apex positionally on the delivered master (extract 3826 ±12f, crest within ±6f by eye).** Assembly unblocked; parent chains the assembly coordinator. (Split work already in HEAD via Q1 1915 commit 970c7c32's `git add -A` sweep — no separate parent commit needed.)

## Stage 5 — Assembly (recovery #3, 2026-11-08 ~22:23 EST – 2026-11-09 ~01:50 EST)

- Assembly coordinator #1 (a4967f48) died ~20:10 EST on a daemon restart with ZERO footprint. Coordinator #2 (57724a69) died 22:17:30 EST on a daemon restart after leaving take-side word times (qc/words_take/, 11 files), the segment plan + WIPE decision (assembly_notes.md), and the builder (assembly_build.py, 411 lines). Recovery #3 (322b027e, spawned ~22:23 EST) resumed from disk: verified all 17 KEEP take md5s, measured the IN-A tail motion (settles <5 after ~7s — H1-A lead covered from the c1 tail, not the IN-A tail, per the motion law), fixed the FH-A L22 PCHIP slow (replaced with uniform 0.5x, 2x cap), built all 17 segments (4493f exactly), built the kinetic layer (mv8_kinetic_v2.ass, 632 events), and wrote assembly_final.py.
- **Pass 1 (full encode, ffmpeg PID 40409):** killed by VM reboot #10 (2026-11-09 04:43:15 UTC) at ~99% — partial master 225,181,744 B, mdat present, NO moov atom (unplayable). Preserved aside as work/rebuild/assembly/master_partial_no-moov_20261109-0443.mp4.
- **Pass 2 (re-encode, ffmpeg PID 6107, 81m33s):** encoded all video data (423,690,293 B) then died at the trailer — `Error writing trailer: Cannot allocate memory` (exit 244). No moov. Preserved aside as work/rebuild/assembly/master_partial_no-moov_20261109-0616_OOM.mp4 (video data complete, recoverable via untrunc if ever needed). Cause: memory pressure (load spiked 18.74, 407 MB swap in use).
- **KEY FINDING:** the single-pass full encode INFLATED the stream — pass 2 wrote 424 MB for what the split proves is ~120 MB of video at the same CRF 18. The inflation came from the full command's audio+apad path, not the segments or concat list (both verified clean).
- **Split encode (the working path):** split at the FH-B/O-A boundary (146.00s) via work/rebuild/split_encode.py. Half 1 (IN-A..FH-B) 3504f, 92,431,678 B, 5m22s; half 2 (O-A..O-C) 989f, 28,044,709 B, 1m35s; both ffprobe-verified. Total video 120,476,387 B for 4493f. Banked as work/rebuild/assembly/master_part1.mp4 + master_part2.mp4.
- **Mux attempt 1:** stream-copy halves + track audio + plain `apad` (no cap) — killed by VM reboot #11 (~06:38 UTC, SIGTERM) ~2.5 min in. Video perfect (4493f) but AUDIO RUNAWAY: AAC 27555.306s / 1,291,656 frames — `apad` pads INDEFINITELY and, without `-shortest`/`-t`, the muxer keeps writing silence after the video ends. **Standing lesson: never use bare `apad` in a master mux — always cap it (`apad=whole_dur=<dur> -t <dur>`).** The same flaw was in the original assembly_final.py command and likely contributed to pass 2's ENOMEM. Broken 138 MB mux deleted.
- **Mux attempt 2 (SUCCEEDED, 2026-11-09 ~06:41 UTC / 01:41 EST):** `ffmpeg -y -v error -f concat -safe 0 -i work/rebuild/assembly/final_concat_halves.txt -i track.mp4 -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -ar 48000 -ac 2 -af apad=whole_dur=187.208 -t 187.21 -movflags +faststart masters/mv8_wipe_and_its_still_there_v2_16x9.mp4` — exit 0, 6.48s, 125,117,565 B, md5 **999da67b92da6ec390efbd851497166f**.
- **MASTER GATES (gate_master.py, ALL PASS):** frames exactly **4493**; duration 187.208333s; h264 1280x720 24fps; AAC 48k stereo; x264 SEI crf=18.0 (two lines, one per half); faststart moov@36 mdat@130340; master-audio agreement vs track.mp4 min corr **0.9978** (5 windows: 0.9978 / 0.9991 / 0.9988 / 0.9989 / 0.9992, all > 0.99).
- **APEX POSITIONAL CHECK (by eye, master frames 3814–3838, work/rebuild/qc/apex_master/):** frame 3824 ascending, frame 3826 AT the crest (rider at the top of the loop), frame 3828 just past crest / tipping over. **Offset 0f** — crest on song frame 3826, inside the ±6f gate, matching the parent-verified proxy (0f ±2f). No diff-peak test applied (retired). WIPE counter verified against beat_grid_v2.json: WIPE 320 active at 159.4167s, ticks to 321 at 159.470; all 346 WIPE events match beat_index+2 with ZERO mismatches. "~ WuBu ~" bug visible bottom-right; Champion is the adult woman; motion present at the apex.
- **CHAT COPY:** masters/mv8_wipe_and_its_still_there_v2_16x9_50mb.mp4, 44,595,557 B (42.5 MB), md5 **8639625f6af9f81212c72fb455002340**, 4493f, h264 1280x720 24fps, AAC copied untouched, faststart moov@36 mdat@130319. Encode: libx264 preset medium -b:v 1700k -maxrate 2000k -bufsize 4000k, -c:a copy, 4m28s.
- **Disclosed flaws carried to delivery:** FH-A L22 words land early at the 2x cap (comes −0.90s, back −0.72s, dirty −0.60s); H2-C L18 words land −0.5 to −1.5s (mouth runs ahead); four transient PCHIP dips 2–7f at 0.43–0.49x (least-bad smooth warps); WIPE counter 347 lands at beat 345 (171.851s) per the corrected numbering; volley disclosures in TAKE_LEDGER.md (wardrobe variances, invented take audio dropped in D-A/O-B, goggles notes, F12 CLEAR).
- **ASSEMBLY COMPLETE.** Master + chat copy verified and on disk. No commit, no delivered flag — parent writes MV8_V2_DELIVERED.flag at the delivery boundary. **v1 (masters/mv8_wipe_and_its_still_there_16x9.mp4, md5 b9d30c32) stays REJECTED — never re-deliver.**

## Stage 6 — v3 Assembly (recovery, 2026-11-09 ~05:25 EST)

- Revive-detector spawn: no v3 assembly coordinator had ever started; v2 master
  COMPLETED ~02:30 EST; volley 5 finished all v3 takes 05:22:50 EST; assembly
  idle since — revive #1 this episode.
- INPUTS VERIFIED: track.mp4 md5 8a4834d2e647fffce6782a3461baa936 ✓; all 28 v3 KEEP
  md5s match TAKE_LEDGER_v3.md ✓; all 6 v2 insert md5s match ✓; all 14 v3
  *_words.json parse ✓ (montage takes need no word times — kinetic layer
  carries words on the song grid; inserts reuse v2's verified PCHIP anchors).
- O-A CREST RE-MEASURED BY EYE (fresh v3 apex-window take O-A_v3_approach):
  5.96 still ascending, 6.04 AT the crown top-left, 6.13 tipping over,
  6.21 descending — crest = take 6.04s (frame 145). Trim-in 2.605s puts the
  crest at in-window 3.435s = segment frame 322 = song frame 3826 (±1f).
  v2 md5s (apex 176da2ac…, proxy 5bc2ccd2…) are v2 reference only, NOT used.
- D-A CHECKED (2fps strip): she dismounts ~1.0s and grapples on foot — the
  ledger's "mounted opening" is only ~1s. Decision: single contiguous span
  take 0-6.29s natural (lunge + grapple reads as fight choreography);
  NO two-span stitch (no-reuse law). Disclosed.
- SEGMENT PLAN (assembly_build_v3.py, analyze exit 0): montage takes at
  natural speed / uniform fit (all speeds >= 0.5); 6 inserts on v2 PCHIP
  anchors; INS-4 first anchor moved 63.62 -> 63.00 (adjudicated L10 onset;
  v2 placed it 0.62s late); H2-A 3f freeze lead on take frame 0 (no-word
  window, keeps proven L12 anchors + strict once-only); O-A split as above.
  CAP AUDIT: two exact-0.50 uniform flags (float artifacts, allowed);
  three transient PCHIP dips IDENTICAL to v2's disclosed set (H2-B L16
  0.43/2.8f, L17 0.48/3.8f, FH-A L20 0.49/2.4f; every interval mean >= 0.5)
  — KEPT, disclosed. H1-A 1f drift fixed by builder (last-piece +1f).
- Segments build into work/rebuild/assembly_v3/seg/ (v2 assembly/ untouched).
  Split-encode path from the start (v2 lesson: single-pass OOM'd at trailer).
- ALL 17 v3 SEGMENTS BUILT (assembly_build_v3.py, assembly_v3/seg/, CRF-14
  intermediates, ffprobe-verified per segment; total 4493f exactly):
  IN-A 143 ba7a0bd9cac1 · H1-A 387 c7ab13a7dbe5 · H1-B 309 82a5ba18b3b8 ·
  I-A 253 12bc7f3da7e7 · I-B 359 65923070e580 · V-0 112 (REBUILT with v2
  anchors verbatim — see INS-4 note below) · PH-A 51 77751b3d9c4c ·
  H2-A 332 b39c439e4c6e · H2-B 286 42f262b4f8fb · H2-C 311 ebdd497af36d ·
  D-A 151 4aac5c53f957 · D-B 187 df3bb3a3bcfd · FH-A 322 4d364ac04360 ·
  FH-B 301 d458d6e75535 · O-A 408 47e412703dde · O-B 408 758983c8bca0 ·
  O-C 173 d59a2e7e2e4c.
- BUILDER DEATH + RECOVERY (mid-run): the first nohup'd builder launch died
  ~10:37 UTC during the I-B raw decode (raw file frozen at 4,980,736 B,
  ~2 frames — orphaned nohup child reaped when its exec session ended).
  Lesson: NEVER nohup a long build — run it as a runtime-managed foreground
  exec (python3 -u ...) so the session supervises it. Relaunched that way;
  it skipped the 4 built segments and finished 17/17 in ~12.5 min.
  Partial raw deleted before relaunch (a truncated .raw would have been
  silently misread as a 1-2 frame take).
- INS-4 CORRECTION (caught before encoding): the first V-0 build placed
  L10's first word at 63.00 (my shift). SONG_WORDS_v2.json (canonical word
  list) puts it at 63.62 (medium); LYRIC_TIMELINE's "63.00" mixes witnesses
  (v1 onset + medium L9 end 63.30 = phantom overlap). v2's 63.62 placement
  matches the canonical words AND the kinetic highlight. REVERTED to v2's
  anchors verbatim; throne montage runs 60.46-63.62 (76f), insert 63.62-65.00
  (33f) + 3f tail to 65.12. Mouth/kinetic agree at 63.62. (The foreground
  builder run already carried the fix — the "rebuild" re-produced the
  identical segment md5 163c7c09e4a2c179b84fb451c16fe6ee.)
- NO-REUSE AUDIT (audit_v3.py): PASS. No take-time interval overlaps;
  all 28 KEEP + 6 inserts used, 0 unused, 0 REJECT takes in cut.
  Disclosed exception: H2-A_v2 3f freeze repeats take frame 0 (single held
  frame, no-word window).
- KINETIC LAYER v3 BUILT (build_kinetic_v3.py → assembly_v3/mv8_kinetic_v3.ass,
  627 events, 27 lyric lines, 135 words): CASCADE on L4/L8/L23 five-Brown
  chants; STACK on L3/L22 Paper lines; SLAM on hook-block openers L1/L12/L20;
  HIGHLIGHT default; one-off slams WIPE AGAIN 66.48, WIPE! 105.94,
  STILL THERE! 112.25 (v2 form kept). WIPE counter FIXED: displayed =
  beat_index+1 (001 @0.00, 001 active at beat 0, 346 @beat345 171.851s,
  last beat 182.346 -> 368, reset 001-CLEAN 183.00-185.50, 001 to 187.20).
  Counter verification: 0 mismatches. NOTE: .ass timestamps round to
  centiseconds, so beat times are stored ±5ms early — imperceptible, same
  as v2. NOTE: kinetic word times come from SONG_WORDS_v2.json; L10's first
  word highlights at 63.62 (canonical), matching the insert mouth.

## Stage 7 — DELIVERY (parent, 2026-11-09 ~07:22 EST)
- Assembly coordinator c05ffc29 was CANCELLED ~06:26 EST with no final report, but its work LANDED: 17/17 segments (4493f), kinetic v3, split halves, house master. Parent verified the master from disk (h264 1280x720 24fps, 4493f, 187.208s, AAC, SEI crf=18.0 x2, faststart moov@36, md5 ef48baee7ef9e5d8c4b50fbe5b24f8e5) and eye-checked the apex tile (swirl mount, rider at crown on frame 3826, WIPE 318->320 ticking, ~ WuBu ~ bug) and the mouth tile (inserts open-mouthed at word onsets).
- The 50 MB chat copy the coordinator was encoding died with it (44,302,384 B, no moov). Parent re-encoded with the v2 recipe (libx264 medium -b:v 1700k -maxrate 2000k -bufsize 4000k, AAC copied, faststart): 43,459,184 B, md5 07ee1c9c9df93b3302850e7c1a54ad32, 4493f, audio md5 identical to house master (9825074e71692e4715dce62b1d9ad77b).
- MV8_V3_DELIVERED.flag written. Disclosed flaws at delivery: (1) style mismatch — 6 v2 inserts glossy-3D vs flat bold 2D v3 montage (~27s); (2) three transient PCHIP dips (H2-B L16/L17, FH-A L20, interval means >=0.5); (3) H2-A 3f held frame (take frame 0, no-word window); (4) D-A dismount ~1.0s into duel; (5) O-B dam close shots: Champion's skin bright yellow.
- Awaiting the user's playback verdict — verdict outranks all gates. v1 and v2 delivered and rejected; never re-deliver either.
