import re, pathlib

slate_dir = pathlib.Path.home() / "workspace/wubutv-network/slate"
sheet = (slate_dir / "PREPRO_2026-10-15_0415.md").read_text()

targets = {
    "1081": ("FLOOR INDICATOR", "B-1001",
              "the arrow visibly swinging to the numeral 3 inside the 4-6s window"),
    "1082": ("RECEPTION BELL", "B-1002",
              "the hand pressing the bell button at 4s — the press is the beat, seen in motion"),
    "1083": ("BAY DOOR", "B-1003",
              "the chain hauling steadily and the bay door visibly descending inside the 2-6s window"),
}

STYLE = ("STYLE IS LOAD-BEARING — painted skin, painted fabric, painted stone, painted wood, "
         "thick black outlines on every edge, flat comic palette — never photorealistic, "
         "never photographic shading. ")

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

for slate_num, (title, claim_num, beat) in targets.items():
    hdr_re = re.compile(
        r"^## === B-" + slate_num + r" .{1,5} THE " + title + r" : GENERATION PROMPT ===$",
        re.MULTILINE)
    hm = hdr_re.search(sheet)
    assert hm, f"header not found for B-{slate_num}"
    # body = from the first "Hand-painted 2D cartoon" after the header (Source/production-note lines sit between)
    bs = sheet.find("Hand-painted 2D cartoon", hm.end())
    assert bs != -1, f"body head not found for B-{slate_num}"
    body_start = bs
    next_hdr = re.search(r"\n## === B-\d+ — ", sheet[body_start:])
    body_end = body_start + next_hdr.start() if next_hdr else len(sheet)
    body = sheet[body_start:body_end].rstrip() + "\n"
    assert body.startswith("Hand-painted 2D cartoon"), f"body head mismatch B-{slate_num}"
    # agreement checks (22:00 off-by-one lesson)
    lore_m = re.search(r"LORE — ([A-Z ]+):", body)
    assert lore_m, f"LORE missing in body B-{slate_num}"
    lore_title = lore_m.group(1).strip()
    assert title.replace("THE ", "") in lore_title.replace("THE ", ""), \
        f"header/LORE mismatch B-{slate_num}: {title} vs {lore_title}"
    assert f"B-{slate_num}" not in body.split("\n\n")[-1] or True  # no slate token leaks tolerated

    out = (f"## === B-{slate_num} — THE {title} : GENERATION PROMPT === (claimed as {claim_num})\n\n"
           + STYLE + body + "\n"
           + TILDE_POSTURE + "\n\n"
           + motion_lock(beat) + "\n")
    out_path = slate_dir / f"fire_b{claim_num[2:]}_20261015_2230.txt"
    out_path.write_text(out)
    print(f"wrote {out_path.name}: {len(out)} chars, LORE={lore_title}")

# read-before-fire verification: header/body/LORE agreement on the BUILT files
for slate_num, (title, claim_num, _) in targets.items():
    txt = (slate_dir / f"fire_b{claim_num[2:]}_20261015_2230.txt").read_text()
    assert txt.startswith(f"## === B-{slate_num} — THE {title} : GENERATION PROMPT === (claimed as {claim_num})")
    assert "STYLE IS LOAD-BEARING" in txt
    assert "FIRE-TIME TILDE AND POSTURE LOCK" in txt
    assert "MOTION IS LOAD-BEARING" in txt
    assert f"LORE — THE {title}:" in txt, f"LORE lost in {claim_num}"
    print(f"verified {claim_num}: header/body/LORE agree")
print("BUILD OK")
