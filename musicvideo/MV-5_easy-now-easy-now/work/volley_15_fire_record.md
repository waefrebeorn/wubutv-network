# Volley 15 fire record — L15 girl-singing fix (take-audit refires), 2026-11-06 ~02:39–02:45 EST

User verdict on the v2 master 2026-11-06 ~02:33 EST: the girl's singing is
missing in the beginning because the cat sings her part. L15 "One small look
from you" (song 51.46–52.80, GIRL per the user's ear + Gemini app spk:1) had
no girl-singing picture in v2 — only a closed-mouth donor cover. Fired on
standing authorization (user order 2026-11-05 02:45 EST: volleys proceed
autonomously; the 6-video cap is a batching limit only). Two parallel-variant
girl takes for L15, same line, same window, different staging, so QC can pick
the better take. Character locks verbatim in every vehicle. ONE 16:9 only,
zero on-screen text, no licensed characters.

CORRECTION (parent, ~02:42 EST, arrived mid-volley): the original brief's
mv5_s28_t5 (GIRL sings L110b) was WRONG — S28 girl generation is CLOSED
(t2/t3/t4 all REJECT PACING, floor ~2.7s vs 1.6s window, no legal placement;
no t5). s28_t5 was already generated before the correction arrived; it is
DISCARDED (no QC row, no verdict). L110b keeps its v2 structural cover. The
revised volley is two L15 takes only.

## Fired (2 L15 takes; 1 discarded pre-correction take)

| Take | Vehicle | md5 | Dur | Result file |
|---|---|---|---|---|
| mv5_s07_t2 | mv5_s07_t2_vehicle_v2.txt (FRESH staging — girl seated on the bike at the boardwalk rail, close-up; the volley-12 vehicle died on integrity_check_failed and was NOT resubmitted) | 39ba0cf638d31f165accd2101ef487e8 | 5.000s | takes/media-generation-mv5-s07-t2-0-a3e702db-fe5e-481d-be84-9ca87eea8149.mp4 |
| mv5_s07_t3 | mv5_s07_t3_vehicle.txt (parallel variant — girl RIDING the bike toward camera, medium-wide moving shot) | 023a9fc3aa862a7c324a0ffa18807ffc | 5.000s | takes/media-generation-mv5-s07-t3-0-84992ad2-323f-4ca5-94e1-519ea38a3fbe.mp4 |
| mv5_s28_t5 | mv5_s28_t5_vehicle.txt (fired pre-correction) | b347c9faf46a1fd51902152cd048b28e | 5.000s | takes/media-generation-mv5-s28-t5-0-affa3f23-6862-4d1b-8722-5a4510f2fb0a.mp4 — DISCARDED, must not enter the v3 cut |

Canonical takes: takes/mv5_s07_t2.mp4, takes/mv5_s07_t3.mp4 (copies of the
generation records above). All 1280x720, 24fps, durations measured with
ffprobe (never the tool's claim).

## QC summary (full verdicts: work/qc_v15/qc_v15_verdicts.md)

- s07_t2: **REJECT (PACING)**. Line sung once, complete, both decodes agree
  (0.0–2.56s); ratio 0.52 vs song 1.34s (clear miss, below the 0.60 grey
  floor); single warp 1.91x, per-word warps 0.54/0.36/0.56/0.71/0.58, best
  two-anchor 0.47/0.64 — no legal placement. Picture PASSES (girl sings,
  cat silent, locks hold, no text; frame rule vocal mean 1.092, run 1).
  Disclosed nit: eyes closed at 0.5s/1.0s.
- s07_t3: **REJECT (PACING + DELIVERY)**. Line sung once, complete, both
  decodes agree (0.0–3.64s); ratio 0.37; "One" held 1.42s with a quiet head
  (RMS 0.007/0.026 at 0–1.0s; audible line ~1.0–3.64s, ratio ~0.51 even
  corrected). Single warp 2.7x. Picture PASSES with nits (mouth open at
  1.5s/2.5s; mouth still open in a smile at 4.0s after the line ended;
  background shop signs carry small letter-like marks — flagged, not failed).
- **Better L15 take: s07_t2** (tighter span, even words, clean hold, cleaner
  picture) — but it does not place legally either.

## Volley 15 result: 0 KEEP / 2 REJECT (both PACING)

## Assembly notes (carried forward)

- L15 is STRUCTURAL for per-line generation: song window 1.34s vs the
  model's ~2.2–2.6s/line pace floor; two pulls on different stagings both
  landed clear-miss (0.52 / 0.37). Per the skill, L15 leaves the generation
  queue — no re-fire, no third pull, no warp beyond the cap.
- CONFLICT FOR THE PARENT: the user's 2026-11-06 law bans closed-mouth
  covers under sung lines, and the warp cap bans the 1.91x playback t2 would
  need — no in-band option remains inside the current rules. Parent's call
  whether v3 places t2 at a disclosed out-of-band warp, uses a montage
  treatment, or another route. This volley makes no recommendation; it
  reports that t2 is the best available girl-singing picture for L15.
- S07: t1 (all-CAT) still keeps L13/L14/L16. L15's only girl-singing
  pictures are t2 (better) and t3.
- S28: unchanged — STRUCTURAL, L110b keeps the v2 cover (s28_t3 closed-mouth
  tail + captions). s28_t5 is discarded and must not enter the cut.
- Song grids agree on L15 (v1 = app: 51.46–52.80), so no alternate-grid fit
  rescue exists (unlike L88 in volley 12).

## Evidence

- work/qc_v15.py + work/qc_v15/qc_v15_results.json + work/qc_v15/qc_v15.log
- work/qc_v15/qc_v15_verdicts.md (full per-take verdicts)
- work/qc_v15/s07_t*.png + s07_t3_t*.png (frame reads, 0.5–4.0s per take)
- Vehicle files: mv5_s07_t2_vehicle_v2.txt, mv5_s07_t3_vehicle.txt,
  mv5_s28_t5_vehicle.txt (discarded take — do not use)
- work/gemini_takes_verdicts.md (audit brief that opened this volley);
  work/volley_12_fire_record.md (proven P-GIRL-SING pattern, s06_t2 KEEP)
