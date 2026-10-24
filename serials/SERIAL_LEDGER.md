# SERIAL LEDGER — Era II fruit-soap serials

R2 gate: eight consecutive ledger rows sharing a serial id, in order, one
callback maximum per unit. Units are 10 s, 16:9, 1280x720, native audio,
no dub. Files: `serials/s1_<nn>_<slug>_16x9.mp4`.

CEO8 ORDER 2: every unit carries the palette-audit and count-audit results in
its row. C0.5s / C9.5s are the human-confirmed blank-card counts at 0.5s and
9.5s (stills in `serials/qc/<unit>/`); a count contradicting the act table is
a RE-FIRE, not a note. Audit tooling: `tools/palette_audit.py`,
`tools/count_audit.py`.

## SERIAL-1 "THE UNFILED CLAIM" (ORIGINALS) — 2026-10-21

| Unit | Title | File | MD5 | Date | Music tag | Callback | C0.5s | C9.5s | Status |
|------|-------|------|-----|------|-----------|----------|-------|-------|--------|
| S1-1 | The Tray | serials/s1_01_the_tray_16x9.mp4 | 96e48b33d78bcae2bef2401803f5cdb0 | 2026-10-21 | bed=serial-1-orig, sting=orig | none | 1 | 1 | SHIPPED |
| S1-2 | The Receipt | serials/s1_02_the_receipt_16x9.mp4 | aeffe30d4e76ab1ed355bd55dbfefe06 | 2026-10-21 | bed=serial-1-orig, sting=orig | none | 1 | 1 | SHIPPED |

## SERIAL-1 "THE UNFILED CLAIM" — FILED AS RETIRED (producer's decision, 2026-10-21 ~01:00 EDT, per CEO9/CEO10)
**Decision: FILE, do not finish.** Reason: the owner retired the grammar this serial was built in (verbatim owner order via CEO9: "do not write any more esoteric slop, we are now in the algo maxxing each 10 seconds being story parts"), and CEO9/CEO10 order no new units in the old grammar. Firing S1-3..S1-8 would burn six renders on a dead grammar while the STATION test piece is the ordered priority. The two shipped units (S1-1 "The Tray", S1-2 "The Receipt") stand as catalogue — retired is filing, never deletion. CEO8's S1-2..S1-8 fire order is superseded by CEO9/CEO10; the S1-8 coherence-score report falls away with the arc.
