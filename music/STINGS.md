# MUSIC TAGS + STING REGISTRY (R1 / R3 interface)

Owner: Producer (Muse) owns the manifest field; CEO office owns the tag grammar
and the registry ids. Written 2026-10-21 to close the open question from the
Muse ACK: *"how does the R3 gate interact with R1, given the PIPS motif audio
isn't built yet?"*

**Answer: it doesn't have to be built to be tagged.** R1 is a *naming* gate, not
an *audio* gate. A sting id may exist in the registry before its audio does. The
only rule is that a tag never names something the registry does not list.

## Tag grammar (one string, no free text)

    music_tag := "legacy-none"                  # anything shipped before R1
               | "<bed-id>"                     # bed only
               | "<bed-id>:<sting-id>"          # bed + sting
               | "reserved:<sting-id>"          # id registered, audio not yet rendered
               | "theme:<theme-id>"             # serial/MV theme (user Suno track)

Rules:
1. Every id must appear in this file's registry. A tag naming an unregistered id
   FAILS ship QC (`slate/qc_music_tag.py`) — that is the whole gate.
2. `reserved:` is legal at ship time. It asserts "this unit belongs to this
   sound", and it is what lets R3 be cast now and rendered later. Nothing
   downstream may treat `reserved:` as missing — it is a promise, not a hole.
3. `legacy-none` is frozen at the Era I backfill (1,652 masters). It may never be
   applied to a new master. A new master tagged `legacy-none` fails QC.
4. A master using THE PIPS on screen must carry `pips-1` as its sting id (not
   `reserved:pips-1`) — the R3 entrance gate applies **only to units in which
   the character appears**. Everything else may stay reserved.
5. One bed per channel, one bed per serial. A bed id may not be shared across
   channels. The serial theme (`theme:serial001`) is not a bed — it plays under
   card frames only and never over a speaking frame.

## Registry — built

| id | what | file | duration | sha256 (first 16) |
|---|---|---|---|---|
| `pips-1` | THE PIPS entrance (R3): three struck notes on A3/C#4/E4, then one held A2+E3 under a slow swell | `music/stings/pips_1.wav` | 4.599979 s | `def9ea851868521f` |

Built by `music/stings_gen.py` (numpy additive synthesis, no samples, no licensed
material). QC measured, not asserted: `pcm_s16le`, 48 kHz, 2 ch, mean −17.3 dB,
**max −1.0 dBFS**, L/R bit-identical so it is mono-safe by construction.
Interval family: root A3 220 Hz; the family's leap is the perfect fifth
(220→330); emitted degree set {1, 3, 5}. Every future sting is drawn from the
same three degrees so the network sounds like one organism.

## Registry — reserved (specified, not yet rendered)

Channel stings, 3–6 s each, same degree set, cuttable at the bar:

| id | channel | spec |
|---|---|---|
| `sting-news` | NEWS | struck bell + one low brass swell; time pressure, no melody |
| `sting-originals` | ORIGINALS | the fifth leap on a detuned room piano, one note |
| `sting-satire` | SATIRE | the hook on a muted plucked bass |
| `sting-labs` | LABS | struck metal, long decay (a measurement) |
| `sting-arena` | ARENA | the leap doubled on two drums, slightly out of phase, crowd-free |
| `sting-mediaschool` | MEDIA SCHOOL | the hook reversed, then forward again |
| `sting-publicaccess` | PUBLIC ACCESS | the same three notes, mistuned, cassette wow |
| `sting-puppet` | PUPPET THEATER | plucked string + a wooden knock |
| `sting-network` | NETWORK | the anthem chorus tag only |
| `theme-serial001` | SERIAL-001 | user's Suno track as the serial theme (card + end card only) |
| `theme-mv1` | MV-1 | "ON FILE" anthem (`musicvideo/MV-1_ON_FILE/`) |

## Music the owner is bringing

The owner is producing tracks in Suno and sending MP3s to both agents. Landing
rule: the delivered MP3 goes to `music/incoming/<id>.mp3`, gets a sha256 recorded
here, and only then may a `theme:` or bed id leave `reserved:`. Never score a
delivered track over a speaking frame — native audio is inviolable.
