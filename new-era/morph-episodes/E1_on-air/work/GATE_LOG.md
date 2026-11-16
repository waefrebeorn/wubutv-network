# ON AIR E1 "The Signed Folder" — GATE LOG

**Provenance:** production coordinator 1 fired all six units
(takes/U*_take1_KEEP.mp4), built the six segments and
work/joined.mp4, and failed ~03:15 EST during final assembly
prep — no master, no gate log. This log was completed by the
recovery coordinator from the disk state: every segment probed,
all gates run, master encoded in one uninterrupted pass from
work/joined.mp4. **No segment was refired** — none failed a
probe or a logged gate.

## SEGMENT PROBES — PASS (all six)

| Seg | Frames | Duration | Size | Video | Audio |
|---|---|---|---|---|---|
| seg_u1 | 240 | 10.000s | 6,189,670 B | 1280×720 24fps h264 | AAC |
| seg_u2 | 240 | 10.000s | 7,490,771 B | 1280×720 24fps h264 | AAC |
| seg_u3 | 240 | 10.000s | 17,104,367 B | 1280×720 24fps h264 | AAC |
| seg_u4 | 240 | 10.000s | 8,891,139 B | 1280×720 24fps h264 | AAC |
| seg_u5 | 240 | 10.000s | 9,553,418 B | 1280×720 24fps h264 | AAC |
| seg_u6 | 240 | 10.000s | 7,289,184 B | 1280×720 24fps h264 | AAC |

**Joined intermediate (pre-master probe):** work/joined.mp4 =
1440 frames / 60.000s — exactly the segment sum. ✓ One assembly
pass owns it; the master encode below is the single master pass.

## DIALOGUE GATE (ASR vs SCRIPT.md) — PASS

Per-unit ASR records (work/qc/u*t1/asr.json) checked word by
word against the locked script:

- U1: 18/18 exact — "That's your mouth. Your signature." /
  "Not my mouth. Not my hand." / "The true video airs tonight.
  By hand."
- U2: 15/15 exact — Peter's interrupted entrance, "You sent his
  face already.", "Strip's ahead of the picture." (ASR renders
  "Strips"; apostrophe artifact only.)
- U3: 8/8 exact — "One shift. Nothing with my mouth in it."
  Plus sung vocables ("Oh, oh, oh") from the aired segment's
  song — singing, not dialogue (see flaw F5).
- U4: 19/19 exact — incl. "It isn't copying you. It's crediting
  you."
- U5: 15/15 exact — incl. "I didn't sell a singer. I sold my
  boss."
- U6: 12/12 exact — incl. the cliff line "Then who already
  aired us?"

**Total: 87/87 scripted words on screen, verbatim.**

## JOINT GATE (seam MAE, 320×180 gray) — PASS ×5

Bands (carried from THE MACHINE E2): PASS ≤58 · CONDITIONAL
≤75 · FAIL >75. Script: work/qc/recovery/jointgate_e1.py.

| Joint | Seam MAE | Band | Downstream head motion f0→f12 |
|---|---|---|---|
| U1–U2 @f240 | 34.7 | PASS | 34.7 |
| U2–U3 @f480 | 1.6 | PASS | 10.7 |
| U3–U4 @f720 | 3.3 | PASS | 62.4 |
| U4–U5 @f960 | 1.7 | PASS | 26.9 |
| U5–U6 @f1200 | 48.4 | PASS | 28.4 |

## COHESION GATE (msg 507 standing rule) — EYE VERDICTS

Per-joint eye check of the ±6-frame strips
(work/qc/recovery/joints/strip_*.png): world / wardrobe /
position / light continuity across each seam — seam MAE alone
does not clear a joint under this rule.

- **U1–U2 — CONDITIONAL.** World, wardrobe and light are
  continuous: same control room, Laura's green shirt, the
  monitor/cat/ON AIR state identical, Peter's yellow jacket
  consistent with his U4 wardrobe. BUT the seam is a hard
  reframing: U1 ends on a tight Laura/UNC two-shot at the
  console; U2 opens on a wider three-shot with UNC out of
  frame and Peter already standing mid-room holding his
  phone — his scripted entrance is not carried across the
  seam and the blocking resets. It reads as a cut to a new
  angle on the same scene, not a last-frame→first-frame
  handoff. The one non-continuous joint in the episode.
- **U2–U3 — PASS (strongest).** Identical camera position,
  blocking, wardrobe and props across the seam (over-UNC
  shoulder; Laura seated opposite; the cat sitting on the
  console; the signed folder on the desk). The mouth handoff
  into the aired segment fires inside U3, so the seam itself
  is frame-matched continuous action.
- **U3–U4 — PASS.** The seam sits inside the aired segment:
  the singer's close-up (black cat, red collar, crystal
  layer-stack world) is continuous across all twelve strip
  frames; the exit handoff back to the room lands inside U4.
  Same subject, same light, no world break.
- **U4–U5 — PASS.** Identical framing across the seam (UNC
  medium shot, paused monitor behind him, warm practical at
  right). GAP 2's held reaction on UNC's face literally
  bridges the joint — the hold is the handoff.
- **U5–U6 — PASS.** Action-continuous: the seam is one
  gesture — hands set the tomorrow invoice down on the
  console and move to the faders. Same desk, same papers,
  same light throughout; U6's hand-fired slot grows out of
  the U5 tail without a reset.

**Episode-level read:** one continuous story in one room
across one deadline — NOT trailer fragments. Four of five
seams are continuous action or a carried hold; the
accusation chain (folder → sale → aired segment → credit →
billing book → hand-fired slot) plays in order with no reset
of place, cast or stakes. The single reframing cut is
U1–U2 (above).

