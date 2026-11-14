#!/usr/bin/env python3
"""Build durable fire prompts for the 00:45 run: B-1019 v3, B-1022, B-1023."""
import re, pathlib

slate_dir = pathlib.Path.home() / "workspace/wubutv-network/slate"

STYLE = ("STYLE IS LOAD-BEARING — painted skin, painted fabric, painted steel, painted wood, "
         "painted iron, painted stone, thick black outlines on every edge, flat comic palette — "
         "never photorealistic, never photographic shading. ")

TILDE_POSTURE = (
    "FIRE-TIME TILDE AND POSTURE LOCK (standing fire standard): TILDE COUNT — the hoodie "
    "wordmark is exactly `~WuBu~`: ONE tilde immediately before the W and ONE tilde "
    "immediately after the final u, plain u letters with no umlaut dots and no dotted glyphs "
    "at any scale, all six glyphs on ONE line, never stacked into two lines, never doubled "
    "as `~~`, never spelled out in words; no panel, patch, box, rectangle, or dark letters "
    "behind the letters — the mark printed directly on the bare black fabric, the black "
    "fabric uninterrupted around every glyph. The same count locks the corner bug line one: "
    "`~ WuBu ~` — tilde, space, W-u-B-u, space, tilde — never doubled, never dotted, never "
    "spelled out, never a third line under the bug. POSTURE — UNC's chest stays square to "
    "the camera and his face to the lens in every front-facing frame; during the beat his "
    "arms work at waist height below the chest panel and his torso never turns; by the 8s "
    "line he is chest-square, facing the lens, his hands clear of the chest panel."
)

def motion_lock(beat):
    return (
        "MOTION IS LOAD-BEARING — this is NOT a still and NOT a held portrait: the drafted "
        "beat MUST render as real visible motion on screen — " + beat + ". The beat frames "
        "must show the beat in motion, never the setup pose held. NO frozen take, no static "
        "hold, no held portrait, no beat that never renders."
    )

def extract(sheet_path, hdr_re_str, title, claim_num):
    sheet = (slate_dir / sheet_path).read_text()
    hm = re.search(hdr_re_str, sheet, re.MULTILINE)
    assert hm, f"header not found for {title}"
    bs = sheet.find("Hand-painted 2D cartoon", hm.end())
    assert bs != -1, f"body head not found for {title}"
    next_hdr = re.search(r"\n## === B-\d+", sheet[bs:])
    body_end = bs + next_hdr.start() if next_hdr else len(sheet)
    body = sheet[bs:body_end].rstrip() + "\n"
    assert body.startswith("Hand-painted 2D cartoon"), f"body head mismatch {title}"
    lore_m = re.search(r"LORE — ([A-Z ]+):", body)
    assert lore_m, f"LORE missing in body {title}"
    assert title.replace("THE ", "") in lore_m.group(1).replace("THE ", ""), \
        f"header/LORE mismatch {title}"
    return body

