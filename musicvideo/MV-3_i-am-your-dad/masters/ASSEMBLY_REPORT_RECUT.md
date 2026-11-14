# MV-3 "I Am Your Dad (HE IS NOT YOUR DAD, RUN)" — word-aligned re-cut assembly report

Built from existing takes only, per `CUTLIST_RECUT.md` and `MV3_RECUT_MEASUREMENTS.md`.
No new video generation, no re-measurement. Render script: `assemble_mv3_recut.py`
(bare invocation only prints the plan; the build used the script's own `build`
then `finals` subcommands). The previous resume attempt's truncated
16:9 intermediate (11,796,528 B, no moov) was overwritten cleanly by the rebuild.

## Finals (verified)

| File | md5 | Size (B) | Frames | Duration | Video | Audio |
|---|---|---|---|---|---|---|
| `mv3_i_am_your_dad_16x9_recut.mp4` | `300c89feaf5276763e0f8598bc2656d6` | 82,781,036 | 8516 | 354.833 s | h264 1280x720, 24 fps | AAC 48 kHz stereo |
| `mv3_i_am_your_dad_9x16_recut.mp4` | `de6230accec1161a81d62046ef233c18` | 101,916,791 | 8516 | 354.833 s | h264 720x1280, 24 fps | AAC 48 kHz stereo |
| `mv3_i_am_your_dad_16x9_recut_chat.mp4` | `b9f508e3a48ffeb0354ffe994376ae0e` | 23,711,895 | 8516 | 354.833 s | h264 854x480, 24 fps | AAC 48 kHz stereo |

Intermediates (on disk, git-ignored): `mv3_intermediate_16x9_recut.mp4`
(159,868,031 B, 8516 frames) and `mv3_intermediate_9x16_recut.mp4`
(234,160,336 B, 8516 frames).

Verification: `ffprobe -count_frames` on each final read exactly 8516 video
frames (full decode, no errors) at the dimensions above, with the untouched
master song audio (`track.mp3`) muxed in. The rejected delivered masters were
never touched or overwritten — all re-cut outputs carry `_recut` in the name.

**Delivery note:** the 16:9 re-cut md5 and byte size match the master already
delivered ~01:13 EST 2026-11-05 and ACCEPTED by the user ("focus on only the
one master this is okay"). Do NOT re-deliver it. Per the user's 01:31 EST
standing rule, only one 16:9 goes forward — the 9:16 and chat copy are
de-prioritized and left on disk, not chased.

## How the re-cut differs from the rejected cut

- Segment boundaries unchanged from the delivered cut (leader 0–2.82 s = S01
  frame 0 held, the one pre-word freeze).
- Every mouth scene trimmed at its first word and placed at segment start, so
  the first word lands on the song's first word.
- Whole-clip setpts warps: usable takes warped by their line ratio (the main
  fix, 14 scenes); grey takes warped to the band-edge FACTOR 1.25 / 0.80
  (all factors inside 0.80–1.25).
- S15 / S17 lead-in trimmed at first word.
- Deficits covered by tail-loops of each take's own post-line tail (moving,
  never freeze). Shortfalls tail-looped: S21 10f, S23 43f, S24 53f, S25 28f,
  S28 50f, S36 23f, S39 31f. Overshoots trimmed by the segment cut.
- Captions reused unchanged (already keyed to SONG word times); master audio
  unchanged; 9:16 is a per-scene reframe via `crops.json`.

## Honest disclosures (from the cutlist — NOT sync claims)

- S07: final word cut 0.15 s by the segment boundary.
- S29: final words fall past the segment cut.
- S31–S33: MANTRA-SLICE cover — repeats are not individually matched.
- S37: hold-loop MONTAGE cover — no sung-burst replay.
- S39: whole-slot MONTAGE cover (ratio 0.573, below the grey floor) — no sync claim.
- Structural cover (no mouth-sung slot): S04, S05, S21, S24, S25, S30, S35.

## What was NOT verified in this build

Word-level sync was built per the measured cutlist warps, but the finished
master was NOT re-measured word-by-word in this run. A word-match audit on
the master is still owed (parent / cross-check sync R&D). Nothing in this
report claims the mouths are proven on the song — only that the frames,
dimensions, duration, decode, and audio are verified as above.
