# MV-19 'Confused NPC' — CDN takes verification (2026-11-17)

Question: the 2026-11-16 ~21:04 EST cleanup deleted all local take mp4s for MV-19
(cross-check 2026-11-17 01:40 EST: 52 ledgered take files missing locally, 40 KEEP +
12 REJECT; takes/ holds only media-generation JSON receipts). The stills-archive
coordinator's 2026-11-16 verdict said 'MV-19 COMPLETE — 48/48 tokens (52 files)',
leaving a 52-ledger-rows vs 48-tokens count mismatch to resolve.

Method (MV-18-proven): dataset tree API lfs.oid does NOT equal ledger md5s, so every
take was DOWNLOADED from WaefreBeorn/wubutv-network-media and md5-hashed; the hash's
first 8 chars were compared against the ledger's recorded md5 prefix in
TAKE_HISTORY.md. Dataset: musicvideo/MV-19_confused-npc/takes/<take>.mp4 (canonical
renamed paths). Read-only: downloads only, ledger untouched.

| # | Token | Ledger verdict | Dataset path | Downloaded md5 (full) | Prefix match |
|---|---|---|---|---|---|
| 1 | s01_t1 | KEEP | musicvideo/MV-19_confused-npc/takes/mv19_s01_t1.mp4 | ae67281f2c129df520d2d0100bb08032 | YES |
| 2 | s09_t1 | REJECT | musicvideo/MV-19_confused-npc/takes/mv19_s09_t1.mp4 | d2a1f7cf655db0ad28c0efe5476ae769 | YES |
| 3 | s11_t1 | REJECT (motion) | musicvideo/MV-19_confused-npc/takes/mv19_s11_t1.mp4 | 9734a0a4949c1b1a73f10c008021f7c6 | YES |
| 4 | s09_t2 | KEEP | musicvideo/MV-19_confused-npc/takes/mv19_s09_t2.mp4 | f0bdc8338d2ef94ced433ca727e47c85 | YES |
| 5 | s11_t2 | KEEP* (flagged) | musicvideo/MV-19_confused-npc/takes/mv19_s11_t2.mp4 | bc60c27b34df8c8d565222c9b441942f | YES |
| 6 | s02_t1 | KEEP | musicvideo/MV-19_confused-npc/takes/mv19_s02_t1.mp4 | 8aeae4548032c30e313c0df9f3ed20b3 | YES |
| 7 | s03_t1 | REJECT (motion) | musicvideo/MV-19_confused-npc/takes/mv19_s03_t1.mp4 | d6feec1d0a6b2a04cb55d0aeaadc1f47 | YES |
| 8 | s04_t1 | KEEP | musicvideo/MV-19_confused-npc/takes/mv19_s04_t1.mp4 | 2c08b3914e12836d9dc9697470160839 | YES |
| 9 | s05_t1 | KEEP | musicvideo/MV-19_confused-npc/takes/mv19_s05_t1.mp4 | 425c21d3d824f54e35d3cb1b57b4b012 | YES |
| 10 | s06_t1 | KEEP* (flagged) | musicvideo/MV-19_confused-npc/takes/mv19_s06_t1.mp4 | d2122d73549d7d3263a2bb3b28897ed1 | YES |
| 11 | s08_t1 | KEEP | musicvideo/MV-19_confused-npc/takes/mv19_s08_t1.mp4 | ee20523290f54e376e1d19ee02b05407 | YES |
| 12 | s07_t1 | KEEP | musicvideo/MV-19_confused-npc/takes/mv19_s07_t1.mp4 | 7671a45959aca60932473a235dc3bcef | YES |
| 13 | s10_t1 | KEEP | musicvideo/MV-19_confused-npc/takes/mv19_s10_t1.mp4 | e3249132e2981cb7977c8cb1fd4ddad6 | YES |
| 14 | s12_t1 | KEEP | musicvideo/MV-19_confused-npc/takes/mv19_s12_t1.mp4 | a104d67b2563d2ecd1900ac7549a6766 | YES |
| 15 | s13_t1 | KEEP (L16 only) | musicvideo/MV-19_confused-npc/takes/mv19_s13_t1.mp4 | 12dbb33425e7aeff074c1f062189569b | YES |
| 16 | s03_t2 | KEEP | musicvideo/MV-19_confused-npc/takes/mv19_s03_t2.mp4 | 6330f82f1184f3d880b2998686d0454e | YES |
| 17 | s14_t1 | KEEP | musicvideo/MV-19_confused-npc/takes/mv19_s14_t1.mp4 | c801bb8d57f936f25fc0721b9807b881 | YES |
| 18 | s15_t1 | REJECT (G2 + motion) | musicvideo/MV-19_confused-npc/takes/mv19_s15_t1.mp4 | fd5fa6b7eba734c375be98202db38ca3 | YES |
| 19 | s16_t1 | KEEP | musicvideo/MV-19_confused-npc/takes/mv19_s16_t1.mp4 | b7908e44e3b5e233b80685f8db79f750 | YES |
| 20 | s17_t1 | KEEP | musicvideo/MV-19_confused-npc/takes/mv19_s17_t1.mp4 | 617581df40b1170149c3eb4f0c6251a1 | YES |
| 21 | s13b_t1 | KEEP | musicvideo/MV-19_confused-npc/takes/mv19_s13b_t1.mp4 | 5663894c72210c8255a32159a511b7a3 | YES |
| 22 | s15_t2 | KEEP | musicvideo/MV-19_confused-npc/takes/mv19_s15_t2.mp4 | 1c1a049f43e86664b307423edee9f133 | YES |
| 23 | s18_t1 | KEEP | musicvideo/MV-19_confused-npc/takes/mv19_s18_t1.mp4 | 266c730a6740e442510baf93f89df19c | YES |
| 24 | s19_t1 | REJECT (motion/event) | musicvideo/MV-19_confused-npc/takes/mv19_s19_t1.mp4 | 3dfc74a27559ff088cb79194a50de7a2 | YES |
| 25 | s20_t1 | KEEP | musicvideo/MV-19_confused-npc/takes/mv19_s20_t1.mp4 | b0fc66be37fe1e4f070e1145423537f1 | YES |
| 26 | s21_t1 | KEEP* (flagged) | musicvideo/MV-19_confused-npc/takes/mv19_s21_t1.mp4 | bb8ff9ce1f42b7776935f93bf5fc042a | YES |
| 27 | s22_t1 | KEEP | musicvideo/MV-19_confused-npc/takes/mv19_s22_t1.mp4 | f82986e625defe9ece160d670c7bcdb6 | YES |
| 28 | s23_t1 | REJECT (event) | musicvideo/MV-19_confused-npc/takes/mv19_s23_t1.mp4 | 88f7cc0e5667a8019786a316b66af78b | YES |
| 29 | s24_t1 | KEEP | musicvideo/MV-19_confused-npc/takes/mv19_s24_t1.mp4 | 2b7a4fdc7d41837142632ccb54ee250f | YES |
| 30 | s25_t1 | KEEP (L31 only) | musicvideo/MV-19_confused-npc/takes/mv19_s25_t1.mp4 | ce14a642af3096526a805e458f407338 | YES |
| 31 | s26_t1 | KEEP | musicvideo/MV-19_confused-npc/takes/mv19_s26_t1.mp4 | 7f0c89fe64a5136ea45187729540c6eb | YES |
| 32 | s27_t1 | KEEP* (flagged) | musicvideo/MV-19_confused-npc/takes/mv19_s27_t1.mp4 | 47e55bcf0d54d2dded3cc7cca7b7267f | YES |
| 33 | s28_t1 | KEEP (L35+L36) | musicvideo/MV-19_confused-npc/takes/mv19_s28_t1.mp4 | 4ded487e1ed639989236d5037688b064 | YES |
| 34 | s19_t2 | KEEP (L22 only) | musicvideo/MV-19_confused-npc/takes/mv19_s19_t2.mp4 | 3c9c808b93a90d60ddada3b066adf332 | YES |
| 35 | s23_t2 | REJECT (motion) | musicvideo/MV-19_confused-npc/takes/mv19_s23_t2.mp4 | 02cba7926e57f5ee8d970391df3b1751 | YES |
| 36 | s25b_t1 | KEEP | musicvideo/MV-19_confused-npc/takes/mv19_s25b_t1.mp4 | 53e2b8a7221346d887ee081306e05dfb | YES |
| 37 | s28b_t1 | KEEP | musicvideo/MV-19_confused-npc/takes/mv19_s28b_t1.mp4 | 76a3969c79c12f26b2608b3f5d53f205 | YES |
| 38 | s29_t1 | KEEP* (flagged) | musicvideo/MV-19_confused-npc/takes/mv19_s29_t1.mp4 | bf9f01827669d814c1b76992ef70a678 | YES |
| 39 | s30_t1 | KEEP | musicvideo/MV-19_confused-npc/takes/mv19_s30_t1.mp4 | b76ab153cc6e048d368b2b21d3038f80 | YES |
| 40 | s19b_t1 | KEEP | musicvideo/MV-19_confused-npc/takes/mv19_s19b_t1.mp4 | 5f7f2b58b2fb42aab33ceba226ed0cc3 | YES |
| 41 | s23_t3 | KEEP* (flagged) | musicvideo/MV-19_confused-npc/takes/mv19_s23_t3.mp4 | 14b66758f466b25ca9bdfbda08f26920 | YES |
| 42 | s31_t1 | REJECT (cast) | musicvideo/MV-19_confused-npc/takes/mv19_s31_t1.mp4 | 1e5eaeffcc5c4d0222c44d5a1cc6379f | YES |
| 43 | s32_t1 | KEEP | musicvideo/MV-19_confused-npc/takes/mv19_s32_t1.mp4 | c016de69f57cedbbddc73964e059589e | YES |
| 44 | s33_t1 | KEEP* (flagged) | musicvideo/MV-19_confused-npc/takes/mv19_s33_t1.mp4 | 9821ae20c09d9181b8fb9953150b0da9 | YES |
| 45 | s34_t1 | REJECT (motion) | musicvideo/MV-19_confused-npc/takes/mv19_s34_t1.mp4 | 002db08221353164c456186027228fee | YES |
| 46 | s35_t1 | KEEP | musicvideo/MV-19_confused-npc/takes/mv19_s35_t1.mp4 | acef86f2f60e1a63ffc9fb3786645193 | YES |
| 47 | s36_t1 | KEEP | musicvideo/MV-19_confused-npc/takes/mv19_s36_t1.mp4 | 6f9c399fe4ca8992d70cc1a7a9eb2866 | YES |
| 48 | s31_t2 | REJECT (cast) | musicvideo/MV-19_confused-npc/takes/mv19_s31_t2.mp4 | 0e7192817499699c5aa21b390369cf0e | YES |
| 49 | s31_t3 | REJECT (cast/cut) | musicvideo/MV-19_confused-npc/takes/mv19_s31_t3.mp4 | ba1d1a8adbe3954e9bd66270b618d1dd | YES |
| 50 | s31_t5 | KEEP | musicvideo/MV-19_confused-npc/takes/mv19_s31_t5.mp4 | 29ea4f66b06a7994024ddf19612b425b | YES |
| 51 | s31_t4 | REJECT (cast + motion) | musicvideo/MV-19_confused-npc/takes/mv19_s31_t4.mp4 | af6f6ee534804c9302383db67d375c91 | YES |
| 52 | s34_t2 | KEEP (disclosed flaw) | musicvideo/MV-19_confused-npc/takes/mv19_s34_t2.mp4 | 86e5cde7e0ad5d4fa508d456582d1481 | YES |

