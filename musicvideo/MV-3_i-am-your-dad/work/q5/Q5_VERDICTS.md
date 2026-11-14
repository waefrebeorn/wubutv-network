# Q5 VERDICTS — MV-3 (recovery coordinator, revived after 3e440d96 died 2026-11-12 10:45:28 EST)

Previous coordinator fired BOTH takes (cap spent — no more generation) and died while QC-ing.
This file is the verdict checkpoint. Takes verified by md5 against disk before any verdict.

## Takes (ffprobe + md5 verified)
- takes/mv3_s13_t2.mp4 — md5 4b0307b5d7fbbd3188ddf7b6661289f4, 2,174,888 B, h264 1280x720 24fps 10.000s, AAC. Gen ok (snapshot 36235768-a0c4-4cd4-b1e2-3c0c78db4d20:5s5kig).
- takes/mv3_s39_t2.mp4 — md5 8bdab6f48e1f225c32efc3b42d509c8b, 1,933,575 B, h264 1280x720 24fps 10.000s, AAC. Gen ok (snapshot 8ce2bb4d-7066-4340-a651-1fc3df3410a0:7qt09k).
- Vehicles re-read from project root (NOT vehicles/): mv3_s13_vehicle_q5.txt, mv3_s39_vehicle_q5.txt. No lyric quotes in either vehicle (hardened rule) — the generator invented its own words in both takes; see transcriptions below. Per the v4 method, anchors are VISIBLE MOUTH EVENTS, not take-audio words; captions carry the song's words.

## Transcription (faster-whisper large-v3-turbo, word timestamps, on work/q5/*/audio.wav; words.json saved alongside)
- S13 t2: "Welcome to my home, it's good to see you here. Now it's time to say goodbye, don't shed a tear."
  Words: Welcome 0.00-0.64, to 0.64-0.98, my 0.98-1.32, home 1.32-1.90, it's 2.22-2.64, good 2.64-2.92, to 2.92-3.16, see 3.16-3.46, you 3.46-3.76, here 3.76-4.36, [gap 4.36-5.18], Now 5.18-5.84, it's 5.84-6.08, time 6.08-6.30, to 6.30-6.46, say 6.46-6.68, goodbye 6.68-7.16, don't 7.18-8.12, shed 8.12-8.36, a 8.36-8.58, tear 8.58-8.98. RMS 0.1295, peak 0.932.
  Song words in slot (90.66-99.00): dad 90.66, you 91.18, got 94.04, your 94.28, real 94.54, one 94.84, maybe 95.12, or 95.84, maybe 96.02, you 96.68, don't 97.18, go 97.70, matter 98.50, to 98.76.
- S39 t2: "Hello, welcome to my street corner." — ONE phrase only, then silent.
  Words: Hello 0.00-0.96, welcome 1.94-2.80, to 2.80-3.46, my 3.46-4.32, street 4.32-4.84, corner 4.84-5.92. Silence 5.92-10.00. RMS 0.1078, peak 0.939.
  Song mantra bursts in slot (344.55-353.71): b1 344.79-345.71, b2 346.35-347.49, b3 348.29-349.59, b4 351.55-353.21. Take-relative onsets: 0.24, 1.80, 3.74, 7.00.

## Mouth-state reads (full-res frame crops, eye-read; O=open, T=transitional/parted, C=closed)
- S13 t2: t0.00 T (lips parted, red smile), t0.25 O (teeth), t0.50 O (teeth), t2.00 C (closed smile, between words), t3.00 O (teeth), t4.00 O (teeth), t4.20 O (teeth), t5.50 O (wide, teeth), t6.50 O (teeth), t8.00 T (parted, teeth).
  The mouth ARTICULATES through the whole take — this is NOT the t1 painted-smile failure. Open at the head: T at 0.00, O by 0.25s.
- S39 t2: t0.24 O (wide open smile), t1.00 O (small dark O), t1.27 O (dark O), t1.80 O (wide open), t2.63 O (open smile), t3.70 T/O (small O), t5.00 O (open smile, teeth/tongue), t7.00 O (open smile), t7.50 O mouth / EYES CLOSED (happy arcs), t8.50 C (thin closed smile).
  Burst-onset mouth states, 1:1 mapping (take = slot): b1 0.24 O, b2 1.80 O, b3 3.74 ~T/O, b4 7.00 O. Under a 1.42x slow warp (take 0-5.92 -> song 0-8.42): b1 take 0.17 T/O, b2 take 1.27 O, b3 take 2.63 O, b4 take 4.93 ~O (5.00 O). Open at all four burst onsets under either mapping.

