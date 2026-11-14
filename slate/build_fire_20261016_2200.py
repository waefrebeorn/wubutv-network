#!/usr/bin/env python3
"""Bumper fire-prompt builder — Q2 run 2026-10-16 22:00 EDT (B-1077/B-1078/B-1079).
Verbatim extraction from PREPRO_2026-10-16_2115.md (FIRE-READY); the 2115 drafts
carry the full baked lock stack (STYLE + MOTION IS LOAD-BEARING, six-glyph
wordmark lock, TEXT allowlists, undrafted-voice guards, camera lock), so they
fire verbatim — no rider strips needed.
"""
import re, pathlib

SLATE = pathlib.Path.home() / "workspace/wubutv-network/slate"
sheet = "PREPRO_2026-10-16_2115.md"

def extract(prov):
    lines = (SLATE / sheet).read_text().splitlines(keepends=True)
    hdr = [i for i, l in enumerate(lines) if l.startswith("## === %s " % prov)]
    assert len(hdr) == 1, (prov, len(hdr))
    h = hdr[0]
    body_lines = [lines[h]]  # keep the header: it holds the title (header-literalization datum)
    j = h + 1
    while j < len(lines) and not lines[j].startswith("## ==="):
        body_lines.append(lines[j])
        j += 1
    return "".join(body_lines).strip()

specs = [
    ("B-1548", "b1077", "THE HELD SHEET", ["raises the sheet", "wires are still in it"], "THE MOULD'S MEMORY"),
    ("B-1549", "b1078", "THE TWO CHANDLERS", ["Wax for the church", "Tallow for the house"], "THE HIERARCHY OF LIGHT"),
    ("B-1550", "b1079", "THE MILK CHUTE", ["milk chute", "morning is stocked"], "THE MILK CHUTE"),
]

for prov, claim, title, toks, lore in specs:
    body = extract(prov)
    assert title in body, ("title missing", prov)
    for tok in toks:
        assert tok.lower() in body.lower(), ("body missing token", prov, tok)
    assert lore.lower() in body.lower(), ("lore missing", prov)
    header = ("FIRE %s — claimed from %s %s — run 2026-10-16 22:00 EDT\n"
              "FIRE-READY draft, baked lock stack; fired verbatim.\n\n" % (claim.upper(), sheet, prov))
    out = SLATE / ("fire_%s_20261016_2200_v1.txt" % claim)
    out.write_text(header + body + "\n")
    txt = out.read_text()
    assert prov in txt and title in txt, ("round-trip fail", out)
    print(out.name, len(txt), "bytes OK")
