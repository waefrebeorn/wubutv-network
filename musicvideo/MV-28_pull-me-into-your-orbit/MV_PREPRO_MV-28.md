# MV-28 PREPRO — "Pull Me Into Your Orbit" (measured plan, 2026-11-20)

Track: 240.000s exact (track.mp3 ffprobe 240.000000s), measured 141.5 BPM
(beat 0.42403s, phase 0.080s — AUDIO_ANALYSIS.md). **Frame target =
round(240.000 × 24) = 5760 frames EXACTLY.** Master: 1280×720, 24fps,
h264 CRF 18, AAC LC 48k from track.mp3 (never stream-copied), faststart,
"~ WuBu ~" gold bug bottom-right. Lyric authority = burned-in sheet
(lyrics.txt, 40 lines); timing authority = SONG_WORDS.json (280 ASR
words, 29.66–232.30s).

Hook timing adjudication (intake "unmatched" lines — all five are sung
hook occurrences ASR garbled; spans recovered from the ASR stream
itself, work/swing/gap_analysis.txt): L11 "Pull me into your orbit" =
68.84–71.10 (ASR "We'll be into your orbit", after the ad-libs); L25 =
135.04–137.86 (ASR "Hold me into your oven"); L32 = 192.12–194.46 (ASR
"No need to be above it" — heavily garbled under the final-chorus
choir, span taken from the garble); L34 = 198.92–201.26 (ASR "Hold me
into your orbit"); L37 = 207.74–210.42 (ASR "Hold me into your orbit",
after the ad-libs). L07 ends 55.16 on the ASR "oven"=orbit slot. L06
ends 51.62 on the ASR "fall"=burn slot. Backing ad-libs "You know the
way / Show us the way" are sung before L11 (65.70–68.84), L25
(131.96–135.04) and L37 (204.72–207.74) — captioned as backing lines
(MV-24 patter precedent). Spoken intro patter "Let's get started"
29.66–29.84 captioned as patter. Outro backing "(Hold on, hold on)"
222.58–225.08 captioned per the sheet's own backing marking. Sheet
repeats sung as one drawn-out phrase (L23+L24, L35+L36) get their
shared span split equally between the two printed lines, disclosed.

## Production bible (identity macros — expanded into every vehicle)

