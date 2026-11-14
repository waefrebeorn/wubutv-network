# MUSIC VIDEO LEDGER — MV-6 "Sell the Lemons"

Track: `track.mp3` md5 `aa7e65560f1b765d156755844eb57aa7`, 228.817s, 390 words
(faster-whisper large-v3-turbo; old base SONG_WORDS.json had 376 words).
Character (this track only): Bacon Head — single vocalist; Joe never sings.
Tempo 152.0 BPM (beat interval 0.3947s, 579 beats, first beat 0.163s;
`work/beat_grid.json`).

## Masters

| Master | md5 | Status |
|---|---|---|
| mv6_sell_the_lemons_16x9.mp4 (delivered) | 206ee9b07b85e9731708d96eec67e927 | delivered 2026-11-06, corrected 2026-11-08 — NEVER overwrite; base for all rework |
| mv6_sell_the_lemons_16x9_50mb.mp4 (chat copy of delivered) | (47,197,553 B, 1280×720 2-pass 1450k) | delivered chat copy of the base master |
| mv6_sell_the_lemons_16x9_lyrics.mp4 (lyrics redo) | 442b2cfc06b5aeb667d34e32ef0b9229 | 113,127,134 B, 5491f — pending parent gate + delivery |
| mv6_sell_the_lemons_16x9_lyrics_50mb.mp4 (chat copy of lyrics redo) | 7a2a61b7fa59610eea18a791ef11b7ca | 39,078,263 B, 854×480 24fps, 5491f, AAC copied (decoded-PCM md5 == house) — DELIVERED 2026-11-12 ~17:35 EST |

## Delivery flag — lyrics redo (defined 2026-11-12)

- **Flag file: `MV6_LYRICS_DELIVERED.flag`** (project root) — name proposed; parent
  decides the exact flag name.
- Meaning: the lyrics-redo master above has passed the parent's own gate
  (md5/ffprobe + burned-frame reads on the master) AND been delivered to the
  user in chat.
- Written ONLY by the parent agent, only after delivery. The lyrics-redo
  coordinator never writes this flag, never commits, never announces.

## Lyrics redo (2026-11-12)

Trigger: user playback verdict 2026-11-12 ~12:41 EST (replying to the MV-3 Q5
delivery): "lyrics on screen are wrong and no alignment to music" — redo lyrics
+ timings for MV-3/4/5/6/2. Only the KINETIC CAPTION layer is replaced; the
takes, the cut, the audio, and the mouth fix all stand. Reassembly only: no new
generation, no new takes, no character changes.

Method: faster-whisper large-v3-turbo full-clip mix backbone (390 words) +
MDX-Net ONNX separated-vocal hybrid for 5 dense spans (head, c1tail, bridge, fc,
outro). Per-word ASR anchors are the timing authority. Full adjudication in
`work/lyrics-redo/LYRICS_REDO_NOTES.md`; new word grid in
`work/lyrics-redo/new_word_grid.json` (72 caption lines); rebuilt .ass in
`work/lyrics-redo/mv6_kinetic_redo.ass` (318 events: 72 captions + 246 kinetic,
36 kinetic lines).

### What was wrong (old captions vs audio)

- **Wrong word:** C1 tail "Never gonna stop." → "Never gonna **sell the lemons**"
  (64.04–69.12); FC L2 "Bacon hits" → "Bacon head selling lemons all day";
  V2 L5 "Multipliers stack"; V3 L8 / FC L1 "Silver lemons" → "Sell the lemons".
- **Wrong time:** intro hook #3 old 15.70 → audio 16.30 (**0.6s early**); C1 L7
  old started **1s late**; C2 L8 "Never gonna stop" old 117.04 → audio 118.76
  (**1.7s early**); outro times **systematically ~2.3s late** (new 216.14–226.70);
  bridge chant 2 old ran 0.76s long (4th "sell" not sung); bridge sustained
  SLAM ran to 145.20 — caption during **1.98s of silence**.
- **Missing entirely:** "And all the lemons" 62.46–64.04 (old missed it); the
  bridge sustained 7-hit "Sell the lemons" chant 133–143s (old captions had
  **NO line at all** — 10s silent); C1/C2 L5+L6 were each one sung phrase split
  into two caption lines (merged to one line each); C1 tail has THREE "Never
  gonna stop" (old showed one).
- **Bonus fix:** old base at 127.06s rendered the HIGHLIGHT "AUTOMATE THE
  LINE…" and the CASCADE chant on top of each other (garbled overlap); the
  corrected chant timing + br3 start eliminate it.
- **Confirmed correct in old:** intro line 1 (2.72), hooks #1/#2, V1/V2/V3 times,
  bridge "Bacon head dancing" (130.14–133.00), FC mantra lines.

### Build

- `work/lyrics-redo/build_redo_ass.py` → `mv6_kinetic_redo.ass`. Standing fixes
  verified: per-line fs capped at 1100px est. width (br4 scaled to fs48);
  **0 double-backslash lines** (MV-12 fix).
- **BUG FOUND + FIXED during the visual gate:** the first build wrote the fs
  override as a nested brace `{\fs48}` inside the event override, which broke
  libass — the v1 master's 130.06s frame printed raw tags on screen. Fixed
  (`\fs` inside the existing braces), verified 0 nested-brace lines, and
  test-rendered clean. The v1 master (md5 `467a7a826d29caf9628b264bfe76a256`) was
  discarded; the delivered master is the v2 re-encode from the fixed .ass.
