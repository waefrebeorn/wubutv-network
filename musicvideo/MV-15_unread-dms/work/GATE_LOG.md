# MV-15 'Unread DMs' — GATE LOG (assembly completed by RECOVERY #3, 2026-11-13)

## DELIVERED MASTER (v2 — the only valid master)
- File: masters/mv15_unread_dms_16x9.mp4
- md5: 0bef4ae5dd2217e481b3ccff840100ac
- Bytes: 792,109,501 (792 MB — grain pass at CRF 18 on this recipe; disclosed, house master is canonical)
- Probe: h264 1280x720, r_frame_rate 24/1, duration 173.625s; audio AAC 48000 Hz stereo
- Frames: 4167 / 4167 exact — PASS
- x264 SEI: crf=18.0 — PASS
- Audio codec AAC (encoded from track.mp3, never stream-copied MP3) — PASS
- Faststart (moov before mdat): true — PASS
- Master-audio agreement (16k mono Pearson vs track.mp3): global 0.99895, worst 10s window 0.99785 — PASS

## ZERO-STILL GATE (user-ordered for this track: no near-dup run >= 2 frames anywhere)
Method: full-master decode at 640x360 gray, mean-abs-diff per consecutive pair, near-dup = diff < 0.5 (work/gates.py spec; executed by work/gates_run.py, a streaming twin with identical math — gates.py OOM-died on its whole-buffer decode of the 792 MB master; identity of method verified by construction). Independent enumeration by work/scan_runs.py.
- MASTER (post-grain): longest run 0; min pair diff 1.209; enumeration: 0 runs >= 2 in 4167 frames — PASS
- PRE-GRAIN (pass-1 output, the honesty measurement): longest run 1 (a single isolated pair below threshold at the head; no two consecutive); enumeration: 0 runs >= 2 in 4167 frames — PASS (honest: the pass does not depend on the grain)

## SUPERSEDED v1 MASTER — DO NOT DELIVER
- md5 eb67f409ed65cb86b7cc4a8fb0a40460, 788,447,363 B. All container/audio gates passed and its POST-grain scan read longest run 0, but the PRE-GRAIN enumeration found 107 near-dup runs >= 2 (longest 4) across S05 head, S09, S13, S17 tail, S18 (dense), S19 tail, S20 tail, S24 tail — the grain was masking still picture. Per SCENE_PLAN's GRAIN HONESTY RULE that master was rejected by this coordinator and replaced. v1 measurements preserved in work/qc/GATES_v1_grain_only.json and work/scan_pregrain.log.
- Honesty fix applied (work/conform_fix2.py + conform_fix3.py; originals in work/conformed_orig/): the 8 flagged scenes were re-conformed with REAL motion — a slow 256px pan across each span plus a geq light-pulse (luma gain+offset, per-frame by construction, periods 0.8s/0.53s on the 150 BPM grid). Each fixed scene was scan-verified 0 runs >= 2 at conform level BEFORE re-assembly. Fixes measured, not assumed: an eq-based pulse was tested and REJECTED (this ffmpeg build does not evaluate eq brightness per frame — output identical to control); a pan alone was tested and found insufficient on the flattest pairs (crop steps round to whole pixels); the geq+pulse+pan combination measured clean on every scene. S20/S18 additionally needed tpad moved BEFORE the pulse so clone tail-frames also receive per-frame values (fix3).

## CHAT COPY
- File: masters/mv15_unread_dms_16x9_chat.mp4 — md5 05d781d6df6cb36acebd1c6096217bc4
- 47,527,059 B (<= 50 MB), h264, 4167 frames verified, video capped 2000k/maxrate 2200k, AAC stream copied from the house master, faststart.

## ASSEMBLY NOTES / SCRIPT FIXES DURING RECOVERY
- Conform S06–S24 completed frame-exact (work/conform_rest.py; the parent's S05 patch in conform.py untouched and its S05 output preserved — S05 was later re-conformed once more by fix2 for the honesty fix, keeping the parent's bounded orb branch: -loop 1 -t 6.86 + post-overlay trim).
- work/final_encode.sh carried two latent bugs (never previously run end-to-end): concat list used paths relative to the list file (fixed to absolute) and an invalid hue 'eval' option (removed; hue evaluates per frame in this build — verified on the S19 inversion frames).
- Overlays: work/make_overlays.py re-rendered work/overlays/kinetic.ass (53 events: phrase captions + kinetic hits + HUD counter line 199 -> 389 UNREAD -> "389 MUTED UNREAD").

## LEDGER RECONCILIATION (tasked item 6)
- Take files on disk: 32 (takes/mv15_s*.mp4) and 32 matching generation-handle JSONs in work/handles/. Generation fires = 32, NOT 33.
- VOLLEY_PROGRESS.md volley sums: Pilot 3 + Reroll 2 + A 6 + B 6 + C 6 + D 6 + E 2 + S21 fragment t2 fire 1 = 32 fires. The "33 fired (24 + 9 re-fires)" figure in MV15_PROGRESS.md / VOLLEY_PROGRESS.md is a miscount by the original coordinator: re-fires total 8, not 9 (volleys B–E re-fired 6 slots, plus 2 pilot re-rolls = 8). No 33rd fire exists; no take file was overwritten in place (all 32 handles distinct).
- KEEP takes = 25 across 24 scenes (S21 ships a t1+t2 composite: t1 phrases L28 + t2 0–3.48s for L29, per work/build_s21.py). REJECT = 7: s01_t1 (photoreal face-swap), s07_t1 (photoreal), s01_t2 (name card), s04_t1 (subtitles), s11_t1 (subtitles), s15_t1 (wrong scene), s16_t1 (multi-KIT).
- TAKE_HISTORY.md was missing the mv15_s21_t2 row — ADDED by this coordinator with md5 78b4a92c3d7ecaaf45fade57d6e8ddd3, verdict KEEP (fragment). TAKE_HISTORY now reconciles 1:1 with takes/ (32 rows = 32 files).
