# MV-8 — Lyric Timeline (measured)

Track: `track.mp4` / `track.mp3` — 187.200 s · tempo **123.05 BPM** (median inter-beat interval; beat grid in `work/beat_grid.json`, 368 beats, first beat 5.968 s; downbeats [inferred] — phase margin only 0.002, so cut on beats/hits, not bars).

**This is a chant track — there is no singing character and no mouth sync.** The sync layer for the edit is the stab/hit map (`work/CRESCENDO_MAP.md`); this timeline places the chant lines and section boundaries.

## How this was measured

Three independent witnesses, cross-checked:

1. **Whisper ASR, small model** (`SONG_WORDS.json`, 112 words) on a proper 16 kHz decode of the track — word-level times. (First attempt fed the raw 48 kHz mp3 as an array and produced 3×-slowed garbage; discarded. Chant ASR is unreliable: known mishear classes below.)
2. **Whisper ASR, tiny model** (`work/SONG_WORDS_tiny.json`) — weaker, but an independent phrase-placement witness; it corroborates Hook 1's chant phrases and confirms no vocal after ~148 s. It is deaf in quiet passages (it missed the confirmed Verse), so its silences are weak evidence.
3. **The Suno lyric-video itself** (`track.mp4`): a karaoke scroller — bold = currently sung, dim = upcoming. 94 frames at 2 s intervals were read (`work/lyricframes/`). Its alignment is Suno's own and it drifts in repetitive chant (see Dispute 3).

Confidence tags per Slopcannon `references/timeline.md`: **[confirmed]** = measured by ASR word times and/or onset/frame evidence that agrees; **[inferred]** = bracketed or single-witness; **[assumed]** = from the user's sheet only, not measurable in the audio.

## Section boundaries (measured, mapped to the user's sheet)

| Section | Start | End | Dur | Basis |
|---|---|---|---|---|
| Intro | 0.00 | 5.97 | 6.0 s | stab @0.55 + build ramp; first beat 5.968 |
| Hook 1 | 5.97 | 34.40 | 28.4 s | groove entry hits 5.96/6.44; chant ends ~34.4 (both ASR models) |
| Interlude *(not on sheet)* | 34.40 | 60.46 | 26.1 s | no chant (display parked, ASR silent); stab-dense instrumental |
| Verse | 60.46 | 65.12 | 4.7 s | ASR-exact "Sitting on the toilet" @60.46 |
| Pre-Hook | 65.12 | 67.26 | 2.1 s | snare build + fast 3-line pile-up |
| Hook 2 | 67.26 | 105.94 | 38.7 s | ASR hook line @67.26 → Drop's "Wipe" @105.94 |
| Drop | 105.94 | 120.40 | 14.5 s | "Wipe..." @105.94 → Final Hook L1 @120.40 |
| Final Hook | 120.40 | 146.00 | 25.6 s | ASR 120.40 → last word "forever" ends ~146.0 |
| Outro (instrumental) | 146.00 | 187.20 | 41.2 s | no vocal in either ASR; sheet's outro stabs inside ~176.6–183.3; decay from ~184.3 |

## Per-line times

### Intro (0.00–5.97) — instrumental [confirmed]
Stab **0.546**, second hit **2.519**, then a steady level build (≈ −33 → −20 dBFS) into the groove-entry hit pair **5.96 / 6.44**. No chant (nothing bold in the lyric video 0–7 s; ASR silent).

### Hook 1 (5.97–34.40) — chant, dense; line boundaries ±~1.5 s
| Line | Start–End | Tag | Evidence |
|---|---|---|---|
| Wipe and it's still there | ~6.4–10.5 | [inferred] | groove hit 6.44; highlight on by t=8; tiny phrase 8.0–10.46 |
| Wipe and it's still there | ~10.5–14.2 | [inferred] | tiny phrase 12.32–14.16; display cue-bold from t=8 |
| Paper comes back dirty | ~14.8–19.1 | [inferred] | tiny hears "…comes back dirty" 16.38–19.14 ("back" p=1.00); display bold front ~13–16 |
| Brown brown (Still there) | ~19.1–21.5 | [inferred] | display: "[Short String Hit] Brown" bold @ t=18–20 |
| Wipe and it's still there | ~21.5–27.5 | [inferred] | display bold t=22–26; tiny phrase 23.78–27.52 |
| Wipe and it's still there | ~27.5–31.8 | [inferred] | tiny 28.30–30.46; display t=26–30 |
| Phantom residue stays | ~30.5–34.0 | [inferred] | display bold t=30–32; tiny mangled phrase 31.82–34.44 |
| Brown + [Orchestral Hit] | ~33.0–34.4 | [inferred] line / [confirmed] hit | "Brown" bold alone @ t=34; hit_major pair **33.35 / 33.85** |

