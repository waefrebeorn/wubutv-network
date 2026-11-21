# CUTLIST — PILOT-2 THE TENTH SECOND (assembly)

Master: 6 units × 240f = 1440f, 60.000s, 1280×720, 24fps.
Build: work/build_master.sh — segments normalised (scale 1280×720 lanczos,
fps 24, yuv420p, AAC 48k stereo), concatenated to work/joined.mp4 (probed
1440f BEFORE the master encode), single master encode with the ~ WuBu ~
bug drawn in the same pass. Exactly one assembly pass owns joined.mp4.

| out | source | treatment |
|---|---|---|
| 0.000–10.000 (U1) | take U1, full 240f | straight |
| 10.000–20.000 (U2) | take U2, full 240f | straight |
| 20.000–30.000 (U3) | take U3, full 240f | straight |
| 30.000–40.000 (U4) | take U4, full 240f | straight |
| 40.000–50.000 (U5) | take U5, frames 6–239 (0.25s head trim: studio-anchor replica) | setpts ×1.025641 + atempo 0.975 → 240f; head lands mid-offer, in motion |
| 50.000–60.000 (U6) | take U6, full 240f | straight |

Bug: "~ WuBu ~" DejaVuSans-Bold 26px, CADMIUM 0xFFCF3F, black border,
bottom-right (x=w-tw-22, y=h-th-18), full duration, applied at master
encode only (never in takes).
Master encode: libx264 preset medium CRF 18, audio copied from joined,
+faststart. Chat copy: CRF 26 / maxrate 5M from the master, audio copied.
