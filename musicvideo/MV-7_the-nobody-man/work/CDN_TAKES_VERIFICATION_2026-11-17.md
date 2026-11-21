# MV-7 'I'm The Nobody Man' — CDN takes verification (2026-11-17)

Question: the 2026-11-16 ~21:04 EST cleanup deleted MV-7's local take mp4s
(cross-check 2026-11-17 09:40 EST: 104 of 109 ledgered take files missing
across all three builds — v2 32/37, otaku 46/46, rebuild2 26/26; segment
mp4s also gone). Masters intact and flag-verified (rebuild2 house master
md5 36176f04c349ad05e2f456e129392b80). Were the deleted takes backed up
on the CDN first?

Method (MV-5/MV-18/MV-19/MV-20-proven): dataset tree API lfs.oid does NOT
equal ledger md5s, so every in-scope file was DOWNLOADED from
WaefreBeorn/wubutv-network-media and md5-hashed; the downloaded md5 was
compared against the ledger's recorded md5 (TAKE_HISTORY.md for v2;
work/otaku_qc/volley*_results.md + reroll1_results.md for otaku, with
MV7_OTAKU_PROGRESS.md for volley 1; MV7_REBUILD2_PROGRESS.md take tables
for rebuild2). Dataset paths are the mirrored project tree under
musicvideo/MV-7_the-nobody-man/. Read-only: downloads only, ledgers untouched.
115 download-md5 jobs run (109 canonical takes + 6 otaku media-generation
originals for the dual-md5 units); 0 failures, 0 transport errors, no 429.

## Class A — v2 build (TAKE_HISTORY.md, 37 ledgered takes): 32/37 on CDN by downloaded md5; 5 local-only

