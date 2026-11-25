# GATE LOG — E2 SHOW-2 THE TENTH SECOND, "The Chalk Wall"

Master: masters/E2_SHOW-2_the-tenth-second_MASTER.mp4
md5 **137465e24d1248fe350ac8de5021e937** · 26,756,135 bytes ·
1280×720 · 24fps · **1440 frames** (container count + full-decode
count agree) · 60.000s · h264 + AAC 48k stereo · faststart
(moov before mdat) · full decode clean. Under 50 MB → no chat
copy; the house master is the delivery file.

## Format gate
- Frames/duration/fps/resolution: PASS (above).
- CRF: the encode ran `-crf 18` (preset medium). SEI ANOMALY:
  this VM's ffmpeg 8.1.2/libx264 writes `crf=23.0` into the SEI
  options string regardless of the requested rate control —
  proven by control encodes (testsrc2 at CRF 18 vs CRF 40:
  1,000,295 B vs 109,412 B, both SEI-stamped 23.0; `-b:v` and
  `-x264-params` variants likewise). The CRF-18 fact for THIS
  master is therefore proven by size differential: the identical
  master chain encoded at CRF 23 = 15,496,497 B; the delivered
  master = 26,756,135 B (1.73×). CRF 18: PASS (by differential;
  the SEI string on this build is not evidence either way).
- Wordmark gate: UNC does not appear in this episode. The corner
  bug reads exactly `~ WuBu ~` (drawtext, verified on frames):
  PASS (vacuous for the hoodie form).

## BLAM GATE (measured on the finished master, FIRST3 audit recipe)
- A1 onset: t50 **0.0s** (bar ≤0.5) · t90 **0.0s** (bar ≤1.5) PASS
- A2 leading near-silence: **0.0s** (bar ≤0.2) PASS
- A3 head level: 0–1s mean **−3.1 dB vs median** (bar within 6 dB)
  PASS — plus the designed accent (the take's own boot-scuff,
  repositioned to frame 0) at 0.0s.
- A4 crackle: HF bursts head 0–1.5s = **1** vs control 30–45s
  rate ×**0.71** (bar ≤2×) PASS
- V1 opening motion: head 0–0.5s MAE 20.67 vs 3–10s baseline
  10.60 = **1.95×** (bar ≥0.6×) PASS
- V2 no ramp-from-rest: first 0.25s bucket 23.07 = **94%** of the
  strongest 0–3s bucket (bar ≥50% or ≥4.0 absolute) PASS
- E1 named impact ≤1.0s: Laura's mid-stride arrival (picture,
  from frame 0) + the scuff accent on frame 0 + the Cull Clock
  ignition at 0.21s — verified on the 0–3s contact strip. PASS
- How U1 got here: both raw takes put speech at 1.7–1.9s
  (t1 head −11.5 dB, t2 −10.5 dB). t2 kept for picture (head MAE
  ratio 2.45×) and repaired in assembly per the audit's own fix
  menu: start-on-the-hit head trim (0.45s) + 1.047× stretch +
  the take's own frame-0 scuff repositioned as the accent. No
  foreign sound was added; nothing was faded in.
- Loudness pass: fixed +10.13 dB (joined median −30.13 → target
  −20), −1 dBFS limiter (0% of 100ms windows over threshold
  pre-limiter; transients only). Measured master median −19.1 dB.

## JOINT GATE (on work/joined.mp4, before any overlay)
All five boundaries are declared BREAKs (the show's law: the
street is culled every 10s; the SCRIPT opens every unit in a new
world) — classification + rotation written pre-volley in
REFERENCE_STACK.md. BREAK class = no seam-MAE bar; the numbers
are recorded anyway: BASE (95th pct in-unit adjacent MAE) 18.96.
- B1 U1→U2: seam MAE 1.95 (0.10×BASE) · chalk in Laura's closed
  fist (U1 cliff) → chalk raised in her hand at U2 frame 0 ✓
- B2 U2→U3: seam MAE 3.47 (0.18×) · her stroke lands across the
  cut: letter L stands on U3's wall ✓
- B3 U3→U4: seam MAE 13.13 (0.69×) · the STRADDLE: parcel offered
  unaccepted at U3's cliff → in Laura's arms at U4 frame 0 ✓
- B4 U4→U5: seam MAE 4.01 (0.21×) · parcel in Laura's arms both
  sides; the borrowed stub is back in her fist ✓
- B5 U5→U6: seam MAE 6.99 (0.37×) · parcel turned signing-side
  up + chalk rising on both sides of the cut ✓
Eye checklist (all five): identities vs CHAR panels hold both
sides; wardrobe unchanged; carry present + correct custody both
sides, straddle at B3 completes at the incoming head; light
direction consistent (morning, frame left); declared matches
(carry + clock snap) present at every joint; motion alive both
sides (no settled tails; every incoming head already moving).
The Cull Clock snaps full exactly on each joint frame (frame
240 verified by eye: full ring + cadmium ghost + tally at 7).
**JOINT GATE: PASS ×5. No joint was dissolved over.**

