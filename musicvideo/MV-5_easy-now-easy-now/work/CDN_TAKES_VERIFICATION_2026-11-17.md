# MV-5 'Easy now, easy now' — CDN takes verification (2026-11-17)

Question: the 2026-11-16 ~21:04 EST cleanup deleted MV-5's local take mp4s
(cross-check 2026-11-17 07:40 EST: all 76 TAKE_HISTORY.md take files with
recorded md5s missing from disk — 30 KEEP, 45 REJECT, 1 DISCARDED; takes/ held
only 83 media-generation JSON receipts + the 2 surviving Q10 mp4s; Q10 KEEP
mv5_q10_s07_l15.mp4 also missing; 30 of 43 v6 assembly takes missing from
work/rebuild-v6/takes/). Masters intact and flag-verified (v6 APPROVED master
is the current cut). Were the deleted takes backed up on the CDN first?

Method (MV-18/MV-19/MV-20-proven): dataset tree API lfs.oid does NOT equal
ledger md5s, so every in-scope file was DOWNLOADED from
WaefreBeorn/wubutv-network-media and md5-hashed; the downloaded md5 was
compared against the ledger's recorded md5 (TAKE_HISTORY.md / Q10_LEDGER.md).
Dataset paths are the mirrored project tree under
musicvideo/MV-5_easy-now-easy-now/. Read-only: downloads only, ledgers untouched.
153 download-md5 jobs run; 0 failures, 0 mismatches, 0 absences.

## Class A — TAKE_HISTORY KEEPs (30): COMPLETE 30/30

