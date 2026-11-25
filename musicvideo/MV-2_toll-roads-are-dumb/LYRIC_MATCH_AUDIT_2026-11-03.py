"""Frame-exact lyric-match audit for the MV-2 viewing cut (2026-11-03).

Three streams, all on the master's output timeline (seconds, 24fps):
  A = song audio: SONG_WORDS_BASE.json (404 words, t0/t1) — ground truth.
  B = on-screen lyrics: captions_v2.srt cues (line blocks from LYRIC_TIMELINE).
  C = mouth: fresh raw Whisper dictation TAKE_WORDS_AUDIT_2026-11-03.json,
      mapped through masters_work_viewingcut/cutlist_working.json clips:
      out = out_start + (take_time - tau0) / factor
      (factor = take span / song span in the cutlist; verified: out span * factor = tau span)

Comparisons (exact normalized words; no mishear folding):
  1. For every take word: song word overlapping its output midpoint.
     MATCH / WORD-SUBSTITUTION (take word != song word) / EXTRA (no song word overlaps).
  2. For every song word: take word overlapping its midpoint (or NONE = uncovered),
     and caption cue shown at its midpoint (or NONE).
  3. Caption lead/lag per song word: cue_start - word_t0, word_t1 - cue_end.
  4. Per-segment summary from VIEWING_CUT_2026-11-03.json segments + clips.

Output: LYRIC_MATCH_AUDIT_2026-11-03.json + .md
"""
import json, pathlib, re

proj = pathlib.Path.home() / "workspace/wubutv-network/musicvideo/MV-2_toll-roads-are-dumb"

def norm(w):
    w = w.lower().replace("\u2019", "'").replace("\u201c", "").replace("\u201d", "")
    return w.strip(".,!?;:\"'()")

song = json.load(open(proj / "SONG_WORDS_BASE.json"))
song = [{"word": w["word"], "n": norm(w["word"]), "t0": w["t0"], "t1": w["t1"]} for w in song]

# --- SRT parse ---
srt = (proj / "captions_v2.srt").read_text()
cues = []
blocks = re.split(r"\n\s*\n", srt.strip())
for b in blocks:
    lines = b.strip().splitlines()
    if len(lines) < 3:
        continue
    m = re.match(r"(\d+):(\d+):(\d+),(\d+) --> (\d+):(\d+):(\d+),(\d+)", lines[1])
    if not m:
        continue
    def ts(h, mi, s, ms): return int(h)*3600 + int(mi)*60 + int(s) + int(ms)/1000
    t0 = ts(*m.groups()[:4]); t1 = ts(*m.groups()[4:])
    text = " ".join(lines[2:])
    cues.append({"t0": t0, "t1": t1, "text": text,
                 "words": [norm(x) for x in text.split()]})

def at(t, items):
    for it in items:
        if it["t0"] <= t < it["t1"] or (t == it["t1"] and it is items[-1]):
            return it
    return None

def song_at(t):
    for w in song:
        if w["t0"] <= t <= w["t1"]:
            return w
    return None

clips = json.load(open(proj / "masters_work_viewingcut/cutlist_working.json"))["clips"]
take_words = json.load(open(proj / "TAKE_WORDS_AUDIT_2026-11-03.json"))

# --- map take words to output time ---
mapped = []  # {take, label, word, n, out_t0, out_t1}
for c in clips:
    tw = take_words.get(c["take"])
    if not tw:
        continue
    for w, t0, t1 in tw:
        out0 = c["out_start"] + (t0 - c["tau0"]) / c["factor"] if c["factor"] else c["out_start"]
        out1 = c["out_start"] + (t1 - c["tau0"]) / c["factor"] if c["factor"] else c["out_start"]
        # only words whose take-time falls inside the used tau window
        if t0 < c["tau0"] - 0.01 or t1 > c["tau1"] + 0.01:
            continue
        mapped.append({"take": c["take"], "label": c["label"], "word": w, "n": norm(w),
                       "out_t0": round(out0, 2), "out_t1": round(out1, 2),
                       "take_t0": t0, "take_t1": t1})

