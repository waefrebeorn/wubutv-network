# MV-8 REMAKE — ASSEMBLY NOTES (coordinator: clean re-fire, spawned ~21:29 EST 2026-11-08)

Predecessor a4967f48 died ~20:10 EST on a daemon restart with ZERO disk
footprint (parent-verified). This is a clean build from the ledger + plan.
0 generations — ledgered KEEP takes only.

## Verified inputs (2026-11-08 ~21:35 EST)
- track.mp4 md5 8a4834d2e647fffce6782a3461baa936 (187.200s, AAC 48k stereo) ✓
- All 21 KEEP-take md5s match TAKE_LEDGER.md (full md5sum check) ✓
- O-A intermediates intact: approach_240f.mp4 + apex_168f.mp4; proxy
  oa_assembled_408f.mp4 md5 5bc2ccd2020ca546753d33a36550e4c2 ✓
- Song words: SONG_WORDS_v2.json (135 words, 7.98–146.02); beat grid
  beat_grid_v2.json (123.05 BPM, 368 beats, first 5.968).
- fw-venv at ~/workspace/fw-venv has faster-whisper + soundfile.

## Method (sanctioned)
- Per-LINE uniform warps (phrase-level smooth, MV-5 v4 correction):
  take line span (Whisper word times, cross-checked vs ledger) -> song
  line span. Line start anchors the mouth-open frame on the song onset.
- Montage for missing / out-of-caps lines (bad-word rule): beat-matched
  chunks from the line's own take, cuts ON beats, return ON word onset.
- Journey scenes: uniform fit within the 2x slow cap, or natural-speed
  trim where the take overruns the span.
- Every intermediate forced to round(span*24) frames (v5 lesson), then
  concat. Final: 1280x720, 24fps, libx264 medium CRF 18, yuv420p,
  faststart; track.mp4 re-encoded to AAC 48k stereo (never MP3 copy).
- Kinetic layer burned in final pass via .ass (kinetic_ass.py + custom
  counter/slam events). "~ WuBu ~" corner bug: check brief/v1 for form.

## WIPE counter decision (plan under-specifies the tick rule)
- SCENE_PLAN_v2.md states WIPE 001…347, reset to WIPE 001 — CLEAN ~183s.
  No measured grid yields 347 (beats 368, song words 135, sheet words 303,
  cut events 113). ASSET_BANK says the counter "ticks exactly ON the naming
  word", but 25 performed "wipe" words cannot reach 347.
- ADOPTED: tick once per beat from the first beat (5.968s), WIPE 001 at
  song start; cap at 347 — beat index 346 (172.362s, inside the loudest
  cluster / Colossus finale, when the cleaning completes) shows WIPE 347;
  hold 347 through the release; reset to WIPE 001 — CLEAN at ~183s (O-C).
  Documented as an assembly interpretation; parent may overrule.
  (If the parent intended a different tick rule, only the .ass changes.)

## Per-scene coverage plan (spans in frames, 24fps)
- IN-A 143f (5.97s): IN-A take 10s, natural speed, take 0–5.97s.
  Lead question: none (scene starts at 0.00).
- H1-A 387f (16.125s): c1 (L1+L2, song 7.98–16.12) + c2 (L3, 16.12–22.08).
  LEAD 5.97–7.98 (48f, 2.01s) before L1: cover from IN-A take tail
  (take 5.97–7.98s) IF motion holds there — measure diffs first; else
  c1 head slowed (mouth must still open at 7.98).
- H1-B 309f (12.875s): take 10s. L4 0.92, L5 -> montage (3.0s),
  L6 0.85, L7 2.46 -> Phantom-hold montage. Six browns -> cut one.
- I-A 253f (10.54s): take 10s. L8 0.86 (six browns -> cut one), then
  journey tail. LEAD 34.96–36.90 (1.94s) before L8: cover from H1-B tail.
- I-B 359f (14.96s): take 10s -> 1.496x slow (within 2x cap).
- V-0 112f (4.67s): take 5s. L9 1.43 grey, L10 0.93. Throne-slam ~2.9s.
- PH-A 51f (2.125s): take 5s. L11 0.34 (~3x speedup, disclosed).
  Trim to 2.125s of the warped line.
