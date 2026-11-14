# MV-6 "Sell the Lemons" — Lyrics Redo Notes

Date: 2026-11-12. Coordinator session 0dbe2952.
Trigger: user playback verdict 2026-11-12 ~12:41 EST (replying to the MV-3 Q5 delivery):
"lyrics on screen are wrong and no alignment to music" — redo lyrics + timings for
MV-3/4/5/6/2. Only the KINETIC CAPTION layer is replaced; the takes, the cut, the
audio, and the mouth fix all stand. Reassembly only: no new generation, no new takes.

## Method (standing, tested)

- faster-whisper large-v3-turbo, int8, cpu_threads=2, NO VAD (fatal on chant),
  numpy-array input, pinned "en", condition_on_previous_text=False, beam 1,
  repetition_penalty 1.1, no_repeat_ngram 3, collapse runs >5.
  Venv `~/workspace/tools/lyrics-venv/bin/python` (faster-whisper 1.2.1, av 18.1.0).
  Full-clip mix backbone: `song_words_v3turbo.json` (390 words, 95 segments, ~14 min).
- HYBRID: MDX-Net ONNX separated vocals (UVR-MDX-NET-Voc_FT) for 5 dense spans
  (head 0–30s, c1tail 59–74s, bridge 130–146s, fc 179–214s, outro 214–229s),
  each transcribed with the same turbo method (`song_words_*_stem.json`).
- Adjudication rule: mix turbo word times are the backbone; stems correct WORDS
  in dense spans and catch mix misses; where mix+old-base agree and the stem is
  the outlier, the stem's late bias (separation onset smearing ~0.25–0.4s on
  quiet attacks) is the explanation and mix+old win. Per-word ASR anchors are
  the timing authority — the audio decides, not the old lyric sheet or old .ass.
- Old witnesses: `SONG_WORDS.json` (faster-whisper base, 376 words), `lyrics.txt`,
  `work/beat_grid.json` (152.0 BPM, beat interval 0.3947s, 579 beats).

## What was wrong in the old captions (with examples + timestamps)

The old caption system (`work/assembly/build_ass.py` + `work/assembly/mv6.ass`,
69 caption lines, hand-invented sub-word splits) diverged from the audio in
three ways: wrong WORD, wrong TIME, and whole phrases MISSING. The full
adjudication is in the word grid (`new_word_grid.json`, "method" field per line).

