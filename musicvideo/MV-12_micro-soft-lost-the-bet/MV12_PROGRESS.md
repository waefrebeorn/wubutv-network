# MV-12 PROGRESS

## Status: VOLLEY 1 FIRING (retry after service restart)

- 2026-11-10 ~07:47 EST: LYRIC_TIMELINE.md written (measured; "I'm gonna win" NOT VERIFIED — gap 76.74–80.86 is instrumental).
- 2026-11-10 ~07:48 EST: work/MV_PREPRO_MV-12.md written — 57 scenes S01–S57, montage-first, era-locked choruses, 10 volleys planned.
- 2026-11-10 ~07:50 EST: reference stack built — gates_lock + jobs_lock + s01–s06 starts, all read back PASS, all conformed 1248x704. Logged in work/REFERENCE_STACK.md with md5s.
- 2026-11-10 ~07:52 EST: 6 vehicles written (work/vehicles/mv12_s01–s06_vehicle.txt).
- 2026-11-10 ~07:53 EST: volley 1 fired 6 videos in parallel — ALL 6 failed: "service restarted while it was running". Disk check: takes/ EMPTY, no partial files anywhere. 0/6 landed. No duplicates exist.
- Retry plan: fire in pairs (S01+S02, S03+S04, S05+S06) so a restart costs at most 2.
- 2026-11-10 ~08:0x EST: volley 1 CLOSED — **3 KEEP / 3 REJECT, cap 6/6 spent.** All 6 takes 5.000s exactly.
  KEEP: S03 (mugshot), S04 (paper tape), S06 (dawn silhouettes).
  REJECT: S01 (G2 garbled magazine title + "RAANDOT" poster), S02 (G5 mouth — "We'll call it Apple" over the hook), S05 (G5 mouth — "We rock the night" over the chant).
  Method lesson: MOUTH RULE for MV-12 — no prominent open mouths in montage scenes (generator invents speech every time); chant lives in kinetic type. G2 needs full-res reads (contact sheets hide garbled text).
  Volley 2 owed: S01 t2 (TEXT + CUTAWAY) + S02 t2 (STAGING) + S05 t2 (STAGING) + S07 t1 + S08 t1 + S09 t1.

## Volley 1 — S01–S06 (chorus 1, 1975 disco/metal)

| Scene | Slot | Take | md5 | Verdict |
|---|---|---|---|---|
| S01 | 0.00–2.08 | t1 `8d527363…` | — | **REJECT — G2 text (garbled magazine title + "RAANDOT" poster).** Re-fire v2 in volley 2 (TEXT + CUTAWAY). |
| S02 | 2.08–3.90 | t1 `76ed38f4…` | — | **REJECT — G5 mouth ("We'll call it Apple" over the hook).** Re-fire v2 in volley 2 (STAGING: back-to-camera). |
| S03 | 3.90–5.73 | t1 `eec9f7ca…` | — | **KEEP — mugshot gag lands, fixed grin, rings pulse.** |
| S04 | 5.73–7.55 | t1 `5a821186…` | — | **KEEP — strongest motion in the volley, tape snakes to camera.** |
| S05 | 7.55–9.38 | t1 `45c4f91e…` | — | **REJECT — G5 mouth ("We rock the night" over the chant).** Re-fire v2 in volley 2 (STAGING: mouth not visible). Poster stayed blank — G2 passes. |
| S06 | 9.38–11.21 | t1 `0ddcad22…` | — | **KEEP — dawn silhouettes land, tape banner streams.** |

Cap: 6 videos this volley. No commit (parent commits at the volley boundary).

## Volley 2 — S01 t2 + S02 t2 + S05 t2 + S07 t1 + S08 t1 + S09 t1 (chorus 1 close, 1975 disco/metal)

- 2026-11-10 ~08:1x EST: volley 2 firing. New stack stills generated + read back PASS: s02_start_v2 (back view), s07_start (Gates disco), s08_start (Jobs robot), s09_start (high-five). Vehicles written: mv12_s01_vehicle_v2.txt (TEXT + CUTAWAY), mv12_s02_vehicle_v2.txt (STAGING: back-to-camera), mv12_s05_vehicle_v2.txt (STAGING: drummer / singer from behind), mv12_s07_vehicle.txt, mv12_s08_vehicle.txt, mv12_s09_vehicle.txt.
- Fire order (pairs): S01+S02, then S05+S07, then S08+S09.
- 2026-11-10 ~08:1x EST: pair 1 LANDED — S01 t2 + S02 t2, both 5.000s, 1248x704.
  S01 t2 KEEP (TEXT axis worked — blank magazine, no posters, no legible text; mouths closed).
  S02 t2 KEEP (STAGING axis worked — back-to-camera, no face visible; invented take audio disclosed, no mouth on screen so no mismatch).
  Volley 2 running: 2 KEEP / 0 REJECT, 2/6 fired.
- 2026-11-10 ~08:1x EST: pair 2 LANDED — S05 t2 + S07 t1, both 5.000s, 1248x704.
  S05 t2 KEEP (singer from behind from 0.5s, drummer-focused, audio silent — no invented speech; front-facing belting head 0–0.5s trimmable, assembly takes 0.5–2.33s).
  S07 t1 KEEP (Gates disco-dances, closed-mouth grin, crash zoom in reads, audio silent).
  Volley 2 running: 4 KEEP / 0 REJECT, 4/6 fired. Firing S08+S09 next.
- 2026-11-10 ~08:1x EST: pair 3 LANDED — S08 t1 + S09 t1, both 5.000s, 1248x704.
  S08 t1 KEEP (Jobs robot, closed-mouth smile, mirror-ball dolly reads, strongest motion of the volley, audio silent).
  S09 t1 KEEP (high-five lands, lights blink, mouths are fixed laughing grins, audio mumbles low-p noise in the surplus tail only).