take_word_rows = []
for m in mapped:
    mid = (m["out_t0"] + m["out_t1"]) / 2
    sw = song_at(mid)
    cue = at(mid, cues)
    if sw is None:
        verdict = "EXTRA-NO-SONG-WORD"
        detail = f"mouth '{m['word']}' at {m['out_t0']}-{m['out_t1']}s ({m['label']}/{m['take']}) while no song word sounds"
    elif sw["n"] == m["n"]:
        verdict = "MATCH"
        detail = ""
    else:
        verdict = "SUBSTITUTION"
        detail = (f"mouth '{m['word']}' at {m['out_t0']}-{m['out_t1']}s ({m['label']}/{m['take']}) "
                  f"while song sings '{sw['word']}' at {sw['t0']}-{sw['t1']}s")
    take_word_rows.append({**m, "song_word": sw["word"] if sw else None,
                           "song_t0": sw["t0"] if sw else None, "song_t1": sw["t1"] if sw else None,
                           "caption": cue["text"] if cue else None, "verdict": verdict, "detail": detail})

# --- song-word coverage ---
song_rows = []
for w in song:
    mid = (w["t0"] + w["t1"]) / 2
    tw = None
    for m in mapped:
        if m["out_t0"] <= mid <= m["out_t1"]:
            tw = m; break
    cue = at(mid, cues)
    cap_has = cue is not None and w["n"] in cue["words"]
    song_rows.append({"word": w["word"], "n": w["n"], "t0": w["t0"], "t1": w["t1"],
                      "mouth_word": tw["word"] if tw else None,
                      "mouth_take": tw["take"] if tw else None,
                      "mouth_label": tw["label"] if tw else None,
                      "mouth_match": (tw["n"] == w["n"]) if tw else False,
                      "caption_text": cue["text"] if cue else None,
                      "caption_has_word": cap_has,
                      "caption_lead_s": round(cue["t0"] - w["t0"], 2) if cue else None,
                      "caption_lag_s": round(w["t1"] - cue["t1"], 2) if cue else None})

# --- per-clip summary ---
clip_rows = []
for c in clips:
    ms = [m for m in mapped if m["take"] == c["take"] and abs(m["out_t0"] - c["out_start"]) < 0.01 or
          (m["take"] == c["take"] and c["out_start"] <= m["out_t0"] < c["out_end"])]
    # simpler: mapped words whose out interval intersects clip
    ms = [m for m in mapped if m["take"] == c["take"] and m["out_t0"] < c["out_end"] and m["out_t1"] > c["out_start"]]
    subs = [r for r in take_word_rows if r["take"] == c["take"] and r["verdict"] == "SUBSTITUTION"]
    clip_rows.append({"label": c["label"], "take": c["take"], "out": [c["out_start"], c["out_end"]],
                      "factor": c["factor"], "words": " ".join(m["word"] for m in ms),
                      "n_substitutions": len(subs)})

summary = {
    "song_words_total": len(song),
    "song_words_mouth_match": sum(1 for r in song_rows if r["mouth_match"]),
    "song_words_mouth_substitution": sum(1 for r in song_rows if r["mouth_word"] and not r["mouth_match"]),
    "song_words_no_mouth": sum(1 for r in song_rows if not r["mouth_word"]),
    "song_words_caption_has_word": sum(1 for r in song_rows if r["caption_has_word"]),
    "song_words_caption_missing_word": sum(1 for r in song_rows if not r["caption_has_word"]),
    "take_words_total": len(take_word_rows),
    "take_words_match": sum(1 for r in take_word_rows if r["verdict"] == "MATCH"),
    "take_words_substitution": sum(1 for r in take_word_rows if r["verdict"] == "SUBSTITUTION"),
    "take_words_extra": sum(1 for r in take_word_rows if r["verdict"] == "EXTRA-NO-SONG-WORD"),
}
out = {"summary": summary, "take_word_rows": take_word_rows, "song_rows": song_rows, "clip_rows": clip_rows}
json.dump(out, open(proj / "LYRIC_MATCH_AUDIT_2026-11-03.json", "w"), indent=1)
print(json.dumps(summary, indent=1))
print("\nSUBSTITUTIONS (mouth != song at same frame):")
for r in take_word_rows:
    if r["verdict"] == "SUBSTITUTION":
        print(" -", r["detail"])
print("\nEXTRA mouth words (no song word at that frame):")
for r in take_word_rows:
    if r["verdict"] == "EXTRA-NO-SONG-WORD":
        print(" -", r["detail"])
print("\nSONG WORDS WITH NO MOUTH (first 60):")
for r in song_rows:
    if not r["mouth_word"]:
        print(f" - {r['word']} {r['t0']}-{r['t1']}s caption={'YES' if r['caption_has_word'] else 'NO'}")
