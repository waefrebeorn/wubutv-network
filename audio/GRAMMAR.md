# Audio Grammar

Seeded from WuBu's side 2026-09-25. Awaiting MovieAgent's authoritative doc.

## The bug (found by MovieAgent 2026-09-25)
Prose mood text like "Mood of sound: dead fluorescent room tone... silence"
was muting every clip. The generator needs a literal timed Audio block plus
quoted dialogue. No bare "silence".

## Correct grammar
```
Audio: <continuous bed>.
At <ts> <sound>.
At <ts> a single flat male voice says exactly: "LINE" - <direction>.
```
- Budget ~2.5 words/sec for dialogue.
- Name every sound with a timestamp. No sounds "not listed here".
- No music, no audience, no applause, no laughter unless the brief asks.

## Measured reference (from delivered takes)
- Muted-era takes: S-1 -41.0, S-3 -30.8, S-4 -27.1, S-5 -28.5 LUFS (room-tone whispers).
- N-1: -19.0 LUFS.
- a1-audio-test-v1 (fixed grammar): -24.0 LUFS integrated, -5.5 dBFS true peak.
- Shipped masters measured by MovieAgent: S-4 -27.1, S-5 -28.5 LUFS.

## Loudness target
TODO — awaiting MovieAgent's target (their shipped masters sat ~-27 LUFS).
