# MV-20 — AUDIO ANALYSIS (intake, 2026-11-14)

- Track: track.mp4 md5 cf4d54e21558a654d8a937d039322f84; track.mp3
  md5 d616cf2fa666c3658172039bb07b8437; duration 162.000s.
- Tempo MEASURED (c11_mir DP on 16k mono): **87.21 BPM** — median
  IBI 0.6880s, 235 DP beats (first 0.320s, last 161.504s); flux
  autocorrelation peak 0.688s (ac 0.612). A strong half-period
  subdivision peak sits at 0.352s (ac 0.571 → 170.45 BPM read) —
  the beat is 87.21 with a busy 8th-note surface; c11_mir's own
  tempo head read 86.5 BPM, consistent.
- Performed grid: large-v3-turbo full-clip ASR, NO VAD — 288 words,
  49 performed lines (grid_lines.json). Performed ≠ sheet where:
  C1 hook 2 (5.32–10.18) was dropped by the full-clip ASR and
  recovered by slice ASR; bridge sings "Still on the floor" ×1
  (not ×2); C4 sings "Living out the basket" ×1 (not ×2); outro
  sings "Still on the floor" ×1 (not ×2) + a wordless "yeah" at
  158.82. ASR mishears kept as timing only ("basketball" for
  basket, "all on the board" for the floor line, "wall"/"record"
  in the outro) — the sheet is the text authority, the grid is
  the timing authority.
- Accents: 689 flux peaks tiered S/A/B/C in ACCENT_MAP.json.
- Energy: outro tail (150–160s) is the loudest span (rel −0.70 dB
  mean at 150–160s); verses sit ~−4 dB; bridge dips before C4.
- Structure: C1 0.00 / V1 22.98 / PC1 34.16 / C2 43.90 / POST
  64.80 / V2 75.44 (ASR 75.0 "a week later" pickup) / PC2 86.56 /
  C3 95.72 / BR 117.26 / C4 126.66 / OUT 150.32; tail to 162.00.
