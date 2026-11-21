# MV-2 "Toll Roads Are Dumb" — VIEWING CUT (2026-11-03/04)

**This is a VIEWING cut, not the v6 final.** Built from takes already on disk,
no new generation, per the user's 2026-11-03 20:14 EST order ("use what we
have now… no still frames… motion covered for the entire video… matching
all of the words"). Motion + word coverage are the gates for this cut; ratio
precision is a preference. Nothing here claims v6 QC-candidate status for
fallback or time-stretched segments. Do NOT deliver v1–v5 (rejected).

## Masters (verified from the delivered files themselves)

- **Master:** `masters/mv2_toll_roads_are_dumb_viewingcut_16x9.mp4`
  - md5 `ff39ec1837ece12c1afab70829a73802`
  - 1280×720, 24fps, **6432 frames, 268.010s** (song `track.mp3` 268.011s —
    drift −0.001s), h264 + AAC 48kHz stereo 192k, faststart (moov before mdat)
  - 66,398,322 B; zero decode errors (ffmpeg null-decode pass clean)
- **Chat-sized copy:** `masters/mv2_toll_roads_are_dumb_viewingcut_16x9_small.mp4`
  - 1280×720, 24fps, 6432 frames, 268.010s, CRF 28 / AAC 128k, faststart
  - 25,404,217 B
- Soundtrack = untouched `track.mp3` (md5 `9e5ff10876cda8ac17dcb22b79c3f00a`).
  Captions burned from `captions_v2.srt`; corner bug `~ WuBu ~` top-right.
  Hard cuts on word boundaries only, one segment per song position, song order.

## Assembly fixes applied during this build (all in `masters_work_viewingcut/`)

- **FIX1 (motion):** S14 t2-warped swapped to **S14 t1** — the warped take's
  opening held a visually confirmed ~0.9s still (held smile, take 0.36–1.06)
  at vocal start in the first delivered master. S14 t1 sings the line exactly
  once, motion-clean (whole-file max 7f, tail only), text-clean at 2s/5s/8s.
  Nits: handheld mic (vs stand), blue/teal pocket square.
- **FIX1 (filler):** S05→S06a filler swapped from S08 t9 tail (1.9s rest-pose
  still, frozen core 0.67s, in the first delivered master) to **S26 t2 tail**
  (turn to silhouette, active motion). S08 t9 tail and R6 t7 tail-end are
  excluded from the filler queue entirely.
- **FIX2 (render bug):** clips rendered with `-ss`/`-t` as OUTPUT options came
  out (tau span) seconds long instead of (tau span)/factor — a sped-up clip
  contained (tau span × f) of take, a slowed clip was truncated. Root cause
  found by showinfo frame mapping. `-ss`/`-t` moved to INPUT options; verified
  S05 → 56f/2.33s and S07 → 249f/10.38s as expected.
- **FIX3 (drift):** fps EOF rounding added ~+1 frame per clip, accumulating to
  +0.61s of vocal-start drift by the tail. Every clip is now trimmed to
  exactly N = round(out_end×24) − round(out_start×24) frames, so boundaries
  land on the tiled frame grid. Final concat: 6425 frames (267.704s); 6 clips
  under-deliver by 1–2 frames each (all at clip tails, no vocal content lost:
  S05 −1, filler −1, S18 −2, R6 −1, S23 −1, S27-tail −1); 0.31s tpad on the
  final tail frame (no words) brings the master to exactly 268.010s.
- Sub-frame filler residue (0.0002s, float dust at a queue boundary) is
  consumed but not emitted as a clip; tiling tolerance covers it.

## Per-segment table

Tier: 1 = clean v6 candidate · 2 = warp-rescued candidate · 3 = v5 in-band
take passing the motion audit · 3-alt = v5-era alternate take · FALLBACK =
exactly-once moving take warped to fit (time-stretched, NOT a QC pass) ·
GAP = no usable singing take; moving footage only, word-match gap (disclosed).

