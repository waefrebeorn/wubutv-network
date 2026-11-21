# GATE LOG — SHOW-1 'THE MACHINE' E2 "The Mouth That Moved First"

Build coordinator log. Every gate result and every flaw, stated plainly.
Script: SCRIPT.md (LOCKED). Stack: PANEL WORKFLOW SPEC v2 + JOINT GATE,
DYNAMIC_GRAPHICS G1–G8 (device: THE DEAD CHANNEL, cobalt), BLAM GATE (§4).

## Panels (all read back at full size before firing)

| Panel | Source | Verdict |
|---|---|---|
| WORLD / CHAR-UNC-hero / CHAR-UNC-face / CHAR-LAURA-hero / CHAR-LAURA-face / PROP-headphones | copied from pilot stack (md5s match pilot GATE_LOG) | PASS |
| PNL-CHAR-BOTH (new, combined two-character anchor — PILOT-4 lesson) | gen `fba31aa7…:7j8wgc` | PASS — both identities match canon, wordmark exact `~ WuBu ~`, LAURA headphones at neck, cat blue eyes |
| PNL-PEAK-U1 (the catch — BLAM impact frame) | gen `f479b38f…:gotwkg`, centre-cropped to 16:9 | PASS — UNC profile MID-WORD, single large monitor BLACK, LAURA frozen at edge, wordmark exact |
| PNL-PEAK-U4 (folder lands on desk) | gen `dfba95eb…:c91k0p` | PASS — folder event legible, UNC hands OFF it, wordmark exact, **cat eye BLUE** (pilot U3 eye-drift nit killed at panel stage) |

Joint plan: all 5 boundaries JOINT (one room, continuous scene; carry = the
mouth handoff straddling each cut). U1 anchor → U2 resume → U3 resume →
U4 RE-ANCHOR (J7 chain cap) → U5 resume → U6 resume.

## Takes

### U1 — the catch (BLAM unit)
- **take1** (`…f4a27b2b…`, resume snapshot `80d3e888…:1r88ff`): BLAM numbers
  excellent (median −28.2 dBFS, t50/t90 0.0/0.0, head −16.1 dBFS, motion ratio
  1.59×, first bucket 0.53 of max). ASR: dialogue EXACT (11/11 words).
  **REJECTED — WORDMARK HARD GATE**: chest wordmark at frame 0 renders
  "~ W'ulBu ~" (apostrophe + extra l) in a large, lit, near-central display.
  The generator recomposed UNC frontal despite the profile PEAK.
- **take2** (`…bdee0862…`): strict-profile staging. Wordmark not displayed.
  **REJECTED — BLAM**: median −38.9 dBFS (basement), head 0–1s ≈ 6.8 dB UNDER
  median (A3 fail), motion RAMPS from rest (first bucket 1.5 → 7.03 at 1.0–1.25s;
  ratio 0.21 — V2 fail). The pilot's exact disease.
- **take3** (`…c2f6e6b8…`, resume snapshot `42079a54…:0wvjae`): edge+shadow
  staging. **KEEP.** BLAM: median −33.0 dBFS, t50 0.0 / t90 0.0 (A1 PASS),
  lead silence 0.0 (A2 PASS), head 0–1s ≈ −31.8 vs median −33.0 (A3 PASS),
  HF bursts head 36 vs control 43 (A4 PASS at take level), motion head ratio
  2.03× baseline (V1 PASS), first bucket 4.95 = 0.96 of 0–3s max (V2 PASS).
  Frame 0: UNC profile mouth OPEN mid-word, LAURA present at left edge frozen,
  monitor black (E1 PASS — the catch). Wordmark at frame 0 reads exactly
  `~ WuBu ~` (small, dim gold, shadowed side). ASR: dialogue EXACT (11/11).
  Cat eyes blue throughout; tail: mouth closed at 9.5–9.7s (see flaw F-3).

