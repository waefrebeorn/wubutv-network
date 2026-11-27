# MV-20 'Laundry Life' — CDN takes verification (2026-11-17)

Question: the 2026-11-16 ~21:04 EST cleanup deleted MV-20's local take mp4s
(cross-check 2026-11-17 02:40 EST: 32 of 33 unique KEEP takes in TAKE_HISTORY.md
missing from disk; only mv20_s29_t2.mp4 remains locally and md5-verifies, prefix
0abfbbca; takes/ holds 40 media-generation JSON receipts). Masters intact and
flag-verified (house md5 1d59b572ba292cd63b80dabb680f23ec). Were the deleted
KEEP takes backed up on the CDN before the cleanup?

Method (MV-18/MV-19-proven): dataset tree API lfs.oid does NOT equal ledger md5s,
so every take was DOWNLOADED from WaefreBeorn/wubutv-network-media and md5-hashed;
the hash's first 8 chars were compared against the ledger's recorded md5 prefix in
TAKE_HISTORY.md. Dataset: musicvideo/MV-20_laundry-life/takes/<take>.mp4
(canonical renamed paths). Read-only: downloads only, ledger untouched.

Scope: the 33 unique KEEP takes, plus the S23 special case (s23_t1/s23_t2 are
ledgered SPARE, but CUTLIST shipped s23_t1 — a pending user decision; both are
swept and reported, ledger NOT edited). The four other SPARE takes present in the
dataset (s07_t1, s08_t1, s13_t1, s29_t1) were also download-verified so the sweep
covers every take file in the dataset folder.

