# MV-23 "Call Me Ranch" — TAKE HISTORY

G7 = word-set overlap |A∩P|/|P| (take ASR screened p≥0.5, seg avg_logprob ≥−1.0; P from plan sheet text; both sides normalized for the documented mishear class rich/range→ranch, dressing→dressin). Ratio = song sung span / take sung span (phrase-warp k before grey-zone judgement; band 0.80–1.25, grey 0.60–0.80 / 1.25–1.60, slow cap 2.0×).
Motion = fps=4 gray frame-diff on the raw take (mean / max near-dup run; fail if run ≥1.0s during words or mean <0.5).

## Volley 1 (2026-11-20) — hook test + openers
| Sc | Take | md5 | G7 | Ratio | Motion | Eye read | Verdict |
|---|---|---|---|---|---|---|---|
| S01 | t1 | 2231ba94f65c7eb9a0679330cafc41cc | 0.900 → 1.0 hand-check | 1.017 | 27.51 / 0.0s | Mid-stride hat-tip entrance, mouth open on lines, adults behind, no text | KEEP |
| S02 | t1 | c9e713421dee82aedaef2810db228a44 | 1.000 | 1.425 (grey, slow) | 15.88 / 0.0s | Triple-mirror turns, bolo/cuff adjustments, preen tail | KEEP (grey warp disclosed) |
| S03 | t1 | 3d00f331cfb81723ae1e560802884958 | 1.000 | 0.882 | 14.14 / 0.0s | Tilly tapes Ranch's chest, chest puffed, singing to camera | KEEP |
| S07 | t1 | 7b47c1849f242b874af6b72271e12a1e | 0.900 | 1.102 | 16.64 / 0.0s | Hat-toss game behind, Ranch leans singing, lands his toss late in take | KEEP |
| S08 | t1 | fc547a0f00f0765f9c255902ddbf34c6 | 0.938 | 0.961 | 13.58 / 0.0s | HOOK TEST PASS: full runner strut, shop clapping, identity on-lock | KEEP |
| S15 | t1 | 083b5bab8a9d5876e0ee60586d884a6f | 0.938 | 0.935 | 22.22 / 0.0s | Ranch sings from balcony rail; Pearl & Cole strut the runner below | KEEP |

Hand-check overrides (G7 protocol):
- S01: screened set missed "ranch" (sung at p=0.494, just under the 0.5 screen) and the second "dressin'" (ASR p=0.006 confidence artifact); the segment text reads the full sheet block "Call me ranch, I be dressin', I be dressing, I'm the best, yeah." Override → 1.0.
- S07: screened 0.900; raw ASR garbles parts of the repeated try/higher phrases ("you can you Try, I Higher") — a repeat-phrase ASR artifact on a take whose segment text carries both full pre-chorus lines. Stands at 0.900 (≥0.5, no override needed).