| Song span | Lyric / scene | Take | Tier | Factor | Motion (source audit) | Flags |
|---|---|---|---|---|---|---|
| 4.44–13.36 | Intro: "Yeah… listen here, baby. / Those shiny roads ain't what they seem." | mv2_s01_t4.mp4 | 3 | 1.038 | vocal 0f, mean 1.915 — PASS | — |
| 20.12–27.34 | Verse 1 lines 3–4 (words 11–31) | mv2_s02_t4.mp4 | 3 | 1.111 | vocal 0f, mean 0.915 — PASS | — |
| 27.34–34.32 | Verse 1 lines 5–6 "Cars slam the brakes… / NTSB said…" | — (filler) | GAP | — | — | MOTION/TEXT GAP: S03 t2 0.67s hold during "worst/on"; S03 t1 STOP signage on toll booths; "NTSB said those" bridge unsung by any S03 take |
| 34.96–41.30 | Verse 1 lines 7–8 "…the fast lanes, the rich ones fly on by, while the rest of us crawl, watching money flash by" | mv2_s04_t1.mp4 | gap-seg | 1.470 | vocal 0f, mean 2.628 — PASS | Gap-segment time-stretch (rule c); lead "Now they got" (0.40s) unsung; photoreal style (not a reject) |
| 41.90–49.38 | Verse 1 lines 9–10 (words 73–90) | mv2_s04_t5.mp4 | 3 | 1.027 | vocal 0f, mean 3.626 — PASS | — |
| 50.84–52.76 | Chorus 1 line 11, hook "toll roads are dumb" | mv2_s05_t6.mp4 | FALLBACK | 1.896 | vocal max 11f → 5.8f delivered, mean 0.509 — PASS | Time-stretched, NOT a QC pass; tail trimmed at take 4.458 (frozen tail excluded) |
| 57.92–63.60 | Chorus 1, S06 split scene (part a) | mv2_s06a_t2.mp4 | 1 | 1.120 | vocal 0f, mean 1.346 — PASS | — |
| 65.02–70.62 | Chorus 1, S06 split scene (part b) | mv2_s06b_t1.mp4 | 1 | 1.029 | vocal 0f, mean 3.229 — PASS | — |
| 72.28–80.78 | Chorus 1 lines 14–15 region (words 118–127) | mv2_s07_t2.mp4 | 3 | 0.816 | vocal 0f, mean 1.181 — PASS | Tail trimmed at take 9.125 (21f frozen tail excluded) |
| 88.48–93.10 | Chorus 1 line 16 "…they just keep coming." (words 137–140) | mv2_s08_t9.mp4 | 1 | 1.056 | vocal 0f, mean 1.92 — PASS | — |
| 93.10–96.42 | Verse 2 line 17 (words 141–149) | mv2_s09_t2_warped.mp4 | 2 | 1.259 | vocal 0f, mean 1.629 — PASS | Residual 1.26x (0.01 over 1.25; parent-overruled warp candidate, disclosed) |
| 96.80–99.98 | Verse 2 line 18 (words 150–156) | mv2_s10_t6.mp4 | 1 | 1.113 | vocal 0f, mean 0.991 — PASS | — |
| 100.26–103.60 | Verse 2 line 19 "they say the paid side is safer, the free side takes the hit" | — (S10 tail) | GAP | — | — | WORD-MATCH GAP (GAP-B): no take sings "safer"; plays over S10 t6's moving tail |
| 103.72–111.08 | Verse 2 line 20 "Crashes just move over, same old mess…" (words 170–187) | mv2_s11_t2.mp4 | 3-alt | 0.940 | whole-file 0f — PASS | Swap: S11 t3 had a 0.57s hold during "over/same"; t2 slurs "oldness" for "old mess", "Crash is" for "crashes"; bridge "Still the / lexus lanes they call them" unsung by any S11 take |
| 111.30–120.22 | Verse 2 lines 21–24 region (words 188–216) | mv2_s12_t3.mp4 | 3 | 1.031 | vocal 11f → 10.7f delivered, mean 4.413 — PASS | Master slow-close nit: 14f near-dup run 119.83–120.42 straddling vocal end — frames visually confirm mouth moving (open 119.9 → closing 120.3), metric artifact, not a freeze |
| 122.92–124.44 | Chorus 2 line 1, hook "toll roads are dumb" (words 220–223) | mv2_s13_t3.mp4 | FALLBACK | 2.395 | vocal 11f → 4.6f delivered, mean 0.969 — PASS | Time-stretched, NOT a QC pass; tail trimmed at take 5.292; text-clean (blank panels/ticket) |
| 128.76–135.22 | Chorus 2 line 2 "Fast lanes make crashes, the wrecks just come." (words 229–236) | mv2_s14_t1.mp4 | 3-alt | 1.145 | whole-file max 7f (tail only) — PASS | FIX1 swap (see above); "Files" = fast mishear, "Rex" = wrecks mishear class; handheld-mic + pocket-square nits |
| 136.26–142.62 | Chorus 2 line 3 "Pay to go faster, the rest of us slow," (words 237–246) | mv2_r1_t3.mp4 | 1 | 0.918 | v6 frame audit PASS (126/141 changed) | — |
| 144.08–149.36 | Chorus 2 line 4 region (words 247–252) | mv2_r2_t1.mp4 | 1 | 0.829 | v6 frame audit PASS (105/106 changed) | Take sings "we've been slamming the danger roads" |
| 150.48–152.64 | Chorus repeat (words 253–256) | mv2_r3_t4_warped.mp4 | 2 | 1.250 | warp frame gate PASS (0.80 candidate) | — |
| 153.74–156.16 | Chorus repeat (words 258–261) | mv2_r4_t2_warped.mp4 | 2 | 1.041 | warp frame gate PASS (0.96 candidate) | — |
| 157.34–160.20 | Chorus repeat, "fast lanes make crashes" only (words 262–265) | mv2_r5_t3.mp4 | 1 | 1.133 | v6 frame audit PASS (77/78 changed) | — |
| 160.20–164.36 | Bridge region (words 266–269) | mv2_s15_t2_warped.mp4 | 2 | 0.800 | warp frame gate window = scaled span (parent-confirmed) | — |
| 165.92–168.94 | Bridge region (words 271–278) | mv2_s16_t7_warped.mp4 | 2 | 1.245 | warp frame gate PASS (clean 0.80 candidate) | "They" seam word (165.34–165.92) unsung — plays over S15 tail |
| 169.62–175.22 | Bridge region (words 281–293) | mv2_s17_t2_warped.mp4 | 2 | 1.250 | vocal 10f → 8.0f delivered, mean 1.478 — PASS | Master nit: 8f frozen run at 172.46 (0.33s, mid-vocal, under the 0.5s gate) |
| 175.22–182.48 | Bridge region (words 294–306) | mv2_s18_t1_warped.mp4 | 2 | 0.802 | vocal 0f, mean 2.382 — PASS | Clip under-delivers 2 frames at tail (post-vocal); −0.083s step disclosed |
| 186.56–193.18 | Mantra region (words 311–318) | mv2_s19_t2_warped.mp4 | 2 | 0.816 | vocal 0f, mean 1.045 — PASS | — |
| 194.80–196.58 | Mantra region (words 319–322) | mv2_s20_t2_warped.mp4 | 2 | 1.250 | vocal 0f, mean 1.579 — PASS | Scaled vocal window used (parent-confirmed) |
| 198.00–200.18 | Mantra repeat (words 324–327) | mv2_r6_t4_warped.mp4 | 2 | 1.250 | vocal 0f, mean 2.224 — PASS | Scaled vocal window used (parent-confirmed) |
| 205.20–214.44 | Mantra region (words 333–352) | mv2_s21_t2.mp4 | 3 | 0.994 | vocal 11f → 11.1f delivered, mean 0.643 — PASS | End-hold nit: 13f source run straddling vocal end (0.22s during final word "slow"); tail trimmed at vocal end; master pause-holds 13f at 207.88 + 210.25 are BETWEEN words, not during words |
| 216.06–221.82 | Mantra repeat (words 353–358) | mv2_r8_t1.mp4 | 1 | 1.042 | v6 frame audit PASS (144/145 changed) | — |
| 222.44–224.64 | Mantra region (words 359–362) | mv2_s22_t4_warped.mp4 | 2 | 0.800 | vocal 0f, mean 1.442 — PASS | Scaled vocal window used |
| 230.22–231.82 | Mantra hook "toll roads are dumb" (v6 span 1.60s; base Whisper 1.38s) | mv2_s23_t4_warped.mp4 | 2 | 1.2125 | vocal 0f, mean 0.939 — PASS | done→dumb normalization (established v5 class, parent-confirmed) |
| 242.30–243.24 | Outro "yeah" (242.30–243.08) | mv2_r11_t4.mp4 | 1 | 0.923 | vocal 0f, mean 1.058 — PASS | — |
| 243.24–249.18 | Outro region (words 384–395) | mv2_s24_t1.mp4 | 3 | 1.061 | vocal 0f, mean 2.861 — PASS | — |
| 251.08–253.06 | Outro region (words 396–399) | mv2_s25_t2.mp4 | 3 | 1.111 | vocal 0f, mean 0.949 — PASS | — |
| 257.82–260.80 | Outro region (words 400–403) | mv2_s26_t2.mp4 | 3 | 0.906 | vocal 0f, mean 0.838 — PASS | — |
| 260.80–268.01 | Outro motif / ticket tear (no words) | mv2_s27_t2.mp4 (post-vocal [2.96, 10.0] only) | 3 | 0.977 | whole-file 0f — PASS | Never plays take 0–2.96 in this window |