## WORDMARK GATE (full-span sweep) — PASS

Everywhere UNC's chest is legible, the hoodie reads exactly
`~ WuBu ~` in cadmium: U4 at 9 sampled points
(work/qc/u4t1/wm_*.png, wm_strip.png) and U5 at 5 points plus
frame 120 (work/qc/u5t1/wm_*.png, wm_stack.png) — no drift at
any point, no refire spent. U1/U2/U6: UNC's chest is never
legible (shadow, profile, hooded back). U3: UNC not on
screen.

## METHOD C POST GRAPHICS

- **U4 credit `SINGER: UNC`** — present in seg_u4 (composited
  during segment build), white bold, legible against the
  paused frame. ✓
- **U6 freeze graphics** — the question "Then who already
  aired us?" and the tomorrow call-sheet box are composited
  in seg_u6 from 8.33s; the final frames hold the freeze
  (ON AIR light + the singer's face). ✓ Legible in the
  master (frame 1430 checked).
- **Broadcast Strip** — added in the master pass: cobalt
  (0x0047AB) waveform, frame-bottom band, driven by the
  episode's own audio advanced +0.4s so the strip literally
  runs ahead of the audible picture, per the show's rule. ✓
  (Head fade-in: flaw F2.)
- **Corner bug `~ WuBu ~`** — added in the master pass,
  top-right, cadmium, full duration. ✓

## BLAM GATE (measured on the finished master) — ALL BARS PASS

Tool: work/qc/measure.py, label "master".

- **A1** onset: t50 0.0s (≤0.5) ✓ · t90 0.1s (≤1.5) ✓
- **A2** dead head: 0.0s (≤0.2) ✓
- **A3** head level: 0.5s means −19.4 / −20.2 / −16.9 dBFS vs
  full-runtime median −27.4 dBFS — the head runs ABOVE the
  median, with the accent inside the first window ✓
- **A4** crackle: HF bursts 0–1.5s = 16 vs 30s control = 14
  → 1.14× (≤2×) ✓
- **V1** opening motion: head 0–0.5s MAE = 3.18× the 3–10s
  baseline (≥0.6×) ✓
- **V2** no ramp-from-rest: first 0.25s MAE bucket 3.77 =
  0.68× of the 0–3s max bucket, 3.2× baseline — motion from
  frame 0 ✓
- **E1** named impact ≤1.0s: frame 0 — ON AIR light lit, the
  big monitor already mid-video at full sound, the singer
  mid-note, Laura up with the folder ✓
- **E2** first graphic ≤3.0s: the Broadcast Strip is live
  from the opening second (full presence ≈0.25s — F2) ✓

## LOUDNESS PASS

Joined measured: −18.28 LUFS integrated / TP −0.30 dBTP /
LRA 14.8. Loudnorm applied in the master pass (target −16
LUFS, TP −1.5). **Master measures: −17.12 LUFS / TP −1.42 /
LRA 10.7** (dynamic fallback; landing disclosed as F3).

## CRF PROOF — differential (SEI string is NOT a valid gate
on this ffmpeg build)

Identical filter chain encoded at CRF 23:
work/qc/recovery/crf23_proof.mp4 = 15,829,747 B.
Master at CRF 18 = 28,253,893 B → **1.78× the CRF-23 size.
CRF 18 proven by differential.** ✓

## MASTER — VERIFIED END TO END

- **File:** masters/ON_AIR_E1_MASTER.mp4
- **MD5:** 06cd491007f6919357716010495a00af
- **Size:** 28,253,893 B (under 50 MB — no chat copy needed;
  the master is the delivery file)
- **Duration:** 60.000s · **Frames:** 1440 counted end-to-end
- **Video:** h264, 1280×720, 24fps · **Audio:** AAC 48kHz
  (mono — source-inherent, see F6)
- **Faststart:** moov at byte 36, ahead of mdat ✓

## FLAWS DISCLOSED (plainly)

- **F1 — U1 mouth composite does not read as scripted.**
  Frame 0's singer sings with a CAT's mouth — wide open,
  fanged. The scripted cross-species composite (the cat with
  UNC's mouth) is not legible as a human mouth. The
  wrongness still lands in the first frame (a singing cat on
  the broadcast monitor + Laura's "That's your mouth"), but
  the specific gag is weaker than written. This is the risk
  SLATE §5 flagged for this show. Not refired: the take
  passes every hard gate, and a refire would re-roll the
  U1–U2 joint.
- **F2 — Broadcast Strip head fade-in.** The strip band
  reaches full presence at ≈ frame 4–6 (0.17–0.25s) rather
  than being fully present at frame 0 exactly (overlay
  framesync). The device is live for 99.6% of the runtime
  and inside the BLAM window; disclosed rather than
  re-encoded.
- **F3 — Loudness landing.** Master integrated loudness
  −17.12 LUFS vs the −16 target (1.1 dB under); true peak
  −1.42 dBTP vs the −1.5 ceiling (0.08 dB over). Within
  delivery tolerance; disclosed.
- **F4 — U1–U2 cohesion CONDITIONAL.** One reframing cut
  among five joints (see the cohesion gate). All other
  joints are continuous.
- **F5 — U3 sung vocables.** The aired segment's song adds
  "Oh, oh, oh" vocables beyond UNC's scripted line. They
  are singing inside the music-video segment, not added
  dialogue; noted for the record.
- **F6 — Mono audio.** The generated takes are mono; the
  master is AAC mono. No stereo stage was fabricated.

Recovery artifacts: work/qc/recovery/ (jointgate_e1.py,
master_filter.txt, crf23_proof.mp4, joint strips, frame
grabs). GATE LOG completed 2026-11-16 by the recovery
coordinator.