- Encode: `work/assembly/concat.mp4` (caption-free, 5491f) + new .ass, base AAC
  copied untouched; libx264 CRF 18, yuv420p 1280×720 24fps, faststart.
  **Do NOT use `-r 24`** — it pads a 5492nd frame (v1 needed a stream-copy trim;
  v2 drops `-r 24` and lands on 5491f directly).

### Gates (v2 run, `work/lyrics-redo/gate_lyrics2.log` — ALL PASS)

- Probe: h264 1280×720 24fps, 5491f, 228.792s, AAC 48k stereo ~196k.
- Frame count: 5491 = 5491 (base) PASS. SEI crf=18.0 PASS. faststart PASS.
- Decoded-PCM md5 == base (`047e89593aac4b584ff694c0ae5c3fa7`) PASS.
- Regression (text-free frames 0.3s, 171.5s): mean |diff| 0.76 / 1.24 — the
  encoding-noise floor (two CRF-18 re-encodes of the same source differ by
  ~0.5–1.2 mean on static frames even when aligned). Aligned + noise-level.
- Motion audit: new 6 runs, base 9 runs; new runs ≥24f are (7,35) and (294,82),
  BOTH inherited from the base — **no NEW frozen runs**.
- Full-res burned-frame reads: captions legible + full-strength at line starts
  (2.72s "Bacon head on the stand…"); SLAM "SELL" (16.30s) and "NEVER" (64.19s,
  +150ms) legible; CASCADE "CLICK" (53.55s, +150ms) legible at final position;
  HIGHLIGHT "AUTOMATE…" (127.06s) first word full-strength yellow at line start
  (Dim `\fad(0,150)` fix works), clean, no overlap; HIGHLIGHT br4 (130.06s,
  fs48) full line legible, fits the frame. SLAM/CASCADE first words are
  invisible at the EXACT line-start frame by design (they animate in over
  60–150ms from full transparency) and are fully visible by +150ms — that is
  the kinetic preset's animation, not the mid-fade-faint nit (which was the
  HIGHLIGHT Dim layer's 120ms fade-in, now fixed).
- Note: the br4 + C1-tail frame reads on the v2 master file itself were blocked
  by a sandbox binary-write restriction (see below); the br4 fix is validated
  by the test render of the fixed .ass on the same concat source + the 0
  nested-brace syntax check. The v1 master (same encode path) proved the
  encoder faithfully burns whatever .ass is given.

### Chat copy — RESOLVED 2026-11-12 ~17:35 EST (parent encode)

- The restriction flaps per-session: the parent's session could write binary,
  and the parent re-ran the encode directly:
  `ffmpeg -y -i masters/mv6_sell_the_lemons_16x9_lyrics.mp4 -vf scale=854:480
  -c:v libx264 -preset medium -crf 23 -pix_fmt yuv420p -c:a copy
  -movflags +faststart masters/mv6_sell_the_lemons_16x9_lyrics_50mb.mp4`
  RC=0. Chat copy: md5 `7a2a61b7fa59610eea18a791ef11b7ca`, 39,078,263 B,
  854×480 24fps, 5491f, 228.817s, AAC copied untouched (decoded-PCM md5
  `047e89593aac4b584ff694c0ae5c3fa7` == house), faststart (moov@40).
- Parent full-res burned-kinetic reads on the v2 master (work/lyrics-redo/
  parent_qc/): hook3 16.5s "SELL", C1 tail 65.0s "NEVER", 127.5s "AUTOMATE
  THE LINE…" (no overlap), bridge chant 135.0s "THE" — 4/4 clean.
- Flag `MV6_LYRICS_DELIVERED.flag` written by the parent; chat copy delivered
  to the user 2026-11-12 ~17:35 EST. Registry `mv-lyrics-mv6` → done.

### Chat copy — BLOCKED (sandbox binary-write restriction) [HISTORICAL]

- The chat-copy encode (854×480 crf 23, AAC copied) was launched, ran to
  ~39 MB, then was killed when its parent session failed on a frame-extraction
  write. The partial file was removed for a clean re-run.
- **The re-run cannot complete right now:** the sandbox is rejecting ALL binary
  writes from exec'd processes with `Operation not permitted` (ffmpeg mp4/PNG
  muxers, Python binary writes, shell binary redirects — all EPERM; text writes
  still work). The restriction appeared ~2026-11-12 21:35 EST, after the v2
  house master + gates completed. A 1-second mp4 test encode fails the same way.
- The sibling MV-2/MV-3/MV-4 encodes (started before the restriction) are still
  writing their mp4s — the block affects NEW write attempts.
- **Action needed (parent):** re-run the chat-copy encode once the restriction
  clears (or from a session that can write binary):
  `ffmpeg -y -i masters/mv6_sell_the_lemons_16x9_lyrics.mp4 -vf scale=854:480
  -c:v libx264 -preset medium -crf 23 -pix_fmt yuv420p -c:a copy
  -movflags +faststart masters/mv6_sell_the_lemons_16x9_lyrics_50mb.mp4`
  Expect ~25–40 MB (must be ≤50 MB). Record its md5 + size here and in the report.
- The house master is DONE and fully gated; only the chat copy is outstanding.

### Take-sync audit (beyond the caption layer)

None found. All divergences are in the caption layer; the video/takes were not
re-timed and no take-sync gaps were measured. (The mouth fix stands.)
