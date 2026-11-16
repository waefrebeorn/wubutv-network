# MV-19 'Confused NPC' — AUDIO ANALYSIS (Stage 0, measured)

Track: track.mp3 md5 f134098b92a84d6df8fd072935cd2d87 · 153.600s.
Source video track.mp4 md5 2f932873fd9e86d819afcee48c8f580a (824×1464
vertical Suno render — reference only; master is built 16:9).

## Tempo (measured, never the claim)
- c11_mir DP beats: 269 beats, median IBI 0.5760s → **104.17 BPM**.
- c11_mir tempo head: 103.0 BPM, period 0.5825s, AC 0.6936.
- Flux autocorrelation (independent check): sharp peak at lag 0.576s
  (ac 0.690) → 104.17 BPM; half-time peak 0.288s (208 BPM) present but
  the DP median + AC agree on **104.17 BPM, beat = 0.576s**. Adopted.
- Accent map: 585 accents (S 95 / A 160 / B 192 / C 138), peak-picked
  flux, work/analysis/ACCENT_MAP.json. First S-accent at 0.16s — the
  track starts hot; frame 0 of the master must already be moving.

## Performed lyric grid (authority)
faster-whisper large-v3-turbo, int8, NO VAD, pinned "en", chunked
60s + 2s overlap, per-chunk checkpoints: 239 words, 61 segments →
grid_lines.json: **48 performed lines**, all matched (see
LYRIC_TIMELINE.md). Performed vs sheet differences (performance wins
on count/timing, sheet wins on text):
- PC1's second "What did I want" is chopped across the C1 downbeat.
- Bridge performs "What was it" ×2 (2nd as the fragment "what was"),
  "I had it" ×1 (sheet ×2), "Now it's gone" ×2 (2nd as "now it is
  gone").
- Choruses sing "just standing here" with the hook's trailing "why"
  landing on the phrase head (word-verified in the grid).
- Post-chorus "forgot why" ×2 verified at word level (56.20, 61.20);
  an overlapping 60.10 segment is a decode echo, not a third line.

## Energy arc (RMS dB rel, per-10s means)
Intro/V1 ≈ −3 to −4.5 · PC dips ≈ −5.5 (26–31s) · C1 ≈ −3.5 ·
POST sparse phrases over ≈ −2.5 backing · V2 ≈ −3 · C2 ≈ −2.6 ·
BR slightly lower, fragmented · C3 full ≈ −2.6 · OUT loudest at the
end (140–150s mean −0.87, peaks at 0.00) — the track's peak is the
outro standing, not the final chorus. Visual peak staging follows:
C3 = multiplication peak; OUT = warm acceptance at full energy.

## Structure (dadaspec read)
Loop-song architecture: intro question → verse narrative → blank
pre-chorus → hook chorus ×3 statements → sparse post-chorus echoes →
check-montage verse → pre-chorus → bigger chorus → fragmented bridge
(texture break) → final chorus → outro echoes → 4.34s instrumental
tail. The song IS a loop: every chorus restates the same failure.
Design family (intake): LOOP/RESET WORLD — the room resets around
him; each chorus is the same entrance failing again, escalated.
