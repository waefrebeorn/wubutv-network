#!/usr/bin/env python3
"""Build the G7 validation fixture (loop 7).

Contents:
  * MV-14: the 65 KEEP takes from work/TAKE_LEDGER.md (one per scene
    S01-S65), take file located in takes/ and md5-verified against the
    ledger. Planned words per scene, two constructions:
      - planned_primary: the lyric fragments quoted in the scene plan
        (work/MV_PREPRO_MV-14.md, lyric column; '/' splits inside a
        fragment are unioned — the chant phrases straddle slot edges).
      - planned_grid: SONG_WORDS.json words whose start falls inside
        the scene's assembly window (cross-check variant; the grid is
        itself ASR output and garbles chant in places — S21's slot
        reads "trip it posted", S63's window holds the plan-flagged
        unverified "We'll be right back" blip the plan says is NOT
        built on — both reported in the loop-7 report).
  * MV-2 real positives (takes that sang the wrong segment, proven by
    the v3/v4 audits and recorded in TAKE_HISTORY.md):
      - mv2_s04_t3: sang the 34.56-40.94s segment at S04's slot
        (slot line = base-grid words 41.90-48.84).
      - mv2_s21_t1: sang a chorus echo line over S21's verse slot
        (slot line = base-grid words 205.20-213.80).
    For mv2_s04_t3 the segment it actually sang is also recorded
    (alt_segment_words) so the scorer can check the take scores HIGH
    against the words it really sang — proving the gate reads content,
    not noise.
Output: fixture.json next to this script.
"""
import glob
import hashlib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from g7_check import normalize  # noqa: E402

MV14 = os.path.expanduser("~/workspace/wubutv-network/musicvideo/MV-14_clip-it")
MV2 = os.path.expanduser("~/workspace/wubutv-network/musicvideo/MV-2_toll-roads-are-dumb")


def words_of(text):
    out = []
    for tok in re.split(r"[\s/]+", text):
        t = normalize(tok)
        if t:
            out.append(t)
    return out


def mv14_keep_takes():
    rows = []
    pat = re.compile(r"\|\s*(S\d+)\s*\|\s*(t\d+)\s*\|\s*([0-9a-f]{32})\s*"
                     r"\|[^|]*\|[^|]*\|\s*(KEEP|REJECT)\s*\|")
    for line in open(os.path.join(MV14, "work/TAKE_LEDGER.md")):
        m = pat.match(line)
        if m and m.group(4) == "KEEP":
            rows.append(m.groups())
    items = []
    for scene, take, md5, _ in rows:
        pats = [f"takes/media-generation-mv14-{scene.lower()}-{take}-0-*.mp4",
                f"takes/media-generation-mv14-{scene.lower()}-0-*.mp4"]
        files = []
        for p in pats:
            files = glob.glob(os.path.join(MV14, p))
            if files:
                break
        if not files:
            raise SystemExit(f"no take file for {scene} {take}")
        f = files[0]
        h = hashlib.md5(open(f, "rb").read()).hexdigest()
        if h != md5:
            raise SystemExit(f"md5 mismatch {scene} {take}: {h} != {md5}")
        items.append({"id": f"mv14_{scene.lower()}_{take}", "project": "MV-14",
                      "scene": scene, "take": take, "file": f, "md5": md5})
    return items


def mv14_planned():
    primary, grid, windows = {}, {}, {}
    grid_words = json.load(open(os.path.join(MV14, "analysis/SONG_WORDS.json")))["words"]
    row_pat = re.compile(r"\|\s*(S\d+)\s*\|\s*([\d.]+)–([\d.]+)\s*\|(.*)")
    for line in open(os.path.join(MV14, "work/MV_PREPRO_MV-14.md")):
        m = row_pat.match(line)
        if not m:
            continue
        scene, a, b = m.group(1), float(m.group(2)), float(m.group(3))
        cells = line.split("|")
        lyric_cell = cells[3] if len(cells) > 3 else ""
        frags = re.findall(r"[\"“]([^\"”]+)[\"”]", lyric_cell)
        planned = []
        for frag in frags:
            planned.extend(words_of(frag))
        primary[scene] = sorted(set(planned))
        windows[scene] = (a, b)
        grid[scene] = sorted({normalize(w["word"]) for w in grid_words
                              if a <= w["start"] < b and normalize(w["word"])})
    return primary, grid, windows


def mv2_grid_words(a, b):
    words = json.load(open(os.path.join(MV2, "SONG_WORDS_BASE.json")))
    return sorted({normalize(w["word"]) for w in words
                   if a <= w["t0"] < b and normalize(w["word"])})


def main():
    items = mv14_keep_takes()
    primary, grid, _win = mv14_planned()
    for it in items:
        it["planned_primary"] = primary[it["scene"]]
        it["planned_grid"] = grid[it["scene"]]
    items.append({
        "id": "mv2_s04_t3", "project": "MV-2", "scene": "S04", "take": "t3",
        "file": os.path.join(MV2, "takes/mv2_s04_t3.mp4"), "md5": None,
        "planned_primary": mv2_grid_words(41.90, 48.84),
        "alt_segment_words": mv2_grid_words(34.56, 40.94),
        "note": "proven wrong-segment positive: sang the 34.56-40.94s "
                "segment at S04's slot (TAKE_HISTORY.md v3 audit; "
                "loop 3 §2 #5, loop 6 §3 #2)",
    })
    items.append({
        "id": "mv2_s21_t1", "project": "MV-2", "scene": "S21", "take": "t1",
        "file": os.path.join(MV2, "takes/mv2_s21_t1.mp4"), "md5": None,
        "planned_primary": mv2_grid_words(205.20, 213.80),
        "note": "candidate positive (loop 6: 'S21 candidate pending "
                "verification'): sang a chorus echo line stretched over "
                "the verse slot (TAKE_HISTORY.md v3 audit)",
    })
    out = os.path.join(HERE, "fixture.json")
    json.dump({"items": items}, open(out, "w"), indent=1)
    print(f"{len(items)} items -> {out}")
    wl = [it['scene'] for it in items
          if it['project'] == 'MV-14' and not it['planned_primary']]
    print(f"MV-14 wordless (planned_primary empty): {len(wl)} {wl}")
    dis = [(it['scene'], it['planned_primary'], it['planned_grid'])
           for it in items if it['project'] == 'MV-14'
           and it['planned_primary'] != it['planned_grid']]
    print(f"primary-vs-grid disagreements: {len(dis)}")
    for s, p, g in dis:
        print(f"  {s}: primary={p} grid={g}")


if __name__ == "__main__":
    main()
