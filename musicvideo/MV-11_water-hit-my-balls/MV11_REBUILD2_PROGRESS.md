# MV-11 REBUILD 2 — PROGRESS ("THE BALL PARK" axis)

Recovery coordinator revived 2026-11-12 ~04:16 EST after a3b81337 died
04:13:30 EST (transport error, 85s after spawn, nothing written).
User order msg 305: full rebuild, montage-first, puns + balls, NO ducky,
NO toilet-becomes-bathtub. Nov 10 rebuild master is the "awful video" —
reference only, its takes never reused.

## 2026-11-12 ~04:2x EST — plan written
- work/MV11_REBUILD2_PLAN.md: 23 scenes, "THE BALL PARK" axis — one
  cartoon carnival/fairground complex, every scene a different ball
  world (bowling / basketball / disco / pinball / golf pond / billiards /
  ball pit / pool party...), camera travels through it. Motif THE DROP.
- New ledger work/TAKE_LEDGER_REBUILD2.md + this progress file. Nov 10
  files untouched.
- Volley 1 (this run): S01–S06, all FRESH starts. Stack2 refs next,
  then vehicles, then fire.

## 2026-11-12 ~04:3x EST — stack2 + vehicles written
- work/stills/stack2/: 12 refs (start/end pairs S01–S06), all read back
  via stack2_contact.jpg — PASS, palette holds, zero retired-world
  elements. Recorded in work/REFERENCE_STACK2.md.
- Vehicles work/vehicles/mv11_r2_s01..s06_vehicle.txt written (two-image
  journey shape, 'at <place>' leads, full-10s motion plans).
- Firing S01 → S06 in song order.

## Volley 1 — S01–S06 (in progress)
- (entries land here as refs/vehicles/takes land, one line per step)
- S01 t1 KEEP (md5 7883b237…; motion 11.95, 0 near-still runs; drop →
  crown → settle arc; G1/G2 pass; no retired-world elements). Ledger row written.
- S02 t1 KEEP (md5 f0a29a92…; motion 14.08, longest near-still 1f;
  sweep → alley → lane journey; G1/G2 pass). Disclosed: invented
  "Thanks for watching!" speech at 8.6–10.0s in the surplus tail only
  (assembly uses ~4.76s; audio discarded). Ledger row written.
- S03 t1 KEEP (md5 0a671b7b…; motion 16.26, longest near-still 1f;
  roll → strike → explosion → splash, the hook lands; G1/G2 pass).
  Disclosed: invented "Thanks for watching!" speech at 6.84–8.28s
  (audio only, discarded; no visual outro). Ledger row written.
- S04 t1 KEEP (md5 aae7cd9b…; motion 10.97, longest near-still 2f;
  dribble → drive → shot → swish → celebration; G1/G2 pass).
  Disclosed: background crowd faces small in the stands; low-prob
  "Thank you" at 0.0s (audio only). QC exec interrupted by a runtime
  restart after qc_take.py finished — recovered from the written
  qc.json, re-ran motion audit only. Ledger row written.
- S05 t1 KEEP (md5 7f937e6f…; motion 14.64, longest near-still 3f;
  spray → dance → flare → gold storm; G1/G2 pass; dancers are
  silhouettes/backs). Disclosed: invented "Thank you ... for
  watching!" at 0.0s and 9.54s (audio only). Ledger row written.
- S06 t1 KEEP, used-span (md5 05f8be2c…; full-take motion flagged 15f
  @9.33s, but the run is entirely in the surplus tail — used span
  0–6.24s clean, mean 11.66, longest 1f; the tail is the planned
  slow-drain end state). Disclosed: score numerals on the machine's
  diegetic display (not words/caption); invented "Thank you ... for
  watching!" (audio only). Ledger row written. VOLLEY 1 CLOSED 6/6.

## 2026-11-12 ~09:53 EST — joint QC J01–J05 (volley 1)
- All five joints FRESH turns (each scene a new attraction). MAEs are
  high by design (46–59: different compositions), so the gate is
  world/lighting/palette continuity, eye-read on
  work/qc/joints/joints_contact.jpg — ALL PASS: same Ball Park
  (teal structures, vermilion banners, warm gold light, cobalt water,
  cadmium balls) across every turn; J02 reads near-continuous
  (S02 ends inside the alley, S03 opens on the lane).
