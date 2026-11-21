# MV-18 "What's a Sigma? ~Mom" — GATE LOG (final, 2026-11-14)

## House master
- Path: `masters/mv18_whats_a_sigma_mom_16x9.mp4`
- **md5: 5e191983f10265d8606e2bf0c79023ee** — 88,456,689 B
- ffprobe: h264 1280×720 @ 24fps, **3782 frames**, duration **157.610s**
  (track 157.600s), AAC 48k stereo, **faststart: yes** (moov before
  mdat), **x264 SEI crf=18.0** (verified by direct annexb extract of
  frame 0; gates18.py's frame-10 SEI probe missed it — same miss as
  MV-17's gates.py, same direct-extract verification).
- Assembly: SINGLE pass. Segments (3782f total, work/segments/
  conform_log.json) concatted to work/joined.mp4 and **probed at
  3782f BEFORE the master encode** (MV-17 lesson); one uninterrupted
  encode, kinetic ASS + texture pass. No superseded master exists.

## Chat copy
- Path: `masters/mv18_whats_a_sigma_mom_16x9_chat.mp4`
- **md5: bb0493380bba9f15ef3fb4fdb3f5ecae** — 45,241,138 B (≤50 MB),
  3782f, AAC copied from the house master, video capped 2100k/2300k.

## Gates (measured)
- **Master-audio agreement** (master AAC vs track.mp3, PCM corr):
  global **0.99867**, worst-10s window **0.99800** (at 140s) — the
  master audio IS the Suno track (AAC encode, never MP3-in-MP4).
- **Zero-still enumeration** (pre-grain master, 96×54 gray, near-dup
  = mean abs diff < 1.0): **worst run 0f — PASS** (bar: no run ≥24f
  anywhere). Every shipped span — including the S26 corpse-pose
  insert span, the S28 bridge, and the S35 push-in confession — is
  clear of the bar at master level.
- **G7 wrong-lyric gate**: every shipped sung take ≥0.909 screened
  word-set overlap vs its scene-plan words; all others 1.0. The two
  sub-1.0 scores (S24 0.92, S30 t2 0.909) are the ASR "mum" for "mom"
  homophone-class spelling with all other words exact. Wordless
  inserts pass on screened-empty ASR (S02, S04i, S14i*, S26i t2,
  S33i). *S14i carries the logged hand-check override (hallucinated
  "Thank you." at segment avg_logprob −0.951; full-res frames show
  both mouths closed; MV-14 S14 precedent) — see TAKE_HISTORY.md.
- **Frame/motion gates**: per-take verdicts in TAKE_HISTORY.md;
  master-level zero-still PASS above is the backstop.

## Disclosures
1. **Montage covers — FIVE spans (S04, S14, S22, S26, S33).** The
   sung vehicles carrying these lines were REFUSED by the generator
   and were NOT retried in altered form. The spans ship as wordless
   inserts/covers — S04i facepalm, S14i freeze, S26i corpse pose,
   S33i sympathy sandwich — and S22 as a two-fragment montage cover
   cut from mouth-closed material (S31 t1's post-line door-reveal
   span + S28 t1's closed-mouth span; neither fragment's sung span
   is reused). The performed vocal + kinetic captions carry those
   lines (L03, L15, L26–L28, L32, L42).
2. **Warp extremes.** Speedups: S19 phrase 1 **1.920×** and S28
   **1.944×** — both marginally above MV-17's shipped 1.904×
   precedent, disclosed (S19's is on a 0.94s phrase; S28 is a uniform
   warp of the two bridge asks that holds both ask onsets within
   0.05s of the grid — it supersedes the phrase-level 1.48×/2.00×
   split noted in the take ledger). Also S06 1.817×, S08 t2 1.800×,
   S29 phrase 1 1.783× (all inside the build's earlier disclosures).
   Slowdowns: slowest is S03's phrase at **0.619×** (floor 0.5×
   never breached), S22 cover fragment 0.670×, S30 0.760×.
   Micro-gap compressions on closed-mouth dead air only: S16
   inter-ask gap 6.08× over 3 frames; S13 inter-ask gap 2.28× over
   4 frames — no sung content is warped at those factors.
3. **S25 sync compromise.** MOM's resurface ask was performed at
   ~2.5s against the song's 1.00s line (L31). Conformed as a uniform
   0.857× stretch across the full 2.90s slot: the "What's" onset is
   exact and her mouth is closed by the slot's end, but the ask's
   tail lands late inside its own slot. No competing vocal follows
   until L32 (a wordless-cover span).
4. **S17 flag (shipped).** Take-ASR hears only ONE of the two
   "I regret it" lines — the repeat is sung through the breaking
   grin (G7 set-overlap 1.0). The take ships at ~1.0× as its
   designed deadpan→grin-crack arc across both lines.
5. **S03 flag (shipped).** The background SON reads younger than
   the locked casting (small in frame).
6. **Incomplete-take resolutions.** S19 t1 sang phrase 1 only →
   S19 t2 sings both phrases (KEEP). S28 t1 sang the ask once →
   S28 t2 sings both asks (KEEP). S30 t1 failed the MOTION LAW
   (51f near-dup head + no standing dance) → S30 t2 dances and is
   in motion from frame 0 (KEEP). S26i t1 failed G2 (printed floor
   pages) → S26i t2's pages are blank (KEEP). All superseded takes
   remain on disk as SPARE/REJECT rows in TAKE_HISTORY.md.
7. **Singer staging.** The song has a single performed vocal; the
   scene plan stages the sigma questions on MOM (S03, S13, S16,
   S25, S28, S36) and the AUNT (S32) as dialogue — MOM/AUNT sing
   the sigma lines over that single performed vocal.
8. **S29 flag (shipped).** SON's hand covers his mouth from the
   start of phrase 2 rather than only on the final word "talking";
   both phrases are complete (G7 1.0) and the payoff hold lands.
9. **S35 notes (shipped).** The generator returned a medium shot,
   not the planned 85mm ECU, and the quiet locked-off take failed
   the native frame gate (56f near-dup run). Conform applies the
   MV-17-precedent slow push-in (also tightening toward the ECU
   intent); master zero-still PASS verifies the shipped span.
10. **3:2 returns.** S32 and S33i were returned at 1152×768 (3:2)
    despite the 16:9 request; both are centre-cropped to 16:9 at
    conform (subjects centred; verified safe in QC).
11. **Partial events (shipped, from take QC).** S08 t2: the literal
    heel-first backpedal + shelf bump land only partially. S15:
    SON reads couch-edge seated, not floor-seated (staging variant).
    S10: the warm→cool grade shift across the pose chain is stronger
    than planned; reads as the pre-chorus tension beat.
12. **Coordination incident (resolved, no output impact).** During
    the double recovery, a duplicate S19 t2 fire briefly overwrote
    the canonical take file; it was restored from the surviving
    generation source and its md5 re-verified against the ledger
    (6a2184961e5b4bde32cfde079e0c01d2) before conform. Record in
    takes/mv18_s19_t2.json.

Build history: intake + Volleys 1–3 by coordinator 9d3ec1bc
(2026-11-13); parked on the 429 daily budget; resumed 2026-11-14 —
Volley 4 + 5 fires by 34ec7846 (died mid-QC), Volley 5 QC + Volley 6
partial by 8b4a7b96, rerolls + Volley 6 completion + conform +
assembly by 61cca0f2. Tempo measured 156.25 BPM; performed grid
46 lines; photoreal live-action lock; distinct event per slot.
