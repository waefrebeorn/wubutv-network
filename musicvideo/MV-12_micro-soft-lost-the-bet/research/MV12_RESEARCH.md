# MV-12 RESEARCH — "Micro Soft (Lost the Bet)"

**Project:** `musicvideo/MV-12_micro-soft-lost-the-bet/` · **Track:** Suno .mov, 114.2s, md5 `25cf688c8a2cc01d5769dedd02f76923`
**Standing rule this build serves:** MONTAGE RULE (2026-11-10 ~07:30 EST) — montage-first, more funnies, more stuff happening, never one static vantage. MV-11 was approved as slop but boring (single toilet-bowl subject). MV-12 is the first build under the rule.
**Design spine (parent-set):** THE LOGO IS THE CARRY — the era-correct Microsoft logo appears in every scene while the world changes around it. Cartoon caricatures, never photoreal likenesses. The logo itself is a post-rendered graphic, never generated in-clip text.

## 0. TRACK — MEASURED (not claimed)

- **Duration 114.22s** (ffprobe). Suno style claims **128 BPM — MEASURED 131.5 BPM** (period 0.4563s, phase 0.250s; top candidates cluster 129.5–131.5). Use 131.5 BPM as the working grid: **1 beat = 0.456s, 1 bar (4 beats) = 1.83s, 2 bars = 3.65s.**
- **First word at 0.00s — cold open, NO intro.** The track starts singing immediately. No establishing-shot runway; the first frame must already be a gag.
- **Loudest 2s at 100s (−14.2 dB)** = final chorus peak. Quietest 2s at 16s (−22.6 dB) = a stripped pocket inside chorus 1.
- **Energy (5s RMS):** flat-ish throughout (−15.3 to −18.0 dB) — a chant track, not a dynamic arc. Peaks at 50s, 80s, 95–105s. There is no quiet verse to rest in; the montage must supply the dynamics the audio doesn't.
- **Lyrics:** large-v3-turbo, fixed config, NO VAD (MV-11-proven). 186 words, 32 segments. "Micro soft" ASR-garbles as MicroSau/MicroSaft/MicroSaur — sung chant, expected. "Lost the bet" occasionally reads "lost a bed" — ASR artifact, not a lyric.

### Section map (turbo word times; section names from the user's lyric sheet)

| Section | Time | Words / notes |
|---|---|---|
| Chorus 1 | 0.00–~21.3 | "I can't believe Bill Gates named that company after his penis" ×3 + "Micro soft" chant. First word 0.00. |
| Post-Chorus | ~21.3–33.2 | "Micro soft (yeah)" / "He lost the bet (yeah)" — chant, stripped. |
| Verse 2 | 33.2–43.8 | "Steve Jobs laughed so hard" 33.20 · "Bill said I have to do it" 36.42 · "Name the company Micro soft" 39.52 · "That's the bet I lost" 41.50. THE STORY VERSE — the only narrative lines in the song. |
| Pre-Chorus | 43.8–47.4 | "Now we all know the story / Now we all know the joke" (ASR garbles line 2; lyric sheet is authority). |
| Chorus 2 | 47.4–~61.6 | Same hook, second hit. |
| Bridge | ~61.6–76.7 | "Lost the bet / Micro soft / He had to name it" — chant, staccato. |
| Gap | 76.7–79.4 | ~2.6s instrumental. Only real breather in the track. |
| "I'm gonna win" | 79.36–80.86 | ASR hears a line NOT in the lyric sheet ("I'm gonna win"). UNVERIFIED — likely a Suno ad-lib or ASR hallucination; plan coordinator to verify against the audio before building a scene on it. |
| Chorus 3 (final) | 80.9–~102.7 | Third hook, loudest stretch (peak 100s). |
| Outro | 105.2–113.5 | "He lost the bet (yeah)" chant to the end. Track ends 114.22. |

**Plan implication:** 3 choruses of the SAME hook + 1 story verse + 1 bridge. The video cannot repeat the same visual 3 times — each chorus needs a NEW era/world for the same words (chorus 1 = 1975 disco, chorus 2 = 1987–2012 Pac-Man era, chorus 3 = 2012 four-squares/modern). The verse is the only place the bet story is TOLD; the choruses are where it is SHOWN.

---

## THREAD 1 — MICROSOFT LOGO HISTORY (the parody's spine)

### The timeline (verified)

