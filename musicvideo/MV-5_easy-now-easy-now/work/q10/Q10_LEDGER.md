# MV-5 Q10 — Volley Ledger (2026-11-13 ~03:05 EST)

Volley: 6 fired. 3 landed, 3 integrity-blocked (NOT retried — system instruction: do not repeat, including with changed arguments or through another tool).

## Landed takes — QC

| take | file | md5 | dur | ffprobe | Whisper | RMS | verdict |
|---|---|---|---|---|---|---|---|
| q10_s04 (CAT L01–L05, 10s) | media-generation-mv5-q10-s04-0-de3b228a-87cd-4d96-ba4c-1d1f1d89607f.mp4 | 9a0d1ae15f0335b4400736bed07ccdaf | 10.000s | 1280×720 24fps 240f h264+aac | 18/18 words in order: Bare 0.00, feet 0.48, on 0.96, the 1.32, boardwalk 1.50, salt 2.54, on 3.68, my 3.92, skin 4.14, You 4.44, came 4.64, in 4.88, laughing 5.08, said 5.54, come 5.96, on 6.26, let's 6.64, begin 6.96 | 0.1571 | **KEEP** — with limitation: sings L01–L04 only; model stopped at 6.96s, NO L05. L05 from old take s04_t1 (its L05 Blue 7.10–8.52, ratio ~1.0). Mouth visibly open on words (frames 1.7, 4.6); girl mouth closed; locks hold; no text. Placement: L01 phrase warp 1.98x; L02 per-word (max offset +0.20 on "on"); L03 phrase warp setpts 1.19; L04 phrase warp setpts 1.51. |
| q10_s06_l11 (CAT L11 brisk, req 5s) | media-generation-mv5-q10-s06-l11-0-087fd77c-41ea-4715-b60c-9f7e5916bd33.mp4 | 2633390fe5c3405b0a800d593f0525df | 10.000s (returned 10s for a 5s request) | 1280×720 24fps 240f h264+aac | 6/6 words in order: You 0.00, nodded 0.44, at 1.42, the 1.72, waves 2.02, like 3.06 | 0.0850 | **REJECT — pacing.** Sings the line in ~3.5s vs 0.98s song (ratio 0.28, WORSE than the old take's 2.76s). You→nodded 0.44s vs song 0.08s (5.5x); nodded→at 0.98s vs 0.36s (2.72x). Mouth is great (frames 0.6, 3.3 wide open) but the pace floor bites: 6 words in 0.98s cannot be mouth-sung by this generator. **L11 is STRUCTURAL.** Repair: montage cover for L11 (43.28–44.58) + s06_t2 girl insert re-anchored to 44.58. Take tail (3.5–10s, mouth closed) usable as donor cover. |
| q10_s12_l43 (GIRL L43 brisk, 5s) | media-generation-mv5-q10-s12-l43-0-8f7d2452-1821-43f3-bdf5-42b929761748.mp4 | 879e2c789c5686fe29b9f7dcf4910f95 | 5.000s | 1280×720 24fps 120f h264+aac | 7/7 words in order: I 0.00, forgot 0.20, the 0.56, list 0.84, forgot 1.44, the 1.74, bills 2.04 | 0.0979 | **KEEP.** Girl mouth visibly open ("bills" frame 2.2); CAT mouth closed; locks hold; no text. Placement: per-word with one gap-trim (list→forgot 0.60s→~0.35s closed-mouth trim); max internal speedup 1.88x, within the 2x ceiling. |
| q10_s07_l15 (GIRL L15 restaged, brisk, 5s) — CAP-LIFT take, parent-approved 2026-11-13 ~03:23 EST | media-generation-mv5-q10-s07-l15-0-93523940-8d77-4d8e-9bb0-70e12555acb2.mp4 → registered `takes/mv5_q10_s07_l15.mp4` | 0f77772d71ab921c599376a95ffc0693 | 5.000s | 1280×720 24fps 120f h264+aac | 5/5 words in order, one segment: One 0.00, small 0.50, look 0.96, from 1.46, you 1.94–2.46 | 0.0785 | **KEEP.** Girl alone in frame, NO CAT; mouth visibly open on every word (frames 0.5, 1.0, 2.0 wide open; 2.5 closing after line end); eyes closed throughout (same as volley-15 s07_t2, picture-PASS trait); locks hold (purple hair, straw hat red ribbon, red jacket); no on-screen text (tiny background shop sign top-right, set dressing only). Placement: single phrase warp 0.6341 (1.58x), One→51.24 ✓, you ends 52.80 ✓. Far better than s07_t2 (2.56s, per-word warps to 0.36). |

## Blocked takes — integrity_check_failed, NOT retried (system instruction)

| take | vehicle | status |
|---|---|---|
| q10_i08 (CAT "Till the morning comes" held) | mv5_q10_i08_vehicle.txt | **BLOCKED.** No take exists of the CAT singing I08. Fallback: montage cover for I08 (12.72–17.52, moving riding/bell/bike cuts on the beat) + captions carry the words. Disclosed structural. |
| q10_l104 (CAT "We're good where we are") | mv5_q10_l104_vehicle.txt | **BLOCKED.** No take exists of the CAT singing L104. Fallback: keep v4 picture (girl sings the hook; CAT's lead line stays mouth-less). **Program item stays OPEN** — Q10 does not close all 4 closed onsets. Disclosed. |
| q10_s07_l16 (CAT "And my whole head replays" held) | mv5_q10_s07_l16_vehicle.txt | **BLOCKED.** Old take s07_t1 sings it in 2.44s, "And" 1.59s late; per-word warp needs 0.43x (below floor). Fallback: montage cover for L16 (52.80–57.74) + captions carry the words; removes the visibly-late mouth. Disclosed structural. |

## Owed — 7th take — RESOLVED 2026-11-13 ~03:30 EST (cap lift granted by parent ~03:23 EST)

- Restaged S07 L15 GIRL insert ("One small look from you", 51.24–52.80) — FIRED + **KEEP** (see landed table above). Girl alone, no CAT; 5/5 words, phrase warp 0.6341. Goes into v5 in place of the donor cover.
- CORRECTION (measured 2026-11-13): the donor cover as specified here (s07_t1 take-time 6.25–7.52s, "CAT mouth-closed gap") was WRONG — s07_t1 sings "from" 6.12–6.38 and "you" 6.38–6.88; the true mouth-closed gap before "And" is 6.88–7.52s (f165–180). A 6.25–7.52s donor cover would have shown the CAT mouthing L15's own words. Moot now (restaged take KEEPs), but do not reuse the 6.25–7.52s span as a mouth-closed cover anywhere.

## QC method (per take)

ffprobe (codec/dims/fps/frames/duration) + md5sum + faster-whisper large-v3-turbo word timestamps (lyrics venv) + RMS on 16k mono wav + 5 full-res frames via separate -ss calls (distinct md5s verified) + eye reads (mouth open on words, identity locks, no on-screen text).

## Addendum — v5 plan build (2026-11-13 ~04:00 EST)

### Registration correction
- The cap-lift take q10_s07_l15 was **NOT actually in `takes/`** — the file
  existed only at `work/q10/takes/mv5_q10_s07_l15.mp4`. The ledger row above
  ("registered `takes/mv5_q10_s07_l15.mp4`") was written before the copy
  happened. FIXED 2026-11-13 ~04:00 EST: copied
  `work/q10/takes/mv5_q10_s07_l15.mp4` → `takes/mv5_q10_s07_l15.mp4`,
  md5 verified `0f77772d71ab921c599376a95ffc0693` (matches the ledger),
  120f 1280×720 24fps. The other two Q10 KEEPs (s04, s12_l43) were already
  in `takes/` with matching md5s.

### v5 plan — corrections found by build_v5_plan.py (all fixed in the builder)
- Takes are 240f, not 241f (10.03s files). Every ef=241 piece capped to the
  take's real frame count (S06 L11a, S07 L16a/L16b, S28 tail). v4's S14
  (s19b_t1 ef 121 > 120f) is verbatim — the assembler tpad-pads it, as in v4.
- S02 pre-I09 cover: s03_t1 f96–120 REJECTED by the reuse check — v4 S13
  owns s03_t1 f115–120. Now s03_t1 f96–115 (19f, verified closed f100) +
  s01_t1 f171–176 (5f, verified gap). s03_t1 f91–118 also rejected — the
  Ta-da vocalise ends 3.78s, f91 is 0.01s after (mouth still open).
- S27 L109b: s27_t1 f114–139 REJECTED — v4 S14 owns s27_t1 f114–144.
  Now s28_t2 f120–145 (25f): girl "Till" take's post-word tail, RMS quiet
  after 4s, frames f120/f145 verified mouth-closed (girl smiling, CAT in
  basket looking at her). Transcribed for the cover check
  (S28_T2_prompted.json: Till 0–0.58, the 0.58–0.84, morning 0.84–1.80,
  comes 1.80–3.24; nothing after 3.24s).
- S12 L44c: s24_t1 f132–155 REJECTED — overlaps S24's own L98b/L100 pieces.
  Now s24_t3 f144–167 (23f, verified closed f150/f155).
- S01: leader f0–34 + I03 starts f125 (not f126 — "Easy" starts 5.24s, the
  f126 boundary clipped its head by 1 frame); I04b out 42 to hold 241f.
- S11 L40 REDESIGNED (builder caught it): v4's single warp put "Time" 2.05s
  early. L40 head is a cover; L40 tail ("time with our feet") is sung at
  warp 1.105 — all four words within ±0.12s of the grid.
- S24 P2 (s24_t3, v4-verbatim): take's 2nd "easy" lands −0.91s between
  L101's "easy" (180.94) and L103's "Easy" (182.78) in the overlapping
  chorus — disclosed v4 carryover, not a v5 regression.
- S01 I02/I04 + S04 L04 were split per-word in the builder (single warps
  put "ride." +0.70s and "begin" +0.86s late). Builder's word-offset report
  is the authority; worst non-disclosed offset in v5 is +0.30s (S04 L05
  "red", v4-verbatim).
- L69 is a mouth-CLOSED cover (s09_t1 f185–211) — v4's "singing tail" label
  was wrong; the take's last "Easy now" (f120–142) sits inside S09's piece
  and cannot be reused. L109 has no sung picture (s28_t2 "Till" would need
  warp 0.42 < 0.5 floor). Both disclosed structural.
