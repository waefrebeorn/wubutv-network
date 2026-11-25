# CUTLIST — PILOT-4 THE COUNT (assembly)

Single assembly pass owns work/joined.mp4. Every unit conformed to
1280×720 / 24 fps / exactly 240 frames before the join; total 1440 f /
60.000 s. Native take audio throughout (dialogue), no added soundtrack.

| unit | source span | conform | notes |
|---|---|---|---|
| U1 | 0.00–10.00 (240 f) | scale 1248×704 → 1280×720 | opens on the locked PEAK frame state |
| U2 | 0.00–10.00 (240 f) | scale 1248×704 → 1280×720 | |
| U3 | 0.00–10.00 (240 f) | none (native 720p) | |
| U4 | 0.00–10.00 (240 f) | crop 1152×768 → 1152×648 (y+60), scale → 1280×720 | take arrived 3:2 (sheet aspect leaked past the text steer) |
| U5 | 0.00–10.00 (240 f) | scale 1248×704 → 1280×720 | |
| U6 | 0.75–10.00 (222 f) | setpts ×1.0811 (0.925× speed), audio atempo 0.925 → 240 f | head-trim removes the ~0.75 s empty-hall establishing beat (banned opener); unit opens mid-walk, chalked 1005 door already in frame |

Master: work/joined.mp4 → masters/pilot4_the-count_16x9.mp4 — x264 CRF 18,
`~ WuBu ~` bug drawn bottom-right in gold (network practice), AAC 192k,
faststart. Chat copy: masters/pilot4_the-count_chat.mp4 — bitrate-capped
video, audio copied from the house master.
