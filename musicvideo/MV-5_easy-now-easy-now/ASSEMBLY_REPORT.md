# MV-5 ASSEMBLY REPORT — "Easy now, easy now (THE VOICE)"

Master: `masters/mv5_easy_now_easy_now_16x9.mp4`
- **md5 `e35be156af5f9c62a5a96fc819354640`**, 113,086,468 B, 1280×720 h264 24fps,
  4954 frames, 206.417s (4954/24; song 206.400s, +0.017s frame rounding), AAC 48kHz
  stereo, faststart. ONE 16:9 only. No 9:16, no chat copy.
- **DELIVERED 2026-11-05 ~10:02 EST** (commit 3572b7cf; MV5_DELIVERED.flag written,
  announced to IRC, kickstand ladder disabled). This report is the delivered
  master's validation record.
- Sole master audio: `track.mp3` (md5 `0c1bcafa568547e2d4fa36e133ad3626`, verified
  before muxing, muxed untouched). Generated clip audio dropped. Captions
  `captions_16x9.ass` (453 events, 0 overlaps) burned in; `~ WuBu ~` bug on all frames.
- Build: `assemble_mv5.py` from `work/assembly_fit_mv5.json` (139 pieces, 4954 frames).
  Encode launched detached 14:29 EST 2026-11-05, BUILD OK 14:37 EST (~8 min).
  Full decode verified: 4954 frames, 0 errors. CUTLIST.md is the scene→take map.
- Validation: `validate_master_mv5.py` rerun 2026-11-05 ~15:05 EST after fixing the
  line-151 results-JSON bug (`best` shadowed by the motion-run variable; lag/corr
  now saved directly as `audio_lag`/`audio_corr`). Rerun completed cleanly and
  wrote `work/master_dictation.json` + `work/master_motion.json`.

## Method (WORD-SYNC, Slopcannon stage 6)

Per-word offsets measured from fresh prompted transcriptions of every KEEP take
(`work/assembly_take_words/`, faster-whisper base, each scene's own performed lines
as prompt) against SONG_WORDS.json, placed by min-total-cost assignment
(`scipy.linear_sum_assignment`, |offset| ≤ 2.0s). Warps in [0.80, 1.25] except the
two sanctioned S17 grey rescues (0.71/0.65). No frozen frame while words play
(the one exception is the S01 pre-word leader freeze, MV-3 precedent).
Structural scenes are donor montage (KEEP takes' post-word tails first, then
REJECTED takes' silent tails — delivery-only rejects, picture on-brief — used ONLY
as silent reaction/B-roll, never as a sung take; each of the 67 slices
motion-verified: mean diff ≥ 0.10 at 160×90 and longest near-dup run < 24f).
Two slices were skipped by the motion check (S14 t1 tail: 29f near-dup run;
S21 t3 tail end: mean 0.07).

Whole-clip SPAN warps fail when a take's internal pace is uneven, so S01/S04/S07/S12
use per-line placement (S07 median 0.763→0.202, S04 0.306→0.100, S01 max 1.746→0.443,
S12 L43 recovered from +2–4s late to 12/12 paired). Whisper repeat-collapses
doubled refrains ("Easy now, easy now" → one pair), so refrains are placed by SPAN,
not word count. SONG_WORDS word times jitter ±0.3s against the line table at section
boundaries (L56/L65/L80/L96/L103/L107) — refrain placements anchor to line-table
starts and word-level offsets are reported honestly.

## Gate results

### Audio identity — PASS (decisive)
Master audio vs track.mp3: **lag 0 samples (0.0000s), correlation 0.9986**
(30s window, lag search ±1s). The master audio IS the song, sample-aligned,
complete, correctly timed. This is the mux proof.

### Master dictation — ADJUDICATED: Whisper recall, not a sync fail
The validator's own "AUDIO GATE: FAIL" is a dictation-recall threshold
(median |offset| ≤ 0.05s and ≤ 5 missing words). It does not veto this master,
for four reasons, all measured:

1. **The master audio is provably track.mp3 itself** — audio identity PASS, lag 0,
   correlation 0.9986 (section (a) above). The mux cannot be the wrong song,
   truncated, or drifted: the audio is the song, sample-aligned. A dictation
   cannot contradict a sample-level identity check.
