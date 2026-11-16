# MV-15 "Unread DMs" — LYRIC TIMELINE (Stage 1, measured)

Method: ASR word grid (faster-whisper large-v3-turbo int8, cpu_threads=2,
NO VAD, chunked 60s+2s — work/analysis/SONG_WORDS.json, 310 words) as the
timing authority; Suno lyric video (track.mp4 frames) as text arbiter where
ASR garbles under distortion; sheet (lyrics.txt) as base text. Performed
words EXCEED the sheet in the breakdowns (user directive 1) — every extra
below is measured, not assumed. Beat grid: 150.0 BPM, period 0.400s,
phase 0.360s (c11_mir, AUDIO_ANALYSIS.md). All times [confirmed] measured
unless tagged.

## Section table

| # | Section | Start | End | Dur | Notes |
|---|---------|-------|-----|-----|-------|
| 1 | Chorus 1 (cold open) | 0.00 | 25.04 | 25.04 | Full chorus at 0s — no intro |
| 2 | Verse 1 | 25.04 | 38.54 | 13.50 | Ad-libs (yeah)/(what)/(uh) at line ends |
| 3 | Pre-Chorus 1 | 38.54 | 44.80 | 6.26 | Performed: extra "Just mute it" tail |
| 4 | Chorus 2 | 44.80 | 56.36 | 11.56 | Compressed lines, chops interleaved |
| 5 | Post-Chorus (chop field) | 56.36 | 76.34 | 19.98 | Hook fragments + one full hook pair |
| 6 | Verse 2 | 76.34 | 89.46 | 13.12 | Ad-libs at line ends |
| 7 | Pre-Chorus 2 | 89.46 | 96.76 | 7.30 | Sparser chants (see line note) |
| 8 | Chorus 3 | 96.76 | 123.02 | 26.26 | Lines + chop fields; breath 123.02–124.72 |
| 9 | Bridge (breakdown) | 124.72 | 134.70 | 9.98 | "200" stutter chops — the named breakdown |
| 10 | Final Chorus | 134.70 | 162.50 | 27.80 | Densest; chop breakdown 2 at 146.70–153.10 |
| 11 | Outro | 162.50 | 173.61 | 11.11 | Words end 172.00; tail music 172.00–173.61 |

## Line table (performed text; sheet differences in **bold**)

| Line | Section | Start | End | Performed text |
|------|---------|-------|-----|----------------|
| L01 | C1 | 0.00 | 5.68 | The group chat has 200 unread and I'm not opening it |
| L02 | C1 | 5.68 | 12.08 | The group chat has 200 unread and I'm not opening it |
| L03 | C1 | 12.08 | 18.48 | **CHOP BREAKDOWN: "200 unread" ×2, "I'm–I'm not opening it", "I'm not opening it" (sheet line 3 fragmented into pitch chops)** |
| L04 | C1 | 18.48 | 25.04 | The group chat has 200 unread and I'm not opening it |
| L05 | V1 | 25.04 | 28.74 | Phone lights up and I freeze on the spot (yeah) |
| L06 | V1 | 28.74 | 31.90 | 200 messages and I already forgot (what) |
| L07 | V1 | 31.90 | 35.34 | If I open it now I'll be stuck for an hour (uh) |
| L08 | V1 | 35.34 | 38.54 | So I'm leaving that badge like a nuclear power |
| L09 | PC1 | 38.54 | 41.02 | Don't open / Don't open |
| L10 | PC1 | 41.02 | 43.42 | Just mute it / Just mute it |
| L11 | PC1 | 43.42 | 44.80 | **Just mute it (extra performed repeat — not on sheet)** |
| L12 | C2 | 44.80 | 50.44 | The group chat has 200 unread and I'm not opening it |
| L13 | C2 | 50.44 | 56.36 | Hook line 2 **compressed + chopped** (fragments: "the group chat has 200 unread / and I'm not opening it") |
| L14 | POST | 56.36 | 63.12 | **Chop field: "not opening it" / "200 unread" / "I'm–I'm not opening it"** |
| L15 | POST | 63.12 | 69.54 | The group chat has 200 unread and I'm not opening it (full pair) |
| L16 | POST | 69.54 | 76.34 | **Chop tail: "I'm not opening it" / "not opening it" / "200 unread"** |
| L17 | V2 | 76.34 | 79.70 | They planning something and I don't wanna know (yeah) |
| L18 | V2 | 79.70 | 83.14 | If I scroll back I'll lose the whole day for sure (what) |
| L19 | V2 | 83.14 | 86.30 | Badge going red and I'm acting like I'm blind (uh) |
| L20 | V2 | 86.30 | 89.46 | Strategic silence is the only peace of mind |
| L21 | PC2 | 89.46 | 93.48 | Don't open / Just mute it |
| L22 | PC2 | 93.48 | 96.76 | Just mute it **[inferred — lyric-video arbitrated; ASR masked under distortion]** |
| L23 | C3 | 96.76 | 102.66 | The group chat has 200 unread and I'm not opening it |
| L24 | C3 | 102.66 | 110.66 | **Chop field over hook lines 2–3** (ASR garble class; text = sheet fragments) |
| L25 | C3 | 110.66 | 123.02 | Hook line 4 + **chop tail ("I'm–I'm not opening it" 110.7–115.2)** |
| L26 | BR | 124.72 | 131.80 | **"200" stutter chops ×4 (124.72/125.76/127.66/128.18) → "I'm not looking I'm not looking" (yeah)** |
| L27 | BR | 131.80 | 134.70 | Leave it / Leave it |
| L28 | FC | 134.70 | 139.86 | The group chat has 200 unread (and I'm not opening it) |
| L29 | FC | 139.86 | 146.70 | Hook lines 2–3 (compressed) |
| L30 | FC | 146.70 | 153.10 | **CHOP BREAKDOWN 2: "200 unread" ×2 / "I'm–I'm not open it" / "and I'm not open it"** |
| L31 | FC | 153.10 | 162.50 | Hook line 4 + **sustained chop tail "I'm NOT O–O–Open it" (156.5–160.7)**, resolves 162.50 |
| L32 | OUT | 162.50 | 164.42 | Not opening it |
| L33 | OUT | 165.68 | 171.00 | Not opening it / 200 unread |
| L34 | OUT | 171.00 | 172.00 | (yeah) |
| — | OUT | 172.00 | 173.61 | Instrumental tail (no words) |

## Notes for the cut

- Every performed word above gets picture or kinetic — the chop fields
  (L03, L14, L16, L24, L26, L30, L31-tail) are first-class content, not
  gaps: kinetic SLAM fragments + glitch cuts on their S-tier accents.
- Hook onsets (mouth-gate targets): L01 0.00, L02 5.68, L04 18.48,
  L12 44.80, L15 63.12, L23 96.76, L28 134.70, L31 153.10.
- ASR garble classes in distorted choruses ("channel/chatt/on read",
  "the boot that has 200 on bread") are mishears of the hook line —
  captions use the arbitrated sheet text; word TIMES stand.
- Word-level grid: work/analysis/SONG_WORDS.json (310 words with prob).
  Low-prob words cluster exactly on the chops — expected: pitch-shifted
  chops defeat ASR confidence, not existence (segments + lyric video
  confirm them).
