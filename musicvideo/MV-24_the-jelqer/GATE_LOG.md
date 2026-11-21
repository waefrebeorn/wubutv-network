# MV-24 "The Jelqer" — GATE LOG

Master: `masters/mv24_the_jelqer_16x9.mp4` — 1280×720, 24fps, **exactly 3994 frames**, 166.4167s, 82,691,799 bytes.
Track: 166.400s measured (153.0 BPM). Target = round(166.400 × 24) = 3994f — HIT EXACTLY.
Spend: **28 / 40** generation calls (26 landed, 1 generator refusal, 1 transient tool error retried at no cost). Zero 429s.

## Gates

- **G1 Cast/identity — PASS.** OLD ELI and THE DRIFTER locked from in-project generated refs (REF_ELI / REF_DRIFTER / REF_TOWN, eye-verified). Every take eye-checked against the locks. One recast caught and rerolled (S08 t2 clean-shaven → t3 restored). Eli's hat tone drifts lighter in bright midday takes (S12/S19) — disclosed nit, face/beard/jacket/guitar constant.
- **G2 Zero legible text — PASS after 3 rerolls.** S07 t1 ("SALOON"), S08 t1 ("STORE"/"SALOON"), S18 t1 ("DUSTWATER" at full-res) rejected on this axis alone and rerolled with blank-fronts clause / square-on framing / low angle. Final master takes carry no legible words; wanted posters are blank weathered paper (S05 verified sheet-by-sheet). Residual texture nits disclosed below.
- **G3 Motion law — PASS.** Every take's motion measured (frame-diff mean 6.0–31.2, near-dup runs ≤0.25s except S16's 0.5s sky stretch, disclosed). Master freezedetect (n=-60dB, d=0.5s): **ZERO freeze events**. All cuts land on moving frames; S01 opens mid-gallop, S23 closes mid-gallop.
- **G4 First-3-seconds — PASS.** S01 head-on gallop through golden dust from frame 1, rider grows to fill frame — no ramp, no titles.
- **G5 Adults only — PASS.** Every take eye-checked; all crowds are grown adults (40s–60s per vehicles). S04 crowd verified at full resolution (adult women in bonnets, older men; no minors). No family stagings anywhere. L06–L09's lyric content is carried by Eli + grown-adult crowd reactions only; no person depicted as a victim.
- **G6 SFW — PASS.** The crude sheet ships as a clean comedy western: L03 → lariat twist (S08), L16 → neckerchief wring (S20), L11 → firework burst (S16), L12 → boot polish, L13 → empty jail cell (S17). Nothing crude or sexual is depicted on screen, ever. On-screen subtitle text keeps the sheet's own asterisk censorship verbatim.
- **G7 Wrong-lyric — PASS.** Singing takes: S07 t2 0.933 · S11 1.0 · S12 1.0 · S19 0.933 · S21 0.778 (hand-check pass: ASR compresses the 4× "I tell ya" repeats; the take's four-stage lean-in visual confirms full delivery) · S22 1.0. Wordless slots verified silent by ASR (two ASR-noise overrides logged: S09 stray "you.", S13 "God." stretched over 4.2s of a silent take — MV-25 noise class, mouths closed on eye-check).
- **G8 Sync/warp — PASS.** Phrase-level smooth setpts warps from per-take ASR word anchors: S07 k 0.725, S11 k 0.904, S12 k 1.146, S19 k 0.740, S21 k 0.957, S22 head k 1.0 + W k 1.200. Grey-zone speed-ups (S07/S19 ≈0.73) disclosed — same class MV-26 shipped. No word warped out of caps; no bad-word freezes needed (the one unlandable line, L04+L05, is a refusal cover — see G9).
- **G9 Generator refusal — RULE APPLIED.** The S09 singing vehicle (L04+L05, incl. the sheet's asterisk-censored "Qu**f") was refused once by the generator and was NOT re-fired or reworded. The window (72.72–76.52s) ships as a wordless event cover: Eli strums and points his guitar at the crowd. The lines remain fully present in the burned karaoke subtitles and the mov_text track.
- **G10 Subtitles burned in — PASS.** Word-timed karaoke ASS (MV-2 v7 house style: bottom-center bold white on semi-transparent black bar, current word yellow), 155 word events / 42 lines, display text = SHEET words mapped onto ASR timing slots (asterisk censorship intact). Verified on master grabs at L01, L06, L11, L19. mov_text track also present (42 cues).
- **G11 Master spec — PASS.** One 16:9 master, CRF 18 proven by SIZE DIFFERENTIAL: master 82,691,799 B vs identical-chain CRF-23 encode 41,614,142 B = **1.99×** (SEI string not used — this VM's x264 always writes crf=23.0). Audio = track.mp3 re-encoded AAC LC 48kHz stereo 192k (never stream-copied). Faststart on. "~ WuBu ~" gold bug bottom-right verified EXACT on head (2s), mid (83s) and tail (164s) grabs.
- **G12 Segment/joined law — PASS.** Every segment built setpts-first → fps=24, each asserted for BOTH frames and duration (24/24 exact). joined.mp4 probed BEFORE encode: 3994 frames AND 166.4167s = segment sums. ONE-WRITER: ps-check showed no other ffmpeg on the path before the master encode (the CRF-23 proof was re-run solo after a service restart killed its first attempt mid-run; the master itself had already completed with RC=0 and probed clean).
- **G13 Event doctrine — PASS.** 23 distinct named events, none repeated within the build, none repeating MV-22/23/25/26 events or stagings; all 23 appended to WUBUMV's USED_EVENTS.md at plan lock. Declared bookend rhyme S01 (charge at camera) → S23 (gallop away) verified on master grabs.
- **G14 Chat copy — PASS** (see COMPLETION.json for md5/size; ≤50 MB, audio stream-copied from the master).

## Disclosed flaws (all shipped knowingly)

1. **S09 is a wordless cover, not a singing take** — generator refusal on L04+L05 (G9). The tale's promise beat plays as Eli's strum-and-point; lyrics carried by subtitles.
2. **S21 ASR repeat compression** — G7 0.778 by word-set; delivery confirmed by the four-lean visual + hand-check.
3. **Grey-zone warps** — S07 k 0.725 and S19 k 0.740 speed the picture up ~1.35× (takes sang slower than the song); inside the disclosed MV-26 class.
4. **S04** — ejection plays through a plain door, not saloon swing doors; a small distant sign board with illegible texture appears ~7s (no readable word).
5. **S16** — 0.5s near-static sky stretch while the rocket climbs (take-level M6 flag class; master freezedetect still zero); frame-1 background carries faint poster/sign texture, no readable word.
6. **S17** — in the first ~2s a figure is visible behind the cell bars before the Sheriff opens the empty cell (staging quirk; the open→empty→head-scratch gag reads clearly).
7. **S18 t2** — duplicate-hat nit: one hat remains on the jail steps while the Drifter dons another fished from the trough; poster sheets on the left wall carry pseudo-print texture (no readable words).
8. **S21 light** — reads dusk-warm rather than midday bright (light-arc nit between S20 and S22).
9. **S23 tail** — a second small distant rider is visible in the sunset flats in the closing seconds (background figure, not scripted).
10. **S03** — the "scatter" reads as ducking/cowering more than full comic dives.
11. **Patter captions** — the track's two spoken "Thank you" stage-patter bits (3.70s, 34.78s) are captioned as performed; they are not sheet lines.
12. **Eli's guitar headstock** carries a tiny illegible brand mark inherited from the reference still (still-only nit, unreadable at master scale).
