"""Lyric-match audit v2 — sequence alignment per viewing-cut clip (2026-11-03).

Fixes v1's midpoint method:
- Aligns the take's dictated word SEQUENCE against the song's word sequence
  in the same output window (difflib opcodes), so a matched line sung at a
  different internal pace reads as TIMING DRIFT, not as substitutions.
- Folds KNOWN Whisper mishear tokens on BOTH sides before aligning, and
  reports the raw tokens alongside, so a fold is visible, not hidden:
  tall/told/toe/tow -> toll ; done -> dumb (hook context, kept visible);
  paid -> pay ; plasers -> plazas ; flaselines -> fast lanes (flagged);
  bricks -> brakes ; comin'/comin -> coming ; weavin' -> weaving ;
  watchin' -> watching ; $1 -> dollar ; gonna -> going (flagged).
  Contraction tails ('s) are stripped for alignment only.
- Captions: per SRT cue, first/last song word inside the cue interval,
  foreign song words inside the interval, cue words with no song word.

Output: LYRIC_MATCH_AUDIT_2026-11-03_v2.json + printed report sections.
"""
import json, pathlib, re, difflib

proj = pathlib.Path.home() / "workspace/wubutv-network/musicvideo/MV-2_toll-roads-are-dumb"

def norm(w):
    w = w.lower().replace("\u2019", "'").replace("\u201c", "").replace("\u201d", "")
    return w.strip(".,!?;:\"'()")

FOLD = {
    "tall": "toll", "told": "toll", "toe": "toll", "tow": "toll", "toll": "toll",
    "done": "dumb", "down": "dumb",
    "paid": "pay",
    "plasers": "plazas", "plaser": "plazas",
    "bricks": "brakes",
    "comin": "coming", "comin'": "coming",
    "weavin": "weaving", "weavin'": "weaving",
    "watchin": "watching", "watchin'": "watching",
    "$1": "dollar", "1": "dollar",
    "rex": "wrecks", "files": "fast",
}
def fold(w):
    n = norm(w)
    n = FOLD.get(n, n)
    if n.endswith("'s"):
        n = n[:-2]
    if n.endswith("s") and n in ("wrecks",):
        pass
    return n

song = json.load(open(proj / "SONG_WORDS_BASE.json"))
song = [{"word": w["word"], "n": fold(w["word"]), "raw": norm(w["word"]), "t0": w["t0"], "t1": w["t1"]} for w in song]

srt = (proj / "captions_v2.srt").read_text()
cues = []
for b in re.split(r"\n\s*\n", srt.strip()):
    lines = b.strip().splitlines()
    if len(lines) < 3:
        continue
    m = re.match(r"(\d+):(\d+):(\d+),(\d+) --> (\d+):(\d+):(\d+),(\d+)", lines[1])
    if not m:
        continue
    def ts(h, mi, s, ms): return int(h)*3600 + int(mi)*60 + int(s) + int(ms)/1000
    cues.append({"t0": ts(*m.groups()[:4]), "t1": ts(*m.groups()[4:]),
                 "text": " ".join(lines[2:]),
                 "words": [fold(x) for x in " ".join(lines[2:]).split()]})

clips = json.load(open(proj / "masters_work_viewingcut/cutlist_working.json"))["clips"]
take_words = json.load(open(proj / "TAKE_WORDS_AUDIT_2026-11-03.json"))

mapped = []
for c in clips:
    tw = take_words.get(c["take"]) or []
    for w, t0, t1 in tw:
        if t0 < c["tau0"] - 0.01 or t1 > c["tau1"] + 0.01:
            continue
        out0 = c["out_start"] + (t0 - c["tau0"]) / c["factor"]
        out1 = c["out_start"] + (t1 - c["tau0"]) / c["factor"]
        mapped.append({"take": c["take"], "label": c["label"], "word": w, "n": fold(w),
                       "raw": norm(w), "out_t0": round(out0, 2), "out_t1": round(out1, 2)})