### U1 — POST-ASSEMBLY WORDMARK DISCOVERY + REFIRE CHAIN (supersedes the take3 KEEP above)
The first assembled master (built on take3) failed graphics QC: a dense
wordmark sweep of take3 found the chest rendering "~ WulBu ~" (extra l)
through the push-in span ~2.5–4.5s — exact at frame 0 (small/dim), garbled
where large and lit. **take3 REJECTED — WORDMARK HARD GATE** (the law judges
what ships, at every second, not at frame 0). That master (md5
`3837c36a4f55226960e26c7be95b8fe7`, 19,713,913 B) was never delivered or
flagged; it was destroyed by overwrite in the rebuild. LESSON (standing):
wordmark QC samples the FULL span wherever the chest is visible, never
frame 0 alone.
- **take4** (`…a377f198…`): strict profile + sideways track (take2 recipe).
  Dialogue EXACT (11/11), wordmark never displayed. **REJECTED — BLAM**:
  t50 1.0s (A1 fail), head ≈9 dB under median (A3 fail), motion ramps
  1.34→5.62 (V2 fail). The profile staging reliably opens quiet and slow.
- **take5** (`…b1b89942…`): wide LOCKED-OFF two-shot. **REJECTED — BLAM**:
  t90 2.9s (A1 fail), head ≈6.8 dB under median (A3 fail); motion decays to
  near-zero after 2s (baseline 0.49) — a still wide.
- **take6** (`…7ae0f8f9…`, snapshot `b0be3474…:nept14`): take3's exact prompt
  re-rolled. **KEEP — all gates.** BLAM: median −35.0, t50 0.0 / t90 0.0,
  head 0–1s ≈ −29.8 (above median), first motion bucket 6.77 = 0.78 of max,
  head ratio 6.0×. ASR: dialogue EXACT (11/11), 2.24–7.82s. WORDMARK
  FULL-SPAN SWEEP (samples every 1s + enlarged crops): exact `~ WuBu ~` at
  1.0 (perspective-narrowed u, crop-adjudicated), 2.0, 3.0, 4.0, 5.0, 9.5s;
  not displayed at 0.0 (profile). The take3 drift window (2.5–4.5s) is
  CLEAN here. Tail cliff PRESENT (fixes F-3): the cat's mouth is open
  mid-sing at 9.5s. LAURA enters within the first second (absent only at
  frame 0 itself). New seam vs U2 take1's head: 37.0 (PASS band) — the
  existing U2/U3 chain survives the swap; no cascade refire needed.

### U4 — the refile demand (FULL-TALK, re-anchor unit)
- **take1** (`…1b939fab…`, resume snapshot `43b0d09c…:7p4v7l`): **KEEP.**
  ASR: ALL SIX fragments EXACT, in order (24/24 words), 0.00–9.38s.
  Wordmark exact `~ WuBu ~` at 0.0/5.0/8.0s (crop-verified). Cat eye BLUE in
  every sampled frame. Folder: presented open at 0.0s, face-to-face volley at
  5.0s, closed on the desk by 8.0s. Median −29.2 dBFS.

### U2 — the watch (resume from U1 take3)
- **take1** (`…8d186a12…`, snapshot `42079a54…:mdjd92`): **KEEP.**
  ASR: dialogue EXACT (11/11). Frame 0 is the build's best joint head: the
  cat's mouth is OPEN mid-sing — U1's deferred onset lands across the cut,
  exactly the joint design. Wordmark never displayed (UNC in dark profile /
  back throughout). Cat blue eyes. Flaw F-6 (tail) disclosed below.
- **take2** (`…ad4fd238…`): dialogue EXACT (11/11) and the monitor stays in
  frame, BUT **REJECTED — WORDMARK HARD GATE**: chest renders "~ WuEu ~"
  (B→E) large and lit at 5.0s and 9.5s.

### U3 — the turn (resume from U2 take1)
Four fragments; the generator repeatedly delivered only 3 of 4:
- take1 (`…a66be56f…`): "I only ever—" absent (lenient re-ASR of the gap
  hears only a sigh). REJECTED — dialogue.
- take2 (`…a6eaa214…`): "Your back is turned." absent. REJECTED — dialogue.
- take3 (`…473ecdce…`): fragment absent + a duplicated "Then turn round."
  variant. REJECTED — dialogue.