### Wrong word
- **C1 tail, 64.36–67.52:** old showed "Never gonna stop." The audio sings
  "Never gonna **sell the lemons**" (mix onset 64.04 + stem "NERGA GONNA SELL
  THE LEMONS"). New line 64.04–69.12.
- **C1 L3, 50.84–53.40:** old "Sell the lemons, sell the lemons" — words were
  right, but the old base's confident reading stands; mix's "sell them" was the
  garble (p=0.0). (Kept as "sell the lemons" — a near-miss, not a change.)
- **V2 L5:** "Multipliers stack" (mix garbled "Multiply a stack"; sheet+base agree).
- **V3 L8:** "Sell the lemons" (mix garbled "Silver lemons").
- **FC L1:** "Sell the lemons, sell the lemons" (mix "Silver lemons" is a slur-garble).
- **FC L2:** "Bacon head selling lemons all day" (mix "Breaking heads" + base
  "Bacon hits" are the same garble of "Bacon head").
- **FC L4:** "Click, upgrade, sell, don't stop the play" — old CAPS line was
  RIGHT; mix garbled "Like a great sell" but the stem heard it cleanly.

### Wrong time
- **Intro hook #3:** old 15.70, audio 16.30 (mix) / 16.10 (stem) — **old 0.6s early**.
- **C1 L7:** old 61.04–64.36 started **1s late** and merged two phrases.
- **C2 L8 "Never gonna stop":** old 117.04–120.90, audio 118.76–120.92 —
  **old start 1.7s early** (the line showed during "Sell the lemons").
- **Outro (216–227s):** words right, times **systematically ~2.3s late**.
  New: "Bacon head" 216.14–216.92, "Sell the lemons" 218.14–220.30 /
  222.14–223.48 / 224.14–226.70.
- **Bridge chant 2:** old showed 4 words and ran 0.76s long (to 126.8); the
  4th "sell" is NOT sung (3 words, 123.68–126.04).
- **Bridge sustained chant (133–143s):** old SLAM ran to 145.20 — caption
  during **1.98s of silence**. The audio has SEVEN "Sell the lemons" hits
  (133.24–143.22); the 8th the old base heard (143.40–145.41) is a
  reverb-tail hallucination (mix+stem agree on 7).

### Missing entirely (caption layer silent while the song sings)
- **C1 extra line:** "And all the lemons" 62.46–64.04 — old missed it entirely
  (old base's "No" is the garble of "and all").
- **Bridge sustained chant (133–143s):** old captions had **NO line at all**
  for the 7-hit "Sell the lemons" chant — 10s of silence on the caption layer.
  New: 4 SLAM lines (hits 1–2, 3–4, 5–6, 7).
- **C1 L5/L6 merge:** old split one sung phrase into two caption lines
  (57.02–58.44 + 58.44–61.04, second ran 1s long into "Bacon head").
  New: ONE line 56.72–60.08. Same merge in C2 (110.16–113.44).
- **C1 tail "Never gonna stop" ×3:** old showed ONE line; the audio has
  THREE (69.04–70.14 / 70.08–71.26 / 71.26–72.84), merged into one SLAM line.

### Confirmed CORRECT in the old captions (kept)
- Intro line 1: old 2.72 CORRECT — stem "Bacon" @2.74 confirms; mix turbo was
  WRONG at 3.32 (missed the quiet entry; the word is a long sustained "Bacon"
  2.74–3.54, sitting exactly between beats).
- Hook #1 (6.88) and hook #2 (9.92–10.08): all witnesses agree within ~0.2s.
- V1/V2/V3: all 8 lines each match old within ~0.2s (times fine).
- Bridge "Bacon head dancing" 130.14–133.00: CORRECT (stem confirms
  "bacon head dancing while the numbers go high" 130.20–132.56).
- FC mantra (187–214): 9 short lines; stem confirms 187.96/189.48/192.70
  "Sell the lemons", 194.90 "Never gonna stop", 199.96/203.10 "Sell the lemons".
  Stem is SILENT 204.54–212.44 (MDX drops the layered/echoed vocal) — mix wins
  (2 witnesses). 206.28–209.98 "Bacon head" is the LEAST-CERTAIN line in the
  grid (mix order "SELL THEN BAKON HEAD" vs sheet order; stem silent).
  Last mantra "Sell the lemons" 211.78–213.98 (mix onset; stem 212.44 is its
  late bias).

### Bonus fix (visual, not lyric): old overlap at 127.06s
The old base master at 127.06s shows the HIGHLIGHT "AUTOMATE THE LINE…" and
the CASCADE chant "CLICK, SELL, UPGRADE, SELL" rendering ON TOP of each other
("AUTOMATECK,HE SELL, UPGRADE,THESELL,SH FLY,") — the old CASCADE tail
overlapped the next HIGHLIGHT line. The corrected chant timing (chant 2 ends
126.04, not 126.8) and the corrected br3 start (127.06, not 126.84) eliminate
it; the new master renders a clean "AUTOMATE THE LINE WATCH THE CASH FLY".

## New word grid

`work/lyrics-redo/new_word_grid.json` — **72 caption lines** (71 sung +
"(Tick, tock, click, clack)" 0.60–2.60, kept as the intro sound cue) + 33
kinetic line assignments. Caption end rule: min(last_word_end + 0.3,
next_start − 0.02). Per-word times derived from the mix (count-checked after
GARBLE normalization) except explicit per-word times in the grid for
glued/garbled tokens (fc1 "Silver" split, c1t1 stem-with-mix-onset, br4
stem-minus-"My", fcl34 L3+L4 merged, fma/fmb/fmd/fme mantra groups, out1–out4).

## Build

- `work/lyrics-redo/build_redo_ass.py` → `work/lyrics-redo/mv6_kinetic_redo.ass`:
  **318 events (72 captions + 246 kinetic), 36 kinetic lines** (SLAM hooks/chorus/
  bridge/outro, CASCADE for the 3 "Click, upgrade" lines + 2 bridge chants,
  HIGHLIGHT for bridge "Automate the line" + "Bacon head dancing" only).
  Kinetic display is UPPERCASE (old design). SLAM cap = longest single word
  (never binding); CASCADE/HIGHLIGHT cap = full line width. HIGHLIGHT Dim layer
  uses `\fad(0,150)` (no fade-in — see below). Per-line fs via inline `{\fsN}`
  override; slots computed at the scaled size.
- Standing fixes, both verified on the rebuilt .ass:
  - Per-line font-size scaling capped at **1100px estimated width** (MV-13 fix).
    Longest caption "Bacon head on the screen, the lemons still flowing." 1040px
    at fs 40. Bridge br4 "BACON HEAD DANCING WHILE THE NUMBERS GO HIGH." scaled
    to fs48 (16 events).
  - **SINGLE-backslash .ass overrides only** (MV-12 fix): **0 double-backslash
    lines** in the rebuilt .ass.
- **BUG FOUND + FIXED (2026-11-12, during the visual gate):** the first build
  wrote the per-line fs override as a NESTED brace `{\fs48}` inside the event
  override (`{\an4\pos(90,576){\fs48}\fscx112…}`), which broke libass parsing —
  the 130.06s frame on the first master (v1) printed raw tags on screen
  ("\fscx112\fscy112\t(0,90,\fscx100\fscy100)}BACON 50)}\fad(\fad(0,150)").
  Only the br4 line (fs48, 16 events) was affected. Fix: `\fs` goes INSIDE the
  existing override braces (`{\an4\pos(90,576)\fs48\fad(0,150)}BACON`), verified
  0 nested-brace lines, and test-rendered clean (br4 fits, "BACON" full-strength
  at line start). The v1 master was discarded; the delivered master is the
  v2 re-encode from the fixed .ass.

## Encode

- `work/lyrics-redo/encode_lyrics.sh`: `work/assembly/concat.mp4` (caption-free
  rebuild source, 5491f) + new .ass burned in, base-master AAC copied untouched.
  libx264 preset medium, crf 18, yuv420p, 1280×720, 24fps, `-threads 6`, faststart.
  **Do NOT use `-r 24`** — it resamples over the audio duration (228.817s × 24
  = 5491.6 → 5492f; the v1 encode came out 5492f and needed a stream-copy trim
  of the last frame). v2 drops `-r 24` and lands on 5491f directly.
- New master: `masters/mv6_sell_the_lemons_16x9_lyrics.mp4` —
  md5 **`442b2cfc06b5aeb667d34e32ef0b9229`**, 113,127,134 B, 5491f (v2: fixed .ass,
  no `-r 24`, landed on 5491f directly). The discarded v1 master (broken br4,
  5492f trimmed to 5491f) was md5 `467a7a826d29caf9628b264bfe76a256`.
  The base master `masters/mv6_sell_the_lemons_16x9.mp4` (md5
  `206ee9b07b85e9731708d96eec67e927`) is untouched.
- Chat copy: `masters/mv6_sell_the_lemons_16x9_lyrics_50mb.mp4`
  (854×480 crf 23, AAC copied untouched) — **BLOCKED, no file on disk.**
  The encode ran to ~39 MB then was killed when its parent session failed on
  a frame-extraction write; the partial was removed for a clean re-run, and
  the re-run cannot complete: the sandbox is rejecting ALL binary writes from
  exec'd processes with `Operation not permitted` (ffmpeg mp4/PNG muxers,
  Python binary writes, shell binary redirects — all EPERM; text writes still
  work). Restriction appeared ~2026-11-12 21:35 EST, after the v2 house master
  + gates completed. A 1-second mp4 test encode fails the same way. The
  sibling MV-2/MV-3/MV-4 encodes (started before the restriction) are still
  writing fine — the block affects NEW write attempts. The parent must re-run
  the chat-copy encode once the restriction clears. The house master is DONE
  and fully gated; only the chat copy is outstanding.

## Gates (v2 run, `gate_lyrics2.log` — ALL PASS; v1 run on the trimmed master
gave the same values, `gate_lyrics.log`)

