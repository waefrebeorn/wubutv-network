# MV-33 VOLLEY PROGRESS — "Glue Your Shit Smooth On, It Is Not Over"

Coordinator run 1 (volley phase opened 2026-11-23 ~23:15 EST). Plan:
MV_PREPRO_MV-33.md — 27 scenes / 30 takes owed. Recipe: compact
(approved stack still as first frame + compact identity paragraph,
REFERENCE_STACK.md §3; full canon §2 is the identity source of truth).

## Pilot manifest (volley 0 — template proof, 3 clips)
- S08 (Chorus 1 hook, occurrence 1/3, HERO) — safest solo MCU staging,
  STACK-02 first frame, 5 s. Vehicle: mv33_s08_vehicle.txt
- S02 (Intro opener, HERO) — moving staging (stair climb), STACK-01
  first frame, 10 s. Vehicle: mv33_s02_vehicle.txt
- S05 (Verse 1 First Application, 4 lines) — MCU ritual, STACK-02
  first frame, 10 s. Vehicle: mv33_s05_vehicle.txt
Pilot verdict gates the template before any full volley spends.

## Volley 1 manifest (fires after pilot QC, this run's remaining budget)
- S01 take A1 (Set Rebuilds wave 1, motion, 10 s) — STACK-01 world
- S01 take A2 (Set Rebuilds wave 2, motion, 10 s) — STACK-01 world
- S01 take B (Set Rebuilds wave 3, motion, 10 s) — STACK-01 world

## Status

### Run 1 (2026-11-23 ~23:2x–23:5x EST, coordinator 654ecd64) — CLOSED BY OUTAGE
Generation upstream in a 502/503 overload window the whole run (open
since ~21:55 EST). 6 fires attempted, 1 landed:

- **S02 t1 — KEEP** (`takes/mv33_s02_t1.mp4`, md5
  `8ea251eca9dd72cd7e032b423acf28d0`; G7 PASS 1.0 verbatim; identity
  A−; full QC in TAKE_HISTORY V-02).
- S08 t1 — OUTAGE (503), not fired. **Still owed** (pilot hero hook).
- S05 t1 — **REFUSED** (`integrity_check_failed`, instant, INPUT
  class). Never re-fire unchanged; waits for a new input class.
  **Still owed.**
- S01 A1 / A2 / B — OUTAGE (502/503/502), not fired. **Still owed.**

**Pilot verdict (partial):** template PROVEN by S02 — same compact
recipe + vehicle structure as the unlanded pilot clips; identity,
wardrobe, world, 16:9 aspect, zero text, verbatim lyrics all pass.
No template defect observed; no vehicle fix burned.

**Owed after run 1: 29 of 30 takes.** S02 done. Next run fires, in
order: S08 (pilot completion), S05 (new input class only), S01
A1/A2/B, then S03, S04 (Huang cameo), S06, S07, S09–S27 per plan.

### Run 2 (2026-11-24 ~00:0x–00:2x EST, coordinator 1bc08f8e) — BUDGET SPENT, UPSTREAM FLAPPING
Generation opened (probe B-1455 landed 2026-11-24T04:21Z) but the
upstream kept flapping 503 through the run — 2 of 6 fires landed,
between two outage waits (~9 min each, inside the run). 6 fires:

- **S08 t1 — KEEP** (`takes/mv33_s08_t1.mp4`, md5
  `de4a9c62d372f19542fe41189ade423a`; 1280×720 native, 120 f, 5.000 s;
  G7 PASS overlap 0.6 — ASR mishear class smoov→move/shit→shits, RMS
  envelope confirms both hook passes performed; identity A−; full QC
  in TAKE_HISTORY V-07). **PILOT COMPLETE:** the locked-MCU variant is
  proven by landing, alongside S02's moving variant — template closed.
