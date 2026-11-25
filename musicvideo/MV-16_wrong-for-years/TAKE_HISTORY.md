# MV-16 — TAKE HISTORY (ledger of record; updated 2026-11-13)

Verdict key: KEEP = ships · SALVAGE = ships with assembly chunk
reorder · REJECT = does not ship · PENDING = ASR verification in
flight. Text verdicts are vs the PERFORMED grid
(work/analysis/grid_lines.json), verified from take-ASR JSONs on
disk (work/swing/*_words.json) — never from delivered log text.

| Take | Scene | md5 | Verdict | Reason |
|------|-------|-----|---------|--------|
| mv16_s01_t1 | S01 | 514528d8b24154a89d1df58bd59f7709 | REJECT | G1 style: photoreal, wrong face (vehicle had no anime lock). Words exact, G7 1.00. |
| mv16_s01_t2 | S01 | a6f0ab603088f09f2c145f4a9f8afc92 | REJECT | Anime ✓, words exact (G7 1.00) but delivery front-loaded: 3.4s closed-mouth posing mid-trio (frames 5.0/7.0), L03 lands 7.08–8.28 vs song 3.82–5.24 — outside warp caps for the hook slot. |
| mv16_s01_t3 | S01 | 992770a790c2bf98cd7efed1e9cceafa | KEEP | Anime ✓ frame-0 peak ✓ words exact, continuous delivery 0–6.5s, phrase warps in band. SHIPS for S01. |
| mv16_s01_t4 | S01 | f88234130e3711c3e734dfa899c3750a | REJECT | Pacing alternate; L03 drags worse than t3 (span 0–7.18+). t3 preferred. |
| mv16_s02_t1 | S02 | 468cd51321de0aea0af4f5bc9b4223e0 | KEEP | Trio exact; friends nodding, mouths closed (frame 0 read ✓). |
| mv16_s03_t1 | S03 | e01801c2f06cb87428f390f548d11db1 | SALVAGE | Right word set, rotated order (WFY/still/WFY vs song WFY/WFY/still). Assembly chunk-reorders lines 8/9. Head-grow frames partially verified (grow not visible at 1.0s sample — event-read at conform). |
| mv16_s04_t1 | S04 | 555b96d8d26dddf19caffed937e19323 | REJECT | Sang sheet rotation text; song span is the trio + Hey. (Shout staging itself verified by eye at 6.8s.) |
| mv16_s04_t2 | S04 | 467d2ca52c8d4722b5e7dffc79799822 | KEEP | Trio exact, span 0–5.8; disco-ball + shout staging carried from t1's verified read (tail frames re-checked at conform). |
| mv16_s05_t1 | S05 | 10d3dc555747ae1fd1b5bf5efbedce9f | REJECT | G1 style: photoreal. Words G7 0.90 (wrote/rode homophone). |
| mv16_s05_t2 | S05 | 1043c3de23aeb4a0092b514756e3f470 | REJECT | CORRECTED AT CONFORM (was pilot-KEEP): the GENERATOR drifted — take sings the friends' lines ("Friends in the back just nodded and let it ride") over S05's belted-car lines L14–L16. Vehicle text was correct; delivery wasn't. G7 in the pilot era compared against the sheet-based plan and missed it. Replaced by t3. |
| mv16_s05_t3 | S05 | d2784618d45636fa372b46c2cd47d89f | KEEP | Correct lines delivered ("Belted the whole chorus in the car / Like I rode it / Yeah") — rode=wrote homophone override. Foreground-verified JSON. SHIPS for S05. |
| mv16_s06_t1 | S06 | f4ea478ccb565486857137250feeb470 | REJECT | Sang sheet line 2 ("like they knew it too"); performed line is "And let it ride". |
| mv16_s06_t2 | S06 | fa28df47911f66ea1e9ff9526d19e003 | KEEP | Performed text exact + (what) thrown (doubled — first instance used). |
| mv16_s07_t1 | S07 | 0a4de9825a23c3f57b3f8f51fced5ba8 | REJECT | Sang sheet quatrain; performed quatrain differs (only "screen says different" matched). |
| mv16_s07_t2 | S07 | 67f5a6397088ca05c13654b66d65cdb6 | KEEP | Performed quatrain exact, span 0–8.04 vs song 9.38 (mild slow warps). |
| mv16_s08_t1 | S08 | 7ad75983d8b2d9bf0b77efdaeedb658f | REJECT | Sang sheet PC (wrong/young/loud/kept); performed PC is wrong×2/kept×2. |
| mv16_s08_t2 | S08 | 52bdc826d444476a5b44cebb24c22b3b | KEEP | Performed PC exact, span 0–7.36 vs song 5.16 (phrase compression ≤ ~1.6×). |
| mv16_s09_t1 | S09 | 533dfefbd8ab90f2d0ecd0c897a8e048 | KEEP | Trio exact ("stop me" = ASR ear-slip); PEEL 1 verified on frames (hawaiian on by 6.5s ✓). |
| mv16_s10_t1 | S10 | 2a1e1f9ebe8e30730fdd2083c2c00f55 | KEEP | Vocalise + trio exact; personal-weather event verified (cloud rains only on HOST, her mouth closed ✓). Take spreads trio (span 0–9.28) — phrase compression at conform. |
| mv16_s11_t1 | S11 | 6288d0cd66d06188d4cfc41c2af4320b | SALVAGE | Vocalise + right word set in rotated order (WFY/still/WFY vs WFY/WFY/still). Assembly chunk-reorders. |
| mv16_s12_t1 | S12 | 0f3ee5268078cc52d08ee7c5c59aa755 | REJECT | Sang rotation text; song span is the trio. |
| mv16_s12_t2 | S12 | 17106616d6d57d4fd657075242a73a74 | KEEP | Trio exact (extra NSM repeat in tail — first pass used). |
| mv16_s13_t1 | S13 | 73487deb90db1b0499a033bc4a46e4b3 | KEEP | POST chant exact (NSM×2/WFY×2); blank-wall word-chase surface verified on frame ✓. |
| mv16_s14_t1 | S14 | 67d7703ce286c31ab08a2eaba8c5e66c | REJECT | Sang sheet lines ("Lights in my face / Wrong from the jump"); performed line 2 is "And the room starts to notice". |
| mv16_s14_t2 | S14 | efc3081fd8e0737867d0b01546e09896 | KEEP | Performed text exact + "Yeah!" ✓. |
| mv16_s15_t1 | S15 | fa899b9c7ef5574ea9df77438e18fc18 | REJECT | Sang sheet quatrain; performed V2 lines differ entirely. |
| mv16_s15_t2 | S15 | c417c42e868509a77c060c0b700fd0df | KEEP | Performed lines exact, span 0–8.06. |
| mv16_s16_t1 | S16 | 13af362e85bda6274cad6e55eca367f0 | REJECT | Sang sheet lines ("No shame in it…"); performed is "(uh) / Ten years deep / And I'm not rewriting it now". |
| mv16_s16_t2 | S16 | 2a58bfc4d70e8acddf722e0bd2acf9be | KEEP | Performed text exact ("Ten years deep, and I'm not rewriting it now"), span 0–5.36 vs song 3.68 (phrase compression ~1.46×). (uh) pickup not in take ASR — folded into head chunk, mouth-checked at conform. |
| mv16_s17_t1 | S17 | c6f4bd6d072894d39ed033d3a374b19d | REJECT | Sang sheet PC; performed PC is wrong×2/kept×2. |
| mv16_s17_t2 | S17 | 33c68e8900a54b950fb0c1419d284577 | KEEP | Performed PC exact (wrong×2/kept×2), span 0–6.96 vs song 4.72 (phrase compression at conform). |
| mv16_s18_t1 | S18 | a7b842867c0e91f642c879be2ec03d77 | KEEP | Trio exact; PEEL 2 verified (gold glitter jacket on by 8.6s, tee blank ✓). |
| mv16_s19_t1 | S19 | 6004e6dd7797fe21959bf146e45da473 | REJECT | Sang rotation text; song span is the trio. |
| mv16_s19_t2 | S19 | 40f8f9e4e1b62094b18b48bbea5f27b0 | KEEP | Trio exact, span 0–6.48. |
| mv16_s20_t1 | S20 | 3769dbf4bdffe5820daa03c568709cb4 | SALVAGE | Right word set, rotated order (WFY/still/WFY). Assembly chunk-reorders (scatter on WFY chunks, reform on still). |
| mv16_s21_t1 | S21 | 6ec0e203bf8b544d1bf469559c561d9e | REJECT | Sang rotation text; song span is the trio. |
| mv16_s21_t2 | S21 | bb3484e7e8b4735364552ceeb42f6265 | KEEP | Trio exact, span 0–6.98 (foreground-verified JSON). |
| mv16_s22_t1 | S22 | b60e3a2628ab1041152b0111bc874cd2 | REJECT | G1 style: photoreal (paper-room swap itself read ✓). Words exact, G7 1.00. |
| mv16_s22_t2 | S22 | 6063dd0213cac90e491b4b9643c1b4ee | KEEP | Anime ✓ medium swap reads (frame ✓); words exact, ratio ~1.05. |
| mv16_s23_t1 | S23 | 54f92d2a7bf87921cde94ea60c1e27a0 | REJECT | Sang "…still going / wrong for years"; song span carries only (yeah) + "And I'm still going". |
| mv16_s23_t2 | S23 | ff3d12f60b285cd7e46e4ef8d33eb925 | KEEP | "(yeah) + And I'm still going" exact, delivered 0–2.66 (early; bend-hold covers the slot tail at conform — foreground-verified JSON). |
| mv16_s24_t1 | S24 | 074d4d83c28a541fa423cba56201c27f | KEEP | FC trio + NSM double exact. |
| mv16_s25_t1 | S25 | daa33ec131806bb3a7667017d397f85b | KEEP | FC trio + NSM doubles exact ("stop me" = ASR ear-slip). |
| mv16_s26_t1 | S26 | f5ece8225c759340587700a5031a878a | SALVAGE | Right word set, rotated order (WFY/still/WFY). Assembly chunk-reorders; tee-blank + worn-graphics surface checked at conform. |
| mv16_s27_t1 | S27 | f466adb70876b9f7637e24ab9afc6e22 | REJECT | Sang rotation text; song span is the trio. |
| mv16_s27_t2 | S27 | 2a4b9965f99383055aa635cfb9ad8c5d | KEEP | Trio exact ("stop me" = ASR ear-slip; foreground-verified JSON). |
| mv16_s28_t1 | S28 | c3097a63b659e5571f000ac4a67010f7 | REJECT | Sang sheet outro (still-going lines); performed outro is NSM×2/WFY×2. |
| mv16_s28_t2 | S28 | e08e2fc0de5d6e893c325e49dfa9deef | KEEP | Performed outro exact (NSM×2/WFY×2; "stop me" = ear-slip; foreground-verified JSON). |

## Ship map (FINAL — all 28 scenes verified)
S01 t3 · S02 t1 · S03 t1 (reorder) · S04 t2 (head-trim 0.30s) ·
S05 t3 · S06 t2 ·
S07 t2 · S08 t2 · S09 t1 · S10 t1 · S11 t1 (reorder) · S12 t2 ·
S13 t1 · S14 t2 · S15 t2 · S16 t2 · S17 t2 ·
S18 t1 · S19 t2 · S20 t1 (reorder) · S21 t2 ·
S22 t2 · S23 t2 · S24 t1 · S25 t1 · S26 t1 (reorder) ·
S27 t2 · S28 t2.
28 of 28 scenes verified (24 KEEP + 4 chunk-reorder SALVAGE).

## REBUILD takes (correct Suno take, 2026-11-13 — fired by coordinator 83770097)

| Take | Scene | md5 | Verdict | Note |
|------|-------|-----|---------|------|
| mv16_s22_t3 | S22 | 129574b40d7be961bd7a66cf2f1d5384 | KEEP (REBUILD) | Fired for the CORRECT take's bridge: WFY×3 + NSM×2 (the new performance adds a third WFY vs the wrong take's bridge). G7 1.00 (screened; segment avg_logprob −0.192). Medium swap reads (paper room, he stays full colour). Ships in the rebuild master. |
| mv16_s28_t3 | S28 | fd4238d883cb2607d8287bce95152c5b | KEEP (REBUILD) | Fired for the correct take's outro: NSM×2 + WFY. The (yeah)×3 adlib is not sung by the take — merged into L85's span per the ad-lib rule. G7 0.857 PASS. Tail conform fixed after motion probe (live-span tail-A + zoompan tail-B; see GATE_LOG). Ships in the rebuild master. |

REBUILD ship map: S22 → t3, S28 → t3; all other scenes keep their
build-1 ship takes (identical performed line texts, re-timed to the
new grid). s22_t2 / s28_t2 are superseded FOR THE REBUILD ONLY —
their sung content matches the WRONG take's BR/OUT, not the correct
performance's; they are not quality rejects. Rebuild master:
masters/mv16_wrong_for_years_16x9.mp4 (md5 e9a64e89395534c74729f164ae19e76a);
gates in GATE_LOG.md, assembly in CUTLIST.md.
