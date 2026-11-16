# MV-18 — TAKE HISTORY (reconciled 2026-11-13 ~17:15 EST)

Template: work/vehicles/TEMPLATE.md. All takes 1248×704 (tool
native); conform scales to 1280×720. G7 = screened take-ASR word-set
overlap vs scene-plan words (≥0.5 ship; all sung keeps are 1.0).

## Pilot
| Take | Scene | md5 | Verdict |
|---|---|---|---|
| mv18_s01_t1 | S01 hook | ac7536affeed90e8aa424133a23ac5a8 | KEEP — sings hook 0.00–6.3 (song 6.46, ratio ~1.03), G7 1.0, MOM leans in mouth-closed |
| mv18_s03_t1 | S03 sigma (MOM) | fb231e24e42aeb262e1d7e45f25d6c25 | KEEP — "What's a sigma" 1.22–2.9, G7 1.0, glasses-drop + tilt land. FLAG: background SON reads younger (small in frame) |
| mv18_s11_t1 | S11 hook | 606c01d25fa16beb1af73ffdcf6b09cd | REJECT — G2: handwritten words on the notebook page |

## Volley 1
| Take | Scene | md5 | Verdict |
|---|---|---|---|
| mv18_s11_t2 | S11 hook | 8ab376b23bc25e28cb08ad1f6f74c4de | KEEP — page blank, hook 0.00–6.1 (song 6.20), G7 1.0 |
| mv18_s02_t1 | S02 lean-in (wordless) | 97febbef0c8d2a3df0105daf52a4bf14 | KEEP — lean-in arc lands, ASR empty (p≤0.05), wordless G7 PASS |
| mv18_s05_t1 | S05 walk hook | 5c0c3b579bf82270672499fd085af95a | KEEP — hook 0.00–6.5 (song 5.88, 1.11×), G7 1.0, walk+arrival land |
| mv18_s06_t1 | S06 screen turn | 519baffe271e1d96b0ae3b7c778d84fa | KEEP — line 0.00–5.3 vs song 2.92 → 1.83× speedup (within MV-17's shipped 1.904 precedent), G7 1.0 |
| mv18_s07_t1 | S07 magnifier | 509c2b562caeb68ef29382f9ba3ec2a9 | KEEP — line 0.00–4.0 (song 3.10, 1.30×), G7 1.0, huge-eye gag lands |
| — | S04 sung vehicle | — | NOT GENERATED (generation refused) → restaged as S04i insert |

## Volley 2
| Take | Scene | md5 | Verdict |
|---|---|---|---|
| mv18_s04i_t1 | S04 facepalm insert | 5b96745ee4327ea8f3f97ad5c692e596 | KEEP — face-in-hands from ~1s, mouth never visible, ASR empty. Use the drop portion (motion) at conform |
| mv18_s08_t1 | S08 backpedal | 83183b29f8c528b4d0ec5127b6910eb9 | SPARE — full line G7 1.0 but event failed (stood gesturing); superseded by t2 |
| mv18_s09_t1 | S09 hunt-and-peck | b4c4a774460d9a6eb802d652a46fde82 | KEEP — line complete, G7 1.0, triumph arms land |
| mv18_s10_t1 | S10 pose chain | e7d89ca5799c8f90bd2efdc084730234 | KEEP — both phrases G7 1.0; stop-hand warm → point cool-blue (grade shift stronger than planned, reads as the PC tension beat) |
| mv18_s12_t1 | S12 pupil | 73fd0803d0298ef0cf13467241d6f8c5 | KEEP — hook 0.00–7.0 (song 6.32, 0.90×), G7 1.0, copycat chain lands |
| mv18_s13_t1 | S13 double ask (MOM) | 7883a0997f6f4dafa99a4877aa2cab3d | KEEP — sigma ×2 (0.00–1.6, 2.02–3.7), G7 1.0, lean + wince land |

## Volley 3
| Take | Scene | md5 | Verdict |
|---|---|---|---|
| mv18_s08_t2 | S08 backpedal | 32e4a34a75af61be3bdabd43862857ac | KEEP — full line G7 1.0; retreat across the room to the bookshelf reads (literal heel-first backpedal + shelf bump only partially land — disclosed); phrase 0.00–5.6 vs song 2.98 → 1.85× speedup (within shipped precedent) |
| mv18_s15_t1 | S15 tea offering | 401163e0260d706cc849f7d11f615689 | KEEP — hook 0.00–7.7 (song 6.48, 0.84×), G7 1.0, mug offering lands (he reads couch-edge seated, not floor — staging variant, fine) |
| mv18_s16_t1 | S16 broadcast (MOM) | d4897a5b4006783e06a9ef6abc29357e | KEEP — sigma ×2 into the phone call, G7 1.0; grade darker/evening (section-break read, fine) |
| mv18_s17_t1 | S17 micro-event ECU | 35bf7a49c317e0ea60b3755a75fb993e | KEEP WITH FLAG — deadpan→grin-crack arc lands perfectly; take-ASR hears only ONE "I regret it" (the repeat is sung through the breaking smile; G7 set-overlap 1.0). Optional t2 (articulation axis) listed in VOLLEY_PROGRESS resume notes; parent eye-check advised |
| mv18_s18_t1 | S18 dog tilt | 9d72eb6213bc6a523348bfe51575f748 | KEEP — line complete G7 1.0, staged head-tilt to full tilt lands |
| — | S14 sung vehicle | — | NOT GENERATED (generation refused) → restaged as S14i insert (Volley 4 doc) |

## Volley 4 (resumed 2026-11-14 — budget relented; coordinator 34ec7846)
| Take | Scene | md5 | Verdict |
|---|---|---|---|
| mv18_s14i_t1 | S14 freeze insert (wordless) | ec4305cb6eb62c33952aa8de77a47c4f | KEEP — SON seated-frozen on the couch, mouth closed and still throughout; MOM rises, moves around him studying him with her phone, flash pops in the back half (statue-study variant of 9.1 The Freeze — event lands). G2 PASS at full res (no text). G7 wordless: take-ASR hallucinated "Thank you." (segment avg_logprob −0.951; ambient-bed RMS −51…−38 dB, no speech) — HAND-CHECK OVERRIDE per wordless-hallucination rule (MV-14 S14 precedent, −0.959): full-res frames incl. inside the ASR window (1.1s) show both mouths closed; take is wordless. Override logged here; the gate output stands. 120f / 5.000s exact. |

| mv18_s19_t1 | S19 fog window | bfcf955a2e8c5ba50150e6aae2cfc34f | SPARE — INCOMPLETE: sings phrase 1 only ("She put it in the group chat" 0.00–2.64, G7 vs phrase 1 = 1.0; split-half ASR confirms phrase 2 "Now my mentions are a fog" never sung). Fog bloom + window staging land; frame gate PASS. Superseded by t2 (completeness axis) |
| mv18_s20_t1 | S20 chain reaction | f0bc5c705efb5e89aec4e8c926d0a193 | KEEP — full line 0.00–3.22 (song span 2.94 → 1.10×), G7 1.0; MOM thumb-types on a blank phone, warm light pulses travel from her phone across the room toward the hallway/front door; frame gate PASS (mean diff 3.01) |
| mv18_s21_t1 | S21 kettle scream | 976944a0c172228b09303a0ab8ca16c5 | KEEP — full line 0.00–3.50 (song 3.82, 0.92×), G7 1.0; kitchen exile lean, kettle steam builds wisp → plume across the line; frame gate PASS |
| — | S22 retreat (sung vehicle) | — | NOT GENERATED (generation refused) — NOT retried. Span covered at conform by a montage cover (see GATE_LOG disclosure 5) |
| mv18_s23_t1 | S23 the swarm (hook) | 8094133665d7499fbc40eefb1e566773 | KEEP — hook 0.00–6.06 (song 6.36, 0.95×), G7 1.0; printer spits blank pages all line, drift grows until the couch is half buried; pages verified BLANK at full res (G2 PASS); frame gate PASS |

## Volley 5 (fired 2026-11-14 by coordinator 34ec7846; QC completed by recovery coordinator after 34ec7846 died mid-QC)
| Take | Scene | md5 | Verdict |
|---|---|---|---|
| mv18_s24_t1 | S24 paper trail (hook) | 95ff3299e7e8e8557cc21ff92abe2373 | KEEP — hook 0.86–6.70 (song span 6.90, 0.85×), G7 0.92 screened (ASR hears "mum" for "mom" — mishear class, all other 11 words exact); SON follows the printout trail gathering pages, ends holding a fan of them on "regretting it"; pages BLANK at full res (G2 PASS); MOM mouth closed throughout; frame gate PASS (mean diff 6.46, worst run 0f) |
| mv18_s25_t1 | S25 the resurface (MOM) | cfcd9156d24c1a9b170d03c2f3b80194 | KEEP — "What's a sigma" 0.00–2.50 (song span 2.90, 0.86×), G7 1.0; MOM up in the paper drift holding a blank printout, asks brightly; SON at frame edge, mouth closed; pages BLANK at full res (G2 PASS); frame gate PASS (mean diff 5.97, worst run 3f) |
| mv18_s26i_t1 | S26 corpse pose insert (wordless) | a8160d10727d2cfcbb8d914dc75f0855 | REJECT — G2: the floor papers are covered in dense printed text and diagrams at full res (this build's printouts are blank — cf. S23/S24/S25 verified blank). The pose itself lands (SON flat on his back in the papers from ~2.0s, mouth closed, one arm flopped out; wordless G7 PASS — screened ASR empty, lone "Huh?" at p=0.06 / avg_logprob −1.077 filtered; RMS bed −45.3 dB) but the printed pages fail the zero-text gate. Owed t2 (blank-pages axis) |
| mv18_s27_t1 | S27 photo shoot (hook) | 2befe25fd141cda46ed785d2b4c48245 | KEEP — hook 0.00–7.32 (song span 6.02, 1.22×, near the band edge — disclosed), G7 1.0; SON sits up in the paper drift singing while MOM holds the phone up snapping photos of him, flash glow at the top of the phone; phone screen shows the live camera view of SON, no text (G2 PASS); MOM mouth closed; frame gate PASS (mean diff 1.73, worst run 12f) |
| mv18_s28_t1 | S28 bridge asks ×2 (MOM) | 1365bf3f7b4b6d54d6b328d4a0a3d89a | SPARE — INCOMPLETE: sings the ask ONCE only (0.00–1.80; G7 set-overlap 1.0 — the set gate cannot count repeats); dense 2.5 fps eye-read confirms mouth closed in a held smile from 2.0–5.0s — the second ask (L35) is never performed. Cooler bridge grade lands, halftone grain emerges at the tail. Superseded by t2 (completeness axis: BOTH asks) |
| mv18_s29_t1 | S29 self-muzzle | caa883375bfcb529309fd982c65a8a9b | KEEP — both phrases complete ("I don't know what it means" 0.00–2.60 + "I just know he's talking" 4.72–7.34), G7 1.0 vs vehicle lines (0.83 vs grid word set); his own hand rises across phrase 2 and covers his mouth through "talking", eyes wide — self-muzzle lands; 1.63× speedup to the 4.50s song span (speedups uncapped; within S06 1.83× / S08 t2 1.85× precedent); frame gate PASS (mean diff 2.25, worst run 5f). Tool returned 10.000s on the 5s request — use the singing span at conform |

## Volley 6 (2026-11-14 — recovery coordinator, revived after 34ec7846 died; S19 t2 reroll + S30–S34)
| Take | Scene | md5 | Verdict |
|---|---|---|---|
| mv18_s19_t2 | S19 fog window | 6a2184961e5b4bde32cfde079e0c01d2 | KEEP — BOTH phrases complete ("She put it in the group chat" 0.00–1.92 + "Now my mentions are a fog" 2.42–4.40), G7 1.0; fog blooms across the blue window behind him across phrase 2, on "fog"; 1.49× speedup to the 2.96s song span (speedups uncapped, within precedent); MOM mouth closed; frame gate PASS (mean diff 3.90, worst run 1f). Supersedes S19 t1 SPARE |
| mv18_s30_t1 | S30 join-in wave (hook) | 68074cff54bb89174691ab0cb37e3355 | SPARE — hook complete 0.00–5.88 (song span 5.98, 0.98×), G7 1.0, BUT two strikes: (1) frame gate FAIL — 51f / 2.12s near-dup run at 0.00–2.08s under the opening words (halted-photo head, MOTION LAW); (2) event fails — no standing side-step dance at any point (dense 2 fps read): MOM's rhythmic bounce is seated hand-motion only and starts after the line, laughing open-mouthed in the tail. Owed t2 (locomotion + in-motion head axis) |
| mv18_s31_t1 | S31 door reveal (hook) | 5758581218af1888b6fcf5204e9cbd10 | KEEP — hook 0.00–6.30 (song span 6.94, 0.91×), G7 1.0; the dance carries them across the room to the front door, the door opens and the AUNT stands revealed, phone raised, mouth closed; MOM mouth closed; frame gate PASS (mean diff 7.42, worst run 3f) |
| mv18_s32_t1 | S32 cast assembly (AUNT) | e8f177ff9150801af838f1b14e50e38d | KEEP — BOTH asks sung by the AUNT (0.00–1.50 + 2.04–3.30), G7 1.0 count-complete; the three assembled in the hall, MOM nodding mouth closed, SON behind stunned mouth closed; frame gate PASS (mean diff 1.39, worst run 7f). NOTE: tool returned 1152×768 (3:2) on the 16:9 request — centre-crop to 16:9 at conform is safe (subjects centred) |
| mv18_s33i_t1 | S33 sympathy sandwich insert (wordless) | 07e0d20d3510b95a943c0716f0274af7 | KEEP — wordless G7 PASS (screened ASR empty — lone "." at p=0.02 / avg_logprob −1.106 filtered; RMS bed −44.7 dB); SON sandwiched between MOM and AUNT, eyes to the ceiling, mouth closed, while both women pat his shoulders in sync; no mouth moves. NOTE: 1152×768 (3:2) return as S32 — centre-crop at conform |
| mv18_s34_t1 | S34 group hug collapse (hook) | 7d72660f7b4c60c649b3ff9e2afef178 | KEEP — hook 0.00–6.88 (song span 7.54, 0.91×), G7 1.0; MOM and AUNT close in from both sides and fold SON into the hug mid-hook, his face squished between their shoulders, still singing; both women mouths closed; frame gate PASS (mean diff 1.92, worst run 4f) |

## Rerolls (2026-11-14 — coordinator 61cca0f2)
| Take | Scene | md5 | Verdict |
|---|---|---|---|
| mv18_s26i_t2 | S26 corpse pose insert (wordless) | 0af62ca424a796297e76974a024fce93 | KEEP — wordless G7 PASS (screened ASR empty — lone "You" at p=0.047 in a segment with avg_logprob −1.248 filtered); G2 PASS: the floor pages are completely BLANK at full res (the t1 defect is fixed); SON flat on his back in the drift from frame 0, mouth closed, one arm flopped out. Frame gate FAIL on the full 5s only via the near-still tail (24f at the gate's <1.0 threshold, ~4.0–5.0s, after the flop — the corpse lying still); conform uses the flop span ~0.5–2.94s and trims the tail; master zero-still gate verifies the shipped span. Supersedes S26i t1 REJECT |
| mv18_s28_t2 | S28 bridge asks ×2 (MOM) | 8c24e83bc88e0c145cbbdb0484ae0026 | KEEP — BOTH asks complete ("What's a sigma" 0.64–1.88 + "What's a sigma" 2.76–3.88), G7 1.0 count-complete (segment avg_logprob −0.395, all word p ≥ 0.858); cooler bridge grade lands, halftone flatten reads subtly. Frame gate FAIL at native speed (32f near-dup run across the scripted inter-ask pause in a locked-off close-up); conform ships a UNIFORM 1.944× warp of the ask span (holds both ask onsets within 0.05s of the grid — supersedes the phrase-warp framing in the original QC note; new extreme, disclosed in GATE_LOG); master zero-still PASS verifies the shipped span. Supersedes S28 t1 SPARE |

## Volley 6 completion + S30 reroll (2026-11-14 — coordinator 61cca0f2)
| Take | Scene | md5 | Verdict |
|---|---|---|---|
| mv18_s30_t2 | S30 join-in wave (hook) | d3bca227ee9e41d40581aab35b04b9ad | KEEP — hook 0.00–4.56 (song span 5.98, 0.76× slowdown), G7 0.909 ("mum" for "mom" — mishear class, all other words exact); EVENT LANDS: MOM stands and step-touches across the floor, SON resists seated then rises and joins her step for the final words; in motion from frame 0; frame gate PASS (mean diff 7.79, worst run 6f) — both t1 strikes (51f halted head, no dance) fixed. Supersedes S30 t1 SPARE |
| mv18_s35_t1 | S35 lamp confession | 5fa0a1c68d8e9397bf57de2507864c71 | KEEP — "I regret it" 0.00–2.56 (song span 2.18, 1.17×), G7 1.0; the quiet confession reads (eyes closed, opens on the words, soft settle; mouth visibly open on "regret"). NOTES: the tool returned a medium shot, not the 85mm ECU asked; frame gate FAIL (mean diff 0.51, worst near-dup run 56f — the quiet locked-off staging); conform applies the MV-17-precedent slow push-in, which lifts the motion floor and tightens the framing toward the ECU intent; disclosed in GATE_LOG |
| mv18_s36_t1 | S36 final ask + yeah | a39ada7dd877802912362a8f3e75abf7 | KEEP — MOM ask "What's a sigma" 0.00–1.66 (G7 1.0), then SON "Yeah" 2.42–3.02 — strictly sequential, never both mouths at once; his thumb rises into a thumbs-up on his word; final frames settled warm on the couch, rhyming S01; frame gate PASS (mean diff 1.52, worst run 5f) |

## All 36 scenes covered — conform / assembly next
Every scene has a KEEP take or a resolved cover: S22's span is
covered at conform by a montage cover (sung vehicle refused,
never retried — see Volley 4); S26's span is covered by the
S26i t2 wordless insert over the montage cover. Spares on disk:
S08 t1, S19 t1, S28 t1, S30 t1. Rejects: S11 t1, S26i t1.
