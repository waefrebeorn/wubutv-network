# PILOT-3 THE ROSTER — CUTLIST + ASSEMBLY RECIPE

## Status: ASSEMBLED + DELIVERED TO DISK 2026-11-15 (finisher)
U1_t2 fired verbatim from VEHICLES.md, gate-passed (see GATE_LOG),
and the recipe below was run as written. As-built deviations, both
disclosed in GATE_LOG: the master shipped as
masters/pilot3_the-roster_16x9.mp4 (brief/sibling naming, not the
draft name in step 3), and the master encode regenerated the
video timeline (setpts) + trimmed audio to the picture window to
land frame-exact after the concat's AAC priming offsets — a plain
`-t 60` encode clipped 4 tail frames and was discarded. Master:
1440f / 60.000s video, CRF 18 (SEI verified), md5
67c7fa105e13c3443b3f03c7892155a7. Chat copy = straight copy of
the master (≤50 MB), same md5.

## Cut (in order, each exactly 10.000s / 240f, hard cuts on motion)
| # | Take | Joint in | Joint out (name state) |
|---|---|---|---|
| U1 | takes/U1_t2.mp4 (PENDING) | frame 0 = PEAK: KEEPER circled, wet | UNC speaks "VASQUEZ." |
| U2 | takes/U2_t2.mp4 | VASQUEZ chalked on door board | speaker: "OKONKWO." |
| U3 | takes/U3_t2.mp4 | OKONKWO circled in monitor log | Keeper: "KEEPER." |
| U4 | takes/U4_t1.mp4 | KEEPER on the chair's shift tag | machine: "KEEPER." |
| U5 | takes/U5_t2.mp4 | second wet circle around KEEPER | Keeper: "HALE." |
| U6 | takes/U6_t2.mp4 | HALE on the page | ends held on WREN; UNC: "WREN." |

Total: 60.000s = 1440f at 24fps. No transitions, no fades — hard
cuts only; every take is already moving at both ends (motion law).

## Recipe (ONE assembly pass owns the joined file — MV-17 rule)
1. Conform each take to a segment (scale 1248×704 → 1280×720,
   setsar=1, fps 24, AAC 48k):
   `ffmpeg -i takes/U<n>_t<x>.mp4 -vf scale=1280:720,setsar=1 -r 24
   -c:v libx264 -crf 18 -c:a aac -ar 48000 work/seg<n>.mp4`
2. Concat demuxer → work/joined.mp4. PROBE IT: must read
   60.000s / 1440 frames before any master encode.
3. Master encode (single uninterrupted pass): joined + "~ WuBu ~"
   corner bug (network practice: drawtext, yellow-gold, bottom-right,
   small) → masters/PILOT-3_the-roster_master.mp4, libx264 CRF 18,
   +faststart. Verify the x264 SEI reads crf=18.0.
4. Re-probe the master end to end: 1280×720, 24fps, 1440f, AAC,
   faststart flag present.
5. Chat copy (≤50 MB, audio copied): bitrate-capped re-encode of
   the master → masters/PILOT-3_the-roster_chat.mp4. (At 60s the
   CRF-18 master will likely already be ≤50 MB; if so the chat copy
   is a straight copy — verify size either way.)
6. Touch PILOT_DELIVERED.flag at the project root; update
   PILOT_PROGRESS.md; commit text files (explicit paths only).

Native clip audio carries all dialogue — do NOT mute, do NOT add a
soundtrack, no TTS anywhere in this build.