| # | Take | Dataset path | Downloaded md5 (full) | Ledger match |
|---|---|---|---|---|
| 1 | S07 t1 (v2) | musicvideo/MV-7_the-nobody-man/takes/media-generation-mv7-s07-t1-0-2491c8cc-5254-4c13-9621-14a85c8da176.mp4 | 9f9a41cdea6d746387de655175b8729e | YES |
| 2 | S01 t1 (v2) | musicvideo/MV-7_the-nobody-man/takes/media-generation-mv7-s01-t1-0-5ed0bfcf-e950-4418-9a9e-fb26c6f43008.mp4 | 3f29a5e8670a91865af44059e14eb68f | YES |
| 3 | S02 t1 (v2) | musicvideo/MV-7_the-nobody-man/takes/media-generation-mv7-s02-t1-0-52866472-cc1e-4357-84d2-4210422550d4.mp4 | 56838020652558bbd07c3d3ec6539e92 | YES |
| 4 | S03 t1 (v2) | musicvideo/MV-7_the-nobody-man/takes/media-generation-mv7-s03-t1-0-a60a7857-1f80-4d05-a1b3-5dddb7c7781c.mp4 | bdbe8d744976861cc3f9c45dfe1c4e43 | YES |
| 5 | S04 t1 (v2) | musicvideo/MV-7_the-nobody-man/takes/media-generation-mv7-s04-t1-0-6cc10eaf-bba6-4ae1-a7d6-dd76a6176e17.mp4 | 23933f5a065ac2ef1e27eea4e297e941 | YES |
| 6 | S05 t1 (v2) | musicvideo/MV-7_the-nobody-man/takes/media-generation-mv7-s05-t1-0-79968a79-5115-4681-8ad5-5959655af7f7.mp4 | 22c5cd650e508075b5fc112e02c658c6 | YES |
| 7 | S01 t2 (v3) | musicvideo/MV-7_the-nobody-man/takes/media-generation-mv7v2-s01-v3-intro-chant-i1-so-0-8a128f27-bc6d-41bd-8315-1f246e5adc1f.mp4 | d6ffd61f7659fbe84d2a4ea6de0ba2f9 | YES |
| 8 | S05 t2 (v2) | musicvideo/MV-7_the-nobody-man/takes/media-generation-mv7v2-s05-v2-pre-chorus-1-pc1-0-2027fb19-64a4-4872-9fed-16acc838d6d0.mp4 | ca22497ecb174eb0d45b69bea19fd456 | YES |
| 9 | S06 t1 (v2) | musicvideo/MV-7_the-nobody-man/takes/media-generation-mv7v2-s06-pre-chorus-1-pc1-3-p-0-caec5eb5-e54a-4bff-b22d-a38f9f6a7e22.mp4 | b27f6c4c4a5dba8749cdbcaf322974c0 | YES |
| 10 | S08 t1 (v2) | musicvideo/MV-7_the-nobody-man/takes/media-generation-mv7v2-s08-chorus-1-c1-5-c1-7-s-0-f954d8e2-27f3-4924-a378-e19fdfdc8541.mp4 | b1a0b44ce3656029c78f186d7518f691 | YES |
| 11 | S09 t1 (v2) | musicvideo/MV-7_the-nobody-man/takes/media-generation-mv7v2-s09-chorus-1-c1-8-song-6-0-a3125b5e-d3e6-4343-91e6-e9e877b39a51.mp4 | 35717edfb9089a9a1921ceebad8c32ef | YES |
| 12 | S10 t1 (v2) | musicvideo/MV-7_the-nobody-man/takes/media-generation-mv7v2-s10-chorus-1-tag-chant-c-0-64689c53-7219-49f8-b5d2-f0839acce3b3.mp4 | 642211b3966a3887f4d1ea820a92d62b | YES |
| 13 | S01 t3 (v4) | — NOT IN DATASET — | — | local-only, see below |
| 14 | S05 t3a (v3a) | — NOT IN DATASET — | — | local-only, see below |
| 15 | S05 t3b (v3b) | — NOT IN DATASET — | — | local-only, see below |
| 16 | S08 t2 (v2) | — NOT IN DATASET — | — | local-only, see below |
| 17 | S09 t2 (v2) | — NOT IN DATASET — | — | local-only, see below |
| 18 | S11 t1 (v2) | musicvideo/MV-7_the-nobody-man/takes/media-generation-mv7v2-s11-verse-2-v2-1-v2-3-so-0-862f031f-fd6d-4d6c-8837-ea591826b343.mp4 | b90cc69e5c58f73e6cc698586de57871 | YES |
| 19 | S05 t4 (v4) | musicvideo/MV-7_the-nobody-man/takes/media-generation-mv7v2-s05-v4-pre-chorus-1-pc1-0-e4acbb70-b259-4c87-ab3f-54a3a31f8a64.mp4 | ac262c73da22068be632a47f1eabc851 | YES |
| 20 | S12 t1 (v2) | musicvideo/MV-7_the-nobody-man/takes/media-generation-mv7v2-s12-verse-2-v2-4-v2-6-so-0-3e5963f7-1461-459e-b0cd-3f2063aff438.mp4 | 13c8cd48372fab4c6470bca897247831 | YES |
| 21 | S13 t1 (v2) | musicvideo/MV-7_the-nobody-man/takes/media-generation-mv7v2-s13-pre-chorus-2-pc2-1-p-0-24146eaf-2c18-4e59-a8a6-f7c524112cc5.mp4 | 1585b73d8927540b7e38624def55b2dc | YES |
| 22 | S14 t1 (v2) | musicvideo/MV-7_the-nobody-man/takes/media-generation-mv7v2-s14-pre-chorus-2-pc2-3-p-0-7b5a8b0a-affc-4a1f-97ea-91f9b5a5a630.mp4 | 2043def7f8a057f53465d4aba34d1000 | YES |
| 23 | S15 t1 (v2) | musicvideo/MV-7_the-nobody-man/takes/media-generation-mv7v2-s15-chorus-2-c2-1-c2-4-s-0-ba6ce068-9c0e-43ac-95aa-f5e7bf4f15a7.mp4 | 432a95e2a70d7dada1a98752923b2dd4 | YES |
| 24 | S16 t1 (v2) | musicvideo/MV-7_the-nobody-man/takes/media-generation-mv7v2-s16-chorus-2-c2-5-c2-6-s-0-2c3694f8-072a-4efa-9288-76d7e4a9494c.mp4 | 9020aead4540165246264240a459c6b3 | YES |
| 25 | S12 t2 (v2) | musicvideo/MV-7_the-nobody-man/takes/media-generation-mv7v2-s12-v2-verse-2-v2-4-v2-6-0-1a61d504-11f7-48f5-a378-14e910f0385e.mp4 | 383a843492b1c954c08b2c6737a65f27 | YES |
| 26 | S13 t2 (v2) | musicvideo/MV-7_the-nobody-man/takes/media-generation-mv7v2-s13-v2-pre-chorus-2-pc2-0-7a93e8d9-7fa0-4a1d-a53a-987a4f2f0227.mp4 | 81933ac4945039cbe0411099bd854103 | YES |
| 27 | S15 t2 (v2) | musicvideo/MV-7_the-nobody-man/takes/media-generation-mv7v2-s15-v2-chorus-2-c2-1-c2-0-44875e3c-d6eb-4b26-8713-3466eebad9ff.mp4 | 43426ec08cbe01f83c5316d1ea37df09 | YES |
| 28 | S17 t1 (v2) | musicvideo/MV-7_the-nobody-man/takes/media-generation-mv7v2-s17-chorus-2-c2-7-c2-8-s-0-70773246-8933-4a21-a3b9-75bd80853392.mp4 | 5440c92c4aba9d1fffd69e0f72d41568 | YES |
| 29 | S18 t1 (v2) | musicvideo/MV-7_the-nobody-man/takes/media-generation-mv7v2-s18-bridge-montage-b1-b4-0-d8514bfa-9877-4564-9b2b-46582a9e311e.mp4 | 6bcdda44b63145084136ffcac40fcfb3 | YES |
| 30 | S19 t1 (v2) | musicvideo/MV-7_the-nobody-man/takes/media-generation-mv7v2-s19-bridge-montage-b5-b6-0-65c522dd-c352-4d26-bf5e-16784d68469f.mp4 | 15aade7b9bb5933b1b0190e974ff96f3 | YES |
| 31 | S20 t1 (v2) | musicvideo/MV-7_the-nobody-man/takes/media-generation-mv7v2-s20-final-chorus-fc1-fc4-0-95f874f2-e42c-4981-9b3a-4399014ab0f5.mp4 | 57a53cf02c1f3d7126660294ad82b18c | YES |
| 32 | S21 t1 (v2) | musicvideo/MV-7_the-nobody-man/takes/media-generation-mv7v2-s21-final-chorus-fc5-fc7-0-f901dd60-cd98-43d9-8ccb-be6c026ee373.mp4 | 8ffb5f4aa5dea56951e83ddd2e54d543 | YES |
| 33 | S22 t1 (v2) | musicvideo/MV-7_the-nobody-man/takes/media-generation-mv7v2-s22-final-chorus-fc8-fc9-0-8461ab5e-54b4-45ef-a0ba-e937660d824f.mp4 | 6ed121aeb20750219f000797e9848e39 | YES |
| 34 | S23 t1 (v2) | musicvideo/MV-7_the-nobody-man/takes/media-generation-mv7v2-s23-final-chorus-fc10-0-553c819f-bd9e-4823-ae36-e538adf3d0d7.mp4 | c07abd209f4836ed00cdef346882f615 | YES |
| 35 | S24 t1 (v2) | musicvideo/MV-7_the-nobody-man/takes/media-generation-mv7v2-s24-final-chorus-tag-cha-0-8a6124cb-18e1-44a4-a038-d3a768b78605.mp4 | de3d132ba3598dc8c2d336410c57a453 | YES |
| 36 | S20 t2 (v2) | musicvideo/MV-7_the-nobody-man/takes/media-generation-mv7v2-s20-t2-0-918d720a-9968-4d6a-ae48-b30351b503e5.mp4 | f80b133c10191def1508480136a40a8c | YES |
| 37 | S24 t2 (v2) | musicvideo/MV-7_the-nobody-man/takes/media-generation-mv7v2-s24-t2-0-c51ead16-af8d-41e9-9a23-9395fae4ad5f.mp4 | 2d9dd5ff1a6c81342925ae3f88909cd9 | YES |

