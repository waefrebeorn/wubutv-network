# MV-34 GATE LOG — Assembly (2026-11-24, RECOVERY coordinator)

"Jensen's Back" — THE FULL RESTAGE. Assembly revived by the revive
detector (no assembly coordinator had ever run; the volley closed
10/10 KEEP and assembly was never chained). Method: anchors from
each take's OWN audio, chunk before warp, capped-QP warp renderer
ONLY (MV-30 fix2 lineage; endpoint-exact PCHIP retired), one
assembly pass owning work/joined.mp4, per-segment checkpoints
(segments_ledger.json + segment_manifest.md5).

## Master

- File: `masters/mv34_jensens-back_16x9.mp4`
- md5 `95765c98411f77954479f01229923f41`, 17,520,525 bytes
- Probe (end to end, post-encode): h264 1280×720 24 fps,
  **1450 frames** (= 60.416 s track at 24 fps, frame-exact);
  AAC 48 kHz stereo from track.mp3 (sole master audio);
  mov_text subtitle track, **25 cues**; duration 60.4167 s;
  faststart (moov at byte 36) ✓
- Chat copy: `masters/mv34_jensens-back_16x9_chat.mp4`, md5
  `95765c98411f77954479f01229923f41` (byte copy — the master itself
  is 17.5 MB, under the 50 MB cap; fresh name per spec)
- Joined intermediate probed BEFORE the encode: 1450 frames,
  60.417 s ✓. Single uninterrupted master encode; master re-probed
  end to end after. (The CRF-23 twin encode was interrupted once by
  a service restart AFTER the master had finished and verified;
  the twin + chat copy were completed by a follow-up unit —
  encode_finish.log. The master was never re-encoded.)

## Gate 1 — Warp-slope histogram (PRE-ENCODE STRUCTURAL GATE): PASS

6,647 derivative samples across all 14 render maps: **min 0.500,
max 2.000, out-of-cap 0.** Per-frame realized ratios in every
segment render log also inside [0.500, 2.000]
(work/assembly/maps/seg*_render.json).

| bin | samples |
|---|---|
| 0.50–0.60 | 1,824 |
| 0.60–0.70 | 797 |
| 0.70–0.80 | 586 |
| 0.80–0.90 | 405 |
| 0.90–1.00 | 378 |
| 1.00–1.10 | 351 |
| 1.10–1.25 | 235 |
| 1.25–1.50 | 129 |
| 1.50–1.75 | 278 |
| 1.75–2.00 | 541 |

## Gate 2 — Pacing law (on the finished master): PASS

Scene shots = the §5 proof: 10 shots, median 5.74 s, mean 6.04 s,
sub-1 s 0, max 6 shots in any 30 s window. Render units (14, the
four verse scenes split at word edges for gap excision): median
2.69 s (≥2.5 ✓), sub-1 s 0, sub-0.5 s 0, densest 30 s window
10 units (≤15 ✓). One shot per sung line-group; no callbacks.

## Gate 3 — Context rhythm (realized, from the render logs)

112 paired sung words measured at their realized output frames
(work/assembly/rhythm_table.json carries the full table), grid
127.0 BPM, period 0.472 s, phase 0.390 s:

- **99 / 112 within ±120 ms** of the song onset
- **107 / 112 within ±250 ms**
- **100 / 112 land inside their song beat cell** (87 inside the
  half-beat cell)

Worst residuals — all one named class (see Disclosed residuals):

| seg | word | song onset | error (ms) | in beat cell |
|---|---|---|---|---|
| S09 | the | 55.72 | −553 | no |
| S09 | line | 55.86 | −402 | no |
| S08 | goes | 42.30 | −383 | no |
| S08 | Stock | 41.14 | +360 | no |
| S08 | up, | 42.84 | −257 | yes |
| S02 | He's | 11.26 | +240 | yes |

## Gate 4 — CRF 18 proof (size differential; SEI never cited)

Same joined file, same filter chain: master (CRF 18, with audio)
17,520,525 B vs CRF-23 twin (video only) 8,387,310 B =
**2.089× differential** — CRF 18 proven. (This VM's ffmpeg stamps
crf=23.0 in the x264 SEI regardless of the requested rate control;
the differential is the valid proof.)

## Gate 5 — Master-audio agreement (MEASURED)

Master AAC decoded vs track.mp3 decoded, sample-aligned search
±2400 samples: **best offset 0 samples**, full-track correlation
**0.9973**, RMS difference 0.0122 against track RMS 0.1659 — the
difference is AAC coding noise only. The master audio IS the track.

## Gate 6 — Motion audit (MOTION LAW)

All 13 joints land on in-motion frames (cut-frame frame-diff
5.3–95.0 vs scene baselines 0.10–5.60; work/assembly/
motion_audit.json) — no halted-photo-then-move cuts. Low-diff runs
≥12 f occur only in wordless spans (S01's dark head before the
3.14 s first word, the inter-hook holds) plus one measurement
artifact adjudicated by eye: S02's first hit (t≈7.7–8.3) reads
near-still at 160×90 in the dark office, but the master frame at
t=8.00 shows the singer mid-phrase, mouth open, in near-silhouette
— the designed staging, not a freeze. No frozen frame carries a
sung word.

## Assembly adjudications (from the takes' own audio)

