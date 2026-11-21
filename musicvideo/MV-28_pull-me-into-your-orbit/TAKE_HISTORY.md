# MV-28 TAKE HISTORY — "Pull Me Into Your Orbit"

All takes 10.000s, h264, 24fps (1248×704 except s03_t1 1280×720).
ASR = house config (faster-whisper large-v3-turbo int8, no VAD);
G7 = screened word-set overlap vs the scene's planned lines
(wordless takes: PASS = screened sung set empty).

| Take | md5 | Scene / lines | G7 | Eye | Verdict |
|---|---|---|---|---|---|
| mv28_s01_t1 | 3e124d72890aa7c318fae19e2516063c | S01 Orrery Awakens (keeper winds) | wordless clean ("Music") | PASS | KEEP |
| mv28_s01_t2 | 5b732e088b109e80e6177fc4067b413f | S01 dome tilt-down | wordless clean (junk "so" screened) | PASS | KEEP |
| mv28_s02_t1 | 23ab30a438c8e89ce96c46181dd9bedf | S02 Long Way Round (HER glide) | wordless clean ("Music") | PASS | KEEP |
| mv28_s02_t2 | b1998a83a7fa86615e896b91bd6b5eff | S02 glass + phone + hostess nod | wordless clean (junk "I" screened) | PASS | KEEP |
| mv28_s03_t1 | e9338553fb63c5e48d449fe078f32132 | S03 L01–L02 | 0.92 | PASS | KEEP for L01 only — its L02 is the vehicle's paraphrase ("Then you took the long way around the room", vehicle defect found at assembly QC 2026-11-21); L02 span = wordless cover (see s03_t2 row) |
| mv28_s04_t1 | 382f3b89b258e299b5de17590dc027d4 | S04 L03–L04 | 1.00 (exact) | PASS | KEEP |
| mv28_s05_t1 | 5a9f91d84e7fac76410b32252e226370 | S05 L05–L06 | 1.00 (exact) | PASS (gown neckline drift nit) | KEEP |
| mv28_s06_t1 | 39feea067b3f798bb1c39b9a1711596b | S06 L07–L08 | 1.00 (exact) | PASS | KEEP |
| mv28_s06_t2 | d11232aed17acf322756eb554bb77a54 | S06 L09–L10 | 0.91 | PASS | KEEP |
| mv28_s07_t1 | 05764a99d86e53020479d3d31cdaae4a | S07 L11–L12 | 1.00 (exact) | PASS (HIM mild drift nit) | KEEP |
| mv28_s07_t2 | 16abec310e48ebecdb7a6d53573d4c02 | S07 L13 wide | 1.00 (exact) | PASS | KEEP |
| mv28_s08_t1 | f525ca009b360187cc4abb74cbdccaa5 | S08 Star Wheel (dome) | wordless clean | PASS | KEEP |
| mv28_s08_t2 | 85f6edaeb4f35acf4a16a696444cabd4 | S08 couples from above | wordless clean ("Music") | PASS | KEEP |
| mv28_s19_t1 | 3106c3182baaedd19a38b7e51d880ab0 | S19 L33–L36 (pilot) | 0.81 | PASS | COVER POOL (hook phrase garbled: "Pull me night, come rushing in" — never warped under L34; t2 anchors all S19 phrases) |
| mv28_s19_t2 | de5464a3c2b9efa94e20f9c79b460411 | S19 L33–L36 (reroll, paced) | 1.00 | PASS | KEEP (primary for all S19 phrases) |

## RESUME 2026-11-21 (continuation coordinator) — volleys 4R/5/6 + 1 refire

