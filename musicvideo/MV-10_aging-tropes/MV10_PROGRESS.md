# MV-10 "Aging tropes" — PROGRESS

Track: track.mp4 md5 `fd60ac7335e3bdb55d97a2242dbee38c`, 178.0s.
Grid: measured ~108 BPM (0.556s, phase 0.152s). Plan:
`work/MV_PREPRO_MV-10.md` (13 scenes, 22 takes). Design:
`CONCURRENT_DESIGN.md` (paired with MV-9).
Status: INTAKE DONE 2026-11-09. Scene plan written. Volley 1 NOT
yet fired — parent chains it after MV-9 volley 1.

## Volley 1 (fired 2026-11-09 ~10:20 EST by recovery coordinator — previous coordinator died ~10:11 EST, daemon restart; takes/ was empty, 6 vehicles reused)
- [x] S04a hook — KEEP mv10_s04a_t1.mp4 (md5 1add1909…) — hook test PASS, look proven
- [x] S01 night bedroom — KEEP mv10_s01_t1.mp4 (md5 0acc63e2…)
- [ ] S02 sit-up singing — t1 REJECT (G4: profile turn during "prostate check"); reroll owed volley 2, axis facing/staging
- [x] S05 soup montage — KEEP mv10_s05_t1.mp4 (md5 a3c8eaac…)
- [x] S08 longest breath — KEEP mv10_s08_t1.mp4 (md5 81682a2f…)
- [x] S09a memory four-squares — KEEP mv10_s09a_t1.mp4 (md5 c4259d63…)

Volley 1 result: 5 KEEP / 1 REJECT (S02). Cap 6/6 used. Volley 2 owed: S02 reroll (facing/staging) + S03a, S03b, S04b, S06a, S06b (5 more, cap 6).

## Volley 2 (DONE 2026-11-09 — S02 reroll v2 axis facing/staging + S03a, S03b, S04b, S06a, S06b)
- [x] S02 reroll v2 — KEEP (c3ccb8fe…) — facing/staging axis FIXED, front-on through "prostate check"; ratio 1.50 grey zone, full line once; 33f whole-frame run widened to mouth-band 16f + eye check (mouth moves at word onsets)
- [ ] S03a bend over — NOT FIRED (integrity_check_failed; not retried per instruction). Slot owed, parent to decide.
- [x] S03b pocket stays tight — KEEP (4331e7af…) — ratio 1.11; doc's mouth closed; wallet + plain wristband + phone all correct; board text illegible
- [x] S04b hook block 2 — KEEP (6ff772bf…) — ratio 1.18; mouth wide open on "oh"; mirror + shuffle right
- [ ] S06a standing slower — REJECT (3f8ce6bd…) — G4: turns to profile ~5.5s, walks away back-to-camera mid-line; reroll v2 axis facing/staging owed V3
- [x] S06b soup on stove — KEEP (e20d5e06…) — ratio 0.95; head drifts ~30° toward pot in last 0.5s of vocal window, mouth stays visible (disclosed)

Volley 2 result: 4 KEEP / 1 REJECT (S06a) / 1 NOT FIRED (S03a). 5 successful generations (cap 6). Running total: 9 KEEP / 2 REJECT / 1 NOT FIRED across V1+V2.
Volley 3 owed: S06a reroll v2 (facing/staging) + S06c, S07a, S07b, S09b, S10a. S03a UNFIRED — parent decision ~10:50 EST: restage in V4 on a new axis (seated exam-table, no bent-over pose; new vehicle, never verbatim re-fire).

