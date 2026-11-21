# TAKE HISTORY — ONE SHORT, E2 "Twenty-Four Chairs"

Video budget: 14 calls authorized (6 first-pass + 8 QC refires).
Spent: U1 ×2. Remaining after U1 lock: 10.
Routes per REFERENCE_STACK.md: U1 fresh two-image (PEAK-U1 + Clerk
sheet 16:9) → U2/U3/U4 resume chain (J7 max) → U5 re-anchor fresh
(PEAK-U5 + Clerk sheet 16:9) → U6 resume. ASR: faster-whisper
large-v3-turbo int8, local cache, NO VAD, word timestamps.

## U1_t1 — REJECTED (kept on disk as alternate)
- Snapshot f7ededf1-fa31-4993-afee-40bcdbb607a3:rrcufq · 1248×704,
  24fps, 10.000s.
- Dialogue (ASR): "Certified 24 chairs, hall pays by the chair."
  @3.20–7.52 — one word wrong ("Certified" for "Certify") AND the
  onset at 3.20s misses the scripted ~0.5s (the BLAM A1 driver).
- Picture: frame 0 is a near-replica of PEAK-U1 (crash mid-impact,
  umbrella on the shelf ✓). But the take pushes in and re-stages:
  by 2.5s Hale is behind the counter in a BLUE PINSTRIPE suit with
  a red tie; at 5.0s the CHAMPION enters unscripted (red-striped
  tracksuit, foam paddle on a stick) — a first-second-law breach
  (he enters at U2's tail, never in U1). Clerk's cobalt reads as
  full blue gloves (E1 saturation drift class).
- BLAM (raw segment): A1 FAIL t50 0.9 / t90 2.7; A2/A3/V1/V2 PASS;
  A4 PASS raw (0 vs 0). Rejected on dialogue + unscripted entrance.

## U1_t2 — KEEP
- Snapshot 85edf3f6-c8bf-4685-8cf6-cbaa0000b818:jn21aj · 1248×704,
  24fps, 10.000s. Refire changes: Hale's line moved to the HEAD of
  the action text ("already shouting… from the very first frame");
  Hale specified "plain dark suit, no tie"; "NO other people are
  in the room" added (Champion lockout).
- Dialogue (ASR): "Certify 24 chairs. Hall pays by the chair."
  @0.00–3.96 — VERBATIM (numbers as digits, E1 hand-check
  precedent), onset 0.00s = the scripted in-flight demand.
- Picture: frame 0 near-replica of PEAK-U1 (door mid-slam, trolley
  tipping, chair mid-fall, umbrella on the right shelf ✓, board
  blank ✓). Tail settles to the scripted joint frame family:
  trolley left, Hale standing at the counter with clipboard,
  envelope flat on the counter, Clerk at her book, Counter
  floor-left head-down over the chairs. NO Champion ✓. Hale in a
  plain dark suit, no tie ✓.
- Nits: the camera pushes in across the take (counter-wide → closer
  two-shot family; the office, wardrobe and light stay continuous);
  the Clerk's cobalt again reads as blue gloves at the tail (E1
  saturation drift class, disclosed); a green banker's lamp sits on
  the back desk (E1's recurring chain dressing).
- BLAM (raw segment): A1 t50 1.5 / t90 2.7 (FAIL — see GATE_LOG:
  the A1 statistic is diluted by the take's quiet tail; speech
  onset 0.00s and accent −11.3 dBFS in the first 0.5s carry the
  design intent; master-level A1 re-measured after assembly);
  A2 PASS (0.0s); A3 PASS (accent rule); A4 raw FAIL 137 vs 1 —
  the scripted slam stack itself; E1 precedent: the master
  limiter pass tamed the same class below threshold (E1 raw 31 vs
  2 → master 0 vs 0); master-level A4 is the operative reading.
  V1 PASS 1.19; V2 PASS.

## U2_t1 — KEEP (fresh route; resume API rejected, see GATE_LOG)
- Snapshot 49f36417-f1f3-4a0d-a80f-d9660ce9fc0c:9hl121.
- Dialogue 3/3 verbatim: Clerk @0.65, Counter @3.95 (split
  rendering of the em-dash pause, full line present), Champion
  @6.14+7.44 (the claim split into two utterances; both halves
  verbatim).
- Picture: frame 0 near-replica of PEAK-U2 (Champion already at the
  pile in frame 0 — entrance staged early, disclosed); rows of six
  read; GAP 1: the slide-back IS staged at the tail (Hale grinning
  at the window, Counter bent over the next chair, the Champion's
  blue-inked fingertips visible on the wobbly chair at the pile).
  Hale grins through the tail (deadpan-law nit, disclosed).

## U3_t1 — KEEP
- Snapshot 7d18327f-0e57-4d8d-bc56-c7da69e7a3c6:iz7d1p.
- Dialogue verbatim: "6, 12, 18." @2.92, "Wobbly again." @5.56,
  Clerk "He needs 24 paid, Hale." @7.36.
- Picture: the X's render from frame 0 (chairs pre-marked — the
  PEAK-U3 panel's dressing propagated; disclosed: the U3 chalking
  beat reads as already-done, U4's marking round still plays in
  full); the Champion's paddle rides as a flat visor (disclosed);
  tail re-stages to a close two-shot at the counter — the readable
  "CLERK" nameplate on the counter front is generator-rendered
  text (disclosed; furniture dressing class, E1 "MR HALL" bottle
  precedent); the Clerk chalks a small X in her book at the tail.