| Era | Logo | Designer / type | What the world looked like |
|---|---|---|---|
| **1975–1980 "Disco"** | MICRO / SOFT stacked, concentric-line groovy letters | Simon Daniels (Aki Lines typeface); Gates + Allen generated the first version in BASIC | Altair 8800 (Jan 1975 *Popular Electronics* cover), paper tape, Albuquerque garage. Two nerds, no office. |
| **1980–1982 "Metal"** | Sharp heavy-metal MICROSOFT, one word, New Zelek font, extended M/R/F | Simon Daniels | IBM deal (1980) — MS-DOS for the IBM PC (1981). First time the name is one word. Metallica's logo came 3 years LATER (the band took inspiration from this, not the reverse). |
| **1982–1987 "Blibbet"** | ITC Avant Garde Gothic, sober sans-serif; the O is stacked horizontal lines | Simon Daniels (3rd and last) | MS-DOS era, IBM PC clones everywhere. The lined O was meant as a CD/disk; employees nicknamed it the "blibbet" and it became a cult object — "Save the Blibbet" petition + buttons when it was retired. |
| **1987–2012 "Pac-Man"** | Helvetica Black Italic, bold; slash cut between "o" and "s"; the O has a Pac-Man bite | Scott Baker (in-house) | Windows 1.0 (1985) → Windows 95 (Aug 24, 1995) → XP (2001) → the whole Windows century. 25-year run, the longest-lived logo. |
| **1994–2002 slogan** | Pac-Man + "Where do you want to go today?" | — | Windows 95 launch, internet arrives. |
| **2002–2006 slogan** | "Empowering us all" (minor) | — | XP era. |
| **2006–2011 slogan** | Pac-Man + "Your potential. Our passion." | — | Vista (2007), Xbox 360. |
| **2011–2012 slogan** | Pac-Man + "Be what's next." | — | Last year of the italic. |
| **2012–present "Four squares"** | Four colour squares (red/green/blue/yellow) + Segoe UI Semibold wordmark, grey, upright | Collective internal effort; Jason Wells led; Pentagram credited in some accounts | Windows 8 / Metro era → cloud/AI era. First logo with a graphic mark beside the wordmark. Squares = Windows (blue), Office (red), Xbox (green), Bing/search (yellow) in the popular reading. |

**Sources:** logotyp.us (Microsoft logo history) · thestreet.com "Microsoft's logo over the years" · fineprintart.com "History of the Microsoft Logo" · logo.com · ghacks.net "Microsoft Company | All Logos | 1975–2022" · itechpost.com · startuptalky.com (slogan dates) · advergize.com (slogan table).

