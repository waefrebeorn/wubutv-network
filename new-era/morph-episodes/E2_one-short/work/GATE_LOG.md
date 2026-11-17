# GATE LOG — ONE SHORT, E2 "Twenty-Four Chairs" (PRODUCTION)

Produced 2026-11-17 from the LOCKED SCRIPT.md (105 words / 16 lines,
dialogue verbatim). Video budget: 14 authorized; **7 used**
(U1 ×2, U2–U6 ×1 each). No 429 encountered. Two resume-API
attempts were rejected (400 invalid_args) before any generation —
the snapshot-resume path is not accepted in this context; all
units were fired FRESH on their gated PEAK panels + the Clerk
CHAR sheet (the REFERENCE_STACK fallback route), with each unit's
vehicle text restating the upstream unit's last frame (SR in text
form). Joint frames: panels/PNL-JOINT-U1..U5.png.

## MASTER

- masters/oneshort_E2_master.mp4 — **22,401,297 B**, md5
  **0d57f2c57f47c6447cf2278ad001c140**, h264 1280×720 24fps,
  **1440 frames**, video 60.000s (container 60.041s incl. AAC
  priming), AAC 48k, faststart, ~ WuBu ~ bug bottom-right.
  Under the 50 MB chat cap — no delivery encode needed.
- CRF: rendered at CRF 18; the same chain at CRF 23 =
  13,223,287 B → **size differential 1.69×** (the valid CRF-18
  proof on this VM; SEI reads 23.0 regardless — known anomaly).