## Class B — otaku build (46 ledgered takes): COMPLETE 46/46 on CDN by downloaded md5

| # | Take | Dataset path | Downloaded md5 (full) | Ledger match |
|---|---|---|---|---|
| 1 | U07 t1 | musicvideo/MV-7_the-nobody-man/takes/otaku/mv7o_u07_t1.mp4 | 8b722e90937097c859c1c8bf6f485e94 | YES |
| 2 | U08 t1 | musicvideo/MV-7_the-nobody-man/takes/otaku/mv7o_u08_t1.mp4 | d4b2147f73714a1113aee938119eae1e | YES |
| 3 | U09 t1 | musicvideo/MV-7_the-nobody-man/takes/otaku/mv7o_u09_t1.mp4 | c8aa1db53297cc5e1d3a9c1fb410f06e | YES |
| 4 | U10 t1 | musicvideo/MV-7_the-nobody-man/takes/otaku/mv7o_u10_t1.mp4 | 60874946585864e349b8117a14266486 | YES |
| 5 | U11 t1 | musicvideo/MV-7_the-nobody-man/takes/otaku/mv7o_u11_t1.mp4 | 7d87d91f5d0bef895be2c77aa35571b3 | YES — matches the recovery-volley ledger md5 (see dual-generation note) |
| 6 | U12 t1 | musicvideo/MV-7_the-nobody-man/takes/otaku/mv7o_u12_t1.mp4 | d9bae5132cff413ec4920293408ed871 | YES |
| 7 | U13 t1 | musicvideo/MV-7_the-nobody-man/takes/otaku/mv7o_u13_t1.mp4 | 2f0d6258278be5bd79f2bae206ef4eaa | YES |
| 8 | U14 t1 | musicvideo/MV-7_the-nobody-man/takes/otaku/mv7o_u14_t1.mp4 | b1bae31e539f2c4e950587e354fc42c0 | YES |
| 9 | U15 t1 | musicvideo/MV-7_the-nobody-man/takes/otaku/mv7o_u15_t1.mp4 | 6367b726ddbd1ff29448f1041ddd54b7 | YES |
| 10 | U16 t1 | musicvideo/MV-7_the-nobody-man/takes/otaku/mv7o_u16_t1.mp4 | 27571967063cf1d9fe24ed8e6abcaaec | YES |
| 11 | U17 t1 | musicvideo/MV-7_the-nobody-man/takes/otaku/mv7o_u17_t1.mp4 | 3372fa052b62765cdf063100361d02eb | YES |
| 12 | U18 t1 | musicvideo/MV-7_the-nobody-man/takes/otaku/mv7o_u18_t1.mp4 | 29d012f5e425351a053888ff4805a7a4 | YES — matches the recovery-volley ledger md5 (see dual-generation note) |
| 13 | U19 t1 | musicvideo/MV-7_the-nobody-man/takes/otaku/mv7o_u19_t1.mp4 | 62f504b6019f31d0e1fdb0cc91967707 | YES |
| 14 | U20 t1 | musicvideo/MV-7_the-nobody-man/takes/otaku/mv7o_u20_t1.mp4 | 35d2da887b479ec33492b868a410ed31 | YES |
| 15 | U21 t1 | musicvideo/MV-7_the-nobody-man/takes/otaku/mv7o_u21_t1.mp4 | 55f5ef0cffb77c45dd6ba8e0347c86bd | YES |
| 16 | U22 t1 | musicvideo/MV-7_the-nobody-man/takes/otaku/mv7o_u22_t1.mp4 | 6f57c8264bf1061fe7b81de6d53d83a9 | YES |
| 17 | U23 t1 | musicvideo/MV-7_the-nobody-man/takes/otaku/mv7o_u23_t1.mp4 | 149b50df61d06abb8ca62627795e7978 | YES |
| 18 | U24 t1 | musicvideo/MV-7_the-nobody-man/takes/otaku/mv7o_u24_t1.mp4 | 6290ea86bf04bdae75a1b82e4e92d652 | YES |
| 19 | U25 t1 | musicvideo/MV-7_the-nobody-man/takes/otaku/mv7o_u25_t1.mp4 | 7e6d06e07559d484cd846e18d433b307 | YES |
| 20 | U26 t1 | musicvideo/MV-7_the-nobody-man/takes/otaku/mv7o_u26_t1.mp4 | 5c09c7c3c1718818a3e67e276ca27943 | YES |
| 21 | U27 t1 | musicvideo/MV-7_the-nobody-man/takes/otaku/mv7o_u27_t1.mp4 | e7a071b4de4f93264bc9f253cd212a49 | YES |
| 22 | U28 t1 | musicvideo/MV-7_the-nobody-man/takes/otaku/mv7o_u28_t1.mp4 | ac2ea0a8cf7ea1ea76968c1bec59f409 | YES |
| 23 | U29 t1 | musicvideo/MV-7_the-nobody-man/takes/otaku/mv7o_u29_t1.mp4 | 82ec75000b6d250bedee2e37bb63fa90 | YES |
| 24 | U30 t1 | musicvideo/MV-7_the-nobody-man/takes/otaku/mv7o_u30_t1.mp4 | 84441cec2c9934b45cd62dd777c005f6 | YES |
| 25 | U31 t1 | musicvideo/MV-7_the-nobody-man/takes/otaku/mv7o_u31_t1.mp4 | 94efb90281ec8a0cb755b6d54758d269 | YES |
| 26 | U32 t1 | musicvideo/MV-7_the-nobody-man/takes/otaku/mv7o_u32_t1.mp4 | d4acd0ada14d5663eee265ce8c2fb413 | YES |
| 27 | U33 t1 | musicvideo/MV-7_the-nobody-man/takes/otaku/mv7o_u33_t1.mp4 | 759c569120d5dcbf5f0d03dc322203f9 | YES |
| 28 | U34 t1 | musicvideo/MV-7_the-nobody-man/takes/otaku/mv7o_u34_t1.mp4 | d358bbb9d2666c9bc4f32de44efa1d4d | YES |
| 29 | U35 t1 | musicvideo/MV-7_the-nobody-man/takes/otaku/mv7o_u35_t1.mp4 | 2c4d0392c71c3ffc02b633c9aeefcb67 | YES |
| 30 | U36 t1 | musicvideo/MV-7_the-nobody-man/takes/otaku/mv7o_u36_t1.mp4 | 725f008d66b1440bb6a1f4153abbf821 | YES |
| 31 | U37 t1 | musicvideo/MV-7_the-nobody-man/takes/otaku/mv7o_u37_t1.mp4 | 3e6970f40e0380025490c97637c9a730 | YES |
| 32 | U38 t1 | musicvideo/MV-7_the-nobody-man/takes/otaku/mv7o_u38_t1.mp4 | a29ecd90c1d46bb858150b6bb9677e45 | YES |
| 33 | U39 t1 | musicvideo/MV-7_the-nobody-man/takes/otaku/mv7o_u39_t1.mp4 | 8754cc863c3bf5682f7845b176b90e67 | YES |
| 34 | U40 t1 | musicvideo/MV-7_the-nobody-man/takes/otaku/mv7o_u40_t1.mp4 | 844b9201b56ce8fb921b5d2d1c418e75 | YES |
| 35 | U01 t1 | musicvideo/MV-7_the-nobody-man/takes/otaku/mv7o_u01_t1.mp4 | d148a2dc591a9c211f11e00c42b36cc4 | YES (ledger records 8-char prefix only) |
| 36 | U02 t1 | musicvideo/MV-7_the-nobody-man/takes/otaku/mv7o_u02_t1.mp4 | 82adf80e2f5373ba03b8727a0ef84245 | YES (ledger records 8-char prefix only) |
| 37 | U03 t1 | musicvideo/MV-7_the-nobody-man/takes/otaku/mv7o_u03_t1.mp4 | 862fcfa8fdbb9481ab5ab68169875900 | YES (ledger records 8-char prefix only) |
| 38 | U04 t1 | musicvideo/MV-7_the-nobody-man/takes/otaku/mv7o_u04_t1.mp4 | e4a04457f20cc1d7b25d8b5e453b19dd | YES (ledger records 8-char prefix only) |
| 39 | U05 t1 | musicvideo/MV-7_the-nobody-man/takes/otaku/mv7o_u05_t1.mp4 | 9a8ab7bd2f250ca34f2b919f7ee9c06c | YES (ledger records 8-char prefix only) |
| 40 | U06 t1 | musicvideo/MV-7_the-nobody-man/takes/otaku/mv7o_u06_t1.mp4 | af46d665f5b268adc05bee0d7e89ef05 | YES (ledger records 8-char prefix only) |
| 41 | U01 t2 | musicvideo/MV-7_the-nobody-man/takes/otaku/mv7o_u01_t2.mp4 | dacf28d7eb78d92208c55ac5db47f019 | YES |
| 42 | U19 t2 | musicvideo/MV-7_the-nobody-man/takes/otaku/mv7o_u19_t2.mp4 | ddad1d0614e4cb62d23913f86c5e52dc | YES |
| 43 | U24 t2 | musicvideo/MV-7_the-nobody-man/takes/otaku/mv7o_u24_t2.mp4 | 46876d777c29ee57f2c682a6d077407b | YES |
| 44 | U34 t2 | musicvideo/MV-7_the-nobody-man/takes/otaku/mv7o_u34_t2.mp4 | 09656768b73db3b491d00ff11d4f312d | YES |
| 45 | U35 t2 | musicvideo/MV-7_the-nobody-man/takes/otaku/mv7o_u35_t2.mp4 | 66fd3dee1f3c59fdc85d1d9b6e179c9f | YES |
| 46 | U39 t2 | musicvideo/MV-7_the-nobody-man/takes/otaku/mv7o_u39_t2.mp4 | 825b8131c7b3bef0b572f3c97b085901 | YES |

