# MV-11 generalisation leg — resume notes

**Purpose:** Bar A stem-to-stem on MV-11 — c11 boundaries within ±0.5 s of
the Demucs stem boundaries (no HPSS ref needed for MV-11).

**Inputs (on disk):**
- Mix: `mv11_mix_44k.wav` — extracted from
  `MV-11_water-hit-my-balls/track.mp4` (ffmpeg, 44.1 kHz stereo);
  7,603,545 samples = 172.416 s, exactly the Demucs stem's length.
- Demucs reference stem:
  `MV-11_water-hit-my-balls/analysis/tests/separation/track_44k_vocals_htdemucs.wav`
  (172.416 s).

**Run (resilient dump mode — a reboot/reap loses at most the in-flight chunk):**
```
cd ~/workspace/wubutv-network/musicvideo/detection-research/c11_sep
./sep_main ../mdx_stemact/mv11/mv11_mix_44k.wav ../mdx_stemact/mv11/mv11_c11_vocals.wav \
  --prog-dir . --dump-dir ../mdx_stemact/mv11/chunk_dumps \
  > ../mdx_stemact/mv11/mv11_sep_run.log 2>&1
```
Chunks whose dump already exists are SKIPPED on re-run — just re-run the
same command to resume. ~39 chunks total (chunk 261120, step 195840).

**After the dumps complete, assemble + score:**
```
cd ~/workspace/wubutv-network/musicvideo/detection-research/c11_sep
python3 assemble_chunks.py --dump-dir ../mdx_stemact/mv11/chunk_dumps \
  --out ../mdx_stemact/mv11/mv11_c11_vocals.wav   # check exact flags in assemble_chunks.py first
cd ../mdx_stemact
python3 stem_activity_curve.py --vocals mv11/mv11_c11_vocals.wav \
  --out stem_activity_c11_mv11.npz --segments-out stem_activity_c11_mv11_segments.json
python3 stem_activity_curve.py --vocals \
  ../../MV-11_water-hit-my-balls/analysis/tests/separation/track_44k_vocals_htdemucs.wav \
  --out stem_activity_demucs_mv11.npz --segments-out stem_activity_demucs_mv11_segments.json
```
Then score Bar A stem-to-stem: RMS-VAD segments from the c11 stem vs the
Demucs stem's segments, span-start metric (same `match_boundaries` as
`validate_stemact.py`), bar max |dStart| ≤ 0.5 s. Record the result in
`mdx_stemact_validation.json` (add an `mv11_leg` key) and in
`SPRINT_2026-11-12_MDX_STEMACT.md` §MV-11 (replace the placeholder).

**Progress:** launched 2026-11-12 ~15:23 UTC; run 1 SIGTERM'd by a VM
reboot at 26/40 chunks (chunk 25/40 at 1184.3 s); resumed same command
~15:46 UTC — 14 written + 26 skipped, 40/40 dumped (1005.0 s wall),
assembled via `assemble_chunks.py` → `mv11_c11_vocals.wav` (172.416 s,
same length as the Demucs stem). Scored by `mv11_score.py` →
`mv11_score.json`: **Bar A stem-to-stem FAILS** (max |dStart| 1.71 s,
corr 0.8466, 7/11 spans within bar, 2 outside, 2 unmatched). Curve
artifacts: `stem_activity_c11_mv11.npz`, `stem_activity_demucs_mv11.npz`
(+ segments JSONs) in `mdx_stemact/`.
