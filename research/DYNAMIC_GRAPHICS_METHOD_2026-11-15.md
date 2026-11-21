# DYNAMIC GRAPHICS METHOD — per-show graphic systems for the new-era shows

**Method Build C · 2026-11-15.** Commissioned by the user's verdict on the
pilots (Telegram msg 445, 2026-11-15): *"better dynamic graphics ideas."*
Companions: Method A (frame-joint cohesion — PANEL WORKFLOW SPEC v2 delta,
`research/JOINT_COHESION_METHOD_2026-11-15.md`), Method B (conversation +
continuity ledger), the FIRST-SECOND DOCTRINE, and the POPPING VISUALS TV
PLAYBOOK. Where this method touches joints, Method A's rules govern and
this method defers; where it touches writing, the doctrine governs. All
named devices below are **house inventions** built on the sourced
principles cited in §7 — no device is claimed as field practice.

---

## §0 — THE ARGUMENT IN ONE PARAGRAPH

Everything the generator makes is re-rendered, and everything re-rendered
drifts: PILOT-4's Clerk held in the units whose call carried her sheet and
was re-invented in the units whose call didn't. The post graphic layer is
the **only pixel-exact repeatable element in the whole pipeline** — a tally
stroke, a stamp, a rendered digit is composited, not generated, so it is
bit-identical on its fiftieth appearance. Broadcast learned this first:
BBC Two's junction system lets trailers "vary hugely in style and tone"
because every one carries the same curve motif — "the glue that holds the
whole system together" (Superunion, §7). Sky Sports' 2025 rebrand made
the same move at larger scale, retiring six sport-specific typefaces for
one system whose logo became "the ground the sport happens on." Our
version: **the graphic layer is each show's second cast — the part of the
cast that cannot drift — and it is where the show's serial memory lives.**
The generator forgets between units; the drawn tally does not.

---

## §1 — THE SHARED SYSTEM (rules G1–G8, binding on all five shows)

**G1. POST ONLY, NEVER GENERATED.** Every graphic in this method is
rendered in post (code, ASS, or ffmpeg filters) and composited in
assembly. No device may ask the generator for text, numbers, tallies,
stamps, or diagrams — the generator garbles them, and a garbled graphic
is worse than none. The only text inside generated picture remains the
standing exception: in-world writing that IS the pictured subject (a
roster page the camera is reading, a count board the scene is about),
which the picture layer owns and QC gates as before. This method's
graphics are how we get that writing *right* when it has to be exact.

**G2. ONE GRAPHIC GRAMMAR PER SHOW, LOCKED IN THE KIT.** Each show's
graphic system — devices, geometry, palette, fonts, motion behaviours,
ledger inputs — is specified on GFX cards stored in the show kit beside
the panels, and freezes when an episode ships, under the same discipline
as the panel kit (playbook §4). A device change is a kit amendment,
logged; a device may not be improvised per episode.

