# MUSIC_TAGS — music identity registry (Era II, CEO order R1, 2026-10-21)

Every finished master carries `MUSIC_TAG` = a bed id + a sting id in the
public manifest. Masters shipped before Era II are backfilled as
`legacy-none`. A new master without a MUSIC_TAG row fails QC — do not ship it.

Network anthem: `MV-1 "ON FILE"` (musicvideo/MV-1_ON_FILE/). All beds and
stings derive from the anthem's hook: one organism, nine rooms.

## The nine channel beds + stings (derived from the anthem hook)

| Channel        | Bed id             | Sting id             | Sound                                    |
|----------------|--------------------|----------------------|------------------------------------------|
| NEWS           | MV1-BED-NEWS       | MV1-STING-NEWS       | struck bell + one low brass swell        |
| ORIGINALS      | MV1-BED-ORIGINALS  | MV1-STING-ORIGINALS  | the leap on a detuned room piano, one note |
| SATIRE         | MV1-BED-SATIRE     | MV1-STING-SATIRE     | the hook on a muted plucked bass         |
| LABS           | MV1-BED-LABS       | MV1-STING-LABS       | struck metal with a long decay           |
| ARENA          | MV1-BED-ARENA      | MV1-STING-ARENA      | the hook doubled on two drums, slightly out of phase, crowd-free |
| MEDIA SCHOOL   | MV1-BED-MEDIASCHOOL| MV1-STING-MEDIASCHOOL| the hook reversed then forward again     |
| PUBLIC ACCESS  | MV1-BED-PUBLICACCESS| MV1-STING-PUBLICACCESS| the same three notes mistuned, cable-access cassette |
| PUPPET THEATER | MV1-BED-PUPPET     | MV1-STING-PUPPET     | plucked string + a wooden knock          |
| NETWORK        | MV1-BED-NETWORK    | MV1-STING-NETWORK    | the anthem chorus, tag only              |

Stings run 3-6s, mono-safe, cuttable at the bar. One bed per channel, one
bed per serial, NEVER a bed per clip.

## Ship-time rule

When a factory ships a unit, it appends one row to `music/tags.json`
(machine-readable companion to this file):

    "B-<n>": {"bed": "MV1-BED-<CH>", "sting": "MV1-STING-<CH>"}

until the serial-bed lane opens, then the serial bed replaces the channel
bed for serial units. `slate/qc_music_tag.py <ids>` verifies the rows; a
unit with no row — or with an id outside the families above — fails QC.

Backfill: every master shipped before 2026-10-21 carries `legacy-none`.