| # | Token | Ledger verdict | Dataset path | Downloaded md5 (full) | Prefix match |
|---|---|---|---|---|---|
| 1 | s01_t1 | KEEP | musicvideo/MV-20_laundry-life/takes/mv20_s01_t1.mp4 | 22d942d46051bbb22ca084621fa50d59 | YES |
| 2 | s03_t1 | KEEP | musicvideo/MV-20_laundry-life/takes/mv20_s03_t1.mp4 | 9e02a5b1b62ae6693e9d85f67fad065f | YES |
| 3 | s05_t1 | KEEP | musicvideo/MV-20_laundry-life/takes/mv20_s05_t1.mp4 | 592000cc6f3a4acdbbde41dad47b4283 | YES |
| 4 | s09_t1 | KEEP | musicvideo/MV-20_laundry-life/takes/mv20_s09_t1.mp4 | 56c1819bc10c2411cfc2408c40961af9 | YES |
| 5 | s02_t1 | KEEP | musicvideo/MV-20_laundry-life/takes/mv20_s02_t1.mp4 | 4750a9c5e295b8505d22c8e35e6da741 | YES |
| 6 | s04_t1 | KEEP | musicvideo/MV-20_laundry-life/takes/mv20_s04_t1.mp4 | b6df9f4cfc6d6dac4d9786c9b980e74c | YES |
| 7 | s06_t1 | KEEP | musicvideo/MV-20_laundry-life/takes/mv20_s06_t1.mp4 | a66103f490f42849490cd5f08812dccf | YES |
| 8 | s10_t1 | KEEP | musicvideo/MV-20_laundry-life/takes/mv20_s10_t1.mp4 | 250b6d8dcbbccefee1bfd07d9ef187df | YES |
| 9 | s11_t1 | KEEP | musicvideo/MV-20_laundry-life/takes/mv20_s11_t1.mp4 | d4b6beeaba2e92f6e76efea40da23207 | YES |
| 10 | s12_t1 | KEEP | musicvideo/MV-20_laundry-life/takes/mv20_s12_t1.mp4 | 4f6115ba304275107b33cdd45b6b25cf | YES |
| 11 | s14_t1 | KEEP | musicvideo/MV-20_laundry-life/takes/mv20_s14_t1.mp4 | 7d755f9e323b76cc8e3f25d30a67852 | YES |
| 12 | s15_t1 | KEEP | musicvideo/MV-20_laundry-life/takes/mv20_s15_t1.mp4 | 1e44453907edbb26a0e71889216c83f3 | YES |
| 13 | s13_t2 | KEEP as S13 | musicvideo/MV-20_laundry-life/takes/mv20_s13_t2.mp4 | 50ce74597569c2a4bb5949972249148d | YES |
| 14 | s07_t2 | KEEP as S07 | musicvideo/MV-20_laundry-life/takes/mv20_s07_t2.mp4 | 920fb446ff7d538c034eab21b00cc698 | YES |
| 15 | s16_t1 | KEEP | musicvideo/MV-20_laundry-life/takes/mv20_s16_t1.mp4 | 619e2a5d0be9f23e6218f0a75265fc60 | YES |
| 16 | s17_t1 | KEEP as S17 | musicvideo/MV-20_laundry-life/takes/mv20_s17_t1.mp4 | 3d3da24e2a08470b5273f15bfa16e1c0 | YES |
| 17 | s18_t1 | KEEP as S18 | musicvideo/MV-20_laundry-life/takes/mv20_s18_t1.mp4 | d80fc3acf2f1ce2d7fae7473a8262470 | YES |
| 18 | s19_t1 | KEEP | musicvideo/MV-20_laundry-life/takes/mv20_s19_t1.mp4 | fbf155333b4fa3352d50e0a9a0160ba8 | YES |
| 19 | s08_t2 | KEEP | musicvideo/MV-20_laundry-life/takes/mv20_s08_t2.mp4 | 796b617cada2b934d0f2497cb793b068 | YES |
| 20 | s13b_t1 | KEEP | musicvideo/MV-20_laundry-life/takes/mv20_s13b_t1.mp4 | 5a0d861e42b3bad82c7d006bfed1e1f6 | YES |
| 21 | s20_t1 | KEEP | musicvideo/MV-20_laundry-life/takes/mv20_s20_t1.mp4 | 1dcda444b911aca52e4b3855a80932eb | YES |
| 22 | s21_t1 | KEEP | musicvideo/MV-20_laundry-life/takes/mv20_s21_t1.mp4 | bbe14429fbd2fe52974ccd68893711b4 | YES |
| 23 | s22_t1 | KEEP | musicvideo/MV-20_laundry-life/takes/mv20_s22_t1.mp4 | cda942e951ae6aa1dffbf26cbdd9edbc | YES |
| 24 | s07b_t1 | KEEP | musicvideo/MV-20_laundry-life/takes/mv20_s07b_t1.mp4 | c558035c12e05a8d0f570e969b81072d | YES |
| 25 | s17b_t1 | KEEP | musicvideo/MV-20_laundry-life/takes/mv20_s17b_t1.mp4 | b41296394d10b1f55afe15cab0c16331 | YES |
| 26 | s18b_t1 | KEEP | musicvideo/MV-20_laundry-life/takes/mv20_s18b_t1.mp4 | 4139214c996322d4eff2c79db22f3324 | YES |
| 27 | s24_t1 | KEEP | musicvideo/MV-20_laundry-life/takes/mv20_s24_t1.mp4 | 6980227374eec7c3301ec8ef06fbce83 | YES |
| 28 | s25_t1 | KEEP | musicvideo/MV-20_laundry-life/takes/mv20_s25_t1.mp4 | 85a4bef30e329d9b0ae4259fcf264c67 | YES |
| 29 | s26_t1 | KEEP | musicvideo/MV-20_laundry-life/takes/mv20_s26_t1.mp4 | b5287da0acd297c87b4e13263e50a41f | YES |
| 30 | s27_t1 | KEEP | musicvideo/MV-20_laundry-life/takes/mv20_s27_t1.mp4 | da29ff900336f230f1f144905d23d3f9 | YES |
| 31 | s28_t1 | KEEP | musicvideo/MV-20_laundry-life/takes/mv20_s28_t1.mp4 | 7a8eb9da608bd62e7b599613b11be85a | YES |
| 32 | s29_t2 | KEEP | ABSENT from dataset (see below) | — (local file: 0abfbbca32e140b587de353bfeaaa56d) | local YES |
| 33 | s30_t1 | KEEP (hand-check override) | musicvideo/MV-20_laundry-life/takes/mv20_s30_t1.mp4 | 6cbc9854e2b312f4c8bbb83394fc7680 | YES |