## Motion (per-frame mean abs diff, 160x90 gray, 24fps; v6 gate: FAIL if vocal near-dup run >=24f during vocal OR vocal mean diff <0.5)
- S13 t2: mean diff 1.55. Longest run <0.5: 20f at take 3.92-4.75s — UNDER the 24f bar, and the mouth is HELD OPEN (teeth) through it, not frozen shut. PASS.
- S39 t2: mean diff 1.38. Runs <0.5: 15f (0.96-1.58, inter-word gap), 11f (3.29-3.75), 19f (6.04-6.83, post-word tail), 26f (8.58-9.67, silent tail hold). The 26f run is AFTER the last take word (5.92) in the end hold — outside the vocal window; the warp trims it. No >=24f run during vocal. PASS.
- MOTION LAW: both takes move from frame 0 (S13 mean-diff at 0.25s = 11.19; S39 = 7.69). No halted-photo-then-move cut.

## Identity / text / adults
- Both: MONSTER MAN, big yellow ball smiley head, black oval eyes (no white), dark suit, yellow tie. Adults only. No children.
- S13 t2: doorway, warm light, lamps. Zero on-screen text in all sampled frames.
- S39 t2: street corner dusk, shopfronts. G2 NIT (disclosed, not a reject): a background shop sign reads "Pharmacy" — out of focus, small at delivery scale, set dressing in a shopfront street the prepro itself calls for. The t1 anchor has a plain wall (no shops); t2's world is busier. Comparable to accepted background signage; the Q4 S04 reject's signs were prominent + paired with a mouth-closed-at-onset failure, which does not apply here.
- S39 t2 EYE-CLOSE NIT (disclosed): eyes close into happy arcs ~7.25-8.0s (verified 7.25/7.50/7.75/8.00 closed; open at 7.00 and 8.50) during the tail hold, mouth held open. ASSEMBLY CONSTRAINT: the used span must end by take ~6.5s (the 1.42x warp does this); a 1:1 mapping is NOT allowed for S39, it would put the eye-closed beat on burst 4's "am" (352.61).

## VERDICTS
- S13 t2: **KEEP**. Real articulating mouth, open at the head (T 0.00 / O 0.25), open at every sampled word; motion PASS; identity PASS; zero text. The take sings different words than the song — captions carry the truth (same class as the accepted S02 "dad"-for-"game"); assembly maps mouth events to song words. This closes the catalogue's ONLY closed onset (S13 L14 90.66): head-trim/shift so an open mouth lands on the onset (mouth O by take 0.25s — a ~6f trim puts O on the onset, same SHIFT method as the corrected build).
- S39 t2: **KEEP**. Mouth open at all four mantra-burst onsets under either mapping; sung span 5.92s vs t1's 3.14s; tail holds an open smile through the fade instead of t1's closed painted smile. Disclosed: the take sings ONE phrase, not four repeats — the mantra is carried by warp, not by performance (mouth events, not words, are the anchors per the v4 method); "Pharmacy" background sign (G2 nit); eyes-close beat 7.25-8.0s in the tail (assembly must trim to <=6.5s); 26f still run 8.58-9.67s in the silent tail (outside vocal window, trimmed by the warp). The S39 disclosure in MV3_CORRECTED_NOTES.md ("final mantra at 351.55 has no visible articulation") CLOSES: burst-4 onset 351.55 reads O on the new master.
- Neither take is a REJECT. No montage re-cut path needed. Swap BOTH into a new Q5 master (corrected master untouched).

## Gate outcome (Q5 master — full record: work/q5/Q5_NOTES.md)
- Master masters/mv3_i_am_your_dad_16x9_q5.mp4 (md5 c88da1544f6479df5b485c1b2b699518, 83,181,246 B, 8516f): gates ALL PASS — SEI crf=18.0, AAC 48k stereo, faststart, audio PCM md5 identical to corrected, mouth 90.66 C→O and 351.55 C→O (both disclosures CLOSED), motion inherited runs only (S39 24f run eliminated), unchanged scenes frame-identical.
- Chat copy masters/mv3_i_am_your_dad_16x9_q5_chat.mp4 (md5 4e702f61e68e18f4d02921e580db6b75, 26,671,217 B, 854x480, 8516f).
- Corrected master untouched. No commit. No delivered flag (parent writes it).
- S13: phrase-smooth warp from t2's mouth events; head-trim so mouth O lands on song 90.66. Slot 90.66-99.00 (8.34s). Take phrase 1 (0-4.36) -> song 0-7.04 needs 1.61x slow (inside 2x cap); phrase 2 (5.18-8.98) covers the slot tail. Do NOT slow any interval past 2x.
- S39: single smooth warp take 0-5.92 -> song 0-8.42 (1.42x slow, inside cap); used span ends by take ~6.5s; NEVER use take 7.25-8.0s (eye-closed beat) or 8.58-9.67s (still tail). Slot 344.55-353.71 (9.16s).
- New master path: masters/mv3_i_am_your_dad_16x9_q5.mp4 (corrected master NEVER overwritten). Same gates as the corrected build: exact frame count 8516f, x264 SEI crf=18.0, AAC codec, faststart, master-audio agreement MEASURED, mouth-state re-read at all 99 onsets on the new master (S13 90.66 must read O/T; S39 burst onsets must read O/T), motion audit. Chat copy <=50MB if gates pass.