| # | Token | Dataset path | Downloaded md5 (full) | Ledger match |
|---|---|---|---|---|
| 1 | mv5_s01_t1 | musicvideo/MV-5_easy-now-easy-now/takes/mv5_s01_t1.mp4 | 1ccf23810114ebbc0558963022d84be0 | YES |
| 2 | mv5_s02_t1 | musicvideo/MV-5_easy-now-easy-now/takes/mv5_s02_t1.mp4 | 4b5de2bbc7ef3ae7b52455095bfd887d | YES |
| 3 | mv5_s03_t1 | musicvideo/MV-5_easy-now-easy-now/takes/mv5_s03_t1.mp4 | 1023ea5f3b705f550d3a6d689b1ff1da | YES |
| 4 | mv5_s04_t1 | musicvideo/MV-5_easy-now-easy-now/takes/mv5_s04_t1.mp4 | ce26e873bd40f2b6058057a427e42f75 | YES |
| 5 | mv5_s05_t1 | musicvideo/MV-5_easy-now-easy-now/takes/mv5_s05_t1.mp4 | 4557cd06fc514e0dd31decc17e1f6514 | YES |
| 6 | mv5_s06_t1 | musicvideo/MV-5_easy-now-easy-now/takes/mv5_s06_t1.mp4 | bc19ed1009cd1324c1135def0f6194ec | YES |
| 7 | mv5_s07_t1 | musicvideo/MV-5_easy-now-easy-now/takes/mv5_s07_t1.mp4 | 3bdd0f48a7999696b27a6c4e1e0da7f2 | YES |
| 8 | mv5_s08_t2 | musicvideo/MV-5_easy-now-easy-now/takes/mv5_s08_t2.mp4 | fc07dcacf30e91cdcd98a89b5148760e | YES |
| 9 | mv5_s09_t1 | musicvideo/MV-5_easy-now-easy-now/takes/mv5_s09_t1.mp4 | 37c3ffb0da3982331bbb4ac2547bd991 | YES |
| 10 | mv5_s10_t1 | musicvideo/MV-5_easy-now-easy-now/takes/mv5_s10_t1.mp4 | 89830a0407ad9c8cafff1879e0dbc548 | YES |
| 11 | mv5_s12_t1 | musicvideo/MV-5_easy-now-easy-now/takes/mv5_s12_t1.mp4 | 4202db31b66386a7979143f587f91119 | YES |
| 12 | mv5_s15_t1 | musicvideo/MV-5_easy-now-easy-now/takes/mv5_s15_t1.mp4 | 72332ff6ccc1839d6c4d5db629a0562a | YES |
| 13 | mv5_s17_t1 | musicvideo/MV-5_easy-now-easy-now/takes/mv5_s17_t1.mp4 | c239ec5925bc66710e080e9b62bb1ff1 | YES |
| 14 | mv5_s18_t1 | musicvideo/MV-5_easy-now-easy-now/takes/mv5_s18_t1.mp4 | 5747e5443e07633313dae30c5486a58f | YES |
| 15 | mv5_s11_t4 | musicvideo/MV-5_easy-now-easy-now/takes/mv5_s11_t4.mp4 | a0321de04e78cc1746d0db4fee9aa626 | YES |
| 16 | mv5_s20_t1 | musicvideo/MV-5_easy-now-easy-now/takes/mv5_s20_t1.mp4 | ebfeb2a65108ad1986e7195aa20b6ca1 | YES |
| 17 | mv5_s23_t1 | musicvideo/MV-5_easy-now-easy-now/takes/mv5_s23_t1.mp4 | 65e471e3cf7c9744a67dd407f2785c1f | YES |
| 18 | mv5_s19b_t1 | musicvideo/MV-5_easy-now-easy-now/takes/mv5_s19b_t1.mp4 | ca4254360cfca2e940c1055cefcbdf90 | YES |
| 19 | mv5_s25_t1 | musicvideo/MV-5_easy-now-easy-now/takes/mv5_s25_t1.mp4 | 008a1934e8a2340b1441e4ddfdec9550 | YES |
| 20 | mv5_s26_t1 | musicvideo/MV-5_easy-now-easy-now/takes/mv5_s26_t1.mp4 | 597218f1dc8282ebefc2fc2253edb4d0 | YES |
| 21 | mv5_s27_t1 | musicvideo/MV-5_easy-now-easy-now/takes/mv5_s27_t1.mp4 | fdc6c6c02e1bf36178294117a4dc2b5b | YES |
| 22 | mv5_s28_t1 | musicvideo/MV-5_easy-now-easy-now/takes/mv5_s28_t1.mp4 | c4030af7f9ab17548d137cd7cbcac652 | YES |
| 23 | mv5_s06_t2 | musicvideo/MV-5_easy-now-easy-now/takes/mv5_s06_t2.mp4 | 5507f6a2875f90bdcc9aa19a51b08762 | YES |
| 24 | mv5_s21_t7 | musicvideo/MV-5_easy-now-easy-now/takes/mv5_s21_t7.mp4 | 81663fbac6114f35f920a9f77049209f | YES |
| 25 | mv5_s21_t11 | musicvideo/MV-5_easy-now-easy-now/takes/mv5_s21_t11.mp4 | 4b91522f554a2893fa3f164197c14873 | YES |
| 26 | mv5_s21_t12 | musicvideo/MV-5_easy-now-easy-now/takes/mv5_s21_t12.mp4 | f2de5e0d8bb254dd5be590b92226457a | YES |
| 27 | mv5_s21_t13 | musicvideo/MV-5_easy-now-easy-now/takes/mv5_s21_t13.mp4 | 479a404a34c327ccf57088882f670599 | YES |
| 28 | mv5_s21_t14 | musicvideo/MV-5_easy-now-easy-now/takes/mv5_s21_t14.mp4 | 3d047b2b662dafa6820f13adbc62f904 | YES |
| 29 | mv5_s21_t15 | musicvideo/MV-5_easy-now-easy-now/takes/mv5_s21_t15.mp4 | be27fe25d38dd0a5da532b6064469d66 | YES |
| 30 | mv5_s21_t16 | musicvideo/MV-5_easy-now-easy-now/takes/mv5_s21_t16.mp4 | c60c1e452c116fa0ee27582add1fe5f7 | YES |

Bonus sweep — the other 46 ledgered takes (45 REJECT + 1 DISCARDED) were
download-verified the same way: **46/46 present and md5-identical to the
ledger**. The dataset therefore holds the complete TAKE_HISTORY set, 76/76.

## Class B — Q10 KEEPs (3): COMPLETE 3/3