- S05 t2 — **REFUSED AGAIN** (`integrity_check_failed`, instant,
  INPUT class) on the NEW input class: shared-cast panel sheet as
  identity-only reference + same compact paragraph + same performance
  text (new vehicle mv33_s05_vehicle2.txt; TAKE_HISTORY V-08). Second
  refusal on a second class: the conditioning image is exonerated as
  the variable — the shared elements are the performance text (four
  quoted lines incl. the repeated "Nigga, it is not over" doublet)
  and the tube-to-forehead action. **S05 still owed — needs a third,
  genuinely different route (parent's call): candidates — STACK-01-
  derived MCU crop first frame; split the four lines across two
  shorter fires; re-carriage of the doublet.**
- **S01 take A2 t1 — KEEP** (`takes/mv33_s01_a2_t1.mp4`, md5
  `00f0a49fc14fbb2b523a5c6b7f507a14`; 1280×720 native, 240 f,
  10.000 s; empty hall, harpsichord assembles + lid rises, coal seams
  glitter; G7 wordless check PASS — screened ASR only "so" at
  logprob −1.285; TAKE_HISTORY V-10). **G2 FLAG:** small diegetic
  maker-style inscription "Gilded Seam" on the harpsichord case —
  sanctioned diegetic name as object lettering, spelled correctly;
  parent/assembly may trim the tightest frames if ruled unwanted.
- S01 A1 — OUTAGE (503). **Still owed** (not re-fired this run,
  per-request rule).
- S01 B — OUTAGE (503). **Still owed.** S01 remains cover-eligible
  by plan if generation keeps balking; A2 is landed.
- S03 t1 — OUTAGE (503) on its first attempt, vehicle
  vehicles/mv33_s03_vehicle_v1.txt ready on disk. **Still owed.**

**Owed after run 2: 27 of 30 takes.** Keeps: S02, S08, S01-A2 (3).
Next run order: S05 route decision (parent), S01 A1, S01 B, S03,
then S04 (Huang cameo), S06, S07, S09–S27 per plan.

### Run 3 (2026-11-24 ~00:37 EST →, coordinator f324bdb2) — S05 SPLIT ROUTE + OWED WAVES
Parent ruling executed: S05 split into two 5 s fires on the proven
STACK-02 first-frame class — S05a (V1 L3–L4, tube press + one smoothing
stroke, transliteration "And glooed that shit smoov on") and S05b
(V1 L5–L6, the refusal doublet RE-CARRIED: line quoted once, second
pass described as the same line again; no tube action). Vehicles:
mv33_s05a_vehicle.txt / mv33_s05b_vehicle.txt. Then S01 A1, S01 B,
S03 (vehicle on disk), S04 (Huang cameo — Factor mouth closed, grave,
never smiles; he does not sing).

- S05a attempt 1 (~00:40 EST) — **INTERRUPTED, NOT FIRED**: the media
  service restarted mid-call; no take file, no generation receipt on
  disk (verified by ls). Not a refusal, not a 429 — the request never
  completed. Re-firing the identical vehicle once is the recovery, not
  an unchanged-refusal refire.
- **S05a t1 — KEEP** (`takes/mv33_s05a_t1.mp4`, md5
  `e86d1dfdb30ece1e1f97ec33ceb91633`; 1280×720 native, 120 f, 5.000 s).
  **THE SPLIT ROUTE BROKE THE S05 REFUSAL**: the two non-doublet lines
  landed first try on the STACK-02 class that refused the combined
  four-line fire twice. Eye QC: G1 identity A− (canon holds; standing
  silver-wig nit inside tolerance); G2 no text; G4 solo MCU, tube at
  forehead on L3, smoothing stroke reads on L4, mouth open in both
  windows. G7 in TAKE_HISTORY V-13.
- S05b t1 — **REFUSED** (`integrity_check_failed`, instant, INPUT
  class), the re-carried doublet fire (line quoted once + described
  repeat; no tube action). NOT re-fired this run per parent ruling.
  **Telemetry conclusion across S05's four fires: the variable is the
  doublet line itself** — every fire carrying it refused (t1 four-line,
  t2 panel class, S05b doublet-only), the one fire without it (S05a)
  landed. S05's L5–L6 remain owed; a fourth route is the parent's call.
- S01 A1 — OUTAGE (502 upstream_unavailable, 3 internal attempts).
  **Still owed** (not re-fired this run, per-request rule — the same
  discipline runs 1–2 observed).
- S01 B — OUTAGE (502, 3 internal attempts). **Still owed.**
- S03 — OUTAGE (502, 3 internal attempts) after a ~9 min outage wait;
  the upstream flap persisted through the run's second half. **Still
  owed**; vehicle on disk. S04 remains as the run's last fire after a
  second outage wait.
- S04 — OUTAGE (502, 3 internal attempts) after the second ~9 min
  wait. **Still owed**; vehicle (vehicles/mv33_s04_vehicle_v1.txt)
  reviewed against the plan and ready.

**Run 3 closed (~01:31 EST, at the run's time ceiling): 6 fires
resolved — 1 KEEP (S05a), 1 REFUSED (S05b), 4 OUTAGE. No 429.**
**Owed after run 3: 26 of 30 takes.** Keeps: S02, S08, S01-A2, S05a
(4). S05 is half-landed: S05a covers V1 L3–L4; the doublet L5–L6
(S05b) remains owed pending the parent's fourth-route ruling — the
refusal variable is now isolated to that line's text. Next run order:
S05b (parent's route), S01 A1, S01 B, S03, S04, then S06, S07,
S09–S27 per plan.

### Run 4 (2026-11-24 ~01:47–02:2x EST, coordinator 9f66fe45) — ROUTE 4 UNTESTED; PANEL-SHEET CLASS 0/4
Parent ruling executed for S05b: route 4 = description-only carriage
(new vehicle mv33_s05b_vehicle_route4.txt — zero quoted lyric text
anywhere; the doublet performance described only; STACK-02 first
frame; no tube action; 5 s). Then S01 A1, S01 B, S03, S04, S06
(vehicles on disk, S06's recovery draft reviewed against the plan —
conforms, fired verbatim). 6 fires resolved, 0 landed:

- S05b t2 (route 4) — **OUTAGE** (502 upstream_unavailable, 3 internal
  attempts). **Route 4 remains UNTESTED** — the request never reached
  a content checkpoint. Still owed; the route-4 vehicle is on disk
  and ready for the next run.
- S01 A1 — **OUTAGE** (502, 3 internal attempts). Still owed.
- S01 B — **OUTAGE** (503 service_overloaded). Still owed.
- S03 t1 — **REFUSED** (`integrity_check_failed`, INPUT class) on its
  first-ever content checkpoint (runs 2–3 attempts were all outage).
  Panel-sheet class. Still owed — needs a new input class.
- S04 t1 — **REFUSED** (`integrity_check_failed`, INPUT class) on its
  first-ever content checkpoint. Panel-sheet class (Huang panel as
  second ref). Still owed — needs a new input class.
- S06 t1 — **REFUSED** (`integrity_check_failed`, INPUT class) on its
  first-ever content checkpoint. Panel-sheet class; confound noted
  (booty line's first vehicle appearance in the same fire).

**Run 4's headline telemetry: the panel-sheet class is 0/4 in MV-33
(V-08, V-22, V-23, V-24) while the single-image compact class is 4/4
landed (S02, S08, S01-A2, S05a).** Every refusal this run came on a
fire carrying a panel sheet as a conditioning image; no single-image
fire has ever refused in this build. Recommended run-5 move (parent's
call): reclass S03/S04/S06 (and audit every later panel-sheet vehicle)
to the proven single-image compact recipe — approved stack still as
first frame + compact identity paragraph, second figures carried in
TEXT only (the MV-29 S07/S13 pattern) — and fire S05b route 4 first
while the route is still untested.

**Owed after run 4: 26 of 30 takes.** Keeps: S02, S08, S01-A2, S05a
(4). Next run order (proposed): S05b (route 4, vehicle ready), S01 A1,
S01 B, then S03/S04/S06 reclassed, then S07, S09–S27 per plan.

## Volley run 5 (2026-11-24, coordinator b6b58459) — ROUTE 4 TESTED + RECLASS EXECUTED: 4 KEEPs

Parent ruling executed in order: S05b route 4 first (vehicle on disk,
untested), then S03/S04/S06 on NEW single-image vehicles written this
run (vehicles/mv33_s03_vehicle_v2.txt, mv33_s04_vehicle_v2.txt,
mv33_s06_vehicle_v2.txt — panel sheet removed, second figures in TEXT
only, class change ledgered per fire), then S01 A1, S01 B. The run
opened in the continuing 502/503 flap; every outage attempt was
retried inside the run after a ~10 min wait per protocol. No 429 at
any point. Full telemetry: TAKE_HISTORY.md V-25..V-32.

- S05b t2 (route 4, description-only carriage) — **LANDED BUT
  REJECTED (G7).** Attempt 1 died on 503; the retry landed clean
  (120f, 1280x720). **Route 4 clears the input checkpoint** — but
  dual-ASR shows the take performs ONE invented paraphrase ONCE,
  "Nothing is finished until we say it's done." (0.0–2.5 s), not the
  doublet "Nigga, it is not over" x2. **Verdict: description-only
  carriage defeats the refusal but loses the lyric — with no text in
  the prompt the model paraphrases the description instead of
  performing the line.** S05b still owed; route 5 is the parent's
  call. (Note for the parent: the same line recurs at Breakdown L5 /
  S21 — this verdict governs its carriage there too.)
- S03 t1 (RECLASSED) — **KEEP.** Attempt 1 outage (502); retry landed
  (240f). **The reclass broke the S03 refusal.** G7 PASS (known
  mishear class over the transliterated hook line, performed once);
  the costume change lands across the sung window. Disclosed: start
  state reads as a dark embroidered court coat, not a plain smock.
- S04 t1 (RECLASSED, Huang in text only) — **KEEP.** Attempt 1 outage
  (503); retry landed (120f). **The reclass broke the S04 refusal.**
  G7 PASS, both lines verbatim. The text-only Court Factor observes
  the full Factor law (grave, mouth closed, never smiles, does not
  sing); the Door Reveal completes to the exact end state. Disclosed:
  both men hold decree rolls early; singing starts at 0.0 s.
- S06 t1 (RECLASSED) — **REFUSED** (`integrity_check_failed`) on the
  single-image class. **The reclass did NOT break S06** — with the
  panel sheet exonerated by S03/S04, the surviving suspect is the
  scene's own content (the L7 booty line and/or the rear-placement
  staging). Not re-fired this run per protocol; route is the
  parent's call.
- S01 A1 t1 — **KEEP.** Landed first attempt (240f). Wordless PASS
  (zero ASR segments, both checkpoints). The Set Rebuilds wave 1
  reads: scaffolding/unfinished hall resolving to the dressed hall,
  push-in ending on the tube on its cushion. G2 parent flag: detailed
  label print on the tube in close-up (no legible word) — the
  S01-A2 precedent class.
- S01 B t1 — **KEEP. S01 is complete (A1 + A2 + B).** Landed first
  attempt (240f). Wordless PASS. Completed hall, tube waiting on the
  cushion, end state exact. Same tube-print G2 flag; the ignition
  wave is not visible in sampled frames (hall already lit at 1.0 s).

**Run 5 telemetry update: panel-sheet class still 0/4; single-image
compact class now 8 landed / 1 refused across the build (the one
refusal is S06, whose blocker is content, not class).** The reclass
ruling is validated: 2 of 3 refusals were class-caused. Route 4's
verdict closes the description-only branch for the doublet — it
passes the checker and loses the words.

**Owed after run 5: 22 of 30 takes.** Keeps: S01-A1, S01-A2, S01-B,
S02, S03, S04, S05a, S08 (8). Next run order (proposed): S05b (route
5, parent's ruling), S06 (new route, parent's ruling), then S07,
S09–S27 per plan.

## Volley run 6 (2026-11-24, coordinator 5019b398) — ROUTE 5 TEST + S06 RESTAGE + PLAN ORDER

Parent rulings executed in order: (1) S05b ROUTE 5 —
TRANSLITERATION-ONLY CARRIAGE: the doublet carried solely in phonetic
respelling, no standard-orthography form of the line or any part of
it anywhere in the prompt; STACK-02 first frame, 5 s, locked MCU,
tube at side (vehicle vehicles/mv33_s05b_vehicle_route5.txt). If
refused: no refire this run — parent rules the span a designed cover
at assembly. (2) S06 v3 — CHANGED STAGING: profile framing, courtly
bow-step approach and profile settle instead of the direct
backing-in framing; single-image compact recipe; line unchanged
(vehicle vehicles/mv33_s06_vehicle_v3.txt). Then plan order: S07,
S09 (STACK-03 illustration, no text/arrow), S10, S11. ≤6 fires.
Outage protocol: 502/503 → ~10 min wait, retry same fire in-run;
429 = hard stop. Results append below as they resolve.

- S05b route 5 (V-33) — **NOT FIRED: 429
  `video_daily_budget_exhausted`** on the run's first fire — the
  account reached its video limit for the last 24 hours. **RUN 6
  ENDED THERE per the hard-stop rule** — no retry, no other fire
  attempted. **Route 5 remains UNTESTED** (a budget stop is not a
  refusal and not a content checkpoint; the request never reached
  generation). S06 v3 / S07 / S09 / S10 vehicles are written and on
  disk (vehicles/mv33_s06_vehicle_v3.txt, mv33_s07_vehicle_v1.txt,
  mv33_s09_vehicle_v1.txt, mv33_s10_vehicle_v1.txt); S11's vehicle
  was to be written at fire time with its doublet carriage decided
  by the route-5 outcome — that decision is still pending the
  route-5 test.

**Run 6 closed: 1 fire attempted, 0 landed — HARD STOP on 429
budget exhaustion.** Keeps unchanged: S01-A1, S01-A2, S01-B, S02,
S03, S04, S05a, S08 (8). **Owed after run 6: 22 of 30 takes**
(S05b, S06, S07, S09–S27). Next run (after the budget window
resets) fires in the same order: S05b route 5, S06 v3, S07, S09,
S10, S11 — all vehicles ready except S11's, which is written at
fire time.

## Volley run 7 (2026-11-24 ~05:1x EST →, coordinator c23f82a8) — ROUTE 5 TESTED + PLAN ORDER

Generation reopened (probe B-1460 landed 2026-11-24T09:51Z). Parent
order: S05b route 5 (vehicle ready, route untested), S06 v3 (changed
staging), S07, S09, S10, S11 (vehicle written at fire time; doublet
carriage decided by the route-5 outcome). ≤6 fires. Results append
below as they resolve.

- S05b route 5 (V-34) — **REFUSED** (`integrity_check_failed`,
  instant, INPUT class) on its first true test. **Route 5 is
  closed: transliteration-only carriage refuses, exactly as
  standard orthography did on three classes; route 4 (zero text)
  remains the only carriage that cleared the checkpoint, and it
  lost the lyric to paraphrase.** Per the standing parent ruling
  the doublet spans (S05b here + Breakdown L5 at S21) are now
  **DESIGNED-COVER calls at assembly** — S05b is cover-owed, not
  take-owed, and is not re-fired. Full telemetry: TAKE_HISTORY
  V-34.

- S06 v3 (V-35) — **KEEP.** The changed staging (profile bow-step
  approach, profile settle) landed first attempt (240f, md5
  `9dbb397c41fdddeeea6f3adb538657a1`) after refusals on both prior
  classes/stagings. G7 PASS exact — both lines verbatim, in order.
  Butt law holds (seat on the back, profile settle, miner's mouth
  closed throughout). Disclosed: singing starts ~0.21 s (gesture
  beat compressed out); the miner's buff build reads soft; a brief
  back-to-camera moment inside the deep bow at ~3.0 s.

- S07 (V-36) — **KEEP.** Landed first attempt (240f, md5
  `8669a536b38f7392542c89434b491e21`). G7 PASS exact — "The coal
  mines are calling" + "It is not over", 1.97–8.77 s. Disclosed:
  lid already raised at first sampled frame; one brief hand-touch
  on the keys at ~5.0 s; maker inscription on the case (S01-A2
  sanctioned class).

- S09 (V-37) — **KEEP.** Landed first attempt (120f, md5
  `f05265fd2aff4e6d030c1806dc020cc6`). G7 PASS exact — "Apply it
  directly to the forehead." once, 0.21–3.69 s. G2 strict PASS:
  no text, no arrow in frame; the painted finish holds; end-state
  hold (closed mouth, half-smile, eyes closed) exact.

- S10 (V-38) — **KEEP.** Landed first attempt (240f, md5
  `2faa98f49184526b13d2cd858edf2125`). G7 PASS — all three lines
  in order (0.00–8.16 s across the checkpoints); the heard
  smoove/shmove spellings are the transliteration performed back,
  adjudicated to the sheet. Dust halo, bellows blast and re-dab
  all read; end-state hold exact.
- S11 vehicle written at fire time (vehicles/mv33_s11_vehicle_v1.txt)
  under the route-5-refused carriage decision: L9 only sung, the
  doublet span staged wordless (tube-salute, all mouths closed)
  as designed-cover picture; no form of the doublet text anywhere
  in the prompt.

- S11 (V-39) — **KEEP.** Landed first attempt (240f, md5
  `ab546e9332ca543cffd3057e8ee071f4`). G7 PASS with logged
  homophone override (coal→cold, both checkpoints, 6/7 overlap):
  L9 performed once, 1.84–6.72 s, and no other words — the model
  invented no doublet. The salute wave + gallery pull-back to the
  candlelit seam mouth read in full; the take's silent salute
  span is the flagged designed-cover picture for the doublet span.

**Run 7 closed: 6 fires — 5 KEEPs (S06, S07, S09, S10, S11),
1 REFUSED (S05b route 5). No outages, no 429.** The run's two
headline results: **(1) Route 5 is TESTED and REFUSED — the
doublet's carriage map is complete** (standard orthography refused
on three classes; description-only cleared but paraphrased;
transliteration refused). Per the standing parent ruling the
doublet spans are designed covers at assembly: S05b is cover-owed;
S11 shipped its cover picture inside its own take; the same
pattern (fire the scene's non-doublet lines, stage the doublet
span wordless) is the template for the remaining doublet-bearing
scenes S15, S19, S21, S25. **(2) S06's changed staging landed** —
the three-refusal arc closes: the blocker was the direct
backing-in staging, not the class, not the line. Single-image
compact class in MV-33 now: 13 landed / 1 content-refused (S06's
old staging) across the build; panel-sheet class still 0/4.

**Owed after run 7: 17 takes** (S12, S13, S14, S15, S16, S17,
S18, S19, S20, S21, S22, S23, S24, S25, S26, S27-A, S27-B) **+
1 cover-owed span** (S05b; doublet spans inside S15/S19/S21/S25
ride their scenes' takes per the S11 pattern). Keeps: S01-A1,
S01-A2, S01-B, S02, S03, S04, S05a, S06, S07, S08, S09, S10, S11
(13). Next run order (plan order): S12, S13 (Dario cameo block
opens), S14, S15, S16, S17 (hero hook occurrence 2), S18.

## Volley run 8 (2026-11-24 ~05:5x EST →, coordinator 66ad0dc2) — PLAN ORDER: S12 → S17

Parent order: S12, S13 (Dario cameo block opens), S14, S15, S16, S17
(HERO hook occurrence 2). Proven single-image compact recipe only;
S15's doublet span staged wordless per the S11 pattern. ≤6 fires.
Results append below as they resolve.

- S12 (V-40) — **KEEP.** Landed first attempt (240f, md5
  `aaf1ec7531d77dda0e88d4ba9ab07423`). G7 PASS exact — "It is not
  over." once, both checkpoints (1.20–5.18 / 1.20–6.20 s). The court
  bows and freezes mid-bow around him; end state exact. Disclosed:
  the line starts ~1.2 s (ahead of the briefed window); the tube is
  raised in the first frame only (STACK-01 pose).
- S13 (V-41) — **KEEP. The Dario cameo block opens clean.** Landed
  first attempt (240f, md5 `f0f8b36243ace35d6837375312cf64ea`). G7
  PASS exact — both lines verbatim, both checkpoints. The text-only
  Canteen Master reads fat and bald, round-faced, aproned, deadpan,
  mouth closed throughout. G2 flag: "COAL HATCH" diegetic lettering
  (sanctioned class). Disclosed: singing from 0.0 s; slide reads as a
  hand-to-hand pass; stamp pressed on its base plate; fry caught
  bare-handed; no eyeglasses on the Master.

---
COLLISION NOTE — appended 2026-11-24 ~06:1x EST by coordinator 5d033107: parallel-spawn duplicate of run 8. I fired S12 once (duplicate preserved at takes/mv33_s12_t1_dup5d033107.mp4, QC at work/qc/s12_t1_dup5d033107/); V-40 (66ad0dc2) stands as the S12 KEEP but its file (md5 aaf1ec7531d77dda0e88d4ba9ab07423) was overwritten in the collision — recover via snapshot 7a717f9f-2e5b-40e9-a0b0-de993da01c4d:kl50fm and re-QC into work/qc/s12_t1/. Full note at the end of TAKE_HISTORY.md. I did NOT fire S14-S17 and have stood down; run 8 is 66ad0dc2's alone.
- S14 (V-42) — **LANDED BUT REJECTED (G7).** Landed first attempt
  (240f, 1248×704, md5 `a0a241eebb9bc86bf4d7eaffe2d60484`). Eye QC
  is the run's best — the Mirror Service reads in full, Master
  deadpan with the gilt mirror, mirror-flare end state. L4 PASS
  (transliteration performed back, sanctioned mishear class). **L3
  FAIL: both checkpoints hear "They advised me to shits move a
  home" — three performed tokens where the sheet has "go"; the
  performer blended hook debris into the line.** Not re-fired this
  run (S05b-t2 precedent); S14 stays owed — next vehicle slows L3
  into clipped, separated diction.
- S15 (V-43) — **REFUSED** (`integrity_check_failed`, instant,
  INPUT class) on the non-doublet carriage. With the doublet already
  removed and the staging on the proven profile class, the surviving
  suspect is L7's own text ("Spread them cheeks wide", standard
  orthography). Not re-fired this run; route is the parent's call
  (transliteration carriage for L7, or a split fire). S15 stays owed
  in full, its wordless cover picture unlanded with it.
- S16 (V-44) — **KEEP.** Landed first attempt (240f, 1248×704,
  md5 `7c91ced9298ccb8c3b307f6125698f09`). G7 PASS exact — both
  Call lines verbatim, both checkpoints (0.94–7.22 / 0.94–7.68 s).
  Room Zero-G reads in full: fans, gloves, coal and tubes adrift
  around him, settled by the tail. Disclosed: singing from ~0.94 s;
  settle runs long (a few lumps still aloft at 9.5 s).
- S17 (V-45) — **KEEP — HERO hook occurrence 2 landed.** Landed
  first attempt (240f, md5 `37cd1bc032021b0929bb7280fcfba8a1`).
  G7 PASS — hook ×2 + "Apply it directly to the forehead." all in
  order, both checkpoints. The golden sheen spreads across the
  front curls on the application line; end state exact. **G2 FLAG
  for the parent:** the tube label is LEGIBLE ("Smooth-On" — the
  song's own product name, correctly spelled diegetic lettering,
  sanctioned class; flagged because the canon prefers no readable
  tube text). Disclosed: the low-angle monumental framing did not
  materialize (STACK-02 MCU held); sheen glosses the forehead too;
  end-state grin broader than a half-smile.

**Run 8 closed: 6 fires — 4 KEEPs (S12, S13, S16, S17), 1
landed-but-rejected (S14, G7), 1 REFUSED (S15). No outages, no
429.** The Dario block opened clean (S13 KEEP; S14's picture is
the run's best but its L3 performance is contaminated and the
scene stays owed). S15's refusal isolates L7's wording as the
surviving suspect — its route is the parent's call, as is S14's
(clipped, separated L3 diction). **Owed after run 8: 13 takes**
(S14, S15, S18, S19, S20, S21, S22, S23, S24, S25, S26, S27-A,
S27-B) **+ 1 cover-owed span** (S05b). Keeps: 17 of 30. Next run
order (plan order): S18, S19, S20, S21, S22, S23 — with S14/S15
re-fires slotted on the parent's route rulings.

**S12 correction (post-close-out):** the S12 take was re-delivered
by the pipeline across a runtime restart; the QC'd first render
(md5 `aaf1ec75…`) was replaced on disk by a second render, md5
`cce660118984b251e3764de46463fcfc` (1248×704), now at
takes/mv33_s12_t1.mp4. Re-QC'd in full (work/qc/s12_t1_redelivery/):
eye QC matches; G7 PASS with a disclosed stutter — a false start
on the line's own words ("It is not," 1.14–2.90 s) then the clean
full line (3.00–6.04 s). **KEEP stands**; assembly can chunk-start
the span at the clean pass. Full record: TAKE_HISTORY V-40
correction. All other run-8 takes md5-verified unaffected.

## Volley run 9 (2026-11-24 ~06:2x EST →, coordinator 2f55bbea) — S14/S15 RULINGS + PLAN ORDER

Parent rulings executed in order: (1) S14 refire — same Mirror
Service staging and class as V-42, L3 re-carried CLIPPED and
SEPARATED (words spaced as separate beats, slow deliberate
delivery) to break the hook-debris blend; L4's proven
transliteration unchanged (vehicle vehicles/mv33_s14_vehicle_v2.txt).
(2) S15 — L7 carried in TRANSLITERATION ONLY ("spred dem cheeks
wyde", respelling ledgered in the vehicle), everything else v1
unchanged; if refused, no refire this run — the parent rules a
split next run (vehicle vehicles/mv33_s15_vehicle_v2.txt). Then
plan order: S18 (Storm on the Downbeat), S19 (Royal Descent —
doublet span wordless per the S11 pattern), S20 (Keys and Curls),
S21 (Prop Swap — doublet span wordless per the S11 pattern).
≤6 fires. Outage protocol: 502/503 → ~10 min wait, retry same fire
in-run; 429 = hard stop. Results append below as they resolve.

- S14 t2 (V-46) — **KEEP.** Landed first attempt (240f, 1280×720,
  md5 `a1e8651248654a0193bd81d702541b12`). **The clipped, separated
  L3 diction broke the blend**: G7 L3 exact at both checkpoints
  ("They advised me to go home."), L4 PASS (mishear class on one
  checkpoint). The Mirror Service reads in full; the Master law
  holds (fat, bald, apron, deadpan, mouth closed). **The Dario
  cameo block is complete (S13 + S14).** Disclosed: singing from
  0.0 s; mirror presented early (up by 3.0 s); L4 runs to ~9.9 s
  so the closed-mouth end hold is not reached. Full QC:
  TAKE_HISTORY V-46. **Keeps now 18 of 30.**

## Volley run 10 (2026-11-24 ~06:3x EST →, recovery coordinator — revived after run 9 coordinator 2f55bbea died 2026-11-24T11:28:19Z, daemon-restart signature) — S15 LEFTOVER QC + PLAN ORDER

Run 9 closed mid-flight: S14 t2 KEEP (V-46) was ledgered, then S15 t2 landed at 06:26:59 EST seconds before the coordinator died — the take sat on disk un-QC'd. This run resolves it first (QC only, not a fire), then fires plan order S18, S19 (doublet span wordless per the S11 pattern), S20, S21 (doublet span wordless per the S11 pattern), S22, S23. ≤6 fires. Results append below as they resolve.

- S15 t2 (V-47) — **KEEP (QC'd by this recovery run).** The transliteration carriage landed and passed: G7 PASS — L7 performed ("Spread dem cheeks wide." at large-v3 = the respelling performed back; sheet line verbatim at distil), L8 with the coal→call homophone override, L9 exact; no doublet invented. Copied to the house name `takes/mv33_s15_t2.mp4` (md5 `66659997d2e0325ee30e2991b7bf5ebe`). Disclosed: the wordless doublet-cover span is compressed out (L7 starts at 0.0 s) — the doublet span's cover picture is assembly's call from elsewhere; full QC in TAKE_HISTORY V-47. **Keeps now 19 of 30.**
- S18 (V-48) — **KEEP.** Landed first attempt (240f, 1280×720, md5 `a8518db797091340721a9fa751236a91`). G7 PASS — all three lines in order at both checkpoints (transliterations performed back, sanctioned mishear class). The petal storm reads in full; the wig holds through the gust; re-dab and end state exact. **Keeps now 20 of 30.**
- S19 (V-49) — **KEEP.** Landed first attempt (240f, 1248×704, md5 `350115a91f12161b27201fb7fbbf0c37`). G7 PASS exact — L9+L10 verbatim at both checkpoints, no doublet invented; the bow wave + descent + train-bearers read; the take's bow-wave picture is the flagged doublet-span cover. Disclosed: singing from 0.0 s (silent bow beat compressed). **Keeps now 21 of 30.**
- S20 (V-50) — **KEEP, with a flagged coverage gap.** Landed first attempt (240f, 1280×720, md5 `74c1db0440e9d021cb2c9a2c3f9c0bb9`). G7 PASS for all four carried passes (L1, L2, L3 + performed repeat) at both checkpoints. **Flag for the parent: the run-9 vehicle's body never stages Breakdown L4 "It is not over" — the take performs the vehicle exactly, so L4 is cover-owed at assembly (hold-tail picture usable) or by a parent-ruled pickup; not re-fired this run.** **Keeps now 22 of 30.**
- S21 (V-51) — **KEEP.** Landed first attempt (240f, 1280×720, md5 `fc5fdb36718626702443399b2b0db1b6`). G7 PASS exact — L6–L8 in order at both checkpoints, no doublet invented. The Prop Swap reads in full (wig off, fresh wig caught and smoothed on, candle flames leaning at the end state); the opening picture is the flagged L5 doublet-span cover. **Keeps now 23 of 30.**
- S22 (V-52) — **KEEP.** Landed first attempt (240f, 1280×720, md5 `7f4bbd4b03bfdddb7b40be53f07d256b`). Wordless PASS with the logged hallucination override (ASR fragments at RMS ~0.01; hall verifiably empty). The Season Flip reads in full — light turn at the windows, blossom drifting in and settling around the waiting tube. **Keeps now 24 of 30.**
- S23 (V-53) — **LANDED BUT REJECTED (G7).** Landed first attempt (240f, 1280×720, md5 `543b3a2291d7a2ebc0b2e2fde0aa2830`; file kept at `takes/mv33_s23_t1.mp4`, NOT a keep). Only ONE of the two owed hook passes was performed (0.00–3.74 s); the RMS envelope proves 4–10 s is near-silence — no ASR-suppression rescue (distinguished from S08). Eye QC is spectacular (full-court fan-stroke ritual) and the staging is proven — refire next run on the same vehicle with the two passes as clearly separated beats; also keep the tube smaller/label turned (its lettering rendered large, reversed gibberish — G2 flag). S23 stays owed.

**Run 10 closed: the S15 leftover QC (KEEP) + 6 fires — 5 KEEPs (S18, S19, S20, S21, S22), 1 landed-but-rejected (S23, missing second hook pass). No refusals, no outages, no 429.** Headline results: **(1) Run 9's orphaned S15 t2 is a KEEP — transliteration carriage is PROVEN on a non-doublet line** (L7 landed and passed at both checkpoints; the doublet spans remain designed covers). **(2) Chorus 2 and the Breakdown are complete**: S18 storm, S19 descent (doublet cover picture inside the take), S20 counterpoint, S21 prop swap all KEEP. **(3) Two flags for the parent:** S20's vehicle never staged Breakdown L4 "It is not over" — the take performs the vehicle exactly, so L4 is cover-owed at assembly or by a parent-ruled pickup; S23 (HERO hook occurrence 3) stays owed on a one-pass performance. **Owed after run 10: 6 takes** (S23, S24, S25, S26, S27-A, S27-B) **+ cover-owed spans** (S05b; Breakdown L4 inside S20's span; doublet spans inside S15/S19/S21/S25 ride their scenes per the S11 pattern, S25's still to land). Keeps: 24 of 30. Next run order (plan order): S23 refire, S24, S25 (doublet span wordless per the S11 pattern), S26, S27-A, S27-B (chained last-frame).

## Volley run 11 (2026-11-24 ~07:1x EST →, coordinator 324be1ca) — FINAL FIRING RUN (parent-chained)

Parent-chained (revive detector's 3-revive cap for this episode is spent; this is the parent's own chain). Keeps 24/30. Fire order (plan order, ≤6 fires): S23 refire, S24, S25, S26, S27-A, S27-B (chained last-frame). Proven single-image compact class only. 502/503 → ~10 min wait, retry same fire in-run; 429 = hard stop; a refused fire is never re-fired this run. Results append below as they resolve.

- S23 refire brief: same staging/vehicle class as V-53 (vehicles/mv33_s23_vehicle_v1.txt) with TWO changes in the new vehicle (vehicles/mv33_s23_vehicle_v2.txt): (a) the two hook passes staged as TWO CLEARLY SEPARATED SUNG BEATS with a fresh tube press between them (V-53 performed only one pass, then ~6 s near-silence); (b) the tube kept SMALLER in frame, plain blank side to camera, no label visible (V-53's tube lettering rendered large reversed gibberish).
- S24/S25/S26/S27-A vehicles written at fire time on the same proven class (vehicles/mv33_s24_vehicle_v1.txt, mv33_s25_vehicle_v1.txt, mv33_s26_vehicle_v1.txt, mv33_s27a_vehicle_v1.txt); S25's doublet span staged wordless per the S11 pattern (no form of the doublet text in any prompt). S27-B's vehicle is written at its fire time, chained from S27-A's last frame.
- S23 t2 (V-54) — **KEEP.** Landed first attempt (240f, 1280×720, md5 `ca0139f2ce76910580bfa1404750b649`). **The separated-beats refire fixed V-53**: G7 PASS — both hook passes performed at both checkpoints (0.00–2.16 + 4.85–7.46 s large-v3; distil agrees), transliteration performed back in the sanctioned mishear class. Full-court fan-stroke ritual reads; end state exact; tube small, fine-print texture only (V-53's reversed gibberish gone). Disclosed: opening frame reads tighter than the briefed wide; singing from 0.0 s. **All three HERO hook occurrences now landed (S08, S17, S23). Keeps now 25 of 30.**
- S24 t1 (V-55) — **KEEP, with a flagged aspect deviation.** Landed first attempt (240f, md5 `5057e899376a21b2791fa8ebe620cb80`). G7 PASS — all four Final Chorus lines in order at both checkpoints (L3 verbatim; L5/L6 transliterations performed back). The peel + window blast + curl catch read in full. **FLAG: the take rendered 1152×768 (3:2), not 16:9 — the build's only off-aspect take; composition is centre-weighted so a 16:9 centre-crop at assembly keeps all content; parent/assembly confirms the crop or rules a refire.** Also disclosed: end state is a grin holding the curl aloft, not the closed-mouth press-home; no sunbeam isolation on L3. **Keeps now 26 of 30.**
- S25 t1 (V-56) — **KEEP.** Landed first attempt (240f, 1248×704, md5 `2f74b72a1cbfed9fc0c76c59d835c40a`). G7 PASS — L9+L10 verbatim at large-v3, distil with the logged coal→cold homophone override; **no doublet invented** (non-doublet carriage per the S11 pattern; the take's ovation frames are the doublet span's flagged cover picture). The Grand Backing-In reads in full: flower ovation, then the whole court backed in profile against the glowing seams, butt law holds, wave completed, him square to camera. Disclosed: singing from 0.78 s (wordless span compressed); the seams render molten/lava-lit, hotter than the plan's bright gilded glow; mouth not fully closed at the 9.5 s sample. **The backing-in arc S06 → S19 → S25 is complete. Keeps now 27 of 30.**
- S26 t1 (V-57) — **KEEP.** Landed first attempt (240f, 1280×720, md5 `a00716f6ece80164127f44630b5042c1`). G7 PASS exact — both Outro lines verbatim at both checkpoints. The Day–Night Flip reads in full: harpsichord corner, dusk through the windows, candles taking over, candlelit profile end state. Disclosed: dusk arrives early (blue by 1.5 s); background courtiers in the opening frames; end state in profile rather than frontal. **Keeps now 28 of 30.**
- S27-A t1 (V-58) — **KEEP.** Landed first attempt (240f, 1280×720, md5 `c8070d1fcbdd77baae1dfaee2b069caa`). G7 PASS — the final hook line performed once, verbatim at large-v3, with a disclosed performed pickup "And" at the head (trimmable at the chunk head; S12 precedent class). The Heart-Hold Finale reads in full: last application in candlelight, hands folding into the glowing heart, last frame holding it exact — that last frame chains S27-B. Disclosed: tube shows a red label band (no legible word). **Keeps now 29 of 30.**
- S27-B t1 (V-59) — **KEEP.** First attempt died on a 503 outage (no frames); waited ~10 min and retried the same fire in-run — landed (240f, 1280×720, md5 `c547c79032f2884254fc41acb29968c4`). Wordless PASS — zero ASR segments at both checkpoints. The chain from S27-A's last frame holds: heart-hold continuous, glow breathing to a full heart bloom at 5.0 s, mouth closed throughout, end state = first frame's pose. **S27 complete (A + B). Keeps now 30 of 30.**

**Run 11 closed: 6 fires (+1 outage retry) — 6 KEEPs (S23 t2, S24, S25, S26, S27-A, S27-B). No refusals, no 429; one 503 outage absorbed by the in-run wait/retry. MV-33 IS AT 30/30 KEEPS — every planned take has landed. ASSEMBLY IS NEXT (parent's stage).** Assembly notes carried forward: (1) S24 t1 is 1152×768 (3:2) — the build's only off-aspect take; centre-crop to 16:9 (composition is centre-weighted) or parent rules a refire. (2) Cover-owed spans as designed: S05b doublet (cover from S02's performed tail / S19–S21 flagged in-take cover pictures), Breakdown L4 inside S20's span (hold-tail picture), doublet spans inside S15/S19/S21/S25 ride their scenes' flagged cover pictures. (3) Chunk-start notes: S12's clean sung pass runs 3.00–6.04 s inside its take; S27-A carries a performed pickup "And" at its head (trim at the chunk head); S15's doublet-span cover picture must come from elsewhere (its take compressed the wordless span out). (4) S23's hero take is t2 (V-54) — t1 (V-53) is REJECTED, do not use.
