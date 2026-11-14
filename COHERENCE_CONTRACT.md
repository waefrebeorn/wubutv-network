# WuBuTV Coherence Contract (public, Era II — effective 2026-10-21)

This is the network's checkable promise. Every clause below can be verified
by a viewer against the public archive (GitHub `waefrebeorn/wubutv-network`
for text, the Hugging Face dataset `WaefreBeorn/wubutv-network-media` for
media + `manifest.json`). Coherence is counted and published, including when
the number is bad.

## The clauses

1. **Native audio only.** Every shipped piece carries the audio its scene
   was generated with. No re-voice, no overdub, no TTS laid over native
   speech. (Verify: `manifest.json` — every master is a native-audio
   generation; QC rejects dubbed takes. The only legal "dub" is a diegetic
   strike landing on the bar.)

2. **Never dub.** Commentary is the editing layer, never a voice laid over
   someone else's speech. A clip whose generated audio has speech-like
   artifacts ships silent rather than dubbed.

3. **One callback max.** Each piece makes at most one callback to an earlier
   bit. A returning viewer is rewarded; a first-timer still gets the joke.

4. **Cast lock.** Every character has a fixed identity spec (UNC, the
   Colonel, Peter, Laura, the Wizard, the teal orb). New pieces re-state the
   lock; drift is re-fired once, then the piece does not ship.

5. **Wordmark gate on every UNC frame.** UNC's hoodie reads exactly
   `~ WuBu ~` in yellow/gold — the tildes are the wordmark. Any drift
   (missing tildes, respelling, restyling, dimming) is a hard QC fail.

6. **Retirement is filing.** Retired numbers, shapes, and subjects are filed
   in the ledger as retired — never silently deleted, never re-shot. A
   number with a finished clip behind it is a fact; a number in a plan is
   a plan.

7. **The ledger is the estate.** Nine channels, one spec each; continuous
   numbering with retirements filed; a per-clip manifest with CDN URLs. The
   fact of the ledger is the asset — more than a thousand numbers with
   finished clips behind them.

## Scoring (per outlet block)

- % of masters with verified cast lock
- % of masters with MUSIC_TAG (Era II; Era I masters carry `legacy-none`)
- retirements filed that week
- callbacks per piece
- static ratio

The score ships in the block notes even when it reads badly.

---
*Era I (the factory era) closed 2026-10-21: volume proved we could build.
Era II (the coherent era): identity proves it was worth building.*
