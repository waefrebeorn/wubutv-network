# PILOT-1 THE MACHINE — CUTLIST

Master: 1440f / 60.000s @24fps, 1280×720. One assembly pass owns work/joined.mp4.
Takes are 1248×704 @24fps, exactly 10.000s each — scaled to 1280×720 in the
segment encode. No trims: every unit ships its full 240f (the generator's
cliff frames land inside the final second by design; mouth-handoff joints are
cut ON the mouth, unit N's last frames = mouth opening, unit N+1's first
frames = same mouth mid-word).

| # | span (master) | frames | source take | joint out |
|---|---|---|---|---|
| U1 | 0.000–10.000s | 0–239 | takes/media-generation-u1-take1-0-e6260d46-cf2b-456d-b789-a63377c9114e.mp4 | cat mouth opening (close) |
| U2 | 10.000–20.000s | 240–479 | takes/media-generation-u2-take1-0-b0487f34-2267-47f6-a2e0-9cabfd77f3ed.mp4 | cat mouth open, profile ECU |
| U3 | 20.000–30.000s | 480–719 | takes/media-generation-u3-take1-0-bbdf8ef9-4534-4238-8d86-51733dd2cc9a.mp4 | cat mouth wide open, frontal ECU |
| U4 | 30.000–40.000s | 720–959 | takes/media-generation-u4-take1-0-c3002dfe-e5c7-4f97-8d7a-b005026325de.mp4 | woman's mouth opening |
| U5 | 40.000–50.000s | 960–1199 | takes/media-generation-u5-take1-0-e2eda8b7-287b-44cf-af26-58eef4f7dbcf.mp4 | giant mouth open on main monitor (see fix) |
| U6 | 50.000–60.000s | 1200–1439 | takes/media-generation-u6-take1-0-739f55bb-dbe4-4015-af69-1250b87a6891.mp4 | bridge cliff: monitor mouth + UNC's mouth open together (see fix) |

Assembly fixes (QC-driven, GATE_LOG has the evidence):
- U5: the take cuts to BLACK at ≈9.13s (mean-gray 46.4 @9.10s → 0.0 @9.15s).
  Ship take frames 0–218 (219f) time-stretched ×240/219 (setpts 1.09589,
  atempo 0.9125) to fill 240f; the unit now ends on the giant open mouth at
  take-8.5s instead of the black tail. Line lands ≈7.7s, inside the window.
- U6: the mouths-open-together beat plays at take ≈8.5s and closes by 9.25s.
  Ship take frames 0–209 (210f) stretched ×240/210 (setpts 1.142857, atempo
  0.875) so the episode's final frames hold the open-mouth bridge cliff in
  motion. Line lands ≈8.0s, inside the window.
- Segments are CRF 12 intermediates; the CRF 18 law applies to the master
  encode from work/joined.mp4 (concat stream-copy, probed at 1440f first).

Master encode: joined → scale 1280×720 (already applied per segment), x264
CRF 18 (SEI-verified), AAC 48k stereo, faststart, `~ WuBu ~` bug bottom-right
(drawtext, DejaVu Sans Bold, cadmium #FFC400, post overlay — network practice).
Chat copy: video bitrate-capped (≤2.7 Mbps), audio copied from house master.

## Finisher corrections to this cutlist (2026-11-15 — what actually shipped)
- **U2:** trimmed to take frames 0–234 (not "no trim") — a full-decode scan
  found a pure-black tail at take frames 235–239 that the 0.5/5.0/9.5s spot
  probes missed. Stretch ×240/235. See GATE_LOG finisher correction #2.
- **U6:** window widened to take frames 0–215 (not 210) — the 210f trim
  amputated the final word "anyway" (take 8.60–8.90s; window ended 8.75s).
  Stretch ×240/216, audio window 0–9.0s, atempo 0.900. See GATE_LOG #1.
- **Join method:** concat FILTER + CRF 12 re-encode (the stream-copy join
  skewed timestamps and broke -ss seeking; a demuxer+re-encode join
  duplicated frame 0 → 1441 decoded frames). Verified: joined decodes to
  exactly 1440 frames, zero black frames, zero exact duplicates. Master
  encoded from this joined file per the spec above.