## Volley 3 (DONE 2026-11-09 — S06a reroll v2 axis facing/staging + S06c, S07a, S07b, S09b, S10a)
- [ ] S06a reroll v2 — REJECT (b900dbf6…) — G4 STILL FAILS: front-on through "kids pay" (f_7.5), turns at ~7.95s, full profile mid-"rent." (f_8.3), back view by 9s. Line complete once, ratio 1.16 in band — fail is staging only. Secondary G2: legible "RENT" on the envelope. SECOND denied reroll → scene RETIRED from reroll (Slopcannon stage 4); fresh staging owed, parent decides.
- [x] S06c bass don't quit — KEEP (bea9ec5b…) — ratio 1.13; mouth open on "sucks"; front-on through the vocal window (turn at 8–9s is post-vocal, prompted end state); phone R / wristband L; sits in bed (anchor replica) — staging drift, not a fail.
- [ ] S07a bop again — REJECT (011ceafd…) — HARD RULE: a child (~8–10, yellow cardigan, soup pot) stands in the doorway the whole take; vehicle said grown kids/adults. Otherwise strong (full line once, ratio 1.19, front-on, mirror right). Secondary G2: legible "RENT" on the woman's envelope. REROLL AXIS: staging — drop the doorway figures entirely, S04a hallway+mirror only. First denied reroll. Owed V4.
- [x] S07b soup montage 2 — KEEP (177e3139…) — montage volley, fast cuts, plain wristband, no text, adults only.
- [x] S09b memory fence — KEEP (dd5d632b…) — fence + hazy figures + wash station, plain blue doors, no text, motion mean 15.06.
- [x] S10a memory chorus — KEEP (92eb8f45…) — two-image journey old → young WORKED; full line once; ratio 0.66 GREY ZONE, assembly speeds vocal span 1.51x (within caps, disclose); mouth open on final "oh" (f_7.9/f_8.2); wristband not visible (disclosed).

Volley 3 result: 4 KEEP / 2 REJECT. Running total: 13 KEEP / 4 REJECT / 1 NOT FIRED across V1+V2+V3.
Volley 4 (parent-confirmed ~11:25 EST): S03a restage (new axis) + S06a fresh staging (seated armchair, rise only after last word) + S07a reroll v2 (no doorway figures) + S10b, S11a, S11b. V5: S12, S13a, S13b (+ re-fire slots).

## Log
- 2026-11-09: intake + audio analysis + timelines written by parent.
  Scene plan + character lock + asset board written (this coordinator).