| Take | md5 | Scene / lines | G7 | Eye | Verdict |
|---|---|---|---|---|---|
| mv28_s09_t1 | d444cdb255428fffe11b57d9c23a693c | S09 L14–L15 | 0.80 vs sheet | PASS | COVER POOL — the s09 VEHICLE carried a paraphrase of L14 ("Your jacket on the chair where you left it" vs sheet "Your jacket's hanging on my chair"); the take sang its vehicle exactly. Vehicle defect, disclosed; superseded by t2 for both sung lines |
| mv28_s09_t2 | 07cd2943d7a30b246945d29aaf77d759 | S09 L14–L15 (refire, sheet-corrected line) | 1.00 (exact) | PASS | KEEP (primary) |
| mv28_s10_t1 | d8891bec861db1fe7833c82673b6e04e | S10 L16–L17 | 1.00 (exact) | PASS | KEEP |
| mv28_s11_t1 | 76d3419b3879b4e3fcc61c40f5036bc0 | S11 L18–L19 | 1.00 (exact) | PASS | KEEP — note: "let me make you burn" IS the sheet wording of L19 (an interim comparison against a misremembered "orbit burn" line was wrong and is corrected here) |
| mv28_s12_t1 | f34503bbe5132e33f842e14f141bbe72 | S12 L20–L21 | 1.00 (exact) | PASS (orrery spark-flare nit) | KEEP (primary) |
| mv28_s12_t2 | 2dc19fd01d6ed10a3fec0f1a4929f8e5 | S12 L22–L23 | 1.00 (exact) | PASS | KEEP (alternate + cover) |
| mv28_s13_t1 | 9b1ed0256607a6adc11f6513e07b9ca3 | S13 L25 + L26/L27 | 1.00 (exact) | PASS | KEEP (primary) |
| mv28_s13_t2 | 4123f324baed549669d854b54944660a | S13 L26/L27 wide | 1.00 (exact) | PASS | KEEP (wide alternate + cover) |
| mv28_s14_t1 | 1466c91463c1b380bdab1f6a4e24186a | S14 Gearheart | wordless clean ("..." artifacts only) | PASS | KEEP |
| mv28_s15_t1 | ead23c8517c9c3bf7fb0bdcd97dd931b | S15 Distant Dance | wordless clean (junk "so" screened) | PASS | KEEP |
| mv28_s16_t1 | 9dd4b242a4fe367ffd385f37c9d46c9c | S16 Moon Crossing | wordless clean | PASS | KEEP |
| mv28_s03_t2 | — (no file) | S03 L02 (refire, sheet-corrected line) | — | — | **REFUSED by the generator** (integrity check) — not re-fired in altered form. The banked s03_t1 sang its own vehicle's wrong L02 ("Then you took the long way around the room" — vehicle defect, same class as s09); its L01 is exact and stays primary. L02's span ships as a WORDLESS COVER from s03_t1's non-sung spans + a 1.1s dome cutaway (s01_t2); the line is carried by the burned karaoke captions. Disclosed in GATE_LOG |
| mv28_s17_t1 | 6d52e4a1a69a0fab7015f20eb3c42e5e | S17 L28–L30 | 0.83 | PASS | COVER POOL — L30 mostly missing (only "No need to hurry" sung); superseded by t2 |
| mv28_s17_t2 | a56b7e3d01ede6aae6713b76862deed4 | S17 L28–L30 (refire) | 1.00 (word set exact) | PASS | KEEP (primary) |
| mv28_s18_t1 | ce19ac59a0a3e4928e15ab05dcfb793a | S18 L31–L32 | 1.00 (exact) | PASS | KEEP |
| mv28_s20_t1 | b41ad1e0e4c999f63b8523549ab200f8 | S20 L37–L38 | 1.00 (exact) | PASS | KEEP |
| mv28_s21_t1 | c9cbb24b9777c7fb1553c11b6d457660 | S21 L39 | 1.00 (exact) | PASS | KEEP |
| mv28_s22_t1 | — (no file) | S22 L40 | — | — | **LOST IN TOOL HANDOFF** — wrapper-level error; render reported ok server-side, no local file saved, failed request not repeatable, NOT re-fired (MV-27 S06 precedent). S22 ships as wordless dawn cover from s21_t1 + s23_t1 non-claimed spans; L40 carried by burned karaoke captions |
| mv28_s23_t1 | c87a9578604e14a5fc07759d27b5d656 | S23 tail | wordless clean | PASS | KEEP |

Spend: 33/40 video calls + 1 generator refusal (s03_t2, no file).
(15 banked + 16 owed fired incl. lost s22 + refires s17_t2, s09_t2.)
All scenes S01–S23 have KEEP coverage → assembly.
