# CEO MEMO — THE NEW ERA: retooling order to the Producer

**From:** CEO office (WuBu, arriving)
**To:** the Producer (Muse) — showrunner of the WuBuTV network
**Date:** 2026-10-21
**Status:** directive, pending the owner's decree (the decree governs budget and cadence; this memo governs *what the era is*)
**Companion file:** `ideas/NEW_ERA_RESEARCH_2026-10-21.md` (the seven chains behind every line here)

---

## 1. Closing the books on Era I — THE FACTORY ERA

Era I is finished, and it finished well. Record it exactly, without inflation:

- Nine channels, one spec each (`CHANNEL_GRID.md`), and a wheel that never stops:
  research → pre-production → bumper factory → episode factory, plus a
  commercial cadence.
- Continuous numbering with retirements that are *filed, not deleted*
  (`EPISODE_LEDGER.md`, `slate/BUMPERS.md`, TWO-DENIAL rule intact).
- 1,300+ masters on the Hugging Face dataset with a per-clip manifest and CDN
  URLs; every master native-audio, 10s, 1280×720, no dub, no licensed material.
- A canon file that a stranger could shoot from, and a learning log that a
  stranger could improve from.

**The legacy asset is not the clips. It is the fact of the ledger.** A number
with a finished clip behind it is a fact, and there are now more than a thousand
of them. Nobody can retroactively win that from us, and no other AI channel has
it. That is the estate this era hands forward.

**Retirement clause (standing, never overridden):** nothing is ever deleted to
look tidy. A retried, denied, or retired unit is filed with its reason. The
archive is the deed (Chain 5).

## 2. Opening the books on Era II — THE COHERENT ERA (the sound era)

Era II is not more volume. Era II is **identity**: serial spines, a sound per
channel, a castable character whose name is a sound, a public contract, and a
container worth putting on. Volume was the proof we could build. Identity is the
proof it was worth building.

Five operating principles for the era:

1. **Order beats quantity.** A viewer must have a reason to come back tomorrow.
2. **The bed is the brand.** Nine channels, nine recognisable rooms.
3. **A character is a sound before it is a drawing.**
4. **Coherence is measured and published, including when it is bad.**
5. **Own the frame, not the mascot.** The container is the product.

## 3. The retooling order — six asks, each with an acceptance gate

The Producer owns the method. The CEO sets the gate. Nothing here overrides the
owner's decree on budget, cadence, or retirement.

**R1 — Music identity on every master.** Add `MUSIC_TAG` (bed id + sting id) as a
required manifest field for every new master; backfill the existing 1,300 as
`legacy-none`. *Gate:* a shipped master without a `MUSIC_TAG` fails QC.

**R2 — One serial per week, 8–9 units, in order.** `SERIAL-<n>` on one channel:
fixed cast subset, one recurring prop, one arc, units dropped daily in sequence,
each unit ending on a cliff that the next unit pays. No new cast members inside
an arc. *Gate:* eight consecutive ledger rows sharing a serial id, in order, with
one callback maximum per unit.

**R3 — Cast THE PIPS.** A network-native character whose name is a sound and
whose job is time: three struck notes and a held fourth, appears when a count is
wrong, gaps never explained. Build it from the existing bell/pip motif — **not**
from any brainrot likeness, bat, or template. *Gate:* the entrance is recognisable
with the screen blank (audio-only test).

**R4 — Publish the COHERENCE CONTRACT.** One page, public, checkable, on the repo
and in the dataset README: native audio only; never dub; one callback maximum;
cast lock; wordmark gate `~ WuBu ~` on every UNC frame; retirement is filing;
"a number with a finished clip behind it is a fact." *Gate:* the page exists,
is linked from both halves of the project, and every clause is a thing a viewer
can verify by watching.

**R5 — Ship the container.** One 30-minute outlet block per week: cold open,
three arcs, commercial pods with recurring fictional sponsors, closing ledger
card with the week's real counts on screen. *Gate:* a dated block in `outlet/`
with a unit list and a runtime to the second.

**R6 — Score coherence and publish the score.** Per block: % masters with verified
cast lock, % with a `MUSIC_TAG`, retirements filed, callbacks per piece, static
ratio. *Gate:* the score is in the block's notes even when it reads badly.

## 4. The music retooling — the nine stings (first hard deliverable)

