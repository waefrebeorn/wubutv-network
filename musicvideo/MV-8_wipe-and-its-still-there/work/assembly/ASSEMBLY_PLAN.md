# MV-8 — Assembly Plan (Stage 6)

Built by the assembly coordinator 2026-11-07 ~23:40 EST from `SCENE_PLAN.md`
(17 scenes, 0.00–187.20), `work/TAKE_LEDGER.md` (rows 1–23, 21 KEEP), and
frame-level inspection of the takes (contact sheets + scene-detect in
`work/assembly/sheet_*.png`).

## Coverage audit

Total take footage usable vs span: every scene covered. Shortfalls are covered
by time-warp (slow), never by freeze — all slows ≤1.94x, inside the standing
warp law (never slow past 2x). No new generation: the only gaps are the
plan's outstanding 2nd clips (H2-B / FH-A / FH-B / O-A / O-B), which are
optional top-ups, not holes — the single-clip coverage plus warps tiles the
full 187.20 s.

## Segment table (song time → take, take in/out, speed)

Frame allocation: segment frames = round(end*24) − round(start*24); speed
factor = (frames/24) / (take_out − take_in). Total 4493 frames / 187.208 s
(8 ms past the 187.200 s audio — no tpad needed).

| # | Scene | Song span | Take | Take in–out | Speed | Notes |
|---|---|---|---|---|---|---|
| 1 | IN-A | 0.00–5.97 | IN-A | 0.00–5.97 | 1.000 | head trim; reveals at 0.55/2.52/~4.5 |
| 2 | H1-A | 5.97–19.10 | H1-A_c1 | 0–10 | 1.000 | cut c1→c2 at 15.97, near the 16.25 stab |
| 3 | H1-A | | H1-A_c2 | 0–3.13 | 1.000 | mountain payoff |
| 4 | H1-B | 19.10–34.40 | H1-B | 0–10 | 1.533 | continuous dive; dive transition at take 1.54 lands ~21.46, on the 21.5 SLAM |
| 5 | I-A | 34.40–45.51 | I-A | 0–10 | 1.111 | slow aerial drift |
| 6 | I-B | 45.51–60.46 | I-B_river | 0–10 | 1.000 | river flight first (storm cluster), cut at 55.51 near the 55.62 stab |
| 7 | I-B | | I-B | 0–4.95 | 1.000 | gate reveal second |
| 8 | V-0 | 60.46–65.12 | V-0 | 0–4.66 | 1.000 | head trim |
| 9 | PH-A | 65.12–67.26 | PH-A | 0–0.75 | 1.000 | handle slam (scene-detect cut @0.75) |
| 10 | PH-A | | PH-A | 2.25–3.64 | 1.000 | plunger pop (scene-detect cut @2.25); BED 0.75–2.25 DISCARDED per ledger |
| 11 | H2-A | 67.26–80.50 | H2-A | 0–10 | 1.324 | arming montage; piece landings land near majors 67.65/70.07/71.02/71.51 |
| 12 | H2-B | 80.50–93.00 | H2-B | 0–1.125 | 1.579 | bathroom hop (scene-detect cut @1.125) |
| 13 | H2-B | | H2-B | 3.208–6.167 | 1.579 | fibre hop (cuts @3.208, @6.167); PALACE 1.125–3.208 DISCARDED — empty hall per ledger |
| 14 | H2-B | | H2-B | 6.167–10 | 1.579 | neon canal hop |
| 15 | H2-C | 93.00–105.94 | H2-C_q1 | 0–2.0 | 1.000 | pull-free only; cut before the mural sweep starts (~2.5) |
| 16 | H2-C | | H2-C_q2 | 0–10 | 1.094 | full mural arc incl. ribbon re-forming + stare |
| 17 | D-A | 105.94–112.25 | D-A | 0–6.31 | 1.000 | head trim; whip-in + spirals, hold to 112.25 |
| 18 | D-B | 112.25–120.40 | D-B | 0–8.15 | 1.000 | head trim; held serpent stare |
| 19 | FH-A | 120.40–133.00 | FH-A | 0–10 | 1.260 | continuous wave-surf |
| 20 | FH-B | 133.00–146.00 | FH-B | 0–10 | 1.300 | climb; sky-break at take ~6.5 lands ~141.5, just before "forever" ~144.9 |
| 21 | O-A | 146.00–163.00 | O-A | 0–2.5 | 1.000 | loop-the-loop plays at real speed as the Outro's opening flourish (~147–148.5) |
| 22 | O-A | | O-A | 2.5–10 | 1.933 | descent / golden-city glide |
| 23 | O-B | 163.00–180.00 | O-B | 0–10 | 1.700 | slow dolly-in 163–169.8; dissolve at take ~4.5 lands ~170.7, on the loudest cluster 170.92 |
| 24 | O-C | 180.00–187.20 | O-C | 0–10 | 1.387 | SPED UP so the full arc fits: Ghost Wipe reveal → flush → vortex → F00-rhyme landing at take ~8–10 lands ~186.5–187.2. A 0–7.2 head trim would have cut the landing off. |