- J01 S01@9.00 → S02@0 MAE 57.80 PASS (fountain → wide park pull-back).
- J02 S02@4.76 → S03@0 MAE 47.96 PASS (alley → lane).
- J03 S03@9.95 → S04@0 MAE 59.44 PASS (channel splash → basketball court).
- J04 S04@9.95 → S05@0 MAE 46.28 PASS (hoop celebration → disco hall).
- J05 S05@5.18 → S06@0 MAE 56.45 PASS (gold light storm → pinball machine).

## Volley 2 — S07–S12 (this run, coordinator 7066f0bf)
- Stack2 S07–S12 refs generated + read back (12/12 PASS, all 2048x1152;
  S10 pair regenerated once — first version returned 3:2, trashed).
  Recorded in work/REFERENCE_STACK2.md; contact sheet
  work/stills/stack2/stack2_contact_s07_s12.jpg.
- Vehicles work/vehicles/mv11_r2_s07..s12_vehicle.txt written (S07 =
  performance-window sung scene, profile mouth; S12 = THE DROP
  returns bigger).
- Firing S07 → S12 in song order.
- S07 t1 KEEP (md5 47407b83…; THE ONE SUNG SCENE — profile mouth open
  at "Water" + "My balls" onsets; disclosed: mouth not visible at the
  0.00 onset, wide back view; take audio late vs song, squeeze ~0.57x
  owed at assembly; illegible pseudo-lettering on a background booth
  sign at frame 0). Ledger row written.
- S08 t1 KEEP (md5 575fcaaf…; motion 12.32, longest 1f; serve → rally
  → forehand → lunge; G1/G2 pass). Disclosed: invented "Thank you for
  watching!" audio; small crowd faces in the stands; ~5 balls in frame
  at 5.0s (rapid serves). Ledger row written.
- S09 t1 REJECT (G2 — md5 b48ee780…; motion 17.71, bounces land on the
  beats, but a booth sign reading "…balls" in legible red script enters
  at ~4.5s, inside the 5.00s used span). REROLL OWED on the TEXT axis
  (t2): explicit "no signs, no shopfront lettering, no booth signage",
  keep the camera on the plaza/fountain. NOT fired — 6-video cap spent
  on S07–S12 t1s; reroll goes to the follow-up run. Ledger row written.
- S10 t1 KEEP (md5 17262994…; motion 28.60, highest so far; dive →
  surf → arms-out; G1/G2 pass). Disclosed: "Thanks for watching!" in
  the surplus tail only. Ledger row written.
- S11 t1 KEEP (md5 d8e34b25…; motion 12.09, longest 1f; no words in
  generated audio; small swing → wide swing → surfacing, water surface
  at the top of the frame at 9.5s; G1/G2 pass — posters pictorial only).
  Ledger row written.
- S12 t1 KEEP (md5 e412ad23…; motion 12.52, longest 0f; no words in
  generated audio; swing → splash → rings → second splash → settle;
  THE DROP lands, hazard sign blank in every frame). Disclosed: second
  splash lands ~1.5s after the second "Water" onset; frame-0 ball sits
  on the grass mid-follow-through. Ledger row written.

## 2026-11-12 ~05:2x EST — joint QC J06–J11 (volley 2)
- All six joints FRESH turns. MAEs high by design (47.69–67.69:
  different compositions), gate is world/lighting/palette continuity,
  eye-read on work/qc/joints/joints_contact_v2.jpg — ALL PASS: same
  Ball Park (teal structures, vermilion banners, warm gold light,
  cobalt water, cadmium balls) across every turn; J08 reads
  near-continuous (tennis → plaza), J11 pays off S11's surfacing cue
  (water-at-top → golf pond).
- J06 S06@6.24 → S07@0 MAE 67.69 PASS (pinball neon → pool wide).
- J07 S07@4.96 → S08@0 MAE 51.50 PASS (close profile → tennis wide).
- J08 S08@5.12 → S09@0 MAE 47.69 PASS (tennis lunge → plaza bounce).
- J09 S09@5.00 → S10@0 MAE 60.06 PASS (plaza balls → ball pit dive).
- J10 S10@5.00 → S11@0 MAE 59.14 PASS (pit surf → cradle hall).
- J11 S11@5.40 → S12@0 MAE 65.79 PASS (cradle surfacing → golf pond).