## S23 special case (ledgered SPARE; CUTLIST shipped s23_t1 — pending user decision, ledger untouched)

| Token | Ledger verdict | Dataset path | Downloaded md5 (full) | Prefix match |
|---|---|---|---|---|
| s23_t1 | SPARE (shipped per CUTLIST) | musicvideo/MV-20_laundry-life/takes/mv20_s23_t1.mp4 | d0dffad6d338a795d09a3ecfaa84eac7 | YES |
| s23_t2 | SPARE | musicvideo/MV-20_laundry-life/takes/mv20_s23_t2.mp4 | 25c1fba43fdd42fa960c7f3bdf0851d2 | YES |

Both S23 takes are on the CDN and content-verified, so whichever way the pending
S23 ledger decision lands, the shipped take (t1) is backed up.

## Other SPARE takes present in the dataset (also download-verified)

| Token | Dataset path | Downloaded md5 (full) | Prefix match |
|---|---|---|---|
| s07_t1 | musicvideo/MV-20_laundry-life/takes/mv20_s07_t1.mp4 | 4c3a11772c3c6a5eaa2f7a6de3f5bbfb | YES |
| s08_t1 | musicvideo/MV-20_laundry-life/takes/mv20_s08_t1.mp4 | 50377526e03c6365346e319b428b5150 | YES |
| s13_t1 | musicvideo/MV-20_laundry-life/takes/mv20_s13_t1.mp4 | 75705fc883d77ce35096a94383db6a84 | YES |
| s29_t1 | musicvideo/MV-20_laundry-life/takes/mv20_s29_t1.mp4 | f52721327cfcbf2878221683f0cc903c | YES |

In total the dataset takes/ folder holds 38 of MV-20's 39 unique ledgered takes,
and all 38 download-verify against the ledger (38/38 prefix matches).

## The one absence: s29_t2

s29_t2 (KEEP, Truce Sit) is the ONLY ledgered take with no video file on the CDN:

- Not in musicvideo/MV-20_laundry-life/takes/ (which holds s29_t1, the SPARE).
- Whole-dataset search (18,129 files, listed 2026-11-17): the only path containing
  's29_t2' anywhere in WaefreBeorn/wubutv-network-media is
  stills/musicvideo/MV-20_laundry-life/work/qc/s29_t2_sheet.jpg — the QC contact
  sheet, not the take. No mv20_s29_t2.mp4 and no media-generation original of the
  take exists anywhere in the dataset.

It is NOT lost: s29_t2 is the single KEEP take the cleanup did not delete. The
local file takes/mv20_s29_t2.mp4 was md5'd during this verification:
0abfbbca32e140b587de353bfeaaa56d — prefix 0abfbbca matches the ledger exactly.
The split is exactly complementary: the 32 KEEP takes deleted locally are all on
the CDN; the 1 KEEP take missing from the CDN is the 1 that survives locally.
s29_t2 should ride the next CDN sync so both copies exist in both places — it is
flagged here, not uploaded (this verification is read-only toward the dataset).

Dataset subtree note: musicvideo/MV-20_laundry-life/ holds 42 files — the 38
takes above plus masters/mv20_laundry_life_16x9.mp4,
masters/mv20_laundry_life_chat.mp4, track.mp4, and work/master_pregrain.mp4.

FINAL: COMPLETE 32/33 on the CDN — every cleanup-deleted MV-20 KEEP take is
present on the dataset and content-verified by downloaded md5 against the ledger;
absent from the dataset: s29_t2 only, which survives locally (md5-verified), so
combined local + CDN coverage is 33/33 and nothing is lost.
