#!/usr/bin/env python3
"""Build durable fire prompts for the 01:15 run: B-1027, B-1028 (0015 drafts, claim header only).
B-1026 reclaim reuses the durable 0100 v2 prompt verbatim (verified below)."""
import re, pathlib

slate_dir = pathlib.Path.home() / "workspace/wubutv-network/slate"

def extract(sheet_path, hdr_re_str, title):
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

def claim_fire(draft_id, title, claim_num, run_tag):
    body = extract("PREPRO_2026-10-16_0015.md",
                   r'^## === ' + draft_id + r' \(provisional\) — "' + title + r'" : GENERATION PROMPT ===$',
                   title)
    assert "STYLE IS LOAD-BEARING" in body, f"{title}: style lock missing"
    assert "MOTION IS LOAD-BEARING" in body, f"{title}: motion lock missing"
    out = (f"## === {draft_id} (provisional) — {title} : GENERATION PROMPT === "
           f"(claimed as {claim_num})\n\n" + body)
    fname = f"fire_b{claim_num}_20261016_{run_tag}.txt"
    (slate_dir / fname).write_text(out)
    print(f"wrote {fname}: {len(out)} chars")
    return fname

f1027 = claim_fire("B-1325", "THE BOARDING BELL", "1027", "0115")
f1028 = claim_fire("B-1326", "THE FORGOTTEN UMBRELLA", "1028", "0115")

# read-before-fire verification
for name, needles in [
    (f1027, ["claimed as 1027", "STYLE IS LOAD-BEARING", "MOTION IS LOAD-BEARING",
             "boarding bell", "LORE — THE BOARDING BELL:", "The crossing is scheduled."]),
    (f1028, ["claimed as 1028", "STYLE IS LOAD-BEARING", "MOTION IS LOAD-BEARING",
             "Laura", "LORE — THE FORGOTTEN UMBRELLA:", "Someone remembered."]),
    ("fire_b1026_20261016_0100_v2.txt",
     ["CORRECTION (named failures, resume-form", "CORRECTION (named failures, resume-form",
      "STYLE IS LOAD-BEARING", "MOTION IS LOAD-BEARING",
      "LORE — THE TURNED SIGN:", "The shop is open.", "no voice event and no mouth opening after 8.75s, ever"]),
]:
    txt = (slate_dir / name).read_text()
    for n in needles:
        assert n in txt, f"{name}: missing {n!r}"
    print(f"verified {name}")
print("BUILD OK")