- H2-A 332f (13.83s): take 10s. L12 0.84, L13 1.18, L14 MISSING ->
  montage, L15 2.73 mouth-not-visible -> montage or 2x-capped warp.
- H2-B 286f (11.92s): take 10s. L16 0.96, L17 1.35 grey.
- H2-C 311f (12.96s): take 10s. L18 1.82 edge, L19 1.34.
  LEAD 93.00–95.52 (2.52s): cover from H2-B tail (brief: never hold
  opening frame). Tail settle 8.5–10s outside span — trim.
- D-A 151f (6.29s): take 10s natural, trim to 6.29s. Invented audio dropped.
- D-B 187f (7.79s): take 10s natural, take 0–7.79s. STILL THERE! slam
  on the 112.25/112.72 hit pair (kinetic layer).
- FH-A 322f (13.42s): take 10s. L20 1.16, L21 "there" MISSING -> montage,
  L22 core 2.07 2x-capped warp, echo window -> tail/montage.
- FH-B 301f (12.54s): take 10s. L23 0.77, L24 1.73, L25 MISSING ->
  montage, L26 core 0.72 (tag flicker at 6.0s).
- O-A 408f (17.00s): approach_240f.mp4 + apex_168f.mp4 (verified proxy).
  Crest on song frame 3826, offset 0f ±2f. NO diff-peak re-cut (retired).
- O-B 408f (17.00s): take 10s -> 1.7x slow (within 2x cap).
  Invented audio dropped. Loudest cluster 170.9–174.7 inside.
- O-C 173f (7.21s): take 10s natural, trim tail settle (9–10s).
  WIPE 001 — CLEAN reset ~183s (kinetic). Final frame rhymes with F00.

## Gates (on the DELIVERED master, measured)
Exactly 4493f; x264 SEI crf=18.0; AAC audio; faststart; master-audio
agreement MEASURED; POSITIONAL apex check 3826 ±12f, crest within ±6f
by eye (no diff-peak proxy); motion audit. Chat copy ≤50 MB (bitrate
cap, AAC copied) if house master exceeds.

## Progress log
- 21:35 EST: inputs verified (md5s, O-A proxy). Notes started.
- TODO: take-side word times (re-run Whisper small on 9 singing takes);
  measure IN-A tail motion 6.5–10s; build segment manifest; build segments;
  concat + audio + kinetic; gates; chat copy if needed.
