# MV-5 CUTLIST — "Easy now, easy now (THE VOICE)"

Master: `masters/mv5_easy_now_easy_now_16x9.mp4` — ONE 16:9 only, 1280x720 h264 24fps,
AAC 48kHz stereo, faststart, 4954 frames, 206.400s. Sole master audio: `track.mp3`
(md5 `0c1bcafa568547e2d4fa36e133ad3626`, muxed untouched; generated clip audio dropped).
Captions: `captions_16x9.ass` (453 events, line-block + per-word cadmium highlight),
keyed to SONG word times. Bug `~ WuBu ~` burned on all frames.

Method: WORD-SYNC (Slopcannon stage 6). Per-word offsets measured from fresh prompted
transcriptions of every KEEP take (`work/assembly_take_words/`) against SONG_WORDS.json,
placed by min-total-cost assignment. Warps in [0.80, 1.25] except the two sanctioned
S17 grey rescues (0.71/0.65). No frozen frame while words play (the one exception is
the S01 pre-word leader freeze, MV-3 precedent). Structural scenes are donor montage
(KEEP takes' post-word tails first, then REJECTED takes' silent tails — delivery-only
rejects, picture on-brief — used ONLY as silent reaction/B-roll, never as a sung take;
each slice motion-verified: mean diff >= 0.10 at 160x90 and longest near-dup run < 24f).

## Scene map

