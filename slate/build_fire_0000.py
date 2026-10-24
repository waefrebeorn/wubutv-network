import re, sys

SHEET = "PREPRO_2026-10-15_0515.md"
REF = "fire_b1011_20261015_2330_v2.txt"  # structure donor (verbatim framing text)
TS = "20261016_0000"
HDR_OPEN = "## === B-"

sheet = open(SHEET, encoding="utf-8").read()
ref = open(REF, encoding="utf-8").read()

# --- extract the fire-time tilde/posture lock paragraph from the donor (verbatim) ---
m = re.search(r"FIRE-TIME TILDE AND POSTURE LOCK \(standing fire standard\):.*?(?=\n\nMOTION IS LOAD-BEARING)", ref, re.S)
assert m, "tilde lock not found"
TILDE_LOCK = m.group(0)

# --- extract the motion-lock framing (prefix + suffix), beat clause is ours ---
mm = re.search(r"(MOTION IS LOAD-BEARING — .*?on screen — )(.*?)( The beat frames must show the beat in motion.*)", ref, re.S)
assert mm, "motion lock framing not found"
MOT_PRE, _BEAT_OLD, MOT_POST = mm.group(1), mm.group(2), mm.group(3)

def draft_body(sheetnum, title):
    # body = text from "Hand-painted 2D cartoon" up to the next draft header (lookahead fix)
    pat = re.compile(HDR_OPEN + re.escape(str(sheetnum)) + r" — .*? : GENERATION PROMPT ===\n(.*?)(?=\n## === B-|\Z)", re.S)
    m2 = pat.search(sheet)
    assert m2, f"draft B-{sheetnum} not found"
    seg = m2.group(1)
    i = seg.find("Hand-painted 2D cartoon")
    assert i != -1, f"style opener missing in B-{sheetnum}"
    body = seg[i:].strip()
    assert len(body) > 2000, f"body too short for B-{sheetnum}: {len(body)}"
    return body

DASH = "\u2014"
jobs = [
    # (sheet_num, title, claim_num, slug, style_materials, beat_clause)
    (1093, "THE BOUND VOLUME", 1013, "the_bound_volume",
     "painted skin, painted fabric, painted wood, painted paper",
     "the volume visibly lifting off the table and being set upright on the shelf ONCE inside the 4-6s window " + DASH +
     " the volume flat on the table at 0.5s, in his hands at 4s, upright on the shelf at 6s and 9.5s."),
    (1094, "THE SCUFF MARK", 1014, "the_scuff_mark",
     "painted skin, painted fabric, painted linoleum",
     "the shoe visibly buffing the scuff mark OFF in one pass inside the 4-6s window " + DASH +
     " the mark on the floor at 0.5s, the shoe over it at 5s, the floor clean at 6s and 9.5s."),
    (1095, "THE FILLED PITCHER", 1015, "the_filled_pitcher",
     "painted skin, painted fabric, painted plaster, painted glass, painted water",
     "the water visibly rising in the pitcher inside the 4-6s window " + DASH +
     " the pitcher empty at 0.5s, half full at 5s, full at 6s and 9.5s."),
]

bodies = set()
for sheetnum, title, claim, slug, materials, beat in jobs:
    body = draft_body(sheetnum, title)
    assert body not in bodies, f"duplicate body for B-{sheetnum}"
    bodies.add(body)
    header = f"## === B-{sheetnum} {DASH} {title} : GENERATION PROMPT === (claimed as B-{claim})\n"
    style_head = ("STYLE IS LOAD-BEARING " + DASH + " " + materials +
                  ", thick black outlines on every edge, flat comic palette " + DASH +
                  " never photorealistic, never photographic shading. ")
    motion = MOT_PRE + beat + MOT_POST
    text = header + "\n" + style_head + body + "\n\n" + TILDE_LOCK + "\n\n" + motion + "\n"
    fname = f"fire_b{claim}_{TS}.txt"
    open(fname, "w", encoding="utf-8").write(text)
    # self-verification (counts, no retyped unicode asserts)
    assert f"(claimed as B-{claim})" in text
    assert body in text
    assert TILDE_LOCK in text
    assert beat in text
    assert "~WuBu~" in text and "~ WuBu ~" in text and "WuBuTV" in text
    print(f"{fname}: {len(text)} bytes, body {len(body)} bytes, OK")