## VOLLEY 2 CLOSED 5/6 KEEP — S09 t2 reroll owed (TEXT axis, see ledger)
- Volley 2 stands at 11/12 KEEP across volleys 1+2 (S01–S06 6/6,
  S07–S12 5/6 + 1 REJECT). Next: follow-up run fires S09 t2 (TEXT
  axis — vehicle mv11_r2_s09_vehicle.txt + ledger row specify the fix),
  then volley 3 (S13–S18). No commit, no delivered flag (parent writes
  it). Assembly is a follow-up run after all 23 scenes hold KEEP.
- S07 V-A "Poolside Chant" (THE ONE SUNG SCENE — Baller poolside,
  side/back, performance-window vehicle) + S08 tennis + S09 bounce
  pickup + S10 ball-pit dive + S11 Newton's cradle + S12 water hazard.
- Stack2 refs for S07–S12 do NOT exist yet — generate start/end pairs
  first (same pipeline), then vehicles, then fire in song order.
- Assembly is a follow-up run after all 23 scenes hold KEEP. NO commit,
  NO delivered flag (parent writes it).

## Volley 3 — S13–S18 (this run, coordinator 782c5e57)
- Parent-verified volley 2 ~05:23 EST: all 6 ledger md5s match disk; S07 mouth confirmed open at 2.0s + 3.5s onsets (parent full-res reads); S09 G2 REJECT confirmed (booth sign legible at 4.5s). Volley 2 CLOSED 5/6 KEEP. S09 t2 reroll goes to volley 4 with S19–S23 (cap math 5+1=6) — NOT fired this run.
- Volley 3 = S13–S18 t1s (6 videos, the cap). Joints J12–J17, all FRESH turns (golf pond → billiards → beach volleyball → freeze plaza → dodgeball → pool party). Stack3 refs first, then vehicles, then fire in song order.
- Stack3 S13–S18 refs generated + read back (12/12 PASS, all 2048x1152; S15 end regenerated once — v1 returned the juggler in a blue striped shirt, jersey-colour drift on the identity carrier; v2 matches the start ref). Recorded in work/REFERENCE_STACK3.md; contact sheet work/stills/stack2/stack2_contact_s13_s18.jpg.
- Vehicles work/vehicles/mv11_r2_s13..s18_vehicle.txt next, then fire S13 → S18 in song order.
- Volley 3 S13 t1 + S14 t1 FIRED and QC'd — BOTH REJECTED (retired world). The generator ignored the explicit duck/toilet/bathtub/bathroom ban and cut back and forth to the SAME invented blue-tiled bathroom (white bathtub/toilet + yellow rubber duck): S13 t1 bathtub+duck at sampled 2.00/4.00/6.00 (md5 f30038f6…), S14 t1 toilet+duck at 0.50–2.00 + 4.00/7.50 (md5 1e45f7cd…). Likely trigger: lyric quotes in the vehicle text + spray/splash action language. Ledger rows written (TAKE_LEDGER_REBUILD2.md, volley-3 note with the mitigation). Next: hardened S13 t2 + S14 t2 as the diagnostic pair (no lyric quotes, "camera never leaves the room/court" clause); if clean, S15+S16 hardened with the last 2 videos; if not, STOP and report.
- DIAGNOSTIC PAIR PASSED: S13 t2 + S14 t2 both KEEP (dense 0.5s-grid reads, 20/20 frames clean on each — no bathroom, no duck, no toilet anywhere; joints J12/J13 PASS, motion PASS both). The hardening works: strip lyric quotes + "camera never leaves the place" clause. Ledger rows written. S15 + S16 vehicles hardened the same way (lyric quotes stripped, never-leaves clause added); firing them with the last 2 videos now.
- Volley 3 CLOSED 4/6 KEEP: S15 t1 KEEP (md5 0197dc3c…, reverse juggle reads, identity holds, no retired world) + S16 t1 KEEP (md5 3fd47fe4…, THE FREEZE lands: ball frozen ~3.0–7.0s with the park alive around it, shatter ~7.0s into confetti rain — earlier than plan, soft alignment, CUTAWAY slot). All 6 videos used. Joints J12–J15 PASS. Volley 4 owed: S17, S18, S09 t2, S19, S20, S21 (hardened vehicles are now the standing pattern — no lyric quotes, never-leaves-the-place clause, named prohibition).