## Class C — rebuild2 build (26 ledgered takes): COMPLETE 26/26 on CDN by downloaded md5

| # | Take | Dataset path | Downloaded md5 (full) | Ledger match |
|---|---|---|---|---|
| 1 | R05a | musicvideo/MV-7_the-nobody-man/takes/rebuild2/mv7r2_r05a_t1.mp4 | ef3221b9e4743932e6aff222d0368e4a | YES |
| 2 | R05b | musicvideo/MV-7_the-nobody-man/takes/rebuild2/mv7r2_r05b_t1.mp4 | 573a5acb33fe6b6c5bf426f69fb2e2c8 | YES |
| 3 | R06a | musicvideo/MV-7_the-nobody-man/takes/rebuild2/mv7r2_r06a_t1.mp4 | 94aad1681d68895762765510ecfe2766 | YES |
| 4 | R06b | musicvideo/MV-7_the-nobody-man/takes/rebuild2/mv7r2_r06b_t1.mp4 | 757fac04f5407c13c78d2699071222b2 | YES |
| 5 | R08a | musicvideo/MV-7_the-nobody-man/takes/rebuild2/mv7r2_r08a_t1.mp4 | 59369bbc80e96dea39411f33d621962d | YES |
| 6 | R08b | musicvideo/MV-7_the-nobody-man/takes/rebuild2/mv7r2_r08b_t1.mp4 | 7976a910d169ea8a39a71b69ffd81fdd | YES |
| 7 | R14 | musicvideo/MV-7_the-nobody-man/takes/rebuild2/mv7r2_r14_t1.mp4 | 458bebbc0d34804c287e916236643d86 | YES |
| 8 | R15 | musicvideo/MV-7_the-nobody-man/takes/rebuild2/mv7r2_r15_t1.mp4 | 80073d064f37ae34984f95c431d83090 | YES |
| 9 | R16A | musicvideo/MV-7_the-nobody-man/takes/rebuild2/mv7r2_r16a_t1.mp4 | c71a7e3e85bc2460ce3c772c85774e0e | YES |
| 10 | R16B | musicvideo/MV-7_the-nobody-man/takes/rebuild2/mv7r2_r16b_t1.mp4 | 32b159f7087ad242701fa05326f85d82 | YES |
| 11 | R21A | musicvideo/MV-7_the-nobody-man/takes/rebuild2/mv7r2_r21a_t1.mp4 | 93731b6170fc7be2178082268b0f6c37 | YES |
| 12 | R21B | musicvideo/MV-7_the-nobody-man/takes/rebuild2/mv7r2_r21b_t1.mp4 | 2d5b4aeb9c4c2a3a9a765ef9ae3d989f | YES |
| 13 | R13A | musicvideo/MV-7_the-nobody-man/takes/rebuild2/mv7r2_r13a_t1.mp4 | 87fd2a4a1200a31d7344e7b988e4bdb3 | YES |
| 14 | R13B | musicvideo/MV-7_the-nobody-man/takes/rebuild2/mv7r2_r13b_t1.mp4 | 8106f08a7da85a1ed81b8628059238cf | YES |
| 15 | R17A | musicvideo/MV-7_the-nobody-man/takes/rebuild2/mv7r2_r17a_t1.mp4 | 7668bdc27907b048a35613f82e6d5087 | YES |
| 16 | R17B | musicvideo/MV-7_the-nobody-man/takes/rebuild2/mv7r2_r17b_t1.mp4 | d260a6cfb80ef3f9a4d671e2617c2a3c | YES |
| 17 | R22 | musicvideo/MV-7_the-nobody-man/takes/rebuild2/mv7r2_r22_t1.mp4 | db67865ea1d278707f327c69efec2420 | YES |
| 18 | R35 | musicvideo/MV-7_the-nobody-man/takes/rebuild2/mv7r2_r35_t1.mp4 | cdaf7e222c9b7373729872048891ff6d | YES |
| 19 | R18A | musicvideo/MV-7_the-nobody-man/takes/rebuild2/mv7r2_r18a_t1.mp4 | 661ea255e5910402f8470206819e8229 | YES |
| 20 | R18B | musicvideo/MV-7_the-nobody-man/takes/rebuild2/mv7r2_r18b_t1.mp4 | 26b1bc2bcd65ced401d8acb7fa3e2c83 | YES |
| 21 | R20A | musicvideo/MV-7_the-nobody-man/takes/rebuild2/mv7r2_r20a_t1.mp4 | ba624287600ca368cba7347b56bef899 | YES |
| 22 | R20B | musicvideo/MV-7_the-nobody-man/takes/rebuild2/mv7r2_r20b_t1.mp4 | fa89ee305f64801ae8d3e3fbb6396147 | YES |
| 23 | R32A | musicvideo/MV-7_the-nobody-man/takes/rebuild2/mv7r2_r32a_t1.mp4 | 5ac75d2215e07e69b28cbd65ba072377 | YES |
| 24 | R32B | musicvideo/MV-7_the-nobody-man/takes/rebuild2/mv7r2_r32b_t1.mp4 | 052e02066a39dc8a00a8a7d326470634 | YES |
| 25 | R34A | musicvideo/MV-7_the-nobody-man/takes/rebuild2/mv7r2_r34a_t1.mp4 | 8cc3ee4d4ea1d3fc937af8f83f727dfb | YES |
| 26 | R34B | musicvideo/MV-7_the-nobody-man/takes/rebuild2/mv7r2_r34b_t1.mp4 | 35e93fd36c4a5f2a8822f5c056ce3edd | YES |