2. **The missing words are the intro "Easy now" refrains.** The rerun's dictation
   (500 words) opens with "Blue" at 30.0s — Whisper drops the entire first 30s
   (I01–I08, the intro refrains + vocalise + first verse lines). The missing list
   starts I01 "Easy now easy now", I02 "We ride we ride", I03 "Easy now easy now".
   This is a repeat-heavy song: "Easy now" recurs dozens of times, and Whisper's
   word-level transcription collapses repeats and drops the soft crooned intro.
3. **The control proves it is a Whisper limitation, not a master defect.**
   Transcribing track.mp3 ITSELF (base, unprompted) gives 475 words, 251/546 pairs,
   median 0.220s, and drops the same first 30s. The known-good song fails the same
   way. Two more Whisper runs on the master (base prompted: 276/546, median 0.220s;
   small: 380/546, median 0.220s, hallucinating "oh" ×222) all fail the same way.
4. **The dictation count is not even stable run to run** — first run 556 words /
   271 pairs, rerun 500 words / 246 pairs, same median 0.180s. A measurement that
   moves by 25 pairs between identical runs is recall variance, not a master property.

Rerun numbers (the canonical validation output): **500 dictated words, 246/546
pairs, median |offset| 0.180s, max 0.500s, 254 dictated words with no song match,
300 song words with no dictated match.** The paired words that DO match land at
median 0.180s — the dictation hears the song, late and incompletely, which is what
Whisper does on this track.

