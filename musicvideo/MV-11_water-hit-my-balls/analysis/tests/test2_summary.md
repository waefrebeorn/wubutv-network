# MV-11 lyrics test #2 — Demucs separation + RMS-VAD + turbo (mix vs vocals)

Separator: Demucs htdemucs (audio-separator). MDX-Net path broken in this venv (torchvision 0.29.2 vs torch 2.15; see script header). Segments: 12 (RMS-VAD on separated vocals: thr 0.1 x p99, min silence 1.0s, max 30s, min 0.5s, pad 0.3s).
Transcriber: large-v3-turbo, fixed test-#1 config, NO VAD. Scoring: lyric-word coverage vs LYRIC_TIMELINE.md anchors (plural-tolerant); tie-break fewer non-lyric words, then mix.

| seg | span | mix words (cov / nonlyr) | vocals words (cov / nonlyr) | winner |
|---|---|---|---|---|
| 0 | 14.1–16.9 | 4 (1.0, 0) | 4 (1.0, 0) | mix |
| 1 | 17.7–24.8 | 9 (1.0, 0) | 9 (1.0, 0) | mix |
| 2 | 25.9–44.9 | 24 (0.677, 3) | 24 (0.677, 3) | mix |
| 3 | 45.4–52.5 | 8 (1.0, 0) | 7 (0.875, 0) | mix |
| 4 | 55.1–65.7 | 4 (0.25, 3) | 4 (0.5, 1) | vocals |
| 5 | 66.8–68.8 | 2 (0.0, 0) | 1 (0.0, 1) | mix |
| 6 | 69.3–82.1 | 4 (0.0, 4) | 3 (0.0, 2) | vocals |
| 7 | 81.5–107.0 | 24 (0.821, 0) | 37 (0.857, 5) | vocals |
| 8 | 109.3–110.4 | 4 (0.0, 3) | 1 (0.0, 1) | vocals |
| 9 | 111.2–140.8 | 23 (0.538, 9) | 30 (0.923, 8) | vocals |
| 10 | 141.5–162.3 | 13 (0.636, 2) | 9 (0.455, 4) | mix |
| 11 | 168.2–171.4 | 3 (0.0, 3) | 2 (0.0, 2) | vocals |

Totals (all segments): mix 122 words, vocals 131 words. Best-per-segment total: 137 words (mix wins 6 segs, vocals wins 6 segs).
102–172s span: test-#1 turbo full-clip = 33 words; test #2 mix-segments = 43; vocals-segments = 42; best-per-segment = 46.

## Verdict
Drop 102–122s: mix-segments 9 words, vocals-segments 2 words (test-#1 turbo full-clip had 6 here).
Outro 155–172s: mix-segments 5 words, vocals-segments 2 words (test-#1 turbo full-clip had 1 here).

## Verdict — separation is a TARGETED tool, not a blanket win

**Where vocals win (real):**
- Seg 9 (Final Hook part 1, 111.2–140.8): vocals 0.923 coverage (12/13) vs mix 0.538 (7/13). The mix falls into the "Water Water Water hits my bones / Bones Bones Bones" repetition loop; separated vocals break the loop and recover two clean "Water hits my balls" + the Balls chant. This is the one place separation earns its keep.
- Seg 7 (81.5–107.0): vocals 0.857 vs mix 0.821 — vocals recovers three clean "Water hits my balls" occurrences where the mix smears them.
- Seg 4 (Pre-Hook): vocals gets the real "my balls" (56.5–57.1); mix hallucinates "But it's my fault".

**Where it loses or washes out:**
- Seg 10 (Final Hook part 2, 141.5–162.3): MIX wins 0.636 vs 0.455. Vocals garbles ("Why hits my balls? / Poo-pit / Strasher") and stops early; the mix is clean. Separation is inconsistent across the two Final Hook spans — same track, same method, opposite result.
- Seg 6 (Hook 2 opening, 69.3–82.1): BOTH score 0.0. Mix hallucinates "Why don't you fall?", vocals "Why / For / Splash". The dense-brass Hook 2 opening defeats both. The vocals "win" here is a tie-break only, not a recovery.
- Drop (seg 8, 109.3–110.4): BOTH fail. Mix hallucinates "We'll be right back." (a classic Whisper stock phrase), vocals "Wow". Worse: the real "Water" onset (110.70) falls in the GAP between seg 8 (ends 110.43) and seg 9 (starts 111.16) — the RMS-VAD boundary ate the word. Full-clip turbo got "Water" 110.7. Segmentation LOST the Drop.
- Outro (seg 11, 168.2–171.4): BOTH fail. Mix "Oh, it's awesome.", vocals "HOLD MAUSING". Full-clip turbo got "Balls" 170.9. Segmentation LOST the outro too — the 3.3s isolated clip has no context for the buried final word.

**Segmentation quality notes:**
- RMS-VAD merged across the wordless gaps: seg 2 spans the 38.94–45.18 brass gap, seg 4 spans into the 13s instrumental gap (57.56–70.66). Demucs vocals carry brass bleed that keeps RMS above the 0.1 x p99 threshold, so boundaries are coarser than the true vocal spans. 12 segments, longest 29.7s.
- Seg 5 (66.8–68.8, inside the wordless gap) exists at all — bleed again. Both sources hallucinate a word or two there.

**Numbers, honestly read:** best-per-segment 137 words vs test-#1 turbo full-clip 132 (+5 overall); 102–172s 46 vs 33 (+13). The dead-zone gain is real but concentrated in seg 9; the Drop and outro words that full-clip turbo found are NOT in the segmented output. Count alone overstates the win — coverage is the honest metric.

## Recommendation — HYBRID pipeline for future tracks

1. **Backbone = full-clip large-v3-turbo, fixed config, NO VAD** (test #1 winner). It alone recovers the Drop "Water" (110.7) and the outro "Balls" (170.9), and it is one pass (250s) vs separation (14.5 min) + 24 segment transcriptions (~10.5 min).
2. **Add per-segment vocals transcription ONLY for long dense spans where the mix loops** (here: Final Hook 111–141s). Merge by per-segment lyric coverage, not by word count.
3. **Fix the segmentation edge-loss before relying on it:** widen the pad (0.3s -> 1.0s) and/or lower the RMS threshold so boundary words don't fall between segments; verify no expected anchor sits in a segment gap.
4. **Do NOT use separated vocals as the default source.** It wins 6/12 segments and loses or ties the rest, including one span where it is clearly worse (seg 10).
5. **Venv fix owed:** MDX-Net is unusable until the torch/torchvision mismatch is resolved (torch 2.15.0+cpu vs torchvision 0.29.2; CPU index has no torchvision 0.30.0). Either pin torch to 2.9.x to match torchvision 0.29.2, or wait for 0.30.0. Demucs htdemucs works and is the MSS-ALT paper's own separator, so this is not blocking.

**Costs (this box, 1.5 CPUs):** Demucs htdemucs separation 14m33s for 172s of audio (~5x realtime); 12 segments x 2 sources with turbo ~10.5 min. Total test #2 wall ~25 min vs test #1 turbo full-clip 250s.
