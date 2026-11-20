# MV-26 PREPRO — "Gotta Poop" (measured plan, 2026-11-20)

Track: 119.616s, measured 127.0 BPM (beat 0.4724s, phase 0.290s). Target master:
exactly 2871 frames @24fps (119.625s container), 1280x720, CRF 18, AAC 48k.
Lyric authority = burned-in sheet (lyrics.txt); timing authority = SONG_WORDS.json
(174 ASR words, 6.14–118.58s). Song shape: 6.1s instrumental intro → distinct
sung blocks (6.14–40.48) → 42s near-continuous "gotta" CHANT (40.48–82.40,
montage problem, NOT per-line generation) → two "Need to go right now" pleas
(85.98 / 93.66) → 21.6s instrumental build → final shouted "Poop!" 117.82.

## Production bible (identity macros — expanded into every vehicle)

- LEAD (S1) = DANNY: a grown man in his early thirties, short messy brown hair,
  light stubble, pale-blue office shirt untucked and rumpled, loosened navy
  striped tie, khaki trousers, brown shoes. Same face, same outfit, every take.
- SUPPORT: grown adults only (30s–60s), each named in its vehicle as a grown
  adult (office workers, a janitor in his 50s, shoppers, wedding guests, a
  bride and groom in their 30s, joggers, a porta-potty attendant in his 40s).
  NO children, NO teenagers, nobody who could read as under 25.
- WORLD: one coherent elsewhere = a single escalating city dash (office →
  corridor → stairwell → elevator lobby → mall → street → wedding marquee →
  park → porta-potty → plaza → restroom door). Danny is the constant; the
  world changes around the dash.
- LOOK: bright photoreal daylight comedy, shot on 35mm film, visible fine
  grain; palette warm amber + sky blue, bone and ink; key = bright daylight.
- FORBIDDEN: any bathroom fixture in use, anything graphic, nudity, text /
  signs / logos / captions rendered in-clip (all signage blank or unreadable),
  children, frozen stills, slow openings.

## The dash (declared recurring spine, escalating — motif law)

THE DASH is the video's connective motion, staged as a DIFFERENT motion
pattern in every slot (sprint → bounce → fold → mash → weave → vault →
squeeze → charge → plead → glide → rise → burst). No slot re-runs another
slot's pattern; each return is a named escalation toward the door.

## Scene table (song order; events invented for this build, checked against
USED_EVENTS.md — none of MV-22/23/25's events or stagings reused)

| S | Out window | Lyric lines (song times) | Tag | Event (Inv.) | Motion motif | Setting / beat |
|---|---|---|---|---|---|---|
| S01 | 0.00–12.90 | "Gotta poop" 6.14, "gotta poop" 7.32, "Need to go right now" 9.22, "Poop poop" 11.20, "gotta go" 12.14 | SINGING | Inv. The Corridor Ignition | corridor sprint | FRAME 0: already mid-sprint down an office corridor, tie streaming; skids toward camera and sings Block A while jogging in place at a water cooler |
| S02 | 12.90–24.74 | "Can't hold it" 16.84, "Poop" 18.44, poop×4 chant 19.64–21.30, "Gotta poop!" 21.80, "Gotta poop" 22.84 | SINGING | Inv. The Locked-Door Dance | bouncing in place | Reaches the office restroom door — LOCKED; bangs, does the knees-together urgent dance, sings at the door |
| S03 | 24.74–32.00 | "Stomach hurts" 28.64 (performed ad-lib, ASR-confirmed) | SINGING | Inv. The Stairwell Fold | folding / clutching | Stairwell landing: doubles over clutching his stomach on the line, straightens, keeps going down |
| S04 | 32.00–40.48 | "Gotta go right now" 32.00, "Gotta poop" ~37.5 | SINGING | Inv. The Wrong-Way Elevator | button-mashing | Elevator lobby: mashes the call button; doors open on a car packed with grown adults going up; he sings squeezed at the doors |
| S05 | 40.48–51.00 | CHANT (montage) | CUTAWAY-chant | Inv. The Mall Slalom | weaving | Mall atrium: slaloms between grown-adult shoppers and kiosks, chanting as he weaves |
| S06 | 51.00–61.50 | CHANT (montage) | CUTAWAY-chant | Inv. The Bench Vault | vaulting | City street: vaults a bench, hurdles a low barrier, chant never stops |
| S07 | 61.50–71.50 | CHANT (montage) | CUTAWAY-chant | Inv. The Wedding Squeeze | squeezing sideways | Wedding reception marquee: side-steps between tables of grown-adult guests, mouthing sorry, chanting under his breath |
| S08 | 71.50–82.40 | CHANT (montage) | CUTAWAY-chant | Inv. The Distant Throne | open-field charge | Park lawn: spots a lone porta-potty far across the grass — hope ignites — charges toward it |
| S09 | 82.40–96.22 | "Need to go right now" 85.98, "Need to go right now" 93.66 | SINGING | Inv. The Porta-Potty Plea | pleading | The porta-potty is OCCUPIED: he knocks, pleads on his knees, sings both lines at the door; attendant shrugs |
| S10 | 96.22–108.00 | (instrumental build) | CUTAWAY | Inv. The Second Door | rising / advancing | Across the plaza he spots a second door (blank, unmarked); rises like a hero, strides into the final run as the music builds |
| S11 | 108.00–119.616 | "Poop!" 117.82 (final shout) | SINGING (one word) | Inv. The Slam & Slide | collapsing in relief | Bursts through the door, slams it, slides down inside a clean bright tiled restroom (no fixture shown), bliss; shouts the final "Poop!" in triumph at 117.82; final held frame rhymes S01's skid (same body angle, opposite emotion) |
| S13 | donor (cuts into 40.48–82.40) | CHANT (montage) | CUTAWAY-chant | Inv. The Platform Dodge | dodging | Subway platform: dodges between grown-adult commuters and pillars, chanting |
| S14 | donor (cuts into 40.48–82.40) | CHANT (montage) | CUTAWAY-chant | Inv. The Walkway Ride | rigid glide | Airport terminal: rides a moving walkway standing rigid, legs crossed, gripping the rail, gliding past travellers |

Energy arc (cuts/min): intro sprint ~30 (one take, internal motion) → blocks
A–C ~20 → CHANT 60+ (sub-cuts on chant onsets / 2-beat grid across S05–S08 +
S13/S14 donors) → plea ~15 → build ~25 rising → payoff hold.
Tension: every scene the door is closer but blocked; release: S11's slam.

Chorus-hook test: pilot volley = S01 (ignition), S05 (chant look), S09 (plea).
QC the pilot before firing the rest.

## Warp / assembly method
Phrase-level smooth warp per scene (setpts FIRST, then fps=24), per MV-23's
build_master.py pattern; every segment asserted for frames AND duration;
joined.mp4 probed (2871f AND ~119.6s) before the master encode. Chant span
assembled as beat/onset sub-cuts across the six chant takes at natural speed.
Master encode: burned word-timed karaoke ASS (MV-2 v7 style) + mov_text +
"~ WuBu ~" gold bug, CRF 18, AAC from track.mp3. CRF-18 proof = size
differential vs identical CRF-23 chain. Freezedetect zero events.
