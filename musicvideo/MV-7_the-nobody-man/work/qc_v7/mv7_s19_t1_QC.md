# MV-7 S19 t1 — QC (v2 verbatim, Era B bridge montage, recovery volley 5, 2026-11-06 ~18:10 EST)

File: takes/media-generation-mv7v2-s19-bridge-montage-b5-b6-0-65c522dd-c352-4d26-bf5e-16784d68469f.mp4
md5: 15aade7b9bb5933b1b0190e974ff96f3 · 4,291,185 B
ffprobe: h264 1248x704, 24fps, 10.000s; aac audio. Duration asked 10s → returned 10.000s EXACT.
Vehicle: redesign_v2/vehicles/mv7v2_s19_vehicle.txt verbatim (OVERHEAD DESK montage, no singing window;
shot ends settled on his face) + refs/nobody_man_v2_eraB.webp (md5 12c2ea7d3d97477f942c1b6e0e499364).
snapshot_id: 1b355be3-d10f-4cf2-acbd-b0694ec2878f:2o7tzz

## Audio / words (faster-whisper small, work/qc_v7/mv7_s19_t1_words.json)
- 1 token: "I" 4.70–6.10s, p=0.004 — adjudicated HALLUCINATION, not a sung word: probability 0.004
  (effectively zero), RMS in that window ~0.005 (near-silent), and the visuals show the overhead→face
  cut with no mouth moving. Per the split-half/hallucination adjudication rule, a near-zero-probability
  token on silent audio is not a line. Effective word count: 0 — as vehicled, no singing window.
- RMS bins 0.0015–0.0196 throughout — essentially silent bed. No vocal energy anywhere in the clip.

## Frame rule (native 24fps, whole clip 0.0–10.0s — montage plate, no vocal window)
- frames=240, mean_diff=4.650, min=0.202, longest near-dup run (<0.5) = 2 frames. Whole-clip mean_diff 4.650.
- PASS (FAIL would be run ≥24f or mean <0.5).

## Visual reads (2fps sheet, work/qc_v7/mv7_s19_t1_sheet.png)
- Montage beats all land: OVERHEAD DESK — paper rings around the keyboard like tree rings, cables
  rooted at the edges, the candle flame carried in and set down steady (hand visible carrying the candle,
  ~1.5–3s). The shot then cuts to his face at the desk (~5s) and settles: face still and silent,
  eyes open then closing in a soft smile in the tail.
- Era B state CORRECT: half-burned candle carried and set down, paper rings, cables.
- No readable text anywhere (paper-ring slips are blank). No other people. No morphing.
- Flag: the overhead→face transition is a hard cut mid-clip rather than a smooth settle — acceptable
  for beat-matched bridge montage (cuts land on the beat); assembly notes it.
- His face in the settle is still and SILENT as vehicled — no mouth movement, no sung line.

## Gates
- G1 character consistency: PASS (identity holds in the settle; overhead hands match Era B continuity).
- G2 zero unwanted on-screen text: PASS.
- G3 no licensed material: PASS.
- G4 performance window: N/A — montage plate, no singing window (flagged "not a mouth-sung slot").
- G5 audio-sync placement: N/A — montage plate; cuts land on the beat at assembly.
- G6 banger check: PASS (bridge contrast holds — overhead desk is the video's one top-down shot).

## VERDICT: KEEP-WITH-FLAG
- Second bridge montage plate lands clean. Flag: "I" p=0.004 hallucination adjudicated no-line (RMS
  silent); overhead→face is a hard cut mid-clip (beat-matched montage, fine); face settles still/silent
  as vehicled. NOT a mouth-sung slot — caption still keyed to song word times (B.5–B.6, 132.58–141.44s).
