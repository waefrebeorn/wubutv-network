# O-A SPLIT — coordinator notes (2026-11-08 ~18:51 EST)
- User decision: SPLIT THE APEX SCENE.
- Vehicle written: work/rebuild/vehicles/mv8_v2_oa_split_apex_vehicle.txt
- Split: approach = take 3 climb (0s to just before ~6.5s crest, warped ~1.54x)
  covering 146.00–156.00 (240f); apex window = this take trimmed so its crest
  lands 3.435s into 156.00–163.00 (frame 3826). Trim-in = crest − 3.435s.
- New axis: APEX-WINDOW / MID-CLIMB START — rider already high at frame 0,
  ring already ahead. Single-anchor F11 only, no F02.
- Status: firing apex take now (1 of ≤6 this run).
- LANDED + QC DONE: takes/O-A_v2_split_apex.mp4, md5 176da2ac05bb4a5af24ae804badb62d0, 10.000s 1248x704 24fps h264+AAC. Transcription empty; RMS max 0.147 (music bed). Motion min 23.4/mean 41.0. Crest BY EYE at 5.50s (take frame 132; 130 ascending, 134 descending).
- VERDICT: KEEP, ledgered. Assembly math verified on 408f proxy (md5 5bc2ccd2020ca546753d33a36550e4c2): approach take-3 frames 0–143 warped 1.667x to 240f (146.00–156.00); apex take frames 50–217 = 168f (156.00–163.00); crest at segment frame 322 = song frame 3826, offset 0f (±2f eye).
- CAVEAT: frame-diff-peak test as written does NOT show a local peak at 3826 (full-frame diffs rise monotonically 8.6→26, seg 285–365; peak seg 364, +42f). Dive accelerates after the crest — diff peak is structurally downstream of any loop crest. No re-cut: no trim fixes it without moving the real apex off 3826. Parent ruling needed at assembly.
- 17/17 scenes KEEP. O-A closed at take level. No commit, no delivered flag (parent's call).