- HER (lead singer, S1 — the sheet is first-person hers: "My lipstick
  marks the porcelain"): a grown woman in her late thirties, long dark
  wavy hair, crimson lipstick, a midnight-teal velvet evening gown, a
  thin gold pendant necklace. Same face, same gown, every take.
- HIM (S2): a grown man in his early forties, short salt-and-pepper
  hair, light stubble, a charcoal suit with an open-collar white shirt,
  no tie. He never sings a lead line; in HER singing takes his mouth
  stays closed. Signature: he is the one who set his glass beside the
  phone; his jacket ends up folded over her chair in verse 2.
- THE KEEPER (support): a grown man in his sixties, white beard,
  burgundy waistcoat — he winds and tends the great orrery. MARA-equivalent
  support: THE HOSTESS, a grown woman in her fifties, silver-streaked
  hair in a low bun, black evening dress, who seats guests and carries
  the second glass in the outro. Crowds: grown adults in their
  thirties to sixties ONLY, in evening dress, stated explicitly in
  every crowd vehicle. NO children, NO teenagers, nobody who could
  read as under 25, no family stagings.
- WORLD — ONE COHERENT ELSEWHERE: THE ORBIT ROOM, a grand domed
  planetarium ballroom on one long night. A circular marble hall under
  a glass dome of stars; at its centre a huge brass orrery — planets
  on brass arms circling a glowing amber sun-lamp; around it a slow
  rotating ring walkway; marble cafe tables at the edge; tall arched
  windows. The whole song is the room's gravity working: verses = the
  two of them on separate wide orbits, glancing across the machine;
  pre-choruses = the ring floor itself turns and carries them;
  choruses = closest passes, sparks off the sun-lamp, the room's
  couples circling too; bridge = one step back out of the orbit, then
  the long way round back in; final chorus = the two orbits merge at
  the centre, dancing inside the orrery's rings; outro = dawn through
  the dome, still circling slowly, "until the morning".
- LOOK: photoreal romantic night, shot on 35mm film, visible fine
  grain. Palette: deep indigo + warm gold + bone + ink; accent crimson
  (her lipstick, one sash) at ≤10% of frame. Section colour map:
  intro deep indigo; verses warm lamp-gold at the tables; pre-choruses
  warming; choruses full gold-teal saturation + sparks; the long break
  cooler moonlight silver-blue; bridge intimate warm dim; final chorus
  peak gold; outro dawn amber-rose through the dome.
- FORBIDDEN: legible text anywhere (all signs, screens, papers and the
  phone BLANK or pure light), logos, children, frozen stills, slow
  openings, ramp-from-rest starts. Every take is already moving at
  frame 0.

## Recurring motif (declared, escalating — motif law)

THE CLOSING ORBIT: every chorus the couple's circling brings them one
ring closer — wide separate orbits (V1) → the turning ring carries
them (PC) → first close pass with sparks (Ch1) → held revolution among
the room's couples (Ch1 tail) → closest pass yet, night rushing in
(Ch2) → the vow ring of joined hands (Ch2 tail) → the step back and
the long way round again (Bridge — the motif's one reversal) → merged
orbit at the centre (FC) → held-on circling into dawn (Outro). Each
slot's MOTION MOTIF is distinct (see table); the escalation is the
closing distance, never a re-run staging.

## Scene table (song order; all events invented for this build, checked
against USED_EVENTS.md — none of MV-22..MV-27's events or stagings
reused; no event or motion motif repeats within this video)

| S | Window (frames) | Lines | Tag | Event (Inv.) | Motion motif | Setting / beat |
|---|---|---|---|---|---|---|
| S01 | 0.00–15.00 (360f) | instrumental | CUTAWAY | Inv. The Orrery Awakens | mechanical circling | FRAME 0: the great orrery already turning, planets circling the amber sun-lamp; the KEEPER winds the brass crank as the dome stars brighten; camera orbits the machine |
| S02 | 15.00–30.63 (375f) | instrumental; patter "Let's get started" 29.66 | CUTAWAY | Inv. The Long Way Round | perimeter glide | HER enters and takes the long way around the room's edge, passing every table; HIM at the far side sets his glass beside a dark blank phone; the HOSTESS nods the evening open |
| S03 | 30.63–37.50 (165f) | V1 L01–L02 | SINGING | Inv. The Glass Beside the Phone | seated lean + glance | HER sings at a marble table, his glass and the blank phone in frame; on L02 she glances along the long curve of the room |
| S04 | 37.50–44.33 (164f) | V1 L03–L04 | SINGING | Inv. The Eyebrow Across the Planets | passing-planet parallax | HER sings as a brass planet on its arm passes between her and HIM across the room; the raised eyebrow lands as the planet clears |
| S05 | 44.33–52.88 (205f) | PC1 L05–L06 | SINGING | Inv. The Room Turns | platform rotation | Both stand on the rotating ring walkway; the floor itself carries them toward each other as she sings the pre-chorus |
| S06 | 52.88–65.71 (308f) | Ch1 L07–L10 | SINGING | Inv. The First Close Pass | ring-circling approach | Circling the orrery on the ring, their orbits bring them shoulder to shoulder at the near point; golden sparks trail the sun-lamp on "sparks begin"; the night doors breathe open on "rushing in" |
| S07 | 65.71–79.00 (319f) | ad-libs + Ch1 L11–L13 | SINGING | Inv. The Held Revolution | sustained revolution | One full held revolution: the couple completes a whole circle holding the gaze while the room's couples circle with them; "don't let go" sung across the turn |
| S08 | 79.00–97.00 (432f) | instrumental | CUTAWAY | Inv. The Star Wheel | overhead wheeling | The dome's star field wheels slowly overhead while couples turn in slow circles on the floor far below; the orrery's shadow sweeps the marble |
| S09 | 97.00–103.63 (159f) | V2 L14–L15 | SINGING | Inv. The Lipstick on the Porcelain | cup raise | Back at the table: his jacket folded over her chair; she lifts the porcelain cup — her crimson lipstick mark on its rim — and sings both lines over it |
| S10 | 103.63–110.92 (175f) | V2 L16–L17 | SINGING | Inv. The Lost Place | gestured-story falter | HIM tells a story with his hands, loses his place, falters silent; HER sings the lines and catches him looking |
| S11 | 110.92–118.42 (180f) | PC2 L18–L19 | SINGING | Inv. The Second Turning | counter-rotation | The ring turns the other way, a touch faster; they end the pre-chorus one ring closer than the first turning |
| S12 | 118.42–131.96 (325f) | Ch2 L20–L24 | SINGING | Inv. The Sparks at Perihelion | closest pass + rushing air | The closest pass of the night: sparks shower at the near point; the tall doors swing wide and the night air rushes in, curtains billowing, on "rushing in" |
| S13 | 131.96–145.21 (318f) | ad-libs + Ch2 L25–L27 | SINGING | Inv. The Morning Vow Ring | hand-held ring rotation | The room's couples join hands into one great ring around the orrery and turn slowly together on "don't let go until the morning" |
| S14 | 145.21–155.50 (247f) | instrumental break | CUTAWAY | Inv. The Gearheart | gear turning | Inside the orrery: great brass gears and escapements turning, planets' arms sweeping past the lens, lamp-light flaring through the teeth |
| S15 | 155.50–165.79 (247f) | instrumental break | CUTAWAY | Inv. The Distant Dance | distant sway | Far across the hall, small in frame, the couple slow-dances at a distance among the turning couples, moonlight silver through the dome |
| S16 | 165.79–176.17 (249f) | instrumental break | CUTAWAY | Inv. The Moon Crossing | sky transit | The moon crosses the glass dome panel by panel above the still-turning orrery; star fields drift; the room breathes before the bridge |
| S17 | 176.17–186.13 (239f) | Bridge L28–L30 | SINGING | Inv. The Step Back | retreat | On "one step back" she steps out of his orbit and the ring carries her away; his hand stays raised; she sings the quiet promise across the widening gap |
| S18 | 186.13–194.46 (200f) | Bridge L31 + FC L32 | SINGING | Inv. The Long Way Round Again | return arc | She takes the long way around the orrery one more time — and this time the arc lands her back in front of him on the hook (rhymes S02, reversed meaning) |
| S19 | 194.46–204.71 (246f) | FC L33–L36 | SINGING | Inv. The Merged Orbit | centre dance | At the centre, inside the orrery's rings: the couple dances face to face while the planets circle THEM; the room's couples orbit outside the rings |
| S20 | 204.71–214.42 (233f) | ad-libs + FC L37–L38 | SINGING | Inv. The Vow at Closest Point | held closeness sway | Foreheads nearly touching, hands held, a slow sway: the last "don't let go until the morning" sung close and quiet inside the loudest light |
| S21 | 214.42–224.00 (230f) | Outro L39 | SINGING | Inv. The First Light | dawn brightening | First dawn light through the dome panels; she sings "until the morning" soft, the room's gold giving way to amber-rose |
| S22 | 224.00–232.29 (199f) | backing + Outro L40 | SINGING | Inv. The Held-On Orbit | slow held circling | On "hold on, hold on" they hold on and circle slowly in the growing light; the final hook sung circling, unhurried |
| S23 | 232.29–240.00 (185f) | instrumental tail | CUTAWAY | Inv. The Empty Dome at Dawn | still machine turning | The empty room at dawn: the orrery still turning, two glasses on the marble table, the ring floor slowing to rest; held into the fade |

Energy arc (cuts/min): intro ~30 (awakening + perimeter glide) →
verses ~18 → PC ~25 → Ch1 ~40 → interlude ~12 (the wheel) → V2 ~18 →
PC2 ~28 → Ch2 ~45 → break ~10 (three long breaths) → bridge ~20 →
FC ~50 (merged orbit, densest) → outro ~10. Tension: the closing
distance; release: dawn. Final frame rhymes S01 (same orrery, dawn
instead of night). Chorus-hook test: pilot volley = S06 (the hook
scene), S03 (verse singing look), S19 (final-chorus centre dance) —
QC before firing the rest.

## Warp / assembly method

Phrase-level smooth warp per singing scene (setpts FIRST, then
fps=24), per MV-24/MV-26/MV-27's build pattern; wordless spans and
inter-line gaps filled with cover from the scene's own takes
(non-claimed spans only, claim-ledger audited); cutaway scenes
assembled as natural-speed sub-cuts on the beat grid across the
scene's takes. Every segment asserted for frames AND duration;
joined.mp4 probed (5760f AND 240.000s) before the master encode. ONE
assembly pass, ONE ffmpeg writer (ps-check first). Master encode:
burned word-timed karaoke ASS (MV-2 v7 style; display text = SHEET
words mapped onto ASR timing slots, MV-24 method — garbled slots
mapped by alias: oven→orbit, fall→burn, Hold/We'll be→Pull me) +
mov_text + "~ WuBu ~" gold bug, CRF 18, AAC from track.mp3. CRF-18
proof = size differential vs identical CRF-23 chain. Freezedetect
zero events target. Chat copy ≤50MB (audio copied) + masters/
_50mb.mp4 sibling byte-copy (house master will exceed 100MB).