**G3. THE INVARIANT.** Every show has exactly ONE invariant graphic
element that appears in **every unit of every episode**: same geometry,
same palette, same screen-region family, same motion behaviour. This is
the show's curve motif — the thing a muted, logo-less frame uses to name
its show (playbook §2's law, carried by graphics instead of sets). The
invariants: THE MACHINE — the Dead Channel strip (§2.1a). THE TENTH
SECOND — the Cull Clock (§2.2a). THE ROSTER — the Wet Circle's ink
(§2.3a; the circle itself fires per §3, its ink style is the invariant
texture on all roster graphics). THE COUNT — the Split Total (§2.4a).
THE LAST SEAT — the Seat Map (§2.5a).

**G4. BEHAVIOUR IS MEANING.** Viewers learn a system's *behaviour*, not
just its assets: consistent movement choices are how a sequence
communicates (IBM Design Language's motion guidance, via §7). So motion
behaviour is fixed per information class and never varies for variety's
sake: new facts always enter the same way, settled facts always rest the
same way, the joint event always moves the same way. Timing grammar is
borrowed from lower-third craft and tightened to our atom: entrances
0.3–0.5 s (one clean move — slide, wipe, draw-on; never a bounce),
holds long enough to read twice, exits faster than entrances and
humble. A behaviour that fires only when it *means* something stays
legible; a celebratory move spent everywhere signifies nothing (§7).

**G5. PALETTE AND TYPE LOCK.** Graphics draw from the station six-colour
system (INK, CADMIUM, FOREST, COBALT, VERMILION, BONE) with one accent
assigned per show at kit lock, and set type in the house display faces
(Noto Sans Bold / Noto Sans Black — the kinetic-type proof faces,
verified on this VM). Two graphic colours + BONE + INK maximum in any
one frame. The graphics palette never spends the picture layer's
scene-inconsistent colour: the one wrong thing in a frame (doctrine F2)
belongs to the picture; a graphic that is also a wrong colour makes two
violations and both read worse.

**G6. DIEGETIC FIRST.** Graphics must read as the world's own
instruments — the board, the ledger, the stamp, the chalk, the monitor —
not as broadcaster furniture pasted over the fiction. The one sanctioned
piece of station furniture is the `~ WuBu ~` corner bug (already house
practice, drawn bottom-right in gold in post — PILOT-4 CUTLIST). Dallas
Sthlm's rule for Uppdrag Granskning was that it must "never be unclear
what is branding and what is content"; ours is the mirror image: it must
never be unclear that the graphic belongs to the *world* — the branding
layer is the bug and nothing else.

**G7. THE LINE OWNS 7–9s.** No graphic event may start inside a unit's
spoken-line slot (7–9s). Graphic events live at the HOOK (0–1.5s, subject
to §3's frame-0 rule), the TURN (4–7s), and the CLIFF/joint (9–10s and
across it, per §3). During the line the viewer is listening; a graphic
igniting then is competing with the show's only voice.

**G8. DETERMINISTIC OR IT DOESN'T SHIP.** Every device is code with
named inputs (episode number, ledger values, beat times). Same inputs →
same pixels, re-renderable on demand. A graphic that exists only as a
hand-tweaked render is a panel that can't be re-fired: banned.

---

## §2 — PER-SHOW DEVICES

Each device: what it is · when it fires · route class (pipeline classes
defined in §5: **P** = PIL frame renderer, **A** = ASS, **F** = ffmpeg
native filters, **B** = Blender one-time kit asset). "Ledger input" names
the serial-state value the device consumes from Method B's continuity
ledger — the mechanism that makes the graphics anti-recursive (§3.4).

### 2.1 SHOW-1 — THE MACHINE (accent: COBALT)

**2.1a THE DEAD CHANNEL — invariant.** A monitor readout strip rendered
from the episode's *own assembled audio* (ffmpeg `showwaves`, mode=line):
the sound of the episode, drawn as the machine hears it. In monitor
full-frame shots it sits in the monitor's lower bezel zone; in room shots
it runs as a thin strip along the frame's lower edge inside the cutting
room's monitor bank area per the kit card. Its story behaviour: **the
waveform flatlines exactly where the machine drops a word** — where a
mouth visibly sings and nothing sounds, the strip is a dead line beside
the moving mouth. The doctrine's SHOW-1 opening (a singer's mouth moving
in total silence) gets its graphic form: the wrongness, drawn. *Fires:*
ambient in every unit (invariant); the flatline event lands at the HOOK
of the unit where the dropped word occurs and at every dropped-word TURN.
*Route:* F (showwaves from the conformed audio slice; thin line mode —
the MV skill's compression note stands: `mode=cline` runs ≈6.6 Mbps at
720p, so line mode, thin strip). *Ledger input:* the dropped-word log
(which words the machine dropped, per episode).

**2.1b THE VOLLEY BOARD.** The cutting room's take slate, post-rendered:
a grid of the episode's take numbers that ticks keeps and strikes
rejects as the episode proceeds — the machine's paperwork, accumulating
inside the fiction. When the crew discusses a take, the board already
shows its verdict. *Fires:* TURN slots; also the show's designated
graphic-match element at declared BREAKs (Method A J14 — the board's
grid is the shape rhyme a break may cut on). *Route:* P. *Ledger input:*
the episode's take log (mirrors TAKE_HISTORY; the fiction reads the
production's own paperwork — the show is about making these videos, so
its graphics are allowed to be the real ones).

**2.1c THE EARLY READOUT.** A small frame-counter-style timecode in the
monitor corner (drawtext, tabular figures) that runs **ahead** of the
episode's true elapsed time by an offset that grows one second per
episode. Nobody comments on it. It is the machine's fixes arriving
before the mistakes they fix, drawn as a number — lore shown, never
explained, in the graphic layer. *Fires:* ambient in monitor shots.
*Route:* F (drawtext timecode expression). *Ledger input:* episode
number (offset = episode number, in seconds).

### 2.2 SHOW-2 — THE TENTH SECOND (accent: CADMIUM)

