# MV-16 "Wrong for Years" — LYRIC TIMELINE (Stage 1, measured)

Method: ASR word grid (faster-whisper large-v3-turbo int8, cpu_threads=2, NO VAD, chunked 60s+2s — work/analysis/SONG_WORDS.json, 354 words) as the TIMING authority; sheet (lyrics.txt) as the TEXT authority; performed line sequence hand-authored from the sheet + measured extras, aligned by token matching with the house mishear table (stop→stopped, decay/day→decade, mike→mic, seen/done→been, three→for) — work/analysis/build_grid.py → grid_lines.json, 97 performed lines, every line span word-verified. Beat grid: 150.0 BPM, period 0.400s, phase -0.192s (work/swing/beat_grid.json). All times [confirmed] measured unless tagged.

## Section table

| # | Section | Start | End | Dur | Notes |
|---|---------|-------|-----|-----|-------|
| 1 | Chorus 1 (cold open) | 0.00 | 26.04 | 26.04 | Cold open, full chorus at 0s; ends with performed shout 'Hey! Hey!' (24.88–26.04) into the verse |
| 2 | Verse 1 | 26.04 | 47.92 | 21.88 | Car chorus story; ad-libs (yeah) x1 performed as yeah-yeah pair, (what); the sheet's '(uh)' after 'different' is not separately audible — folded into L21's tail |
| 3 | Pre-Chorus 1 | 48.94 | 54.10 | 5.16 | 4 short lines, call-and-repeat |
| 4 | Chorus 2 | 54.10 | 77.90 | 23.80 | Chorus with backing vocalise inside: (oh-oh-oh) after trio 1, (oh-uh-oh) after trio 2 — performed extras beyond the sheet |
| 5 | Post-Chorus | 77.90 | 84.66 | 6.76 | Nobody stopped me x2, Wrong for years x2 (sheet-exact on word check) |
| 6 | Verse 2 | 86.66 | 100.06 | 13.40 | Karaoke room verse; ad-libs (yeah)/(what)/(uh) all present |
| 7 | Pre-Chorus 2 | 100.06 | 104.78 | 4.72 | Same 4-line figure as PC1 |
| 8 | Chorus 3 | 104.78 | 132.24 | 27.46 | Full chorus; short breath gaps inside trio 3 (128.74–130.32) |
| 9 | Bridge | 132.24 | 145.08 | 12.84 | Texture break: WFY x2, NSM x2 with a performed '(no,)' pickup at 135.58, (yeah), held 'still going' |
| 10 | Final Chorus | 145.08 | 172.84 | 27.76 | Densest + loudest section; 'Nobody stopped me' DOUBLED inside trios 1 and 2 (performed, beyond the sheet block) |
| 11 | Outro | 174.10 | 182.80 | 8.70 | NSM, (oh) vocalise, NSM, WFY, WFY+(yeah); words end 182.80, tail music to 183.20 |

## Line table (performed text = sheet text; ASR column is the timing evidence)