# ---- B-1019 v3: by-number reclaim, v2 + new named-failure CORRECTION (logos+verdict+audio)
v2 = (slate_dir / "fire_b1019_20261016_0030_v2.txt").read_text()
v3_correction = (
    "\n\nCORRECTION — the v2 fire rendered three named failures; this re-fire corrects all "
    "three, named verbatim, without re-describing the setting. (1) LOGOS: v2 rendered legible "
    "Coca-Cola signage throughout the take — a real-logo break against the explicit NEGATIVE "
    "item, unshippable. v3 renders NO logos, NO brand marks, NO brand dressing anywhere in "
    "the frame, ever. The vending row stays the plain unlettered clear-steel rack of the "
    "setup — bare steel, no signs, no labels, no lettering, no branding of any kind; the "
    "machine is not re-imagined, not improved, not dressed. (2) VERDICT: v2 left the leftmost "
    "coil EMPTY at 9.5s while rendering the other four filled — the verdict never read, two "
    "fires in a row. v3: the leftmost coil is the ONLY empty coil at 0.5s; UNC slides the bar "
    "into THAT leftmost coil; at 9.5s ALL FIVE coils hold one bar — the complete row is the "
    "verdict; the leftmost coil is never left empty; exactly one filling, never two. "
    "(3) AUDIO: v2 rendered the directed 8s line \"Restocked.\" at -47.2 dB — inaudible "
    "(B-980/B-984/B-985 class). v3: the line is LOUD AND VISIBLE at 8s — UNC's mouth visibly "
    "OPEN at 8s, exactly ONE mouth opening, one audible voice event 8.0-8.5s for "
    "\"Restocked.\", the take's loudest voice event; the ONLY voice in the take; no voice "
    "event and no mouth opening before 7.5s or after 8.75s, ever.\n"
)
v3 = v2.rstrip() + "\n" + v3_correction
assert "Coca-Cola" in v3 and "ALL FIVE coils" in v3 and "LOUD AND VISIBLE" in v3
(slate_dir / "fire_b1019_20261016_0045_v3.txt").write_text(v3)
print(f"wrote fire_b1019_20261016_0045_v3.txt: {len(v3)} chars")

# ---- B-1022: 0515 B-1103 "The Cleared Grate" (0515 draft + lock stack)
body1103 = extract("PREPRO_2026-10-15_0515.md",
                   r"^## === B-1103 — THE CLEARED GRATE : GENERATION PROMPT ===$",
                   "THE CLEARED GRATE", "B-1022")
out1022 = ("## === B-1103 — THE CLEARED GRATE : GENERATION PROMPT === (claimed as B-1022)\n\n"
           + STYLE + body1103 + "\n"
           + TILDE_POSTURE + "\n\n"
           + motion_lock("he visibly lifts the leaf off the storm drain grate inside the "
                         "4-6s window — the leaf on the grate at 2s, in his hand at 5s, "
                         "the grate bare and clear at 9.5s") + "\n")
(slate_dir / "fire_b1022_20261016_0045.txt").write_text(out1022)
print(f"wrote fire_b1022_20261016_0045.txt: {len(out1022)} chars")

# ---- B-1023: 0015 B-1321 "The Tide Table" (locks baked into the 0015 draft; claim header only)
body1321 = extract("PREPRO_2026-10-16_0015.md",
                   r"^## === B-1321 \(provisional\) — \"THE TIDE TABLE\" : GENERATION PROMPT ===$",
                   "THE TIDE TABLE", "B-1023")
assert "STYLE IS LOAD-BEARING" in body1321 and "MOTION IS LOAD-BEARING" in body1321
out1023 = ("## === B-1321 (provisional) — THE TIDE TABLE : GENERATION PROMPT === "
           "(claimed as B-1023)\n\n" + body1321)
(slate_dir / "fire_b1023_20261016_0045.txt").write_text(out1023)
print(f"wrote fire_b1023_20261016_0045.txt: {len(out1023)} chars")

# read-before-fire verification
for name, needles in [
    ("fire_b1019_20261016_0045_v3.txt",
     ["claimed as B-1019", "CORRECTION — the v2 fire", "Coca-Cola", "LOUD AND VISIBLE",
      "FIRE-TIME TILDE AND POSTURE LOCK", "LORE — THE COIL GAP:"]),
    ("fire_b1022_20261016_0045.txt",
     ["claimed as B-1022", "STYLE IS LOAD-BEARING", "FIRE-TIME TILDE AND POSTURE LOCK",
      "MOTION IS LOAD-BEARING", "LORE — THE CLEARED GRATE:"]),
    ("fire_b1023_20261016_0045.txt",
     ["claimed as B-1023", "STYLE IS LOAD-BEARING", "MOTION IS LOAD-BEARING",
      "no voice event and no mouth opening before 7.5s", "LORE — THE TIDE TABLE:"]),
]:
    txt = (slate_dir / name).read_text()
    for n in needles:
        assert n in txt, f"{name}: missing {n!r}"
    print(f"verified {name}")
print("BUILD OK")
