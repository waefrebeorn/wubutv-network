# MV-24 PREPRO — "The Jelqer" (measured plan, 2026-11-20)

Track: track.mp3 measured **166.400s** (ffprobe, both mp3 + mp4 agree) →
target master = round(166.400 × 24) = **exactly 3994 frames @24fps**
(166.4167s container), 1280x720, CRF 18, AAC 48k.
Tempo: measured **153.0 BPM** (beat 0.3922s, phase 0.220s).
Lyric text authority = burned-in sheet (lyrics.txt, asterisk censorship
verbatim); timing authority = SONG_WORDS.json (156 ASR words, 3.70–158.90s).

Song shape: a **63.5s instrumental intro** (two spoken "Thank you" stage-patter
bits at 3.70 + 34.78–36.04 — not sheet lines) → verse block A (63.52–76.52,
L01–L05) → 6.0s gap → block B (82.54–96.04, L06–L09) → 17.4s gap → block C
(113.46–132.68, L10–L13) → 6.5s gap → final block D (139.14–158.90,
L14–L19) → 7.5s instrumental outro.

## SFW LAW (binding on every vehicle)

The sheet is a crude outlaw ballad; the PICTURE is a clean comedy western.
On screen the Jelqer is only ever THE DRIFTER — a charming rogue who gallops,
ducks posses, hides in hay and tips his hat. Nothing crude, sexual or violent
is ever depicted. The crudest sung lines ship as WORDLESS EVENT COVERS whose
staging is a clean visual rhyme, never a depiction:
- L03/L16 "twistin' a d*ck in his hands" → he twists a lariat loop (S08) /
  wrings out his wet neckerchief (S20).
- L11 "bout to bust … supernova" → a firework rocket bursts over town (S16).
- L12 "Rubbing it out, every day" → he vigorously polishes his boot (S17).
- L06–L09 (victims / sights / not comin' home) stay on the STORYTELLER singing
  + grown-adult crowd reactions; no victim is ever shown, no young person
  appears anywhere in the video.
Singing vehicles quote the sheet verbatim (asterisks included). Only ONE
singing vehicle carries an asterisk word: S09 ("Qu**f"). If the generator
refuses S09 repeatedly it ships as a wordless cover per the refusal rule.

## Production bible (identity macros — expanded into every vehicle)

- THE STORYTELLER = OLD ELI: a grown man of 68, long silver-grey beard,
  deep-lined weathered face, warm squint, battered brown wide-brim hat,
  fringed buckskin jacket over a faded red shirt, dark trousers; a battered
  honey-wood acoustic guitar across his knee. He sings EVERY sung line,
  from the saloon porch, straight at his crowd. Same face, same outfit.
- THE DRIFTER: a grown man of 38, short dark beard stubble, charming
  lopsided grin, black wide-brim hat pulled low, long charcoal duster coat,
  red neckerchief, dusty brown boots, plain silver belt buckle. He NEVER
  sings (every Drifter slot is a wordless cover; mouth closed and still).
- THE SHERIFF: a grown man of 55, iron-grey moustache, tan duster coat,
  silver star badge (a star shape, never text).
- TOWNSFOLK: grown adults only, 30s–70s, each named in its vehicle as a
  grown adult (the barkeep in his sixties, the schoolmarm in her forties,
  the blacksmith in his fifties, deputies in their thirties and forties).
  NO children, NO teenagers, nobody who could read as under 25.
- WORLD: one coherent elsewhere = DUSTWATER, a dusty frontier town — one
  main street (saloon with swing doors + wide porch, jail with a barred
  door, water tower, hitching posts, troughs, a poster wall, livery
  stable, hay carts, rooftops), desert flats and a mesa rim beyond it.
  Light arc: golden hour (intro) → dusk (block A) → lantern night
  (block B) → dawn (posse gap) → morning (block C) → midday (final
  block) → sunset (outro). The town is held; events change inside it.
- LOOK: photoreal western, shot on 35mm film, visible fine grain; palette
  dust amber + sage green + denim blue; key = low golden sun, then
  lantern warmth at night.
- FORBIDDEN: any legible text anywhere (wanted posters and signs are
  blank weathered paper / bare wood, texture only), licensed characters,
  children, nudity, anything crude or sexual, frozen stills, slow
  openings, singing from anyone but Eli.

## Scene table (song order; all events invented for this build and checked
against USED_EVENTS.md — none of MV-22/23/25/26's events or stagings
reused; MV-23's tailor-shop western is a different world and none of its
stagings — hat-tip entrance, strut, mirror check, swing-door entrance,
hat toss — are repeated; S04 here is an EJECTION out of the doors,
hands up, the reverse direction and a different gag)