## Kinetic type layer (`work/assembly/mv8_kinetic.ass`)

Built by `work/assembly/build_kinetic.py` (imports `kinetic_ass.py` presets).
Noto Sans Bold, BONE #F4EEDC with CADMIUM #FFC61E accent, INK outline.
Type is an ASSEMBLY overlay only — no generated in-clip text.

- SLAM per chant line (word-pop via kinetic_ass SLAM, lower third, 300%→100%).
  V-0's three lines are full-phrase slams at fs 80 ("biggest chant type").
- CASCADE: "WIPE AGAIN" / "STILL THERE" 65.1–67.3.
- HIGHLIGHT: "PHANTOM RESIDUE STAYS" 30.5; "PHANTOM WIPER NEVER STOPS" ~97;
  "ENDLESS WIPE FOREVER" held 142.66–146.0.
- STACK: "BROWN BROWN" 19.1; "DIRTY" echo 130.50.
- "WIPE…" 105.94: custom, fs 120, stretched, held ~6 s (the only word on
  screen across the vocal gap).
- "STILL THERE!" 112.72: custom full-phrase SLAM, fs 96, 300%→100% in 150 ms,
  held to ~114.5 — the film's biggest slam.
- WIPE counter (top-left, fs 34): ticks on sheet reveals — 001@0.55,
  002@2.52, 003@~4.5, 004@6.4, 005@10.5, 006@14.8, 007@21.5, 008@27.5,
  009@60.46, 010@62.20, 011@64.02, 012@81.66, 013@85.96, jumps to
  100@93.0, 101@97.0, 102@104.0 (WIPE 100+ territory). Sleeps during
  flights. Reset gag "WIPE 001 — CLEAN" at 180.3 over the clean reveal
  (cue list says ~183, but the reveal is at take 0–1 s = song 180.0–180.7 —
  type follows the picture).
- Corner bug "~ WuBu ~" bottom-right, fs 22, ~50% alpha, 0.00–187.20.

## Disclosures / known imperfections

1. **O-A loop-the-loop does NOT land on the true peak 159.435.** The
   generated take front-loads its loop at take ~1–2.5 s; forcing it onto
   159.435 would need a ~4.5x slow of the opening flight (past the 2x warp
   law, would read frozen). The loop plays at real speed as the Outro's
   opening flourish (~147–148.5); the 159.435 peak lands on the golden-city
   glide instead. Producer call at delivery: accept, or fire the plan's
   outstanding 2nd O-A clip as a top-up.
2. **H2-B is held footage slowed 1.58x.** The scene is designed as ~3 s
   holds per hop, so the slow reads as longer holds; the neon-canal tail is
   near-static by generation. No freeze — motion continues throughout.
3. **O-B's burst/dissolve is slowed 1.70x.** The water burst reads stately
   rather than explosive; the audio cluster is a sustained loud window
   (170.9–174.7), not a single transient, so the slow release still tracks.
4. **H2-A piece landings are near — not on — the majors** (68.6/69.9/71.2/
   72.6 vs 67.65/70.07/71.02+71.51/75.35). The montage rhythm survives;
   exact per-piece alignment would need per-piece speed keyframes.
5. **PH-A is a 2-shot alternation** (handle → plunger) across 5 hits; the
   5-hit flicker-montage is approximated by one hard cut at 65.87.
6. **O-C is sped up 1.39x** to keep the F00-rhyme landing; the reveal,
   flush and vortex all play slightly brisk.
7. **H2-C uses q2 for the whole mural** (q1's mural half unused — redundant
   with q2, which has the ribbon re-forming + stare payoff).
8. **2nd clips outstanding** (plan): H2-B / FH-A / FH-B / O-A / O-B — single
   clips + warps cover their spans; top-ups would add variety, not coverage.

## House master

`masters/mv8_wipe_and_its_still_there_16x9.mp4` — libx264 preset medium,
CRF 18, yuv420p, 1280x720, 24 fps, faststart; audio AAC 48 kHz stereo
192 kbps re-encoded from track.mp3 (the Suno track, sole master audio).
Chat copy (if house > 50 MB): same cut, video-only bitrate-capped
re-encode, AAC audio copied untouched.