Ledger split verified: 40 KEEP-family rows + 12 REJECT rows = 52 rows.

## The 52-vs-48 question — RESOLVED

The dataset takes/ folder holds exactly 52 take files, and all 52 download-verify
against the ledger (52/52 prefix matches above) — including all 12 REJECT takes.
Nothing is absent, so no token had to be declared missing and no dual-naming or
shared-file accounting is involved: the mapping is one ledger row → one dataset
file → one md5 match, 52 times.

The '48' in the earlier verdict is a token-counting artifact on the coordinator's
side (its own line reads '48/48 tokens (52 files)' — it counted 52 FILES in the
dataset but only 48 TOKENS). The only group of exactly 4 among the 52 ledgered
takes that a strict sXX_tY token pattern (two digits, no letter suffix) would fail
to capture is the four split-scene 'B' takes:

- s13b_t1 (S13B The Self-Remote) — present, md5 5663894c… match
- s19b_t1 (S19B The Second Shrug) — present, md5 5f7f2b58… match
- s25b_t1 (S25B The Desync) — present, md5 53e2b8a7… match
- s28b_t1 (S28B The Empty Hands) — present, md5 76a3969c… match

52 − 4 = 48: drop those four from both sides of a token comparison and it reports
48/48 while the folder still holds 52 files. All four are verified present above,
so the discrepancy was in the counting pattern, not in the backup.

Dataset subtree note: musicvideo/MV-19_confused-npc/ holds 54 files total — the 52
takes plus masters/mv19_confused_npc_chat.mp4 and track.mp4.

FINAL: COMPLETE 52/52 — every ledgered MV-19 take (40 KEEP + 12 REJECT) is present
on the CDN dataset and content-verified by downloaded md5 against the ledger.
