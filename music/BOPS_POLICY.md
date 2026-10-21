# THE BOPS POLICY — short bangers on one grid (owner order 2026-10-21)

Owner, verbatim: *"help me write suno v6 music bangers using my bops policy … short
bangers 1:30 or 0:10 and 0:30 for bumper lengths and 1:00 for stuff … better genres,
no rap, no nu metal, no pop, this is earworm memes only … heartbeat dance 4:4 or
faster."*

This file is the policy translated into numbers a factory can execute. The source
research is the owner's `BANGER_DOCTRINE.md` (seven layers, 27 sources) in the
SlopCannon tree: earworm features, dumb-vocabulary measurement, second-person
address, prosody, structure maths, punch-as-engineering, and picture/sound mapping.

## 1. One tempo, four lengths — 144 BPM

The tempo is chosen for arithmetic, not taste. In 4/4 at **144 BPM** one bar is
**1.6667 s**, so every owner length is a whole number of bars and every video cut
lands on a bar line:

| Length | Bars | What it is for |
|---|---|---|
| **0:10** | **6** | channel sting / bumper ident. Hook only, contiguous ×3, no verse |
| **0:30** | **18** | bumper or ad bumper with a lift: hook ×4, four-bar verse, hook, break, hook |
| **1:00** | **36** | the bed for a **3–4 part story piece** (30–45 s of picture) plus tail |
| **1:30** | **54** | the banger: two verses, three hooks, break, outro — release length |

Other tempos are legal only if they keep whole bars at all four lengths
(120 BPM → 5/15/30/45 bars also works). 144 is the default because the policy says
"heartbeat dance 4/4 or faster".

## 2. The genres we are allowed to use

Earworm dance only. **Banned outright: rap, nu metal, pop.** No artist imitation,
ever (describe the sound, never the name).

- **happy hardcore / rave** — piano stabs, hoover, 144–160
- **eurodance** — gated snare, octave brass, key-change lift
- **UK garage two-step** — shuffled swing over a heartbeat sub
- **amapiano house** — log-drum bassline over a four-on-the-floor kick
- **Italo disco / nu-disco** — arpeggio bass, octave strings
- **acid house / Chicago house** — 303 squelch, open hats
- **Baltimore / Jersey club** — chopped breaks, horn stabs, call-and-answer
- **big beat**, **baile funk**, **soca**, **hi-NRG** — all legal fallbacks
- **chiptune rave** — for 0:10 stings only

"Heartbeat feel" in the style box means the kick is the pulse: four-on-the-floor
with an off-beat double-kick figure (lub-dub) at bar ends. Say it in the style
field — `144 bpm four-on-the-floor heartbeat kick` — because it is a rhythm
instruction, not a mood.

## 3. Earworm requirements (from the doctrine, kept)

1. **Hook at 0:00.** No intro. No countdown, no atmosphere, no fade.
2. **Hook contiguous, three times minimum.** The strongest measured predictor of
   involuntary musical imagery is the *same fragment back to back*.
3. **Chorus melody rises then falls**, with **exactly one unusual interval**, and
   the oddity lives in the riff or the first two syllables of the hook. Written
   into the section cue of every prompt.
4. **"You" in the hook.** Second-person density is the one lyric lever with a
   controlled study behind it; our lines run 14–44% "you".
5. **Dumb vocabulary, concrete objects.** All nine songs measure **89–93%
   monosyllables**, Flesch-Kincaid **0.0–1.0**, zero four-syllable words.
6. **One beat count per section, stressed on strong beats.** Every line in the pack
   was selected by measurement: verses hold **5 beats in 7–9 syllables**, hooks
   hold **5 beats in 10–12 syllables**.
7. **Chorus lift by arrangement, not volume:** double-time hats, a second piano or
   log-drum layer, octave strings. Never "louder".
8. **Dry, wide, mono-safe chant.** No reverb stack — reverb smears when a video
   tool slices on a bar line.

## 4. One documented exception to the house gate

`scripts/suno_qa.py` flags lyrics under **200 words** as "thin for a full song".
At 6 bars (0:10) and 18 bars (0:30) that floor is unreachable without breaking the
line-length rules that keep the meter intact — a 30-second song simply cannot hold
200 words. The floor is therefore **waived for the 0:10 and 0:30 lengths and only
those**, on the record, with the arithmetic stated: 18 bars × 4 beats = 72 beats,
at one line per bar and ≤12 syllables a line the ceiling is ~150 words. The 1:00
and 1:30 lengths must clear the floor and do (272–333 words).

## 5. Suno v6 settings that decide whether the prompt is used at all

| Switch | Setting | Why |
|---|---|---|
| Variety | **Off** | at any setting above Off, Suno rewrites the style field and diverges the takes |
| Style Influence | **~75** | default 50 throws away half of a deliberately written prompt |
| Weirdness | low | a tight hook fights weirdness |
| Max Mode | **off for 0:10/0:30**, on for 1:00/1:30 | costs 2× credits; short bangers do not need it |
| Vocal gender | set explicitly | better than describing gender in prose |
| Duration | **Custom, stated** | auto trends slower, sparser and longer |
| Model | **v6-wild first** on dance genres, then Cover the keeper onto v6 | dance and hardcore are where v6 vocals drift generic |

Export: **WAV, exact duration to the millisecond, 0.3 s clean silence head and
tail, no fade-in**, mastered to **−14 LUFS / −1.0 dBTP**, mono-compatible (check
the hook on a phone speaker, not headphones).

## 6. Which length goes where

- **0:10 stings** → channel idents and bumper heads; they are *one gesture*, and a
  video part using one must have no dialogue under it.
- **0:30** → bumper or ad bumper; carries a lift, still no verse-and-chorus sprawl.
- **1:00** → the standard bed under a 3–4 part story piece; duck it 4 dB under the
  spoken line and never re-voice anything.
- **1:30** → the banger; also the bed for a 9-part (90 s) assembled piece.

All four lengths stay inside the network's rule: a theme may score card-free or
speech-free frames only. Native dialogue is inviolable.
