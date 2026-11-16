# CUTLIST — E2 SHOW-2 THE TENTH SECOND, "The Chalk Wall"

Master: masters/E2_SHOW-2_the-tenth-second_MASTER.mp4
md5 137465e24d1248fe350ac8de5021e937 · 26,756,135 bytes ·
1280×720, 24fps, exactly 1440 frames (count-verified), 60.000s,
h264 CRF 18 (see GATE_LOG for the SEI anomaly + size proof),
AAC 48k stereo, faststart. Under 50 MB — no chat copy needed;
the house master is itself the delivery file.

Assembly (Method C §5.5 order): six segments conformed to
1280×720/24fps/yuv420p + AAC 48k stereo (each exactly 240f),
concatenated to work/joined.mp4 (probed: 1440f = segment sum),
Joint Gate run on the joined picture, then ONE master encode
compositing the graphic layer (work/gfx/frames, PIL Class P)
+ the `~ WuBu ~` bug + the loudness pass (fixed +10.13 dB gain
to a −20 dBFS median target, −1 dBFS limiter; measured master
median −19.1 dB).

| seg | source take | conform notes |
|---|---|---|
| 1 (U1) | U1_t2 | start-on-the-hit: 0.45s head trim, 1.04712× picture stretch, atempo 0.95496; the take's own frame-0 boot-scuff segment repositioned at +5 dB onto the new frame 0 (the BLAM fix menu's post sound accent, sourced from the take itself) |
| 2 (U2) | U2_t1 | straight conform |
| 3 (U3) | U3_t1 | straight conform |
| 4 (U4) | U4_t1 | straight conform |
| 5 (U5) | U5_t1 | straight conform |
| 6 (U6) | U6_t4 | straight conform — NO head trim: the scripted silence beat and the unit head are protected as delivered |

Graphics (one combined layer + bug): Cull Clock (ignition
frames 5–19 of U1; empties one segment per 8 frames; snaps full
with a cadmium ghost on every joint frame), Chalk Tally (serial
count 7→12 across the episode, one draw-on per unit, furniture
corner under the clock — placement ruling in GFX_CARDS.md),
the Stamp (one firing, U6 local frame 185 = the handover frame,
"CULL 423 / TO THE COURIER", bottom-left corner), bug
`~ WuBu ~` DejaVuSans-Bold 26px CADMIUM, bottom-right, full
duration.