## Dual-generation otaku units (U11, U17, U18)

Three otaku units carry TWO different ledger md5s for the same canonical
file: the first volley agent's report for U09–U12 was not backed by files
and volley 3's agent died mid-run, so recovery volleys 2b/3b re-fired
U11/U17/U18 and recorded new md5s (MV7_OTAKU_PROGRESS.md). The canonical
dataset file holds ONE generation; the download check proves the OTHER
generation also survives on the CDN as its media-generation original:

| Unit | Canonical file md5 (= generation) | Other generation md5 | Survives as dataset original |
|---|---|---|---|
| U11 t1 | 7d87d91f5d0bef895be2c77aa35571b3 (volley 2b) | 25f96a61f862c8906a469bf8d5536211 (volley 2) | takes/otaku/media-generation-mv7o-u11-0-1e665e57-2fbc-4f22-8052-d223bd41e6d1.mp4 — downloaded md5 identical |
| U17 t1 | 3372fa052b62765cdf063100361d02eb (volley 3b) | b28bf44f23c4d869e4bd6fa91e4c8bb6 (volley 3) | takes/otaku/media-generation-mv7o-u17-0-677436d3-e2b0-4722-9d09-ff2fc67485e4.mp4 — downloaded md5 identical |
| U18 t1 | 29d012f5e425351a053888ff4805a7a4 (volley 3b) | 07c01de66deb848b75585bfd615f7cbd (volley 3) | takes/otaku/media-generation-mv7o-u18-0-e5f0870f-b22f-4d41-a70d-983b75da90f1.mp4 — downloaded md5 identical |

