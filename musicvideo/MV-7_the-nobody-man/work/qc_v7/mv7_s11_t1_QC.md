# MV-7 S11 t1 — QC (v2 verbatim, Era B first fire, recovery volley 3, 2026-11-06 ~17:27 EST)

File: takes/media-generation-mv7v2-s11-verse-2-v2-1-v2-3-so-0-862f031f-fd6d-4d6c-8837-ea591826b343.mp4
md5: b90cc69e5c58f73e6cc698586de57871 · 2,668,775 B
ffprobe: h264 1248x704, 24fps, 10.000s; aac audio. Duration asked 10s → returned 10.000s EXACT.
Vehicle: redesign_v2/vehicles/mv7v2_s11_vehicle.txt verbatim + refs/nobody_man_v2_eraB.webp (md5 12c2ea7d3d97477f942c1b6e0e499364).
snapshot_id: b6dd0a13-f636-427e-b5e3-8064b1843e11:s0hehj

## Audio / words (faster-whisper small, work/qc_v7/mv7_s11_t1_words.json)
- 23 tokens, 3 segments: "I got drafts in the drawer like coins," 0.00–2.88s · "half-mad thoughts and a stack of joins,"
  3.68–6.68s · "tiny wins in a low-lit room." 7.06–9.08s.
- 22/22 words exact — "half-mad" and "low-lit" arrive as hyphen-split token pairs, same as SONG_WORDS.json; "joins" heard
  correctly (not "joints"), "low-lit" correctly (not "lonely"). All three lines, once, in order.
- Take line span 0.00–9.08s vs song slot 75.84–82.94s (7.10s; word span 75.84–82.88 = 7.04s) → line ratio 7.10/9.08 = 0.782
  (word-span 0.775) — GREY (0.60–0.80).
- Phrase math for assembly: V2.1 take 0.00–2.88s vs song 2.54s → 1.13x; V2.2 take 3.68–6.68s (3.00s) vs song 2.08s → 1.44x;
  V2.3 take 7.06–9.08s (2.02s) vs song 2.30s → 0.88x. All inside warp-rescue; overall ~1.29x.
- RMS check: vocal throughout with a quiet inter-line gap 3.0–4.0s (bins ~0.006) and quiet tail 9.0–10.0s — trims cleanly.
- Repeat-defect scan: no word/line subsequence recurs after first delivery. PASS.
- Zero-word result? No — 23 tokens; split-half recheck not needed.

## Frame rule (native 24fps, vocal window 0.5–9.5s)
- frames=240, mean_diff=1.108, min=0.666, longest near-dup run (<0.5) = 0 frames. Whole-clip mean_diff 1.135.
- PASS with margin (FAIL would be run ≥24f or mean <0.5).

## Visual reads (2fps sheet, work/qc_v7/mv7_s11_t1_sheet.png)
- Era B state CORRECT: candle HALF-BURNED (shorter than Era A's tall candle), cork strip crowded with receipts, stacks of paper
  on the desk, glowing-screens wall behind him. Draft drawer reads as the paper stacks / desk clutter.
- 0.5s: mouth open mid-"I got"; identity holds vs Era B still (thinning hair, stubble, frayed patches, charcoal crewneck).
- 4.5s: mouth open mid-"thoughts"; framing is a WIDER desk-lean shot than the Era A MCU takes — continuity note for assembly.
- 8.0s: mouth open at "room" (8.44–9.08); eyes half-closed, singing expression.
- 9.5s: held crooked grin after the last word.
- No readable text anywhere (receipts and screens illegible/abstract glow). No other people. No morphing.

## Gates
- G1 character consistency: PASS (identity holds; Era B state correct). G2 zero unwanted on-screen text: PASS.
- G3 no licensed material: PASS.
- G4 performance window: PASS (mouth visibly moving/open at 0.5s, 4.5s, 8.0s reads; single singer facing camera).
- G5 audio-sync placement: PASS-WITH-FLAG (all 22 words, once, in order; ratio 0.775–0.782 grey — warp-rescue ~1.29x, disclose).
- G6 banger check: PASS (Verse 2 opening: the room now holds receipts + scattered screens; desk-lean composition).

## VERDICT: KEEP-WITH-FLAG
- Flags: (1) RATIO 0.775 grey — assembly warp-rescue ~1.29x, disclose; V2.2 carries the squeeze (1.44x). (2) RASTER 1248x704
  (~16:9, 1.773) — neither the Era B still's 3:2 nor true 1280x720; assembly crops/pads to 1280x720. (3) WIDER framing than the
  Era A MCU takes — assembly continuity note (S11 is the first Era B scene; S12+ will share the wider desk-lean look).
  (4) Sings 0.00–9.08 vs vehicle window 0.5–9.5s (starts 0.5s early; last word ends 0.42s before window end).
- Era B is OPEN and proven on first fire. S11 is COVERED.