- take4 (`…971c109c…`): closing line absent again. REJECTED — dialogue.
- **take5** (`…46b36e3a…`, snapshot `42079a54…:8rk6hl`): **KEEP.**
  Stripped dialogue-block prompt (four lines as one conversation, beats
  compressed) — ASR: ALL FOUR fragments EXACT, in order (16/16).
  Picture: UNC back-turned with the monitor behind him, cat frontal with
  BLUE eyes, mouth parted at the tail. Nit F-7 (back wordmark cropped by
  the frame's lower edge at 0.0s; visible glyphs exact).

### U5 — the empty room (SPARSE; resume from U4 take1)
- **take1** (`…937bf2c2…`, snapshot `43b0d09c…:yx654w`): **KEEP.**
  ASR: dialogue EXACT (8/8) — "Out. It sings alone." at 0.0–1.9s, the long
  held silence the SPARSE unit wants, "It waits for me." at 7.1–8.1s.
  UNC exits through the doorway on camera; LAURA small beside the big
  screen; the cat's mouth stays CLOSED at every sampled frame (the failed
  handoff reads); empty chair in the foreground at the tail. Wordmark
  exact at 0.0s. Nit F-8 (corkboard handwriting).

### U6 — the wrong word + BRIDGE CLIFF (resume from U5 take1)
- **take1** (`…6257e9fd…`): ASR dialogue EXACT (16/16) BUT **REJECTED —
  CLIFF**: the camera pushes into a full-frame cat close-up (monitor
  framing lost), the cat's mouth stays closed at 9.5/9.9s, UNC out of
  frame — the bridge cliff (monitor opens on an unmouthed word, UNC's
  mouth shut) is absent, and the 2.5s silence beat is squeezed out
  (speech runs to 9.16s).
- **take2** (`…71a12e24…`): **KEEP.** ASR: dialogue EXACT (16/16), speech
  done by 8.40s. FINAL FRAME (9.9s): the cat's mouth is WIDE OPEN mid-sing
  on the monitor while UNC sits in profile, mouth SHUT, LAURA refereeing
  at frame left — the bridge cliff lands exactly as scripted (= E3's
  first frame). Wordmark exact `~ WuBu ~` at 0.0s. Cat eyes blue.
  Nits F-9/F-10/F-11 disclosed below.

## Flaws disclosed so far
- **F-1 (U1 take1, rejected):** wordmark garble "~ W'ulBu ~" — take does not ship.
- **F-2 (U1 take2, rejected):** BLAM fail (quiet head + motion ramp).
- **F-3 (U1 take3, KEEP with nit):** the U1 cliff beat — the monitor's mouth
  opening on the next sung word in the final second — is not visible at
  9.5–9.7s (mouth closed, cat watching). The handoff into U2 carries the
  opening instead (U2 is a resume of this exact moment). Weaker than take1's
  wide-open 9.5s mouth, traded for a passing wordmark + BLAM.
- **F-4 (U1 take1 only, moot):** monitor UI microtext incl. a "LAURA" label at
  9.5s — in the rejected take; take3's monitor shows no UI chrome.
- **F-5 (U2 take2, rejected):** wordmark garble "~ WuEu ~" — take does not ship.
- **F-6 (U2 take1, KEEP with nit):** the camera pushes into the face-to-face
  and the cat leaves the frame mid-unit; at the tail (9.5s) the monitor is a
  blank pale screen — U2's own cliff (UNC mouths, monitor follows) does not
  read inside the unit. The unit's scripted point (LAURA watches UNC, not
  the screen) is what the picture plays; the handoff resumes in U3.
- **F-7 (U3 take5, KEEP with nit):** frame 0 is UNC's back; the back wordmark
  is cropped by the frame's lower edge ("~ WuBu" visible, trailing tilde
  out of frame) — a partial at a frame edge, glyphs exact where visible.
- **F-8 (U5 take1, KEEP with nit):** corkboard at frame left carries
  handwritten in-world notes (illegible scribbles, one reads "LAURA") —
  set dressing, not a caption or overlay.
- **F-9 (U6 take2, KEEP with nit):** the scripted 2.5s silence beat lands
  compressed (~1.5s of tail: his stillness, the cat's first opening, then
  the cliff opening) because the generator spread the three lines to
  8.40s despite the front-load instruction. The beat reads, shorter than
  scripted.
- **F-10 (U6 takes 1+2, KEEP with nit):** UNC's face renders gaunter /
  older than the CHAR panels in the U6 resume chain (identity softness at
  the shadowed right edge); LAURA and the cat are exact.
