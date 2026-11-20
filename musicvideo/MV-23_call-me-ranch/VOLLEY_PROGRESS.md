# MV-23 "Call Me Ranch" — VOLLEY PROGRESS

Budget: 40 video generations. Spend: 29 landed. Refusals: 2 (S11 t2 ×2). 429s: 0.
Plan: MV_PREPRO_MV-23.md (24 scenes). Refs: REFERENCE_STACK.md (4 refs, eye-verified).

## Volleys 1–6 — ALL FIRED. Every scene has a chosen take (see TAKE_HISTORY.md).
Chosen: S01 t1 · S02 t1 · S03 t1 · S04 t1 · S05 t1 · S06 t2 · S07 t1 · S08 t1 · S09 t1 · S10 t1 · S11 t1 (costume drift disclosed; reroll refused ×2) · S12 t1 · S13 t2 · S14 t2 · S15 t1 · S16 t1 · S17 t1 · S18 t2 · S19 t1 · S20 t2 · S21 t1 · S22 t1 · S23 t1 · S24 t1.
Rejected takes kept on disk: S06 t1 (identity), S13 t1 (lyric), S14 t1 (costume), S18 t1 (wrong man), S20 t1 (identity).

## Remaining
1. Finish ASR QC chains (qc_t1_v3/v4/v5/v6, qc_t2_v4/v5 logs) — confirm ratios/spans for S14 t2, S16, S17, S19, S20 t2, S21–S24, S13 t2.
2. Build work/swing/captions_karaoke.ass (word-timed, MV-2 v7 house style) + work/swing/lyrics.srt from SONG_WORDS.json + sheet lines.
3. Assembly: adapt MV-22 build_master.py (setpts FIRST then fps=24; per-segment frame+duration asserts; joined probe frames AND duration = 4243f / 176.792s).
4. Master encode: CRF 18 + burned karaoke ASS + mov_text + corner bug "~ WuBu ~"; CRF-23 differential proof; chat copy ≤50MB.
5. Paperwork: GATE_LOG.md, CUTLIST.md, COMPLETION.json, MV23_DELIVERED.flag, USED_EVENTS.md append.

## Update 2026-11-20 ~16:05 EST (post-stall recovery)
- QC waiter deadlock found + fixed by parent steering: waiter shells killed by PID; remaining QC run DIRECTLY (qc_t2_v4, qc_t1_v4, qc_t2_v5, qc_t1_v5, qc_t1_v6 logs all complete).
- QC finals: S13 t2 G7 1.0 (full line) k=0.616 · S14 t2 G7 0.900 k=1.008 · S16 t1 G7 1.0 k=0.757 · S17 t1 G7 1.0 k=0.718 · S18 t2 cutaway motion 36.66 · S19 t1 G7 0.857 (line-span warp k=1.094 per L56) · S20 t2 G7 0.938 k=0.820 · S21 t1 G7 1.0 k=0.815 · S22 t1 G7 1.0 k=0.604 · S23 t1 G7 1.0 k=0.969 · S24 t1 G7 1.0 (lyric span to 174.76; grid tail = documented ASR hallucination).
- Karaoke ASS built: work/swing/captions_karaoke.ass (349 word events, MV-2 v7 house style) + lyrics.srt (70 cues).
- Segments built via work/swing/build_master.py: every segment frame+duration assert PASS; TOTAL 4243f = target.
- joined.mp4 PROBED: 4243 frames AND 176.791s duration, 1280x720 24fps — PASS both axes.
- Master encode RUNNING: CRF 18, subtitles burn + drawtext bug + AAC 48k + mov_text, faststart -> masters/mv23_call_me_ranch_16x9.mp4.
- Remaining: CRF-23 differential, chat copy, subtitle/bug frame-grab verification, freezedetect, GATE_LOG/CUTLIST/COMPLETION/flag, USED_EVENTS append.

## DELIVERED 2026-11-20 ~16:35 EST
- DUAL-WRITER RACE: the first master encode raced a recovery coordinator's
  parallel encode of the same file (~7 min interleaved writes). Parent
  killed both; corrupt file (51,742,541 B) deleted unshipped on parent
  instruction. Solo re-encode from joined.mp4 (detached, only ffmpeg
  writer throughout) completed clean.
- Master: masters/mv23_call_me_ranch_16x9.mp4 — md5 0573d8c67cd64aba6036d60731a396d1,
  105,259,893 B, 4243f (count_frames), 176.792s video / 176.810s format,
  AAC 48k, mov_text 70 cues, faststart (moov front). CRF-18 proof 1.80x.
- Burned karaoke verified by eye at 3.0s + 52.0s (bar + yellow highlight);
  bug "~ WuBu ~" exact at 3.0s/52.0s/176.0s. Freezedetect: 0 events.
- Chat copy: masters/mv23_call_me_ranch_chat.mp4 — md5 e2e037c2254a08e926296f06ccb17c70,
  44,871,602 B, 4243f.
- Paperwork: GATE_LOG.md, CUTLIST.md, COMPLETION.json, MV23_DELIVERED.flag
  all in the project dir. USED_EVENTS.md MV-23 block appended (WUBUMV repo).
- FINAL SPEND: 29/40 landed, 2 refusals, 0 429s.