**2.2a THE CULL CLOCK — invariant.** A chalk-textured segmented ring,
fixed in its kit corner, that empties over exactly the unit's 10.0 s and
**snaps full on the joint frame**. The show doc demands the countdown be
visible ("the audience always knows which second it is"); the clock is
that demand as a system. Its reset is the joint's punctuation: the snap
lands exactly on the cut (§3.2), so every cull in the fiction is marked
by the same drawn event. Chalk texture (BONE strokes, slight edge
jitter baked into the ring segments) ties it to the Watcher's wall —
chalk survives the cull, and so does the clock, because we draw it.
*Fires:* continuous, every unit; snap event at every joint. *Route:* P
(renderAt(t) ring, one full ring-cycle rendered per unit). *Ledger
input:* none (it is the atom itself).

**2.2b THE STAMP.** The parcel stamp: a rotated rectangular stamp —
cull number + address fragment in tabular type — that SLAMS onto the
parcel at the carry moment (the countdown renderer's back-out spring,
the move ASS cannot express). Each unit's stamp increments the cull
number, continuing the fiction's count across episodes: the audience
can audit the arithmetic. *Fires:* CLIFF or the following HOOK, on the
unit where the carry changes hands or the parcel changes state; max
one per unit. *Route:* P (rotated PNG sequence). Preferred placement
on-parcel where the take's parcel position is QC-verified; fallback is
the kit's frame-corner furniture position — never a guessed mid-frame
placement (§6, risk 1). *Ledger input:* the cull number (serial,
never resets).

**2.2c THE CHALK TALLY.** The Watcher's wall tally, post-rendered as
chalk strokes that draw themselves on: one mark per unit, accumulating
across the episode and **across episodes** — the wall is the show's
memory, and because we draw it, the tally never drifts, never resets,
never loses a mark to a re-render. At each unit's HOOK the wall state
in frame is exactly the accumulated marks; the one changed detail the
show stages lives in the picture around it. *Fires:* HOOK of units 2+
(draw-on of the new mark may straddle the joint, §3.1). *Route:* P
(stroke PNGs, reveal by crop-wipe). *Ledger input:* units elapsed in
the show's whole run.

### 2.3 SHOW-3 — THE ROSTER (accent: VERMILION — the ink)

**2.3a THE WET CIRCLE — the show's signature event.** A hand-drawn-style
circle, rendered in post as an irregular wet-ink stroke, that **draws
itself around a name on the roster page — with no hand in the room.**
The doctrine's SHOW-3 frame 0 is exactly this impossibility ("one name
freshly circled in wet ink with no hand in the room"); post-rendering
the circle lets the circling *happen on screen*, mid-unit, as an event
the Keeper watches happen. The stroke's irregular edge and slight bleed
are baked into the stroke assets; the ink's colour and texture are the
show's invariant graphic texture across all its devices. *Fires:* HOOK
(the circle completes around the episode's name inside the first
second's aftermath — it may be already complete at frame 0 per the
doctrine frame, in which case the *next* circle is the event); CLIFF
(a second circle begins around a name not yet read — the cliff's
unspent fact, drawn). *Route:* P (stroke sequence, alpha), keyframed
to the page position per take — one circle per unit maximum (§6,
risk 1). *Ledger input:* the roster itself — which names are circled
is ledger state and never un-circles.

**2.3b THE HAND THAT ISN'T.** Names write themselves onto the page,
stroke-revealed, in the roster's hand — the post version of the show's
name handoff (spoken at the cliff → written at the next hook). Its
production virtue is exactness: the playbook's legibility gate ("if it
can't be read on a phone at arm's length, the handoff didn't happen")
is passed by construction, and the written name is *character-exact*
the spoken name, every time — the generator's handwriting is never
trusted with the chain. *Fires:* HOOK (the name lands written as the
unit opens; the reveal may straddle the joint, §3.1). *Route:* P/A
(stroke-reveal wipe over a set name plate). *Font honesty:* the house
font set has no true handwriting face (verified: Noto / DejaVu /
Liberation families only) — the kit stands in Noto Serif Italic as
"the hand" until a handwriting face is added to the kit; the Wet
Circle, being a drawn stroke and font-free, carries the hand illusion
in the meantime (§6, risk 3). *Ledger input:* the name chain.

**2.3c THE DISPATCHER'S LOG.** A typewriter-register log line that
types itself onto the log book's page margin at a STATE slot: the
building's receipt for the reading just heard (time, name, kept). One
per episode maximum — it is the device nearest the caption line, so it
is rationed hardest (§4). *Fires:* STATE (1.5–4s), never during the
line, never at a joint. *Route:* A (drawtext/ASS type-on). *Ledger
input:* the Dispatcher's log (which is itself a roster — show canon).

### 2.4 SHOW-4 — THE COUNT (accent: FOREST)

