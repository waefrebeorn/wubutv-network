# MV-26 GATE LOG — "Gotta Poop"

Master: `masters/mv26_gotta_poop_16x9.mp4` · md5 `7e1afe037d9598088c0500c0f1f20640` · 64,201,757 B
Chat copy: `masters/mv26_gotta_poop_chat.mp4` · md5 `fb9700934f84f2c7822ba582ec35f392` · 46,218,294 B
Spend: **17/40 video generations · 0 refusals · 0 429s**

## Gates

- **Frames/duration (SEGMENT LAW)** — PASS. 38/38 segments asserted for BOTH frame count AND duration at build (setpts warp FIRST, then fps=24 resample). joined.mp4 probed before the master encode: 2871 frames, 119.624s, 1280×720. Master: exactly **2871 frames**, 119.625s container duration (track 119.616s; 9ms padding delta, disclosed below).
- **Format** — PASS. One 16:9 master only: h264 1280×720, 24fps, yuv420p, faststart.
- **CRF 18 proof (size differential)** — PASS. Identical-chain CRF 23 encode = 34,681,715 B vs master 64,201,757 B = **1.85×**. (This VM's x264 SEI always claims crf=23.0; SEI not cited.)
- **Audio** — PASS. track.mp3 re-encoded to AAC LC 48 kHz, 192k, stereo. Never stream-copied.
- **Subtitles burned in** — PASS. Word-timed karaoke ASS built from SONG_WORDS.json (174 word events, 33 lines; current word yellow, bold white on semi-transparent black bar, bottom-center, MV-2 v7 house style) and burned into the picture. Verified on frame grabs at 8.0s / 60.0s / 87.2s / 118.9s. mov_text track also present (33 cues) but does not count alone.
- **Corner bug** — PASS. "~ WuBu ~" gold, bottom-right, verified EXACT on all four grabs (head/mid/S09/tail).
- **Freezedetect** — PASS. Zero freeze events over the master (n=-50dB, d=1.5s).
- **G7 lyric check (per-take ASR)** — PASS. Keeper takes: S01 1.000, S02 t2 1.000, S03 1.000, S04 1.000, S06 1.000, S07 1.000, S08 1.000, S09 t3 1.000 (both "Need to go right now" performances ASR-confirmed), S11 1.000; chant donors S05 t2 0.800 / S13 t1 0.800 / S14 t1 1.000 (chant words; sub-cut by design, see disclosures).
- **Motion law** — PASS. Every keeper take: max near-dup run 0.0s; every cut lands on motion; no halted-photo starts (the one static source span found in assembly QC was replaced, see disclosures).
- **Adults only** — PASS. Every take eye-checked. S05 t1 REJECTED for an apparent infant in a stroller (~5–7s); rerolled on the cast axis (adults 30–70 named, no strollers) — shipped S05 t2 is senior-shoppers only. All crowds (mall, wedding, elevator, platform, plaza) verified grown adults.
- **One-writer rule** — PASS. ps-check before the master encode showed no other ffmpeg on the output path; exactly one assembly pass owned joined.mp4 (the S01 fix re-concatenated from the same segment set before encoding, single writer).
- **Chat copy** — PASS. 46,218,294 B ≤ 50 MB, 2871 frames, bitrate-capped from the master, audio copied.

## Disclosed flaws (plainly)

1. **S04 held "poop" (34.58–38.46)** — the song holds the word ~3.3s; the take sings it in 0.46s, an interval that cannot land inside warp caps. BAD-WORD RULE applied: the span ships as a montage — the sung "gotta poop" warped 1.79× (grey zone), a button-mash insert, a trapped-slump insert, and the elevator-arrival tail. The held note is not lip-matched for its full length.
2. **S01 intro (0–6.14)** — the take's own post-line tail was a static held pose; replaced in assembly rather than shipped. The intro is a 1.9× slow-motion sprint (4.54s) plus a 1.58s eyes-darting platform close-up insert (S13's unused tail) before the first word.
3. **S09 intercut takes** — the scene intercuts t3 (both sung performances) with t2 (slowed 1.51× arrival head; natural closed-mouth dance/plea gap cover). Same set, wardrobe and attendant; the joints are visible cuts, not hidden.
4. **S11 build (96.22–117.82)** — the pre-shout slide/settle is slowed 1.63× across the 9.83s instrumental build; the final shouted "Poop!" is sped 0.54× to fit the song's 0.76s shout.
5. **S10 cutaway** — the whole 10s take is slowed 1.18× to fill its 11.79s instrumental window.
6. **S02 tail** — t2's ASR shows the closing "gotta poop" sung once explicitly amid extra "poop"s (G7 1.000 on planned words); the song's doubled "Gotta poop! Gotta poop!" ending is a near-match, not a verified double.
7. **Chant span (40.48–82.40)** — natural-speed sub-cuts on chant onsets across six donor stagings, not per-word lip sync. By design: the ~130-word chant is unmatchable per-word (documented at intake). Mouths sing the same chant words throughout.
8. **Background text texture (nits)** — S01 frames carry small blurry unreadable office posters/glass etching; S04's elevator panel shows a small red floor numeral; S13 has small environmental transit signage, mostly blurry. No legible words anywhere in the shipped master. (S09 t1's legible "OCCUPIED" door sign was a reject reason; the shipped door is blank with only the red indicator dot.)
9. **Duration delta** — master container duration 119.625s vs track 119.616s (9ms). Frame count is exact (2871).