- 2026-11-09 ~10:20 EST: VOLLEY 1 fired by recovery coordinator (revive detector; previous coordinator died ~10:11 EST, daemon restart, takes/ empty; 6 vehicles + anchor still reused). 6 videos, 5 KEEP / 1 REJECT: S04a KEEP (hook test PASS, look proven), S01 KEEP, S05 KEEP, S08 KEEP, S09a KEEP, S02 t1 REJECT (G4 — profile turn during "prostate check"; reroll axis facing/staging, owed volley 2). QC script work/qc/qc_v1_rest.py; per-take qc in work/qc/<scene>-t1/.
- 2026-11-09 ~10:4x EST: VOLLEY 2 fired (this coordinator). 6 vehicles written, 5 videos landed: 4 KEEP / 1 REJECT / 1 NOT FIRED. S02 t2 KEEP (facing/staging FIXED, front-on through "prostate check"; ratio 1.50 grey zone), S03b KEEP (ratio 1.11), S04b KEEP (ratio 1.18), S06b KEEP (ratio 0.95), S06a t1 REJECT (G4 — turns away mid-line, walks off back-to-camera; reroll v2 axis facing/staging owed V3), S03a NOT FIRED (integrity_check_failed on the generation call; not retried per instruction — parent to decide). QC script work/qc/qc_v2.py; per-take qc in work/qc/<scene>-t1/ + close/ frames.
- 2026-11-09 ~11:0x EST: VOLLEY 3 fired (this coordinator). 6 vehicles written, 6 videos landed: 4 KEEP / 2 REJECT. S06c KEEP (ratio 1.13), S07b KEEP (montage volley), S09b KEEP (memory fence, motion 15.06), S10a KEEP (two-image old→young journey WORKED; ratio 0.66 grey zone, 1.51x speedup at assembly). S06a t2 REJECT (G4 — turns during final words "the rent."; SECOND denied reroll → scene RETIRED from reroll, fresh staging owed, parent decides; secondary G2 legible "RENT" envelope). S07a t1 REJECT (HARD RULE — a child ~8–10 in the doorway the whole take; reroll axis staging: drop doorway figures, S04a hallway+mirror only; secondary G2 legible "RENT" envelope). Running total 13 KEEP / 4 REJECT / 1 NOT FIRED. QC script work/qc/qc_v3.py; per-take qc in work/qc/<scene>-t1/ + <scene>-t2/ + close/ frames.
- 2026-11-09 ~11:3x EST: VOLLEY 4 firing (this coordinator). 6 vehicles written, 6 videos to fire: S03a RESTAGE v2 (seated exam-table, parent decision ~10:50 EST), S06a FRESH staging (seated armchair throughout vocal window, parent decision ~11:25 EST), S07a reroll v2 (drop doorway figures entirely, S04a staging), S10b (two-image young→old return, no words), S11a, S11b (final bop 1+2). QC script work/qc/qc_v4.py.
- 2026-11-09 ~11:5x EST: VOLLEY 4 DONE (this coordinator). 5 videos landed: 5 KEEP / 0 REJECT / 1 NOT FIRED. S06a t3 KEEP (fresh staging FIXED the G4 axis — seated front-on throughout, rise only after the last word; disclosed 0.42s bed-shot head + swing-warp note), S07a t2 KEEP (hard rule CLEARED — no doorway figures, no children; mouth wide open on the "oh"s; disclosed compressed 2.12s pause), S10b t1 KEEP (two-image young→old return WORKED, mirroring S10a; zero words, correct), S11a t1 KEEP (final chorus lands; disclosed "drink it" ×3 vs song ×10 — patter tail covered by CASCADE montage per the plan's SINGING/MONTAGE tag), S11b t1 KEEP (full short line once, mouth open on "don't stop"; disclosed WARP RISK — slow "Bop-bee-bop" needs ~2.9x phrase compression, overall ~1.76x at the proven rescue edge; assembly must verify the warped render passes the mouth gate or S11b is owed a re-fire in V5). S03a v2 NOT FIRED (integrity_check_failed on the seated exam-table restage — SECOND failure for this scene; parent decision ~11:36 EST: third restage moves the scene OUT of the exam room entirely, slots into V5). Running total 18 KEEP / 4 REJECT / 2 NOT FIRED. V5 owed: S03a restage v3 (out of the exam room, per parent decision) + S12, S13a, S13b (+ re-fire slots incl. S11b if the warp fails). QC script work/qc/qc_v4.py; per-take qc in work/qc/<scene>-t3/ + <scene>-t2/ + <scene>-t1/ + close/ frames.

## Volley 5 (DONE 2026-11-09 — S03a restage v3 + S12, S13a, S13b)
- [x] S03a restage v3 — KEEP (a549cfdb…) — THE FILTER PASSED: hazy recollection at the fence, no exam room, no doctor, no table, no clinic on screen. Full line once 0.00–6.34s, ratio 1.03 in band; mouth WIDE open on "sucks" (f_5.0). Fence + four squares + QR phone + plain porta-potties. Disclosed: eyes closed throughout (recollection); 12fps doubling; wristband partially visible at frame edge.
- [x] S12 tail — KEEP (1763d807…) — full sheet line once 0.00–8.28s, 19 words. Ratio 1.30 GREY ZONE (assembly swing-warps 1.30x, within cap). Mouth open on "don't stop" (f_2.0) and "pocket stays tight" (f_7.0). Disclosed: opens in the bedroom, hallway from ~0.7s (S06a-t1 pattern); mouth nearly closed at 0.5s on the first "Bop" (mouth-lag); wall posters illegible scribble.
- [x] S13a memory resolves — KEEP (1a5c5a87…) — two-image journey WORKED: young man at the festival → morph holds BOTH faces in one frame (f_2.0) → old man in bed, QR phone carrying across. 0 words, correct. Disclosed: 31f near-still run at 8.67–9.96s sits PAST the assembly cut (uses 0–6.2s).
- [x] S13b morning glass — KEEP (80e20cf2…) — the morning glass LANDS, last frame rhymes with S01. 0 words, correct. Disclosed: first ~2s is a night beat before the reach; 14f run at 7.58s past the 6.6s assembly cut.

Volley 5 result: 4 KEEP / 0 REJECT / 0 NOT FIRED. Running total: 22 KEEP / 4 REJECT / 2 NOT FIRED. All 22 planned takes now hold a KEEP — every scene covered. Assembly next (parent chains). S11b warp risk remains an assembly check (warped render must pass the mouth gate). QC script work/qc/qc_v5.py; per-take qc in work/qc/<scene>-t3/ + <scene>-t1/ + close/ frames.
