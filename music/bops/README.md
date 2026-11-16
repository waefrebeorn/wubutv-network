# BOPS PACK — nine songs, four lengths, one grid

Built by `music/BOPS_POLICY.md`. Every prompt is a complete Suno v6 two-box file
(STYLE / EXCLUDE / LYRICS). Feed a file to Suno as-is; settings are in the policy.

| file | length | bars @144 | genre |
|---|---|---|---|
| `BD-60A_say_it_again_suno.txt` | 60s | 36 bars | amapiano house |
| `BD-60B_the_line_up_suno.txt` | 60s | 36 bars | Italo disco |
| `BG-90A_one_more_viewer_club_mix_suno.txt` | 90s | 54 bars | happy hardcore |
| `BG-90B_heartbeat_four_suno.txt` | 90s | 54 bars | acid house |
| `BM-30A_one_more_viewer_suno.txt` | 30s | 18 bars | eurodance |
| `BM-30B_roll_the_tape_suno.txt` | 30s | 18 bars | UK garage two-step |
| `ST-10A_press_play_suno.txt` | 10s | 6 bars | happy hardcore rave sting |
| `ST-10B_on_air_suno.txt` | 10s | 6 bars | chiptune rave sting |
| `ST-10C_one_more_suno.txt` | 10s | 6 bars | Baltimore club sting |

## Measured, not asserted (suno_qa + prosody, at build time)

| song | words | mono | you | FK grade | gate |
|---|---|---|---|---|---|
| ST-10A PRESS PLAY | 36 | 89% | 22.2% | 1.0 | meter PASS, word-floor waived (0:10) |
| ST-10B ON AIR | 36 | 89% | 22.2% | 1.0 | meter PASS, word-floor waived (0:10) |
| ST-10C ONE MORE | 36 | 89% | 44.4% | 1.0 | meter PASS, word-floor waived (0:10) |
| BM-30A ONE MORE VIEWER | 144 | 92% | 18.1% | 0.3 | meter PASS, word-floor waived (0:30) |
| BM-30B ROLL THE TAPE | 156 | 92% | 16.7% | 0.6 | meter PASS, word-floor waived (0:30) |
| BD-60A SAY IT AGAIN | 276 | 92% | 15.6% | 0.2 | **PASS** |
| BD-60B THE LINE UP | 272 | 92% | 21.3% | 0.3 | **PASS** |
| BG-90A ONE MORE VIEWER (CLUB MIX) | 333 | 92% | 14.7% | 0.0 | **PASS** |
| BG-90B HEARTBEAT FOUR | 333 | 93% | 20.1% | 0.0 | **PASS** |

Every line in every song holds **5 content beats** and the right syllable count
(verse 7–9, hook 10–12). The lines were selected by running the prosody tool over a
candidate bank, not by ear — the bank of valid verse shapes alone measured 15,840.

## Where the delivered audio goes

Rendered tracks land in `music/incoming/<id>.mp3` (or `.wav`), then the sha256 is
recorded and the `music_tag` for the piece flips from `theme:<id>` reserved to live.
Never lay a track over a speaking frame.