## U4_t1 — KEEP
- Snapshot 4c7107c8-cfe8-4b87-93a5-07fca96a272c:g8is59.
- Dialogue 3/3 verbatim: teach @0.00 to lens; question @4.24
  ("What do you get?" — "you" for "'d you", homophone class);
  cost line @7.50.
- Picture: PEAK — the Counter holds the wobbly chair high bearing
  TWO big chalk X's, fully legible (the episode's proof object
  lands); Hale lunges with the envelope mid-frame; the Clerk at
  her book. Nits: a stray chalk X sits on the manila envelope at
  2.5s (prop-dressing class); the foam X is not separately visible
  in the sampled frames (the U5/U6 foam X renders clearly).

## U5_t1 — KEEP
- Snapshot 82b0e3b4-60a5-4ba6-baee-6e8bb86a2027:meddmv.
- Dialogue 4/4 verbatim: accusation @0.00; direct address @2.14;
  Hale @5.02; verdict @7.38 (the board settle flip is keyed to the
  verdict onset, master 47.58).
- Picture: the two-X chair held centre; the foam bears ONE blue
  chalk X (cobalt-tinted chalk, disclosed); the Clerk stamps;
  tail: she writes the shortfall in the book (illegible handwriting
  texture, book-dressing class), the kept chair visible behind her
  with its two X's.

## U6_t1 — KEEP
- Snapshot 51b58b55-49c4-4fbb-990a-f34956383370:6iq1nm.
- Dialogue 3/3 verbatim: Hale signs @0.48; hanger question @3.40
  (both halves); office count @7.22.
- Picture: the shelf state is EXACT — one black umbrella handle-up
  + the folded wobbly chair with two X's on the seat panel (a third
  X rides the chair's top rail); the final freeze holds on the
  shelf (umbrella + folded two-X chair, no people). The office
  count's "fourth" beat: the Champion exits in profile at U6's
  head with the foam 4 ALREADY rendered on the foam's back face —
  generator-rendered digit, legible, facing away (disclosed in
  GATE_LOG; the no-decals fallback was unnecessary). Extra X's on
  the outgoing trolley chairs + the door glass (marking-round
  dressing). The Counter wears a chalk X on his scalp in U6
  (panel artifact propagated; disclosed).

## ASSEMBLY NOTE — wrong-take catch (see GATE_LOG for full record)
The first conform inherited E1's implicit U{n}_t1 take map and
joined the REJECTED U1_t1. The full-master ASR caught it (line at
3.38s). conform_join.py now carries an explicit TAKES map
(U1→U1_t2); the join was rebuilt and re-verified (seg_U1 ASR:
line @0.00). The wrong master was deleted before any delivery.