- **F-11 (U5/U6 wide shots, KEEP with nit):** a small secondary editing
  display with UI/waveforms appears at the desk's right edge in the wide
  geography. The singer only ever appears on the one large monitor; the
  small display is set dressing. Also the take-file folder sits open on
  the desk again in U6 (closed at U4's tail) — a minor continuity wobble,
  contradicted by no line.
- **F-12 (U1 take3, REJECTED post-assembly):** mid-take wordmark drift
  "~ WulBu ~" through the push-in span ~2.5–4.5s, found by a dense sweep
  after the first master was built. take3 does not ship; F-3's nit died
  with it (take6's tail carries the open mouth). STANDING LESSON:
  wordmark QC samples the full span wherever the chest is visible —
  frame-0 checks are not sufficient.

## Assembly
### v1 (built on U1 take3 — REJECTED PRE-DELIVERY, never flagged/shipped)
Segments scaled to 1280×720 (CRF 12), joined with the concat FILTER (one
pass owning work/joined.mp4), probed 1440 frames. Joint Gate on the joined
picture: all five PASS (38.8 / 32.9 / 49.4 / 29.7 / 24.8). Loudnorm to
−16.29 LUFS. Master v1 (md5 `3837c36a4f55226960e26c7be95b8fe7`,
19,713,913 B) verified 1440f / 60.000s / SEI crf=18.0 / faststart and
BLAM-measured ALL PASS — then INVALIDATED by F-12 and destroyed by
overwrite in the v2 rebuild. Its one-graph DEAD CHANNEL strip also
rendered GREEN, dashed and faint (showwaves format/channel mangling
inside the composite graph) — fixed in v2.

### v2 (built on U1 take6 — THE SHIPPING MASTER)
- seg_u1 rebuilt from take6; ONE new assembly pass owns work/joined.mp4;
  probed 1440 frames before the master encode.
- **JOINT GATE (re-run on the rebuilt joined picture): ALL FIVE PASS** —
  U1→U2 37.0 (head motion 13.5) · U2→U3 32.9 (17.9) · U3→U4 49.4 (15.4) ·
  U4→U5 29.7 (9.4) · U5→U6 24.8 (20.7). Strips in work/qc/joints/.
- **STRIP FIX**: the strip was rendered as a STANDALONE video
  (work/strip.mp4) from the final audio — eye-verified TRUE COBALT
  (0x0047AB), dense in speech, near-flat across U5's hold and U6's beat
  (honest by construction) — and overlaid as a yuv video input at y=684
  in the master encode. Master band grabs confirm a legible filled
  cobalt waveform, live from frame 0.
- Loudness re-measured on the rebuilt joined (input −20.35 LUFS,
  TP −3.33, LRA 12.60) → work/audio_final.wav at −16.29 LUFS / TP −1.50.
- **MASTER: masters/SHOW1_E2_MASTER.mp4 — md5
  `bce7ea141f9828d5b5c9fc066f8e5098`, 20,954,083 bytes** (under 50 MB —
  no chat copy needed). Verified end to end: 1440 frames, 1280×720,
  24 fps, duration exactly 60.000s, h264 + AAC 48 kHz stereo, faststart
  (moov before mdat), x264 SEI contains exactly one crf string:
  **crf=18.0**.
- **BLAM GATE ON THE MASTER — ALL BARS PASS**: median −27.2 dBFS;
  A1 t50 0.0s / t90 0.0s; A2 lead silence 0.0s; A3 head 0–1s ≈ −22.4 dBFS
  (ABOVE the median); A4 9 HF bursts in 0–1.5s (the designed console
  click + speech onset; no crackle bed); V1 head motion 5.2× the 3–10s
  baseline; V2 first bucket 6.76 = 0.77 of the 0–3s max (no ramp);
  E1 the catch itself at frame 0 (UNC mid-word, monitor black, LAURA
  enters inside the first second) + the Dead Channel live from frame 0.
- **DIALOGUE, FULL MASTER**: ASR of the finished master returns all 86
  scripted words exact and in order (sole deviation: the homophone
  "songs" for "song's", hand-checked). One ASR artifact investigated
  and cleared: whisper reported "I don't know." at 58.6–59.3s (word
  probabilities as low as 0.07); RMS measurement of that span reads
  −42.8 dBFS (silence floor) — an ASR hallucination on the silence
  beat, NOT shipped audio. The beat's audio is genuinely silent.