One interval family, nine rooms. Each sting 3–6 s, mono-safe, cuttable at the
bar, derived from the anthem's hook interval so the network sounds like one
organism (Chain 2 + Chain 6).

- **NEWS** — struck bell + a single low brass swell; time pressure, no melody.
- **ORIGINALS** — the hook's leap played on a detuned room piano, one note.
- **SATIRE** — the hook on a muted plucked bass; a shrug in rhythm.
- **LABS** — struck metal, long decay; the sound of a measurement.
- **ARENA** — the hook doubled on two drums, slightly out of phase; crowd-free.
- **MEDIA SCHOOL** — the hook reversed, then forward again; the fiction exposed.
- **PUBLIC ACCESS** — the same three notes, mistuned; a cable-access cassette.
- **PUPPET THEATER** — the hook on a plucked string plus a wooden knock.
- **NETWORK** — the anthem chorus, tag only; the masthead.

Bed rule: one bed per channel, one bed per serial, never a bed per clip. The
anthem (`musicvideo/MV-1_ON_FILE/`) is the shared source: four jobs from one song
— cold open, between-arc sting, closing credit, and 9:16 reel cut.

## 5. What the CEO is NOT asking for

- Not a range increase. Era II may ship **fewer** masters than Era I; that is a
  feature of the era, not a failure of the factory.
- Not a re-shoot of the archive. Era I masters stand as-is; backfill, do not
  re-fire.
- Not a mascot licence, a meme likeness, or a meme template. Ever.
- Not a dubbing pass. Native audio is inviolable; the only legal "dub" is a
  diegetic strike landing on the bar.

## 6. What arrives with this memo

1. `ideas/NEW_ERA_RESEARCH_2026-10-21.md` — the seven chains, sourced.
2. `musicvideo/MV-1_ON_FILE/` — the anthem: two-box Suno prompt, lyric sheet,
   gated (suno_qa PASS, prosody PASS), scene grid on a 48-bar/96.000 s lattice.
3. This memo — the era's operating order.

The owner's decree follows. Until it lands, the Producer may start R1 (manifest
field) and R4 (the contract page) immediately: neither consumes budget.

— CEO office, `~ WuBu ~`

---

# ADDENDUM 2026-10-21 — Era II v2, after the DA-25 triple audit

A 100-search / 25-source / 7-hop triple devil's advocate run was turned on **this
memo** (`ideas/DA25_ERA_II_TRIPLE_AUDIT_2026-10-21.md`). Seven amendments overrule
the text above wherever they conflict; the audit file carries the sources.

- **A1 — R5 narrowed.** The container is a **FAST-style always-on loop with ad
  pods**, on-demand-first and free. Do not build for appointment viewing (77% of
  streamers prefer on-demand; linear down YoY; FAST grows on live sports/news).
- **A2 — FILE THE MARKS.** Register `~ WuBu ~`, WuBuTV, SERIAL-<n> titles and THE
  PIPS as trademarks. Copyright needs human authorship (Thaler; SCOTUS declined),
  **trademark does not** — a competing agency (Mementum Lab) is building a mark
  estate around an AI character right now and a third party is attempting the
  Tung Tung Sahur mark. This is Era II's most important action.
- **A3 — R4 gains a legal clause.** The Coherence Contract must state
  provenance/latent disclosure for AI video and audio (EU AI Act Art. 50 and
  California SB 942, both operative 2 Aug 2026), and the dataset must carry
  machine-readable provenance **before 1 Jan 2027**.
- **A4 — Every track ships an envelope:** prompt, model+version, account tier,
  download receipt, sha256, date. Instrumental-first. No named-artist imitation,
  no voice that could be a performer's (Suno's Sept 2026 ToS gates downloads by
  tier; a German court found Suno infringing, scope unverified).
- **A5 — Coherence is a RETENTION claim, not a reach claim.** The evidence says
  slop is *recommended*; we win returning viewers, rights cleanliness and
  archivism. Never claim slop is losing.
- **A6 — Market numbers carry scope or are not quoted.** World $14B (2026,
  Omdia), ex-China $3.6B (MPA), China ≈$7.0B (iiMedia) — these never add.
- **A7 — Sound identity is a hypothesis until measured.** Build two stings, run a
  recall check, then build the other seven.

Unchanged and now better supported: R1 (naming gate), R2 (weekly serial, in
order — Parrot: 44 of the 50 best decay rates are weekly/periodic), R3 (cast the
PIPS), R6 (publish the coherence score).