### Interlude (34.40–60.46) — instrumental [confirmed]
Lyric display parks on "Brown" for the whole stretch; both ASR models hear no chant. 21 tiered hits (6 major) — the arrangement stabs hard here (majors at 46.46, 47.91, 48.40, 48.88…). The sheet places Hook 1's trailing "(Brown brown)" backing in this zone; no intelligible chant is measurable, so the edit should treat it as instrumental.

### Verse (60.46–65.12)
| Line | Start–End | Tag | Evidence |
|---|---|---|---|
| Sitting on the toilet | 60.46–62.20 | [confirmed] | ASR small, exact words; display ✓ |
| Wipe once | 62.20–64.02 | [confirmed] | ASR words (Wipe 63.00, once →64.02); display "[Light Rimshot] Wipe once" bold @ t=62 |
| Still brown | 64.02–65.12 | [confirmed] | ASR words 64.08/64.72; display bold @ t=64 |
| (Phantom) backing | ~64–65 | [assumed] | on the sheet; not separable in ASR |

The Verse carries the track's single strongest hit: **63.32 (strength 1.907)** — plus majors at 61.87, 63.81, 64.76.

### Pre-Hook (65.12–67.26) — fast pile-up, brackets overlap
| Line | Start–End | Tag | Evidence |
|---|---|---|---|
| Wipe again | ~65.1–67.3 | [inferred] | ASR small heard it inside the mangled segment "Santa, wipe, wipe again" (words: wipe 66.38, wipe 66.64, again 66.82–67.26); [Building Snare] runs under it |
| Still there | ~65.5–67.9 | [inferred] | display: "[Brass Accent] Still there" bold @ t=66 |
| (Never clean) | 68.90–69.96 | [confirmed]* | ASR heard "Never cleaned" — normalized; lands across the Hook 2 boundary as a backing line |

### Hook 2 (67.26–105.94)
| Line | Start–End | Tag | Evidence |
|---|---|---|---|
| Wipe and it's still there | 67.26–68.90 | [confirmed]* | ASR "Wipe in the stool, there" (systematic mishear); display current @ t=68–70 |
| Wipe and it's still there | 71.00–72.90 | [confirmed]* | ASR 71.00–72.90; display @ t=72–74 |
| (fragment — line tail/pickup) | 74.89–76.02 | [inferred] | ASR fragment "Wipe in the stool" |
| Endless wipe forever | 77.56–80.48 | [confirmed]* | ASR "And there's water forever" (mishear class: "water" = "wipe"); display line starts ~75–77 |
| Brown brown (Still brown) | ~80.5–81.7 | [inferred] | display: Brown bold @ t=80; ASR catches no "brown" here |
| Wipe and it's still there | 81.66–83.74 | [confirmed]* † | ASR word probs 0.86–1.00 — **display disputes (shows a park); see Dispute 3** |
| Wipe and it's still there | 85.96–88.26 | [confirmed]* † | ASR word probs 0.52–1.00 — **display disputes; see Dispute 3** |
| (Still brown) + [Orchestral Hit] lead-in | ~88.3–93 | [inferred] | display shows this annotation pair heading the next sung line; ASR "Yeah" 90.66–91.50 ≈ the shout |
| Wipe-line material (display's L5/L6 slot) | ~89.5–97 | [inferred] | display bolds it t=90–96; if the 81.7/86.0 ASR lines are L5/L6, this is display lag or extra repeats — unsettled, see Dispute 3 |
| Phantom wiper never stops | ~97.0–105.5 | [inferred] | ASR fragments 97.02–99.68 (low prob) + "…never stop" 102.52–105.46; display bold front @ t=96–98 |
| Brown (Brown brown) | ~104–107 | [inferred] | display: "Brown" bold @ t=104–106 |

### Drop (105.94–120.40)
| Event | Time | Tag | Evidence |
|---|---|---|---|
| Wipe… | 105.94–106.36 | [confirmed] | ASR lone word "Wipe" |
| [Orchestral Hit] + **STILL THERE!** | hit pair 112.25 / 112.72; shout ~112.7–114.5 | [inferred] | the gap's strongest events (112.72: strength 1.04, peak −4 dBFS); no other candidate in 106–120; shout itself not ASR-detected |
| (Brown brown) | — | [assumed] | sheet only; nothing measurable separates it |
| [Silence – half bar] | — | **NOT PERFORMED** | fine-RMS scan: no dip below −38 dBFS ≥0.25 s anywhere after the leader; Drop level is flat (~−16.5 dBFS). See Dispute 1 |

### Final Hook (120.40–146.00)
| Line | Start–End | Tag | Evidence |
|---|---|---|---|
| Wipe and it's still there | 120.40–122.80 | [confirmed]* | ASR 120.40–122.80; display bold @ t=122; hit cluster 121.42/121.78 |
| Wipe and it's still there | ~123–127 | [inferred] | display bold @ t=124–126 |
| Paper comes back dirty | 127.44–130.50 | [confirmed] | ASR exact words; display bold @ t=126–128 |
| Dirty (echo) | 130.50–132.14 | [confirmed] | ASR |
| Brown brown (Brown brown) | ~130–136.34 | [inferred] | display: Brown bold @ t=130; ASR brown run 133.08–136.34 (5 browns) = backing echoes |
| Wipe and it's still there | 136.34–139.28 | [confirmed]* | ASR; display bold @ t=136–138 |
| (Still there) Wipe and it's still there | 139.28–142.00 | [confirmed]* | ASR; display @ t=140 |
| (Phantom wipe) Endless wipe forever | ~142.66–146.00 | [inferred] | ASR segments 142.66–144.94 + 144.94–146.00 are mangled but land exactly on this slot; display reaches "forever" by t=144; last sung word **"forever" ≈ 144.9–146.0** |

### Outro (146.00–187.20) — instrumental [confirmed]
No vocal after ~146 in either ASR model (tiny's last segment ends 148.0; small's 176–186 "I'm gonna" loop has zero-duration stamps and is disregarded as hallucination over the stabs). The lyric display parks on "forever" to the end. The sheet's outro stabs ([Brass Stab] / Brown / [Brass Stab]) map to the late cluster — hit_majors at **176.63** and **180.56**, stabs running to ~183.3 [inferred]. Audio decays from ~184.3 and ends at 187.2.

\* **[confirmed]\*** = ASR-measured after applying the known mishear normalization (below). The times are measured; the words are the sheet's, matched through the mishear class.

† **Dispute 3 (the timeline's one soft spot):** in Hook 2's back half the Suno display and ASR-small disagree. The display shows an instrumental park ~82–89 with the next lines at ~90–97; ASR-small hears two full hook lines at 81.66–83.74 and 85.96–88.26 with word probabilities 0.86–1.00, normal word durations, and the track's usual ~4.3 s line cadence. **I trust ASR for the existence of chant at 81.7 and 86.0** (the display's aligner demonstrably drifts in this repetitive material — it pre-bolds lines ~1 s early at the Verse and parks through the Interlude). What an ear check would still need to settle: whether those two lines are the sheet's L5/L6 sung early (making the display's 90–97 bolding a lagged echo) or extra repeats. Edit-relevant either way: **80–106 is chant-covered, not an instrumental park.**

