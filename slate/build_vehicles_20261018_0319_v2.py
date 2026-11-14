#!/usr/bin/env python3
"""Build v2 named-correction vehicles for the 2026-10-18 0319 commercial factory run.
v1 QC verdicts: AD-276 v1 REJECTED on the bug axis (bug text on a dark-brown rounded
backing panel vs the explicit 'NO backing panel or plaque or chip behind the bug'
NEGATIVE lock); AD-277 v1 REJECTED on the count axis (TWO sheets at 9.5s — one held,
one on the outfeed table — vs drafted exactly ONE sheet). Narrow single-axis named
corrections per the correction-regression datum; everything else verbatim."""
import hashlib, pathlib

slate = pathlib.Path.home() / "workspace/wubutv-network/slate"
RUN = "20261018_0319"

def v2(ad, corrections):
    body = (slate / f"fire_ad{ad}_{RUN}_v1.txt").read_text()
    for old, new in corrections:
        assert old in body, f"anchor missing for AD-{ad}: {old[:60]}"
        body = body.replace(old, new, 1)
    body = body.rstrip() + "\n"
    fn = slate / f"fire_ad{ad}_{RUN}_v2.txt"
    fn.write_text(body)
    print(f"{fn.name}  md5={hashlib.md5(body.encode()).hexdigest()}  bytes={len(body.encode())}")

# AD-276 v2: named BUG correction — the single named failing axis.
v2("276", [
    ("CORNER BUG (every frame): EXACTLY TWO lines of plain WHITE text, bottom-right, painted directly on the scene itself: line one `~ WuBu ~`, line two `WuBuTV` — and NOTHING beneath them.",
     "CORNER BUG (every frame): EXACTLY TWO lines of plain WHITE text, bottom-right, painted directly on the scene itself: line one `~ WuBu ~`, line two `WuBuTV` — and NOTHING beneath them. THE BUG TEXT FLOATS ON THE SCENE ITSELF: no rounded rectangle, no panel, no plaque, no chip, no backing shape of any kind behind or under the bug text — the background scene is visible directly around and between every bug glyph."),
    ("no spelled-out wordmark descriptions as on-screen text, no yellow or gold bug letters, no real logos, no brands,",
     "no spelled-out wordmark descriptions as on-screen text, no yellow or gold bug letters, no real logos, no brands, no rounded rectangle or any backing shape behind the bug text,"),
])

# AD-277 v2: named COUNT correction — the single named failing axis.
v2("277", [
    ("Exactly ONE machine, ONE sheet, the same single props throughout.",
     "Exactly ONE machine, ONE sheet, the same single props throughout — the single sheet is the ONLY sheet in the room; at every second the outfeed table holds NO second sheet."),
    ("- 9.5s (verdict): the glazed sheet held up to the light with its sheen visible, the rolls still, the crank at rest, his eyes on the lens, mouth closed.",
     "- 9.5s (verdict): the glazed sheet held up to the light with its sheen visibly catching the light, the rolls still, the crank at rest, THE OUTFEED TABLE EMPTY — the single sheet is in his hands and nowhere else — his eyes on the lens, mouth closed."),
    ("no second sheet, no second crank, no nameplate lettering,",
     "no second sheet anywhere at any point, the outfeed table empty at 9.5s, no second crank, no nameplate lettering,"),
])
print("OK")
