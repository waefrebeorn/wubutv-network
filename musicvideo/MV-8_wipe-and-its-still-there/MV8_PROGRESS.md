# MV-8 Stage 1 progress — timeline + crescendo map (audio analysis only)

Track: track.mp3 md5 63799741a41e9c2c9082d8c57b4f18d0, 187.200s, AAC→MP3 48k stereo (source track.mp4).
Tooling: ~/workspace/fw-venv (faster-whisper 1.2.1, librosa 1.0.0, scipy).

## Deliverables
- [x] SONG_WORDS.json — faster-whisper (small) word timestamps
- [x] work/beat_grid.json — MV-7 make_beat_grid.py reused verbatim (3 tempo witnesses)
- [x] work/CRESCENDO_MAP.md + work/crescendo_map.json — onset/stab list, 0.5s RMS energy curve, ramps, silence gap, loudest moment
- [x] LYRIC_TIMELINE.md — section boundaries + per-line times, confidence tags
- [x] Commit (explicit paths), message "MV-8 stage 1: timeline + crescendo map"

## Log
- Stage 1 started. DIRECTION.md + lyrics.txt + Slopcannon SKILL.md + references/timeline.md read. NO singing character — sync = stab/crescendo; mouth machinery N/A.
- Beat grid DONE (work/beat_grid.json): primary tempo **123.05 BPM** (median inter-beat + beat_track agree; onset-autocorrelation witness 83.35 = 2:3 artefact). Beat interval 0.4876s. Downbeat phase index 1 but confidence margin only 0.002 — downbeat placement is WEAK evidence; treat downbeats as [inferred].
- Crescendo raw DONE (work/crescendo_raw.json): true peak -2.16 dBFS @ 159.435s; loudest 0.5s window @ 174.75s (-12.03 dBFS RMS) — peak region is the Final Hook. Energy curve: continuous build, mean RMS rises from -25.2 dBFS (0–10s) to ~-14.6 dBFS (130–140s).
- **ANOMALY (major, sheet vs performance): NO performed silence gap.** Fine-RMS scan (0.05s windows) finds no dip below -38 dBFS lasting ≥0.25s anywhere after the 0.52s leader; deepest mid-track fine window is -29.26 dBFS @ 63.7s (a groove dip). The sheet's Drop [Silence - half bar] was NOT performed as silence — Suno kept the groove running. Report both; trust the measurement.
- Raw onset pass over-detects (1056 onsets incl. every drum/bass transient; 546 naively "strong") — refinement pass (cluster ≤0.15s + neighborhood prominence) in work/stab_events.py.
- Transcription running (faster-whisper small, pid 100348).
- Transcription GOTCHA: first run fed raw 48k track.mp3 via soundfile → faster-whisper treated it as 16k → 3×-slowed garbage (deleted). Fix: decoded to work/track_16k.wav first; re-run valid. Small model: 112 words, nothing before 60.46s. Second witness: tiny model (work/SONG_WORDS_tiny.json) — corroborates Hook 1 phrases + no vocal after ~148s; deaf in quiet passages.
- Lyric-video frame sweep (94 frames @2s, work/lyricframes/ sheets 00–11, all read): karaoke scroller (bold=current) is the decisive line-placement witness; Suno's aligner drifts in repetitive chant (pre-bolds ~1s early at the Verse, parks through passages).
- Hit tiering FINAL (work/crescendo_final.py → work/hit_list.json): uncapped onset envelope, cluster ≤0.12s, beat-quantized — **113 events = 33 hit_major + 78 stab + 2 intro stabs**. Two intermediate passes superseded (capped raw pass; prominence pass collapsed in loud sections).
- Section boundaries MEASURED: Intro 0–5.97 / Hook 1 5.97–34.40 / **Interlude 34.40–60.46 (not on sheet)** / Verse 60.46–65.12 / Pre-Hook 65.12–67.26 / Hook 2 67.26–105.94 / Drop 105.94–120.40 / Final Hook 120.40–146.00 / **Outro 146.00–187.20 (41.2s instrumental — holds the true peak AND the loudest window; sheet's outro is a fraction of it)**.
- Drop resolved: "Wipe..." 105.94 [confirmed]; [Orchestral Hit] + "STILL THERE!" placed [inferred] on the hit pair 112.25/112.72; NO silence, NO level strip — groove flat at ~−16.5 dBFS.
- ONE SOFT SPOT: Hook 2 back half — ASR hears hook lines at 81.66–83.74 + 85.96–88.26 (probs 0.86–1.00) where the Suno display shows a park. Trust ASR for chant existence (80–106 is chant-covered); whether they are L5/L6-early or extra repeats needs an ear check. Documented as Dispute 3 in LYRIC_TIMELINE.md.
- Strongest single hit: 63.32 (Verse, strength 1.907). Loudest stab cluster: 170.9–174.7 (Outro). Final Hook = loudest section (mean −14.7 dBFS) but zero hit_majors (off-grid peaks) — cut it on the stab tier.
- STAGE 1 COMPLETE. Deliverables: SONG_WORDS.json, work/beat_grid.json, work/CRESCENDO_MAP.md, work/crescendo_map.json, LYRIC_TIMELINE.md. No generation fired. Scene plan waits on the parent's research track.

---

# MV-8 Stages 2–3 progress — asset bank + journey scene plan

Coordinator: Stages 2–3 (bank + plan). Read: DIRECTION.md, LYRIC_TIMELINE.md, work/CRESCENDO_MAP.md + work/crescendo_map.json (all 113 events), work/beat_grid.json summary (123.05 BPM, downbeats weak), research report (report.md), Slopcannon SKILL.md + visual-mv-forms + video-api-mastery skills.

## Deliverables
- [x] work/ASSET_BANK.md — character/world locks
- [x] Hero test still (16:9) → work/stills/F_HERO_TEST.webp — inspected before chain spend — PASS
- [x] Full F0→Fn anchor still chain → work/stills/ + work/STILL_CHAIN.md — 22 stills, all inspected PASS
- [x] SCENE_PLAN.md — journey across all 9 measured sections, cut points from the 113 events
- [x] Commit (explicit paths) — 25f59faa "MV-8 stages 2-3: asset bank, 22-still anchor chain, journey scene plan"

## Log
- Stages 2–3 started. Key Stage 1 facts carried into the plan: NO silence beat in the Drop (visual drop must be manufactured); Interlude 34.40–60.46 is a real movement (21 hits; note the tiered map's first event inside it is at 45.51 — the 34.40–45.51 stretch is cut from the raw onset list / RMS swells, caveat in CRESCENDO_MAP.md); Final Hook cut on stab tier (zero majors); Outro 146.00–187.20 is a major movement (true peak 159.435, loudest window 174.75, cluster 170.9–174.7).
- work/ASSET_BANK.md WRITTEN: global style lock (glossy stylised 3D cartoon; chocolate-substitution brown rule; yellow = sole accent), characters C1 Champion / C2 the Mount "Sir Swirl" (soft-serve mascot) / C3 the Squire (TP-roll sidekick) / C4 Brown Ribbon Serpent / C5 Clog Colossus; grail = the Ghost Wipe, curse = the Marker Wipe; props P1–P9 (TP breastplate, TP cape-streamer, toilet-seat shield, golden plunger sword, yellow glove gauntlets, brush-crown helmet, throne toilet, golden flush handle, spare rolls); worlds W1–W9; anchor-still doctrine (conditioner, not frame source — end anchors land recomposed; exact loop frame is laid in at edit).
- **HERO TEST STILL: PASS.** work/stills/F_HERO_TEST.webp (md5 8699ec5900f461a1f12c0490f0b34bf0, snapshot 89bf9e53-a426-462b-b684-a3f9c02d2e8e:teoe61). Inspected: the Mount is a glossy chocolate soft-serve swirl with curled tip, huge round cartoon eyes, cheerful smile, aviator goggles, cream scarf streaming — cute mascot, ZERO gross factor, moderation clean. Champion: layered TP-wrap breastplate, giant TP streamer cape off a backpack roll, golden plunger raised like a sword, porcelain toilet-seat shield, bright yellow rubber-glove gauntlets as sole accent. Porcelain palace city + bidet fountains + golden hour behind. No text/letters/watermark. This still is the identity anchor for the chain and doubles as chain still F11 (first flight).
- **FULL CHAIN GENERATED + INSPECTED: F00–F21 (22 stills incl. F11 = hero test), ALL PASS.** Canonical files work/stills/F00.jpg…F21.jpg (md5s in STILL_CHAIN.md); generation originals (.webp) alongside. Highlights: F01 the marker sheet and F02 the vortex + golden handle are exact; F10 delivers the full kit incl. brush-crest helmet + the Squire (C3); F19 the Colossus; F21 the Ghost Wipe (glowing clean sheet + swooning Squire). Watch items logged in STILL_CHAIN.md: (1) F04's armour arrived early via the test anchor → the pipe flight is assigned to the Final Hook victory lap (FH-C), the first descent stays character-free FPV (F02→F03); (2) F12's pupil reflection holds miniature neon glyphs, unreadable at size — Stage 4 QC fails any take where they resolve into letters; (3) F17's serpent wears goggles in the vortex (rival-flyer read) — F18 is its true smug form.
- SCENE_PLAN.md WRITTEN (project root): 17 scenes tiling 0.00–187.20 across all 9 measured sections, every scene with span, cut points from the 113 events, anchor pair, Stage-4-ready motion prompt, Star Guitar assignment, type cues. Key plan decisions: the Drop's missing silence is MANUFACTURED visually (held serpent stare-down across the flat groove; the "STILL THERE!" slam lands on the 112.25/112.72 hit pair); the Interlude's quiet first half (34.40–45.51, no tiered events) is two long holds in the paper-macro world, cut from raw onsets/RMS; Final Hook cut on the stab tier (zero majors); the Outro is three movements with the film's biggest visual (loop-the-loop) placed on the TRUE PEAK 159.435 and the Colossus finale on the 170.9–174.7 cluster; loop close = final clip F21→F00 with the seam inside the flush vortex + crossfade insurance; kinetic-type cue list (counter gag resets to "WIPE 001 — CLEAN" at the Ghost Wipe) is post-layer only. Stage 4 firing order: hook-proof volley first (H1-A + IN-A + D-B).
- STAGES 2–3 COMPLETE. Stage 4 (fire) not started, per brief.

---

# MV-8 Stage 4 progress — firing (coordinator #1: hook-proof volley)

Volley 1 per SCENE_PLAN firing order: H1-A (10s + 5s) + IN-A (10s) + D-B (10s)
= 4 planned generations, ≤6 budget incl. re-fires. QC rows in work/TAKE_LEDGER.md.

- Coordinator #1 died on transport error after firing gen 1. CONTINUATION (#1-CONT) recovered from disk — no restart.
- H1-A c1 QC'd: **KEEP** (ledger row 1). 1280x720, 10.0s, motion strong, text gate PASS, locks hold. Copied to takes/H1-A_c1.mp4 (md5 a6a6a4a09dbc177b319e0570867f25d1); raw original in place.
- Firing remaining volley-1: H1-A c2 (5s), IN-A (10s), D-B (10s).
- **VOLLEY 1 COMPLETE (coordinator #1-CONT): 4/4 scenes KEEP.** H1-A c1 KEEP · H1-A c2 KEEP (gen1 REJECT 3:2 → re-fire gen2 KEEP) · IN-A KEEP · D-B KEEP (held shot, ambient-motion pass). Ledger rows 1–5 in work/TAKE_LEDGER.md. Takes: takes/H1-A_c1.mp4, takes/H1-A_c2.mp4, takes/IN-A.mp4, takes/D-B.mp4 (raws kept alongside).
- ASPECT LESSON (Stage 4, measured): the chain stills are MIXED aspect — F00 is 2048x1152 (16:9) but F01/F18 are 1920x1280 (3:2). A two-image call leading with F01 (3:2) returned 1152x768 despite aspect text; single-anchor calls returned 1280x720 exact (F18) or 1248x704 (F00 — 16:9 within 0.3%, conform-scale at assembly, no crop). FUTURE VOLLEYS: prefer single-anchor or 16:9-first image order; treat 1248x704 as the pipeline's near-16:9 plate and conform at assembly; never lead a two-image call with a 3:2 still.
- Next: volley 2+ in journey order (H1-B, I-A, I-B, V-0, PH-A, H2-A, H2-B, H2-C, D-A, FH-A, FH-B, O-A, O-B, O-C) — NOT started by this coordinator. No master assembled.

---

# MV-8 Stage 4 progress — firing (coordinator #2: volley 2, journey order)

Volley 2: H1-B, I-A, I-B, V-0, PH-A, H2-A. Budget ≤6 generations incl. re-fires (≤1 re-fire per failed scene). QC rows in work/TAKE_LEDGER.md; QC tooling work/qc_take.py (ffprobe + decode + 2fps mean-abs-diff motion + 8 full-res grabs + contact sheet).

Aspect plan (measured stills: F00/F02/F06/F08/F09/F10 = 2048x1152 16:9; F01/F05/F07 = 1920x1280 3:2 — NEVER lead with a 3:2 still):
- H1-B: single-anchor F06 (fibre landscape = the dive's landing; F05 is 3:2, not led with).
- I-A: single-anchor F06 (F05→F06 journey collapsed to the 16:9 end anchor; slow drift text).
- I-B: single-anchor F08 (reveal clip only — the river-flight clip is NOT fired in this volley; outstanding for volley 3).
- V-0: single-anchor F00 (5s).
- PH-A: single-anchor F02 (16:9 handle-slam close-up; F01 ECU is 3:2, not used).
- H2-A: two-image F09→F10 (both 16:9; arming montage, journey recipe).

## Volley 2 continuation (coordinator #2-CONTINUATION, from ~18:37 EST)

- Predecessor (#2) died on transport ~13:18 EST after firing H1-B (KEEP, row 6) + I-A raw. Recovered from disk — no restart.
- **I-A: KEEP (ledger row 7).** takes/I-A.mp4 md5 a2c171c74c1535b1b7f0126bddbef30c · 1248x704, 10.0s, clean decode, motion mean YDIF 21.9 (min 12.9, no freeze) · text PASS at full res · slow drift over fibre hills + chocolate river, hero tiny at the bank by the tail, ribbon arch over the ridge · locks hold. (qc_take.py hung on its first ffmpeg grab in this session — killed; probe/decode/motion recomputed directly, grabs from the 20:21 UTC run on the same file.)
- Generations used this run so far: 0 (I-A was predecessor's generation; QC only).
- Firing next, journey order: I-B, V-0, PH-A, H2-A.
- **I-B: KEEP (ledger row 8).** takes/I-B.mp4 md5 368675406e3705e87cb78522217f7783 · 1248x704, 10.0s, clean decode, motion mean YDIF 33.3 (min 24.1) · text PASS · yellow-gloved hand pushes the porcelain gate open → camera pushes through into the palace city, sweeping aerial over domes/geysers/TP banners · locks hold.
- **V-0: KEEP (ledger row 9).** takes/V-0.mp4 md5 aa0d9a498b26975dd184cbf0f6bffd8d · 1248x704, 5.0s exact, clean decode, motion mean YDIF 37.2 (tail hold 4.0–4.5s at 4.2 — settled reaction close-up) · text PASS · hero on the golden throne-toilet, pulls sheet, inspects the chocolate stroke: curiosity → disbelief → determined frown · nit (disclosed): hero reads younger than the F00 anchor — tunic + yellow gloves + blue eyes carry identity.
- **PH-A: KEEP (ledger row 10).** takes/PH-A.mp4 md5 c2c27d4745648c4ff0f5cb6afa91644b · 1248x704, 5.0s exact, clean decode, motion mean YDIF 48.9 (min 15.1) · text PASS · handle slam (head) + golden plunger pop (tail) on-brief · ASSEMBLY CUT NOTE: middle ~1.5–3s is a BED (generator read "a sheet snapping taut" as bed linen) — DISCARD the middle, cut handle↔plunger alternation for the 2.1s window.
- **H2-A: BLOCKED (ledger row 11, no file).** The two-image F09→F10 generation returned `integrity_check_failed` on its first attempt; per the media tool's instruction the request was NOT repeated (no re-fire, no reworded variant, no alternate tool). Scene stays OPEN for volley 3 — a redesigned vehicle on a new axis is a producer decision for the next coordinator / parent, not taken in this run.
- **VOLLEY 2 COMPLETE (5/6 scenes KEEP; H2-A blocked).** Ledger rows 6–11. Generations used this run: 3 (I-B, V-0, PH-A) + 1 failed H2-A attempt (no video produced, does not count toward the 6-video cap). Takes: takes/H1-B.mp4, takes/I-A.mp4, takes/I-B.mp4, takes/V-0.mp4, takes/PH-A.mp4.
- Next: volley 3 (H2-B, H2-C, D-A, FH-A, FH-B, O-A, O-B, O-C) + H2-A redesign decision, then assembly. No master assembled.
- **H2-A: KEEP (ledger row 12, volley 3a).** Redesign worked: single-anchor F09 after the two-image F09→F10 integrity_check_failed (row 11). takes/H2-A.mp4 md5 e0700cac2304d9974960194fc5082050 · 1248x704, 10.0s, clean decode, motion mean YDIF 21.1 (min 3.9) · text PASS at full res · arming montage completes piece-by-piece, Squire cheering · nit (disclosed, anchor-consistent): hero reads young, same as V-0.
- Generations used this run so far: 1 (H2-A). Firing next, journey order: H2-B, H2-C, D-A, FH-A, FH-B.
- **H2-B: KEEP (ledger row 13).** takes/H2-B.mp4 md5 a009cfcd923d0d0e7e52cf6eab92e43b · 1248x704, 10.0s, clean decode, motion mean YDIF 14.9 (min 0.7 within-hop holds, max 94.8 at hop cuts) · text PASS at full res (neon = abstract pseudo-glyphs) · world-hop reprise plays across 4 worlds, hero anchor-faithful to F00 · ASSEMBLY CUT NOTE: palace hop ~2.5–5s is an empty hall, hero+throne absent — DISCARD, cut bathroom→fibre directly; plan's 2nd H2-B clip still outstanding.
- Generations used this run so far: 2 (H2-A, H2-B). Firing next, journey order: H2-C, D-A, FH-A, FH-B.
- **H2-C quest 1: BLOCKED (ledger row 14, no file).** Single-anchor F15 generation returned `integrity_check_failed`; NOT repeated per the media tool's instruction. Quest 1 stays OPEN for volley 3b — redesign is a producer decision for the next coordinator / parent. Quest 2 (F16 mural) NOT fired this run; also outstanding.
- Generations used this run so far: 2 successful (H2-A, H2-B) + 1 failed H2-C attempt (no video produced, does not count toward the 6-video cap). Firing next, journey order: D-A, FH-A, FH-B.
- **D-A: KEEP (ledger row 15).** takes/D-A.mp4 md5 905f5add14ee496b2291517fdf6dcb0b · 1248x704, 10.0s, clean decode, motion mean YDIF 53.6 (min 43.3 — strongest motion of the volley) · text PASS at full res · two-image F17→F18 (both 16:9) works — the vortex duel plays as one continuous orbiting move · nit (disclosed): hero sometimes rides a toilet-seat strapped to the Mount.
- Generations used this run so far: 3 successful (H2-A, H2-B, D-A) + 1 failed H2-C attempt (no video produced, does not count toward the 6-video cap). Firing next, journey order: FH-A, FH-B.
- **FH-A: KEEP (ledger row 16).** takes/FH-A.mp4 md5 570994f2a7beb1ba012c243526c6ee24 · 1248x704, 10.0s, clean decode, motion mean YDIF 38.8 (min 33.4) · text PASS at full res · the synchronised flush plays as one continuous forwardtracking move; wipe-clean progression reads across the clip.
- Generations used this run so far: 4 successful (H2-A, H2-B, D-A, FH-A) + 1 failed H2-C attempt (no video produced, does not count toward the 6-video cap). Firing next, journey order: FH-B (last of this volley).

---

## Volley 3a COMPLETE (coordinator #3) — 5/6 scenes KEEP; H2-C quest 1 blocked

Ledger rows 12–17. Generations used this run: 5 successful + 1 failed H2-C attempt (integrity_check_failed, no video produced, does not count toward the 6-video cap). Takes: takes/H2-A.mp4, takes/H2-B.mp4, takes/D-A.mp4, takes/FH-A.mp4, takes/FH-B.mp4 (all 1248x704, 24fps, parent md5s in ledger).
- H2-A KEEP (row 12): single-anchor F09 redesign after the two-image F09→F10 integrity failure (row 11) — redesign works.
- H2-B KEEP (row 13): world-hop reprise; ASSEMBLY CUT NOTE: palace hop ~2.5–5s is an empty hall, hero+throne absent — DISCARD, cut bathroom→fibre directly.
- H2-C quest 1 BLOCKED (row 14): single-anchor F15 integrity_check_failed, NOT repeated per tool rule. Quest 1 + quest 2 (F16 mural) both OPEN for volley 3b — redesign is a producer decision.
- D-A KEEP (row 15): vortex duel, strongest motion of the volley (mean YDIF 53.6); two-image F17→F18 both-16:9 works.
- FH-A KEEP (row 16): synchronised flush, wipe-clean progression reads.
- FH-B KEEP (row 17): Brown Deep flight + sky-break into the Outro.
- Assembly cut notes carried in ledger: PH-A middle 1.5–3s is a bed (discard); H2-B palace hop empty (discard).
- Next: volley 3b — O-A, O-B, O-C + I-B river-flight clip + H2-C quests 1+2 (redesign) + plan 2nd clips for H2-B / FH-A / FH-B (if assembly wants them), then assembly. No master assembled.

---

## Volley 3b (coordinator #4) — O-A, O-B, O-C, I-B river-flight, H2-C quest 2, H2-C quest 1 redesign

Budget: ≤6 generations. Aspect checks (ffprobe, 2026-11-07): F11/F15/F16/F20/F21 = 2048x1152 (16:9); F14/F19 = 1920x1280 (3:2). O-A: single-anchor F11 (loop-the-loop on the true peak). O-B: single-anchor F19 (3:2 still — D-B precedent: single-anchor F18 3:2 returned 1280x720 with aspect text stated; QC will catch it). O-C: two-image F21→F00 (both 16:9). I-B river-flight: single-anchor F06. H2-C quest 2: single-anchor F16. H2-C quest 1 REDESIGN: two-image F15→F16 (both 16:9; new axis — journey from clog pull-free to mural; single-anchor F15 verbatim NEVER repeated; brief's F14→F15 example rejected — F14 is 3:2 and must never lead).
- **O-A: KEEP (ledger row 18).** takes/O-A.mp4 md5 daad4028e4701276e8d9470bfe4e3869 · 1248x704, 10.0s, clean decode, motion mean YDIF 30.8 (min 17.7) · text PASS at full res · loop-the-loop + descent over the porcelain city; plan's 2nd O-A clip still outstanding.
- Generations used this run so far: 1 (O-A). Firing next, journey order: O-B, O-C, I-B river-flight, H2-C quest 2, H2-C quest 1 redesign.
- **O-B: KEEP (ledger row 19).** takes/O-B.mp4 md5 e3e3856b5c92328c514558badb53ba96 · 1280x720 exact, 10.0s, clean decode, motion mean YDIF 35.1 (min 14.1) · text PASS at full res · Colossus + wave + dissolve; nit: tiny hero gold/red, palette drift (disclosed) · plan's 2nd O-B clip still outstanding.
- Generations used this run so far: 2 (O-A, O-B). Firing next, journey order: O-C, I-B river-flight, H2-C quest 2, H2-C quest 1 redesign.
- **O-C: KEEP (ledger row 20).** takes/O-C.mp4 md5 ca68bc59e346c58fa62e7bde7c083da7 · 1248x704, 10.0s, clean decode, motion mean YDIF 28.8 (min 2.2 = wonder hold, designed) · text PASS at full res · Ghost Wipe → vortex → F00 rhyme landing; the loop closes.
- Generations used this run so far: 3 (O-A, O-B, O-C). Firing next, journey order: I-B river-flight, H2-C quest 2, H2-C quest 1 redesign.
- **I-B river-flight: KEEP (ledger row 21).** takes/I-B_river.mp4 md5 7136008c44329ae6fd32574ed3b9f05b · 1248x704, 10.0s, clean decode, motion mean YDIF 32.4 (min 22.1) · text PASS at full res · river flight down the chocolate river; I-B now has both its plan clips.
- Generations used this run so far: 4 (O-A, O-B, O-C, I-B river). Firing next, journey order: H2-C quest 2, H2-C quest 1 redesign.
- **H2-C quest 2: KEEP (ledger row 22).** takes/H2-C_q2.mp4 md5 fc34fbaecf3a606b152495099fb6a041 · 1248x704, 10.0s, clean decode, motion mean YDIF 25.0 (min 2.1 = tail stare, designed) · text PASS at full res · mural wipe + re-forming ribbon + stare; nit: F16 curly hair (disclosed).
- Generations used this run so far: 5 (O-A, O-B, O-C, I-B river, H2-C q2). Firing next, last of this volley: H2-C quest 1 redesign (two-image F15→F16).
- **H2-C quest 1: KEEP (ledger row 23).** Redesign worked: two-image F15→F16 after the single-anchor F15 integrity_check_failed (row 14). takes/H2-C_q1.mp4 md5 eada7ebfbd54214f65bd846132d1b8fe · 1248x704, 10.0s, clean decode, motion mean YDIF 38.6 (min 17.2) · text PASS at full res · pull-free + mural wipe; nit: hero's legs blue-grey (disclosed).
- Generations used this run: 6 of 6 (O-A, O-B, O-C, I-B river, H2-C q2, H2-C q1 redesign). Budget exhausted.

---

## Volley 3b COMPLETE (coordinator #4) — 6/6 scenes KEEP

Ledger rows 18–23. Generations used this run: 6 successful, 0 failed. Takes: takes/O-A.mp4, takes/O-B.mp4, takes/O-C.mp4, takes/I-B_river.mp4, takes/H2-C_q2.mp4, takes/H2-C_q1.mp4 (all 1248x704 except O-B 1280x720 exact, 24fps, parent md5s in ledger).
- O-A KEEP (row 18): return flight, loop-the-loop on the true peak, descent over the porcelain city.
- O-B KEEP (row 19): Colossus last stand — wave bursts through, Colossus dissolves; nit: tiny hero gold/red (disclosed). Single-anchor F19 (3:2 still) returned 1280x720 exact — D-B precedent holds.
- O-C KEEP (row 20): Ghost Wipe reveal → full-frame vortex → F00 rhyme landing; the loop closes.
- I-B river-flight KEEP (row 21): hero runs the chocolate river bank through fibre hills; I-B now has both plan clips.
- H2-C quest 2 KEEP (row 22): mural wipe + re-forming ribbon + stare; nit: F16 curly hair (disclosed).
- H2-C quest 1 KEEP (row 23): REDESIGN worked (two-image F15→F16) — pull-free + mural wipe; nit: hero's legs blue-grey (disclosed).
- Stage 4 firing is now COMPLETE: all 17 scenes have KEEP takes (rows 1–23, incl. both H2-C quests, both I-B clips, all three Outro scenes). H2-A's blocked two-image attempt (row 11) and H2-C quest 1's blocked single-anchor attempt (row 14) are the only non-KEEP rows.
- Assembly cut notes carried in ledger: PH-A middle 1.5–3s is a bed (discard); H2-B palace hop ~2.5–5s is an empty hall (discard).
- Still outstanding for assembly (optional, not blocking): plan 2nd clips for H2-B / FH-A / FH-B / O-A / O-B (assembly may or may not want them — producer call at assembly).
- Next: ASSEMBLY — one 16:9 CRF-18 AAC house master + kinetic type layer + ~ WuBu ~ corner bug + loop close, per SCENE_PLAN.md. No master assembled.

---

## Assembly (coordinator, Stage 6) — STARTED 2026-11-07 ~23:45 EST

Plan: work/assembly/ASSEMBLY_PLAN.md. All 17 scenes covered from the 21 KEEP
takes; shortfalls covered by time-warp (max 1.93x, inside the 2x law), no new
generation. Cut notes applied: PH-A bed 0.75–2.25 discarded (scene-detect
cuts @0.75/@2.25); H2-B palace hop 1.125–3.208 discarded (scene-detect cuts
@1.125/@3.208/@6.167). O-C sped 1.39x so the F00-rhyme landing survives.
O-A loop-the-loop lands ~147–148.5, NOT on the 159.435 true peak (take
front-loads the loop; forcing it would need ~4.5x slow — disclosed in plan).
Kinetic layer: work/assembly/mv8_kinetic.ass (121 events, kinetic_ass.py
presets + custom STILL THERE! / WIPE… / counter / reset gag / ~ WuBu ~ bug).
Build: work/assembly/build.py → masters/mv8_wipe_and_its_still_there_16x9.mp4
(CRF 18, 1280x720, 24fps, AAC 192k from track.mp3). Encode running detached,
log work/assembly/build.log.

## Assembly COMPLETE (coordinator, Stage 6) — 2026-11-07 ~23:50 EST

House master: masters/mv8_wipe_and_its_still_there_16x9.mp4
- md5 b9d30c32e0fa3f28fab593e3f02725bb · 109,071,442 B · 4497 frames, 187.375 s
  (plan 4493; +4 frames from fps-filter rounding — picture runs ≤167 ms
  behind the song clock by the end, invisible on the held shots)
- ffprobe: 1280x720, 24 fps, h264; audio AAC 48 kHz stereo ~196 kbps,
  187.200 s, start 0.000. x264 SEI reads crf=18.0. Decode clean.
- Kinetic layer verified on frames: WIPE counter ticks (001/004/011),
  word-pop SLAMs, CASCADE "WIPE AGAIN", "WIPE…" held over the mural tail,
  "STILL THERE!" on the serpent stare, "WIPE 001 — CLEAN" on the Ghost Wipe
  reveal, "~ WuBu ~" bug on every frame. Loop closes on the F00 rhyme
  (hero on throne, Squire on sink) at 186.9.
- Cut notes applied: PH-A bed discarded, H2-B palace hop discarded.
- Chat copy (≤50 MB, AAC copied) encoding; see below.
- Chat copy: masters/mv8_wipe_and_its_still_there_16x9_50mb.mp4 — md5
  81894bc5f4c31fe0fe1c2064cd8cc0d8 · 46,365,260 B (under 50 MB) · 4497 frames,
  187.375 s · video re-encoded 1778 kbps avg, AAC audio copied untouched
  (audio md5 identical to house: c92b496f6af0d1ac7a58c75908832d13). Decode clean.
  House master is 109,071,442 B — chat copy is the delivery file.
- Masters are git-ignored (*.mp4); assembly record (plan, scripts, ASS,
  logs, verify frames) committed. Parent verifies + writes
  MV8_DELIVERED.flag at delivery.