## Dialogue gate (ASR: faster-whisper large-v3-turbo, no VAD)
- U1 (t2): 4/4 lines in order. ASR reads "call" for "cull" in
  the last line (t1 read "cool") — homophone hand-check: the
  prompted word is "cull"; U3/U4 ASR reads "cull" correctly from
  the same cast; the U1 reads are ASR lexicon guesses on an
  ambiguous short vowel. Ruled VERBATIM with this note.
- U2 (t1): 4/4 EXACT. U3 (t1): 4/4 EXACT. U4 (t1): 4/4 (ASR
  numerals "421"/"20" = the spoken words). U5 (t1): 4/4 EXACT.
- U6 (t4): 5/5 EXACT — after t1 dropped the Courier's answer and
  t2/t3 dropped the Watcher's cliff line; t4 restaged the
  Watcher as a full in-frame presence and all five landed.
- Speaker order and address terms verified against SCRIPT.md.

## Graphic audit (Method C §4.1/§5.6)
- Cull Clock: (1) it IS the show's subject — the cull made
  visible; (2) exists with the sound off — it is the deadline
  itself; (3) never competes with speech (visual channel,
  furniture corner). Snaps full on all five joint frames ✓;
  empties over exactly 10.0s per unit ✓; ignition 0.21–0.79s on
  U1 (the BLAM fix menu's sanctioned early fire; frame 0 itself
  carries no graphic — §3.5 tension logged in GFX_CARDS.md).
- Chalk Tally: serial arithmetic vs ledger — pilot banked 6;
  E2 carries 7→12, one draw-on per unit (U6 frame shows exactly
  12: two five-bar gates + 2) ✓. Placement ruling (furniture
  corner under the clock, not the in-frame wall) in GFX_CARDS.md.
- The Stamp: one firing, U6 local frame 185 = the QC-located
  handover frame (pass completes ≈7.7s); text "CULL 423" =
  U6's cull in the episode's 418–423 run ✓; legible at full
  res and on the strip ✓. Timing note (G7): local 7.71s sits
  inside the nominal 7–9s clock band — but U6's grammar is
  displaced by the silence beat: the turn line runs 5.2–7.0s
  and the cliff line 8.2–9.4s, so the stamp fires in the
  speech-free gap between them, exactly on the state change
  it exists to mark (Method C: the stamp fires on signings
  and handovers). It overlaps no spoken line.
- Frame-0 audit: master frame 0 = clean generated picture, no
  graphic event ✓. Bug: exact `~ WuBu ~`, CADMIUM, bottom-right,
  full duration ✓.
- Ledger advancement (§3.4): culls 418–423 consumed one per
  unit; F-018 (parcel signed, Laura's hand, Courier's name,
  chalk) delivered in U6 — the signature is visible on the
  parcel in the final frames; F-019 (wall completed LAURA while
  every hand in frame was busy) delivered — the completed name
  is large and legible in U6's final frames. PASS.

## Known flaws (plain)
1. **The U6 silence beat is compressed.** Scripted 2.5s; the
   keeper take delivers a 0.74s word gap (≈1.3s of held action:
   chalk hovering, street still) between the Courier's answer
   and the signing line. All four U6 takes compressed it.
   Assembly protects what exists (no trim on U6) but does not
   manufacture the missing ~1.2s. The beat reads; it is shorter
   than scripted.
2. U1's dialogue carries the homophone note above ("cull" ASR-
   read as "call"/"cool" in U1 only). Ruled verbatim; flagged
   for the parent's ear at delivery.
3. U3's head is quiet: first word at 0.62s over paper-creak
   ambience (head mean −19.8 dB vs its own median). Within
   normal unit-opening behaviour and not BLAM-gated, but it is
   the softest unit head in the episode.
4. U6's head motion is the episode's stillest (the held signing
   tableau the script asks for): head MAE ratio 0.82 on the
   keeper — inside the motion law, but the unit opens held, by
   design, before the signing.
5. Minor picture nits: the Courier's coat reads bright cobalt
   in U1/U6 close-ups (within the pilot's accepted range, much
   reduced vs the pilot's U2/U5 drift); U4's parcel carries a
   small yellow label with red marks that reads as a printed
   shipping label (no legible words); U5's final frame shows a
   blank label outline on the parcel; U2's PEAK staging (finger
   meeting the chalk rather than the tallies) carries into the
   take's opening beat — the wall count itself plays in the
   unit's close-ups.
6. The stamp is large (≈37% of frame width) and overlaps the
   parcel's lower-left corner in the final frames. It is the
   show's cliff device at its designed fallback position;
   flagged as a size nit, not a placement error.
7. Laura's ponytail reads loose in a few U6 frames; identity
   holds throughout. The Watcher's identity — the pilot's U3
   failure — holds in every unit of this episode (anchored per
   the rotation table).

## Verdict
All hard gates PASS: format, BLAM (all seven bars), Joint ×5,
dialogue verbatim (one homophone note), ledger advancement,
graphic audit. Flaws above are disclosed, none gate-blocking.
E2_DELIVERED.flag written.