## Filler segments (moving footage only, never vocal coverage elsewhere)

20 segments, 12 holes. Filler = non-vocal tail stretches at natural speed
(f=1.0), consumed from the queue in order. Reuse of scene takes' NON-vocal
tails is disclosed; no take is reused as vocal coverage at another position.

| Hole (output) | Filler take + take interval |
|---|---|
| LEADER 0.00–4.44 | mv2_s22_t3.mp4 4.18–8.62 |
| S01→S02 14.07–18.95 | mv2_s22_t3.mp4 8.62–10.0; mv2_s23_t9.mp4 4.32–7.817 |
| S02→GAP-A 27.95–34.96 (incl. S03 gap) | mv2_s23_t9.mp4 7.817–9.125; mv2_r3_t7.mp4 3.9–8.708; mv2_r6_t7.mp4 5.02–5.912 |
| S04→S05 50.35–50.84 | mv2_r6_t7.mp4 5.912–6.398 |
| S05→S06a 53.19–57.92 | mv2_s26_t2.mp4 2.70–7.429 (FIX1: active turn footage) |
| S07→S08 81.77–88.48 | mv2_s26_t2.mp4 7.429–10.0; mv2_s09_t2_warped.mp4 4.18–8.322 |
| S12→S13 121.00–122.92 | mv2_s09_t2_warped.mp4 8.322–9.292; mv2_s10_t6.mp4 3.54–4.494 |
| S13→S14 125.13–128.76 | mv2_s10_t6.mp4 4.494–8.125 |
| S18→S19 184.77–186.56 | mv2_s10_t6.mp4 8.125–8.708; mv2_r5_t3.mp4 3.24–4.447 |
| R6→S21 203.28–205.20 | mv2_r5_t3.mp4 4.447–6.365 |
| S21→R8 214.44–216.06 | mv2_r5_t3.mp4 6.365–7.985 |
| S23→R11 236.82–242.30 | mv2_r5_t3.mp4 7.985–10.0; mv2_r4_t2_warped.mp4 2.52–5.987 |