## Volley 4 — S17, S18, S09 t2, S19, S20, S21 (this run, coordinator d7caf71d)
- Parent-verified volley 3 ~05:53 EST: all 6 md5s match; S13/S14 t1 REJECTs confirmed on the contact sheet (bathtub + duck, 3 of 8 frames); hardened t2s both KEEP on 20/20 dense reads. Volley 3 CLOSED 4/6 KEEP.
- Stack note: S17/S18 start/end refs ALREADY exist from volley 3 (REFERENCE_STACK3.md) — verified on disk, md5s match exactly (S17s 3ba313b1…, S17e 526afe6e…, S18s dacdf5d1…, S18e d1c5f631…). NOT regenerated — reuse the read-back PASS pairs. S09 t2 reuses its stack2 pair. Only S19/S20/S21 pairs are new (6 images) → REFERENCE_STACK4.md.
- Vehicles: S17/S18 t1 files exist from volley 3 but are UNHARDENED (S18 quotes "(Splash back)", neither carries a never-leaves clause) — hardening in place before firing. S09 t2 vehicle new (no-signage + plaza/fountain + never-leaves + no lyric quotes). S19/S20/S21 vehicles new, hardened from the start.
- Fire order (pairs): S17+S18, S09 t2+S19, S20+S21. Joints J16–J20 (FRESH turns) + J08/J09 re-check for the S09 t2 reroll.
- Stack4: S19/S20/S21 pairs generated + read back at full res (6/6 PASS, all 2048x1152; S20 end disclosed nit: Baller dark pants vs white shorts in start — striped jersey matches, identity carrier holds). REFERENCE_STACK4.md written; contact sheet work/stills/stack2/stack4_contact_s19_s21.jpg.
- Vehicles hardened: S17 (never-leaves-the-court clause added; prompt already lyric-free), S18 ("(Splash back)" quote stripped → 8.98s as a number; never-leaves-the-pool clause added), S09 t2 NEW (no-signage wording + plaza/fountain + never-leaves + no lyric quotes), S19/S20/S21 NEW hardened from the start. All 6 vehicles on disk.
- Firing pair 1: S17 + S18.
- S17 t1 GENERATION FAILED: media.generate_video returned an internal worker error; the named file never landed on disk (verified). Per the no-retry instruction on that failed call, S17 was NOT re-fired. S17 t1 is OWED to a follow-up run (hardened vehicle ready). Ledger notes the gap.
- S18 t1 KEEP (md5 ea64ebe1…; motion 15.43, longest 1f; dense 0.5s-grid 20/20 frames the pool party, no retired world; G2 confirmed on full-res 0.00s + 5.00s reads — spiral decorations only, no lettering). Arc: wave rolls → crest ~8.0s (vs plan 8.98, soft alignment) → crowd cheering. Disclosed: invented "Thank you for watching!" 6.76–9.66s (audio only); small background crowd faces far background. Ledger row written.
- Firing pair 2: S09 t2 + S19.
- S09 t2 KEEP (md5 b767c451…; motion 11.06, longest 1f; dense 0.5s-grid 20/20 frames the open plaza at the fountain — no booth street, no signs; G2 confirmed on full-res 0.00s + 4.50s reads). The G2 fix worked: no-signage wording + plaza/fountain + never-leaves. Arc: two big balls rising together ~2.0–3.0s, impact splashes 4.5s, ball pit at the right edge in the tail. Disclosed: "Music" @2.16 (audio only); big balls crop at frame top ~5.0s. Ledger row written.
- S19 t1 KEEP (md5 7cfc94f9…; motion 17.37, longest 0f; dense 0.5s-grid 20/20 frames the pinball arcade, no retired world). Arc: flippers → ricochet close-ups → score climbing → multiball → steel-ball storm 8.0–9.5s. Disclosed: "SCORE" word + numerals legible on the diegetic backbox display most frames — SAME CLASS as S06's disclosed display numerals (KEEP, parent-verified); parent may overrule on the TEXT axis. Also: "Thanks for watching!" 0.0–0.96s (audio only); peak strobe ~8.0s vs plan 7.42 (soft alignment). Ledger row written.
- Firing pair 3: S20 + S21 (last 2 videos of the volley).
- S20 t1 KEEP (md5 8a447878…; motion 22.78, longest 0f — highest of the rebuild; dense 0.5s-grid 20/20 frames the ball pit, no retired world). Arc: crest → surf down → arms-out peak. Disclosed: "Thank you." 0.0–1.32s (audio only); Baller in dark pants throughout (matches end ref; start ref had white shorts — take resolves consistently, jersey holds). Ledger row written.
- S21 t1 KEEP (md5 7661e2c9…; motion 12.75, longest 1f; dense 0.5s-grid 20/20 frames the grand hall, no retired world). THE APEX IS IN THE TAKE: strike ~3.5–4.0s, mirror-ball drop ~4.5s, splash crown ~6.0s holding at apex. Disclosed: TIMING — peak events land after the 4.06s used span; assembly note written in the ledger (place take-time ~2.0–6.06 onto the slot so the drop lands ~song 153.5 and the crown rises through the patter). Also: "Thanks for watching!" 6.1–7.5s (audio only). Ledger row written.
- QC hiccup: S20 qc_take.py crashed mid-run (transient ffmpeg miss on the 4.5s frame extract — verified fine on retry); stale Nov-10 S20_t1 frames found in work/qc/ and removed; re-run completed clean for S20 + S21. Joint-frame lesson: -ss 9.96 is past the last frame (239/24 = 9.958s) — use 9.95 for end frames.
- Joint QC (joints_contact_v4.jpg, eye-read + MAE): J18 S18@9.95 → S19@0 MAE 50.99 PASS; J19 S19@9.95 → S20@0 MAE 50.59 PASS; J20 S20@9.95 → S21@0 MAE 51.38 PASS; J08 re-check S08@5.12 → S09 t2@0 MAE 47.43 PASS; J09 re-check S09 t2@5.00 → S10@0 MAE 54.81 PASS. All FRESH turns, same Ball Park (teal, vermilion, gold light, cobalt water). J16/J17 BLOCKED — S17 not fired.

