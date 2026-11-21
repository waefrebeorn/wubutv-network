# MV-27 VOLLEY PROGRESS — "WuBu"

Budget: 40 video generation calls. Frame target: 6048f EXACT.
FINAL SPEND: 33 video fired (32 landed, 1 artifact lost) / 5 images.
All volleys QC'd — every landed take KEEP (S15b/S16b partial-coverage
keeps closed by S15c and by S16's two-take sub-cut plan). Generation
phase CLOSED.
ASSEMBLY + MASTER COMPLETE 2026-11-20: 149 segments (each asserted
frames+duration), joined probed 6048f EXACT, master encoded CRF 18
(1.87x differential proof), karaoke subs burned in + mov_text,
freezedetect 0, bug exact. Deliverables + md5s in COMPLETION.json;
gates + all disclosures in GATE_LOG.md. MV27_DELIVERED.flag written.
Intermediates (segments/*.mp4, joined.mp4, CRF-23 twin) deleted after
verification; provenance (plan.json, segments.json, logs) kept.

## Pilot volley (3) — FIRED + QC PASS 2026-11-20
- S01 t1 KEEP — G7 1.0 ("-boo! Let's go!"), motion 11.8, near-dup 0.0s.
  Ignition reads (dark panel frame → lights cascade → chant → shout).
- S05 t1 KEEP — G7 0.947 (ASR screened out "Pay"; ear/visual clear),
  ratio 1.138 in band, motion 7.77, near-dup 0.0s. Desk look locked.
- S09 t1 KEEP — G7 0.917 (chant lines heard near-verbatim), ratio 0.854
  in band, motion 22.64, near-dup 0.0s. Background neon = blurred
  pseudo-glyph texture, no legible words (full-res verified) — nit
  disclosed; street vehicles now carry a "signs are smooth light bars,
  no letter shapes" clause.
Pilot verdict: look + singing + chant all proven. Fire the rest.

## Volley 2 (6) — FIRED 2026-11-20; tool-handoff incident
5 of 6 calls returned tool-level failure wrappers while the upstream
generation reported ok:true. 4 artifacts (S02b, S03, S04a, S04b) were
recovered intact from the delivery URLs in the results (valid 10.000s
videos, md5s in TAKE_HISTORY). S02a landed normally. S06's artifact
could not be recovered (signed URL failed signature check) and was NOT
re-fired; its window becomes a wordless event cover (see TAKE_HISTORY).

## Volley plan (revised)
- Volley 3 (6): S07, S08, S10, S11, S12, S06cover (wordless)
- Volley 4 (6): S13a, S13b, S14, S15a, S15b, S16a
- Volley 5 (6): S16b, S17, S18a, S18b, S19, S20
- Volley 6 (5): S21a, S21b, S22a, S22b, S23
- Planned total: 32 fired + 1 lost = 33. Reroll headroom: 7.