Frame windows are cumulative round(t×24); sung spans are the ASR word
spans from SONG_WORDS.json (sheet text, ASR timing).

| S | Frames | Window (s) | Lyric lines (song times) | Tag | Event (Inv.) | Motion motif | Setting / beat |
|---|---|---|---|---|---|---|---|
| S01 | 0–254 | 0.00–10.58 | (instrumental intro) | CUTAWAY | Inv. The Dustwall Arrival | head-on charge | FRAME 0: ALREADY mid-gallop straight at camera across desert flats, dust wall behind, hat low, grin; thunders past camera ~8s, dust swallows the frame |
| S02 | 254–509 | 10.58–21.21 | (intro) | CUTAWAY | Inv. The Wrong-Way Posse | lateral pursuit | Five grown posse riders gallop left-to-right along the mesa rim; the Drifter pops up from behind a foreground rock, watches them pass the wrong way, grins, ducks down |
| S03 | 509–763 | 21.21–31.79 | (intro) | CUTAWAY | Inv. The Main-Street Scatter | retreating dolly | He rides down main street toward a retreating camera; grown townsfolk dive comically into rain barrels, under porches, behind troughs; he tips his hat to each |
| S04 | 763–1018 | 31.79–42.42 | (intro; patter "Thank you" 34.78) | CUTAWAY | Inv. The Swing-Door Ejection | backward stumble | He backs OUT of the saloon swing doors hands raised, grinning, the grown barkeep shaking a fist inside; at the patter beat he sweeps his hat off in a mock bow to the applauding boardwalk crowd, then sidesteps away |
| S05 | 1018–1272 | 42.42–53.00 | (intro) | CUTAWAY | Inv. The Poster-Wall Peek | lateral peek-slide | A wall of BLANK weathered wanted posters (texture only, no marks); he slides in from behind a barrel stack, peers at the wall, pulls his hat lower, slides out |
| S06 | 1272–1524 | 53.00–63.52 | (intro) | CUTAWAY | Inv. The Porch Gathering | advancing push-in | Dusk: lanterns lit along the saloon porch; grown townsfolk settle with mugs and chairs around OLD ELI, guitar on his knee; he raises a hand, the crowd hushes; camera pushes in as he opens his mouth into L01 |
| S07 | 1524–1668 | 63.52–69.52 | L01 63.52–66.42 + L02 66.42–69.52 | SINGING | Inv. The Tale Opens | seated lean | Eli on the porch at dusk sings both lines straight at the crowd, leaning in hard on "wanted man"; crowd mouths closed |
| S08 | 1668–1745 | 69.52–72.72 | L03 (cover) | CUTAWAY | Inv. The Lariat Twist | rope twirl | At a hitching post at dusk the Drifter idly twists a lariat loop in both hands, watching the street; clean visual rhyme for the covered line; mouth closed |
| S09 | 1745–1836 | 72.72–76.52 | L04 72.72–74.38 + L05 74.38–76.52 | SINGING | Inv. The Story Promise | strum-and-point | Eli sings both lines, pointing his guitar neck out at the crowd on "tell you"; crowd leans in |
| S10 | 1836–1981 | 76.52–82.54 | (gap) | CUTAWAY | Inv. The Ridge Silhouette | skyline crossing | Night: a huge moon rises behind the mesa; the Drifter's silhouette crosses the ridge on horseback, horse rears slightly mid-crossing, rides on |
| S11 | 1981–2129 | 82.54–88.72 | L06 82.54–85.36 + L07 85.36–88.72 | SINGING | Inv. The Warning Verse | lantern lean | Lantern-lit porch: Eli sings both lines, a playful fist-shake on "fight"; grown crowd mock-gasps; nobody else is depicted |
| S12 | 2129–2305 | 88.72–96.04 | L08 88.72–91.70 + L09 91.70–96.04 | SINGING | Inv. The Hush Verse | held stillness | Eli drops to a near-whisper delivery for both lines; the grown crowd (all 40s–60s) exchanges worried looks, a woman in her fifties fans herself; lantern dims a touch. No young person anywhere |
| S13 | 2305–2515 | 96.04–104.79 | (gap) | CUTAWAY | Inv. The Dawn Posse | saddle-up mount | First light in the livery yard: the Sheriff and four grown deputies saddle up, mount in sequence, ride out the town gate single file |
| S14 | 2515–2723 | 104.79–113.46 | (gap) | CUTAWAY | Inv. The Hay-Cart Hide | burrowing concealment | The posse thunders past in the foreground while the Drifter burrows into a hay cart midground — hat and eyes above the hay — then sinks as they pass; a hen hops onto the cart |
| S15 | 2723–2840 | 113.46–118.34 | L10 (cover) | CUTAWAY | Inv. The Rooftop Creep | tiptoe creep | Morning: the Drifter tiptoes along a rooftop ridge, arms out for balance, one blink-freeze when a rooster crows below; grown townsfolk point up at him. The picture answers the lyric's question |
| S16 | 2840–2991 | 118.34–124.64 | L11 (cover) | CUTAWAY | Inv. The Firework Supernova | sky burst | A firework rocket launches from behind the water tower and bursts into a huge star over the town — the "supernova" as pure visual pun; the Drifter silhouetted on a rooftop edge watching it bloom |
| S17 | 2991–3184 | 124.64–132.68 | L12+L13 (covers) | CUTAWAY | Inv. The Boot Polish & The Empty Cell | seated rub | One wide midday shot outside the jail: foreground, the Drifter sits on the boardwalk vigorously polishing his boot with a cloth; background, the Sheriff unlocks the jail door, stares into the EMPTY cell, shakes his head at the sky |
| S18 | 3184–3339 | 132.68–139.14 | (gap) | CUTAWAY | Inv. The Tumbleweed Verdict | rolling pass | Deserted midday main street: a lone tumbleweed rolls through, snags on the jail steps, breaks free; the Drifter pops up from behind the trough, snatches his forgotten hat off the steps, gone |
| S19 | 3339–3490 | 139.14–145.40 | L14 139.14–142.38 + L15 142.38–145.40 | SINGING | Inv. The Tale Retold | crowd sway | Midday porch, bigger crowd: Eli sings the repeat; the crowd sways and taps feet around him, mouths closed — only Eli sings |
| S20 | 3490–3564 | 145.40–148.48 | L16 (cover) | CUTAWAY | Inv. The Neckerchief Wring | wringing twist | At a water trough the Drifter wrings out his wet red neckerchief with both hands, water dripping, then snaps it straight and ties it back on |
| S21 | 3564–3699 | 148.48–154.14 | L17 148.48–151.82 + L18 151.82–154.14 | SINGING | Inv. The Tell-Ya Lean | lean-in crescendo | Eli leans further toward camera on each of the four "I tell ya"s, then settles back and sweeps an arm wide on "A story 'bout the Jelqer" |
| S22 | 3699–3814 | 154.14–158.90 | L19 154.98–158.90 (0.84s cover head) | SINGING | Inv. The Final Accusation | pointed stand | Eli rises from his chair during the head beat, points straight at camera on "Tell you what he's done"; the crowd rises behind him; held final frame |
| S23 | 3814–3994 | 158.90–166.42 | (outro) | CUTAWAY | Inv. The Sunset Ride-Off | away-gallop (declared bookend rhyme of S01) | The Drifter gallops AWAY from camera into a huge sunset, dust glowing; half-turns in the saddle ~163s and tips his hat back toward town; final frame small rider against the sun — rhymes S01's head-on charge |