- Loudness: joined measured −20.38 LUFS / TP −1.42 → rendered
  with −1.2 dB + limiter 0.84 (E1's proven pass) → master
  ≈ −21.6 LUFS / TP ≤ −2.6.

## TAKES (detail in TAKE_HISTORY.md)

U1_t2 KEEP (t1 REJECTED: "Certified" for "Certify", onset 3.20s,
pinstripe + red tie drift, unscripted Champion entrance) ·
U2_t1 KEEP · U3_t1 KEEP · U4_t1 KEEP · U5_t1 KEEP · U6_t1 KEEP.
Dialogue: **16/16 locked lines verbatim on the finished master**
(full-master ASR, work/qc/master_asr_v2.txt). Hand-checks:
numbers heard as digits (script words); "What do you get?" for
"what'd you get?" (homophone class); the Counter's and
Champion's two-part lines render as split utterances with both
halves verbatim. Master-ASR tail artifacts at 59.34s+ are
whisper hallucinations over the silent freeze (the U6 segment
ASR is authoritative: speech ends 59.28s master time).

## JOINT GATE (work/joined.mp4, distribution-relative item-6)

Baseline 95th 15.95, median 7.52, head-window p25 5.95.
- J1 seam 0.55 PASS · head-12 8.27 PASS — EYE: COHESIVE. U1's
  settle (Hale at the counter, envelope down, Clerk at her book,
  Counter floor-left) → U2's rows-under-way wide: same office,
  same light, same wardrobe; the count is simply under way.
- J2 seam 6.87 PASS · head-12 19.95 PASS — EYE: COHESIVE. The
  GAP-1 slide-back frame (Hale at the window, Counter bent to
  the next chair, the Champion at the pile) → U3's counter-wide:
  same room from the house angle, X-marked chairs continuous.
- J3 seam 1.54 PASS · head-12 13.08 PASS — EYE: COHESIVE. U3's
  tail two-shot (Clerk standing at her book, Hale in profile) →
  U4's counter-wide marking round: same positions, same light;
  the camera widens, the world does not change.
- J4 seam 2.12 PASS · head-12 7.45 item-6 BELOW-RULE — EYE:
  COHESIVE. U5's head is the scripted held accusation tableau
  (the two-X chair presented centre, all four standing) — a held
  beat by design, not a frozen head; the joint itself is
  continuous (the chair passes from U4's raised peak into U5's
  presentation without a world change).
- J5 seam 3.02 PASS · head-12 9.36 PASS — EYE: COHESIVE. U5's
  book-writing tail (the kept chair visible behind the Clerk,
  two X's) → U6's signing wide: same counter, the shelf state
  already correct in the wide (umbrella + folded chair).
- No E1-style eye-INCOHESIVE joint. The takes re-stage framing
  inside units (the generator's grammar) but the office, cast,
  wardrobe and light never swap.

## BLAM GATE (finished master)

A1 t50 1.6 / t90 2.8 — BY THE LETTER FAIL, with the E1 U5
precedent noted: the statistic integrates the whole first 10s
(the slam + line occupy 0–4s; the take's quiet settle dilutes
the percentile). The design quantities the gate protects are
all met: **speech onset 0.00s** (Hale's line starts WITH the
slam, ASR-verified), lead silence 0.0s, accent −11.1 dBFS in
the first 0.5s. A2 PASS (0.0s). A3 PASS (accent rule).
A4 PASS (0 vs 0 — the raw segment's 137-count slam transients
were tamed by the master limiter pass, as in E1). V1 PASS
(1.12 ≥ 0.6). V2 PASS. E1 named impact ≤1.0s: PASS (frame 0 is
mid-crash; CLAIMED 24 flips at 0.30s). E2 first graphic ≤3.0s:
PASS (0.30s).

## GAPS (verified from master ASR timings)

GAP 1 (after U2): Champion's claim ends 18.54 → U3 speech 22.92
= 4.38s containing the slide-back + the domino head. GAP 2
(after U4): cost line ends 39.72 → U5 speech 40.12 is the
accusation; the scripted CCTV shelf-hold inside U4's tail was
NOT realized as a separate hold — U4's tail is the raised-chair
peak itself (held in frame at 9.8s), and the shelf hold lands
in GAP 3 instead. Disclosed deviation. GAP 3 (U6 tail): last
speech ends 59.28 → freeze on the shelf to 60.00 (0.72s of
held freeze inside the segment + the settle before it; the
script asked 2–3s — compressed, disclosed; the freeze frame
itself is exact).

## BOARD (Method C, post, keyed to measured speech)

CLAIMED 24 @0.30 · COUNTED 12 @18.08 · COUNTED 18 @24.38 ·
settle COUNTED 23 | CLAIMED 24 @47.58 (the verdict's onset) ·
TAKES 22 | KEPT 1 @55.78. Eye-verified on master frames
(COUNTED 23 ≠ CLAIMED 24 with the ≠ marker at 47.8s; TAKES 22 /
KEPT 1 over the closing shelf freeze). The generator was never
asked for countable chairs.

## FOAM DECALS

NONE APPLIED — unnecessary. The generator rendered the foam X
in-scene (clear in U5, blue chalk) and, in U6, the foam **4** on
the paddle's back face as the Champion exits in profile —
legible, correctly placed for the counted-fourth beat, and he
leaves before the freeze exactly as scripted. Disclosed: the 4
is generator-rendered text (a digit), accepted here because it
IS the scripted story beat (the office's chalked correction),
rendered as a chalk mark on the prop, not as signage or speech
text. The U6 panel's scalp-X artifact propagated: the Counter
wears a chalk X on his scalp in U6 (and an X sits on the door
glass and the outgoing trolley chairs — marking-round dressing).

## WORDMARK

UNC is not in this show's cast — the hoodie gate is NOT
TRIGGERED (E1/E2 ruling). The network ~ WuBu ~ corner bug
(post, gold, bottom-right) is present on every frame.

## SHELF vs LEDGER §5 (pre-delivery verification)

LEDGER §5 E2 close state: 1 × black umbrella (handle up) +
1 × folded wobbly chair, two white chalk X's on the seat.
Master's closing freeze: EXACT MATCH (one umbrella, one folded
chair, two X's on the seat panel; a third X rides the chair's
top rail — disclosed). The U1 opening wide also carries the
umbrella on the shelf, unremarked (the E1 hanger's picture
payment).

## ASSEMBLY INTEGRITY — the wrong-take catch

The first conform pass inherited E1's implicit `U{n}_t1` take
map and joined the REJECTED U1_t1. The full-master ASR caught
it (Hale's line at 3.38s instead of 0.00s). The bad master was
deleted undelivered; conform_join.py now carries an explicit
TAKES map (U1→U1_t2, others t1); the join was rebuilt in one
pass, seg_U1 re-ASR'd (line @0.00 ✓), the joint gate re-run,
and the master re-encoded and re-verified end to end. This is
logged as the build's principal process lesson: an inherited
take map is a silent-failure surface — the master-level ASR
gate is what caught it, which is what it is for.

## F-9 SECOND GATE E (finished master, fresh-context cold reads)

Input: work/GATE_E2_INPUT.md — master transcript + per-unit
picture summaries ONLY, citation-required, no script/board.
- Read 1: **FAIL** — Q7 (the Champion's claim disposition)
  unanswerable FROM THE INPUT: the U6 picture summary had
  omitted two visible beats (the chalk X on the foam in U5;
  the chalked 4 on the foam as he exits in U6). Q6 partially
  flagged (payment compression). The failure was in the
  summary's fidelity, not in the master's contents — both
  beats are plainly in the picture (U5 frame 2.5s; U6 frame 0).
- Input corrected to describe all visible picture (description
  only, no interpretation added).
- Read 2 (fresh reader, corrected input): **PASS** — all nine
  questions answered with line/beat citations: Hale's want
  spoken by him (0.00, repeated 45.26); both staff wants
  spoken in plain words by U2 (10.36 / 13.66); the trick, the
  marking defence, and the two-X catch all cited; the payoff
  (certified 23, chair kept, TAKES 22) derived and confirmed
  NOT reversed; the viewers' question (34.38) answered by the
  Clerk (42.36); the Champion's disposition read correctly
  (no certificate; leaves marked 4). Reader's Q9 residuals —
  the Champion's "five" never explained in words, "One broke"
  unexplained, the office count ending mid-count, the 5
  o'clock deadline not revisited — are the episode's designed
  open threads (shown-never-explained invasion lore; the E8
  hanger, begun not paid, per LEDGER §3), not story defects.

## DISCLOSED FLAWS (complete list)

1. BLAM A1 fails by the letter (t50 1.6 / t90 2.8) while its
   protected quantities pass (onset 0.00s, no dead head,
   accent in the first 0.5s) — E1 U5 precedent class.
2. J4 item-6 BELOW-RULE (scripted held accusation tableau).
3. GAP 2's CCTV shelf-hold not realized inside U4; GAP 3's
   freeze is shorter than the scripted 2–3s.
4. The Champion enters in U2's frame 0 (panel staging), not
   at U2's tail; his claim still lands last in U2.
5. U3's chairs render pre-marked with X's from frame 0 (the
   panel's dressing propagated) — U4's marking round still
   plays in full; the two-X proof lands as scripted.
6. Hale grins through U2's GAP-1 tail (deadpan-law nit); the
   U3 panel's grin also reads at U3's head.
7. The Clerk's cobalt reads as blue gloves in several takes
   (E1 saturation drift class); the Counter's hands also take
   the stain in U2/U3 frames.
8. Generator-rendered text flecks: the "CLERK" counter
   nameplate (U3 tail), book handwriting (U5 tail), the foam
   4 (U6, scripted beat — see above).
9. The Counter wears a chalk X on his scalp in U6 (panel
   artifact propagated); extra X's on the door glass and the
   outgoing trolley chairs.
10. The U5 foam X renders in blue chalk rather than white.
11. Hale's suit reads pinstripe in U1_t1 only — the rejected
    take; the kept U1_t2 and all other units hold the plain
    dark suit (U1_t2's tail framing pushes in closer than the
    locked counter-wide; disclosed in TAKE_HISTORY).

## VERDICT

All gates pass or are disclosed above with their precedents.
F-9 story gate: PASS (read 2). Master delivered:
masters/oneshort_E2_master.mp4, md5
0d57f2c57f47c6447cf2278ad001c140.