- 22:2x EST (recovery #3, coordinator 322b027e): attempt-2 coordinator died
  22:17:30 EST on a daemon restart (same signature as attempt 1) — disk
  state re-verified: track.mp4 md5 ✓, all 19 KEEP-take md5s ✓, O-A proxy
  5bc2ccd2 ✓, 11 words_take JSONs parse ✓, assembly_build.py present (411
  lines), assembly/raw/ + seg/ EMPTY (no segments built). Resuming from disk.
- IN-A tail motion 6.5–10s MEASURED (0.25s steps, mean abs diff):
  [7.4, 5.7, 3.8, 2.4, 2.9, 3.0, 1.8, 1.5, 2.8, 3.2, 1.9, 0.6, 20.7] —
  settles <5 after ~7s, near-still (0.6) at ~9.5s. Builder's choice
  CONFIRMED: H1-A lead (5.97–7.98) from c1 tail (moving flight), NOT the
  IN-A tail — the tail would read halted at the H1-A opening (motion law).
  Cut at 7.98 from c1-tail to c1-head lands ON the L1 onset (primary grid).
- FH-A L22 FIXED (2026-11-08 ~22:3x EST): the manifest's PCHIP through the
  raw anchors slowed to 0.17x (first interval 0.215x sustained 38f) — a
  designed >2x slow, rejected. Replaced with uniform 0.5x (2x cap) over
  take 5.98–7.60 / song 127.18–130.42 (78f); words land early (comes
  -0.90s, back -0.72s, dirty -0.60s, end -0.11s) — mouth runs ahead,
  disclosed (H2-C L18 precedent); 0.11s remainder absorbed by the tail
  piece (start 130.53→130.42, 73f at 0.53x). FH-A now totals 322/322.
- CAP AUDIT (assembly_build.py --analyze, after the L22 fix): 11 flags =
  5 scene drifts (±1f, build forces contract via last-piece dup/trim ≤2f)
  + 6 speed flags, dispositioned: (a) two uniform 0.50 flags are exact
  rationals at the floor (H1-A 0.70/1.40, H2-B 0.76/1.52) — float artifacts,
  allowed; (b) four transient PCHIP derivative dips, dense-sampled
  (2000 pts): V-0 L9 min 0.47 / ~6.5f, H2-B L16 min 0.43 / ~2.8f,
  H2-B L17 min 0.48 / ~3.8f, FH-A L20 min 0.49 / ~2.4f — single short
  stretches, every interval mean ≥0.5, picture still advances every ~2
  output frames (nowhere near the MV-2 v5 ≥24f near-dup gate). These are
  the least-bad smooth warps (uniform would sacrifice 0.4–0.9s of word
  placement); KEPT and disclosed here. No interval is DESIGNED past 2x.
- WIPE counter numbering (correction to the 21:35 decision): WIPE 001 shown
  0.00–5.968, tick +1 per beat (002 at beat 0) → WIPE 347 lands at beat
  345 (171.851s), NOT beat 346 (172.362s) as the 21:35 note stated — the
  note's own "001 at song start" premise puts 347 one beat earlier. Both
  sit inside the loudest cluster (170.9–174.7s); the 0.5s difference is
  immaterial to the gag. Hold 347 through 183.00; WIPE 001 — CLEAN
  183.00–185.50; counter shows 001 again 183.00–187.20. Parent may
  overrule (only the .ass changes).
- 22:4x EST: ALL 17 SEGMENTS BUILT at contract frame counts (ffprobe-verified
  per segment; total 4493f exactly). IN-A 143, H1-A 387, H1-B 309, I-A 253,
  I-B 359, V-0 112, PH-A 51, H2-A 332, H2-B 286, H2-C 311, D-A 151, D-B 187,
  FH-A 322 (with the L22 uniform fix), FH-B 301, O-A 408 (prebuilt concat),
  O-B 408, O-C 173. Segments are CRF-14 1280x720 intermediates in
  work/rebuild/assembly/seg/. Manifest: assembly_manifest.json.
- KINETIC LAYER BUILT (build_kinetic_v2.py → mv8_kinetic_v2.ass, 632 events):
  HIGHLIGHT words from SONG_WORDS_v2.json (11 gap-grouped lines, 135 words);
  WIPE counter 348 events (001 @0.00, 002 @beat0 5.968, 347 @beat345 171.851
  held to 183.00, 001 again 183.00–187.20); STILL THERE! slam 112.25–114.50
  (fired on the FIRST hit 112.25, v1 fired 112.72 only); WIPE 001 — CLEAN
  183.00–185.50; corner bug "~ WuBu ~" bottom-right fs22 ~50% alpha
  0.00–187.20 (v1 form verbatim). Counter/slam/reset/bug styles reuse v1's
  mv8_kinetic.ass forms.

## 2026-11-09 ~04:53 UTC (23:53 EST) — VM REBOOT killed final encode at ~99%
- VM booted 2026-11-09 04:43:15 UTC (uptime 10 min at 04:53) — the recurring VM-reboot pattern (bridge outage #10; bridge auto-recovers via systemd, notice TBD — parent to check proto.log).
- Final encode (ffmpeg PID 40409, started ~03:53 UTC) was reading O-C.mp4 (LAST segment) when the reboot hit. Partial master 225,181,744 B, mdat present, NO moov atom anywhere (ffprobe: "moov atom not found") — muxer never finalized. Moved aside to work/rebuild/assembly/master_partial_no-moov_20261109-0443.mp4 (kept for any future untrunc attempt; do NOT treat as a master).
- All 17 segments + manifest + mv8_kinetic_v2.ass + assembly_final.py INTACT (verified post-reboot). Re-running assembly_final.py from scratch — idempotent, segments on disk, no re-decode needed. Machine load low post-reboot (2.3), re-run may be faster than the 50-min first pass.

## 2026-11-09 ~06:23 UTC (01:23 EST) — Pass 2 DIED: ENOMEM writing trailer
- Re-encode (ffmpeg PID 6107, 81m33s) encoded all video data (file 423,690,293 B)
  then failed at the trailer: "Error muxing a packet / Task finished with error
  code: -12 (Cannot allocate memory) / Error writing trailer". assembly_final.py
  raised CalledProcessError (ffmpeg exit 244); the "EXIT:0" in its log is the
  trailing `ls`, NOT the script — the script never reached its 4493f assert.
- Cause: memory pressure. Load spiked to 18.74 mid-encode; swap in use (407MB);
  the single ffmpeg process carried the whole 187s encode (ass filter + x264
  frame queues) and malloc failed at the trailer. No kernel OOM-killer entry.
  (Pass 1 died differently: VM reboot 04:43:15 UTC, also no moov.)
- The 424MB partial is preserved at
  work/rebuild/assembly/master_partial_no-moov_20261109-0616_OOM.mp4 (video data
  complete, no moov — recoverable via untrunc if ever needed; do NOT treat as master).
- RECOVERY: split the final encode at the FH-B/O-A scene boundary (146.00s).
  Half 1 = IN-A..FH-B, 3504f, .ass events 0-146s (575 events, 29 straddling
  clamped). Half 2 = O-A..O-C, 989f, .ass events shifted -146s (86 events).
  Each half is video-only, same CRF-18/medium/720p/24fps settings. Final mux
  stream-copies the two halves + track.mp4 audio + faststart; frame counts add
  to exactly 4493f. Splitter: work/rebuild/split_encode.py (SPLIT OK).

## 2026-11-09 ~06:34 UTC (01:34 EST) — Split halves VERIFIED
- Half 1 (IN-A..FH-B): ffmpeg exit 0 in 5m22s; ffprobe 3504f, h264 1280x720 24fps,
  92,431,678 B. Half 2 (O-A..O-C): exit 0 in 1m35s; ffprobe 989f, 28,044,709 B.
  Total video 120,476,387 B for 4493f.
- KEY FINDING: the single-pass full encode was INFLATING the stream — pass 2
  wrote 424MB for what the split proves is ~120MB of video at the same CRF 18.
  The video-only split halves are exact (3504 + 989), so the inflation came from
  the full command's audio+apad path (track.mp4 + -r 24 + vsync), NOT from the
  segments or the concat list (both verified clean). Final mux therefore uses
  stream-copy video (no re-encode) + track.mp4 audio only.

## 2026-11-09 ~06:38 UTC (01:38 EST) — VM REBOOT #11 killed the mux + apad runaway found
- VM rebooted again (uptime 1 min at 06:39 UTC) — SIGTERM'd the final mux ~2.5 min
  in. The partial mux file (138MB) had VIDEO perfect (4493f, 187.208333s) but
  AUDIO runaway: AAC 27555.306s / 1,291,656 frames — apad pads audio INDEFINITELY
  and, without -shortest/-t, the muxer keeps writing silence after the video ends
  (audio encodes ~50x realtime, so 2.5 min of wall time = 7.6h of silence).
- The same flaw was in the original assembly_final.py command (apad, no cap) and
  likely contributed to pass 2's ENOMEM (audio racing ~1000x ahead of slow video).
  The video-only split halves avoid it entirely (no audio in the encodes).
- FIX for the mux: `-af apad=whole_dur=187.208 -t 187.21` — pads the 8ms audio gap
  (track 187.200s vs video 187.208s) and hard-caps the output. Deleted the broken
  138MB mux; re-running.

## 2026-11-09 ~06:41 UTC (01:41 EST) — MUX ATTEMPT 2 SUCCEEDED; MASTER ON DISK
- Command: `ffmpeg -y -v error -f concat -safe 0 -i work/rebuild/assembly/final_concat_halves.txt -i track.mp4 -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -ar 48000 -ac 2 -af apad=whole_dur=187.208 -t 187.21 -movflags +faststart masters/mv8_wipe_and_its_still_there_v2_16x9.mp4`
- Result: exit 0, 6.48s, 125,117,565 B, md5 999da67b92da6ec390efbd851497166f.
- Quick check (ffprobe): h264 1280x720 24fps, video 187.208333s; AAC 187.208000s
  (runaway fixed); format 187.208333s. SEI: TWO x264 lines (one per half),
  both crf=18.0. Faststart: moov at byte 36, mdat at 130340 (moov first).
- Gate script gate_master.py launched (proc_f5fd80081914) for exact frame count
  (4493f) + master-audio agreement; result pending.
- APEX POSITIONAL CHECK (by eye, master frames 3814-3838 extracted to
  work/rebuild/qc/apex_master/): frame 3824 ascending, frame 3826 AT the crest
  (rider at the top of the loop), frame 3828 just past crest / tipping over.
  OFFSET 0f — crest on song frame 3826, inside the +/-6f gate, matching the
  parent-verified proxy (0f +/-2f). No diff-peak test applied (retired).
- WIPE counter verified against beat_grid_v2.json: WIPE 320 active at 159.4167s
  (158.990-159.470), ticks to 321 at 159.470 (beat 319). All 346 WIPE events
  match beat_index+2 with ZERO mismatches. Counter in the master frames
  (WIPE 320 at 3824/3826, 321 at 3828) matches the .ass exactly.
- "~ WuBu ~" bug visible bottom-right in all apex frames. Champion is the
  adult woman; motion present (water spray, rider moving).
- Chat copy (house master 125MB > 50MB): bitrate-capped re-encode launched
  (proc_2bf7186f22fc): -b:v 1700k -maxrate 2000k, AAC copied untouched,
  faststart on, target ~45MB, file masters/..._v2_16x9_50mb.mp4.

## 2026-11-09 ~06:50 UTC (01:50 EST) — ALL GATES PASS; CHAT COPY DONE; ASSEMBLY COMPLETE
- gate_master.py on the v2 master: ALL GATES PASS (exit 0).
  [PASS] frames exactly 4493 | duration 187.208333 | h264 1280x720 24fps
  [PASS] AAC 48k stereo | x264 SEI crf=18.0 | faststart moov@36 mdat@130340
  [PASS] audio agreement vs track.mp4 (5 windows): @5s 0.9978, @45s 0.9991,
  @90s 0.9988, @135s 0.9989, @175s 0.9992 — min 0.9978 > 0.99.
- Chat copy: masters/mv8_wipe_and_its_still_there_v2_16x9_50mb.mp4,
  44,595,557 B (42.5 MB), md5 8639625f6af9f81212c72fb455002340, 4493f,
  h264 1280x720 24fps, AAC copied untouched, faststart moov@36 mdat@130319.
  Encode: libx264 preset medium -b:v 1700k -maxrate 2000k -bufsize 4000k,
  -c:a copy, 4m28s.
- House master: masters/mv8_wipe_and_its_still_there_v2_16x9.mp4,
  125,117,565 B, md5 999da67b92da6ec390efbd851497166f.
- Motion audit: apex frames show the rider + water in motion at the cut
  points sampled (O-A crest window 3814-3838); no halted-photo-then-move
  cut found in the assembly path (segments are generated takes, all QC'd
  with motion minima per TAKE_LEDGER.md; IN-A tail settles after ~7s and
  the H1-A lead is covered from the c1 tail, per the 22:3x note).
- Disclosed flaws carried to delivery (from volleys + assembly):
  FH-A L22 words land early at the 2x cap (comes -0.90s, back -0.72s,
  dirty -0.60s); H2-C L18 words land -0.5 to -1.5s (mouth runs ahead);
  four transient PCHIP dips 2-7f at 0.43-0.49x (least-bad smooth warps);
  WIPE counter 347 lands at beat 345 (171.851s) per the corrected
  numbering; volley disclosures in TAKE_LEDGER.md (wardrobe variances,
  invented take audio dropped in D-A/O-B, goggles notes, F12 CLEAR).
- Preserved partials (NOT masters): master_partial_no-moov_20261109-0443.mp4
  (225,181,744 B, pass 1, VM reboot kill) and
  master_partial_no-moov_20261109-0616_OOM.mp4 (423,690,293 B, pass 2,
  ENOMEM at trailer; video data complete, recoverable via untrunc).
- Split halves banked: master_part1.mp4 (3504f, 92,431,678 B) +
  master_part2.mp4 (989f, 28,044,709 B) — a future re-mux needs only the
  ~7s concat+audio step, never the encodes.
- ASSEMBLY COMPLETE. No commit, no delivered flag (parent's boundary).
