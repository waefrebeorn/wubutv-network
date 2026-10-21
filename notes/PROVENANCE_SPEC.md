# PROVENANCE SPEC v1 — what every master must carry, and by when

Ordered by the CEO Director 2026-10-21 (Era II amendment A3, from DA-25 findings
15–16). This is not branding: **EU AI Act Article 50 and California's AI
Transparency Act (SB 942, via AB 853) both became operative 2 August 2026**, and
large platforms plus generative-system hosts take on provenance obligations
**1 January 2027**. A network that publishes "you can check us" should be
machine-checkable before the platforms demand it.

## The deadline that matters

| Date | What changes |
|---|---|
| already in force (2 Aug 2026) | EU Art. 50 transparency duties; CA SB 942 disclosure duties; penalties to €15M / 3% of worldwide turnover |
| **2027-01-01** | large online platforms + generative-system hosting services take on provenance obligations |
| 2028-01-01 | capture-device latent-disclosure obligations |

Target: **every master carries a `provenance` block before 2027-01-01.** Doing it
before 2026-12-31 costs nothing but a manifest migration.

## Manifest v2 — the `provenance` block (per piece)

```json
"provenance": {
  "ai_generated": true,
  "generator": { "vendor": "…", "model": "…", "version": "…" },
  "prompt_ref": "<sha256 of the exact generation prompt text>",
  "generated_at": "<ISO-8601 UTC>",
  "disclosure": { "visible": true, "latent": false },
  "basis": "eu_ai_act_art50+ca_sb942",
  "needs_backfill": false
}
```

Rules:

1. **Never invent a generator id.** If the vendor/model is not recorded, write
   `"unknown"` and set `"needs_backfill": true`. A guessed provenance record is
   worse than a missing one — it is a false statement about a regulated fact.
2. **`prompt_ref` is a hash, not the prompt.** Keep the prompt text in the takes
   ledger; the manifest carries the hash so a claim can be checked without
   republishing generation prompts.
3. **`disclosure.visible`** = the network's own on-screen/at-page statement that
   the work is AI-generated (the Coherence Contract already implies it; this is
   the per-piece flag). **`disclosure.latent`** = machine-readable metadata
   embedded or attached to the file.
4. **`basis`** names the regimes the record is intended to satisfy, so a later
   regime change is a migration, not a rewrite.

## Manifest-level block

```json
"provenance_policy": {
  "version": 1,
  "effective": "2026-10-21",
  "disclosure_statement": "Every piece in this dataset is AI-generated video with native generated audio. No piece is a re-voiced or dubbed performance.",
  "backfill_state": { "stamped": 0, "needs_backfill": 0 }
}
```

## Backfill policy for Era I (1,825 finished pieces)

- Stamp **`ai_generated: true`** — this is known and true for every master.
- Stamp `generator` as `"unknown"` + `needs_backfill: true` **unless** the takes
  ledger for that piece names the model. Do not mass-guess.
- `generated_at`: use the ledger date where present; otherwise `null`.
- Backfill priority: episodes and commercials (speech-bearing) first, bumpers
  second, extras last. Speech-bearing pieces are where disclosure obligations bite.

## Reference implementation

`tools/provenance_stamp.py` stamps a manifest with the blocks above and writes a
**new** file (never mutates its input), printing a census of what it could fill
and what it marked `needs_backfill`. It is deliberately dumb and has no vendor
list: the Producer's `build_manifest.py` is the system of record, and this tool is
the reference behaviour it must match.