## VOLLEY 4 CLOSED 5/6 KEEP — S17 t1 OWED (generation failed, not retried per instruction)
- S18 t1 KEEP, S09 t2 KEEP, S19 t1 KEEP, S20 t1 KEEP, S21 t1 KEEP. S17 t1 NOT FIRED: media.generate_video internal worker error, no file on disk, no retry per instruction. Hardened vehicle ready for the follow-up run.
- Rebuild totals: volleys 1–4 = 21/23 scenes hold KEEP (S01–S16 minus S09 t1 REJECT + S13/S14 t1 REJECTs, all rerolled KEEP; S17 owed). Remaining: S17 t1 (reroll, 1 video) + volley 5 (S22, S23, 2 videos) = 3 videos to close the rebuild, then assembly.
- No commit, no delivered flag (parent writes it). Assembly is a follow-up run after all 23 scenes hold KEEP.

## Volley 5 — S17 t2, S22 t1, S23 t1 (this run, coordinator 9a1949a6)
- Parent-verified volley 4 ~06:24 EST: all 5 md5s match; volley 4 CLOSED 5/6 KEEP. S17 t1 NOT FIRED (internal worker error). Rebuild 20/23 KEEP.
- S17 refs REUSED from stack4 (md5s re-verified on disk this run: start 3ba313b1f252, end 526afe6e44b8 — exact match). Vehicle work/vehicles/mv11_r2_s17_vehicle.txt hardened and ready — REUSE verbatim.
- Stack5: S22/S23 pairs generated + read back at full res (4/4 PASS, all 2048x1152; S22 start = peak splash crown, S22 end = settling rings, S23 start = single ball hanging above still fountain, S23 end = ball dropped, one last ring). Recorded in work/REFERENCE_STACK5.md; contact sheet work/stills/stack2/stack5_contact_s22_s23.jpg. DISCLOSED: S22/S23 end refs use different fountain designs than their start refs (tiered / pedestal-basin vs round basin) — same plaza world, the journey morphs.
- Vehicles work/vehicles/mv11_r2_s22_vehicle.txt + mv11_r2_s23_vehicle.txt written, hardened from the start (no lyric quotes, never-leaves-the-plaza clause). S22 placed at the fountain plaza (158s peak splash ~take 2.94s); S23 CHAINS from S22 (J22), final drop rhymes with S01.
- Fire order (pairs): S17 t2 + S22 t1, then S23 t1. Joints J21 (S21→S22 FRESH) + J22 (S22→S23 CHAIN). J16/J17 unblock when S17 lands.
- Firing pair 1: S17 t2 + S22 t1 — BOTH LANDED.
- S17 t2 KEEP (md5 f5c6d7bf…; motion 21.18, longest 1f; M6 0.0042 / run 0.04s, no flag; dense 20/20 frames the dodgeball court, no retired world). Arc: volley → diving → peak ball storm 8.0–9.5s. Disclosed: players in dark navy shorts (background players, consistent); a few profile faces small mid-dive; "Thank you for watching!" audio only. Ledger row written. J16 UNBLOCKED (PASS).
- S22 t1 KEEP (md5 a7f9da60…; motion 4.35, longest 1f; M6 0.1590 but longest dup run 0.04s — flag bar needs both, NO FLAG; dense 20/20 frames the fountain plaza, no retired world). Arc: crown erupting at frame 0 → collapse ~3s, tiered fountain emerging → rings widening → balls at rest. Disclosed: 158s peak lands on the collapse not the eruption (soft alignment, CUTAWAY slot; whole 10s is the used span); fountain morphs round-basin → tiered ~3–4s; "Music" @2.4 audio only. Ledger row written. J21 PASS.
- Firing S23 t1 (last video of the volley) now.
- S23 t1 KEEP (md5 00b2fa29…; motion 5.73, longest 4f @0.00s; M6 0.0167 / run 0.17s, no flag; dense 20/20 frames the fountain plaza, no retired world). Arc: ball hanging → DROPS ~0.5s, one last ring blooming → ball bobbing, slow push-in, park still. THE LAST DROP lands; the final frame rhymes with the first. Disclosed: drop lands ~0.5s, earlier than the vehicle's 3–7s plan (soft alignment, CUTAWAY slot — final "Balls" unmeasured); pedestal fountain rises mid-take ~2.5–5s as the round basin morphs (same plaza world); "Thanks for watching!" 0.0–1.96s audio only. Ledger row written. J22 CHAIN PASS.
- Joint QC (joints_contact_v5.jpg, eye-read + MAE): J16 S16@9.22 → S17 t2@0 MAE 49.07 PASS (confetti rain → dodgeball court); J17 S17 t2@9.95 → S18@0 MAE 54.37 PASS (ball storm → pool-party wave); J21 S21@6.06 → S22@0 MAE 58.44 PASS (grand hall splash + pins → fountain plaza crown); J22 S22@9.95 → S23@0 MAE 42.34 PASS (settled tiered fountain → still fountain, single ball hanging — lowest MAE, as a chain should be; fountain design differs tiered vs round basin, world/lighting/palette hold). All FRESH turns except J22 CHAIN, same Ball Park throughout.