The operative word-sync measurement is therefore the fit-level per-word score
below — measured from the takes themselves (prompted transcription, which worked
cleanly), placed by the assembly — plus the caption spot-checks (correct at every
sampled time: 1.81s "Easy now", 22.15s "Bare feet", 106s "You said, don't think
too hard", 150s "We stay out in it", 168s "No, no, no", 205s "Till the morning
comes"). A dictation-recall threshold does not veto a master whose picture fit is
measured.

### Word sync (fit-level, placed-time min-cost assignment) — the operative numbers
202 pairs / 237 song words in sung scenes (the other 309 song words are in
structural-cover scenes or covered portions — captioned, not mouth-sung).
**158/202 within ±0.50s (78%)**. Per-scene medians:

| Scene | Pairs | Median |off| | Max |off| | Within ±0.50s |
|---|---|---|---|---|
| S01 | 16/16 | 0.238 | 0.443 | 16/16 |
| S04 | 22/22 | 0.100 | 0.479 | 22/22 |
| S05 | 16/16 | 0.342 | 0.888 | 10/16 |
| S06 | 14/14 | 0.174 | 0.880 | 10/14 |
| S07 | 20/20 | 0.202 | 0.665 | 19/20 |
| S08 | 7/12 | 0.322 | 0.423 | 7/7 |
| S09 | 9/16 | 0.197 | 0.346 | 9/9 |
| S11 | 8/12 | 0.336 | 0.430 | 8/8 |
| S12 | 12/12 | 0.268 | 1.272 | 8/12 |
| S15 | 5/5 | 0.897 | 1.891 | 1/5 |
| S17 | 8/16 | 0.290 | 0.562 | 7/8 |
| S19b | 13/13 | 0.200 | 0.571 | 12/13 |
| S20 | 4/4 | 0.732 | 0.788 | 1/4 |
| S21 | 23/23 | 0.724 | 1.368 | 7/23 |
| S23 | 9/16 | 0.282 | 0.775 | 7/9 |
| S25 | 4/8 | 0.291 | 0.333 | 4/4 |
| S26 | 4/4 | 0.176 | 0.384 | 4/4 |
| S27 | 4/4 | 0.231 | 1.751 | 3/4 |
| S28 | 4/4 | 0.160 | 0.516 | 3/4 |

Refrain scenes show ~half the song words as "missing" — those are Whisper's
repeat-collapse (each doubled "Easy now" reported as one pair), sung by the take,
not missing words. CAT-half words in split lines (S11 L40, S23 L96 "run") are
covered, not sung.

### Motion gate — PASS
Decoded 4954 frames at 160×90 and 320×180. Overall mean diff 5.149 (160×90).
**Longest near-dup run 39f at frames 0–39 (0.00–1.62s) at BOTH resolutions — this
is the sanctioned S01 pre-word leader freeze** (frame 0 held 40f before the first
word at 1.66s; MV-3 precedent), not a vocal freeze. Per-scene vocal longest
near-dup runs all ≤13f (S07 13f, S01 9f, S28 8f, S21 7f) — well below the 24f
frame-rule threshold. No vocal freeze anywhere.
S01 vocal mean 0.470 at 160×90 — this is the KNOWN S01 t1 take property (QC
vocal mean 0.486, carried forward as a disclosure; parent decides), not a new
master defect. S07 vocal mean 0.531, run 13f (slow-warped L13) — PASS.

### Picture gate — PASS (spot-checked at full size)
- Locks hold in every sampled frame: CAT black / red collar / yellow bell / blue
  eyes; GIRL straw hat (or solid red — S01 class) / purple hair / purple eyeshadow /
  red lipstick / red short jacket / cut-off jean shorts; BIKE blue / black tires /
  white rims / front basket (CAT rides in it).
- Mouths correct: open on sung words (CAT singing "Easy" 1.81s, "Bare" 22.15s,
  "Till the morning comes" 205s), closed on structural covers (S13 106s, S19a 150s,
  S22 168s — all mouths closed, captions on song times).
- Captions correct at every sampled time (see above); `~ WuBu ~` bug on all frames;
  no generated text, no watermark, no licensed material.
- Known drift nits (disclosed, not rejects): CAT fangs on singing beats (205s);
  background extras reusing the girl's purple hair (S13 106s); solid red hat in
  S19a (S01 class); basket wicker colour variance.

## Per-scene disposition (see CUTLIST.md for the full map)

- **KEEP (22):** S01 t1 (per-line; leader freeze 40f pre-word), S02 t1 (cutaway @1.0),
  S03 t1 (vocalise SPAN 0.889), S04 t1 (per-line), S05 t1 (SPAN 1.030), S06 t1
  (SPAN 0.80 + tail-loop deficit), S07 t1 (per-line), S08 t2 (per-refrain; R3 CAT
  reaction cover), S09 t1 (per-refrain; warp rescue ≤1.5x, max 1.133), S10 t1
  (cutaway @1.0), S11 t4 (L38 montage cover, L39 grey rescue 0.80, L40 tail 0.88,
  trimmed 10.00s→7.84s), S12 t1 (per-line; L43 overruns 1.41s into L44),
  S15 t1 (GREY RESCUE SPAN 0.914), S17 t1 (GREY RESCUE per-refrain: R1 0.93,
  R2 0.71 grey, R3 0.65 grey, R4 1.09 by RMS envelope 6.9–8.0s; R3/R4 times are QC's
  adjudication + RMS, not Whisper's), S18 t1 (cutaway @1.0), S19b t1 (GREY RESCUE
  SPAN 0.808; "We still" one unit at the head), S20 t1 (GREY RESCUE SPAN 0.80;
  "breeze" overruns 1.05s), S23 t1 (per-refrain; "No" onset 5.64 per unprompted +
  mouth frame), S25 t1 (per-refrain; R1 0.80), S26 t1 (pre-word donor cover 39f +
  SPAN 0.80), S27 t1 (SPAN 1.232; breath gap), S28 t1 (GREY RESCUE SPAN 0.80, trim 0.05s).
- **PARTIAL (1):** S21 t3 — head L82–L86 by measured word times (SPAN 0.80, drift to
  +1.37 on "pace"); tail L87–L89 montage cover + captions (not a mouth-sung slot).
- **STRUCTURAL (6, "not a mouth-sung slot"):** S13 (static MCU girl + CAT reaction
  inserts), S14 (dusk-rail CAT reaction / B-roll), S16 (chorus cover like S13),
  S19a (grey-sky CAT reaction / B-roll), S22 (head-shake reaction cover, 1.66s slot),
  S24 (chorus cover like S16). All captions keyed to song word times.

## Honest disclosures for the user

1. **Weakest sync — S15 (median 0.897s, max 1.891s, 1/5 within ±0.5s).** Grey rescue:
   the take's fast pickups ("Keep it loose, keep it low") land +0.26 to +1.89s late.
   The whole slot is SPAN-warped 0.914 over the held vocalise; the pickups cannot be
   placed tighter without breaking the warp band.
2. **S20 (median 0.732s).** Band-edge 0.80 warp; "breeze" overruns 1.05s past the line
   end into L81's window.
3. **S21 (median 0.724s, max 1.368s).** Band-edge 0.80 SPAN over the head; drift
   grows across the slot (last word "pace" +1.37s). Tail is montage cover.
4. **S27 "easy" +1.75s.** The take's breath gap (1.74–2.72s) is longer than the
   song's; the held line's third word lands late. The other three words are within
   ±0.5s.
5. **S12 "bills" +1.27s.** The take sings L43 far too slowly for its 1.60s window;
   L43 overruns 1.41s into L44 (covered by donor). L41/L43 at the 0.80 band edge.
6. **S17 R3 placed +0.34s late** (grey rescue; R3/R4 times are QC adjudication + RMS,
   not Whisper's). During 135.02–135.36s the song sings L69's "Easy now" over a
   donor listening shot. Within the disclosed grey range (median 0.290s).
7. **S01 vocal mean 0.470 (take property, disclosed at QC as 0.486).** Slow drift,
   not a freeze (vocal run 9f). Parent decides; not overruled here.
8. **S23 low-motion disclosure stands** (vocal mean 0.558 @160×90 in QC; 0.642 in the
   master re-audit). The CAT listens through most of the slot; mouth opens on the
   refrains.
9. **S01 leader freeze: the CAT's mouth is open in frame 0** (the take starts mid-"Easy"),
   held 1.66s before the first word. Pre-word only, MV-3 precedent — a visual oddity,
   not a sync error.
10. **Master dictation is adjudicated, not a gate fail** (see above) — the validator's
    own "AUDIO GATE: FAIL" is a dictation-recall threshold (246/546 pairs, median
    0.180s, rerun). The master audio is provably track.mp3 (identity 0.9986, lag 0);
    the missing words are the intro "Easy now" refrains Whisper drops; the control
    on track.mp3 itself fails the same way (251/546). The fit-level scores are the
    operative sync numbers.
11. **Donor policy deviation from MV-4 (documented):** structural covers + response
    windows + gaps need ~1276f of non-word picture; KEEP takes' clean non-word footage
    supplies only ~655f, so the shortfall comes from REJECTED takes' silent post-word
    tails / inter-word silences, used ONLY as silent reaction/B-roll, never as a sung
    take. Those takes were rejected on DELIVERY only (picture passed QC, no G1/G2
    fails); each slice is motion-verified. One slice was replaced after a full-size
    read (S08 L22: S09's tail showed the girl's mouth open in a small "o" after
    "now" — wrong mouth for a CAT line; replaced with S01's CAT close-up tail).
12. **Drift nits carried (not rejects):** CAT fangs on singing beats; generator seats
    the girl ON the bike where vehicles ask standing; hat variance (solid red vs
    straw); basket wicker colour variance + basket reads rear not front (S24);
    background extras reusing the girl's purple hair + a black dog (S10) + duplicate
    cat on the counter (S11 t4); render-style drift (S19 t3 realistic fur, S22 t2
    round eyes/pink nose — the "glossy black fur, flat anime cel style" lock is not
    fully holding).

## Files

- `masters/mv5_easy_now_easy_now_16x9.mp4` (the master)
- `assemble_mv5.py`, `work/assemble_mv5.log` (build)
- `work/fit_mv5.py`, `work/assembly_fit_mv5.json`, `work/fit_mv5.log` (placement)
- `work/measure_takes_mv5.py`, `work/assembly_take_words/` (take word times + RMS)
- `make_captions_mv5.py`, `captions_16x9.ass` (453 events)
- `validate_master_mv5.py`, `work/validate_master_mv5.log` (first run, crashed at
  the results-JSON write), `work/validate_master_mv5_rerun.log` (rerun, completed
  cleanly), `work/master_dictation.json` (rerun: 500 words) +
  `work/master_motion.json` (rerun: lag 0, corr 0.9986, 246 pairs, 300 missing)
  (gates; dictation)
- `work/master_dictation_prompted.json` (base prompted, first run),
  `work/master_dictation_small.json` (small unprompted),
  `work/track_dictation_control.json` (base unprompted on track.mp3 itself)
- `work/motion_reaudit_mv5.py`, `work/motion_reaudit.log`,
  `work/master_motion_fixed.json` (motion re-audit, fixed SUNG kinds)
- `validate_pictures_mv5.py`, `work/master_contact_sheet.jpg`,
  `work/donor_contact_sheet.jpg` (picture checks)
- `make_cutlist_mv5.py`, `CUTLIST.md`, `ASSEMBLY_REPORT.md` (this file)
- `work/take_md5s.json` (44 take md5s)