| Scene | Slot (s) | Take | md5 | Warp(s) | Disposition |
|---|---|---|---|---|---|
| S01 | 0.00-10.04 | mv5_s01_t1 | 1ccf23810114ebbc0558963022d84be0 | 0.812, 1.103, 1.250 | KEEP t1 — per-line placement (intro refrains; take gaps dropped, hard cut on line boundary). Leader freeze 40f (frame 0 held, pre-word only). |
| S02 | 10.04-18.64 | mv5_s02_t1 | 4b5de2bbc7ef3ae7b52455095bfd887d | 1.000 | KEEP t1 — cutaway @1.0x (intro repeat, CAT sings, girl listening). |
| S03 | 18.64-22.00 | mv5_s03_t1 | 1023ea5f3b705f550d3a6d689b1ff1da | 0.889 | KEEP t1 — vocalise SPAN @0.889 (ta-da, GIRL). |
| S04 | 22.00-31.48 | mv5_s04_t1<br>mv5_s05_t1<br>mv5_s12_t1 | ce26e873bd40f2b6058057a427e42f75<br>4557cd06fc514e0dd31decc17e1f6514<br>4202db31b66386a7979143f587f91119 | 0.826, 1.073, 1.243, 1.250 | KEEP t1 — per-line placement (L03 rushed, L05 drags; whole-clip SPAN left L03 +1.0-1.5s late). L03/L05 at 1.25 band edge. |
| S05 | 31.48-40.44 | mv5_s05_t1 | 4557cd06fc514e0dd31decc17e1f6514 | 1.030 | KEEP t1 — SPAN @1.030. |
| S06 | 40.44-47.76 | mv5_s06_t1 | bc19ed1009cd1324c1135def0f6194ec | 0.800 | KEEP t1 — SPAN @0.80 band edge + tail-loop deficit (take tail, moving). |
| S07 | 47.76-57.52 | mv5_s07_t1<br>mv5_s08_t2 | 3bdd0f48a7999696b27a6c4e1e0da7f2<br>fc07dcacf30e91cdcd98a89b5148760e | 0.800, 0.817, 1.107, 1.250 | KEEP t1 — per-line placement (whole-clip SPAN left L16's pickups +1.3-1.9s late). L13 @0.80, L16 @1.25 band edges; +0.30s lateness propagates L13→L16 (disclosed). |
| S08 | 57.52-67.06 | mv5_s01_t1<br>mv5_s08_t2<br>mv5_s20_t1 | 1ccf23810114ebbc0558963022d84be0<br>fc07dcacf30e91cdcd98a89b5148760e<br>ebfeb2a65108ad1986e7195aa20b6ca1 | 0.966, 1.106, 1.197 | KEEP t2 — per-refrain placement (R1/R2/R4 sung; R3 CAT reaction cover; response windows donor cover). R3 cover is a CAT reaction, not a mouth-sung slot. |
| S09 | 67.06-76.80 | mv5_s01_t1<br>mv5_s09_t1<br>mv5_s10_t1<br>mv5_s12_t1 | 1ccf23810114ebbc0558963022d84be0<br>37c3ffb0da3982331bbb4ac2547bd991<br>89830a0407ad9c8cafff1879e0dbc548<br>4202db31b66386a7979143f587f91119 | 0.869, 0.915, 1.096, 1.133 | KEEP t1 — per-refrain placement (all 4 refrains in band); response windows donor cover. Warp rescue ≤1.5x carried (max warp 1.133). |
| S10 | 76.80-85.16 | mv5_s10_t1 | 89830a0407ad9c8cafff1879e0dbc548 | 1.000 | KEEP t1 — cutaway @1.0x (C1 tail tag, CAT sings, girl listening). |
| S11 | 85.16-93.80 | mv5_s02_t1<br>mv5_s09_t1<br>mv5_s11_t4<br>mv5_s18_t1 | 4b5de2bbc7ef3ae7b52455095bfd887d<br>37c3ffb0da3982331bbb4ac2547bd991<br>a0321de04e78cc1746d0db4fee9aa626<br>5747e5443e07633313dae30c5486a58f | 0.800, 0.880 | KEEP t4 — L38 montage cover (0.17x, not a mouth-sung slot); L39 grey rescue @0.80 band edge; L40 CAT-half donor cover + girl tail @0.88. Take trimmed 10.00s → 7.84s slot. |
| S12 | 93.80-102.40 | mv5_s03_t1<br>mv5_s09_t1<br>mv5_s12_t1<br>mv5_s26_t1 | 1023ea5f3b705f550d3a6d689b1ff1da<br>37c3ffb0da3982331bbb4ac2547bd991<br>4202db31b66386a7979143f587f91119<br>597218f1dc8282ebefc2fc2253edb4d0 | 0.800 | KEEP t1 — per-line placement (take's L43 far too slow for its 1.60s window; whole-clip SPAN left L43 +2-4s late). L41/L43 @0.80 band edge; L43 overruns 1.41s into L44 (disclosed). L42/L44 CAT lines donor cover. |
| S13 | 102.40-111.90 | mv5_s03_t1<br>mv5_s04_t1<br>mv5_s06_t1<br>mv5_s08_t2<br>mv5_s13_t1<br>mv5_s13_t2<br>mv5_s13_t3<br>mv5_s13_t4<br>mv5_s13_t5<br>mv5_s13_t6<br>mv5_s13_t7<br>mv5_s17_t1<br>mv5_s19b_t1<br>mv5_s28_t1 | 1023ea5f3b705f550d3a6d689b1ff1da<br>ce26e873bd40f2b6058057a427e42f75<br>bc19ed1009cd1324c1135def0f6194ec<br>fc07dcacf30e91cdcd98a89b5148760e<br>deeac574cd58014601a9b21116b2d8bf<br>951a9afb3aac9c779940934a9d51c1db<br>cee68e6058e289884ef55ecd1bdbea1c<br>9350ea502b912c28d467b9a965180c9f<br>d30276b8d331ba90804854effa4f6c38<br>15024c3303e174fa01df916cc2e05508<br>384e1f6ca8d4700f00a189c20faaa6b9<br>c239ec5925bc66710e080e9b62bb1ff1<br>ca4254360cfca2e940c1055cefcbdf90<br>c4030af7f9ab17548d137cd7cbcac652 | cover | STRUCTURAL — 3 stagings, 7 takes, all delivery-failed. Chorus cover: static MCU girl + CAT reaction inserts + captions (not a mouth-sung slot). Donors: S13's own rejected tails first. |
| S14 | 111.90-116.00 | mv5_s14_t3<br>mv5_s16_t1<br>mv5_s19b_t1<br>mv5_s27_t1 | 8e43590d7367caff0460af4de244fc23<br>c47a0ed1c0bbdcbb5f3607e93062df70<br>ca4254360cfca2e940c1055cefcbdf90<br>fdc6c6c02e1bf36178294117a4dc2b5b | cover | STRUCTURAL — 3 takes, pace floor (0.42x). Dusk-rail CAT reaction / B-roll montage cover + captions (not a mouth-sung slot). |
| S15 | 116.00-121.30 | mv5_s15_t1<br>mv5_s21_t3 | 72332ff6ccc1839d6c4d5db629a0562a<br>f35916faac7b59a401857dd1539f3505 | 0.914 | KEEP t1 — GREY RESCUE: SPAN @0.914 over the whole slot incl. the held vocalise; fast pickups land +0.26 to +1.89 late (disclosed). Breath gap donor cover. |
| S16 | 121.30-130.78 | mv5_s16_t2<br>mv5_s16_t3 | fb876049fe1250a503eb6dbeb317e167<br>41cc9f72c6e07ee44f3dae9ea441e55c | cover | STRUCTURAL — 6 takes, 3 stagings; the voice never restarts the refrain pattern after R1. Chorus cover like S13 (not a mouth-sung slot). |
| S17 | 130.78-140.52 | mv5_s16_t1<br>mv5_s17_t1<br>mv5_s21_t3 | c47a0ed1c0bbdcbb5f3607e93062df70<br>c239ec5925bc66710e080e9b62bb1ff1<br>f35916faac7b59a401857dd1539f3505 | 0.651, 0.714, 0.932, 1.091 | KEEP t1 — GREY RESCUE: per-refrain (R1 @0.93, R2 @0.71 grey, R3 @0.65 grey, R4 @1.09 by RMS envelope 6.9-8.0s). R3/R4 times are QC's adjudication + RMS, not Whisper's (Whisper's R3/R4 times are wrong — RMS silence 4.6-5.5s and 8.0-10.0s). |
| S18 | 140.52-148.70 | mv5_s18_t1 | 5747e5443e07633313dae30c5486a58f | 1.000 | KEEP t1 — cutaway @1.0x (both mouths closed, locks hold). |
| S19a | 148.70-152.36 | mv5_s19a_t1<br>mv5_s19a_t2 | 2905f33d0cd6db49af0ab5377866b304<br>103dfcdad4ad8d6a994d84f8d0a89247 | cover | STRUCTURAL — split half, 2 takes, delivery-failed. Grey-sky CAT reaction / B-roll cover + captions (not a mouth-sung slot). S19b stays as the sung half. |
| S19b | 152.36-155.72 | mv5_s19b_t1 | ca4254360cfca2e940c1055cefcbdf90 | 0.808 | KEEP t1 — GREY RESCUE: SPAN @0.808 (L77 head re-measured by forced alignment / energy envelope; 'We still' placed as one unit at the head; caption as written). |
| S20 | 155.72-158.06 | mv5_s16_t1<br>mv5_s16_t3<br>mv5_s20_t1 | c47a0ed1c0bbdcbb5f3607e93062df70<br>41cc9f72c6e07ee44f3dae9ea441e55c<br>ebfeb2a65108ad1986e7195aa20b6ca1 | 0.800 | KEEP t1 — GREY RESCUE: SPAN @0.80 band edge; 'breeze' overruns 1.05s past the line end into L81 (disclosed). L81 listen tail donor cover. |
| S21 | 158.06-167.50 | mv5_s16_t3<br>mv5_s21_t1<br>mv5_s21_t3 | 41cc9f72c6e07ee44f3dae9ea441e55c<br>15997b13a7544d36f93e44e97b7e9920<br>f35916faac7b59a401857dd1539f3505 | 0.800 | PARTIAL t3 — head L82-L86 by measured word times (SPAN @0.80 band edge; drift disclosed, last word +1.07s); tail L87-L89 montage cover + captions (not a mouth-sung slot). |
| S22 | 167.50-169.16 | mv5_s22_t2<br>mv5_s22_t3 | 4422acfcbf01ee5a1769c5c093436596<br>0169337b988896dee221fc6989f51fae | cover | STRUCTURAL — 3 takes, pace floor (three distinct 'No' attacks need ~3.3s for a 1.66s slot). Head-shake reaction cover + caption (not a mouth-sung slot). Donor: S22 t3's own tail (after the attack, mouth closed). |
| S23 | 169.16-176.04 | mv5_s16_t3<br>mv5_s16_t4<br>mv5_s23_t1 | 41cc9f72c6e07ee44f3dae9ea441e55c<br>176a94644a7151fdbdb1037c316e17fb<br>65e471e3cf7c9744a67dd407f2785c1f | 0.812, 0.919, 0.962, 1.121 | KEEP t1 — per-refrain placement by measured word times (R1 @0.96, R2 @0.92, R3 @1.12, 'No need to' @0.81). Unprompted 'No' onset 5.64s used (not prompted 5.24). Low-motion disclosure stands (vocal mean 0.558 @160x90, 0.727 @320x180). |
| S24 | 176.04-182.78 | mv5_s24_t1<br>mv5_s24_t2<br>mv5_s24_t3 | eda851c484e4a4d84ad8d4b88b55e74c<br>f138d39f8dbcb6afccea817ef1f6084e<br>b75916ef1e1db22762683f924e222f09 | cover | STRUCTURAL — 3 takes; third refrain never restarts (3/3). Chorus cover like S16 (not a mouth-sung slot). |
| S25 | 182.78-190.42 | mv5_s16_t4<br>mv5_s25_t1 | 176a94644a7151fdbdb1037c316e17fb<br>008a1934e8a2340b1441e4ddfdec9550 | 0.800, 1.091 | KEEP t1 — per-refrain placement by measured word times (R1 @0.80 band edge, R2 @1.09). L104 gap + L106 CAT reaction cover + breath gap donor cover. |
| S26 | 190.42-197.58 | mv5_s16_t4<br>mv5_s16_t5<br>mv5_s26_t1 | 176a94644a7151fdbdb1037c316e17fb<br>b2aca41fc66f639d219e79e1065a9ce3<br>597218f1dc8282ebefc2fc2253edb4d0 | 0.800 | KEEP t1 — per-refrain placement by measured word times (pre-word donor cover 39f, SPAN @0.80, L108 cover from take tail). 'Is it' mishear adjudicated (take sings 'easy'). |
| S27 | 197.58-203.42 | mv5_s27_t1 | fdc6c6c02e1bf36178294117a4dc2b5b | 1.232 | KEEP t1 — SPAN @1.232 (held line; breath gap 1.74-2.72s). 3rd word 'easy' lands +1.75s late (the take's breath gap is longer than the song's — disclosed). |
| S28 | 203.42-206.40 | mv5_s28_t1 | c4030af7f9ab17548d137cd7cbcac652 | 0.800 | KEEP t1 — GREY RESCUE: SPAN @0.80 band edge (trim 0.05s) + outro tail from take. Ratio 0.78 → 0.80. |

## Per-word sync scores (fit, placed-time min-cost assignment)

Pairs = take words matched to song words (Whisper repeat-collapses each doubled
"Easy now" refrain to one pair, so refrain scenes show ~half the song words as
"missing" — those are the collapsed repeats, sung by the take, not missing words.
CAT-half words in split lines (S11 L40, S23 L96 'run') are covered, not sung.

| Scene | Pairs | Median |off| | Max |off| | Within ±0.50s |
|---|---|---|---|---|
| S01 | 16/16 | 0.238s | 0.443s | 16/16 |
| S02 | cover (no sung words) | — | — | — |
| S03 | cover (no sung words) | — | — | — |
| S04 | 22/22 | 0.100s | 0.479s | 22/22 |
| S05 | 16/16 | 0.342s | 0.888s | 10/16 |
| S06 | 14/14 | 0.174s | 0.880s | 10/14 |
| S07 | 20/20 | 0.202s | 0.665s | 19/20 |
| S08 | 7/12 | 0.322s | 0.423s | 7/7 |
| S09 | 9/16 | 0.197s | 0.346s | 9/9 |
| S10 | cover (no sung words) | — | — | — |
| S11 | 8/12 | 0.336s | 0.430s | 8/8 |
| S12 | 12/12 | 0.268s | 1.272s | 8/12 |
| S13 | cover (no sung words) | — | — | — |
| S14 | cover (no sung words) | — | — | — |
| S15 | 5/5 | 0.897s | 1.891s | 1/5 |
| S16 | cover (no sung words) | — | — | — |
| S17 | 8/16 | 0.290s | 0.562s | 7/8 |
| S18 | cover (no sung words) | — | — | — |
| S19a | cover (no sung words) | — | — | — |
| S19b | 13/13 | 0.200s | 0.571s | 12/13 |
| S20 | 4/4 | 0.732s | 0.788s | 1/4 |
| S21 | 23/23 | 0.724s | 1.368s | 7/23 |
| S22 | cover (no sung words) | — | — | — |
| S23 | 9/16 | 0.282s | 0.775s | 7/9 |
| S24 | cover (no sung words) | — | — | — |
| S25 | 4/8 | 0.291s | 0.333s | 4/4 |
| S26 | 4/4 | 0.176s | 0.384s | 4/4 |
| S27 | 4/4 | 0.231s | 1.751s | 3/4 |
| S28 | 4/4 | 0.160s | 0.516s | 3/4 |

Weakest scenes (disclosed): S15 median 0.897s (grey rescue, fast pickups +0.26 to +1.89);
S20 median 0.732s (band-edge 0.80, 'breeze' overruns 1.05s); S21 median 0.724s
(band-edge 0.80, drift to +1.37 on 'pace'); S27 'easy' +1.75s (breath gap longer than
the song's); S12 'bills' +1.27s (take's L43 too slow for its 1.60s window).

## Donor ledger (all 68 donor slices, motion-verified)

Format: scene | window (s) | donor take [frames] | kind. Donor ranges are disjoint
from every direct piece's source range. Two slices were skipped by the motion check
in the final fit (S14 t1 tail: 29f near-dup run; S21 t3 tail end: mean 0.07).

- S04 26.13-26.42s: mv5_s05_t1[209:216] (donor-tail, md5 4557cd06fc514e0dd31decc17e1f6514)
- S04 26.42-27.76s: mv5_s12_t1[175:207] (donor-tail, md5 4202db31b66386a7979143f587f91119)
- S07 56.15-57.52s: mv5_s08_t2[205:237] (donor-tail, md5 fc07dcacf30e91cdcd98a89b5148760e)
- S08 59.84-60.22s: mv5_s20_t1[68:77] (donor-tail, md5 ebfeb2a65108ad1986e7195aa20b6ca1)
- S08 62.44-62.52s: mv5_s20_t1[77:79] (donor-tail, md5 ebfeb2a65108ad1986e7195aa20b6ca1)
- S08 62.52-63.66s: mv5_s20_t1[79:107] (donor-tail, md5 ebfeb2a65108ad1986e7195aa20b6ca1)
- S08 63.94-64.48s: mv5_s20_t1[107:120] (donor-tail, md5 ebfeb2a65108ad1986e7195aa20b6ca1)
- S08 64.48-64.92s: mv5_s01_t1[223:233] (donor-tail, md5 1ccf23810114ebbc0558963022d84be0)
- S09 68.74-69.11s: mv5_s12_t1[207:216] (donor-tail, md5 4202db31b66386a7979143f587f91119)
- S09 69.11-69.40s: mv5_s01_t1[233:240] (donor-tail, md5 1ccf23810114ebbc0558963022d84be0)
- S09 70.96-71.66s: mv5_s10_t1[202:219] (donor-tail, md5 89830a0407ad9c8cafff1879e0dbc548)
- S09 73.28-74.02s: mv5_s10_t1[219:236] (donor-tail, md5 89830a0407ad9c8cafff1879e0dbc548)
- S09 75.04-75.21s: mv5_s10_t1[236:240] (donor-tail, md5 89830a0407ad9c8cafff1879e0dbc548)
- S09 75.21-76.80s: mv5_s09_t1[142:180] (donor-tail, md5 37c3ffb0da3982331bbb4ac2547bd991)
- S11 87.00-87.60s: mv5_s11_t4[107:121] (cover-L38, md5 a0321de04e78cc1746d0db4fee9aa626)
- S11 88.92-89.80s: mv5_s11_t4[219:240] (donor-tail, md5 a0321de04e78cc1746d0db4fee9aa626)
- S11 89.80-90.21s: mv5_s02_t1[206:216] (donor-tail, md5 4b5de2bbc7ef3ae7b52455095bfd887d)
- S11 90.21-91.05s: mv5_s18_t1[196:216] (donor-tail, md5 5747e5443e07633313dae30c5486a58f)
- S11 91.05-91.42s: mv5_s09_t1[180:189] (donor-tail, md5 37c3ffb0da3982331bbb4ac2547bd991)
- S11 93.00-93.80s: mv5_s09_t1[189:208] (donor-tail, md5 37c3ffb0da3982331bbb4ac2547bd991)
- S12 95.38-96.71s: mv5_s09_t1[208:240] (donor-tail, md5 37c3ffb0da3982331bbb4ac2547bd991)
- S12 96.71-96.84s: mv5_s26_t1[151:154] (donor-tail, md5 597218f1dc8282ebefc2fc2253edb4d0)
- S12 99.85-101.43s: mv5_s26_t1[154:192] (donor-tail, md5 597218f1dc8282ebefc2fc2253edb4d0)
- S12 101.43-102.40s: mv5_s03_t1[91:115] (donor-tail, md5 1023ea5f3b705f550d3a6d689b1ff1da)
- S13 102.40-102.90s: mv5_s13_t5[228:240] (cover-rej-tail, md5 d30276b8d331ba90804854effa4f6c38)
- S13 102.90-103.73s: mv5_s13_t3[220:240] (cover-rej-tail, md5 cee68e6058e289884ef55ecd1bdbea1c)
- S13 103.73-104.57s: mv5_s13_t4[220:240] (cover-rej-tail, md5 9350ea502b912c28d467b9a965180c9f)
- S13 104.57-105.44s: mv5_s13_t2[219:240] (cover-rej-tail, md5 951a9afb3aac9c779940934a9d51c1db)
- S13 105.44-106.32s: mv5_s13_t1[219:240] (cover-rej-tail, md5 deeac574cd58014601a9b21116b2d8bf)
- S13 106.32-106.86s: mv5_s13_t7[227:240] (cover-rej-tail, md5 384e1f6ca8d4700f00a189c20faaa6b9)
- S13 106.86-107.36s: mv5_s13_t6[228:240] (cover-rej-tail, md5 15024c3303e174fa01df916cc2e05508)
- S13 107.36-108.82s: mv5_s28_t1[85:120] (cover-tail, md5 c4030af7f9ab17548d137cd7cbcac652)
- S13 108.82-109.03s: mv5_s03_t1[115:120] (cover-tail, md5 1023ea5f3b705f550d3a6d689b1ff1da)
- S13 109.03-110.53s: mv5_s04_t1[204:240] (cover-tail, md5 ce26e873bd40f2b6058057a427e42f75)
- S13 110.53-111.28s: mv5_s06_t1[194:212] (cover-tail, md5 bc19ed1009cd1324c1135def0f6194ec)
- S13 111.28-111.40s: mv5_s08_t2[237:240] (cover-tail, md5 fc07dcacf30e91cdcd98a89b5148760e)
- S13 111.40-111.69s: mv5_s17_t1[233:240] (cover-tail, md5 c239ec5925bc66710e080e9b62bb1ff1)
- S13 111.69-111.90s: mv5_s19b_t1[100:105] (cover-tail, md5 ca4254360cfca2e940c1055cefcbdf90)
- S14 111.90-112.57s: mv5_s19b_t1[105:121] (cover-tail, md5 ca4254360cfca2e940c1055cefcbdf90)
- S14 112.57-112.86s: mv5_s14_t3[233:240] (cover-rej-tail, md5 8e43590d7367caff0460af4de244fc23)
- S14 112.86-114.11s: mv5_s27_t1[114:144] (cover-tail, md5 fdc6c6c02e1bf36178294117a4dc2b5b)
- S14 114.11-116.00s: mv5_s16_t1[151:196] (cover-rej-tail, md5 c47a0ed1c0bbdcbb5f3607e93062df70)
- S15 120.02-121.30s: mv5_s21_t3[198:229] (donor-tail, md5 f35916faac7b59a401857dd1539f3505)
- S16 121.30-127.76s: mv5_s16_t2[85:240] (cover-rej-tail, md5 fb876049fe1250a503eb6dbeb317e167)
- S16 127.76-130.78s: mv5_s16_t3[108:181] (cover-rej-tail, md5 41cc9f72c6e07ee44f3dae9ea441e55c)
- S17 132.42-132.88s: mv5_s21_t3[229:240] (donor-tail, md5 f35916faac7b59a401857dd1539f3505)
- S17 132.88-133.08s: mv5_s16_t1[196:201] (donor-rej-tail, md5 c47a0ed1c0bbdcbb5f3607e93062df70)
- S17 134.94-135.36s: mv5_s16_t1[201:212] (donor-rej-tail, md5 c47a0ed1c0bbdcbb5f3607e93062df70)
- S17 136.52-137.62s: mv5_s16_t1[212:238] (donor-rej-tail, md5 c47a0ed1c0bbdcbb5f3607e93062df70)
- S19a 148.70-151.32s: mv5_s19a_t2[57:120] (cover-rej-tail, md5 103dfcdad4ad8d6a994d84f8d0a89247)
- S19a 151.32-152.36s: mv5_s19a_t1[89:114] (cover-rej-tail, md5 2905f33d0cd6db49af0ab5377866b304)
- S20 157.75-157.84s: mv5_s16_t1[238:240] (donor-rej-tail, md5 c47a0ed1c0bbdcbb5f3607e93062df70)
- S20 157.84-158.06s: mv5_s16_t3[181:186] (donor-rej-tail, md5 41cc9f72c6e07ee44f3dae9ea441e55c)
- S21 164.65-166.57s: mv5_s21_t1[194:240] (donor-rej-tail, md5 15997b13a7544d36f93e44e97b7e9920)
- S21 166.57-167.50s: mv5_s16_t3[186:208] (donor-rej-tail, md5 41cc9f72c6e07ee44f3dae9ea441e55c)
- S22 167.50-169.00s: mv5_s22_t3[84:120] (cover-rej-tail, md5 0169337b988896dee221fc6989f51fae)
- S22 169.00-169.16s: mv5_s22_t2[80:84] (cover-rej-tail, md5 4422acfcbf01ee5a1769c5c093436596)
- S23 170.58-171.44s: mv5_s16_t3[208:229] (donor-rej-tail, md5 41cc9f72c6e07ee44f3dae9ea441e55c)
- S23 173.08-173.54s: mv5_s16_t3[229:240] (donor-rej-tail, md5 41cc9f72c6e07ee44f3dae9ea441e55c)
- S23 173.54-173.62s: mv5_s16_t4[172:174] (donor-rej-tail, md5 176a94644a7151fdbdb1037c316e17fb)
- S24 176.04-180.04s: mv5_s24_t1[72:168] (cover-rej-tail, md5 eda851c484e4a4d84ad8d4b88b55e74c)
- S24 180.04-182.04s: mv5_s24_t3[120:168] (cover-rej-tail, md5 b75916ef1e1db22762683f924e222f09)
- S24 182.04-182.78s: mv5_s24_t2[83:101] (cover-rej-tail, md5 f138d39f8dbcb6afccea817ef1f6084e)
- S25 184.40-185.02s: mv5_s16_t4[174:189] (donor-rej-tail, md5 176a94644a7151fdbdb1037c316e17fb)
- S25 189.24-190.42s: mv5_s16_t4[189:217] (donor-rej-tail, md5 176a94644a7151fdbdb1037c316e17fb)
- S26 190.42-191.38s: mv5_s16_t4[217:240] (donor-rej-tail, md5 176a94644a7151fdbdb1037c316e17fb)
- S26 191.38-192.06s: mv5_s16_t5[175:191] (donor-rej-tail, md5 b2aca41fc66f639d219e79e1065a9ce3)


## v6 FULL REBUILD (2026-11-13) — CURRENT

User order 2026-11-13 04:44 EST: the lyric sheet is the LOOK SPEC — Verse 1
sings "Blue shirt, red bicycle"; v1–v5 inverted both (blue bicycle, red
jacket). v6 is a TOTAL refire: zero footage reuse; only the lyrics-redo
word grid (118 lines, 548 words) + captions
(`work/lyrics-redo/mv5_kinetic_redo.ass`) carry over. Singer assignments
RE-DERIVED in-build from the MDX vocal stem + F0 (corrections vs the old
ear record: L12 = CAT, L41 = CAT, L55 = CAT, L109 = CAT, L16 = GIRL sung;
bridge opens with CAT, not GIRL-first). Colour is a G1 hard gate: GIRL in
a BLUE SHIRT, bicycle RED in every frame — zero colour rejects.

Masters: `masters/mv5_easy_now_easy_now_16x9_v6.mp4` (md5
`2071388f3fb5672849e29462cb3f2b64`, 197.2 MB) + chat copy
`masters/mv5_easy_now_easy_now_16x9_v6_chat.mp4` (md5
`2e2688bd592821e0a4c6ab3ab5f4657b`, 46.1 MB, crf 26, AAC copied). ONE 16:9,
1280x720 h264 CRF 18, 24fps, exactly 4954 frames, 206.4167s, AAC 48k
stereo, faststart, `~ WuBu ~` bug, texture pass (grain/vignette/sat 0.88)
under the captions. Fit: `work/rebuild-v6/assembly_fit_mv5_v6.json`
(0 errors, 29 disclosures). Gates: `work/rebuild-v6/qc/GATE_LOG_V6.md`,
`work/rebuild-v6/qc/VISUAL_GATE_V6.md`. Assembler:
`work/rebuild-v6/assemble_mv5_v6.py`. Takes registered in `takes/` as
`mv5_v6_*.mp4`. Parent delivers — no delivered flag written by coordinator.

| Scene | Start (s) | Pieces (take [kind, warp, out-frames]) |
|---|---|---|
| S01 | 0.00 | s02_ride[fill w1.79 34f]<br>s01_cat[phrase w0.93 59f]<br>s01_cat[phrase w1.30 60f]<br>s01_cat[phrase w1.29 41f]<br>s01_cat[phrase w1.15 47f] |
| S02 | 10.04 | s02_ride[fill w4.48 13f]<br>s02_girl[phrase w1.82 51f]<br>s02_girl[span w0.76 142f] |
| S03 | 18.62 | s03_girl[span w0.99 81f] |
| S04 | 22.00 | s04_cat[phrase w1.11 23f]<br>s04_cat[phrase w0.54 61f]<br>s04_cat[phrase w1.53 50f]<br>s04_cat[phrase w1.10 60f]<br>s04_cat2[phrase w1.93 34f] |
| S05 | 31.50 | s02_ride[fill w1.47 8f]<br>s05_cat[phrase w1.09 43f]<br>s05_cat[phrase w1.24 60f]<br>s05_cat[phrase w0.52 77f]<br>s01_cat[fill w0.88 27f] |
| S06 | 40.46 | s02_ride[fill w2.21 9f]<br>s06_cat[phrase w1.14 48f]<br>s11_cat[fill w0.95 42f]<br>s06_cat[phrase w0.96 73f] |
| S07 | 47.62 | s07_girla[phrase w1.62 24f]<br>s07_cat[phrase w1.74 63f]<br>s07_girla[phrase w1.94 37f]<br>s07_girlb[phrase w0.68 113f] |
| S08 | 57.50 | s02_girl[fill w1.25 6f]<br>s08_duet[span w1.39 223f] |
| S09 | 67.04 | s09b_duet[span w0.75 234f] |
| S10 | 76.79 | pilot_p2_cat[fill 0f — dropped in layout]<br>s10_cat[phrase w0.91 41f]<br>s10_cat[phrase w0.97 104f]<br>s10_cat[phrase w0.89 56f] |
| S11 | 85.17 | s03_girl[fill 0f — dropped in layout]<br>s11_cat[phrase w1.11 32f]<br>s11_cat[phrase w1.64 26f]<br>s11_cat[phrase w1.28 36f]<br>s11_cat[phrase w0.64 60f]<br>s11_girl[phrase w1.38 53f] |
| S12 | 93.79 | s12_cat[phrase w1.18 40f]<br>s12_cat[phrase w1.47 32f]<br>s12_girl[phrase w1.94 40f]<br>s12_cat[phrase w0.91 88f] |
| S13 | 102.14 | s13_cat[phrase w1.46 34f]<br>s13_girl[phrase w1.19 39f]<br>s13_cat[phrase w1.82 30f]<br>s13_cat[phrase w1.48 25f]<br>s13_boombox[fill w6.72 32f]<br>s13_girl[phrase w1.90 23f]<br>s13_spin[fill w1.03 27f]<br>s13_girl[phrase w1.95 25f] |
| S14 | 111.92 | s15_girl[phrase w1.05 17f]<br>s15_cat2[phrase w1.37 28f]<br>s15_cat2[phrase w1.17 19f]<br>s15_girl[phrase w0.93 7f]<br>s15_cat2[phrase w1.23 26f]<br>s15_girl[phrase w1.41 76f] |
| S15 | 119.15 | s15_girl[fill w1.07 52f] |
| S16 | 121.29 | s16_duet[span w0.66 228f] |
| S17 | 130.79 | s17_duet[span w1.03 233f] |
| S18 | 140.50 | s18_girl[span w0.90 197f]<br>s18_girl[fill 0f — dropped in layout] |
| S19 | 148.71 | s02_girl[fill w1.98 4f]<br>s19_bridge[span w1.47 164f] |
| S20 | 155.71 | s20_bridge[phrase w1.92 31f]<br>s20_cat2[phrase w1.96 25f] |
| S21 | 158.04 | s21_all2[phrase w1.89 28f]<br>s21_all2[phrase w0.94 25f]<br>s21_all2[phrase w0.79 29f]<br>s21_all2[phrase w1.40 24f]<br>s21_spin[fill 0f — dropped in layout]<br>s21_all2[phrase w1.11 29f]<br>s21_girl2[phrase w1.64 29f]<br>s21_all2[phrase w0.55 32f]<br>s21_walk[phrase w1.43 31f] |
| S22 | 167.50 | s21_walk[fill w0.90 29f] (+ blackout-snap fade dip, post grade) |
| S23 | 168.72 | s23_duet[span w1.36 176f] |
| S24 | 176.04 | s24_duet[span w1.11 162f] |
| S25 | 182.79 | s25_cat2[phrase w0.80 53f]<br>s25_girl[phrase w1.61 35f]<br>s25_girl[phrase w1.20 95f] |
| S26 | 190.42 | s26_chain[fill w1.04 62f] |
| S27 | 193.00 | s26_chain[fill w6.00 5f]<br>s27_chant[span w0.90 205f]<br>s27_cat2[phrase w1.32 50f] |
| S28 | 203.83 | s28_cat2[phrase w1.32 62f] |

Dispositions: every sung line is a measured phrase (DP-aligned to fresh
take transcriptions) except the six duet/chant continuous-shot spans
(S02 I08, S03, S08, S09, S16, S17, S18, S19, S23, S24, S27) whose interiors
two-voice ASR cannot anchor — endpoints anchored, interiors disclosed in
the fit JSON. Covers: L09 (s01_cat tail, backpack in frame), L11 (s11_cat
vendor head), L49 (boombox plate, ADULTS), L51 (spin plate), L90 (blackout
interlude), L103 hook (rides under L104's lead picture — layered duet).
REJECTED: s25_cat v1 (identity intrusion at L104) — replaced by s25_cat2.
REFUSED by generator (never retried): pilot p1, pilot p3, s09_duet.