| Line | Sec | Start | End | Text | Kind | ASR heard |
|------|-----|-------|-----|------|------|-----------|
| L01 | C1 | 0.00 | 2.14 | I've been singing the wrong lyrics | line | i've been singing the wrong lyrics |
| L02 | C1 | 2.14 | 3.44 | For a decade | line | for a decade, |
| L03 | C1 | 3.92 | 5.24 | Nobody stopped me | line | nobody stopped me |
| L04 | C1 | 5.24 | 8.52 | I've been singing the wrong lyrics | line | i've been singing the wrong lyrics |
| L05 | C1 | 8.52 | 9.90 | For a decade | line | for a decade, |
| L06 | C1 | 10.26 | 11.74 | Nobody stopped me | line | nobody stop me |
| L07 | C1 | 12.82 | 14.62 | Wrong for years | line | wrong for years, |
| L08 | C1 | 15.20 | 16.46 | Wrong for years | line | wrong for years |
| L09 | C1 | 16.46 | 19.28 | And I'm still going | line | and i'm still going |
| L10 | C1 | 19.28 | 21.32 | I've been singing the wrong lyrics | line | i've been singing the wrong lyrics |
| L11 | C1 | 21.32 | 22.66 | For a decade | line | for a decay, |
| L12 | C1 | 22.94 | 24.88 | Nobody stopped me | line | nobody stops me |
| L13 | C1 | 24.88 | 26.04 | Hey! Hey! | extra | hey! hey! |
| L14 | V1 | 26.04 | 28.86 | Belted the whole chorus in the car | line | belted the whole chorus in the car |
| L15 | V1 | 28.86 | 30.36 | Like I wrote it | line | like i rode it yeah, |
| L16 | V1 | 30.60 | 31.86 | (yeah) | adlib | yeah |
| L17 | V1 | 31.86 | 34.84 | Friends in the back just nodded | line | friends in the back just nodded |
| L18 | V1 | 34.84 | 37.34 | And let it ride | line | and let it ride |
| L19 | V1 | 37.34 | 38.14 | (what) | adlib | what? |
| L20 | V1 | 38.54 | 39.98 | Now I'm at karaoke | line | now i'm at karaoke |
| L21 | V1 | 39.98 | 42.48 | And the screen says different | line | and the screen says different |
| L22 | V1 | 42.48 | 45.00 | But I'm already locked in | line | but i'm already locked in |
| L23 | V1 | 45.00 | 47.92 | And I'm not switching sides | line | and i'm not swooning itch inside |
| L24 | PC1 | 48.94 | 50.30 | I learned it wrong | line | i learned it wrong, |
| L25 | PC1 | 50.42 | 51.18 | I learned it wrong | line | i learned it wrong |
| L26 | PC1 | 51.18 | 52.52 | And I kept it | line | and i kept it, |
| L27 | PC1 | 52.66 | 54.10 | And I kept it | line | and i kept it |
| L28 | C2 | 54.10 | 56.38 | I've been singing the wrong lyrics | line | i've been singing the wrong lyrics |
| L29 | C2 | 56.38 | 57.56 | For a decade | line | for a decade |
| L30 | C2 | 57.56 | 59.46 | Nobody stopped me | line | nobody stop me |
| L31 | C2 | 59.84 | 60.62 | (oh-oh-oh) | extra | -oh -oh |
| L32 | C2 | 60.62 | 62.74 | I've been singing the wrong lyrics | line | i've been singing the wrong lyrics |
| L33 | C2 | 62.74 | 63.96 | For a decade | line | for a decade |
| L34 | C2 | 63.96 | 65.84 | Nobody stopped me | line | nobody stop you |
| L35 | C2 | 65.84 | 67.22 | (oh-uh-oh) | extra | oh -uh -oh |
| L36 | C2 | 67.22 | 68.84 | Wrong for years | line | wrong for years |
| L37 | C2 | 68.84 | 70.22 | Wrong for years | line | wrong for year |
| L38 | C2 | 70.22 | 73.40 | And I'm still going | line | and i'm still going |
| L39 | C2 | 73.40 | 75.44 | I've been singing the wrong lyrics | line | i've done singing the raw lyrics |
| L40 | C2 | 75.44 | 76.32 | For a decade | line | for a day |
| L41 | C2 | 76.32 | 77.90 | Nobody stopped me | line | nobody stop |
| L42 | POST | 77.90 | 79.54 | Nobody stopped me | line | nobody stop |
| L43 | POST | 79.54 | 81.10 | Nobody stopped me | line | nobody stop |
| L44 | POST | 81.10 | 83.06 | Wrong for years | line | wrong for years |
| L45 | POST | 83.06 | 84.66 | Wrong for years | line | wrong for years |
| L46 | V2 | 86.66 | 88.54 | Mic in my hand | line | mike in my hand |
| L47 | V2 | 88.54 | 90.08 | And the room starts to notice | line | and the room starts to notice |
| L48 | V2 | 90.08 | 90.38 | (yeah) | adlib | yeah |
| L49 | V2 | 90.38 | 92.40 | But the wrong version hits harder | line | but the wrong version hits harder |
| L50 | V2 | 92.40 | 93.18 | So I'm staying | line | so i'm staying |
| L51 | V2 | 93.18 | 93.50 | (what) | adlib | what? |
| L52 | V2 | 93.68 | 95.54 | They can read the screen all they want | line | they can read the screen all they want, |
| L53 | V2 | 95.58 | 96.38 | I'm committed | line | i'm committed |
| L54 | V2 | 96.38 | 96.64 | (uh) | adlib | uh, |
| L55 | V2 | 96.84 | 97.70 | Ten years deep | line | ten years deep |
| L56 | V2 | 97.70 | 100.06 | And I'm not rewriting it now | line | and i'm not rewriting it now |
| L57 | PC2 | 100.06 | 101.04 | I learned it wrong | line | i learned it wrong |
| L58 | PC2 | 101.04 | 101.96 | I learned it wrong | line | i learned that wrong |
| L59 | PC2 | 101.96 | 103.22 | And I kept it | line | and i kept it |
| L60 | PC2 | 103.22 | 104.78 | And I kept it | line | and i keep it |
| L61 | C3 | 104.78 | 107.10 | I've been singing the wrong lyrics | line | i've been singing the wrong lyrics |
| L62 | C3 | 107.10 | 108.24 | For a decade | line | for a decade |
| L63 | C3 | 108.24 | 110.08 | Nobody stopped me | line | nobody stopped me |
| L64 | C3 | 111.16 | 113.12 | I've been singing the wrong lyrics | line | i've seen the wrong words |
| L65 | C3 | 113.12 | 114.58 | For a decade | line | for a decades |
| L66 | C3 | 114.58 | 116.48 | Nobody stopped me | line | nobody stopped you |
| L67 | C3 | 118.04 | 119.56 | Wrong for years | line | wrong for years, |
| L68 | C3 | 119.84 | 121.62 | Wrong for years | line | wrong for years |
| L69 | C3 | 121.62 | 124.02 | And I'm still going | line | and i'm still going |
| L70 | C3 | 124.02 | 126.28 | I've been singing the wrong lyrics | line | i've been singing the wrong lyrics |
| L71 | C3 | 126.98 | 128.74 | For a decade | line | for a decade |
| L72 | C3 | 130.32 | 132.24 | Nobody stopped me | line | nobody stopped me |
| L73 | BR | 132.24 | 133.40 | Wrong for years | line | wrong for year, |
| L74 | BR | 133.72 | 135.58 | Wrong for years | line | wrong with years no, |
| L75 | BR | 135.58 | 138.54 | Nobody stopped me | line | nobody stopped me |
| L76 | BR | 138.54 | 140.10 | Nobody stopped me | line | nobody stopped you |
| L77 | BR | 140.10 | 140.96 | (yeah) | adlib | yeah, |
| L78 | BR | 142.64 | 145.08 | And I'm still going | line | and i'm still going |
| L79 | FC | 145.08 | 148.12 | I've been singing the wrong lyrics | line | i've been singing the wrong lyrics |
| L80 | FC | 148.12 | 149.26 | For a decade | line | for a decade |
| L81 | FC | 149.26 | 151.04 | Nobody stopped me | line | nobody stopped me, |
| L82 | FC | 151.04 | 152.46 | Nobody stopped me | extra-double | nobody stopped me |
| L83 | FC | 152.46 | 154.38 | I've been singing the wrong lyrics | line | i've been singing the wrong lyrics |
| L84 | FC | 154.38 | 155.68 | For a decade | line | for a decade |
| L85 | FC | 155.68 | 157.30 | Nobody stopped me | line | nobody stopped me, |
| L86 | FC | 157.38 | 158.98 | Nobody stopped me | extra-double | nobody stop me |
| L87 | FC | 158.98 | 160.50 | Wrong for years | line | wrong three years, |
| L88 | FC | 160.68 | 162.38 | Wrong for years | line | wrong three years |
| L89 | FC | 162.38 | 164.90 | And I'm still going | line | and i'm still going |
| L90 | FC | 164.90 | 166.76 | I've been singing the wrong lyrics | line | i've be singing the wrong lyric |
| L91 | FC | 167.94 | 169.72 | For a decade | line | for a decad |
| L92 | FC | 170.98 | 172.84 | Nobody stopped me | line | nobody stopped me |
| L93 | OUT | 174.10 | 176.06 | Nobody stopped me | line | nobody stop me |
| L94 | OUT | 176.06 | 177.28 | (oh) | adlib | oh |
| L95 | OUT | 177.28 | 179.22 | Nobody stopped me | line | nobody stop me |
| L96 | OUT | 179.22 | 180.60 | Wrong for years | line | wrong for years |
| L97 | OUT | 180.60 | 182.80 | Wrong for years (yeah) | line | wrong for years, yeah |

Gaps / breaths: 47.92–48.94 (V1→PC1), 84.66–86.66 (POST→V2), 104.78 boundary PC2→C3 is tight, 110.08–111.16 and 116.48–118.04 (inside C3), 128.74–130.32 (C3 trio 3), 141.0–142.64 (inside BR, held), 166.76–167.94 and 169.72–170.98 (inside FC trio 3), 172.84–174.10 (FC→OUT).
