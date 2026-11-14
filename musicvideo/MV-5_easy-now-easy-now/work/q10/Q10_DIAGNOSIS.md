# MV-5 Q10 — Diagnosis (frame-verified 2026-11-13 ~02:55 EST)

Delivered master under repair: `masters/mv5_easy_now_easy_now_16x9_lyrics.mp4`, md5 a3e659220dd2870ab57c20cad198567e, 4954f, 206.417s. User verdict 2026-11-13 ~02:31 EST: "bad timing, cat talking when she is, low grab for song intro, this one is the weakest." Gates passed; the master is still wrong. Owned, not defended.

Grid: `work/lyrics-redo/grid_merged.json` (118 lines / 548 words). Caption .ass VERIFIED faithful to the grid (548/548 events; highlighted word + time match a grid word in every case; the 13 apparent mismatches in a first pass were my checker's substring bug). The caption text is right — the PICTURE is wrong. "Lyrics on screen are wrong" = mouths off the words, not wrong caption text.

## Defect 1 — BAD TIMING (picture placed on the old grid; lyrics redo swapped only the .ass)

- **Intro (S01/S02):** leader is the CAT mid-yawn, near-still (frames 0.5 / 1.9 near-identical); I05 CAT insert 0.56s early (10.04 vs song 10.60); I07 insert mouths "Easy now" while the song sings I08 "Till the morning comes" (frame 15.5: CAT mouth wide open, caption "Till the morning comes"). I06/I07 were never sung (dropped from grid).
- **S04 (L01–L05):** frame 22.96 — CAT mouth CLOSED, eyes half-shut, while the song sings "Salt" and the caption is on L01's "boardwalk". Take sings Bare→Salt in 2.12s vs song 0.96s; L02 mouth 1.1–1.5s late. No warp fixes it (per-word needs 2.21x then 0.58x). → fresh take.
- **S06 L11:** take sings "You nodded at the waves like" in 2.76s vs song 0.98s (ratio 0.36). → fresh brisk take.
- **S07 L16:** take sings the line in 2.44s vs 4.94s window; "And" lands 1.59s late (frame 54.4: CAT barely starting "And", caption on "head"). Per-word warp needs 0.43x — below the 0.5x floor. → fresh held take.
- **S12 L41/L43:** frame 96.0 — girl mouthing OPEN during the CAT's L42 ("Like a hand drum roll"). L43 take 3.76s vs 1.68s song (ratio 0.45), overruns 2.32s into CAT's L44. L41 fits a 1.25x re-warp. → fresh brisk L43 take + L41 re-warp.
- **S20 L80/L81:** frame 157.2 — girl mouth WIDE OPEN singing "breeze" 0.31s into the CAT's L81 ("And the bass moves slow"), CAT mouth shut. Fix by reassembly: re-anchor S20 phrase −0.35s (breeze ends 156.98 < L81 head 157.02). No take.
- **S11 L37–L40:** take pauses 1.4s where the song has none; "Socks" 2.18s late. Frame 89.2: market montage, girl mouth closed — no wrong-mouth, just a mistimed take. Fix by reassembly: L38 montage + L39/L40-tail re-warp. No take.
- **S23 L96:** "No" 0.68s late; "run" uncovered (take has no "run"). Fix by reassembly: re-anchor phrase to 174.44, cut at "to", CAT reaction cover for "run".
- **S24 R2:** take mouth opens 0.76s before hook L99. Fix by reassembly: per-line re-warp (1.33x/1.55x).
- **S25 L104:** CAT mouth CLOSED at the line's onset (frame 182.8; girl carries the hook picture, CAT's lead line has no mouth — no take of the CAT singing it exists). → fresh take (program item).
- **Tail L108–L110:** chant is continuous 193.20–201.56 (9 pairs, 0.93s/pair, NO gap — v4's "verified gap" was an old-grid artifact). Frame 198.5: girl singing her pair correctly. L110 (CAT, 203.84–205.62): s28_t1 re-warped 0.645 setpts lands words within ±0.32s — reassembly. L109 (GIRL, 201.74–203.10): no girl "Till" take exists; frame 201.8 shows the CAT MCU mouth-closed as cover — swap to a girl-listening shot in reassembly (disclosed structural).
- **S15** likely fine (held vowel covers new end 119.14). **S16** shifts ±0.2s. **S17** inserts L69/L70 ~0.5–0.66s late → re-anchor.

## Defect 2 — CAT TALKING WHEN SHE IS (singer-ownership violations, frame-verified)

- **S06 L12 head, 44.58–45.36 (0.78s):** CAT take mouths "at / the / waves" while the GIRL sings L12 "Yeah, they already understand". Frame 44.6: CAT mouth open mid-word (tongue tip), girl mouth closed. (Frame 45.2 catches it between words, nearly closed — the articulation is real but intermittent.) Fix: fresh brisk L11 take ending by 44.58 + re-anchor the EXISTING KEEP girl insert s06_t2 (md5 5507f6a2…, 5.0s) from 45.36 to 44.58.
- **S07 L15 head, 51.24–51.46+:** CAT mouth WIDE OPEN singing "One" while the GIRL sings L15 (frame 51.3: CAT teeth/tongue visible, girl eyes closed, mouth shut). Blatant. The girl insert s07_t2 was NEVER FIRED (integrity_check_failed, no retry per developer bar). Fix: donor cover — s07_t1 take-time 6.25–7.52s (CAT mouth-closed gap before "And") under L15, disclosed structural. A restaged girl insert is the 7th take — OVER CAP, see below.
- **Mirror defects (girl mouthing CAT lines), reported honestly:** S12 L42 (frame 96.0), S20 L81 head (frame 157.2, 0.31s), S11 L37 (girl pre-word head — verify mouth closed), S16 base inter-lines L58/L60/L62 (GIRL base, "transitional-open" at L64, disclosed in v4).

## Defect 3 — LOW GRAB FOR INTRO

First 1.67s is a near-frozen yawning CAT; then a long S02 cutaway (10.04–18.64, mouths closed) with two short CAT inserts, one mouthing wrong words (I07 over I08). Fix: motion from frame 0 (riding montage 0–1.40, bike rolling + bell glint), hard cut to CAT MCU singing I01 at 1.40; fresh CAT take for I08 held (12.72–17.52); delete I06/I07 inserts; re-anchor I05 insert to 10.60.

## Volley fired (cap 6 — ALL SIX)

1. q10_i08 — CAT "Till the morning comes" held, 5s (intro)
2. q10_s04 — CAT L01–L05 verse, 10s (L01 fast in first second)
3. q10_s06_l11 — CAT "You nodded at the waves like" brisk, 5s
4. q10_s12_l43 — GIRL "I forgot the list, forgot the bills" brisk, 5s
5. q10_l104 — CAT "We're good where we are", 5s
6. q10_s07_l16 — CAT "And my whole head replays" held, 5s

Image refs: CAT takes ← work/q10/frames/f_15.5.png; GIRL take ← work/q10/frames/f_96.0.png.

## OWED — 7th take, over cap (do NOT fire without a cap lift)

- **Restaged S07 L15 GIRL insert** ("One small look from you", 51.24–52.80). Original vehicle s07_t2 failed integrity once; a restage (girl alone, no CAT in frame, different composition) is the sanctioned path per the skill (retire + restage, never a third reroll of the same vehicle). Until it fires, L15 rides the donor cover (disclosed structural: no sung picture for the girl's line).

## Reassembly-only fixes (after the volley lands)

S01 per-line re-warp + intro re-cut · S02 delete I06/I07, I05→10.60 · S06 L12 insert s06_t2→44.58 · S07 L15 donor cover + L13–L14 re-anchor · S11 L38 montage + L39/L40 re-warp · S12 L41 re-warp (1.25x) + L44 cover · S17 re-anchor L69/L70 · S20 re-anchor −0.35s · S23 re-anchor + "run" CAT-reaction cover · S24 per-line re-warp · S25 L104 fresh take in · tail chant montage on the 0.93s pair beat + L109 girl-listening cover + L110 s28_t1 re-warp (0.645 setpts) · L102 "drift" disclosure STANDS (unresolved tie, sheet+GEM) unless measurements resolve it.

## Gates (on the delivered master, per brief)

Exact frame count · SEI crf=18.0 · audio agreement measured · motion audit (no new frozen runs during words) · full-res burned-kinetic frame reads. House libx264 CRF 18, yuv420p, 1280×720, 24fps, faststart, track audio sole master audio AAC 48k stereo; chat copy ≤50 MB, AAC copied. No commit. No delivered flag (parent writes it).

## Addendum — corrections, 2026-11-13 ~03:30 EST (cap-lift take landed)

- **L15 / s07_t2 — the "NEVER FIRED" line in Defect 2 was WRONG.** TAKE_HISTORY line 165 corrects line 154: volley 15 fired a FRESH s07_t2 staging (md5 39ba0cf6, REJECT PACING but picture PASSES) and it IS v4's L15 picture (build_v4_plan.py S07: s07_t2 sf0 warp 0.5234 out 32, dst 51.47–52.80). The defect mechanism is a 0.23s-LATE insert head, not a missing take: song L15 starts 51.24 but the girl insert starts 51.47, so 51.24–51.47 shows s07_t1's tail at take-time ~4.88s — 0.04s after "fade" ends, mouth still open — while the caption highlights the girl's "One". The defect is real; the mechanism is the late head.
- **Donor-cover span correction:** s07_t1's true mouth-closed gap before "And" is 6.88–7.52s (f165–180). The 6.25–7.52s span quoted in this diagnosis and the ledger contains "from" (6.12–6.38) and "you" (6.38–6.88) — it would have shown the CAT mouthing L15's own words. Do not use 6.25–7.52s as a mouth-closed cover.
- **Cap lift GRANTED by parent ~03:23 EST; restaged L15 take fired + KEEP** (ledger): girl alone, no CAT, 5/5 words, sings in 2.46s vs song 1.56s, single phrase warp 0.6341 (1.58x), One→51.24, you ends 52.80. Goes into v5 for L15. s07_t2 is retired for L15 (pacing-rejected; per-word warps to 0.36).
