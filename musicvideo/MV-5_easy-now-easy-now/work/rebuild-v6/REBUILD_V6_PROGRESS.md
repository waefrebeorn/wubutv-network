# MV-5 REBUILD v6 — PROGRESS (disk is the record)

Coordinator: mv5-full-rebuild. Started 2026-11-13 ~04:50 EST.
Order: FULL REFIRE — lyric look lock: GIRL in BLUE SHIRT, RED BICYCLE.
Grid + captions inherited unchanged (lyrics-redo). v5 structure/singers
inherited. L104 CAT take fires this build.

## Identity macros (v6)
GIRL: young woman, long wavy purple hair, straw sun hat with red
ribbon, BLUE short-sleeve shirt, backpack half-zipped, bare feet on
the boardwalk; warm expressive face.
CAT: black cat, red collar with round yellow bell, bright blue eyes.
BIKE: RED bicycle with a front wicker basket (the CAT rides in it).
WORLD: sunny beach boardwalk + pier, vendors, mango stalls, anime
illustration, bright pop palette (verse cool-bright, chorus warm,
bridge gray-sky shift). NO red jacket. NO blue bicycle. Adults only.

## USER EXPANSION 2026-11-13 ~04:50 EST (folded in pre-pilot)
1. ZERO REUSE: only grid+captions and lyrics.txt carry authority.
   Plan rebuilt from lyric sheet + grid; v5 rows NOT copied.
2. SINGERS RE-DERIVED IN-BUILD: MDX vocal stem → per-line F0 →
   SINGER_MAP_V6.md. Hard rule: non-singer's mouth closed/out of
   frame; both-mouth onset reads at QC where both are in frame.
3. BRIDGE = FULL REBUILD: rain/gray-sky light-shift section change,
   walking pace, hand in hand, lean-back spin, motion throughout.
4. NO-STARE GATE (reject tier = colour): gaze + motivated action in
   every vehicle; staring at camera unsinging/unmotivated = REJECT.
   Visual gate doc gains singer-mouth-pair reads + no-stare audit.

## Stages
- [x] Read: lyrics.txt, SKILL.md, visual-mv-forms, Q10 diagnosis +
  ledger + v5 plan report, LYRICS_REDO_NOTES, grid (118 lines/548w).
- [x] Plan written + expansion folded: plan/V6_PLAN.md.
- [x] Reference stack stills (colour-checked, all 4 PASS)
- [x] Singer derivation DONE → plan/SINGER_MAP_V6.md (F0 on MDX
  stem; corrections vs old record: L12 CAT not GIRL, L41 CAT not
  GIRL, L55 CAT, L109 CAT, L16 = GIRL sung showcase, bridge opens
  CAT; confirmed: I09 G, L15 G, L37 C, L40 split, L56 G, L104 C)
- [ ] Pilot volley-0 (3 clips) — colour gate at full res
- [ ] Volley V1 (6) — intro + verse 1
- [ ] Volley V2 (6) — PC1 + verse 2a
- [ ] Volley V3 (6) — verse 2b + PC2 + chorus 2 base
- [ ] Volley V4 (6) — choruses
- [ ] Volley V5 (6) — L104 + bridge + tail
- [ ] Volley V6 (≤6) — L109 + instrumental + rerolls
- [ ] Transcribe all KEEPs → take-word JSONs
- [ ] build_v6_plan.py → assembly_fit_mv5_v6.json (0 errors, 4954f)
- [ ] assemble_mv5_v6.py → v6 master + chat copy
- [ ] Gates: house gate + audio agreement + motion audit + mouth reads
- [ ] Visual gate doc (colour lock proof frames)
- [ ] CUTLIST.md + MUSIC_VIDEO_LEDGER.md + final report

## Log
- 04:50 EST: setup done, plan written. Firing reference stills next.

## Log
- 05:0x EST: PILOT: p2 (CAT hook, cat_basket ref) GENERATED + COLOUR
  PASS at full res (red bike, blue shirt, both frames verified;
  md5 94c9f7c2). p1 (GIRL lips) + p3 (ride motion), both conditioned
  on ref_girl_bike.png, were REFUSED by the generator
  (integrity_check_failed) — NOT retried, per policy. Adaptation:
  girl vehicles re-anchored on ref_girl_face.png (different input);
  pair/ride vehicles on stills/ref_pair_ride.png (frame extracted
  from the accepted p2). If girl-face vehicles also refuse, the
  girl route is escalated to the parent as a hard blocker.
- PILOT VERDICT: PASS. Colour proven on both routes (p2 cat route;
  s03_girl girl-face route: BLUE shirt + RED bike + open singing
  mouth + gaze on the cat, full-res verified).
- VOLLEY V1 CLOSED: 6/6 generated, all transcribed.
  s01_cat bc6b2975 (I01-I04 sung once, 16w) · s02_ride 0c34f891
  (motion, mouths closed) · s03_girl 4eb69537 (ta-da x3 groups) ·
  s04_cat 32c056f0 (L01-L05 ALL sung, incl. the look line) ·
  s05_cat 208d2917 (L06-L09 all) · s06_cat 9343168b (L10-L12 all;
  KEYS BEAT on screen; "MANGO" stall sign = diegetic set dressing,
  disclosed). All colour-PASS at full res. KEEP x6 (assembly ratios
  to be confirmed by the plan builder).