No generation of any dual-recorded unit is lost.

## Not on the CDN — local-only survivors (5, all v2 build, all volley 3)

These five takes are absent from the dataset under every name (filename
token search across all 438 subtree files + exact-size search, both
negative). They are NOT lost: they are the five takes that survived the
cleanup locally, and their local md5s were re-verified against the ledger
in this run. They are, however, the only MV-7 takes with NO CDN backup —
a future cleanup that deletes them destroys them. Three of the five are
KEEP-WITH-FLAG takes used in the v2 assembly (S05 t3a, S08 t2, S09 t2).

| Take | File | Ledger md5 = local md5 | Ledger verdict |
|---|---|---|---|
| S01 t3 (v4) | takes/media-generation-mv7v2-s01-v4-intro-chant-i1-so-0-27ce3c0b-70af-433b-806d-6b832f16c405.mp4 | 9f8d2c3b8fdddac9c09ed92edf0aec3b | REJECT |
| S05 t3a (v3a) | takes/media-generation-mv7v2-s05-v3a-pre-chorus-1-pc1-0-69783a26-930b-4f00-bac2-d97001a694b3.mp4 | 0181fd7e25c2de8af39314ec4cc3dc5e | KEEP-WITH-FLAG |
| S05 t3b (v3b) | takes/media-generation-mv7v2-s05-v3b-pre-chorus-1-pc1-0-a936dfd3-e4bb-4fd0-a6c4-8565a72571e4.mp4 | 223844bc5b180bc9df91d14eadf22625 | REJECT |
| S08 t2 (v2) | takes/media-generation-mv7v2-s08-v2-chorus-1-c1-5-c1-0-485705b7-c49a-4e4e-a84e-6026abff5048.mp4 | c04f5f46cfd67c05352289a303711c0c | KEEP-WITH-FLAG |
| S09 t2 (v2) | takes/media-generation-mv7v2-s09-v2-chorus-1-c1-8-son-0-9eb3da14-e138-4ab0-9112-78f8178a9838.mp4 | 68a47b6e724cda3f2dfb1d61686a131d | KEEP-WITH-FLAG |

## Absences

NONE absent everywhere. Every one of the 109 ledgered take files exists
in at least one verified copy: 104 on the CDN (download-md5 verified) and
the remaining 5 as local survivors (md5 re-verified). Contrast MV-4
(s25t2 lost) and MV-17 (s06t1 lost) in the same cleanup event — MV-7 lost
nothing. Caveat: 6 otaku volley-1 takes (U01–U06 t1) are verified against
the only md5 evidence the project recorded for them — an 8-char prefix in
MV7_OTAKU_PROGRESS.md; their full downloaded md5s are in the Class B table
above and match those prefixes.

FINAL: COMPLETE with one flagged gap — 109 ledgered takes accounted for:
otaku 46/46 and rebuild2 26/26 fully CDN-verified by downloaded md5;
v2 32/37 CDN-verified by downloaded md5, remaining 5/37 verified as local
survivors but NOT CDN-backed (listed above — the only MV-7 takes a future
cleanup could still destroy). No MV-7 take is missing everywhere; nothing
was lost in the 2026-11-16 cleanup.
