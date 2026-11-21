# CUTLIST V3 — SWING CUT — MV-2 "Toll Roads Are Dumb"

Status: RENDERED + VERIFIED 2026-11-02 ~04:20 EST. Delivered as chat attachment.
Supersedes v2 (denied 2026-11-02 for no sync edit). Do not re-deliver v2.

## Master
- `masters/mv2_toll_roads_are_dumb_v3_16x9.mp4`
- md5 `a847810701b4e0d309f30b4b4752cdd4`, 74,168,025 bytes, 268.041 s
- h264 1280x720 24 fps + AAC LC 48 kHz stereo + mov_text subtitles (48 cues)
- moov at byte 36 (+faststart) — fixed-audio form, same as the fixed v2 copy
- Audio = track.mp3 untouched as the mux source (take audio discarded throughout)

## Method (user order 2026-11-02: "swing the speeds and make the words match")
- faster-whisper base word timings: song 404 words, takes 219 words.
- Every take word warped onto its matched song word with unclamped setpts
  per word interval — the swing IS the aesthetic ("time sweeping").
- Scene start = max(its raw start, previous scene's last word end);
  scene end = next scene's start. Pre-vocal action trimmed, post-vocal tail
  swept into the gap — no scene's tail ever swallows the next scene
  (that flaw squeezed S16 to 0.56 s in the first, crashed run).
- Noise-merge before window derivation: an anchor whose onset interval
  implies >4x or <0.25x speed drops the middle anchor.
- S27 has no song anchors (its "toll roads are done" is S26's final line);
  it starts at S26's last word end 260.80 as the visual outro, full take
  swept uniformly to 268.01. S26's turn-to-silhouette tail is therefore cut
  to zero — disclosed trade.
- First swing run crashed on S27 (empty anchor list -> negative window ->
  `No such filter: ''`, concat=n=0). Fixed by the window model above;
  second run rendered S01-S27 clean. Full per-scene windows/speeds in
  `CUTLIST_V3_SWING.json`. Speed range overall: 0.2x-9.85x (S02 tail 9.85x
  is a swept gap, not a sung word).

## Verification (frame at every lyric line boundary, 48 samples)
- Samples: first detected sung word at/after each of the 48 lyric-line
  boundaries from LYRIC_TIMELINE.md (whisper onset + 0.35 s), taken from
  the finished master, not the takes. Sheets in `masters_work_v3/verify/`.
- Result: PASS with disclosed nits. Every boundary frame is the singer in
  the toll-plaza performance — no wrong scene, no action beat swallowing
  a line, no on-screen text in any of the 48 frames, `~ WuBu ~` bug
  visible in all 48, 48 subtitle cues, zero audio silences >= 2 s at -50 dB.
- Nits (staging in the takes, NOT timing errors — the words land exactly):
  - L11 (chorus 1 opens, 50.84-52.76 s): S05 sings "Toll roads are dumb"
    with his back to camera, raising the ticket at the striped sign; he
    turns face-forward for "baby" at 53.57 s. Mapping verified in
    WORD_MATCH_V3.json (take "Tall/roads/are/done" -> song words 91-94),
    so this is the take's staging, not a slip. A re-slip cannot fix it
    without breaking word-exactness; fixing it needs a take re-fire.
  - Single-frame closed mouths at word tails / between syllables
    (L01, L06, L08, L19, L23, L27, L29, L30, L38, L39, L45): cartoon
    mouths close between syllables; stills catch that. Not mis-sync.
  - L05 / L17: down-glance ticket beats on line-tail words. Take-internal.
  - L32 (bridge, "dollar and a dime"): coin close-up on the dime line —
    content-matched illustrative cut, not a mismatch.
  - L35: single profile frame. Take-internal.
- Honest limit (unchanged): word-level sync from whisper timings, NOT
  phoneme-accurate lip-sync. True phoneme classification (wav2vec2 + GPU)
  was not built; it needs a separate go-ahead.

## Scope note
- v3 was built 16:9 only. No 9:16 v3 exists yet; a 9:16 cut is a separate
  step if the user wants it (a blind center-crop of this master was NOT
  shipped, to avoid cutting the singer out of wide frames).

## Best cut (V4 rebuild) — 2026-11-02, SUPERSEDES the verification above

- Master: `masters/mv2_toll_roads_are_dumb_v3_16x9.mp4`,
  md5 `e5dcfe3a598b989b6d021e3e702a50b4`, 75,396,196 bytes, 268.01 s,
  h264 1280x720 24 fps + AAC 48 kHz stereo + mov_text, +faststart.
- Active takes changed from the first v3 render: S01 t4, S05 t4, S04 t4,
  S21 t2 (all other 23 unchanged). Windows in CUTLIST_V3_SWING.json are
  the rebuilt windows (S01 4.44–20.12, S04 40.76–49.38, S05 49.38–57.86,
  S21 201.34–222.44; all other windows identical to the pre-V4 cutlist
  except S03's end, which moved 43.14 → 40.76 with S04's new start, and
  S20's end, which moved 205.20 → 201.34 with S21's new start).
- The old headline nits are RESOLVED in this cut: S01 now opens on
  "Yeah" (t4, Yeah take 0.00–1.24 → song 4.44; leader hold is 4.44 s, not
  7.36 s); S05's chorus-1 opening is face-to-camera (t4), not
  back-turned; S04 sings the correct 43–48 s lyric (t4); S21 sings the
  verse opening (t2), not a stretched chorus echo.
- Re-verified with word-matched frames (`masters_work_v3/audit_v5/`):
  first-anchor sheets for all 26 anchored scenes, fastest-sweep strip
  (S16 13.33x, static coin-hold, harmless), verify sheet (S05→S06 cut
  ~0.1–0.2 s early, sub-5-frame rounding; S01 moving at 7.50; S27 outro
  tear 266.0 + final smile 267.5 present). No on-screen text in any
  audit frame; `~ WuBu ~` bug in all.
- Remaining disclosed nits: S02 profile opening, S03 neutral mouth at
  onset, S08 down-glance, S12 back-to-camera on its first word only,
  S04 garbled "weave" head and S21 burst head both unanchored at natural
  speed, S05 'are' dropped by noise-merge (interpolated +0.08 s),
  video stream 6 frames / 0.26 s shorter than audio at the tail
  (frame rounding; last frame held over the final audio decay), and the
  structural tail-hold limit — 27 scenes over 48 lyric lines, longest
  S14's 25.6 s static hold (see DEVILS_ADVOCATE_V4.md). Full record:
  DEVILS_ADVOCATE_V4.md.