## VOLLEY 5 CLOSED 3/3 KEEP — REBUILD COMPLETE, 23/23 SCENES HOLD KEEP
- S17 t2 KEEP, S22 t1 KEEP, S23 t1 KEEP. All 3 videos used, no 429, no generation failures. All joints J16/J17/J21/J22 PASS.
- Rebuild tally: volleys 1–5 = 23/23 KEEP (S01–S23; the three volley-2/3 REJECTs — S09 t1, S13 t1, S14 t1 — all rerolled KEEP; S17 t1's volley-4 generation failure closed by t2 this run).
- Assembly notes carried forward: S21 — place take-time ~2.0–6.06 onto the slot (drop ~song 153.5, crown through the patter). S22 — crown erupts at take 0 and collapses ~3s; the 158s peak lands on the collapse; whole 10s is the used span. S23 — drop at take ~0.5s (song ~165.5s); calm bobbing tail fills the slot to the cut-clean last stab.
- No commit, no delivered flag (parent writes it). ASSEMBLY is the follow-up run: one 16:9 master, CRF 18, AAC 48k stereo, faststart, track.mp4 sole master audio, kinetic type in post on the song's own word grid.

## ASSEMBLY — REBUILD 2 (coordinator fef733aa, started ~06:45 EST)
- Inputs VERIFIED: track.mp4 md5 18273d7a593e623b720105df195bede2; all 23 R2 KEEP takes md5-match the R2 ledger (23/23, incl. S22 a7f9da60 restored row). ffmpeg 8.1.2, Noto Sans present, numpy ok, 26G free.
- Method: Nov 10 assembly toolchain, R2 variants in work/assembly_r2/ (Nov 10 scripts + work/assembly/ untouched). Per-scene CRF-14 intermediates (1280x720, 24fps) forced to contract frames, manifest checkpointed after EVERY segment. Split final encode at S12/S13 (78.66s). Kinetic .ass burn-in with the MV-13 FIT RULE (HIGHLIGHT/CASCADE lines scaled to est <=1100px; SLAM never scaled; zero double-backslash lines verified by grep before encoding).
- S07 (THE ONE SUNG SCENE) — MOUTH-ANCHORED pieces, not audio-phrase warps: take audio runs late (Water 3.52, My balls 6.28-8.22) but the VISIBLE mouth opens at take 2.0s + 3.5s (parent-verified full-res reads), matching the song onsets (slot 2.00s + 3.46s). Pieces: (0,48,48) 1.0x / (48,84,35) 0.972x / (84,120,36) 1.0x — take 0-5.0s continuous, rate changes only at the mouth anchors. An audio-phrase warp (0.53x) would put the mouth 0.65s early — rejected.
- S21 per the ledger assembly note: take-time 2.0-6.06 (frames 48-145) -> 97f, 1.0x; drop lands ~song 153.5, crown rises through the patter.
- All other scenes: uniform trims/slowdowns <=1.09x (S05 1.0417x, S06 1.0347x, S11 1.0833x, S15 1.0179x, S16 1.0231x); everything else 1.0x. No warp past the 2x cap anywhere; no freeze frames.
- BUILD STATUS ~12:04 EST: segments S01-S04 built + manifest-checkpointed (810f). S05 ffmpeg died 12:02 EST with EDQUOT (Disk quota exceeded, exit 134) — 4th EDQUOT hit of the morning, all transient so far; 20 MB probe passed again 12:03, partial S05.mp4 (3.5 MB) deleted, build resumed (session proc_6567d16d77eb, skips S01-S04). ~2-3 min/segment; 19 segments left. If EDQUOT strikes again, resume the same way — the script is idempotent per segment.
- BUILD STATUS ~12:52 EST: ALL 23 SEGMENTS BUILT, 4138f exact, no EDQUOT on the resumed run (48 min wall). Segment md5s in work/assembly_r2/assembly_manifest.json. Split-encode (kinetic burn-in, halves at S12/S13) starting next.
- ASSEMBLY DONE ~15:05 EST: halves 1888f/2250f (split-encode SIGTERM at the tail, both halves already complete on disk, verified before mux); master MUXED 4138f md5 3e914df3d92fabab317268d24609149e, 200,502,407 B. ALL GATES PASS (audio agreement min corr 0.9977; SEI crf=18.0; faststart moov@36). Motion audit PASS (0 near-still runs >=12f, mean diff 17.06). Chat copy 40,728,025 B (38.8 MB) md5 06aef1d49ff3d33d26398624bdffd050, audio md5 == house. Kinetic: 7 full-res frames read (15.0/22.5/27.0/47.5/99.0/133.0/171.5) — no overflow/cut/misplaced; L15b scaled fs54->39 by FIT RULE. Flag MV11_REBUILD2_DELIVERED.flag written with gate numbers + disclosed flaws. Old master untouched.