- VOLLEY V2 CLOSED: 6/6 generated + transcribed, all usable
  (s07_cat ASR garble on L14 tail noted for the builder; s11_cat
  absorbed a "Mango Sweet" vendor pickup before L37 - usable).
- EVENT RULE APPLIED (steer 05:20 EST): library read; EVENT column
  in plan for all 28 scenes; V3 fired event-first (6/6 landed).
- VOLLEY V4: 5/6 landed (s08/s16/s17 duets, s10_cat, s18_girl).
  s09_duet (umbrella cascade) REFUSED by the generator - not
  retried; C1b restaged as invented "Kite Lift" in V5.

## Checkpoint 2026-11-13 ~06:20 EST — volleys V3–V7 closed, fit CLEAN, assembly running
- V3 (6/6): s12_girl, s13_ice (spare insert), s13_boombox, s13_spin, s15_cat, s15_girl (posterize tail VERIFIED on screen).
- V4 (5/6): s08_duet, s16_duet, s17_duet, s10_cat, s18_girl.
- V5 (6/6): s09b_duet (kite restage after s09_duet integrity refusal), s23_duet, s24_duet, s25_girl, s19_bridge (storm VERIFIED: sunny-wet f_0.8 -> full rain f_8.5), s25_cat REJECTED at QC (identity intrusion: unknown girl in pink floral beside the CAT's L104 close-up — do not use).
- V6 (6/6): s20_bridge, s21_walk, s21_spin, s26_chain, s27_chant, s28_outro.
- V7 gap volley (5/5): s02_girl (S02 now fully sung), s25_cat2 (L104 solo close-up, full-res verified clean — replaces rejected s25_cat; NO fallback cover needed), s13_cat, s13_girl, s21_gap.
- V8 brisk re-fires (4/4, builder-driven: verse takes sang short bridge/PC2/outro lines 2-4x too slow for phrase warps): s15_cat2 (PC2 brisk, all 3 lines in 4.6s), s20_cat2 (L81 in 1.94s), s21_all2 (L82-L86+L88; L83/L84 hand-windowed, L87 mangled), s28_cat2 (one held Till line — used via onset window for L110).
- V9 micro (2/2): s21_girl2 (L87 brisk, clean), s27_cat2 (L109 brisk, clean).
- V10 micro (1/1): s04_cat2 (L05 'Blue shirt, red bicycle' — used via PX2 duration window; the song rattles the line, onset warp 2.86 on every take).
- Generator refusals (integrity_check_failed, never retried): pilot p1, pilot p3 (both on ref_girl_bike.png), s09_duet.
- Colour gate: ZERO colour rejects across all landed takes (all full-res verified in QC reads).
- FIT: build_v6_plan.py v3 (text-derived grid sequences, cursor-ordered DP alignment, onset-anchored warps, tail absorption, core-based src clamp) -> assembly_fit_mv5_v6.json: 0 ERRORS, exactly 4954 frames, 29 disclosures (duet-span internal onset offsets — two-voice ASR cannot anchor chorus interiors; phrase internal drifts on held lines L16/L56; L05 PX2 onset compromise; L02 PX2 slow-down 0.56).
- ASSEMBLY: assemble_mv5_v6.py running (house chain + texture pass + S22 blackout fade dip + kinetic .ass + ~ WuBu ~ bug + track.mp3 AAC).

## FINAL 2026-11-13 ~07:35 EST — v6 BUILT, ALL HOUSE GATES PASS, READY FOR PARENT
- House master: masters/mv5_easy_now_easy_now_16x9_v6.mp4 md5 2071388f3fb5672849e29462cb3f2b64 (197.2 MB, 4954f, 206.4167s, CRF 18, AAC 48k, faststart).
- Chat copy: masters/mv5_easy_now_easy_now_16x9_v6_chat.mp4 md5 2e2688bd592821e0a4c6ab3ab5f4657b (46.1 MB, crf 26 — crf 23 overshot at 62.9 MB because of the texture grain; AAC copied).
- Audio agreement min 0.9985 / mean 0.9989. Motion: mean diff 9.77; longest near-dup run 24f at L12 (held tableau, disclosed).
- Visual gate: ~60 full-res master frames read (every solo onset direct or same-take bracketed; spans sampled). Colour rejects ZERO. L104 sung by s25_cat2 (no cover fallback needed).
- Deliverables written: CUTLIST.md v6 section, MUSIC_VIDEO_LEDGER.md v6 rows, qc/GATE_LOG_V6.md, qc/GATE_V6.json, qc/VISUAL_GATE_V6.md (event-read sentences for all 28 scenes), USED_EVENTS.md MV-5 section marked SHIPPED, EVENT_LIBRARY.md annex (8 invented events).
- NOT done (parent's, per brief): delivered flag, git commit.
- Heartbeat registry key mv5-full-rebuild: the whitelist file was never written by this coordinator (parent manages it) — flagging as instructed.