- 2026-11-10 ~08:1x EST: **volley 2 CLOSED — 6 KEEP / 0 REJECT, cap 6/6 spent.** KEEP total: S01–S09 (chorus 1 all but S10–S12 covered).
  Method lessons: (1) the STAGING axis works — back-to-camera (S02) and singer-from-behind (S05) both removed the mouth-speech mismatch; (2) SILENT take audio is now the norm on closed-mouth vehicles — 4 of 6 takes transcribed to near-silence, and the two with invented audio (S02's confident line, S09's tail mumbles) were harmless because no talking mouth was on screen / they sat past the slot; (3) single-image calls open IN the world immediately (S05's front-facing band at frame 0) — a staging that must hold from frame 0 needs the still itself to carry it, not the vehicle text; (4) fixed laughing grins read as CUTAWAY-correct (S09, S03 precedent) — open mouth ≠ talking mouth when the shape never changes across samples.
  Volley 3 owed: S10 t1 + S11 t1 + S12 t1 + S13 t1 + S14 t1 + S15 t1. No commit (parent commits at the volley boundary).

## Volley 3 — S10 t1 + S11 t1 + S12 t1 + S13 t1 + S14 t1 + S15 t1 (chorus 1 close + post-chorus open, 1975 disco/metal)

- 2026-11-10 ~08:3x EST: volley 3 firing. New stack stills generated + read back PASS: s10_start (crowd tape-strip lighters), s11_start (Gates back-view thumbs-up — RESTAGED from the plan row's "turns to the lens" per the less-to-camera directive + MOUTH RULE), s12_start (roof dusk), s13_start (crowd pointing at blank wall), s14_start (Jobs pointing, propeller bow tie — nit: wide open laughing grin in the still, vehicle pins it as a FIXED laugh), s15_start (Gates shrug, glasses sliding). Vehicles written: mv12_s10–s15_vehicle.txt.
- Fire order (pairs): S10+S11, then S12+S13, then S14+S15.
- 2026-11-10 ~08:3x EST: pair 1 LANDED — S10 t1 + S11 t1, both 5.000s, 1248x704.
  S10 t1 REJECT (G5 mouth — take audio invents "Hey, hey, hey!" p=1.00 across the usable span while the crowd's mouths visibly articulate; song chants "Micro soft". Re-fire axis STAGING: crowd from behind / silhouetted, no prominent mouth. Gag reads — tape-strip lighters + dolly).
  S11 t1 KEEP (restage worked — back-view thumbs-up from ~1.0s, audio silent; front-facing morph head 0–0.5s trimmable, usable span 0.5–2.33s).
  Volley 3 running: 1 KEEP / 1 REJECT, 2/6 fired. Firing S12+S13 next.
- 2026-11-10 ~08:4x EST: pair 2 LANDED — S12 t1 + S13 t1, both 5.000s, 1248x704.
  S12 t1 KEEP (crane to wide dusk reads; slow by design, no near-still runs; no people/text).
  S13 t1 KEEP (crowd points in sync, wall stays blank, mouths closed; invented "Point at the wall" sits in the surplus tail only, past the slot).
  Volley 3 running: 3 KEEP / 1 REJECT, 4/6 fired. Firing S14+S15 next.
- 2026-11-10 ~08:5x EST: pair 3 LANDED — S14 t1 + S15 t1, both 5.000s, 1248x704.
  S14 t1 KEEP (Jobs points + laughs, propeller bow tie, push-in reads; fixed-laugh call: one mouth shape across all five samples + audio is laughter, not words; morph head opens on the lock's curtain-stage world, usable span 0.5–2.33s).
  S15 t1 KEEP (shrug lands by ~1.0s, palms up, eyes closed, mouth closed; "Hmm." is a non-word shrug vocal; glasses slide subtle; 21f near-still run in the surplus tail only).
  **VOLLEY 3 CLOSED: 5 KEEP / 1 REJECT, cap 6/6 spent. KEEP total S01–S09 + S11–S15 (14/57).** Re-fire owed: S10 t2 (STAGING — crowd from behind / silhouetted).
  Volley 4 owed: S10 t2 + S16 t1 + S17 t1 + S18 t1 + S19 t1 + S20 t1. No commit (parent commits at the volley boundary).

## Volley 4 — S10 t2 + S16 t1 + S17 t1 + S18 t1 + S19 t1 + S20 t1 (post-chorus close + verse 2)

- 2026-11-10 ~09:0x EST: volley 4 firing. New stack stills generated + read back PASS: s10_start_v2 (crowd from behind, silhouetted), s16_start (Allen blank sign), s17_start (dance battle face-off), s18_start (Jobs silhouette spotlight), s19_start (tiny Jobs laughing, giant blank screen), s20_start (giant Gates-face screen). Vehicles written: mv12_s10_vehicle_v2.txt (STAGING), mv12_s16–s20_vehicle.txt.
- Fire order (pairs): S10+S16, then S17+S18, then S19+S20.
- 2026-11-10 ~09:0x EST: pair 1 LANDED — S10 t2 + S16 t1, both 5.000s, 1248x704.
  S10 t2 KEEP (STAGING axis worked — crowd from behind, no faces/mouths, audio silent; the t1 reject is fixed).
  S16 t1 REJECT (G5 mouth — Allen's mouth opens wide into a laugh at 1.0s then closes; fails the fixed-laugh test part (a). Text alone does not hold a mouth. Re-fire axis STAGING: wider shot, face not prominent.)
  Volley 4 running: 1 KEEP / 1 REJECT, 2/6 fired. Firing S17+S18 next.
- 2026-11-10 ~09:1x EST: pair 2 LANDED — S17 t1 + S18 t1, both 5.000s, 1248x704.
  S17 t1 KEEP (dance battle lands, whip-pan reads, mouths closed, audio silent; Jobs hair drifts slicked-back mid-take).
  S18 t1 KEEP (dark-stage turn lands — silhouette + spotlight + slow fist-close; morph head's lit laughing Jobs trims off at 0.5s; slow by design, S12 precedent).
  Volley 4 running: 3 KEEP / 1 REJECT, 4/6 fired. Firing S19+S20 next.
- 2026-11-10 ~09:1x EST: pair 3 — S19 t1 + S20 t1 both returned integrity_check_failed, no takes on disk (only .json sidecars). NOT retried — the failure instruction bars repeating the request, including with changed arguments. Ledgered BLOCKED per convention.
  S16 t2 fired in the freed cap slot instead (independent request): LANDED, 5.000s, 1248x704.
  S16 t2 KEEP (STAGING axis worked — wide shot, face small/turned away, sign blank, audio silent; tiny "FRAGILE" book-spine label disclosed as a background nit).
  **VOLLEY 4 CLOSED: 4 KEEP / 1 REJECT / 2 BLOCKED, cap 5/6 spent. KEEP total S01–S18 (18/57).**
  OPEN ITEM: S19 + S20 BLOCKED — the verse (1997 Macworld stage + giant Gates-face screen) needs a parent-directed redesign removing the depiction category (S03a precedent). Do not re-fire as designed.
  Volley 5 owed: S21 t1 + S22 t1 + S23 t1 + S24 t1 + S25 t1 + S26 t1. No commit (parent commits at the volley boundary).

## Volley 5 — S19 t2 + S20 t2 + S21 t2 + S22 t2 (REDESIGNED) + S23 t1 + S24 t1 (verse close + pre-chorus + C2 open)

- 2026-11-10 ~09:2x EST: volley 5 firing. New stack stills generated + read back: first pass S19–S22 v2 + S24 v1 ALL REJECTED at read-back — the image generator put legible "Macworld • 1997" banners (one with an Apple logo) on every stage still and covered the S24 office in legible MS-DOS text. Lesson: stage/office stills attract signage — the still prompt must say "no signage" explicitly and never name the event. Regenerated as v3 (S19–S22) / v2 (S24) with explicit no-signage wording: all PASS, no legible text anywhere. S23 PASS first try (TV wall, blank cards). Vehicles written: mv12_s19–s22_vehicle_v2.txt (REDESIGNED — logo screen, never a face), mv12_s23_vehicle.txt, mv12_s24_vehicle.txt.
- Fire order (pairs): S19+S20, then S21+S22, then S23+S24.
- 2026-11-10 ~09:4x EST: pair 1 LANDED — S19 t2 + S20 t2, both 5.000s, 1248x704.
  S19 t2 KEEP (redesigned logo-screen lands — tiny Jobs doubled over laughing, one fixed laughing grin 0.5–2.0s, audio silent, screen blank, motion live).
  S20 t2 KEEP (redesigned logo-screen lands — crash zoom out reads, screen pulses bright into a sunrise by 1.5s, Jobs small below with mouth closed, laughter audio is non-word with no mouth saying it; 22f near-still run at the slot tail is a calm settle, under the 24f threshold, S12/S18 precedent).
  Volley 5 running: 2 KEEP / 0 REJECT, 2/6 fired. Firing S21+S22 next.
- 2026-11-10 ~09:5x EST: pair 2 LANDED — S21 t2 + S22 t2, both 5.000s, 1248x704.
  S21 t2 KEEP (redesigned logo-screen lands — Jobs points up, mouth closed, crowd gasps, confetti, screen blank, audio silent; motion excellent, zero near-still runs).
  S22 t2 REJECT (framing — the handheld wobble tilts up and Jobs exits frame by ~1.2s, absent 1.5–2.0s, only a cropped head/hand back at 2.5s; the screen DIM does read, the wave does not survive the slot. Re-fire axis FRAMING: lock the camera, keep Jobs fully in frame below the screen).
  Volley 5 running: 4 KEEP / 1 REJECT, 5/6 fired. Cap has 1 generation left — S22 t3 CANNOT fire in this volley; it is owed to volley 6. Firing S23+S24 (final pair) next.
- 2026-11-10 ~10:0x EST: pair 3 LANDED — S23 t1 + S24 t1, both 5.000s, 1248x704.
  S23 t1 KEEP (TV wall lands — era worlds scroll past on the dolly, wall ends blank by ~3.5s inside the slot; liveliest motion of the volley, no text, crowd are pure silhouettes).
  S24 t1 KEEP (Gates holds the blank box high, closed-mouth grin in every in-slot sample; invented "I don't know" audio has no mouth saying it in-slot; mouth opens only at 2.0s, past the slot; box blank, monitors plain green).
  **VOLLEY 5 CLOSED: 5 KEEP / 1 REJECT, cap 6/6 spent. KEEP total S01–S21 + S23–S24 (23/57).** Re-fire owed: S22 t3 (FRAMING — lock the camera, keep Jobs fully in frame below the screen).
  Volley 6 owed: S22 t3 + S25 t1 + S26 t1 + S27 t1 + S28 t1 + S29 t1. No commit (parent commits at the volley boundary).

## Volley 6 — S22 t3 + S25 t1 + S26 t1 + S27 t1 + S28 t1 + S29 t1 (verse close + chorus 2, 1997 stage → 1995 Win95)

- 2026-11-10 ~10:15 EST: volley 6 firing — RECOVERY coordinator (revive detector; volley 5 coordinator 634d14b5 completed 09:57:12 EST, no volley 6 chained, disk idle since 09:54:08 EST). Duplicate-coordinator race resolved in the parent's favour of the recovery run: parent-spawned 7d8c6b1e (10:14:57 EST) was closed ~10:18 EST before firing any take; its S25 start still (generated 10:16 EST) was adopted, read back PASS, no work lost.
- New stack stills generated + read back PASS: s25_start (adopted), s26_start, s27_start_v2 (v1 rejected — open laughing grin, restaged closed), s28_start, s29_start. S22 t3 reuses s22_start_v3. Vehicles written: mv12_s22_vehicle_v3.txt (FRAMING — locked slow dolly-in, never tilts up), mv12_s25–s29_vehicle.txt.
- Fire order (pairs): S22+S25, then S26+S27, then S28+S29.
- 2026-11-10 ~10:2x EST: pair 1 LANDED — S22 t3 + S25 t1, both 5.000s, 1248x704.
  S22 t3 KEEP (FRAMING axis worked — Jobs fully in frame at all five samples, screen dims white → blue-grey by 2.0s; invented "Thank you." audio has no mouth saying it, S02 t2 precedent; slowest KEEP yet, usable mean 2.54, eye-decided calm precedent).
  S25 t1 KEEP (relic procession lands — solemn closed mouths, crash zoom out reads, audio silent; ring gains a blue gem top 0.0→0.5s, O shape preserved).
  Volley 6 running: 2 KEEP / 0 REJECT, 2/6 fired. Firing S26+S27 next.
- 2026-11-10 ~10:3x EST: pair 2 LANDED — S26 t1 + S27 t1, both 5.000s, 1248x704.
  S26 t1 REJECT (G1 duplicate character — the push-in morphs Gates across the doors; at 1.5s he appears TWICE in one frame, big head behind Jobs + small head at door 2; 0.0–0.5s is the plan exactly. Re-fire axis STAGING: wide locked framing, Gates stays small at door 2 for the whole take).
  S27 t1 KEEP (tiny computer pops out waving by 2.0s inside the usable span; mouth closed; "Ha ha ha" audio sits in the surplus tail only).
  Volley 6 running: 3 KEEP / 1 REJECT, 4/6 fired. Firing S28+S29 next.
- 2026-11-10 ~10:4x EST: pair 3 LANDED — S28 t1 + S29 t1, both 5.000s, 1248x704.
  S28 t1 KEEP (walk-out lands — Jobs from behind in all five samples, skull flag bobbing, level wobble, audio silent; box full of papers).
  S29 t1 KEEP (midnight queue lands — overhead drop reads, silhouettes shuffle, arms raised at the glowing blank button; "Oh, my God." audio is tail-only, no mouth can say it).
  **VOLLEY 6 CLOSED: 5 KEEP / 1 REJECT, cap 6/6 spent. KEEP total S01–S25 + S27–S29 (28/57).** Re-fire owed: S26 t2 (STAGING — wide locked framing, Gates stays small at door 2 for the whole take; reuse s26_start).
  Method lessons: (1) a push-in can drag the background character forward — S26's duplicate Gates came from the camera move, not the still; two-door scenes need wide locked framing; (2) the FRAMING axis works as a lock (S22 t3 fixed first try); (3) slowest KEEP yet is an eye call — S22 t3 usable mean 2.54 KEEPs on the verified dim event with zero near-still runs.
  Volley 7 owed: S26 t2 + S30 t1 + S31 t1 + S32 t1 + S33 t1 + S34 t1. No commit (parent commits at the volley boundary).

## Volley 7 — S26 t2 + S30 t1 + S31 t1 + S32 t1 + S33 t1 + S34 t1 (chorus 2 close + bridge open, 1995 Win95 → PARC door)

- 2026-11-10 ~10:5x EST: volley 7 firing — coordinator ad9df08f. S26 t2 re-fire axis STAGING (wide locked framing — the t1 push-in cloned Gates; no push-in at all, reuse s26_start). Fresh stack stills generated + read back PASS: s30_start, s31_start, s32_start, s33_start, s34_start. S32 original was 3:2 (1920x1280) — conformed by center-crop to 16:9 then scale, never stretch; the duck is already complete at frame 0, so the flicker + push-in must carry the motion. Vehicles written: mv12_s26_vehicle_v2.txt, mv12_s30–s34_vehicle.txt.
- Fire order (pairs): S26+S30, then S31+S32, then S33+S34.
- 2026-11-10 ~11:0x EST: pair 1 LANDED — S30 t1, 5.000s, 1248x704. S26 t2 BLOCKED on integrity_check_failed (public_figure_likeness) — no take file, sidecar only; the same image pair passed for t1, so enforcement is non-deterministic. NOT re-fired in this volley; S26 stays owed, parent decides the redesign.
  S30 t1 KEEP (chime gag lands — keypress colour flashes read positionally, red ring → blue → green → orange; whip-pan in reads; mouth closed; invented "What is the most important thing to do?" audio sits in the surplus tail only).
  Volley 7 running: 1 KEEP / 0 REJECT / 1 BLOCKED, 2/6 fired. Firing S31+S32 next.
- 2026-11-10 ~11:1x EST: pair 2 LANDED — S31 t1 + S32 t1, both 5.000s, 1248x704.
  S31 t1 KEEP (BSOD curtain lands — Gates shrugs palms-up, crash zoom out arrives by 1.0s, giant blue screen descends plain blue through 2.0s; invented "Well, that's not supposed to happen." audio sits in the surplus tail only).
  S32 t1 KEEP (duck-and-flicker lands — hands fumble cables under the desk, monitor brightens pale→saturated blue, push-in reads; no face ever visible; non-word "Ah, ah." audio, no mouth can say it).
  Volley 7 running: 3 KEEP / 0 REJECT / 1 BLOCKED, 4/6 fired. Firing S33+S34 next.
- 2026-11-10 ~11:2x EST: pair 3 LANDED — S33 t1 + S34 t1, both 5.000s, 1248x704.
  S33 t1 KEEP (mugshot flash lands on the slot boundary — whiteout peaks ~1.3s in a 1.33s slot, pinned with 0.1s-spaced frames; 17f in-slot hold under the 24f threshold; audio silent).
  S34 t1 KEEP (door slams ~0.9s, mouse out by 1.3s, blank window emerging — the float-out reads inside the slot; open mouth at 2.0s is surplus tail, S24 precedent).
  **VOLLEY 7 CLOSED: 5 KEEP / 0 REJECT / 1 BLOCKED, cap 5/6 spent. KEEP total S01–S25 + S27–S34 (33/57).** S26 remains owed — parent-directed redesign for volley 8: S26 t3 FACELESS, hands-only two-door reach, fresh still, never reuse s26_start.
  Method lessons: (1) the likeness check is probabilistic — the same two-image pair passed t1 and BLOCKED t2, so the remove-the-category redesign is the only path; (2) pin a boundary event with 0.1s-spaced frames; (3) a late event counts when it starts inside the slot; (4) a still showing the end state works when the vehicle carries a second event.
  Volley 8 owed: S26 t3 (FACELESS redesign) + S35 t1 + S36 t1 (needs redesign first — giant Gates-face screen, parent-flagged) + S37 t1 + S38 t1 + S39 t1. No commit (parent commits at the volley boundary).

## Volley 8 — S26 t3 (FACELESS redesign) + S35 t1 + S36 t1 (LOGO-SCREEN redesign) + S37 t1 + S38 t1 + S39 t1 (bridge, 1979 PARC door → 1998 COMDEX)

- 2026-11-10 ~12:0x EST: volley 8 firing. Fresh stack stills generated + read back PASS: s26_start_v3 (FACELESS — hands only, no faces, no people; the window icon reads as four glowing panes), s35_start (burglars + blank TV), s36_start (giant blank screen, tiny Jobs, mouth closed), s37_start (queue from behind, blank sunrise button), s38_start (overhead curtain-catch), s39_start (worker from behind, tipping cup — S32 end-state precedent noted). All conformed 1248x704 by center-crop, never stretch. Vehicles written: mv12_s26_vehicle_v3.txt (FACELESS — single image, NO lock), mv12_s35–s39_vehicle.txt (S36 two-image jobs_lock -> s36_start; S38 two-image gates_lock -> s38_start; S35/S37/S39 single-image).
- Fire order (pairs): S26+S35, then S36+S37, then S38+S39.
- 2026-11-10 ~12:0x EST: pair 1 LANDED — S26 t3 + S35 t1, both 5.000s, 1248x704.
  S26 t3 KEEP (FACELESS redesign lands — hands-only two-door reach, no face ever appears, audio silent; the icon sparkles at 1.0s as both hand-pairs converge; calm motion, usable mean 4.66, S18/S22 t3 precedent).
  S35 t1 KEEP (race lands — burglars sprint 0.5–1.0s, arrive at the window together ~1.5s inside the slot; mouths closed, TV blank; "Oh, my God." audio is tail-only; poster fragments below G2).
  Volley 8 running: 2 KEEP / 0 REJECT, 2/6 fired. Firing S36+S37 next.
- 2026-11-10 ~12:1x EST: pair 2 LANDED — S36 t1 + S37 t1, both 5.000s, 1248x704.
  S36 t1 KEEP (logo-screen redesign lands — screen blank in all five samples, dips like a nod 1.0–1.5s; Jobs small below, mouth closed in profile from 0.5s; morph head's open grin trims off at 0.5s; audio silent).
  S37 t1 KEEP (wave lands — arms rise left→right from ~1.0s, button flares as the wave reaches it; queue stays faceless silhouettes; audio silent; 0.0→0.5s arm-drop is a morph-head re-render, assembly takes 0.5–1.40s).
  Volley 8 running: 4 KEEP / 0 REJECT, 4/6 fired. Firing S38+S39 next.
- 2026-11-10 ~12:1x EST: pair 3 LANDED — S38 t1 (5.000s) + S39 t1 (10.000s — slot-length unreliability, assembly trims).
  S38 t1 KEEP (curtain catch lands at ~2.0s — usable window 0.6–2.0s holds the whole arc: pull-up + wide + drop + catch; morph head trims off; audio silent).
  S39 t1 KEEP (flicker + spill + duck all land in-slot; the cup spills onto the desk instead of falling off — disclosed partial gag miss; "Ah, ah." audio is deep tail only).
  **VOLLEY 8 CLOSED: 6 KEEP / 0 REJECT, 6/6 fired. KEEP total 39/57 (S01–S25 + S26 t3 + S27–S39).** Volley 9 owed: S40 (needs redesign first — giant Gates-screen handshake, parent-flagged) + S41–S45 in plan order.

## Volley 9 — S40 t1 (HANDS-ONLY redesign) + S41 t1 + S42 t1 + S43 t1 + S44 t1 + S45 t1 (bridge close + gap + final chorus open)

- 2026-11-10 ~12:3x EST: volley 9 firing. Fresh stack stills generated + read back PASS: s40_start (REDESIGN — hands-only handshake, blank screen, tiny figure from behind, NO faces), s41_start (four spotlights converge on empty pedestal), s42_start (spotlights circling, cube pedestal, orbit circle), s43_start (two dancers, mouths closed), s44_start (crowd silhouettes from behind), s45_start (frozen grin, spinning office, papers blank). All conformed 1248x704 by center-crop, never stretch. Vehicles written: mv12_s40–s45_vehicle.txt (S40 single image, NO lock — no faces; S43/S45 two-image gates_lock -> start; S41/S42/S44 single image).
- Fire order (pairs): S40+S41, then S42+S43, then S44+S45.
- 2026-11-10 ~12:3x EST: pair 1 LANDED — S40 t1 (2.000s — slot-length request worked) + S41 t1 (10.000s — slot-length unreliability, assembly trims), both 1248x704.
  S40 t1 KEEP (HANDS-ONLY redesign lands — handshake grows to giant arms by 0.5s, screen blank in all five samples, figure never turns; invented "Thank you." audio has no mouth saying it).
  S41 t1 KEEP (convergence lands — beams tighten onto the pedestal by 1.5s, pedestal lights in four colours; slow by design, eye-decided calm precedent; invented "Thank you." audio, no mouth).
  Volley 9 running: 2 KEEP / 0 REJECT, 2/6 fired. Firing S42+S43 next.
- 2026-11-10 ~12:4x EST: pair 2 LANDED — S42 t1 (4.000s — slot-length request worked) + S43 t1 (2.000s), both 1248x704.
  S42 t1 KEEP (circling lands — beams rotate around the pedestal through the full 4s, verified at 1.0/2.0/3.0/3.9s; pull-back reads; audio silent; 10f head settle disclosed).
  S43 t1 KEEP (dance lands — steps change through the take, mouths closed in every sample, tiles light underfoot; audio effectively silent; world morphs to a disco club by ~1.0s, disclosed).
  Volley 9 running: 4 KEEP / 0 REJECT, 4/6 fired. Firing S44+S45 next.
- 2026-11-10 ~12:5x EST: pair 3 LANDED — S44 t1 + S45 t1, both 2.000s, 1248x704.
  S44 t1 KEEP (wave lands — arms rise left→right, crowd surges toward the lens at 1.5s, crests at 1.9s; silhouettes only, no faces; audio effectively silent).
  S45 t1 KEEP (hold lands — office vortex spins around the frozen man, push-in reads, grin one fixed closed-mouth shape in every sample; audio effectively silent; papers carry faint motion-blurred scribbles, disclosed, below G2).
  **VOLLEY 9 CLOSED: 6 KEEP / 0 REJECT, 6/6 fired. KEEP total 45/57 (S01–S25 + S26 t3 + S27–S45).** Volley 10 owed: S46 t1 + S47 t1 + S48 t1 + S49 t1 + S50 t1 + S51 t1 in plan order. No commit (parent commits at the volley boundary).

## Method lessons (volley 9)

1. **Slot-length requests mostly work now.** Five of six takes returned exactly the requested duration (S40 2.000s, S42 4.000s, S43/S44/S45 2.000s); only S41 returned 10.000s on a 2s request. Ask for the slot length; ffprobe anyway, assembly trims.
2. **The remove-the-category redesigns keep working first try.** S40's hands-only handshake is the third application (after S19/S20 logo-screen and S26 t3 faceless) — no integrity failure, no face anywhere, and the giant-handshake growth by 0.5s is a better gag than the plan's static handshake.
3. **A 2.000s take has no frame at exactly 2.0s.** Extract the fifth QC frame at 1.9s (S40, S43) — the -ss-at-duration edge silently yields nothing.
4. **Calm shots KEEP on a verified positional event, not a number.** S41's usable mean 1.77 is the slowest KEEP since S22 t3 (2.54) — the beams converging onto the pedestal by 1.5s is the event; S42's circling beams are the same pattern at 3.96.
5. **A two-image morph can re-render the world and still KEEP.** S43's wall becomes a disco club by 1.0s; S45's office becomes a vortex by 0.5s. When the motion + gag survive the re-render, the morph-head is a disclosure, not a reject.

## Volley 10 — S46 t1 + S47 t1 + S48 t1 + S49 t1 + S50 t1 + S51 t1 (final chorus mid, cloud room → green room → yellow room → tile floor → stage → cloud room)

- 2026-11-10 ~12:5x EST: volley 10 firing. Fresh stack stills generated + read back PASS: s46_start (Jobs juggling orbs, yellow orb orbiting on a ring), s47_start (green room crowd from behind, giant controller), s48_start (yellow magnifying-glass room, overhead), s49_start (back-to-back dance on glowing tiles), s50_start (Jobs presenting the tiny glowing square, blank screen), s51_start (Gates riding the server rack through clouds). All conformed 1248x704 by center-crop, never stretch. Vehicles written: mv12_s46–s51_vehicle.txt (S46/S49/S50/S51 two-image lock -> start; S47/S48 single image).
- Fire order (pairs): S46+S47, then S48+S49, then S50+S51.
- 2026-11-10 ~12:5x EST: pair 1 LANDED — S46 t1 (10.000s — slot-length unreliability, assembly trims) + S47 t1 (2.000s), both 1248x704.
  S46 t1 KEEP (juggle lands — orbs arc between his hands, yellow orb circles his head, mouth closed in every sample; audio effectively silent; disclosed: blue orb passes over his face at ~0.5s, orb colours wobble at the tail, tiny 0/1 digits in the data streams below G2).
  S47 t1 REJECT — G2 generated on-screen text (giant "CROWD CHEERS!" caption covers the whole usable span; crowd staging itself works). Reroll axis TEXT (reuse s47_start, forbid caption-style text bursts) → S47 t2 owed in volley 11 (cap: 4 generations remain in this volley for S48–S51).
  Volley 10 running: 1 KEEP / 1 REJECT, 2/6 fired. Firing S48+S49 next.
- 2026-11-10 ~12:5x EST: pair 2 LANDED — S48 t1 + S49 t1, both exactly 2.000s, 1248x704.
  S48 t1 KEEP (overhead drop lands — view descends into the room of magnifying glasses, lenses glint and grow; no people, no text; audio invents "Thank you." with no mouth on screen, harmless).
  S49 t1 KEEP (back-to-back dance lands — both groove on tiles that light underfoot, whip-pan closes in at 0.5s and pulls back by 1.0s, both fully in frame, mouths closed throughout, audio silent; disclosed: tight 0.5s close-up, eyes closed mid-groove, disco-club world from the still).
  Volley 10 running: 3 KEEP / 1 REJECT, 4/6 fired. Firing S50+S51 next.
- 2026-11-10 ~13:0x EST: pair 3 LANDED — S50 t1 + S51 t1, both exactly 2.000s, both 1280x720 (house resolution, not 1248x704).
  S50 t1 KEEP (presentation lands — square flares at 0.5s, lifted high and blazing by 1.0s, blank screen, mouth closed, audio silent; disclosed: crash zoom went IN not out).
  S51 t1 KEEP (surf-ride lands — Gates surfs the cloud corridor, arms out, data streams streaking, strongest motion in the volley at 27.93; disclosed partial gag miss: the rack morphs into a rainbow surfboard by 0.5s and drops out of frame — the ride survives, the rack-as-board does not).
  **VOLLEY 10 CLOSED: 5 KEEP / 1 REJECT, 6/6 fired. KEEP total 50/57 (S01–S25 + S26 t3 + S27–S45 + S46 + S48–S51).** Volley 11 owed: S47 t2 (TEXT reroll) + S52–S57 in plan order. No commit (parent commits at the volley boundary). No Telegram sitreps (parent sends).

## Method lessons (volley 10)

1. **A caption can slam in after a clean first frame.** S47's frame 0 was the clean still; the "CROWD CHEERS!" caption arrived by 0.5s and stayed. A clean morph head does not clear a take — the 0.5s sample is the first real gate sample.
2. **The generator invents captions, not just words.** S47's caption is a comic-book text burst the vehicle never asked for — the anti-text clause must name caption-style bursts explicitly ("no comic-book captions, no text bursts") in the reroll, not just "no text".
3. **A crash zoom can flip direction.** S50's zoom went in, not out — the vehicle asked "crash zoom out" and the take crash-zoomed in. The event still landed, but a zoom's direction is not steerable; don't build a scene that depends on the direction.
4. **A morph can swap the prop and still KEEP.** S51's rack became a rainbow surfboard — the ride survived, the prop identity didn't. Judge the action, not the prop name: if the one-sentence gag still reads, it's a disclosure.
5. **1280x720 returns happen.** S50/S51 came back true 720p, not 1248x704 — the take resolution is whatever the generator returns; ffprobe anyway, assembly handles house resolution natively.

## Volley 11 — S47 t2 (TEXT reroll) + S52 t1 + S53 t1 (LOGO-HOLOGRAM redesign) + S54 t1 + S55 t1 + S56 t1 (HANDS-ONLY redesign) (final chorus close + outro)

- 2026-11-10 ~13:3x EST: volley 11 firing. Fresh stack stills generated + read back PASS: s52_start (crowd lifts both caricatures overhead, from behind), s53_start (four-squares logo hologram over the dance floor, both caricatures dancing beneath — REDESIGNED, no face anywhere), s54_start (empty tile room, one flipped tile), s55_start (crowd from behind, hands in the air), s56_start (hands-only handshake, both from behind, blank screen — REDESIGNED on the S40 precedent). S47 t2 reuses s47_start (volley-10 read-back PASS). All conformed 1248x704 by center-crop, never stretch. Vehicles written: mv12_s47_t2_vehicle.txt + mv12_s52–s56_vehicle.txt (all single image).
- Fire order (pairs): S47+S52, then S53+S54, then S55+S56.
- 2026-11-10 ~13:4x EST: pair 1 LANDED — S47 t2 (2.000s, 1248x704).
  S47 t2 KEEP (TEXT reroll lands — the "CROWD CHEERS!" caption is gone, no text in any sample; crowd surges from behind, arms pumping, controller buttons glowing; audio effectively silent; disclosed: slow push-in, not a handheld wobble).
  S52 t1 BLOCKED — integrity_check_failed (no take file; the two-caricature crowd-surf depiction tripped it). NOT retried as designed. Redesign: crowd surfs the glowing four-squares tile overhead, NO caricatures in the scene → S52 t2.
  Volley 11 running: 1 KEEP / 1 BLOCKED, 1/6 fired. Firing S52 t2 + S53 next.
- 2026-11-10 ~13:5x EST: pair 2 LANDED — S52 t2 + S53 t1, both exactly 2.000s, 1248x704.
  S52 t2 KEEP (redesign lands — crowd surfs the glowing four-squares tile overhead, dolly past reads; no caricatures, no faces, no mouths; audio effectively silent; disclosed: illegible neon scribble-signs below G2, tile gains cube depth by 1.0s, two small background profiles at the left edge at 1.9s with no mouths).
  S53 t1 KEEP (THE PEAK lands — four-squares hologram pulses above the dancers, tiles strobe in four colours, both caricatures dance with arms up; no face anywhere, no mouths, no text; audio effectively silent; disclosed: overhead drop reads as a slow push, hologram squares shift colours as they strobe).
  Volley 11 running: 3 KEEP / 1 BLOCKED, 3/6 fired. Firing S54+S55 next.
- 2026-11-10 ~13:4x EST: pair 3 LANDED — S54 t1 (2.000s) + S55 t1 (4.000s — slot-length request worked), both 1248x704.
  S54 t1 KEEP (the flip lands — tile flat at 0.0–0.5s, up on edge at 1.0–1.5s, flat again by 1.9s; calm by design, eye-decided on the positional event; audio effectively silent; disclosed: flip mid-slot, room reads plain rather than a dance floor).
  S55 t1 KEEP (last chant lands — crowd from behind, hands pumping in rhythm, tiles glowing, whip-pan in reads; no faces, no mouths, no text; invented "Hey! Hey!" audio with no mouth on screen, harmless per S13 precedent; disclosed: world morphs to a club by 0.5s).
  Volley 11 running: 5 KEEP / 1 BLOCKED, 5/6 fired. Firing S56 next.
- 2026-11-10 ~13:43 EST: S56 t1 LANDED — 4.000s, 1248x704.
  S56 t1 KEEP (hands-only seal lands — firm handshake at 0.0–0.5s, joined hands pump up high at 1.0s and hold through 1.9s as the crowd roars below; both figures from behind throughout, no faces, no mouths, no text, no signage; audio effectively silent; disclosed: hands-pump beat at ~1.0s, crowd only enters the bottom edge from ~1.9s).
  **VOLLEY 11 CLOSED: 6 KEEP / 1 BLOCKED, 6/6 fired. KEEP total 56/57.** Volley 12 owed: S57 t1 (finale). No commit (parent commits at the volley boundary).

## Method lessons (volley 11)

1. **The TEXT axis works when the clause names the artifact.** S47 t2's "no comic-book captions, no text bursts" killed the caption that "no text" alone could not. Name the artifact the last failure produced.
2. **A two-caricature depiction can trip integrity even from behind.** S52 t1 failed on the crowd-surf with both caricatures visible (from behind in the still). The remove-the-category redesign (crowd surfs the glowing four-squares tile, no caricatures at all) fired clean first try — the fifth application of the pattern, and the second this volley after S53/S56 were redesigned before firing.
3. **The remove-the-category redesigns keep working first try — all three in this volley.** S52 t2 (logo rider), S53 (logo hologram), S56 (hands-only) — zero integrity failures across the volley after the one S52 t1 block.
4. **A morph can turn a flat prop 3D and still KEEP.** S52 t2's tile gains cube depth by 1.0s — judge the action (the surf), not the prop's geometry.
5. **Invented chant audio with no mouth on screen stays harmless.** S55's "Hey! Hey!" (p=0.99) has zero visible mouths — the S13 precedent holds at full confidence.
6. **Slot-length requests keep working.** S55 + S56 returned exactly 4.000s on 4s requests; S47/S52/S53/S54 returned exactly 2.000s. Ask for the slot length; ffprobe anyway.

## Volley 12 — S57 t1 (finale, dorm-hallway bookend)

- 2026-11-10 ~14:0x EST: volley 12 firing. Fresh stack still generated + read back PASS: s57_start (the S01 hallway, now empty; magazine glowing on the floor, cover blank except for a small plain computer illustration; no people, no legible text). Vehicle written: mv12_s57_t1_vehicle.txt (single image, slow dolly in, calm by design — S41/S42/S54 precedent).
- Fire: S57 t1 (slot-length request ~4.5s).
- 2026-11-10 ~14:0x EST: S57 t1 LANDED — 10.000s (slot-length unreliability, assembly trims), 1248x704, md5 verified 5d3df5984055279ac248cd74a72b9304.
- 2026-11-10 ~14:13 EST: previous volley-12 coordinator died mid-QC (daemon restart, 14:10:51 EST) — RECOVERY coordinator resumed from disk. QC completed from the on-disk frames + audio: transcription effectively silent (one p=0.03 "I" 0.00–0.96s, no mouth); motion usable mean 4.49, no near-still runs in the 4.45s span; full-res eye-read of all five frames — magazine cover blank except the small plain computer illustration, no legible text anywhere, no people/faces/mouths; dolly-in + glow pulse verified positionally.
  S57 t1 KEEP (the bookend lands — empty hallway, glowing magazine, rhymes with S01's first frame).
  **VOLLEY 12 CLOSED: 1 KEEP / 0 REJECT, cap 1/6 spent. KEEP total 57/57 — ALL SCENES COVERED. Assembly next (parent chains).** No commit (parent commits at the volley boundary). No Telegram sitreps (parent sends).

## ASSEMBLY — coordinator c43865be, 2026-11-10 ~14:2x EST
- Contract: 57 segments, boundaries = plan slot starts (contiguous), S42 ends 80.57 (S43's plan start — resolves the plan's 0.29s S42/S43 overlap; section timeline's C3 start 80.86 is superseded by the scene table's 80.57 downbeat). S57 ends 114.22. Total = round(114.20*24) = 2741f.
- Usable spans per TAKE_LEDGER.md are the authority; warp factors all inside the 2x slow cap (slowest 1.60x S33/S34, 1.55x S36/S37, 1.38x S31; rest 0.96–1.14x). S42 take is 4.000s vs 4.12s slot — window is take frames 0–96, warped 0.958x to 92f.
- Pattern follows MV-11 rebuild: per-segment CRF-14 intermediates (scale 1280x720) → split encode halves with kinetic .ass burned → mux with track.mp4 audio re-encoded AAC 192k, apad capped, -t 114.20, faststart.
- 2026-11-10 ~14:3x EST: ASSEMBLY segments built — all 57 KEEP takes resolved by ledger md5 (65 mp4s hashed), all segments exact frame counts, total 2741f. Manifest work/assembly/assembly_manifest.json.
- Kinetic + post layers built (work/assembly/mv12_kinetic.ass, 423 events): 30 lyric lines / 182 words (4 dropped: "I'm gonna win" unverified + pre-chorus garble tail "you"), SLAM hook / CASCADE chant / HIGHLIGHT verse; era logo lower-third per scene (disco/metal/blibbet/Pac-Man-italic/four-squares); Clippy photobomb S08/S29/S49; Pac-Man logo pass S10/S30/S51; "~ WuBu ~" corner bug. ASR corrections applied vs lyric sheet (MicroSaw->"Micro soft", bed/ball/best->bet, make->name, pre-chorus line 2 rebuilt as "Now we all know the joke", outro "He lost the bet he lost the").
- Density audit (assembly contract): C1 33.8/min PASS, PC 30.3 PASS, Verse 22.6 PASS, Pre-Ch 16.5 PASS, C2 33.8 PASS, Bridge 40.5/min vs rule-4 target 66/min = 61% — FAIL on the letter of rule 4 (plan's bridge slots are ~1.5s/shot by design, "staccato era flashes (~1.5s/shot)"; assembly delivers the plan's density exactly — a plan-level density choice, not an assembly miss; no jump-cut hack applied). Gap sanctioned slow shot. C3 35.7 PASS, Outro 15.6 PASS.
- Vantage audit: no two consecutive shots share a camera move (all 56 joints change angle/distance). Logo-era audit: NONE mismatched after fixing S57 to disco (1975 bookend rhymes with S01; four-squares there would have been the one violation).
- Split encode: halves S01–S29 (1408f) + S30–S57 (1333f), CRF 18, kinetic .ass burned in. Half 2 re-encoded once: S57 logo era corrected disco (1975 bookend rhymes with S01; four-squares there would have been the one logo-era violation).
- Mux: masters/mv12_micro_soft_lost_the_bet_16x9.mp4 — 2741f, 92,877,987 B, md5 a074f68bbfdc6be7bca0b6afc1adf370.
- GATES ALL PASS: h264 1280x720 24fps, 2741f, 114.20s, AAC 48k stereo, SEI crf=18.0, faststart moov@36, audio agreement min corr 0.9986 (5 windows).
- Motion audit: mean diff 19.04; one near-still run ≥12f: 13f @38.58–39.08s during words (S20 screen settle, QC-disclosed calm; under the 24f fail threshold). No fail-range runs.
- Chat copy: masters/mv12_micro_soft_lost_the_bet_16x9_50mb.mp4 — 38,130,438 B (36.4 MB), 2741f, md5 4671fd25aa705dd7b873bbdd6980baec; AAC stream md5 identical to house (copied untouched), faststart verified.
- Eye review (10 md5-distinct frames from the master): cold open, Clippy S08, Pac-Man S10 (eating the O — lands), verse S19, C2 open S24, bridge S33, gap S42 (four-squares logo renders), peak S53, bookend S57 (disco logo, rhymes with S01). All 10 gags read in one sentence. Clippy renders small/ambiguous at the corner (reads as a white edge mark at still scale — disclosure, not a fail). Cold-open 0.5s frame is the hallway world arriving (same payphone wall as S57), gag lands by 1.5s per QC.
- Word-sync: kinetic type on measured SONG_WORDS times (182 words, 30 lines); no take attempts lip-sync by design (MOUTH RULE — chant lives in kinetic type + master audio). "I'm gonna win" NOT captioned (unverified).
- DENSITY AUDIT: 8/9 sections PASS; Bridge 40.5/min vs rule-4 target 66/min = FAIL on the letter (plan's bridge slots are ~1.5s/shot by design; assembly delivers the plan's density exactly — plan-level choice, no jump-cut hack applied).
- ASSEMBLY COMPLETE — master + chat copy ready for parent delivery. No commit, no _DELIVERED.flag, no Telegram sitrep (parent-owned).

## Q1 — MV-12 kinetic rebuild (MV improvement program, user msg 303; coordinator 2026-11-12 ~04:05 EST)
- Defect (parent-verified): work/assembly/mv12_kinetic.ass carried 99 `\\i1` Dim events eating `\an4`/`\an5` (88x an4 + 11x an5, 33.20–75.10s). Root cause: build_kinetic_mv12.py era-font override added a literal `\` separator before `extra` (`\i1`), doubling it for pacman-era lines. Fixed at source (separator dropped); Clippy scaled 1.6x in the same pass (44x84 -> ~70x134, anchored bottom-right (1224,644)).
- Stem verdict 2026-11-12 ~04:30 EST (MDX-Net ONNX vocal stem + faster-whisper large-v3-turbo, fixed config, 16k mono): "I'm gonna win" NOT sung — stem silent (RMS 9–121) across 79.36–80.86 vs 1100–2600 for the detected solo vocal; stem-whisper hears nothing after 77.78; both independent mix passes agree on "I can't believe you" smeared 78.60–82.24, neither hears "I'm gonna win". "you" 47.28 NOT sung — clean-stem whisper hears "Now we all know the joke." (p=0.94–0.99), "joke" spanning 47.24–47.64 exactly where "you" was alleged. Both stay dropped; kinetic stays 182 words. Caveat logged: MDX routes this track's chant hook to the inst stem (known-sung hook 80.86+ is silent on the vocal stem) — the stem rules out a solo delivery, not a chant one; the mix passes + RMS + sheet agree with the verdict.
- Regenerated mv12_kinetic.ass: 0 double-backslash lines, 419 events (unchanged), words JSON byte-identical, 123 lines changed (99 Dim + 24 Clippy). Part .ass files re-split by split_encode_mv12.py (68+32 incl. 1 straddle duplicate).
- Split re-encode running (halves deleted, re-encoding CRF 18 with fixed .ass); v2 master + chat copy + gates to follow. Delivered v1 master NEVER overwritten.
- Rebuild COMPLETE 2026-11-12 ~05:00 EST: split re-encode (half1 1408f/46,675,389 B; half2 1333f/43,372,073 B; one runtime kill mid-half-1 ~04:46, partial deleted, relaunched, finished clean) -> v2 master masters/mv12_micro_soft_lost_the_bet_v2_16x9.mp4 (2741f, 92,880,433 B, md5 361396c2d80e273f3be1ab1b97beaf13) + chat copy v2 (38,129,387 B, md5 634e3f3e61e00c63b57bd31828954aea, audio md5 == house 11a1ce52a8783ae5008e7ff6d4ac3e7a). V1 master untouched (md5 a074f68bbfdc6be7bca0b6afc1adf370). Gates ALL PASS (h264 1280x720 24fps, AAC 48k stereo, SEI crf=18.0, faststart moov@36, audio agreement min corr 0.9986). Motion audit PASS: only near-still 13f @38.58s (same S20 settle as v1, under 24f bar). Frame reads (full-res, 8 distinct md5s): 33.20 "Steve" an4 middle-left bold yellow + Dim trail; 47.44/51.26/56.76/80.86 Dim "I" at an5 middle-center; S08/S29/S49 Clippy 1.6x reads as a paperclip at bottom-right, clear of bug/logo. Disclosed carry-overs: bridge density + 4 dropped words unchanged (stem verdict stands); first word of each line is mid-fade (fad 120ms) and faint at exact line-start frames against bright backgrounds — same as v1, not introduced by this rebuild. NO commit, NO delivered flag (parent writes it).

## Q2 — MV-12 bridge-density re-cut (MV improvement program; RECOVERY coordinator, revived 2026-11-12 ~05:13 EST after Q2 coordinator 84137522 died 05:10:02 EST, transport error, zero disk output)
- Defect (v2 disclosure): bridge 40.5 cuts/min vs rule-4 target 66/min — the only FAIL in the v2 density audit. Plan's bridge section = 63.42–76.74 (S33–S41, 13.32s, 9 shots); S42 is the Gap (sanctioned slow shot, 76.74–80.57), NOT in the audited bridge span.
- Verified this run: v2 master md5 361396c2d80e273f3be1ab1b97beaf13 ✓; track.mp4 md5 25cf688c8a2cc01d5769dedd02f76923 ✓; all 10 bridge takes resolved by ledger md5 ✓. Kinetic .ass reused as-is (words stay on measured SONG_WORDS times; 0 double-backslash lines).
- Surplus analysis (work/assembly/q2/analyze_surplus.py + surplus_motion.log; per-frame 160x90 diffs + 4fps contact sheets, all 10 sheets eye-read): S33 strobe (rainbow laser chart 2.75–3.75s, motion 4.8–6.8), S34 float-out (mouse+window fully out 1.5–2.5s, motion 11–17), S35 close-up faces (lunge+close-up 2.25–2.75s, burst 28.2), S37 button flare peak + push-in (2.0–2.5s, motion 9.7–13.1), S38 cape spread (3.5–4.0s, motion 10–21), S39 ducked-worker aftermath + flicker (1.5–2.5s, motion 5–7), S41 tightened beams + push-in (3.5–4.5s, motion 4.6–5.7). NO split: S36 (surplus = slow settle, no distinct event; dip stays whole), S40 (take 2.0s, 7f surplus tail only), S42 (whole take used, no surplus).
- Split design (7 scenes → 2 sub-shots each; all warps are speedups, none past the 2x slow cap; every sub-shot cut lands on a word boundary or a beat, every B first frame in-motion by the diff numbers):
  S33 32f: A f12–31→14f (0.70x, mugshot+flash) | B f66–89→18f (0.75x, rainbow strobe) | cut 64.00 ("a"/"bet,")
  S34 32f: A f12–31→20f (1.00x, slam) | B f36–47→12f (1.00x, float-out) | cut 65.58 ("the"/"ball")
  S35 38f: A f6–37→24f (0.75x, race+arrival) | B f60–73→14f (1.00x, close-up faces) | cut 67.06 ("bed"/"and")
  S37 34f: A f12–33→22f (1.00x, wave sweep) | B f48–59→12f (1.00x, button flare) | cut 70.02 ("he"/"had")
  S38 34f: A f14–47→21f (0.62x, pull-up+drop+catch) | B f84–96→13f (1.00x, cape spread) | cut 71.36 ("name"/"it")
  S39 34f: A f0–23→20f (0.83x, spill+duck) | B f36–49→14f (1.00x, ducked+flicker) | cut 72.75 (beat 72.754, held "it")
  S41 41f: A f0–40→22f (0.54x, converge+light) | B f84–107→19f (0.79x, tightened beams) | cut 75.95 (beat 75.946, held "it")
  S36/S40/S42 single (v2 segments reused). Bridge shots 9 → 16; predicted density 16/13.32×60 = 72.1/min vs 66 target. Half 1 (S01–S29) untouched — master_part1.mp4 reused; only half 2 re-encoded. Kinetic .ass unchanged.
- Sub-shots BUILT 2026-11-12 ~05:2x EST (work/assembly/q2/build_subshots_v3.py): 14/14, 245f, all exact frame counts, md5s in work/assembly/q2/manifest_v3.json. All warps speedups (0.54–1.00x); slowest 0.54x S41a (1.86x speedup, inside caps).
- Half-2 v3 ENCODED 2026-11-12 ~05:36 EST (work/assembly/q2/split_encode_v3.py): 1333f, 44,499,502 B; half 1 master_part1.mp4 (1408f) reused untouched.
- V3 MUXED 2026-11-12 ~05:37 EST (q2/mux_v3.py): masters/mv12_micro_soft_lost_the_bet_v3_16x9.mp4 — 2741f, 94,007,898 B, md5 87cad49658d1cb41a110a69e3e9f85f3. v1 (a074f68bbfdc6be7bca0b6afc1adf370) + v2 (361396c2d80e273f3be1ab1b97beaf13) untouched.
- GATES v3 ALL PASS 2026-11-12 ~05:38 EST (gate_master_mv12.py): 2741f, 114.20s (114.208333), h264 1280x720 24fps, AAC 48k stereo, x264 SEI crf=18.0, faststart moov@36, audio agreement min corr 0.9986 (5 windows 0.9986–0.9997).
- MOTION AUDIT v3 PASS 2026-11-12 ~05:39 EST (motion_audit_mv12.py): only near-still run >=12f is the known 13f @38.58s S20 settle (disclosed carry-over); NO fail-range runs >=24f during words.
- DENSITY AUDIT v3 PASS 2026-11-12 ~05:47 EST (q2/density_audit_v3.py, exit 0): bridge 63.42–76.74 = 16 shots → 72.1 cuts/min vs 66 target (v2: 9 shots → 40.5/min). S33–S42 span 17 shots → 59.5/min (S42 sanctioned gap). All 7 sub-shot cuts verified REAL on-master (exact frame indices, A-last vs B-first mean abs-diff 25.5–45.5 vs within-shot medians 3.2–20.2). Audit-method notes: (1) -ss frame sampling lands one frame late on non-frame-aligned cut times — switched to exact frame-index select; (2) 3x cut-vs-median rule miscalibrates on violent-motion scenes (S34/S38 medians 15.6/20.2) — recalibrated to 2x + absolute floor 20, S34/S38 eye-verified at full res (different framing + moment across each cut); (3) ffmpeg trim=start_frame ignored start_frame on this master (returned 1860f) — select+vsync 0 is the reliable exact-frame path; (4) S37 cut confirmed at frame 1680 (70.00s), cut-diff 33.82 — the first 0.24 reading was the off-by-one sampler, not a missing cut.
- EYE-READ v3 bridge PASS 2026-11-12 ~05:47 EST: 21 full-res frames from the v3 master (7 A-mid, 7 B-mid, S34/S38 cut pairs, S36/S40/S42 spots) in work/assembly/q2/check/. Every B sub-shot reads as a distinct in-motion beat (S33 rainbow strobe, S34 mouse+window fully out, S35 burglar close-up, S37 button sunburst, S38 cape spread, S39 ducked+flicker, S41 tightened beams); all A re-times hold their events (S34 slam motion blur, S39 mid-spill droplets); no halted-photo-then-move cuts; mouths closed or backs to camera; no legible in-clip text; kinetic on SONG_WORDS times, .ass byte-identical to Q1. NOTE (disclosed, not a defect): S33 flash peak re-times 64.69s (v2, 1.60x slow) → 63.96s (v3, 0.70x fast) — same chant line, accent lands on "a"/"bet," instead of "lost".
- CHAT COPY v3 DONE 2026-11-12 ~05:52 EST (q2/chat_copy_v3.py): masters/mv12_micro_soft_lost_the_bet_v3_16x9_50mb.mp4 — 38,182,616 B (36.4 MB), 2741f, 114.21s, 1280x720 24fps h264+aac, md5 847bdaaa9f08e4bc60718ca4a74cf252; audio md5 == house 11a1ce52a8783ae5008e7ff6d4ac3e7a.
- Q2 COMPLETE 2026-11-12 ~05:52 EST: v3 master delivered to disk (house + chat copy). Bridge density FAIL closed: 40.5 → 72.1 cuts/min (target 66). Gates ALL PASS, motion PASS, eye-read PASS. Disclosed carry-overs: 13f near-still @38.58s S20 settle; S33 flash peak re-times 64.69→63.96s; first word of each line mid-fade faint at exact line-start frames (Q1 carry-over). NO commit, NO delivered flag (parent writes it).
