# Volley 12 fire record — ear-confirmed GIRL inserts (take-audit conditional refires), 2026-11-06 ~00:2x–00:40 EST

User answered the three ear checks 2026-11-06 ~00:20 EST: L12 GIRL, L15 GIRL,
bridge ALTERNATING (GIRL-first: L82 GIRL, L83 CAT, L84 GIRL, L85 CAT, L86 GIRL,
L87 CAT, L88 GIRL, L89 CAT). Fired on standing authorization (user order
2026-11-05 02:45 EST: volleys proceed autonomously; the 6-video cap is a
batching limit only). All six vehicles are P-GIRL-SING (proven S28 t3 grammar):
girl sings ONLY the one line to camera in medium close-up, brisk, no held note,
line finished in ~2s of a 5s take, hold still after; CAT sits in the basket,
mouth closed and still for the whole clip. Character locks verbatim in every
vehicle. ONE 16:9 only, zero on-screen text, no licensed characters.

## Fired (5 of 6 generated; 1 failed at generation — volley cap 6 spent)

| Take | Vehicle | md5 | Dur | Result file |
|---|---|---|---|---|
| mv5_s06_t2 | mv5_s06_t2_vehicle.txt (GIRL insert for L12 "Yeah, they already understand", song 44.58–46.86; staging from mv5_s06_vehicle.txt — keys, boardwalk, girl beside bike) | 5507f6a2875f90bdcc9aa19a51b08762 | 5.000s | takes/media-generation-mv5-s06-t2-0-56b51eff-6c16-4116-831a-32758fec4807.mp4 |
| mv5_s21_t4 | mv5_s21_t4_vehicle.txt (GIRL insert for L82 "If the sky turns gray", song 158.06–159.1; bridge staging from mv5_s21_t3_vehicle.txt — sun returning, boardwalk) | 25bf777120d14118cfa4b44ef2b2475c | 5.000s | takes/media-generation-mv5-s21-t4-0-6f29ea82-ea90-4ed0-a097-2899e65843d1.mp4 |
| mv5_s21_t5 | mv5_s21_t5_vehicle.txt (GIRL insert for L84 "We lean right back", song 160.24–161.36; same bridge staging/rules as t4) | ce336b3e576330d7d6f3f5f433a0e2bd | 5.000s | takes/media-generation-mv5-s21-t5-0-6451f3bf-b49f-4c74-9ee9-e140fac0aa4a.mp4 |
| mv5_s21_t6 | mv5_s21_t6_vehicle.txt (GIRL insert for L86 "You and me, same pace", song 162.46–163.58; same bridge staging/rules as t4) | 3ff0dc823b84ac0b945c1a70e5160a32 | 5.000s | takes/media-generation-mv5-s21-t6-0-dcbee773-d9ba-4e10-b74b-96f4c9b85ff7.mp4 |
| mv5_s21_t7 | mv5_s21_t7_vehicle.txt (GIRL insert for L88 "Nothing to prove", song 164.9–165.88; same bridge staging/rules as t4) | 81663fbac6114f35f920a9f77049209f | 5.000s | takes/media-generation-mv5-s21-t7-0-b3e0f250-0266-499d-8041-626e01151c19.mp4 |

## NOT fired — mv5_s07_t2 (GIRL insert for L15 "One small look from you", song 51.46–52.80)

`media.generate_video` returned `integrity_check_failed`. Per the parent's
instruction (developer bar on repeating the request, including with changed
arguments or through another tool/endpoint), NO retry was made. Vehicle file
`mv5_s07_t2_vehicle.txt` exists; no take file exists. S07 stays with s07_t1
(all-CAT) for L15 unless the parent decides otherwise; assembly fallback is a
two-anchor placement of the CAT take (S15/S20 style) or donor cover.

## QC summary (full verdicts: work/qc_v12/qc_v12_verdicts.md)

- s06_t2: **KEEP**. Line sung once, complete, both decodes agree (0.0–2.6s);
  ratio 0.88 vs song 2.28s (in band); app-start fit slope 0.69 (playback 1.44x,
  within the 1.5x cap), median |resid| 0.04. Frame rule PASSES (vocal mean 1.11,
  run 2). Picture: girl mouth open at 0/1/2s, closed after; cat mouth closed
  throughout; locks hold; no text. Disclosed nit: "they" ~0.35s late under the
  single 0.88x warp (head words spread: take "Yeah→they" 0.76s vs song 0.1s).