**User-supplied logo refs (in `work/stills/`, reference only):** `ref_logo_timeline_7.jpg` (7-row timeline: '75 / '75–'87 / '87–'12 / '94–'02 / '06–'11 / '11–'12 / NEW) · `ref_logo_timeline_4.jpg` (4-row: 1975 / 1987 / 1994 / 2012) · `ref_logo_1975_disco.jpg` (disco wordmark close-up). These match the verified timeline above — the 7-row version's slogan rows ('94–'02, '06–'11, '11–'12) are slogan eras of the SAME Pac-Man logo, not new logos.

### The REAL name origin — the joke the parody plays against

- **"Micro-Soft" = microcomputer + software.** Suggested by **Paul Allen**; first used by Gates in a letter July 29, 1975; registered Nov 26, 1976. Founded **April 4, 1975, Albuquerque, New Mexico**, to sell BASIC interpreters for the Altair 8800. Gates CEO, Allen the name-guy.
- **There was no bet.** The Gates–Jobs naming bet is the song's invention — pure parody premise. The video's comedy engine is the CONTRAST: the dry real story (two nerds, a hyphen, a magazine cover) vs. the song's lurid invented story (a lost bet, a laughing Jobs, a name Gates is stuck with forever). Play both: show the real founding as the straight setup, then let the bet joke stomp on it.
- **The logo never changed its NAME, only its clothes.** That's the parody's spine and why "the logo stays the same" works as a visual: same word, 50 years, five outfits. The carry is literal — the word MICROSOFT persists while disco → metal → blibbet → italic → squares march past.

### Era gags the timeline hands you (free)

- **Disco logo:** the concentric lines ARE a visual gag already — a logo that looks like a vinyl record / circuit board / sound wave. Animate the lines pulsing to the kick.
- **Metal logo:** a software company dressed as a hair-metal band. Lean in: the logo on a tour poster, pyrotechnics, a guitar solo nobody asked for.
- **Blibbet:** the O is a CD / steering wheel / rising sun. Employees LOVED it enough to petition. Gag: the blibbet as a cult relic, carried on a pillow.
- **Pac-Man bite:** the O literally has a bite taken out of it. Gag: Pac-Man himself swims in and takes the bite, every era.
- **Four squares:** a window made of four coloured tiles. Gag: the tiles as a dance floor, a Rubik's cube, a window someone keeps falling through.

---

## THREAD 2 — GATES vs JOBS LORE (gag-ready, verified only)

### The looks (from the user's 6 supplied photos — describe, don't reproduce)

- **Young Gates:** messy sandy hair, **oversized glasses**, cream cable-knit sweater, grey slacks, loafing on a desk beside a CRT monitor showing MICROSOFT on blue; later, dark pinstripe suit + red patterned tie holding a Windows 1.0 box and grinning. The sweater + glasses + desk-lean is THE Gates silhouette (1983 photo). Caricature lock: sweater, big glasses, messy hair, smug-nerd grin.
- **Young Jobs:** dark shaggy hair, **white shirt with red collar + green striped bow tie**, black double-breasted suit, arms crossed in front of a giant Apple logo; presenting the first Macintosh with both hands open over the keyboard, bow tie, delighted smile. Caricature lock: bow tie, shaggy hair, showman hands, black suit. **NOT the black turtleneck — that look is 1998+, not this era.** The photos the user supplied are the 1970s–80s looks; stay in them.

### 12 gag-ready moments (verified; one-line visual each)

1. **The magazine cover, Jan 1975.** Allen spots the Altair 8800 on the cover of *Popular Electronics* in Harvard Square, sprints to show Gates. VISUAL: a magazine cover that GLOWS; two nerds colliding over it in a dorm hallway.
2. **The phone call that started it.** Gates cold-calls MITS claiming they already have a BASIC interpreter — they don't yet. They write it in 8 weeks. VISUAL: Gates on a rotary phone, lying with total confidence, Allen behind him typing frantically.
3. **The 1977 mugshot.** Gates, 22, arrested in Albuquerque Dec 13, 1977 — speeding in a Porsche, ran a stop sign, no licence on him. Grinning in the booking photo. VISUAL: the grinning mugshot on a police height chart; the chart's lines morph into the disco logo's concentric lines. (Bonus, UNVERIFIED as intentional: the Outlook 2010 default-contact silhouette matches the mugshot outline — Ars Technica overlay; Microsoft never confirmed; Snopes/AFP label it unverified. Use as a wink only if flagged UNVERIFIED.)
4. **Xerox PARC, Dec 1979.** Jobs visits PARC, sees the Alto: GUI, mouse, windows, icons. He later quotes (attributing to Picasso): "Good artists copy, great artists steal" — said in the 1996 *Triumph of the Nerds* interview; the Picasso attribution is Jobs's, and Quote Investigator traces variants of the line back through T.S. Eliot, Faulkner, Stravinsky — Picasso himself is UNVERIFIED as the source. VISUAL: Jobs peeking through a door labelled XEROX while a mouse and a window float out past him; Gates peeking through a SECOND door behind Jobs.
5. **The rich-neighbour line (Pirates of Silicon Valley, 1999 — dramatised).** Gates's movie line: both of them are guys who snuck into rich neighbour Xerox's house to steal a TV; Gates got there first. VISUAL: two cartoon burglars in striped shirts racing to the same open window; a TV labelled GUI. (Flag as film dialogue, not a transcript — the film is a dramatisation of *Fire in the Valley*.)
6. **Macintosh launch, Jan 24, 1984.** Jobs in bow tie + double-breasted suit pulls the Mac out of a bag at the Flint Center; the Mac speaks: "Hello, I am Macintosh." The "1984" Super Bowl ad (Ridley Scott, $500k, aired Jan 22) had run two days earlier. VISUAL: Jobs unzips a bag, a tiny computer pops out waving; the bag is labelled with the disco logo.
7. **Windows 1.0, Nov 1985.** Microsoft ships a GUI a year after the Mac; Jobs accuses Gates of stealing. Gates's real-life answer (per Isaacson): "Well, Steve, I think there's more than one way of looking at it. I think it's more like we both had this rich neighbour named Xerox who left the door open." VISUAL: the same open door from gag 4, now with TWO burglars arguing in front of it.
8. **Jobs ousted, 1985.** Board sides with Sculley; Jobs resigns, founds NeXT the same year. VISUAL: Jobs walking out of Apple HQ carrying a cardboard box labelled PIRATE FLAG; Gates waving from a window.
9. **Windows 95, Aug 24, 1995.** Midnight launch queues; Rolling Stones' "Start Me Up" as the campaign song; Brian Eno composed the startup chime. VISUAL: a queue around the block at midnight; the Start button glowing like a sunrise; Eno at a tiny keyboard composing 3.25 seconds of chime.
10. **Clippy, Office 97 (1996–97).** Clippit, designed by Kevan Atteberry (~260 designs pitched), pops up uninvited: "It looks like you're writing a letter." Disabled by default 2002, gone 2007; TIME's 50 worst inventions list. VISUAL: a paperclip with googly eyes photobombing EVERY era scene — the running gag that never leaves.
11. **The BSOD on stage, Apr 20, 1998.** COMDEX/Windows World demo: Gates's assistant plugs in a scanner, Windows 98 blue-screens in front of the audience; laughter; Gates: "That must be why we're not shipping Windows 98 yet." VISUAL: a giant blue screen descending like a theatre curtain mid-demo; Gates shrugging under it. (The BSOD text itself was originally composed by Steve Ballmer, per Tech Xplore.)
12. **Macworld Boston, Aug 6, 1997 — THE BET'S REAL COUSIN.** Jobs, newly returned, announces Microsoft is investing **$150M in non-voting Apple stock** + 5 years of Office for Mac + IE as default browser. The crowd boos; then Gates appears via satellite, GIANT, looming over Jobs on the screen behind him. Jobs later called it "my worst and stupidest staging event ever… it made me look small, and Apple look small." VISUAL: tiny Jobs on stage; a colossal Gates-face filling the sky behind him; the audience booing in waves. **This is the closest real moment to the song's bet — Jobs on stage, Gates towering, a deal nobody wanted to announce. Stage the bet handshake HERE.** (Deal signed ~3 AM that morning; Gates was supposed to attend in person. Microsoft sold the stake in 2003 for $550M.)

**Sources:** en.wikipedia.org/wiki/Microsoft, en.wikipedia.org/wiki/History_of_Microsoft · thoughtco.com · neowin.net, cultofmac.com, tidbits.com (1997-08-11), stratechery.com, mac-history.net (1997 staging) · subslikescript.com (Pirates script) · pure.mpg.de (Meyer/Spasche paper — PARC visit Dec 1979, Picasso-quote provenance) · poynter.org, americanhistory.si.edu, folklore.org (1984 launch) · techxplore.com (BSOD/Ballmer, Eno chime, Clippy) · thisdayintechhistory.com (1998 BSOD) · mundobytes.com, iplogger.org (Clippy/Bob) · grunge.com, commons.wikimedia.org/wiki/File:Bill_Gates_mugshot.png (mugshot Dec 13, 1977).

### What NOT to stage

- **No photoreal Gates/Jobs.** Caricatures only (sweater-glasses nerd vs bow-tie showman). The user's photos are reference for costume/era, not frames to copy.
- **No real-person lip-sync of the dirty hook.** The singers are cartoon caricatures / a gang-chant crowd; the hook line is a CHANT, not a Gates confession. Keep the joke on the LOGO and the BET, not on a real person's mouth saying it.
- **The bet is fictional.** Never present it as history in any caption/kinetic line. The kinetic type may quote the SONG ("He lost the bet"), never a fake historical claim.

---

## THREAD 3 — MONTAGE-FIRST CRAFT + BETTER FIRING

### Why MV-11 bored (the lesson this build exists to fix)

MV-11 was approved because every gate passed — but one chained world, one subject, one vantage for 172s reads as a screensaver. The continuity method (last-frame→first-frame chaining, one autogenerated stack) is a COHERENCE tool; applied to a whole video it becomes a MONOTONY tool. MV-12 inverts it: **continuity lives in ONE element only (the era logo); everything else changes every cut.** The user's order is explicit: more montage, more funnies, more stuff happening, NOT static vantage shots.

### What the research says (2026)

**Cut density — the numbers:**
- Cut-rate framework (datafield.dev, ch. 20; cutscore.io, Jun 2026): **30+ cuts/min = hyperspeed** (music videos, montages, action); 15–30 = fast (comedy, vlogs); 8–15 = moderate. Short-form runs 30–60+/min. Average shot length 2–5s for most formats, under 2s for frantic ones.
- Beat-cutting arithmetic (umbrellacreators.com, 2026 guide): at 120 BPM, cutting every 2 beats = 1s shots = **60 cuts/min** (energetic montage); every 4 beats (one bar) = 2s shots = **30 cuts/min** (each shot still registers); every 8 beats = 4s = 15/min (calmer). Cutting on EVERY beat sounds right and looks frantic within seconds — vary the rhythm per section, don't flatline it.
- **MV-12 grid (131.5 BPM):** 1 beat 0.456s · 2 beats 0.91s · 1 bar 1.83s · 2 bars 3.65s. Target: **choruses cut every bar (1.83s ≈ 33 cuts/min)**; **verse/pre-chorus every 2 bars (3.65s ≈ 16/min)** so the story lands; **bridge staccato every 2 beats (0.91s ≈ 66/min)** for the chant pile-up; **outro relax to 2 bars**. A new cutting rhythm at each new section is most of what makes an edit feel cut to the music.
- **One readable gag per shot.** A 1.83s shot holds exactly ONE idea (Adobe community montage guidance: shots get shorter and shorter toward a peak; 2–3-frame flashes only at the very climax). If a shot needs two ideas, it needs two shots.

**Parody structure (Weird Al formula):**
- **Shot-for-shot + ONE twist.** "Eat It" recreated "Beat It" obsessively (same dancers, same pool hall, same red jacket) and changed exactly one thing: the climax is a guy struggling with chicken instead of a gang war. "Fat" used the SAME subway set Scorsese shot "Bad" on, same choreography frame-for-frame, in a fat suit. Commit to the bit — half-measures don't go viral. (diffsense.com; manualdobruxo.com.br)
- **One clear idea per edit.** Filmora's mashup research: a familiar setup must register FULLY before the twist drops; one strong contrast lands better than five crammed jokes. For MV-12: the familiar setup is the logo timeline itself (everyone knows these logos); the twist is the bet joke invading each era.
- **Let the absurd stray.** "Amish Paradise" works because Al strays outside the concept (chickens fed pizza; a Buster Keaton barn-raising gag). MV-12's stray layer: Clippy photobombing every era, Pac-Man eating the O, the BSOD curtain. (imvdb.com)
- **Kinetic type as a second channel.** "Word Crimes" (Jarrett Heather, 2014) built the whole video from animated typography — lyrics as the visual, old-vs-new media as the concept. MV-12's kinetic layer carries the hook ("MICRO SOFT" / "HE LOST THE BET") in post, in the era's own typeface (disco lines → metal → Avant Garde → Helvetica Italic → Segoe UI). (pcmworldnews.com)

**AI-video montage technique (2026 practice):**
- **Prompt anatomy (versely.studio, 2026):** a strong video prompt is a shot description — [subject] + [action] + [style] + [lighting] + [camera] + [lens]. Forgetting camera/motion means the model picks its default: "static medium shot, mild drift" — the exact failure MV-11 was criticised for. **Every MV-12 vehicle must name a camera move.**
- **One scene, one action, one camera move per prompt** (blog.picassoia.com / Sora 2 guide). Describing five actions in one clip confuses the model. A take that must do two things is two takes.
- **Image-to-video beats text-to-video for fidelity** (sureprompts.com; wildpines.ai). Generate the still first (compose the gag frame exactly), then animate it. For MV-12: the era still IS the gag frame (logo era + caricatures + one prop); the video prompt adds ONE motion.
- **Multi-shot chaining with LOCKED variables** (versely.studio template 5): lock character description + location + lighting across shots when shots share a world. **MV-12 inverts this:** shots do NOT share a world — each cut is a new era. Lock only TWO things across the whole video: (a) the two caricature designs (sweater-Gates, bow-tie-Jobs), (b) the era logo as post graphic. Everything else (room, decade, camera, props) changes per cut.
- **First+last frame / multi-shot generation** (wildpines.ai): Kling 3.0 / Seedance 2.0 take a sequence description and return a 15s mini-scene with characters locked — use ONLY when shots share characters AND you want zero drift. MV-12 wants drift (era change), so prefer single-shot generations with fresh first frames per cut.
- **Trim heads/tails** — AI clips carry ~0.5s of weirdness at one end; the MV-11 chain method hid this, montage cutting TRIMS it (wildpines.ai).
- **Two-image morph warning (WuBu's own MV-11 finding):** the morph's midpoint is glued to whatever dominates BOTH images; a timing prompt cannot move it. In a montage build this is a FEATURE, not a bug: use two-image calls only for WITHIN-era motion (same world, small move), never for era changes. Era changes are hard cuts to a fresh first frame.

### FIRING RULES FOR THE PLAN COORDINATOR (concrete, not generic)

1. **FRESH FIRST FRAME EVERY CUT.** No chaining between eras. Each scene's vehicle names its own start still (era world + caricatures + one prop). The ONLY continuity device is the era logo (post graphic) + the two caricature designs. A coordinator that chains S14's last frame into S15's first frame has misunderstood the brief — flag it.
2. **CAMERA MOVE IN EVERY VEHICLE, AND NEVER THE SAME MOVE TWICE IN A ROW.** Rotate: whip-pan in · crash zoom out · low-angle push-in · overhead drop · dolly past foreground prop · handheld wobble · static wide ONLY as a punchline (max 1 per chorus). "Static wide" as a default is a REJECT reason on this project.
3. **ONE GAG PER SHOT, READABLE IN 1.8s.** Vehicle = [era world] + [ONE action] + [ONE camera move] + [ONE prop/gag]. If the vehicle text needs a semicolon to list a second action, split the scene.
4. **CUT DENSITY BY SECTION (131.5 BPM grid):** choruses 1 bar/shot (1.83s, ~33 cuts/min) · verse/pre-chorus 2 bars/shot (3.65s) · bridge 2 beats/shot (0.91s, chant pile-up) · outro 2 bars/shot. Slots are 2–4s, NOT 10s. Plan ~35–45 scenes for 114s, not 23.
5. **ERA-LOCK THE CHORUSES:** chorus 1 = 1975–82 (disco + metal) · chorus 2 = 1982–2012 (blibbet + Pac-Man + slogans) · chorus 3 = 2012–present (four squares + modern). Same words, new world each time — that IS the joke.
6. **THE VERSE IS THE ONLY STORY SCENE.** 33.2–43.8s gets the bet told straight: Jobs laughs (33.2) → Gates agrees (36.4) → the naming (39.5) → the regret (41.5). Four beats, four shots, 2 bars each. Do not montage the verse into noise; the story needs to land.
7. **RUNNING GAGS, LAYERED IN POST/ASSEMBLY (not in generation):** (a) Clippy photobombs one shot per chorus; (b) Pac-Man eats the O once per chorus; (c) the era logo as a post-rendered lower-third/centre graphic in the era's real typeface. Generated in-clip text stays banned — the logo is never generated, always composited.
8. **KINETIC TYPE IN POST, ERA-MATCHED:** "MICRO SOFT" / "HE LOST THE BET" rendered in the era's typeface per chorus (disco lines → Helvetica Italic → Segoe UI). SLAM on the hook line, CASCADE on the chant. Same kinetic tooling as MV-9/11 (kinetic_ass.py); same SLAM last-word fix applies.
9. **SINGING RULE (unchanged):** the hook is a gang chant — the crowd/caricatures chant it; NO real-person lip-sync of the hook line; NO photoreal Gates/Jobs mouths. Sung lines get sung pictures only where a caricature mouth is visible and on-beat; otherwise montage.
10. **QC GATES, MONTAGE EDITION:** (a) motion audit per take as usual — but ALSO a **density audit at assembly**: count cuts/min per section vs rule 4; a section 30% under its target density FAILS; (b) **gag-readability check**: every shot's gag must be describable in one sentence by a cold reviewer from the contact sheet — if it needs explaining, it isn't a gag; (c) **vantage audit**: no two consecutive shots from the same angle/distance; (d) logo-era correctness: the era logo in a scene must match the scene's decade (disco logo never appears in a 1997 scene).
11. **VOLLEY SHAPE:** ≤6 videos per volley as always, but a volley here is ~6 SCENES (2–4s each), not 6 ten-second takes. Cap is per generation, not per scene — the coordinator may fire 6 short takes per volley and the plan should budget ~7 volleys for ~40 scenes. Do NOT pad takes to 10s to fill the old shape; slot-length requests (2–4s) are the correct ask.
12. **RESEARCH DEBT, CLOSED:** this report answers the user's "even go further with online research and better firing" — the firing rules above ARE the better firing. The plan coordinator's job is to apply them, not re-research them.

### Sources (Thread 3)

- datafield.dev/why-they-watch/part-04/chapter-20/ (cut-rate framework, beat edits)
- umbrellacreators.com/blog/how-to-edit-video-to-the-beat-of-music (2026 beat-cutting arithmetic)
- cutscore.io/blog/cuts-per-minute (Jun 2026 ranges)
- community.adobe.com (montage quick-cut technique)
- diffsense.com (Eat It shot-for-shot; Jurassic Park claymation)
- manualdobruxo.com.br (Fat / Bad recreation)
- imvdb.com/blog/2013/07/music-video-relapse-amish-paradise-1996-by-weird-al-yankovic
- pcmworldnews.com/2014/07/the-story-behind-the-weird-al-word-crimes-video-with-designer-animator-jarrett-heather/
- versely.studio/blog/ai-video-prompt-engineering-advanced-techniques-2026 (six-part prompt, multi-shot chaining)
- blog.picassoia.com/how-to-make-ai-music-videos-with-sora-2 (one action per prompt)
- sureprompts.com/blog/ai-video-prompting-complete-guide-2026 (image-to-video, 2026 model landscape)
- wildpines.ai/blog/how-i-actually-make-ai-video/ (multi-model 2026 workflow, trim heads/tails)
- filmora.wondershare.com/ai-generation/ai-video-mashup-maker.html (familiar setup → one twist)

---

## UNVERIFIED / FLAG

- "I'm gonna win" at 79.36s — in the audio per ASR, NOT in the user's lyric sheet. Verify against the audio before building on it.
- "Your potential. Our passion." dates: most sources say 2006–2011; one table says 2002–2012 (slogan vs logo-lockup confusion). Use 2006–2011 for the logo lockup.
- Outlook 2010 contact silhouette = Gates mugshot: visual match noted by Ars Technica (2010); Microsoft never confirmed; Snopes/AFP call it unverified. Wink only, flagged.
- Picasso as the source of "good artists copy, great artists steal": Jobs attributed it to Picasso in 1996; Quote Investigator traces the lineage through Eliot/Faulkner/Stravinsky with no firm Picasso original. Attribute the line to JOBS, not to Picasso.
- Metallica-logo claim: the 1980 Microsoft "metal" logo predates Metallica's logo (1983) — repeated across logo histories; treat as lore, not courtroom fact.
- Windows 1.0 release month November 1985 is solid; the exact day (Nov 20) is commonly cited but not re-verified here.
- Slogan "Empowering us all" (2002–2006) appears in some lists as a logo-era slogan and in others as a campaign line only. Minor; not load-bearing.

## REFERENCE STILLS ON DISK (parent-supplied, `work/stills/`)

`ref_logo_1975_disco.jpg` · `ref_logo_timeline_4.jpg` · `ref_logo_timeline_7.jpg` · `ref_gates_young_desk.jpg` · `ref_gates_young_white.jpg` · `ref_gates_windows_box.jpg` · `ref_jobs_young_redcollar.jpg` · `ref_jobs_bowtie_apple.jpg` · `ref_jobs_macintosh.jpg` · `work/stills/stack/` is currently EMPTY — the plan coordinator must build the era stack from these refs; do NOT assume a stack exists.

## HANDOFF TO THE PLAN COORDINATOR

- Track: 114.22s, 131.5 BPM grid (0.456s/beat), cold open at 0.00s, peak 100s, sections in §0.
- Spine: logo eras as chapters; the bet told once (verse 2, 33.2–43.8); the hook shown three times in three different worlds.
- Method: montage-first per the standing MONTAGE RULE — fresh first frame every cut, camera move in every vehicle, one gag per shot, density targets in firing rule 4, volley shape in rule 11.
- Hard gates carried over: adults only; caricatures not photoreal likenesses; logo as post graphic, never generated in-clip text; one 16:9 master, CRF 18, AAC, chat copy ≤50 MB; song is tempo gospel; no generated audio as soundtrack.