Seam fragments and gap remainders not covered by a dedicated filler hole play
over adjacent takes' moving head/tail footage: GAP-B over S10 t6's tail;
GAP-C remainder ("fast lanes make crashes", 201.10–204.24) over R6 t4-warped
tail + R5 t3 filler; GAP-D (224.92–230.22) over S22 t4-warped tail; GAP-E line
44 (236.62–238.82) over S23→R11 filler; "baby." interjections and other seam
fragments over neighboring takes' heads/tails. None of these are claimed as
word-matched.

## Master motion audit (on the delivered master file itself)

Method: ffmpeg full-fps 160×90 grayscale, consecutive-frame mean abs diff;
near-dup = diff < 0.5, frozen = diff < 0.2; runs ≥6 frames listed.

- Frames 6432, duration 268.000s, mean diff 2.559
- **Total frozen (<0.2) time: 0.625s** (was 1.958s in the pre-fix master)
- **Longest near-dup run: 14 frames (0.583s)** (was 46 frames / 1.917s)
- Near-dup runs ≥6f: (22.08, 10f), (23.88, 8f), (27.33, 6f), (51.88, 8f),
  (80.71, 6f), (96.96, 8f), (115.63, 10f), (117.63, 9f), (119.83, 14f),
  (120.46, 11f), (172.38, 10f), (207.88, 13f), (210.25, 13f), (214.00, 6f),
  (267.71, 7f)