**2.4a THE SPLIT TOTAL — invariant.** The show's two totals — the
board's count and the Clerk's ledger count — rendered as code type in
their two house styles (board: Noto Sans Black, lit-board white on
INK; ledger: Noto Serif, ink on BONE), **disagreeing by exactly one**,
present in every unit the desk is in frame and as a furniture pair in
the kit corner when it isn't. The doctrine's SHOW-4 frame 0 ("two
totals in frame that disagree by exactly one") is delivered with
guaranteed legibility and guaranteed arithmetic. At the TURN, one
digit **migrates**: it slides from the board total to the ledger total,
changing style mid-travel — the number between ours, moving. *Fires:*
ambient (invariant); the migration event at the TURN; the increment
event at the CLIFF (§3). *Route:* P (the countdown proof renderer's
spring vocabulary). *Ledger input:* the count — the show's master
serial value, continuous across episodes (show doc: "the show's
numbers are continuous across episodes, and the audience can check").

**2.4b THE TALLY THAT RE-COUNTS ITSELF.** A five-bar-gate tally cluster
that, at the TURN, un-draws one of its marks and re-draws it in the
other ledger's style — the count auditing itself on screen, the audit
as a visible event. *Fires:* TURN, max one per episode (it is the
show's biggest graphic event; scarcity is its meaning). *Route:* P.
*Ledger input:* the audit state (which side currently holds the
disputed mark).

**2.4c THE n/? CHIP.** Family-I furniture, house pattern from the
countdown proof (its "n / 5" progress chip): a small counter chip,
"n counted / ? ", that increments **on the naming beat** — the frame
the counted thing is named — never between beats. The denominator is
always "?": the count never completes, drawn as furniture. *Fires:*
on naming beats inside units; never at frame 0. *Route:* A/P.
*Ledger input:* n = the count.

### 2.5 SHOW-5 — THE LAST SEAT (accent: BONE — light itself)

**2.5a THE SEAT MAP — invariant.** A theatre seat-map diagram: a grid
of seat glyphs, all dark but one. The lit seat is the viewer's. Across
episodes **the lit seat moves by exactly one position** — the viewer
is migrating through the house, and nobody comments. The map is the
show's invariant and its serial clock: a returning viewer reads the
season's progress off the map's one lit glyph. *Fires:* HOOK of the
episode's first unit (the map state shown as the act begins) and as
the episode's final graphic at the last CLIFF. *Route:* P (grid
renderer; the lit position is one integer). *Ledger input:* the seat
position (Method B ledger field; the map is a graphic that carries
serial state in one number).

**2.5b THE SPOTLIGHT CONE.** A rendered light cone — gradient wedge,
additive-feel alpha — from the dark at the back of the house toward
the stage, behaving as a graphic actor: it narrows at the TURN (the
seat's attention focusing), widens at the CLIFF, and at designated
joints it **sweeps across the frame** — the sweep's bright edge
crossing the lens is a joint cover (§3.2), the drawn form of the
hidden-cut carrier "light at the lens." The cone rhymes with the
generated stage light; it does not pretend to be it. *Fires:* TURN,
CLIFF, and swept joints (max one swept joint per episode). *Route:*
F/P (gradient wedge PNG sequence, overlay with animated position;
a static gradient is a geq/PNG one-off). *Ledger input:* none.

**2.5c THE TWO TICKETS.** The Usher's two tickets for a house of one
seat (doctrine SHOW-5 frame: "the USHER's hands hold two tickets for
a house of one seat"), post-rendered as a ticket-stub graphic in the
near-foreground furniture position: the stub's printed seat number is
the episode number, and one stub of the pair tears itself along its
perforation per episode — the torn halves accumulate in the stub's
design across the season. *Fires:* HOOK, from ~1.5s (never frame 0,
§3.3). *Route:* P. *Ledger input:* episode number; torn count.

---

## §3 — GRAPHICS AS COHESION (the joint rules)

Method A established that our joints cannot be made invisible: the
generator re-renders everything, the seam floor is MAE ~43–52, and
chaining converts "a different room with a different woman" into "the
same moment, re-rendered." Graphics do not lower that floor. What they
do is give the eye a **constant to hold while the floor moves** — the
classical graphical-match finding: matched shots joined at a cut hold
the viewer's attention on the constant element "whilst the rest
gradually changes," and the matched element works best when it is
salient and moving (§7). A face cannot be that constant (it is the
thing that drifts). A drawn object can. The rules:

**3.1 STRADDLE (strongest; JOINT-class boundaries).** A graphic event
begins in unit N's cliff and completes in unit N+1's hook, across the
cut: the Wet Circle finishing its stroke across the joint; the Chalk
Tally's new mark drawing on across it; the Hand That Isn't completing
the written name across it; a Split Total digit mid-migration across
it. The eye follows the drawn event; the picture swap happens
underneath it. This is Method A's J9 straddle rule with the carry
made of ink instead of footage — and ink, unlike a generated handoff,
is frame-exact: the stroke's position at the cut is a number in the
renderer, not a hope in a prompt. *Constraint:* a straddle rides a
boundary that is ALSO chained/resumed per Method A J3. The graphic
straddle adds to chaining; it never substitutes for it.

**3.2 SNAP / SWEEP (punctuation on the cut).** An invariant event timed
exactly ON the cut: the Cull Clock snapping full on the joint frame;
the Spotlight Cone's bright edge crossing the lens at the cut. The
graphic's own event gives the cut a diegetic reason — the cull
*happens*, the seat *looks* — so the viewer reads the seam as an event
in the fiction rather than an edit. Channel 4's ident system designs
its world-to-world transitions the same way: "overlapping elements,
light spill and movement sympathetic to each environment, so that
every scene feels surprising but not jarring" (§7). *Constraint:*
max one snap/sweep event per joint, and the event must be the show's
own invariant behaving — never a novel effect invented for one seam.

**3.3 MATCH (declared BREAKs).** Method A J14 already licenses a BREAK
whose two sides share "a named graphic match (shape/colour/composition
rhyme)." This method supplies the matches: the Volley Board's grid →
the next world's grid-like set dressing; the Cull Clock's ring → a
round object in the new world at the same screen position; the Split
Total's two-style pair → any two-style pair (board/ledger, stage/seat).
The match must be named in the episode plan at script time (Method A
J2's discipline: the joint is designed at planning, not rescued in
the edit).

**3.4 GRAPHICS CARRY THE SERIAL NUMBERS.** Because every device
consumes ledger state (cull number, tally total, circled names, the
count, the seat position), the graphic layer **cannot repeat itself**
as long as the ledger advances: even if a generated face drifts back
to a default, the drawn tally says this is cull 414, not 412. This is
the direct answer to the user's recursion worry (msg 440/445):
recurrence in the picture is forgiven when the fiction's paperwork
proves time has passed. Production rule: **an episode whose ledger
values do not advance may not ship** — if the count, the tally, the
seat, and the roster are all unchanged, the episode is a repeat
wearing a new take, whatever the picture does.

**3.5 HARD LIMITS — what graphics may NOT do at a joint.**

- **Never rescue a failed Joint Gate.** Method A J13 bans dissolves
  from rescuing a failed joint; the same law binds graphics. A joint
  that FAILS the Joint Gate goes through Method A's remedy ladder
  (re-place, re-trim, re-derive, reclassify) — a graphic straddle
  laid over a failed joint is a banned cosmetic, and a master with a
  failed joint does not ship, however good the ink looks.
- **Never open on episode frame 0.** Frame 0 is the generated peak
  image, already wrong, sound-off legible, no text (doctrine F1–F4;
  playbook §1a). The invariant may be *present* from frame 0 in its
  ambient state (the clock mid-count, the Dead Channel strip running,
  the Split Total resting) — presence is allowed; **no graphic EVENT
  may start before ~1.5s** in unit 1. (Unit 2+ joints are exempt: a
  straddle/snap at a joint is joint furniture, governed by 3.1/3.2.)
  The `~ WuBu ~` bug is pre-existing station furniture and is not a
  graphic event under this rule.
- **Never ignite during the line** (G7) — including at joints: a
  straddle that would complete inside the next unit's line slot is
  re-timed to complete in its hook.
- **Density cap: one graphic event per unit**, plus invariant
  ambience. Doctrine F2 allows one wrong thing per frame; a big
  graphic event IS a wrong thing, so when it fires, it is the unit's
  one event — the picture's staged change waits for another unit.
- **The gate measures picture only.** Assembly order (§5.5) runs the
  Joint Gate on the joined picture BEFORE the graphic composite, so
  no overlay can game the seam MAE. Graphics are audited separately,
  on the finished master (§5.6).

---

## §4 — GRAPHICS ARE NOT CAPTIONS (the line, and the kinetic-type ruling)

**4.1 THE THREE-QUESTION TEST.** A graphic is legal only if all three
answers are yes. (1) *Is it the show's subject or the world's
instrument?* Board totals, roster names, stamps, tallies, logs, slates
— the fiction's paperwork — yes. Words a character is saying — no.
(2) *Would it exist if nobody spoke?* A tally exists in silence; a
subtitle does not. (3) *Does it stay out of the audio channel's way?*
A graphic may render a spoken token **only after the speech ends**,
as the handoff object — the COUNT's cliff number is spoken at 9–10s
and shown at the next unit's hook; the ROSTER's cliff name likewise.
Simultaneous with its own spoken form, any rendered word is a caption
wearing a costume: banned. Every episode's GATE_LOG gets a graphic
audit row answering the three questions per device used.

**4.2 KINETIC TYPE OF SPOKEN WORDS — what transfers, what doesn't.**
From the MV side (visual-mv-forms skill, Families A/D/G):

- **TRANSFERS — the craft.** The timing grammar of the five house
  moves (SLAM's 150 ms settle, CASCADE's onset-locked builds, STACK's
  row discipline), the palette law, the house faces, burn-in-never-
  soft-mux, and HIGHLIGHT's core discipline (the full line present;
  only the active element moves). These govern how the fiction's
  documents move: the Split Total's migrating digit is a HIGHLIGHT
  move; the Stamp is a SLAM with a spring.
- **TRANSFERS — the sync law.** Graphic events land on measured times
  (the naming beat, the joint frame), never approximately — the MV
  rule "a counter hits 7 ON the word 'seven', never after" is the
  n/? chip's rule and the stamp's rule verbatim.
- **DOESN'T TRANSFER — lyric type as a standing layer.** In an MV the
  words are the song and type is a sanctioned picture. In the shows,
  kinetic-typed dialogue is a subtitle with better PR: **banned for
  spoken dialogue.** Legal kinetic type in the shows is the fiction's
  own documents only — log lines, slates, stamp text, board figures,
  roster names: text that belongs to objects in the world.
- **THE ONE NAMED EXCEPTION — THE MACHINE's monitor transcript.** The
  machine transcribes the song; the transcription is a document inside
  the fiction, and the show's premise is that it is *wrong*. The
  monitor may therefore display a typed line **only when it disagrees
  with, drops, or comments on the sung line** — the dropped word shown
  missing, the misheard word shown wrong. If the typed line duplicates
  the sung line, it is a caption: reject at the graphic audit.
- **Name straps / lower thirds: banned outright.** Broadcast lower
  thirds exist to identify speakers; our soap grammar wants
  recognition earned by sets, faces, and the invariant. A name strap
  is a caption's cousin and spends the audience's reading on furniture
  instead of the fiction. No exceptions.

---

## §5 — PRODUCTION PIPELINE (per device class, costed at 720p)

House encode law stands throughout: one 16:9 master, 1280×720, 24 fps,
CRF 18, AAC, faststart; graphics composite inside the master encode.

**5.1 CLASS P — PIL FRAME RENDERERS (the house code-render route).**
Pattern proven on this VM by the visual-forms proofs (`kinetic_ass.py`,
`render_countdown_proof.py`, `render_visualizer_proof.py` — deterministic
`renderAt(t)` → PNG sequence → ffmpeg encode; the countdown proof's
back-out springs, accumulating chips, and n/5 counter are the direct
ancestors of the Stamp, the Split Total, and the n/? chip). PIL drawing
at 1280×720 is CPU-trivial (tens of ms per frame for stroke/type work);
a 10 s unit's graphic layer renders in well under a minute. *Devices:*
Cull Clock, Stamp, Chalk Tally, Wet Circle, Hand That Isn't, Volley
Board, Split Total, Tally Re-count, Seat Map, Two Tickets, Spotlight
Cone (wedge sequences). *Composite:* one `overlay` input per graphic
layer in the master filtergraph; **maximum two graphic layers + the
bug per encode.**

**5.2 CLASS A — ASS.** Hand-authored or generated .ass burned at the
master encode (libass; the kinetic tool's style law applies: BONE
primary, INK outline 4, one display face). *Devices:* Dispatcher's
Log (type-on), n/? chip (simple form), Early Readout fallback.
*Limits (honest):* libass `\t` is a power curve, not a spring — no
overshoot; anything needing a spring goes Class P. Cost: negligible.

**5.3 CLASS F — FFMPEG NATIVE FILTERS.** `showwaves`/`showspectrum`
(audio-reactive, sync intrinsic — the graphic is drawn *from* the
sound), `drawtext` (timecode expressions, tabular figures), `geq` /
gradient PNGs (cone bases, washes). *Devices:* Dead Channel
(showwaves mode=line off the conformed episode audio), Early Readout
(drawtext), Spotlight Cone base. *Cost:* filter-time only, no frame
files. *Note:* the Dead Channel is composited after audio conform —
it renders from the assembled audio slice, so an audio change
re-renders the strip (cheap, same class).

**5.4 CLASS B — BLENDER (fenced).** Blender 4.5.15 LTS is on the VM;
Cycles CPU is proven and EEVEE is blocked (no libEGL); measured 720p
cost ≈ 1–2 min/frame makes a 3 s accent ≈ 1.2–2.4 CPU-hours. **Verdict:
Blender is for one-time kit assets only** — an element rendered once
at kit lock and reused as a looping video asset (e.g., a physical
tally-gate token for THE COUNT, a model-theatre seat map for THE LAST
SEAT) — **never per-episode.** No device in §2 requires Class B;
each show *may* commission one hero asset at kit lock, deferred until
the Class P version has shipped and proven the device.

**5.5 ASSEMBLY INTEGRATION (order is law).** (1) Conform picture
segments → joined picture. (2) Probe joined picture (frame count =
plan). (3) **Joint Gate on the joined picture** (Method A §6 — the
gate never sees an overlay). (4) Composite graphic layers + bug in
the single master encode (CRF 18). (5) Master QC (§5.6). A graphic
note in the CUTLIST names, per unit: device, fire slot, ledger inputs,
layer order. Devices are planned at script time (Method A J2
discipline), never invented in assembly.

**5.6 GRAPHIC QC (on the finished master).** Per episode, logged in
GATE_LOG beside the Joint Gate: (a) legibility — every rendered word/
figure readable at phone size on extracted frames over the actual
footage (the playbook's arm's-length test); (b) the §4.1 three-question
audit per device; (c) arithmetic audit — counts, tallies, cull numbers
checked against the ledger (the audience counts too; so do we, first);
(d) frame-0 audit — no graphic event started before ~1.5s of unit 1;
(e) line-slot audit — no graphic event started inside any 7–9s slot.

---

## §6 — OPEN RISKS

1. **Tracking.** On-object devices (Wet Circle on the page, Stamp on
   the parcel, Split Total on the board) must sit on generated objects
   that move unpredictably. We have no auto-tracking in the house
   stack. Mitigations, in order: design furniture-first (fixed screen
   regions) wherever the fiction allows; cap on-object devices at one
   per unit and keyframe their position manually in assembly (bounded
   labour, minutes per unit); if a take's object won't hold still,
   the device falls back to its furniture variant or is cut — a
   floating circle chasing a page is worse than no circle.
2. **Caption creep.** Every production conversation will push the Log,
   the Slate, and the Board to say more. The §4.1 test and the GATE_LOG
   audit row are the only defences; they are cheap and they are
   mandatory.
3. **The missing hand.** No handwriting face exists in the house font
   set (verified this build). THE ROSTER's written names stand in a
   serif italic until a handwriting face is added to the kit; if the
   stand-in reads as "typed," 2.3b weakens — the Wet Circle (font-free)
   is the hedge.
4. **Palette collision.** A CADMIUM stamp on a CADMIUM-lit take
   vanishes; a BONE clock on a BONE wall is wallpaper. Kit rule: each
   show's graphic palette is chosen against its WORLD plates at kit
   lock — check the plates, not the palette chart — and the §5.6
   legibility audit runs over real footage, not plates.
5. **Wallpaper risk.** An invariant the audience stops seeing stops
   carrying identity (doctrine §5.4: lore as wallpaper). Defence: the
   invariant must DO something once per episode — the clock's reset is
   watched because the fiction runs on it; the tally matters because
   the Watcher writes it. A device that only decorates for a full
   episode gets flagged in the graphic audit.
6. **Two-layer ceiling.** The §5.1 composite cap (two graphic layers +
   bug) is an encode-simplicity rule, not a render limit; an episode
   design needing three simultaneous layers must pre-composite two of
   them into one Class P sequence. Plan for it at script time.
7. **Audio dependence.** The Dead Channel is only as honest as the
   conformed audio; if an episode ships a wordless unit, the strip
   runs flat for 10 s — which is either the gag or a bug, and the
   CUTLIST must say which, in advance.

---

## §7 — SOURCES

Web (accessed 2026-11-15; X not used — cross-platform per standing
order):
- BBC Two / Superunion junction system — 25 "moods," one curve motif
  in every ident as "the glue that holds the whole system together":
  https://www.brandimpactawards.com/trophies/bestofshow
- Sky Creative, Sky Sports 2025 rebrand — six typefaces retired for
  one system; the logo as "The Stage," the ground content happens on:
  https://creatypestudio.co/sky-creative-sky-sports-rebrand/
- Channel 4 2023 idents (4creative/Pentagram) — the "4" as traveller/
  portal unifying 25 scenes by 17 makers; transitions designed with
  "overlapping elements, light spill and movement sympathetic to each
  environment, so that every scene feels surprising but not jarring":
  https://www.channel4.com/press/news/channel-4-unveils-ground-breaking-new-series-idents-reflect-modern-britain
  and https://www.creativereview.co.uk/channel-4-idents-2024/
- Dallas Sthlm on Uppdrag Granskning — the "search lights" identity
  catalyst; graphics integral to storytelling, never an overlay; never
  unclear what is branding vs content:
  https://www.red-dot.org/magazine/interview-dallas-sthlm
- Motion-design consistency practice — viewers learn behaviour, not
  just assets; consistent movement choices communicate (IBM Design
  Language motion guidance); separate fixed rules from content
  decisions: https://open-design.ai/blog/motion-graphics-brand-consistency/
- Lower-third craft — two-tier anatomy; animate-in 0.3–0.7 s, hold to
  read twice, exit faster; title-safe placement:
  https://anfx.co/blog/lower-thirds-design-rules-free-templates/
- Graphical match / hiding a cut — attention held on the matched
  constant while the rest changes; salience + movement hold the eye:
  https://1library.net/article/graphical-match-focus-constant-hiding-cut.zp0pwpvq
- Hidden-cut carriers — darkness/light at the lens, whip blur, shape
  in the same screen position; exit/entry matching:
  https://flashboards.yaroflasher.com/learn/editing/seamless-transitions/
- Show-package anatomy — opener, bumpers, mortises, lower thirds
  unified by typography, palette, imagery, motion characteristics:
  https://www.pixelprobazm.com/lecture1-2

House: SHOW-1..5 treatments; FIRST_SECOND_DOCTRINE_2026-11-15;
POPPING_VISUALS_TV_PLAYBOOK_2026-11-15 (§§1–4); JOINT_COHESION_METHOD
(Method A, esp. J9/J13/J14 and §6); visual-mv-forms SKILL (Families
A/B/D/G/I, the five kinetic house moves, Blender feasibility record);
PILOT-4 CUTLIST (bug practice) and PILOT-4 GATE_LOG (the Clerk drift
this method answers). Tools verified on this VM 2026-11-15: ffmpeg
8.1.2 (drawtext/drawbox/geq/overlay/xfade present), Noto Sans Bold +
Black at /usr/share/fonts/truetype/noto/, Blender 4.5.15 LTS at
~/workspace/tools/blender/, PIL renderers + proofs in
musicvideo/visual-forms/tools/ and proof/.

*All named devices (§2), the G-rules, the joint placements (§3), and
the caption test (§4) are house inventions built on the principles
above; the precedents are cited for the principles, not the devices.*

---

## APPENDIX — DEVICES CONSIDERED AND REJECTED

1. **Speaker name straps / lower thirds.** The broadcast default, and
   the easiest cohesion device to build — rejected outright (§4.2).
   They are captions' kin: they spend the audience's reading on
   furniture, tax cold arrivals with homework, and teach viewers to
   learn names from straps instead of faces — the opposite of the
   recognition the soaps run on.
2. **Kinetic dialogue type as a standing layer (MV Family A,
   transferred whole).** The strongest MV form and the most tempting
   import — rejected for dialogue (§4.2). In an MV the type *is* the
   picture; under a spoken scene it is a subtitle with better PR. Only
   the fiction's documents keep the craft.
3. **Full-screen episode title cards.** Standard show-package practice
   (opener/cards) — rejected. Playbook §1a and doctrine F4 ban text in
   frame 0 and throat-clearing openings generally; a 30–40 s episode
   cannot spend its first second on its own name. The bug + invariant
   carry identity instead.
4. **Animated ident/sting between units.** Broadcast bumpers exist to
   separate programmes from advertising; we have no advertising, and a
   2–5 s sting inside a 30–40 s episode breaks the 10 s atom's chain
   to do work the joint devices (§3) already do inside the fiction.
5. **A persistent episode-progress HUD / progress bar.** Duplicates
   the platform player's own chrome, reads as UI rather than world
   (violates G6), and tells the viewer how much is left — the count
   that never finishes is our progress bar, and it lies on purpose.
6. **"Previously on" recap cards.** Captions again, and a tax on cold
   arrivals (doctrine §5.9). Serial continuity is carried by story
   (Method B's ledger) and by the graphic serial state (§3.4) — the
   tally, the count, the seat position *are* the recap, shown as the
   world, never summarised as text.
7. **Reaction stickers / meme glyphs.** Short-form-native and cheap —
   rejected on register: the shows' graphics are the world's
   paperwork, not the audience's commentary track. The one emoji-class
   element the house already owns is the `~ WuBu ~` bug, and it is
   enough.
8. **Per-episode Blender set pieces.** Rejected as a class (§5.4):
   at 1–2 min/frame the cost buys nothing the Class P renderers can't
   draw, and it breaks G8's cheap re-renderability. Blender stays
   fenced to one-time kit assets.