report = {"clips": [], "captions": [], "filler_words": []}
for c in clips:
    sw = [w for w in song if w["t1"] > c["out_start"] and w["t0"] < c["out_end"]]
    mw = [m for m in mapped if m["take"] == c["take"] and m["out_t0"] < c["out_end"] and m["out_t1"] > c["out_start"]]
    sm = difflib.SequenceMatcher(a=[w["n"] for w in sw], b=[m["n"] for m in mw], autojunk=False)
    ops = []
    offsets = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            for k in range(i2 - i1):
                s_, m_ = sw[i1 + k], mw[j1 + k]
                off = round(((m_["out_t0"] + m_["out_t1"]) / 2 - (s_["t0"] + s_["t1"]) / 2) * 24)
                offsets.append(off)
            ops.append({"op": "equal", "song": " ".join(w["word"] for w in sw[i1:i2]),
                        "mouth": " ".join(m["word"] for m in mw[j1:j2])})
        elif tag == "replace":
            ops.append({"op": "REPLACE", "song": " ".join(w["word"] for w in sw[i1:i2]),
                        "mouth": " ".join(m["word"] for m in mw[j1:j2]),
                        "song_span": [sw[i1]["t0"], sw[i2-1]["t1"]] if i2 > i1 else None,
                        "mouth_span": [mw[j1]["out_t0"], mw[j2-1]["out_t1"]] if j2 > j1 else None})
        elif tag == "delete":
            ops.append({"op": "SONG-ONLY (mouth skips)", "song": " ".join(w["word"] for w in sw[i1:i2]),
                        "song_span": [sw[i1]["t0"], sw[i2-1]["t1"]]})
        elif tag == "insert":
            ops.append({"op": "MOUTH-ONLY (extra/spill)", "mouth": " ".join(m["word"] for m in mw[j1:j2]),
                        "mouth_span": [mw[j1]["out_t0"], mw[j2-1]["out_t1"]]})
    off_s = f"median {sorted(offsets)[len(offsets)//2]}f" if offsets else "n/a"
    off_r = f"{min(offsets)}..{max(offsets)}f" if offsets else ""
    report["clips"].append({"label": c["label"], "take": c["take"],
                            "out": [c["out_start"], c["out_end"]], "factor": c["factor"],
                            "song_words": " ".join(w["word"] for w in sw),
                            "mouth_words": " ".join(m["word"] for m in mw),
                            "matched": sum(1 for o in ops if o["op"] == "equal"),
                            "offset_median_frames": off_s, "offset_range_frames": off_r,
                            "ops": ops})
    if c["label"] == "FILLER" and mw:
        report["filler_words"].append({"take": c["take"], "out": [c["out_start"], c["out_end"]],
                                       "words": " ".join(m["word"] for m in mw)})

for cue in cues:
    inside = [w for w in song if w["t1"] > cue["t0"] and w["t0"] < cue["t1"]]
    foreign = [w for w in inside if w["n"] not in cue["words"]]
    missing = [w for w in cue["words"] if w not in [x["n"] for x in inside]]
    lead = round(inside[0]["t0"] - cue["t0"], 2) if inside else None
    lag = round(cue["t1"] - inside[-1]["t1"], 2) if inside else None
    report["captions"].append({"cue": cue["text"], "interval": [cue["t0"], cue["t1"]],
                               "first_song_word_at": inside[0]["t0"] if inside else None,
                               "last_song_word_end": inside[-1]["t1"] if inside else None,
                               "caption_leads_first_word_s": lead,
                               "caption_outlives_last_word_s": lag,
                               "foreign_song_words_in_interval": " ".join(w["word"] for w in foreign),
                               "cue_words_with_no_song_word": " ".join(missing)})

json.dump(report, open(proj / "LYRIC_MATCH_AUDIT_2026-11-03_v2.json", "w"), indent=1)

for cl in report["clips"]:
    print(f"\n== {cl['label']} {cl['take']} {cl['out'][0]}-{cl['out'][1]}s x{cl['factor']} | matched={cl['matched']} offset {cl['offset_median_frames']} range {cl['offset_range_frames']}")
    print(f"   SONG : {cl['song_words']}")
    print(f"   MOUTH: {cl['mouth_words']}")
    for o in cl["ops"]:
        if o["op"] != "equal":
            print(f"   !! {o['op']}: song[{o.get('song','')}] mouth[{o.get('mouth','')}] {o.get('song_span','')} {o.get('mouth_span','')}")
print("\n== FILLER CLIPS WITH WORDS:", report["filler_words"] or "none")
print("\n== CAPTION CUES WITH LEAD>1s, LAG>1s, OR FOREIGN WORDS:")
for cu in report["captions"]:
    lead, lag = cu["caption_leads_first_word_s"], cu["caption_outlives_last_word_s"]
    if (lead is not None and lead > 1) or (lag is not None and lag > 1) or cu["foreign_song_words_in_interval"]:
        print(f" - [{cu['interval'][0]}-{cu['interval'][1]}s] \"{cu['cue']}\" lead={lead}s lag={lag}s foreign=[{cu['foreign_song_words_in_interval']}] cue-words-missing=[{cu['cue_words_with_no_song_word']}]")