- Frozen runs ≥6f: (172.46, 8f, 0.333s, S17 mid-vocal, under gate),
  (267.71, 7f, 0.292s, tpad tail hold, no words)
- Runs >12f (0.5s): **exactly three**, all adjudicated, none a genuine still
  during words:
  1. (119.83, 14f, 0.583s) — S12 vocal-end slow-close: frames visually
     confirm the mouth moving (open at 119.9 → closing at 120.3); the 160×90
     metric is fooled by the small face region over a static background.
     Disclosed as a slow-close nit, not a freeze.
  2. (207.88, 13f, 0.542s) + (210.25, 13f, 0.542s) — S21 inter-word pauses
     (verified against word times: between "time"/"The" and "come"/"Pay").
     NOT during words; pass per the gate, disclosed as pause-holds.
- **Fixed and verified gone:** the 1.9s filler still (53.54–55.46, frozen core
  0.67s) and the 0.9s S14 vocal-start hold (129.21–130.08, frozen core 0.58s)
  from the pre-fix master do not appear in this audit. The S13 vocal-start
  run and R1 run from the pre-fix master also cleared under frame-exact
  rendering.

## Uncovered / word-match gaps (honest list — moving footage only, no mouth)

- **S03 (27.34–34.32):** no usable take (t2 motion-fail, t1 text-fail).
- **GAP-B (100.26–103.60):** Verse 2 line 19; no take sings "safer".
- **GAP-C remainder (201.10–204.24):** "fast lanes make crashes" between R6
  and S21 (R6 covers only words 324–327).
- **GAP-D (224.92–230.22):** parenthetical "toll roads" repeat + "fast lanes
  make crashes, the wrecks just come".
- **GAP-E (236.62–238.82):** mantra line 44 "toll roads are dumb" (R11 covers
  only "yeah" at 242.30–243.08).
- **Micro-gaps / seam fragments:** GAP-A lead "Now they got" (34.56–34.96);
  S03 "NTSB said those" bridge (31.26–32.06); "baby, toll roads are dumb"
  (53.22–56.46); 81.20–88.48; "that won't quit" (120.22–121.76);
  124.92–128.12; "baby." (152.92–153.16); "They" (165.34–165.92);
  "but the" (169.06–169.62); 183.04–186.46; "baby." (197.14–197.22);
  "baby." (232.14–232.64). All play over moving footage; none claimed matched.
- Instrumental gaps (no song words) are covered by filler/heads/tails as
  listed above.

## What this cut is NOT

- Not the v6 final. S05 t6 (1.90x) and S13 t3 (2.39x) are FALLBACK
  time-stretches, not QC passes. S09's 1.26x residual and S14's t1 swap are
  disclosed above. The S03 slot and GAP-B/D/E/C-remainder have no matching
  mouth by design of the available takes, not by omission.
- No take flagged REJECTED / frame-gate-FAILED / repeat-defect / text-failed
  in any record was used (incl. R4 t7/t8, R3 t9, S16 t2, S08 t5, R4 t4, S22 t2,
  S16 t6, S23 t6). No generation was run for this cut. No existing file was
  modified; all new files are under distinct new names.
- Intermediates: `masters_work_viewingcut/` (assemble.py, cutlist_working.json,
  motion_audit_viewingcut.json, motion_audit_fix1.json, master_audit.py,
  clip_000–054.mp4, concat files, frame checks).