- s21_t4: **REJECT (PACING)**. Line sung once (unprompted "If the sky turns grey";
  prompted 2nd delivery is a hallucination — zero-duration words, RMS tail
  baseline). Span 2.94s vs song 1.04s → ratio 0.35, clear miss; fit slope 0.30
  → playback 3.3x, beyond the rescue cap. Frame rule PASSES; picture PASSES
  (girl sings, cat silent). Next: volley 13 reroll on PACING (brisk, finish by
  ~1.5s); if it lands ≥2.5s, L82 goes structural.
- s21_t5: **REJECT (PACING)**. Line sung once (0.0–3.78s); ratio 0.30, clear
  miss; fit slope 0.20 → playback 5x. "We" held 1.92s (delivery defect on top
  of the pace miss). Frame rule PASSES; picture PASSES (girl sings, cat silent).
  Next: volley 13 reroll on PACING/DELIVERY (brisk, no held first word, finish
  by ~1.5s); if it lands ≥2.5s, L84 goes structural.
- s21_t6: **REJECT (PACING)**. Line sung once (unprompted confirms; prompted
  2nd/3rd deliveries are hallucinations — zero-duration words). Span 4.44s vs
  song 1.12s → ratio 0.25, clear miss; fit slope 0.11 → playback 9.4x. Extra
  defects: 0.7s mid-line gap, quiet head (RMS 0.004–0.006 at 0–1.0s). Frame
  rule PASSES; picture PASSES (girl sings, cat silent). Next: volley 13 reroll
  on PACING (brisk, no mid-line pause, finish by ~1.5s); if it lands ≥2.5s,
  L86 goes structural.
- s21_t7: **KEEP (grey rescue)**. Line sung once, complete, both decodes agree
  (0.0–1.5s); ratio 0.65, grey zone. Re-measured per the grey rule: the two
  song grids disagree on L88 (app shifted it ~0.6s later, compressed; dt_start
  up to +0.74 on "to"). App-start fit slope 0.44, residuals ≤0.08; v1-grid fit
  slope 0.89 → playback 1.12x, IN BAND, max resid 0.27 ("to"). Assembly places
  by the v1-grid starts with "to" +0.27s disclosed; the master gate re-checks
  L88, and if it fails, L88 falls back to donor cover. Frame rule PASSES
  (vocal mean 0.959, run 2). Picture PASSES (girl sings, cat silent; red sun
  hat variant like t4).

## Volley 12 result: 2 KEEP / 3 REJECT (s07_t2 not fired). Cumulative: 24 KEEP / 40 REJECT
(effective 23 KEEP: 21 + s06_t2 + s21_t7; S28 t1 KEEP superseded by the audit).

## Assembly notes (carried forward)

- S06: t2 KEEP — cut the girl in for L12 only; s06_t1 keeps L10/L11.
  Disclosed: "they" ~0.35s late under the single warp; two-anchor option.
- S07: t2 NOT FIRED — s07_t1 (all-CAT) stays for L15; two-anchor placement or
  donor cover at assembly.
- S21: t7 KEEP (L88, grey rescue — place by v1-grid starts, "to" +0.27s
  disclosed, master gate re-checks). t4/t5/t6 REJECT — L82/L84/L86 await volley
  13 PACING rerolls; if those land ≥2.5s, the three bridge GIRL lines go
  structural (t3 CAT picture + captions, "not a mouth-sung slot"). L83/L85 keep
  s21_t3's picture; L87/L89 stay donor-covered.
- S28: unchanged — STRUCTURAL (t3 tail cover). No further S28 generation.
- Prompted-repeat adjudication (t4, t6): prompted second/third deliveries with
  zero-duration words + baseline RMS tail are hallucinations, not repeat
  defects — same class as S19a t2 and S28 t2–t4.

## Evidence

- work/qc_v12.py + work/qc_v12/qc_v12_results.json + work/qc_v12.log
- work/qc_v12/qc_v12_verdicts.md (full per-take verdicts)
- work/qc_v12/sheets/*_sheet.png (1 fps contact sheets, 0–4s per take)
- work/gemini_takes_verdicts.md (audit brief that opened this volley)
- Vehicle files: mv5_s06_t2_vehicle.txt, mv5_s07_t2_vehicle.txt,
  mv5_s21_t4_vehicle.txt, mv5_s21_t5_vehicle.txt, mv5_s21_t6_vehicle.txt,
  mv5_s21_t7_vehicle.txt (project root)