| Token | Dataset path | Downloaded md5 (full) | Ledger match |
|---|---|---|---|
| mv5_q10_s07_l15 | musicvideo/MV-5_easy-now-easy-now/takes/mv5_q10_s07_l15.mp4 | 0f77772d71ab921c599376a95ffc0693 | YES |
| mv5_q10_s07_l15 (2nd copy) | musicvideo/MV-5_easy-now-easy-now/work/q10/takes/mv5_q10_s07_l15.mp4 | 0f77772d71ab921c599376a95ffc0693 | YES |
| mv5_q10_s04 (media-generation original) | musicvideo/MV-5_easy-now-easy-now/work/q10/takes/media-generation-mv5-q10-s04-0-de3b228a-87cd-4d96-ba4c-1d1f1d89607f.mp4 | 9a0d1ae15f0335b4400736bed07ccdaf | YES |
| mv5_q10_s12_l43 (media-generation original) | musicvideo/MV-5_easy-now-easy-now/work/q10/takes/media-generation-mv5-q10-s12-l43-0-8f7d2452-1821-43f3-bdf5-42b929761748.mp4 | 879e2c789c5686fe29b9f7dcf4910f95 | YES |

mv5_q10_s07_l15 — the Q10 KEEP the cleanup deleted — is on the CDN at two
paths and content-verified. The other two Q10 KEEPs (s04, s12_l43) verify via
their media-generation originals under work/q10/takes/; their renamed copies
also survive locally in takes/ and md5-verify (9a0d1ae1…, 879e2c78…).

## Class C — v6 assembly takes (43 distinct, from work/rebuild-v6/assembly_fit_mv5_v6.json): COMPLETE 43/43

No ledger md5s exist for the v6 takes, so verification is: (a) the 13 takes
that survive locally — dataset copy downloaded and md5-compared against the
local file (13/13 identical); (b) the 30 cleanup-deleted takes — the dataset
holds two independent copies of each (project-root takes/ canonical +
work/rebuild-v6/takes/ canonical) and all 30 copy-pairs downloaded
md5-identical to each other (30/30).

