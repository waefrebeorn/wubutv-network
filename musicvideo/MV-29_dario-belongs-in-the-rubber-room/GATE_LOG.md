# MV-29 "Dario Belongs in the Rubber Room" — GATE LOG

Assembly coordinator run, 2026-11-21/22. Generation was already
complete (25/25 scenes covered, spend 35/40 video, 4 images); this
run was assembly ONLY — zero video generations fired.
Pipeline adapted from MV-28's proven swing build (plan_build.py /
build_master.py / build_captions.py / encode_master.sh), with the
MV-29 dispositions from TAKE_HISTORY.md applied in the planner.

## Authorities
- Text authority: lyrics_user_sheet.txt (user's sheet, msg 831) —
  identical to lyrics.txt.
- Timing authority: SONG_WORDS.json (269 words) + LYRIC_TIMELINE.md.
- Track: 185.216s, performed grid 122.5 BPM. Master target
  4445 frames / 185.208s picture at 24fps.

## Gates (all measured on the finished master unless noted)

- JOINED ASSERT (pre-encode, MV-17 rule): joined.mp4 probed at
  4445 frames AND 185.205s BEFORE the master encode — PASS.
  (joined md5 1b77eb8db8101cf31a08e362839db720; intermediates
  removed after delivery per clean-as-you-go.)
- FRAME COUNT: master video stream = exactly 4445 frames — PASS.
- DURATION: master = 185.216s = track duration exactly — PASS.
- SPEC: 1280×720, 24fps, h264, yuv420p; AAC-LC 48kHz stereo
  (track.mp3 re-encoded, never stream-copied); faststart verified
  (moov before mdat) — PASS.
- CRF-18 PROOF (size differential; the SEI string on this ffmpeg
  build always reads 23.0 and is never cited): CRF-23 twin of the
  same joined file with the same filter chain = 43,152,548 B vs
  house master 82,267,792 B = 1.91x — PASS (house band 1.73–1.99x).
- FREEZEDETECT (n=0.003, d=1.2, full master): ZERO freeze events —
  PASS. No freeze sits under any sung word.
- WORDMARK BUG: "~ WuBu ~" gold bottom-right verified on head
  (1.0s), mid (92.6s) and tail (184.5s) frame grabs — PASS.
- SUBTITLES BURNED IN: word-timed karaoke ASS (55 lines, 281 word
  events; bottom-center bold white on semi-transparent black bar,
  current word yellow) verified on frame grabs at 1.0 / 4.6 / 35.0 /
  92.6 / 105.5 / 107.3 / 145.0 / 184.5s — single line, correct word
  highlighted at every sample — PASS. mov_text track also present
  (55 cues) — PASS.
- MASTER TRANSCRIPT SPOT-CHECK: the finished master's own audio
  re-transcribed (faster-whisper large-v3-turbo, Checkpoint A) and
  diffed against the track's SONG_WORDS: 267 vs 269 words, sequence
  similarity 0.9776; landmark words land within 0.16s (Dario 3.50 /
  105.24 / 142.96, Yeah 168.60, Rubber 183.24). The first word's
  timestamp jitters (1.00 vs 0.00 — decoder onset placement on the
  sustained "Rubber"; its end 1.90 ≈ track 1.92 and every later
  landmark aligns, so the audio is unshifted). Residual diffs are
  echo-layer alignment noise between two ASR runs of the same
  audio — PASS.
- MOUTH SPOT-CHECKS (frame grabs): 4.6s L03 "belongs" — mouth open
  mid-word; 35.0s L09 — mouth mid-phrase; 92.6s L25 "stays" — mouth
  on the word; 105.5s L28 "Dario" (slowed seg) — mouth open in the
  sung shape; 107.3s L28 cover — bouncing-traders montage, no
  stumble mouth — PASS.
- ZERO REUSED PICTURE: planner claim ledger over all 25 takes —
  final audit reports no picture span used twice (0.15s joint
  tolerance at segment seams, the MV-28 standard) — PASS.
- WARP CAPS: every sung warp inside the 2x slow cap; slowest =
  S16 L28 "Dario" seg k=1.875 (the song itself sustains "Dario"
  105.22–107.02, 1.80s — the mouth is on the word throughout).
  Segment filter order setpts FIRST, then fps=24 — PASS.

## Dispositions applied (from the brief / TAKE_HISTORY.md)

- S04 (L07–L08) — CAPTION-CARRIED COVER. Generation was BLOCKED
  twice (integrity_check_failed / public_figure_likeness, incl. a
  wordless cosplay cover). Ships as designed cover picture:
  s03_t1 podium-mic→cash-case prop-swap span (16.98–20.34) +
  s01_t1 room-bounce span (20.34–25.28), both at k=1.0, with the
  burned-in captions carrying both lines.
- S08 L14 (52.24–57.36) — BEAT-CUT MONTAGE COVER per the bad-word
  rule: two pacing attempts hit the structural floor (ratios
  1.68 / 1.72; sung floor ~3.0s vs the 5.12s slot), no third pull.
  Cover built only from s08_t2/t1 NON-SUNG complement spans (wafer
  catch, slow walk, room moves). L13 matched from t2 (word-span
  warp 1.126). One nit inside the cover: the final 0.31s is a
  fill-stretched sliver of the t2 walk at k=1.667 (planner
  stretch, inside the 1.85 fill cap).
- S16 L28 — BAD-SPAN SPLIT per the bad-word rule: the take's
  "belong" stumble (take 4.98–5.80) is NEVER used or warped.
  "Dario" seg (take 4.02–4.98) slowed k=1.875 onto the song's
  sustained "Dario" (105.22–107.02); the song's "belongs" span
  (107.02–107.72) is covered by the same take's bouncing-traders
  tail at k=1.0; the correct "belongs in the rubber room" phrase
  (take 5.80–8.10) warps in at k=0.635 at the next good anchor.
- S01 L02 "Yeah" — take-tail token (9.00–9.70) cut as its own
  sub-segment onto 2.32–2.92. DEVIATION, disclosed: the planner
  fitted the whole 0.70s token to the 0.60s slot at k=0.857
  rather than a k=1.0 hard trim; a 14% rate change on a 0.6s
  picture-only interjection (take audio is never heard).
- S24 — KEEP take t3: the doubled head "Yeah" (0.00–0.40) is
  trimmed, never used; L45 anchors on the SECOND "Yeah"
  (0.76–1.48, k=1.139). L46 grey warp k=1.743 (word-span figure
  incl. the 0.12s tail micro-gap absorption; ledger onset figure
  1.68). The designed one-beat impact freeze was not separately
  eye-verifiable at 1fps sampling in any S24 take — no freeze
  touches the words (freezedetect on the master: zero).
- S15 / S19 / S20 wordless cutaways placed on their ledger tail
  spans (padded-tunnel bloom culmination / Huang silhouette in
  the door window / IPO bill hanging mid-air).
- S25 outro — TB head (172.90–175.216, two-wall lineup) + TA full
  (175.216–185.216, dawn-gold lineup, Dario upright, calm lean
  finish). Mid-block cut between the two wordless takes by
  design (11.76s chant block > 10s takes).

## Grey warps (phrase-level, planner word-span figures)
S02 hooks 0.692 / 0.668 (speed ×~1.45) · S12 lines 0.674 / 0.697
(speed ×~1.45) · S13 t2 lines 0.630 / 0.620 (speed ×~1.6) ·
S03 L06 1.350 · S07 L12 1.328 · S08 L13 1.126 · S24 L46 1.743 ·
S16 L28 split 1.875 / 0.635. All inside caps; setpts-first order.

## Disclosures
- S21 EVENT-READ SHORTFALL: The Freeze did NOT land — the
  orderlies move during hook 1 and stand in the tail, the inverse
  of the design. The weave reads. Ships as-is per the brief.
- S25: NEITHER outro take lands the designed tail mid-bounce
  rhyme with frame 0, and the unison sway reads minimal in both —
  disclosed at intake; TA is primary, TB alternate, mid-block cut.
- L29 (109.18–113.30): the song-side ASR hears a hook repeat
  (unmatched line at intake); the SHEET line "Talks the doom then
  he takes the cash" is what is captioned, and S17's take sang
  that sheet line verbatim (take-verified).
- CAPTION TIMING FALLBACKS: 47 of 55 lines carry real ASR word
  timings (segmentation incl. hyphen merges and documented
  ASR-side repairs: toss→talks, while→huang / hes→is, atom "and"
  matching sheet "then", plural-s tolerance, sub-0.05s decoder
  junk atoms skipped). 8 lines are syllable-weight splits: L29
  (above), L33–L38 (breakdown — ASR silent, spans display-derived
  ±~1s, wordless cutaway scenes, captions carry them), L40 (song
  ASR merged both final-chorus hooks into one stretched "Room"
  token 145.64–150.60; L39 keeps real timings with that sustain
  event clamped to its line end).
- ASSEMBLY INCIDENT (caught by the frame-grab gate, fixed,
  re-encoded): the first master encode burned captions from an
  .ass whose [Events] Format line omitted "Layer", so libass
  shifted every field and rendered all 281 word events stacked
  at once. The header in MV-28's build_captions.py SOURCE omits
  Layer — but MV-28's shipped .ass on disk includes it; the .py
  and the shipped .ass diverge. MV-29's builder is fixed
  (Format: Layer, Start, End, ...), a 10s test render verified
  single-line karaoke, and the full encode suite was re-run.
  The defective encodes were deleted before any delivery; the
  master reported in COMPLETION.json is the fixed encode.
  NOTE for future builds: copy MV-28's shipped .ass header, not
  its .py source.
- S08 cover nit and S01 k=0.857 deviation: see Dispositions.

## Spend
Video generations this run: 0 (assembly only). Project final:
35/40 video, 4 images (REF_DARIO, REF_HUANG, REF_ROOM, REF_OFFICE).