## Disputes — sheet vs performance (report both; measurement wins)

1. **The Drop's [Silence – half bar] was not performed.** Fine-RMS scan (0.05 s windows): no dip below −38 dBFS lasting ≥0.25 s anywhere after the 0.50 s intro leader; the deepest mid-track fine window is −29.26 dBFS @ 63.7 s (a groove dip). The Drop's level is flat. **Do not plan a silence beat — there isn't one.** The only true silence in the track is the leader, 0.00–0.50 s.
2. **The Drop's micro-sequence is mostly sheet-only.** Of [Wipe…] / [Silence] / [Orchestral Hit] / STILL THERE! / (Brown brown) / [Brass Stab], the performance measurably contains: the "Wipe…" (105.94), the vocal gap, and one hit pair (112.25/112.72). The shout is placed [inferred] on that pair.
3. **Hook 2 back half** — ASR vs Suno display; see † above. Trust ASR for chant existence.
4. **The performed Outro dwarfs the sheet's.** Sheet: stab / "Brown" / stab. Performance: a 41.2 s instrumental outro containing the track's loudest 0.5 s window (174.75 s) and 11 hit_majors. The sheet's Final Hook also ends ~16 s earlier in performance than a naive read would suggest — the tail belongs to the outro.
5. **The Interlude is not on the sheet at all** — 26.1 s of stab-dense instrumental between Hook 1 and the Verse. The journey plan needs a visual idea for it; it is not dead air (21 tiered hits).
6. **Downbeats are weak evidence** (phase confidence margin 0.002). Beats are solid; bar phase is not. Cut on beats and hits.

## ASR mishear classes (small model, this track)

| ASR heard | Actually | Where |
|---|---|---|
| "in the stool" | "and it's still" | systematic, every hook line |
| "Santa" | shouted chant fragment (Phantom/Still-there region) | 65.12, 102.52 |
| "water forever" | "wipe forever" | 77.56 |
| "Never cleaned" | "(Never clean)" | 68.90 |
| "The water in this pipe" + fragments | "(Phantom wipe) Endless wipe…" region | 142.66–146.00 |
| "I'm gonna" (loop, zero-duration stamps) | hallucination over outro stabs — disregarded | 176–186 |
