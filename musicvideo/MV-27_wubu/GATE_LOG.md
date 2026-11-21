# MV-27 "WuBu" — GATE LOG

Master: `masters/mv27_wubu_16x9.mp4` — md5 4933d459bf24b06a8dc8a3efbd3b70e8
Chat copy: `masters/mv27_wubu_chat.mp4` (≤50 MB) + `masters/mv27_wubu_16x9_50mb.mp4` sibling (same encode; house master exceeds 100 MB)
Track: 252.011s, 127.0 BPM measured. Spend: 33/40 video calls, 5 image calls. No 429 encountered.

## Gates

- **Frame target** — PASS, EXACT. Target = round(252.010667 × 24) = 6048. Every one of the 149 segments asserted for frames AND duration at build; joined.mp4 probed at 6048 frames before the master encode; finished master count_frames = 6048.
- **Format** — PASS. One 16:9 master only: 1280×720, 24fps, H.264 yuv420p, faststart.
- **CRF 18** — PASS by SIZE DIFFERENTIAL (this VM's x264 SEI reads crf=23.0 regardless of rate control, so the SEI string is not cited): master (CRF 18 chain) = 156,710,487 B vs identical-chain CRF-23 encode = 84,020,493 B → 1.87×.
- **Audio** — PASS. track.mp3 re-encoded to AAC LC 48 kHz 192k stereo (never stream-copied). Master duration 252.010s.
- **Corner bug** — PASS. "~ WuBu ~" gold, bottom-right, verified EXACT on head/mid/tail grabs (2s/60s/130s/200s/250s + full-resolution crop).
- **Subtitles burned in** — PASS. Word-timed karaoke ASS (MV-2 v7 house style: bottom-center bold white on semi-transparent black bar, current word yellow), 358 word events / 74 caption lines, rendered into the picture; PLUS a mov_text track from the same line timings. Visible verified in master grabs.
- **Freezedetect** — PASS. Full-master scan (6048 frames): zero freeze events ≥0.5s at −50 dB.
- **Motion law** — PASS. Every take QC'd at frame 0 already moving (per-take near-dup run 0.0s in all QC rows); cuts land on moving frames; no freeze under any word.
- **G7 wrong-lyric gate** — PASS at scene level for every scene (per-take ASR in TAKE_HISTORY). Exceptions are itemised under Disclosed flaws — no wrong word was ever warped or frozen (BAD-WORD rule held).
- **Adults only** — PASS. Every take eye-checked at full resolution (per-volley contact sheets + dense mouth strip for the cover take): all performers are grown adults (30s–60s crowds); no apparent minor in any frame.
- **Zero legible on-screen text** — PASS with texture nits disclosed below. All signage/billboards/screens are blank or abstract in every kept take.
- **Zero reused footage** — PASS. The assembly planner's claim ledger was audited: no picture span is used twice (0 overlaps at 0.15s tolerance), including all cover/donor sub-cuts.
- **First 3 seconds** — PASS. Opens mid-chant at the ignition panel (mid-action, mouth open on the name chant), the switch cascade lands inside the first 3s; no titles, no ramp, no crackle intro.
- **Event doctrine** — PASS. 23 distinct named events, one per slot, checked against MV-22/23/24/25/26 stagings and appended to WUBUMV's USED_EVENTS.md at plan lock. Motif: THE ANSWERING CITY.
- **Continuity** — PASS by reference stack (5 generated refs: host/city/desk/crew/tower) carried in every vehicle; identity and wardrobe verified per take at eye-check.
- **Assembly discipline** — PASS with a process note: segments were built by one script; the first run was killed by the runtime process reaper at segment 90 (no error in the segments themselves), and the resumed run REUSED the 90 finished segments only after md5 + frame-count re-verification, encoding the remaining 59. joined.mp4 was written exactly once; the master encode ran as a single ffmpeg writer (ps-checked: zero other writers).

## Disclosed flaws (plainly)

1. **S06 singing take LOST.** The Two-Days Chair Glide generation succeeded upstream but the artifact never landed locally, and its signed delivery URL failed the signature check on recovery. It was not re-fired (a failed media request is not repeated). The S06 window (59.52–68.54s, lines L11–L13) ships as a WORDLESS EVENT COVER — The Corridor Dash — with the lines carried by the burned karaoke subtitles, per the MV-24 S09 / MV-25 refusal-cover precedent. The cover take's own audio ASR hallucinated a looped phrase at constant logprob over its music bed; take audio is never used, and a dense 0.5s mouth strip verifies the picture is wordless (mouth closed/neutral in all 20 frames).
2. **Volley-2 tool-handoff incident.** 5 of 6 calls returned tool-level failure wrappers while the upstream reported ok:true. Four artifacts were recovered intact from the delivery URLs inside the error payloads (each a valid 10.000s video; md5s in TAKE_HISTORY.md). The fifth was S06 (above).
3. **Chorus-1 "Clip it up, clip it up" (L05) has no distinct phrase** in the song's own ASR/performance (chorus 1 compresses) and no S02 take chanted it; its caption slot is covered by name-chant crowd spans. Caption timing for L05 is sequence-inferred.
4. **ASR-invisible / ASR-deaf spans.** The name lines are woo/oh chants in the song (adjudicated by sheet + take ASR + eye, never by song ASR). The final chorus (215.02–246.16s) is ASR-deaf (dense choir): its caption timings and picture phrase placements are sequence-inferred on the phrase grid; which lines each take chanted is verified from the takes' own ASR. The intro chant L01's caption span is likewise inferred.
5. **S19 triplet shortfall.** The S19 take truncated the breakdown's second triplet and sang "growing" where the song's L56 is "going" — a wrong word, never warped (BAD-WORD rule). L56–L59 slots are covered by the take's own crowd tail plus short cross-scene crowd donor spans (S02/S03) on whoa beats; captions carry the lines.
6. **S15b missed "keep it growing"** — closed by a dedicated S15c take from budget headroom; the line lands at 150.98–153.04s from S15c.
7. **S16b partial delivery.** It chanted exactly the two "keep it growing" the scene needs (0–3.06s) and then went chant-free (stomping only); the stomping tail is used as whoa cover inside S16.
8. **Grey-zone warps** (phrase band is 0.80–1.25; k = setpts multiplier): S05 L09 k=1.31, L10 k=1.28; S08 L18 k=0.63, L19 k=1.49; S13 L32 chunk k=0.57, L33 k=0.63; S14 L36 k=0.67. No vocal warp exceeds 1.49 slow-down or 0.57 speed-up. Cover stretches: S03 ×1.22, S10 ×1.36, S11 ×1.17, S19 ×1.07 applied evenly (windows are longer than the 10s takes), plus six micro-stretch cover segments ≤1.85 (longest: two 1.79 donor micro-cuts in S19).
9. **Cross-scene donor spans** (claim-audited, never under a lexical line, all on whoa/transition beats): S10/S11/S17/S20 tails borrow S01 control-room spans; S14's tail borrows S01/S02 spans; S19 borrows S02/S03 crowd spans.
10. **Timeline correction.** The intake's inferred spans for L36/L38 ("When the backlog grows") excluded the final word; measured song word times are 129.44–130.74 and 132.94–134.52 (song ASR hears "rolls" where the sheet prints "grows" — the sheet is the display authority; warps used the measured word spans).
11. **Texture nits (illegible, verified at full resolution):** neon pseudo-glyph texture in S02/S03/S09/S18 street backgrounds — no legible words; a small illegible sleeve patch on S02 t1; a small illegible chest-crest texture on the jacket in some S20 frames; S03's jacket reads brighter royal-blue (wardrobe tone drift); S06 cover corridor wall papers and exit signs are illegible texture; S13b's line-head word "Backroom" fell below the ASR screen (mouth is mid-phrase at the head).
12. **Master size** 156.7 MB — dense grain/crowd/confetti entropy at CRF 18. Chat copy (≤50 MB) and the `_50mb` sibling are provided for the release lanes.
13. **Duration bookkeeping.** joined.mp4's container duration read 251.996s against exactly 6048 frames (= 252.000s of picture) — concat metadata rounding of ~4ms; the master's container duration is 252.010s, governed by the audio track. Frame counts are exact at every stage.

## Verdict

All gates PASS; every flaw above is disclosed, none is hidden. The master's remaining judgements are matters of taste for the parent's verification pass (playback verdict outranks this log).