Cross-pair check (volley 1): no take's overlap vs a different scene's planned set exceeds its own-scene score (hook scenes S08/S15 share the chorus word set by design — sibling Jaccard ≥0.5 class; both contain their own scenes' full sets).

Spend after volley 1: 6/40. Refusals 0. 429s 0.

## Volley 2 (S04, S05, S06, S09, S10, S11) — QC complete (qc_t1_v2.log, qc_t1_v2b.log)
- S04 t1 `2fc062d7bf0d8f5a6073027e0f8fbfc5`: G7 1.0, ratio 0.577 (extreme warp, disclosed — MV-22 shipped 0.513), motion clean. Eye: ribbon pin reads, identity on-lock. KEEP.
- S05 t1 `66b8b735f2d5c3195eca172fa27b84f9`: G7 0.900, ratio 0.770 (grey-zone edge). Eye: register pop + bill fan read. KEEP.
- S06 t1 `7fbe983f8c654f16b271897a8af31000`: G7 0.900, ratio 0.709 — EYE G1 FAIL: singer's face/hair change mid-take (back half a different, lighter-haired man, no moustache, bolo missing) + tiny red header smudges on calendar pages. REJECTED → rerolled t2.
- S09 t1 `064ca526b0e37aea811038aaadaa83d0`: G7 1.0, ratio 0.913. Eye: boot-shine, identity on-lock. KEEP.
- S10 t1 `6b256eadbe03fba0f207192e645ed336`: G7 0.917, ratio 1.023. Eye: jacket flip, identity on-lock. KEEP.
- S11 t1 `8ef9cf99194aedee8317d3a74b14b742`: G7 0.917, ratio 0.860 — EYE G1 FLAG: suit embroidered with red/blue floral patterns in every frame (rhinestone-cowboy drift, not the plain cream fringed suit). Reroll attempted twice (v2 vehicle, plain-suit emphasis) — generator REFUSED both attempts. Per the refusal rule, no further re-fires: t1 SHIPS with the costume drift disclosed.

## Volley 3 (S06 t2, S12, S13, S14, S16)
- S06 t2 `01c8be2a4477953f785f286f3ce6b363`: G7 1.0, ratio 0.686 (grey-zone). Eye: SAME man in every frame (dark slicked hair, pencil moustache, bolo always present); calendar pages blank with gold stars only, no headers/marks. Identity axis FIXED. KEEP (replaces t1).
- S12 t1 `6f95239b1147cfe49822b67681b2f4e8`: G7 1.0, ratio 0.855. Eye: bottle spin + clean catch read, identity on-lock. KEEP.
- S13 t1 `7ab4a2289286743f01ad78f42aead51e`: G7 0.714 — take ASR drops "You" before "stay late" and truncates the tail. REJECTED for lyric completeness → rerolled t2.
- S14 t1 `866c5ecb588e491ebf3b8774015e6b70`: EYE G1 FLAG — floral embroidery on lapels/sleeves in most frames (same costume drift as S11 t1). → rerolled t2 with plain-suit vehicle.
- S16 t1 `862d4655b7d554e202b0d5051bd5d853`: Eye: fringe shake + spin read, identity on-lock, plain suit; adult seamstress visible in background frames. KEEP-candidate (QC in take_qc.json).

## Volley 4 (S11 t2 REFUSED again, S14 t2, S17, S18, S19, S20)
- S14 t2 `96502dbdf3e2d89dfc122524b9e8d427`: Eye: PLAIN cream suit, no embroidery — costume fixed; staircase rise reads, identity on-lock. KEEP (replaces t1; QC in qc_t2_v4.log).
- S17 t1 `27c310de65b16d71c73cb3fd60608ed4`: Eye: pose chain reads — Tilly/Hank/Cole/Pearl all named adults, Ranch biggest last, singing. KEEP-candidate.
- S18 t1 `0c16c2ebc0edba41a3015f4e6e19f693`: Eye: dressin' relay beats read (hat/boots/buckle/grin) BUT the back half performs the relay on an older grey-bearded man wearing Ranch's suit. → rerolled t2 (same-young-man vehicle).
- S19 t1 `a3f145f4043f695e7288f9f443f53e16`: Eye: golden window hook + turn reveals the celebrating shop, all adults, identity on-lock. KEEP-candidate.
- S20 t1 `3bb09861e6b7a3f6c5422d78c42f6aa1`: Eye: hat rain reads BUT the singer is a different man (light brown hair, no pencil moustache) — G1 identity FAIL. REJECTED → rerolled t2.

## Volley 5 (S13 t2, S18 t2, S20 t2, S21, S22, S23)
- S13 t2 `b8a0d1f610adb866690071dca27baefe`: Eye: identity on-lock, cufflink/bolo action + mirror read. KEEP-candidate (QC decides vs t1).
- S18 t2 `602aa6e529726f0948676da2e8ad9dc3`: Eye: relay now on the young dark-haired man throughout; minor embroidery on jacket back in one shot (wordless cutaway). KEEP (replaces t1).
- S20 t2 `57f6ffad65dd020dbcdc84c9c35bd643`: Eye: the RIGHT man (dark slicked hair, pencil moustache), hat rain + Stetson catch read, crowd all adults. KEEP (replaces t1).
- S21 t1 `3c8103aa9c02cb24a9be45198511b360`: Eye: final strut — whole shop in line on the runner behind Ranch, all adults, identity on-lock. KEEP-candidate.
- S22 t1 `a23903f2aa29c60231cd8438f2c10df5`: Eye: encore bow reads (deep bow mid-take, rises grinning). KEEP-candidate.
- S23 t1 `f28d97df3e545d4b4451e59cc0fecf93`: Eye: last stitch — Tilly with pincushion, Ranch reclined singing, wink at end; mild turquoise swirl embroidery on his jacket (nit, disclosed). KEEP-candidate.

## Volley 6 (S24)
- S24 t1 `d0c558ca56e5304ec22c58f02ddb5094`: Eye: hat-on-peg bookend reads, evening light, ends held on the hat; tiny "SINGER" brand plate on prop sewing hardware (incidental real-world prop branding, nit). KEEP-candidate.

Spend after volley 6: 29/40 landed. Refusals: 2 (both S11 t2 attempts). 429s: 0.
