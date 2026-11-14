# MV-5 v6 — GATE LOG (house)

Build: **MV-5 "Easy now, easy now (THE VOICE)" — FULL REBUILD v6**, 2026-11-13.
Coordinator: mv5-full-rebuild. Parent delivers; no delivered flag written,
nothing committed by the coordinator.

## Masters

| File | md5 | Spec |
|---|---|---|
| masters/mv5_easy_now_easy_now_16x9_v6.mp4 | 2071388f3fb5672849e29462cb3f2b64 | 197,194,272 B · h264 1280×720 · 24fps · **4954 frames** · 206.4167s · AAC 48kHz stereo 192k · faststart · CRF 18 |
| masters/mv5_easy_now_easy_now_16x9_v6_chat.mp4 | 2e2688bd592821e0a4c6ab3ab5f4657b | 46,122,464 B (≤50 MB) · 854×480 crf 26 · AAC copied |

Sole master audio: track.mp3 (md5 0c1bcafa568547e2d4fa36e133ad3626, verified
pre-mux). Generated clip audio dropped everywhere. Captions:
work/lyrics-redo/mv5_kinetic_redo.ass (548 events, reused as-is from the
verified lyrics redo). `~ WuBu ~` bug burned on all frames. Texture pass
(noise 5 / vignette PI/5 / saturation 0.88 / contrast 1.02) applied to the
picture BEFORE caption burn. S22 carries the blackout-snap fade dip (post
grade, 7.2).

## Fit gate

- Builder: work/rebuild-v6/build_v6_plan.py (v3) → assembly_fit_mv5_v6.json.
- **0 errors.** Plan frames = 4954 = target exactly. No src frame used twice
  (core-based clamp). All phrase/span warps inside [0.52, 1.96] ⊂ [0.5, 2.0].
- 29 disclosures carried in the fit JSON: duet-span internal onset offsets
  (two-voice ASR cannot anchor chorus interiors; endpoints anchored, mouths
  eye-verified at onsets — see visual gate), phrase internal drift on the
  two held GIRL lines (L16 +1.19 max, L56 +1.11 max — rubato inside a
  sustained line, mouth moving throughout), L05 PX2 onset compromise
  (+~0.3s on the last word), L02 PX2 (warp 0.54; internal onset drift
  ~0.49 disclosed).
- Out-of-band FILLS (warn class, all brief beats): s13_boombox w6.72 over
  32f (scatter time-lapse), s26_chain 5f head flash w6.00 into S27,
  s02_ride 13f head flash w4.48 into S02.

## Audio agreement

Master audio vs track.mp3, 20 × 10s windows, 8kHz mono Pearson:
**min 0.9985 · mean 0.9989 — PASS.**

## Motion audit

Mean frame diff (160×90) 9.77. Near-dup runs ≥12f: 24f, 17f, 13f, 12f.
- 24f @ 44.58s (S06, L12): held two-shot tableau while the CAT sings L12 —
  eye-read at full res: composed tableau (keys in her hand, mango stall,
  gulls), the cat's mouth articulates in-frame; micro-motion falls under
  the 160×90 dup threshold. Disclosed nit, not a freeze-frame.
- 17f @ 46.88s (S06 tail), 13f @ 188.04s (S25, L106 head), 12f @ 99.08s
  (S12, inside the sustained L44 hold — by design). All sub-threshold.
- No halted-photo starts: S01 opens on the rolling ride fill + sung hook
  from frame 0 (eye-read I01).

## Colour gate (G1, hard)

Rule: GIRL's defining top = BLUE SHIRT (no red top anywhere); bicycle =
RED in every frame including background. Verified at full res per take in
volley QC (zero rejects) and again on the master at ~60 onset/scene frames
(visual gate doc). Diegetic text exception carried from volley QC:
s06_cat's "MANGO" stall sign (set dressing, not generated caption text).

## Rejects + refusals (complete)

- REJECT (QC): mv5_v6_s25_cat v1 — identity intrusion: an unknown
  brown-haired girl in a pink floral top with an open mouth at frame right
  beside the CAT's L104 close-up (G1 + singer-pair). REPLACED by
  mv5_v6_s25_cat2 (solo close-up, full-res verified clean) — L104 has a
  real CAT take; the disclosed-cover fallback was NOT needed.
- Generator refusals (integrity_check_failed, never retried per policy):
  pilot p1 and pilot p3 (both conditioned on ref_girl_bike.png — the girl
  route was rebuilt on ref_girl_face.png / ref_pair_ride.png), s09_duet
  (umbrella cascade — restaged as the s09b kite).
- Pilot verdict: PASS (p2 colour-locked at full res before volley 1).

## Verdict

ALL HOUSE GATES PASS with the disclosures above and in VISUAL_GATE_V6.md.
Ready for the parent's own gate + delivery.