Energy arc (cuts/min): intro = 6 big set-pieces, ~5.7 cuts/min but every
take is continuous high motion at a 153 BPM gallop (internal-motion
density carries it) → verses alternate sung porch takes with covers
(~9–13 cuts/min effective) → block C covers quicken (creep / burst /
two-plane gag) → final block is the densest sung passage + the ride-off.
Tension: the town wants him caught — the posse forms, saddles, passes
within feet of him — and every block tightens it; Release: he always
slips away smiling, and the tale itself is the town's revenge.

Chorus-hook test: the recurring hook is L01/L14 "I said the Jelqer is a
wanted man". Pilot volley = S01 (opener look + gallop), S07 (hook
singing look — Eli proven before the song is fired on his face),
S08 (cover look). QC the pilot before firing the rest.

## Warp / assembly method

Phrase-level smooth warp per singing scene (setpts FIRST, then fps=24),
per MV-26's build_master.py pattern; every segment asserted for frames
AND duration; joined.mp4 probed (3994f AND ~166.42s) before the master
encode. Covers run at natural speed (mild fit factors only, disclosed).
Master encode: burned word-timed karaoke ASS + mov_text + "~ WuBu ~"
gold bug, CRF 18, AAC re-encoded from track.mp3. CRF-18 proof = size
differential vs identical CRF-23 chain. Freezedetect zero events.

## Captions ruling (sheet = text authority)

Caption DISPLAY text comes from lyrics.txt (sheet words, asterisk
censorship intact — the burned-in captions never show the uncensored
words ASR hears); caption TIMES come from SONG_WORDS.json word slots
(sheet words mapped onto the ASR slots of their line; L10's sheet has
7 words vs ASR's 8 slots — mapped proportionally). The two performed
"Thank you" patter bits are captioned as performed (they are audible
in the track; not sheet lines — disclosed in GATE_LOG).