- Probe: h264 1280×720 24fps, 5491f, 228.792s, AAC 48k stereo ~196k.
- Frame count: 5491 = 5491 (base) PASS — landed direct, no trim needed.
- SEI crf=18.0 PASS. faststart (moov@36, mdat@158928) PASS.
- Decoded-PCM md5 == base master (`047e89593aac4b584ff694c0ae5c3fa7`) PASS —
  the audio is the base master's AAC, untouched.
- Regression (text-free frames 0.3s, 171.5s): new-vs-base mean |diff| 0.76 / 1.24,
  new-vs-concat 0.60 / 1.03 — the encoding-noise floor (two CRF-18 re-encodes
  of the same source differ by ~0.5–1.2 mean on static frames even when aligned;
  the base shows the same vs concat). Aligned + noise-level, NOT absolute 0.
- Motion audit (near-still runs ≥12f, diff<0.5, 160×90 gray): new 6 runs,
  base 9 runs; new runs ≥24f are (7,35) and (294,82), BOTH inherited from the
  base (identical in base and new) — **no NEW frozen runs**. The new master has
  FEWER runs than the base (the new kinetic text breaks up the base's frozen
  runs at 900, 1048, 2485).
- Full-res burned-frame reads (from the v1 master for fs54 lines — unchanged
  in v2 — and from test renders of the fixed .ass for br4; the br4 + C1-tail
  reads on the v2 master file itself were blocked by the sandbox binary-write
  restriction that appeared ~21:35 EST, so the br4 fix is validated by the
  test render of the fixed .ass on the same concat source + the 0 nested-brace
  syntax check, and the v1 master proved the encoder faithfully burns whatever
  .ass is given):
  - 2.72s caption "Bacon head on the stand…" — legible, full-strength at line start.
  - 16.30s SLAM "SELL" — mid-slam-in (large, semi-transparent), caption correct.
  - 53.40s CASCADE "CLICK" — invisible at the exact frame (150ms fly-in), fully
    visible by +150ms (53.55s test render: "CLICK" legible at final position).
  - 64.04s SLAM "NEVER" — invisible at the exact frame (60ms slam-in), fully
    visible by +150ms (64.19s test render: "NEVER" legible, centered).
  - 127.06s HIGHLIGHT "AUTOMATE THE LINE WATCH THE CASH FLY" — first word
    "AUTOMATE" full-strength yellow at the exact line start (the Dim `\fad(0,150)`
    fix works); clean, no overlap (old master garbled here).
  - 130.06s HIGHLIGHT "BACON HEAD DANCING WHILE THE NUMBERS GO HIGH." (fs48) —
    full line legible, fits the frame (spans ~x95–1185), "BACON" full-strength
    at line start; caption below correct.
  - SLAM/CASCADE first words are invisible at the EXACT line-start frame by
    design (they animate in over 60–150ms from full transparency) and are fully
    visible by +150ms. That is the kinetic preset's animation, not the
    mid-fade-faint nit — the nit was the HIGHLIGHT Dim layer's 120ms fade-in,
    which is fixed (Dim now `\fad(0,150)`).

## Take-sync audit (beyond the caption layer)

None found. All divergences are in the caption layer; the video/takes were
not re-timed and no take-sync gaps were measured. (The mouth fix stands.)

## Files

- `work/lyrics-redo/transcribe_v3turbo.py` + `song_words_v3turbo.json`
- `work/lyrics-redo/separate_stems.sh`, `stem_separate.log`, `stem_driver.log`,
  `stems/*_{mix,vocals,16k}.wav`, `transcribe_stems.py`,
  `song_words_{head,c1tail,bridge,fc,outro}_stem.json`
- `work/lyrics-redo/align_lines.py`, `new_word_grid.json`
- `work/lyrics-redo/build_redo_ass.py`, `mv6_kinetic_redo.ass`
- `work/lyrics-redo/encode_lyrics.sh`, `encode_lyrics.log` (v1),
  `encode_lyrics2.log` (v2), `gate_lyrics.py`, `gate_lyrics.log`
- `masters/mv6_sell_the_lemons_16x9_lyrics.mp4` (new master),
  `masters/mv6_sell_the_lemons_16x9_lyrics_50mb.mp4` (chat copy)