1. **Verse gap excisions (chunk-before-warp).** S03–S06 each sing
   line A + line B's first word, hold a 2.7–4.9 s silent pause
   INSIDE line B, then finish it; the song's line B is continuous.
   Each scene renders as two WARP units split at line B's second
   word (S03 @17.86 "the", S04 @21.64 "the", S05 @25.40 "checked",
   S06 @29.04 "said"); the pause is excised at the word edge
   (MV-33 S15/S19 precedent). The b-units run chunk-clean
   (worst drift +30 ms class).
2. **Pause-absorbed token guard.** Whisper holds line-B first-word
   tokens open across the pause (S03 "then" stamped 3.08–5.67);
   prep v2 caps the last word's effective end by its song duration
   at the mean ratio + 0.25 s. A-unit worst drifts improved from
   −984/−1014 ms (v1) to −133…−175 ms (v2).
3. **S02 stays one unit.** Its 6.24 s inter-hit gap carries THE
   BLINDS action and the song holds a real 2.40 s gap there; the
   capped-QP map compresses the gap at the 0.50 floor. Hit 2 lands
   +240 ms (realized) — disclosed below.
4. **Chorus L1 adjudication settled by the take:** S08's own ASR
   performs ONE "Jensen's back" at the Chorus L1 position (the
   sheet's double is captioned as performed — once).
5. **Take ASR completed at assembly:** S01/S03/S04/S05/S06 had no
   word-level asr_g7.json on disk; re-ran the house QC ASR
   (large-v3-turbo, NO VAD) on the KEEP takes into work/qc_s*/
   (transcripts match the ledgered QC reads exactly).

## Chunk map (14 render units / 10 scene shots)

| # | unit | take span (s) | song span (s) | frames | method |
|---|---|---|---|---|---|
| 01 | S01 | 3.55–8.32 | 0.00–7.67 | 184 | capped warp |
| 02 | S02 | 0.00–10.00 | 7.67–14.96 | 175 | capped warp |
| 03 | S03a | 0.00–4.02 | 14.96–17.88 | 70 | capped warp |
| 04 | S03b | 6.36–8.53 | 17.88–19.17 | 31 | chunk (in cap) |
| 05 | S04a | 0.00–4.52 | 19.17–21.63 | 59 | capped warp |
| 06 | S04b | 6.28–8.40 | 21.63–23.21 | 38 | capped warp |
| 07 | S05a | 0.00–3.74 | 23.21–25.42 | 53 | capped warp |
| 08 | S05b | 6.42–8.14 | 25.42–26.79 | 33 | chunk (in cap) |
| 09 | S06a | 0.00–2.68 | 26.79–29.04 | 54 | capped warp |
| 10 | S06b | 7.02–8.94 | 29.04–30.58 | 37 | chunk (in cap) |
| 11 | S07 | 0.00–9.52 | 30.58–38.50 | 190 | capped warp |
| 12 | S08 | 0.00–9.31 | 38.50–47.67 | 220 | capped warp |
| 13 | S09 | 0.00–9.34 | 47.67–56.42 | 210 | capped warp |
| 14 | S10 | 0.62–3.96 | 56.42–60.42 | 96 | chunk (in cap) |

## Subtitles

- mov_text: 25 cues (the 25 performed lines) from lyrics.srt.
- Burned-in karaoke ASS: 112 word-step events, header copied
  verbatim from the shipped MV-28 file, bottom-center bold white
  on semi-transparent black bar, current word highlighted yellow;
  **zero syllable-split fallbacks** — every word timed from the
  track's own stamps. Display text is the sheet (Chorus L4's
  "Thirty percent" rides the performed "30"/"%" tokens; Chorus
  L6 reads "Board" per the sheet).
- Spot-checked on the master: t=3.30 (H1, lights on, "Jensen's"
  highlighted), t=8.00 (H3 in the dark, "He's" highlighted),
  t=41.60 (chorus doorway, "Stock" highlighted), t=54.60 (thesis
  line, "one" highlighted), t=59.20 (tail in the chair, "He's"
  highlighted) — karaoke + gold ~ WuBu ~ bug correct in all five.

## Disclosed residuals (named, not hidden)

1. **Sustained-word class (the cap cannot close it):** the song
   sustains "Stock" for 1.16 s (S08) and "He's" for 0.96 s into
   Chorus L8's tail (S09) where the takes sing both compactly.
   The capped maps run those chunks at the 2.00 ceiling and split
   the error: S08 Stock +360 / goes −383 ms; S09 the −553 /
   line −402 ms (realized). Phrase edges on both sides land
   tight; the mouth is on the held word's shape throughout.
2. **S02 hit 2 at +240 ms** (realized): the blinds gap compresses
   at the 0.50 floor; hit 1 lands −13 ms. The scene's event (the
   blinds pull + daylight flood) plays through the gap as staged.
3. **S01 head at the 2.00 ceiling:** the take holds 5.12 s of dark
   office before H1 against the song's 3.14 s head; the head chunk
   runs at ratio 2.00 and both hook words land within ±21 ms
   (map-level). The dark hold is the plan's BLAM setup.

## Verdict

All structural gates PASS: warp-slope histogram (pre-encode),
pacing, joined probe, master probe (1450 f exact, AAC, faststart),
CRF differential 2.089×, measured audio agreement (offset 0,
corr 0.9973), context rhythm (99/112 within ±120 ms, 100/112 in
beat cell), motion audit. The master is shipped to the parent with
the residuals above disclosed. No delivered flag, no commit —
those are the parent's.
