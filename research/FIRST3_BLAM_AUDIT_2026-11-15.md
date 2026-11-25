# FIRST-3 BLAM AUDIT — openings measured, causes diagnosed, gate proposed

**Date:** 2026-11-15 · **Scope (corrected):** the user's first-3-seconds order was about **every video — the new-era SHOWS first of all**. The five pilots are the primary evidence set. Their audio is *generated clip audio*, not a Suno track, so for the shows the causes live in generation behaviour and assembly choices. MV-18…21 appear only in a demoted comparison appendix (§5). The BLAM GATE itself (§4) is universal — it binds every video we ship — but its examples and fix menu are written show-first.

**Method.** Per master: audio RMS envelope in 100 ms windows over the full runtime (median = the video's own reference loudness); time to reach 50 %/90 % of median (sustained 2 windows); leading near-silence; HF transient-burst counts in 0–1.5 s vs a mid-video 1.5 s control window (crackle proxy); frame-to-frame MAE at 320×180 gray in 0.25 s buckets for 0–3 s vs the 3–10 s baseline; first hard cut; and a 0–3 s contact strip (frames at 0 / 0.5 / 1 / 1.5 / 2 / 2.5 / 3 s) read by eye. Raw numbers: `measurements.json` beside this report. Limits in §6 — read them before quoting any number.

---

## 1. The pilots — per-video measurements

| Pilot | Audio t50 / t90 | Lead silence | Head level (0–1 s vs median) | HF bursts head vs control | Motion 0–0.5 s (ratio vs 3–10 s baseline) | Motion shape 0–3 s | First impact event |
|---|---|---|---|---|---|---|---|
| **P1 THE MACHINE** | **3.1 s / 4.1 s** | 0.0 s | **≈ −47 dB vs −38.1 median (≈9 dB under)** | 11 vs 25 (not head-concentrated) | 1.82 (0.81×) | flat, low (1.9→2.5) | **none in 0–3 s** — first speech ≈5 s |
| **P2 THE TENTH SECOND** | 0.1 s / 1.5 s | 0.0 s | −36.9…−35.2 vs −33.5 (≈ at level) | 0 vs 15 | **10.28 (3.01×)** | opens hot, decays (11.7→7.3) | **frame 0** — courier mid-stride, parcel offered |
| **P3 THE ROSTER** | 0.0 s / 0.0 s | 0.0 s | −27.4…−28.5 vs −34.6 (hotter than median) | 0 vs 0 | 1.81 (0.82×) | **ramps 0.56 → 9.89** | ≈1.0 s — hand enters over the circled name |
| **P4 THE COUNT** | 0.0 s / 0.0 s | 0.0 s | −17.2…−19.0 vs −28.7 (much hotter) | 17 vs 27 (speech transients on a loud bed — **not crackle**) | **0.65 (0.10×)** | **monotonic ramp 0.53 → 7.74** | **none in 0–3 s** |
| **P5 THE LAST SEAT** | 0.7 s / 0.7 s | 0.0 s | first 0.5 s −47.7 vs −38.3 (≈9 dB under), hit at ≈1.0–1.5 s | **51 vs 15 (head-concentrated, noise-flatness 0.44)** | 2.86 (0.71×) | leap at f0, dip at apex, aisle advance | **frame 0** — dancer mid-leap down the lens |

Pilots contain **no cut in 0–3 s by construction** (unit 1 is a single 10 s take; the first cut is the unit joint at 10.0 s). For episodes, the first impact must therefore be an *in-shot* event or a planted graphic event — nothing in the current format supplies one by default.

### What the strips show (0–3 s, by eye)

- **P1 THE MACHINE** — frame 0 is the doctrine image (operator at the console, monitor cat mid-snarl, mouth wide, in silence) — and then the shot simply *holds*: a slow push-in on a static tableau for three full seconds. The image BLAMs; the timeline does not. With the audio bed sitting ≈9 dB under the episode median and the first line ≈2 s beyond the window, the opening reads exactly as the user described: quiet, then slow.
- **P2 THE TENTH SECOND** — the one pilot that opens at speed. Courier is mid-stride at frame 0, parcel extended; the push-in closes distance continuously; motion in the first half-second is 3× the episode baseline. This is the model opener, and it was not an accident: its PEAK panel depicts a body already in motion.
- **P3 THE ROSTER** — frame 0 is the held roster page (legible, sound-off readable, KEEPER circled) — a still. A hand enters at ≈1.0 s and the camera wakes up; MAE climbs from 0.56 to 9.89 across the window. One dead second, then the episode starts.
- **P4 THE COUNT** — a wide, static counting-hall tableau. Almost nothing moves for ≈1.5 s; the MAE curve rises monotonically for the entire 3 s (0.53 → 7.74) — a camera easing in from rest, the purest "slow" in the set. Its audio, ironically, is the loudest from frame 0 of any pilot: the failure is entirely pictorial.
- **P5 THE LAST SEAT** — frame 0 is a genuine BLAM picture (dancer mid-leap down the lens, usher's gloved hands and tickets in the foreground). But the first second of *audio* is a quiet, artifact-textured bed (51 HF transients, spectral flatness 0.44 = noise-like) before the hit lands at ≈1.0–1.5 s. Picture passes, soundtrack crackles.

---

## 2. Diagnosis — why the shows open with a crackle or a slow

### (a) Audio properties of what we ship

1. **Episode masters are quiet overall, and their heads are quieter.** Pilot medians sit at −38.1 / −33.5 / −34.6 / −28.7 / −38.3 dBFS. There is no loudness pass on episode masters; whatever level the generated clips came back at is what ships. On a phone speaker, an opening already ≈9 dB under its own episode median (P1, P5) is effectively silence with texture.
2. **P5's crackle is real and head-concentrated:** 51 HF transient bursts in 0–1.5 s vs 15 in the control window, on a bed ≈9 dB under median, with noise-like spectral flatness (0.44). That is the generated take's ambience/artifact texture, shipped at the natural head of the take.
3. **P1's problem is level and emptiness, not crackle** — bursts are *not* head-concentrated (11 vs 25). Precision matters: the fix for P1 is an earlier sound event and a level pass, not de-crackling. Likewise **P4's 17 head bursts are speech transients on a loud bed, not crackle** — nobody should "fix" P4's audio; its failure is the picture.

### (b) Generation behaviour

4. **Takes ramp motion in from rest.** P3 (0.56 → 9.89) and P4 (0.53 → 7.74, monotonic across all 3 s) show the generator easing into the shot over ~2 s — the opening frame is a held composition and movement accrues. Where the PEAK panel depicted a body *already at peak action* (P2's mid-stride offer, P5's mid-leap), the take opens at speed (3.01× and frame-0 impact). The generator can open hot; it does so only when the anchor image is itself a peak, not a tableau.
5. **Generated clip audio starts on room tone; the designed sound lands late.** P1's first speech arrives at ≈5 s (t50 3.1 s / t90 4.1 s against its own median); P5 idles ≈1 s before its hit. The vehicles design a *picture* for frame 0 but no *sound event* for the first second, so the take's ambient head is what the viewer hears.
6. **The frame-0 doctrine beat is bought with stasis.** The FIRST-SECOND DOCTRINE demands a legible frame 0; in P1 and P4 that legibility was achieved with a held tableau, and the generator then holds it. Legibility and motion were treated as a trade; P2/P5 prove they are not — a mid-action frame is both legible and moving.

### (c) Assembly choices

7. **Every master starts at the natural head of its first take.** No head trim, no start-on-the-hit placement, no opening accent anywhere in the set. P5's crackly second and P3's dead second were both *inside* their takes and both shippable-around — assembly shipped them.
8. **Nothing is planted in 0–3 s.** The episode format puts the first cut at 10 s and (outside the frame-0 image) schedules no event in the opening window: no graphic device fires early (the Method C systems exist but were not aimed at the opening), no sound accent is laid, no impact frame is placed. The opening is whatever the first take happens to do first.
9. **AAC priming is NOT a cause** — measured head offset is sub-frame (≤ ~50 ms); the dead time in these openings is seconds of real content, not codec padding. Stated so it is never chased.

---

## 3. Verdict against the proposed gate (§4)

| Pilot | A1 onset | A2 dead head | A3 head level | A4 crackle | V1 motion | V2 no-ramp | E1 impact ≤1 s | **BLAM?** |
|---|---|---|---|---|---|---|---|---|
| P1 THE MACHINE | ✗ 3.1/4.1 s | ✓ | ✗ −9 dB | ✓ | ✓ | ✓ | ✗ none | **NO** |
| P2 THE TENTH SECOND | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ f0 | **YES** |
| P3 THE ROSTER | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ ramp | ✓ ≈1.0 s | **NO** |
| P4 THE COUNT | ✓ | ✓ | ✓ | ✓ | ✗ 0.10× | ✗ ramp | ✗ none | **NO** |
| P5 THE LAST SEAT | ✓ | ✓ | ✓ | ✗ 51 vs 15 | ✓ | ✓ | ✓ f0 | **NO** (audio) |

**One of five pilots BLAMs.** The user's judgement is measured, not vibes: the shows open on held tableaux, ramping cameras, room-tone heads, and — once — literal crackle.

---

## 4. THE BLAM GATE (proposed spec — paste-ready)

> ## BLAM GATE — the first 3 seconds of every shipped video
>
> Measured on the finished master, first 3.0 s. All bars must pass; a single fail blocks delivery until fixed in assembly or re-fired. Measurement: 100 ms RMS windows against the video's own median loudness; frame-MAE at 320×180 gray; HF burst count vs a mid-video control window; contact strip at 0/0.5/1/1.5/2/2.5/3 s read by eye.
>
> **Audio**
> - **A1 Onset:** time to 50 % of median loudness ≤ 0.5 s; time to 90 % ≤ 1.5 s (sustained 2 windows).
> - **A2 Dead head:** leading near-silence (windows under max(−50 dBFS, 5 % of median)) ≤ 0.2 s.
> - **A3 Head level:** mean level of 0–1.0 s within 6 dB of the video's median — or a designed accent transient placed at ≤ 0.5 s.
> - **A4 Crackle:** HF transient bursts in 0–1.5 s ≤ 2× the count in a mid-video 1.5 s control window. If the source audio's head itself carries a crackle texture (head bursts > 3× control), the master may not open on that head — start past it or cover it (see fixes).
>
> **Picture**
> - **V1 Opening motion:** mean frame-MAE over 0–0.5 s ≥ 0.6× the video's 3–10 s baseline MAE.
> - **V2 No ramp-from-rest:** MAE of the first 0.25 s bucket ≥ 50 % of the strongest bucket in 0–3 s, **or** ≥ 4.0 absolute (already moving in absolute terms).
> - **E1 First impact ≤ 1.0 s:** a named impact event lands by 1.0 s — a subject at peak action, a hard cut, a graphic-device event, or a sound accent locked to a picture event — verified on the contact strip. A legible-but-static frame 0 does **not** satisfy E1.
> - **E2 (montage formats / MVs):** first hard cut or graphic event ≤ 3.0 s. Episode formats are exempt from the cut (unit structure), never from E1.
>
> **Fix menu — generation (shows first)**
> - The U1 PEAK panel must depict the **impact moment itself** (mid-leap, mid-stride, mid-shout), never a tableau, portrait, or establishing wide. If the panel could hang on a wall, it is not a peak.
> - U1 vehicles open *in medias res*: the first sentence of the prompt describes motion already at full speed ("already sprinting / mid-fall / slamming"); ban "stands in", "sits at", "a wide shot of" as U1 openers.
> - Every U1 vehicle names a **sound event inside the first second** (a slam, a stamp, a bell, a shouted word) — speech lands late by generator habit, so the designed early sound must be an *event*, not a line.
> - Dialogue for U1 is written to land wherever it lands (standing lesson); the opening's audio job belongs to the event, not the line.
>
> **Fix menu — take selection**
> - Run the onset/MAE measurement on candidate U1 takes before assembly. Reject takes that ramp (V2 fail) or idle (A1/A4 fail) when another take passes; a ramp take may still serve later units.
> - Prefer the take whose frame 0 is already the peak frame; never select a U1 take for its *later* content.
>
> **Fix menu — assembly**
> - **Start on the hit:** the master opens at the first BLAM event. Trim dead/crackly/ramping head without ceremony — the take's natural head has no rights. (P5's crackle second and P3's dead second were both trimmable.)
> - **Plant the graphic event early:** on episodes, fire the show's Method C device inside 0–1.0 s on U1 (the Cull Clock snap, the Dead Channel spike, the Wet Circle completing) — a graphic event is a designed impact the generator cannot ramp away from.
> - **Post sound accent:** when source audio cannot satisfy A1/A3, lay one designed transient (thump, stamp, tick, sting) exactly on the impact frame. One accent, on the frame, never a fade-in.
> - **Loudness pass on episode masters:** normalize toward a consistent house band so "at level" on paper is audible on a phone; never ship a master whose median sits in the −38 dBFS basement.
> - **Never** fade audio in at the head, never open on a fade-from-black, never let a title or bug carry the opening — the event carries it.

---

## 5. Appendix (demoted): MV-18…21 as comparison

Same measurements, for calibration only — the directive was not about MVs, and MV audio is the Suno track shipped as-is, so their causes split differently.

| MV | t50 / t90 | Lead silence | Bursts head vs control | Motion 0–0.5 s (ratio) | First cut | BLAM? |
|---|---|---|---|---|---|---|
| MV-18 What's a Sigma? ~Mom | 0.0 / 0.7 s | 0.0 s | 0 vs 0 | 2.61 (1.00×, flat absolute) | **6.54 s** | NO — talking-head stasis, E2 fail |
| MV-19 Confused NPC | 0.0 / 0.0 s | 0.0 s | **141 vs 0** | 5.50 (1.14×) | 2.0 s | NO — A4: crackle head |
| MV-20 Laundry Life | 0.0 / 0.4 s | 0.0 s | 0 vs 0 | 4.66 (0.66×) | 4.5 s | **YES** (E2 advisory only) |
| MV-21 Wowie Pants That Fit | **2.6 / 24.7 s** | **1.9 s** | 0 vs 0 | 2.07 (0.29×) | 2.12 s | NO — worst opening in the set |

Two findings worth keeping: **MV-19's crackle is a track property, proven** — track.mp4's own head carries 151 bursts vs 0 at 30 s, and the master's head envelope matches the track's head dB-for-dB (−14.6 / −16.2 / −15.8 …); assembly shipped the track's intro texture untouched. **MV-21's silence is also the track's** (its head ramps −57.3 → −23.0 dB across 3 s) — but the *decision to open the picture on a motionless folded garment in that silence* was ours: first impact at 2.12 s. For MVs the gate's remedy is placement (open on the track's first hit, or cut the picture's impact to ≤1 s regardless of the track's intro), never re-recording the track.

---

## 6. Honest limits

- **Crackle detection is a proxy, not a listening test.** HF transient density also fires on legitimate percussion and speech transients (see P4). The control-window comparison disciplines it, but every A4 flag still deserves a 2-second human ear check before a fix is ordered.
- **MAE absolutes are scale-bound.** All MAE values were measured at 320×180 grayscale; the gate's ratios are portable, the single absolute floor in V2 (4.0) is calibrated to this pipeline and must be re-based if the measurement size changes.
- **Cut detection** uses a spike threshold (max of 4× baseline median, baseline + 25); dissolves and soft transitions can pass under it. Pilots' first cut (the 10 s unit joint) is outside the audit window by design.
- **t50/t90 reference is each video's own full-runtime median RMS** — long quiet passages pull the median down and *flatter* the numbers (MV-21 still failed at 24.7 s).
- **Event timings from contact strips are ±0.5 s** (0.5 s sampling). "≈1.0 s" means the event is present in the 1.0 s frame and absent at 0.5 s.
- Nothing in this audit re-measures beyond 10 s; a video can pass the gate and still sag at second 4. The gate governs the opening only, as ordered.