| # | Token | Dataset md5 (full) | Corroboration |
|---|---|---|---|
| 1 | mv5_v6_s01_cat | bc6b29752ac14245b39a132afcb53c1e | local survivor, md5-identical |
| 2 | mv5_v6_s02_girl | 27116db078c7c342de54703542a6489f | two dataset copies, md5-identical |
| 3 | mv5_v6_s02_ride | 0c34f89135e98767376ea522d05fc3c5 | local survivor, md5-identical |
| 4 | mv5_v6_s03_girl | 4eb695371ff08dfd955dcc8ddd2c4cf7 | local survivor, md5-identical |
| 5 | mv5_v6_s04_cat | 32c056f021d57ec6814f6ac4e1a60395 | local survivor, md5-identical |
| 6 | mv5_v6_s04_cat2 | 749c08bdebc2d1c8f3a52b860aa7fc75 | two dataset copies, md5-identical |
| 7 | mv5_v6_s05_cat | 208d291701d2dccffa8df9e7688d295d | local survivor, md5-identical |
| 8 | mv5_v6_s06_cat | 9343168b29bde33c43c621eaec82a660 | local survivor, md5-identical |
| 9 | mv5_v6_s07_cat | cf7796abcde770a420646d3f0bba0d8c | local survivor, md5-identical |
| 10 | mv5_v6_s07_girla | a3adfcb980970454ae3ab214a9e7a536 | local survivor, md5-identical |
| 11 | mv5_v6_s07_girlb | 28cbf2091407c3520c30d590717b90f5 | local survivor, md5-identical |
| 12 | mv5_v6_s08_duet | ed36496c6f1804e0a0934fc49af8b307 | two dataset copies, md5-identical |
| 13 | mv5_v6_s09b_duet | dc752e32ba3c7654c5cb3e99eefa3f39 | two dataset copies, md5-identical |
| 14 | mv5_v6_s10_cat | 5eac8235aa9dc80ff7810a66bc27c0ee | two dataset copies, md5-identical |
| 15 | mv5_v6_s11_cat | cc3bac4beb373b01bf30052be645e889 | local survivor, md5-identical |
| 16 | mv5_v6_s11_girl | 1f19fdf8a4e7ba77d641c77e3de0d12d | local survivor, md5-identical |
| 17 | mv5_v6_s12_cat | c49f31617bdc8df07b949f234faf2d48 | local survivor, md5-identical |
| 18 | mv5_v6_s12_girl | 76c7bb1c86a3390a81bb16c9554937f5 | two dataset copies, md5-identical |
| 19 | mv5_v6_s13_boombox | aedd0eb57a75b45fd5cf1a45dc8d5db5 | two dataset copies, md5-identical |
| 20 | mv5_v6_s13_cat | 6a56bc200b671e17be7e1bea6eb58511 | two dataset copies, md5-identical |
| 21 | mv5_v6_s13_girl | f753e623eb71fe189e3dfa8d72c38e71 | two dataset copies, md5-identical |
| 22 | mv5_v6_s13_spin | adca3986ec0215e54324948e992f91fb | two dataset copies, md5-identical |
| 23 | mv5_v6_s15_cat2 | cb44f6dc78866264f7a73f6264b6f72e | two dataset copies, md5-identical |
| 24 | mv5_v6_s15_girl | c2f93f982f2b24ea6e3011f1e58fe3c1 | two dataset copies, md5-identical |
| 25 | mv5_v6_s16_duet | e3194c72414a3533df0a023f22375e50 | two dataset copies, md5-identical |
| 26 | mv5_v6_s17_duet | 92728704649c21aec16fe3452b6446ee | two dataset copies, md5-identical |
| 27 | mv5_v6_s18_girl | a71bb929cbe47e67870d93c74580d53e | two dataset copies, md5-identical |
| 28 | mv5_v6_s19_bridge | 7c2c8be25318e754ee59789c2d646879 | two dataset copies, md5-identical |
| 29 | mv5_v6_s20_bridge | 56d3181340c3d13c6779853dd06fa899 | two dataset copies, md5-identical |
| 30 | mv5_v6_s20_cat2 | cbf4ca0e4ffe48ba5aadefa5f580f68f | two dataset copies, md5-identical |
| 31 | mv5_v6_s21_all2 | aad29cea30d4e3536e98ef49dd561927 | two dataset copies, md5-identical |
| 32 | mv5_v6_s21_girl2 | 6f9f95a4c6a030e2f03ee9a5fcfd3202 | two dataset copies, md5-identical |
| 33 | mv5_v6_s21_spin | 404d9c2f1e0d0b50539daa2c8fadb306 | two dataset copies, md5-identical |
| 34 | mv5_v6_s21_walk | 8e3769f43350d73d5fb86c36daa313f6 | two dataset copies, md5-identical |
| 35 | mv5_v6_s23_duet | 892058eb2e782274cc7bc9ea3b0accb1 | two dataset copies, md5-identical |
| 36 | mv5_v6_s24_duet | 3209e8a9124417cf6978bfa7addf71d5 | two dataset copies, md5-identical |
| 37 | mv5_v6_s25_cat2 | e1f21d47517aa66f76155c0ee8250479 | two dataset copies, md5-identical |
| 38 | mv5_v6_s25_girl | fa6d7c64b11101fe91292c932a446fb3 | two dataset copies, md5-identical |
| 39 | mv5_v6_s26_chain | 898fd3940c45c60ecc474e3f454854d8 | two dataset copies, md5-identical |
| 40 | mv5_v6_s27_cat2 | 66276ccd6c2a3e36f042ba8fdb1c93b5 | two dataset copies, md5-identical |
| 41 | mv5_v6_s27_chant | b14d5d09b2ee70bd4db347dd4e1dd7b4 | two dataset copies, md5-identical |
| 42 | mv5_v6_s28_cat2 | 6719fa6694e7aeb0b8ee3c350980b2db | two dataset copies, md5-identical |
| 43 | pilot_p2_cat | 94c9f7c2802b84fd3414072798c66b3f | local survivor, md5-identical |

## Absences

NONE. Every in-scope token was found inside the MV-5 subtree of the dataset
(239 files), so no whole-dataset token search was needed. Contrast MV-4
(s25t2 lost) and MV-17 (s06t1 lost) in the same cleanup event — MV-5 lost
nothing.

FINAL: COMPLETE — TAKE_HISTORY KEEPs 30/30 CDN-verified by downloaded md5
(full ledgered set 76/76), Q10 KEEPs 3/3 (incl. the locally-deleted
mv5_q10_s07_l15, verified at two dataset paths), v6 assembly takes 43/43
(13 md5-identical to local survivors; 30 corroborated by identical dual
dataset copies). No MV-5 take is missing from the CDN; nothing was lost in
the 2026-11-16 cleanup. Combined with the surviving local copies, every
class is covered in both places where local copies remain.
