# MV-2 "Toll Roads Are Dumb" — v6 assembly map (2026-11-04)

## Standing language (do not reword into stronger claims)

Mouth-sung slots carry "directional mouth movement roughly occupying the
described window" — never "lip-synced", never "fixed", never
frame-accurate lip-sync. Covered slots are flagged "not a mouth-sung
slot". The master audio is the untouched `track.mp3` (md5
`9e5ff10876cda8ac17dcb22b79c3f00a`); generated clip audio is discarded
everywhere. No take is reused as vocal coverage at another position,
except the two disclosed within-scene assignments below (S07-tail
anchor, C1-hook2, C2-hook2 — each a scene's own take covering an
occurrence of its own scene's line, gates passing on its own timing).

## Build

- Script: `masters_work_v6/assemble.py` (frame-exact tiling, same method
  as the viewing-cut renderer: N = round(out_end×24) − round(out_start×24)
  frames per segment, input-side `-ss`/`-t`, `setpts` factor + `fps=24` +
  `scale=1280:720`, crf 18, concat).
- Cutlist: `masters_work_v6/cutlist_v6.json` — 104 clips, exactly 6432
  frames. Every clip ≤10s. No per-word warp outside 0.80–1.25x. No
  freeze during words (verified by the motion audit on the master
  itself, §5).
- Captions: `masters_work_v6/captions.ass` — line block + per-word
  highlight from measured song word times (`SONG_WORDS_BASE.json`),
  highlight 3 frames early, performed words where sheet and performance
  differ (see §4).
- Corner bug: `~ WuBu ~`, top-right, CADMIUM yellow, on all masters.
- Outputs (all UNCOMMITTED — parent verifies, commits, delivers):
  `masters/mv2_toll_roads_are_dumb_v6_16x9.mp4` (1280x720/24fps),
  `masters/mv2_toll_roads_are_dumb_v6_9x16.mp4` (720x1280 proper reframe,
  center 9:16 crop — the performer is centered in every take, verified
  on sample frames, never a blind crop),
  `masters/mv2_toll_roads_are_dumb_v6_16x9_chat.mp4` (chat-sized 16:9).
- Do NOT create `V6_DELIVERED.flag` — the parent creates it at delivery.

## 1. Slot table — mouth-sung slots

Factor = take vocal span ÷ song span. Ratio = song span ÷ take vocal
span. "Scaled" = the S09-precedent assembly span (warped boundaries
matched to scaled within ~0.08s); where scaled is used, the factor shown
is the scaled factor and the measured ratio is noted.

| Slot | Song span | Take (take span, factor) | Ratio | Gates | Disclosures |
|---|---|---|---|---|---|
| S01 | 4.44–13.36 | S01 t4 (0–9.26, f=1.038) | 1.038 | lyric PASS, frame PASS (mean 1.91, run 0) | None. Caption splits on the song's 2.32s spoken pause after "Yeah." |
| S02a | 20.12–21.44 (+head from 18.95) | S02 t4 (0–3.04, f=1.111) | — | lyric PASS, frame PASS (mean 1.99, run 1) | "roads" 21.44–21.98 unmouthed micro-gap (mouth finishes "toll" as the clip ends) |
| S02b | 22.68–27.34 | S02 t4 (4.06–9.24, f=1.111) | — | lyric PASS, frame PASS (mean 0.58, run 3) | "roll" heard as "road" (substitution); second "they" 26.18–26.36 effectively dropped (take's "they" lands 1 frame into the word's tail); final "go" trimmed 2 frames early (take 9.24 vs word end 9.32) |
| S03 | 27.34–34.32 | S03 v6gap t1 (0–8.60, f=1.232) | 0.81 | lyric PASS (20/20), frame PASS, character PASS, text PASS (volley 14) | None |
| S04a | 34.56–41.30 | S04a v6final t1 warped (0–8.423 scaled, f=1.2497) | meas 0.799 / scaled 0.800 | lyric PASS (22 words matched; record's "21" is a miscount), frame PASS warped (mean 0.64, run 6), character INCONSISTENT (see note †), text PASS (volley 17) | None on lyric. Closes the GAP-A "Now they got" lead with it. Warped S04 t1 (profile/facing FAIL) NOT used. Restage (volley 18) REJECTED: lyric FAIL (missing tail), photorealistic + text FAIL. † Character: see note † below. |
| S04b | 41.90–49.38 | S04 t5 (1.32–9.0, f=1.027) | 1.027 | lyric PASS, frame PASS (mean 3.61, run 0) | "weave in, weave out" compressed to a single "weave" mouth; "in, weave out" 42.56–43.14 dropped as distinct mouths; caption carries full phrase. "at" matches sheet ("match at all") |
| C1-hook1 | 50.84–53.48 | hook v6gap2 t1 warped (0–3.30 scaled, f=1.25) | meas 0.795 / scaled 0.80 | lyric PASS, frame PASS, character PASS, text PASS (volley 15) | Mouth's "dumb" tail extends into "baby." 53.22–53.48 — baby is a micro-gap (caption carries) |
| C1-hook2 | 54.22–56.46 | S05 t6 warped (0–2.80 scaled, f=1.25) | meas 0.794 / scaled 0.80 | lyric PASS (4/4), frame PASS warped (mean 0.61, run 12), character PASS, text PASS (volley 17 §4) | Within-scene assignment: S05's take covers the second hook of its own scene's line (was a 0.54x miss against the 1.92s opener span; grey → warp-rescuable against this 2.24s span) |
| S06a | 57.92–63.60 | S06a t2 (0–6.36, f=1.120) | 1.120 | PASS | None |
| S06b | 65.02–70.62 | S06b t1 (0–5.76, f=1.029) | 1.029 | PASS | Second "to" 67.48–68.04 dropped (minor class) |
| S07 | 72.28–80.78 | S07 v6final t1 (0–8.18, f=0.962) | 1.039 | lyric PASS (10/10), frame PASS (mean 0.54, run 13), character INCONSISTENT (see note †), text PASS (volley 17) | "toll" early-hold drift nit (fit-mapped −32.7f on that word; rest within ~0.2s). PERFORMED-LINE EAR DEPENDENCY (§4). Restage (volley 18) REJECTED: frame FAIL (0.496), photorealistic + text FAIL. † Character: see note † below. |
| S07-hook2 | 82.28–84.64 | S07 t2 tail fragment (6.06–8.32, f=0.958) | 1.044 | lyric PASS ("toll roads are dumb", done→dumb class), frame PASS (mean 0.72, run 1) | Sub-fragment anchor from the scene's own take; gates pass on its own timing. The take's main line (sheet version) is NOT used. "baby." 81.20–81.42 between S07 and the anchor is a micro-gap |
| S08 | 88.48–93.10 | S08 t9 (0–4.88, f=1.056) | 1.056 | PASS | Sings ONLY "they just keep coming" (words 137–140); preceding words 85.88–88.48 are filler + caption (§2) |
| S09 | 93.10–96.42 | S09 t2 warped (0–4.18, f=1.259) | meas 0.794 / scaled 0.800 | PASS (parent-overruled warp-rescue; viewing-cut factor retained) | "but the" 95.12–95.48 dropped; "hot" vs song-transcription "high" — take sings sheet word "hot" (unresolved token; sheet supports the take) |
| S10 | 96.80–99.98 | S10 t6 (0–3.54, f=1.113) | 1.113 | PASS | None |
| S11a | 103.72–107.74 | S11 t3 warped (0–5.0247 scaled, f=1.2500) | meas 0.795 / scaled 0.800 | lyric PASS (11 words), frame PASS (full vocal mean 0.72, run 17), character PASS, text PASS (warped 5s frame) | "still the" 105.86–106.56 dropped |
| S12a | 111.30–114.78 | S12 t3 (0–3.585, f=1.031) | — | lyric PASS, frame PASS (mean 10.2, run 0) | "while the" 112.68–113.10 dropped; "ones" 113.34–113.62 dropped; "rich ones disappear" 113.10–114.34 unmouthed (take's late "rich disappear" excluded to avoid wrong-words overlap) |
| S12b | 118.18–120.22 | S12 t3 (7.36–9.46, f=1.031) | — | lyric PASS, frame PASS (mean 0.60, run 8) | "still" 118.40–118.76 dropped; "the" 119.26–119.74 dropped |
| C2-hook2 | 125.16–128.12 | S13 t3 (0–3.64, f=1.230) | 0.813 | lyric PASS (hook exactly once, tall→toll class), frame PASS (mean 0.97, run 11), character PASS, text PASS (volley 17 §4) | Within-scene assignment: S13's take covers the second hook of its own scene's line (was a 0.42x miss against the 1.52s first-hook span; in band against this 2.96s span) |
| S14 | 128.76–135.22 | S14 t1 (0–7.40, f=1.145) | 1.145 | lyric PASS, frame PASS (mean 4.74, run 1) | "files"=fast, "rex"=wrecks mishear classes (sequence PASS with classes). Uses t1, NOT warped t2 (viewing-cut FIX1: warped t2 held a visually confirmed ~0.9s still at vocal start) |
| R1 | 136.26–142.62 | R1 t3 (0–5.84, f=0.918) | 0.918 | PASS | Second "to" 139.20–140.22 dropped (minor class) |
| R2 | 144.08–149.36 | R2 t1 (0–4.38, f=0.829) | 0.829 | PASS | Performed line. None |
| R3 | 150.48–152.64 | R3 t4 warped (0–2.70, f=1.25) | 1.25 | PASS | None |
| R4 | 153.74–156.16 | R4 t2 warped (0–2.52, f=1.041) | 1.041 | PASS | None |
| R5 | 157.34–160.20 | R5 t3 (0–3.24, f=1.133) | 1.133 | PASS | Sings words 262–265 only ("fast lanes make crashes"); the caption line continues into S15's span |
| S15 | 160.20–164.36 | S15 t2 warped (0–3.328 scaled, f=0.80) | scaled 0.80 | PASS (parent-confirmed scaled) | Sings the line's tail ("they just keep coming") |
| S16 | 165.92–168.94 | S16 t7 warped (0–3.76, f=1.245) | 1.245 | PASS | None |
| S17 | 169.62–175.22 | S17 t2 warped (0–7.0, f=1.25) | 1.25 | PASS (all 10 beat words; unwarped drops resolved by warp) | None |
| S18 | 175.22–182.48 | S18 t1 warped (3.84–9.66, f=0.802) | 0.802 | PASS (13-word segment: bridge line + hook words 303–306) | "oh" interjection + "timings"/"down" tokens disclosed as nits (per warp record) |
| S19 | 186.56–193.18 | S19 t2 warped (0–5.40, f=0.816) | 0.816 | PASS | "the" before "wrecks" dropped (take sings "fast lanes make crashes wrecks just come") |
| S20 | 194.80–196.58 | S20 t2 warped (4.414–6.639 scaled, f=1.25) | scaled 1.25 | PASS (parent-confirmed scaled) | Measured onset snap disclosed (scaled window governs) |
| R6 | 198.00–200.18 | R6 t4 warped (1.355–4.08 scaled, f=1.25) | scaled 1.25 | PASS (parent-confirmed scaled) | "toll" included via the scaled window (viewing-cut trim had cut it) |
| GAP-C | 201.10–204.24 | GAP-C v6gap t1 warped (0–3.92, f=1.248) | 0.80 | lyric PASS, frame PASS (volley 14) | PROVISIONAL — "first"=fast mishear class unconfirmed until the user's ear confirms it. Onset-trim at evidenced 0.85s pre-warp (GAP-C precedent) |
| S21 | 205.20–214.44 | S21 v6final t1 (0–8.14, f=0.881) | 1.135 | lyric PASS (13/14), frame PASS (mean 0.71, run 5), character INCONSISTENT (see note †), text PASS (volley 17) | Dropped "to" 211.18–212.60 (minor class). See §4 for the phantom-token note. Restage (volley 18) REJECTED: photorealistic + text FAIL (lyric 13/14 same drop class, frame PASS). † Character: see note † below. |
| R8 | 216.06–221.82 | R8 t1 (0–6.0, f=1.042) | 1.042 | PASS | Performed line. None |
| S22 | 222.44–224.64 | S22 t4 warped (3.27–5.03 scaled, f=0.80) | scaled 0.80 | PASS (parent-confirmed scaled) | None |
| GAP-D | 224.92–230.22 | GAP-D v6gap t1 warped (0–6.625 scaled, f=1.25) | meas 0.79 / scaled 0.80 | lyric PASS, frame PASS (volley 14, parent-confirmed) | Last word "come" trimmed ~2 frames early by the scaled window |
| S23 | 230.22–231.82 | S23 t4 warped (0–1.94, f=1.2125) | 1.2125 | PASS | Sings "toll roads are dumb"; the line's "baby." 232.14–232.64 falls in the following filler (caption line spans both) |
| GAP-E | 236.62–238.82 | GAP-E v6gap2 t1 warped (0–2.75 scaled, f=1.25) | meas 0.786 / scaled 0.80 | lyric PASS, frame PASS (volley 15, parent-confirmed) | Last word trimmed ~1 frame early by the scaled window |
| R11 | 242.30–243.08 | R11 t4 (0–0.72, f=0.923) | 0.923 | PASS | Word: "yeah". None |
| S24 | 243.24–249.18 | S24 t1 (0–6.30, f=1.061) | 1.061 | lyric PASS, frame PASS (mean 2.86, run 1) | None |
| S25 | 251.08–253.06 | S25 t2 (0–2.20, f=1.111) | 1.111 | lyric PASS, frame PASS (mean 0.95, run 1) | Leading "the" nit (take sings "the" before "toll"; mouth forms "the" briefly during song "toll") |
| S26 | 257.82–260.80 | S26 t2 (0–2.70, f=0.906) | 0.906 | lyric PASS, frame PASS (mean 0.84, run 3) | Leading "the" nit (same class) |
| S27-tail | 260.80–268.01 | S27 t2 post-vocal (2.96–10.0, f=0.977) | — | TAIL (no words; ticket-tear motif) | None |

## 2. Cover / filler slots — NOT mouth-sung slots

Each cover interval passed a motion pre-check (mean diff ≥0.5, no
near-dup run ≥24f) before assembly; the master motion audit (§5) is the
final check. Captions carry every word on song time in all of these.

| Slot | Song span | Picture | Why not mouth-sung |
|---|---|---|---|
| S02-accent | 22.10–22.68 (0.58s) | Single visual accent: S26 t2 turn 2.70–3.28 (motion mean 3.65, run 1) | STRUCTURAL (task §S02): sub-second fragment; volley-15 take 0.207x + frame FAIL. Both words highlight in sequence inside the line block. Disclosed micro-gap (mouth-covered, not mouth-sung) |
| S08-gap | 85.88–88.48 | Filler (S26 t2 tail + S09 warped tail) + caption "Fast lanes make crashes" | S08 t9 sings only "they just keep coming"; no take mouths these 4 words. Micro-gap |
| GAP-B | 100.26–103.60 | 3 shots, face/detail/face: S10 t6 3.54–4.88 (mean 2.01, run 0) / S26 t2 3.28–4.48 (mean 4.19, run 0) / S10 t6 4.88–5.68 (mean 4.77, run 0). Anchor back to the performer's face between covers; caption carries "safer" on song time | STRUCTURAL: no take sings "safer" at pace (volley-14 take 0.40x, volley-15 take 0.438x; warp would need 1.82x, over cap). Two compression failures closed the generation route |
| S11-cover | 107.74–111.08 | 3 shots, face/detail/face: S10 t6 5.68–6.84 (mean 2.03, run 0) / S26 t2 4.48–5.58 (mean 3.72, run 0) / S10 t6 6.84–7.92 (mean 1.54, run 0). Caption carries lexus + money words | STRUCTURAL (pace-floor): lexus 0.439x, money phrases ~0.50–0.55x; no sub-phrase fits within band (verified from volley-16 take timings: "lexus lanes" 0.46x, "they call them" 0.48x; ×1.5 still <0.80). Volley-16 take NOT used as singing coverage |
| S12-cover | 114.78–118.18 | 2 shots on the line's internal word boundary: shot 1 face S10 t6 7.92–9.40 (114.78–116.26, mean 1.37, run 7) covering "stop and go plazas used to kill"; cut lands on the kill\|and boundary (116.26) as the visual accent on stressed "kill"; shot 2 reaction R11 t4 0.72–2.64 (116.26–118.18, mean 1.14, run 0) covering "and electronic helps a bit, but the" | STRUCTURAL: volley-15 take 0.258x + frame FAIL (25f run) — NOT used as a singing close-up. Fully covered per research adjudication |
| S12-tail | 120.22–121.76 | Filler (S09 warped tail) + caption "that won't quit" | Take has no words here. Micro-gap |
| C2-hook1 | 122.92–124.44 | Single reaction shot: S19 t2 warped 5.40–6.92 (mean 2.68, run 2). Caption carries hook words | Hook-floor: S13 t3 0.42x against this 1.52s span; the take covers hook2 instead (see §1) |
| S18-tail | 182.48–186.56 | Filler (R4 warped tail + S15 warped tail) + caption (hook words 183.04–186.46) | S18 spill tail 1.78s vs 3.42s song = ratio 1.92, unusable as mouth. Micro-gap |
| All other holes | (see cutlist) | Moving non-vocal filler from the viewing-cut filler pool at f=1.0, consumed in order (excluded: S08 t9 tail and R6 t7 tail-end per viewing-cut FIX1 frozen cores) | Silence or micro-gap words (listed in §3); captions carry any words |

Frame-rounding micro-clips (documented, not errors): two 1-frame filler
clips fall in silence gaps — 34.50–34.56 (R3 t7 3.9–3.955) and
153.70–153.74 (R4 warped 2.52–2.557). They are 42ms shot fragments at pool
boundaries, not freezes; the motion audit (§5) confirms no run arises
from them.

## 3. Micro-gap master list (every remaining unmouthed word/span)

- "roads" 21.44–21.98 (S02a clip ends mid-word)
- "baby, make" 22.10–22.68 (S02 accent cover)
- "in, weave out" 42.56–43.14 (S04b single-"weave" compression)
- "baby." 53.22–53.48 (C1-hook1 mouth tail overlaps it)
- Second "to" 67.48–68.04 (S06b); second "to" 139.20–140.22 (R1);
  "to" 211.18–212.60 (S21) — all minor single-word drop class
- "baby." 81.20–81.42 (between S07 and hook2 anchor)
- "fast lanes make crashes" 85.88–88.48 (S08-gap filler + caption)
- GAP-B full line 100.26–103.60 (cover)
- "still the" 105.86–106.56 (S11a); lexus line 108.02–109.52 + money
  phrase 109.86–111.08 (S11-cover)
- "while the" 112.68–113.10; "ones" 113.34–113.62; "rich ones
  disappear" 113.10–114.34 (S12a span)
- S12 middle line 115.60–118.18 + "stop and go plazas" 114.78–115.60
  (S12-cover)
- "still" 118.40–118.76; "the" 119.26–119.74 (S12b span)
- "that won't quit" 120.22–121.76 (S12-tail filler + caption)
- C2-hook1 122.92–124.44 (cover); "baby." 124.92–125.16 (between hooks)
- "baby." 152.92–153.16 (between R3 and R4; filler + caption)
- "They" 165.34–165.92 (filler + caption); "but the" 169.06–169.62
  (filler + caption)
- S18-tail hook 183.04–186.46 (filler + caption)
- "the" before "wrecks" in S19 (take sings "fast lanes make crashes
  wrecks just come")
- "baby." 197.14–197.22 (filler + caption); "baby." 232.14–232.64
  (filler + caption, S23 line's tail)
- S25/S26 leading "the" (mouth forms "the" during song "toll" onset)
- Early trims: S02b "go" 2 frames early; GAP-D "come" ~2 frames early
  (scaled window); GAP-E last word ~1 frame early (scaled window)
- Substitutions/classes (mouth differs from song token, disclosed, not
  counted as gaps): S02b "roll"→"road"; S14 "files"=fast, "rex"=wrecks;
  S09 "hot" vs song-transcription "high"; S03 caption "brakes" vs
  song-transcription "bricks" (mouth + sheet agree; see §4)
- S07 "toll" early-hold drift nit (see §1)
- GAP-C PROVISIONAL ("first"=fast unconfirmed; see §1)
- Chorus-line ear check (see §4) — the one open ear check that can be
  re-cut without re-shooting (captions re-cut)

## 4. Captions

- Source: `SONG_WORDS_BASE.json` (404 measured words), grouped into 52
  caption lines by gaps >0.9s plus forced breaks at sheet line
  boundaries with small gaps (builder: `masters_work_v6/captions.py`).
  396 caption events (one per word; events tile contiguously, highlight
  3 frames early).
- Display cleanup (song tokens → caption text, punctuation preserved):
  toe/tall/told→toll, done→dumb (hook "dumb"), flaselines→"fast lanes",
  plasers→plazas, -old→old, watchin'→watching, weavein'→weaving,
  comin'→coming. Overrides where mouth + sheet agree against a
  song-Whisper token: "bricks,"→"brakes," (S03 line; the take clearly
  sings "brakes" and the sheet says "brakes") and "high."→"hot." (S09
  line; the take sings "hot" and the sheet says "hot"). Mid-line
  capitals lowercased ("The"→"the" mid-line); line-start capitals kept.
- PERFORMED chorus line: captions use "we've been slamming the danger
  roads" (the performed line, matching the S07/R2/R8 mouths), NOT the
  sheet's "Weaving and slamming, the danger grows". OPEN EAR CHECK
  (flagged once, not re-asked): if the user's ear hears "weaving"
  instead, the S07/R2/R8 takes themselves would need revisiting —
  captions alone cannot fix a mouth. The delivery note must carry this
  flag; the re-cut path (captions only) applies only if the ear agrees
  with the performed line.
- Phantom tokens EXCLUDED from captions (7): SONG_WORDS_BASE words
  333–339 ("the road gets meaner every single time.") all carry the
  identical zero-duration stamp 205.2–205.2 — a transcription echo of
  the S17 line, not words sung at 205.2. Evidence: zero duration is
  physically impossible for 7 sung words; the S21 take (prompted from
  the true line) sings exactly the real line words 340–353; the phrase
  is really sung once, at S17 (172.86–179.02). Excluding them does not
  change any take verdict.
- Folded token (1): word 371 "the" at 228.6–228.6 (inside GAP-D's line,
  between "crashes," and "wrecks") has a collapsed zero-duration stamp
  but IS sung (the GAP-D take sings "the", warped 5.24–5.62). It is
  folded into the following "wrecks" highlight (joint highlight "the
  wrecks" during the wrecks window) rather than dropped.
- Covered words are still captioned on song time — the caption is the
  lyric track, the picture is coverage. No on-screen gap disclaimer
  (disclosure belongs in the delivery note, never on screen).

## 5. Verification (final, on the delivered files themselves)

- Master `masters/mv2_toll_roads_are_dumb_v6_16x9.mp4`: md5
  `b2d386bf138aa5e3b654a8382b7b68c0`, 78,154,776 B, 1280×720/24fps
  h264 + AAC 48kHz stereo, 6432 frames (container + full-decode
  count), 268.010s, faststart OK (moov@36 < mdat@186691). Song
  untouched: `track.mp3` md5 still
  `9e5ff10876cda8ac17dcb22b79c3f00a`. Exactly 1 video + 1 audio
  stream.
- 9:16 reframe `masters/mv2_toll_roads_are_dumb_v6_9x16.mp4`: md5
  `758554e8f668271b72eadab37f1d59d6`, 84,116,707 B, 720×1280/24fps
  h264 + AAC 48kHz stereo, 6432 frames (full-decode count),
  268.010s, faststart OK. REBUILT from the silent video (not a crop
  of the captioned master): the first reframe (center-crop of the
  captioned master, md5 `e96c12f571fd7fd13cb2527b3019c6b6`) clipped
  long caption lines at the sides and cropped the `~ WuBu ~` bug out
  entirely. The rebuilt version uses `captions_9x16.ass` (PlayRes
  720×1280, same 396 events, lines wrapped) + bug; verified on 3
  sample frames (21.0, 101.5, 206.0): performer centered, captions
  fully visible with correct per-word highlight, bug top-right.
- Chat copy `masters/mv2_toll_roads_are_dumb_v6_16x9_chat.mp4`: md5
  `473a108745f7782559055d1114fea464`, 30,492,411 B, 1280×720/24fps
  h264 + AAC 48kHz stereo, 6432 frames, 268.010s, faststart OK.
- Frame-count fix (assembly verification catch): the first clip
  render summed to 6445 frames, not 6432 (23 clips off by ±1 from
  fps-filter rounding). All 23 re-rendered with exact frame caps
  (`-frames:v N` + tpad); silent video and all masters are exactly
  6432 frames. Record: `/tmp/v6_fixframes.py` (method), clip counts
  verified per clip.
- Motion audit on the delivered master itself (full-fps 160×90
  grayscale, consecutive-frame mean abs diff; viewing-cut master
  reference: mean diff 2.559, total frozen 0.625s, longest near-dup
  14f): frames 6432, mean diff 2.838, near-dup runs ≥6f: 12, frozen
  runs ≥6f: 1 (185.167s, 14f, 0.583s total frozen — BETTER than the
  viewing cut), longest near-dup 22f (72.333–73.250, S07 "We've"
  onset — the take's slow mouth-opening, under the 24f gate; the
  silent video's longest run in the same window is 19f, the
  caption overlay extends it to 22f, still passing). Runs >12f:
  only 72.333 (22f, S07 onset) and 184.958 (19f, S18-tail filler
  during captioned-but-unmouthed hook words — rest pose, not a
  freeze during mouthed words). Full record:
  `masters_work_v6/motion_audit_v6_final.json`. (Note: an earlier
  "52.8s frozen" figure counted ALL sub-0.2 transitions including
  isolated 1-frame dips; the viewing-cut-comparable figure is
  runs-only, 0.583s.)
- Mouth-state pass at every cut point: programmatic
  (`finish.py --cuts`) finds exactly 1 violation — the S02a→filler
  cut at 21.69, 0.25s into the disclosed unmouthed word "roads"
  (21.44–21.98): adjudicated as a normal between-shot cut during a
  covered word, not a mid-word pop (mouth open→rest across a scene
  change; "roads" is a disclosed micro-gap). All other 103 cuts land
  on word boundaries or in silence. Visual spot-check: all 10
  boundary pairs viewed (`masters_work_v6/cutcheck2/`, frame-exact
  indices from the cutlist; note the select-output order is
  ascending frame number, NOT pre/post pairs — pairs are
  (520,521), (543,544), (1283,1284), (1354,1355), (1938,1939),
  (2030,2031), (2585,2586), (2754,2755), (2789,2790), (2835,2836)).
  Cover/filler word checks: S10 t6 tail (cover-1) and S26 t2 tail
  (S07 filler) Whisper-verified NO WORDS in their used spans, so
  their open-mouth frames are held poses, not borrowed mouths.
  Cover-2 re-cut (R11 t4 0.76–2.68) for the yeah-tail frame — see §6.
- Lyric re-audit of the delivered master itself: segment mapping
  verified at plan (every (tau1−tau0)/factor matches its out-span
  within 0.02); caption timing verified at build (396 events tiling
  the song words, highlight 3 frames early) and on the delivered
  master at 3 spot frames — 21.0 (S02: mouth open, "the"
  highlighted), 101.5 (GAP-B cover: reaction shot, "safer"
  highlighted — caption carries the covered line on song time),
  206.0 (S21: mouth open, "wrecks" highlighted) — all with line
  block + yellow highlight + `~ WuBu ~` bug rendering correctly.
  Audio: exactly 1 AAC 48kHz stereo stream; generated clip audio
  discarded everywhere; song md5 unchanged.

## 6. QC rows for every covered slot

(See §1 for mouth slots and §2 for covers. Summary counts: mouth-sung
slots 50 (including S27-tail motif, excluding filler-only holes);
cover slots 8 designed covers (S02-accent, GAP-B ×3 shots, S11-cover
×3 shots, S12-cover ×2 shots, C2-hook1) + filler-with-words holes
(S08-gap, S12-tail, S18-tail) flagged "not a mouth-sung slot"; micro-gap
words per §3. Full per-take QC records: TAKE_WORDS_V6_VOLLEY*.json,
VOCAL_WINDOW_V6V*.json, WARP_RESCUE_V6.json, V6_SUPPLEMENTAL_QC.json,
V6_SUPPLEMENTAL_QC2.json, VOLLEY14/15/16/17_GAP_COVERAGE.md,
VOLLEY18_RESTAGE_COVERAGE.md, TAKE_WORDS_V6_RESTAGE.json.)

† CHARACTER NOTE — CORRECTION TO THE VOLLEY-17 RECORD: the volley-17
"character PASS" verdicts for S07, S21, and S04a are WRONG. Re-viewing
the QC frames on disk during assembly verification shows all three
takes share a DIFFERENT cartoon performer from the rest of the video
(darker skin, rounder face, gold chain, daytime open-road setting;
consistent across the three takes, different from the night-VOICE of
every other slot). The assembly uses these takes anyway — no passing
alternative exists (restages rejected, cap spent, old takes fail
lyric/facing) — so S04a (6.74s), S07 (8.50s), and S21 (9.24s), ~24.5s
total, show a different face than the rest of the video. Costume,
props, mic, ticket, and cartoon style match; the FACE does not. This
is v6's single largest known defect and must be flagged prominently
in the delivery note; the parent/user is the final judge.

Cover-2 fix (assembly verification catch): S12-cover-2 was first cut
from R11 t4 0.72–2.64, but the take's only word ("yeah") spans
0.00–0.72, so the cover's first frame was the last yeah-mouth frame.
Re-cut to R11 t4 0.76–2.68 (same 46 frames, same out-span 116.26–
118.18); Whisper on the full take confirms no words after 0.72, and
the new span motion-checks PASS (mean 1.19, run 1). S10 t6 tail
(cover-1) and S26 t2 tail (S07 filler) were Whisper-verified NO WORDS
in their used spans, so their open-mouth frames are held poses, not
borrowed mouths.

Restage rows (volley 18, all REJECTED, none assembled): S07 restage —
lyric 10/10, ratio 1.2248, frame FAIL (0.496), character FAIL
(photorealistic), text FAIL ("STOP" + ticket print); S21 restage —
lyric 13/14 (same dropped-"to" class), ratio 1.2126, frame PASS,
character FAIL (photorealistic), text FAIL; S04a restage — lyric
FAIL (18/22, tail missing), frame PASS (18-word portion), character
FAIL (photorealistic), text FAIL ("FAST LANE" + ticket print).
Restage prompts omitted "flat cartoon" (construction error, disclosed
in VOLLEY18_RESTAGE_COVERAGE.md).

## 7. What was NOT done (per task limits)

- No commit, no ledger edit, no announcement, no posting, no chat
  delivery — parent verifies, commits, delivers.
- No `V6_DELIVERED.flag` created.
- Volley 18 restages fired (3 videos: S07, S21, S04a character
  restages) — all REJECTED, none assembled. Task cap now 6/6 used, 0
  remaining; no further videos may be fired for this task. The four
  structural slots were never re-fired.
- No spend, no account connections, no repaint/audio-driven backend,
  no new tools or installs, no deletions.
- No `git add -A` (nothing staged).
