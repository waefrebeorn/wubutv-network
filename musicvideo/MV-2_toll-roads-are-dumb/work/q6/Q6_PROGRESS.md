# MV-2 Q6 IMPROVEMENT — progress (coordinator: recovery, revived 2026-11-12 ~12:22 EST)

Previous Q6 coordinator ccfb1530 INTERRUPTED 12:19:21 EST (daemon restart, null
final response). It wrote nothing except the empty work/q6/ directory.
This recovery starts from the queue definition; nothing to redo.

## Scope (program.md §2 Q6)
- Restage S04a (34.56–41.30), S07 (72.28–80.78), S21 (205.20–214.44) — one take
  each, cap 6 videos this run INCLUDING re-fires. STYLIZED axis ONLY.
- Re-cut section boundaries to true line boundaries (LYRIC_TIMELINE.md).
- S25 place-beat re-cut (use the take's later frames).
- Reassembly → new master v7 from v6 takes + 3 restages at new cut points.
- OUT OF SCOPE: performed-chorus-line ear item + GAP-C "first"=fast (Q16),
  pocket-square drift, S26/S11 mic/turn nits, S07 gantry signals (disclosed).

## Why the restages must differ from volley 18
Volley-18 restages failed because the prompts OMITTED "flat cartoon" —
generator returned photorealistic live-action + legible text ("STOP",
"FAST LANE"). Q6 vehicles lead with the flat-cartoon style term AND carry
an image anchor: work/q6/voice_anchor_night.png (frame 3.0s of S06a t2,
a v6 KEEP take — night-VOICE, face to camera, CADMIUM square, mic, blank
ticket, night road; read back and verified before use).

## Cap accounting
Task cap: 6 videos this run including re-fires. Used: 0/6 so far.

## Step log
- 12:22 EST: recovery start. Read program.md §1 MV-2 + §2 Q6, LYRIC_TIMELINE.md,
  V6_ASSEMBLY_MAP_2026-11-04.md, V6_10S_CUT_PLAN.md, MUSIC_VIDEO_LEDGER.md,
  VOLLEY18_RESTAGE_COVERAGE.md, Slopcannon skill, video-api-mastery skill.
- 12:24 EST: anchor still extracted + eye-read (S06a t2 @3.0s; S01 t4 @5.0s
  also read — ticket-dominant, square reads blue; S06a chosen).
- 12:2x EST: vehicles written (work/q6/vehicles/): S04a, S07, S21.
- 12:2x EST: FIRED 3 restages (cap 3/6). All landed first attempt, 10.000s,
  1280x720/24fps. Canonical md5s: S04a 6009bfaf…, S07 t1 563b67fe…,
  S21 412a5ca8… (see Q6_LEDGER.md).
- QC (qc_v6_q6.py + qc_v6_q6_followup.py, Whisper base int8):
  S04a t1 22/22, ratio 0.711 GREY → warp-rescue 1.1322x → 22/22, ratio
  0.804, frame PASS; S07 t1 REJECTED (frame FAIL 33f run 1.71–3.08s +
  legible STOP signs) → t2 re-fire (staging axis): 10/10, ratio 1.190,
  frame PASS (run 1), text PASS (plain dark booths, no signs);
  S21 t1 13/14 (dropped 2nd "to", same minor class as v6final), ratio
  1.108, frame PASS. Character PASS 4/4 takes — the image anchor closed
  the volley-17/18 face failure. Cap now 4/6. Full verdicts: Q6_LEDGER.md.
- RE-CUT audit (Q6_RECUT.md): v6's cuts already track SONG_WORDS_BASE
  (measured words) — 5 of 7 section boundaries exact at 0.00; the brief's
  "worst today" numbers are V2-grid numbers, not v6's. Two real changes:
  filler source switch at 121.76 (V2/C2, end of "quit.") and at 165.34
  (C2/Bridge, onset of "They"), both verified wordless + motion PASS.
  S25 place-beat: post-slot filler re-cut to S25 t2 tau 3.34–5.72 (place
  lands ~254.2; motion mean 3.98). Post-re-cut boundary error 0.00/7.
- 12:4x EST: assemble_v7.py plan-only validates (106 clips, 6432f);
  full render running (background proc_1e324ff8b86f).
- 13:05:22 EST: v7_silent.mp4 built (70,776,704 B, 106 clips) — c786bbd9
  CANCELLED 13:08:52 EST before the finish; no live coordinator since.
- 13:19 EST: RECOVERY coordinator start (revived by MV coordinator
  revive detector). Resumed from disk: ledger/recut verified, no
  re-fires (cap stays 4/6).
- 13:2x EST: FRAME-COUNT FIND — v7_silent decode-counted 6448f, NOT
  6432 (duration 268.665s). Per-clip container audit: 22/106 clips
  ±1f (19× +1, fps boundary frame; 3× -1, clips 62/87/105 whose
  windows run to the take end tau1=10.0). Root cause: fps=24 emits a
  boundary frame / -t cuts before the last source frame exists.
  FIX (assemble_v7.py + repair_v7.py): -t +0.021s, -frames:v n, per-clip
  container verification, plus tpad=stop_mode=clone after fps so a
  take-end clip pads its last frame to exactly n (1 cloned frame at a
  cut point, below the 6f motion threshold). All 22 re-rendered;
  container total 6432; rebuilt v7_silent md5
  e06a4fe64f95ceb142f6f2c7c9e80792; decode-count re-verification running.
  No cutlist/take change; v6 master untouched (md5 b2d386bf… verified).

- 14:06:51 EST: RECOVERY coordinator 2293be03 CANCELLED (final response =
  cancellation boilerplate, no report) after building both masters; its
  session checkpoint (19:18:39Z) lists gates/ledger/flag/report as undone.
  The detached chat-copy ffmpeg finished 14:19 EST on its own.
- 14:19-14:40 EST: PARENT FINISH from disk — no re-assembly, no re-encode.
  Gates (gate_v7_parent.py, log masters_work_v7/gate_v7_parent.log): house
  6432f DECODE-counted, 268.010s, h264 1280x720 24fps, AAC 48k stereo, SEI
  crf=18.0, faststart moov@36, md5 701fa50b19f6697fb37511dec6f932eb,
  82,739,324 B; audio agreement vs track.mp3 min corr 0.9981 (10 windows);
  chat 6432f, 32,701,938 B, md5 050161faa8ee5941c1abefdad77ac74c, audio PCM
  md5 == house (f8371c2b5dbd9ebc389b9a11d1bc0428). v6 untouched (md5 b2d386bf
  re-verified). Captions: 396 Dialogue events, 0 double-backslash lines.
- Motion audit (motion_audit_v7_parent.py): mean diff 3.37; ONE run >=12f,
  18f @184.96-185.67s during words — frame-identical to v6's run in the
  same R4 filler clip (words "roads/are/done,"), INHERITED, not new. The
  v6 S07 18f run is GONE (t2 fixed it). v6 had 2 runs, v7 has 1. PASS.
- Mouth-at-cut (parent full-res eye reads, frames in work/q6/gate/):
  S04a "Now" @34.56 OPEN; S07 "We've" @72.28 OPEN; S21 chorus burst
  @205.20 OPEN. Caption "The wrecks just come." verified against measured
  words (the "road gets meaner" burst is the collapsed chorus layer at
  the same 205.20 stamp). Kinetic highlight leads the word by ~0.1s
  (styling, within tolerance). All three swaps PASS.
- outputs_v7.json written by parent (the file 2293be03 never wrote).
- Ledger Q6 section appended to MUSIC_VIDEO_LEDGER.md; MV2_V7_DELIVERED.flag
  written at project root; registry mv-improvement-q6 -> done; dedupe
  2293be03 CONSUMED. Chat copy delivery follows the commit (same turn).
- Q6 CLOSED. MV-2 lyrics redo chains next, on the v7 base.
