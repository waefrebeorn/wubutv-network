#!/usr/bin/env python3
"""MV-4 assembly cutlist builder v3: grid-search the best single-warp placement.

Per scene, search warp in [0.80, 1.25] x trim in [max(0, t_first-0.1), t_first+0.5]
(step 0.01 / 0.02s) and pick the placement minimizing median |word-start offset|
subject to:
  - first word placed within +-0.30s of the song's first word
  - last word END residual >= -0.75s (mouth must not close >0.75s early)
  - trim >= 0 (cannot start before the take begins)
Tie-break: smaller max |off|, then warp closest to the span warp.
This subsumes SPAN (trim=t_first, warp=span) and FIT (regression point) and
rejects infeasible fits (negative trim) automatically. S29's missing repeat
(7 take words vs 10 song words) cannot be fixed by any warp; it stays SPAN
with the repeat disclosed.
"""
import json, difflib, os
import numpy as np

PROJ = os.path.dirname(os.path.abspath(__file__))
SONG = json.load(open(os.path.join(PROJ, "SONG_WORDS.json")))["words"]

def norm(tok):
    t = tok.lower().strip(".,!?\"'()[]").replace("'s", "s").replace("n't", "nt")
    return t.replace("twenty-thirteen", "2013").replace("twentythirteen", "2013").replace("twenty-seven", "2027")

def merge_future(words):
    out = []
    i = 0
    while i < len(words):
        w = words[i]
        if norm(w["word"]) == "future" and i + 1 < len(words) and norm(words[i + 1]["word"]).startswith("rama"):
            out.append({"word": "Futurama's", "start": w["start"], "end": words[i + 1]["end"]})
            i += 2
        else:
            out.append(w); i += 1
    return out

def load_take(sc):
    ws = merge_future(json.load(open(os.path.join(PROJ, "work", "assembly_take_words", f"{sc}_unprompted.json"))))
    # FIRST-WORD ONSET CORRECTIONS (visual + RMS cross-check, 2026-11-05):
    # Whisper back-fills the first word to 0.00 on a quiet lead-in, and the
    # prompted decode overshoots to 1.06. Contact-sheet frames show NOVA's
    # mouth CLOSED at 0.0s and OPEN (singing shape) by 0.5s in both takes;
    # RMS rises from ~0.00 at 0.0-0.2s (S08) / is already 0.13 (S03).
    # True onsets: S03 ~0.45s, S08 ~0.30s. Only the first word's start is
    # corrected; all later word stamps are used as measured.
    if sc == "S03":
        ws[0]["start"] = 0.45
    if sc == "S08":
        ws[0]["start"] = 0.30
    return ws

SCENES = [
    ("S01", "mv4_s01_t1", 0.00, 7.70, None), ("S02", "mv4_s02_t1", 7.70, 15.32, None),
    ("S03", "mv4_s03_t1", 16.00, 23.34, None), ("S04", "mv4_s04_t1", 23.34, 30.54, None),
    ("S05", "mv4_s05_t1", 32.36, 39.72, None), ("S06", "mv4_s06_t3", 39.72, 46.88, None),
    ("S07", "mv4_s07_t1", 46.88, 54.20, None), ("S08", "mv4_s08_t1", 54.20, 63.04, None),
    ("S09", "mv4_s09_t1", 64.82, 72.04, None), ("S10", "mv4_s10_t1", 72.80, 79.52, None),
    ("S11", "mv4_s11_t1", 79.52, 86.96, "first15"), ("S12", "mv4_s12_t1", 86.96, 95.40, None),
    ("S13", "mv4_s13_t1", 95.40, 103.36, None), ("S14", "mv4_s14_t1", 103.36, 110.34, None),
    ("S15", "mv4_s15_t1", 110.34, 117.96, None), ("S16", "mv4_s16_t1", 117.96, 126.44, None),
    ("S17", "mv4_s17_t1", 126.44, 133.82, None), ("S18", "mv4_s18_t1", 133.82, 140.56, None),
    ("S19", "mv4_s19_t1", 140.56, 147.86, None), ("S20", "mv4_s20_t1", 148.40, 155.16, None),
    ("S21", "mv4_s21_t1", 158.76, 166.54, None), ("S22", "mv4_s22_t1", 166.54, 173.90, None),
    ("S24", "mv4_s24_t1", 181.24, 187.46, None), ("S26", "mv4_s26_t1", 194.06, 198.38, None),
    ("S27", "mv4_s27_t1", 198.38, 204.72, None), ("S29", "mv4_s29_t1", 211.75, 220.77, None),
]
SEG_END = {
    "S01": 7.70, "S02": 16.00, "S03": 23.34, "S04": 32.36, "S05": 39.72, "S06": 46.88,
    "S07": 54.20, "S08": 64.82, "S09": 72.80, "S10": 79.52, "S11": 86.96, "S12": 95.40,
    "S13": 103.36, "S14": 110.34, "S15": 117.96, "S16": 126.44, "S17": 133.82, "S18": 140.56,
    "S19": 148.40, "S20": 158.76, "S21": 166.54, "S22": 173.90, "S24": 188.24,
    "S26": 198.38, "S27": 205.09, "S29": 220.77,
}

def pairs_for(take, song, sc=None):
    t_tok = [norm(w["word"]) for w in take]
    s_tok = [norm(w["word"]) for w in song]
    if sc == "S29":
        # Take sings "Good news, everyone" ONCE then "For real this time";
        # the song repeats "Good news, everyone" twice. Align the take's
        # single delivery to the FIRST occurrence + "For real this time".
        return [(0, 0), (1, 1), (2, 2), (3, 6), (4, 7), (5, 8), (6, 9)]
    if len(take) == len(song):
        return list(zip(range(len(take)), range(len(song))))
    sm = difflib.SequenceMatcher(a=t_tok, b=s_tok, autojunk=False)
    pairs = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            for k in range(i2 - i1):
                pairs.append((i1 + k, j1 + k))
    return pairs

results = {}
print(f"{'sc':4} {'warp':>6} {'trim':>6} {'band':>6} {'med':>6} {'max':>6} {'first':>6} {'lastEnd':>7} {'span_w':>6}  note")
for sc, f, s0, s1, special in SCENES:
    take = load_take(sc)
    if special == "first15":
        take = take[:15]
    song = merge_future([w for w in SONG if s0 - 0.05 <= w["start"] < s1])
    pairs = pairs_for(take, song, sc)
    t_first, t_last = take[0]["start"], take[-1]["end"]
    span_w = (s1 - s0) / (t_last - t_first)
    xs = np.array([take[i]["start"] for i, _ in pairs])
    ys = np.array([song[j]["start"] for _, j in pairs])
    # SPAN baseline (trim at first word, warp = song span / take span)
    o_span = s0 + (xs - t_first) * span_w - ys
    span_med = float(np.median(np.abs(o_span)))
    best = None
    for warp in np.arange(0.80, 1.251, 0.01):
        for trim in np.arange(max(0.0, t_first - 0.10), t_first + 0.251, 0.02):
            placed = s0 + (xs - trim) * warp
            offs = placed - ys
            first_off = placed[0] - ys[0]
            if abs(first_off) > 0.30:
                continue
            last_end = s0 + (t_last - trim) * warp - s1
            if last_end < -0.75 or last_end > 0.50:
                continue
            band = int((np.abs(offs) <= 0.50).sum())
            med = float(np.median(np.abs(offs)))
            mx = float(np.max(np.abs(offs)))
            # PRIMARY: most words inside +-0.50s (a median can hide a
            # sacrificed line); then median, then max, then closest to span.
            key = (-band, round(med, 3), round(mx, 3), abs(warp - span_w))
            if best is None or key < best[0]:
                best = (key, warp, trim, med, mx, first_off, last_end, band)
    _, warp, trim, med, mx, first_off, last_end, band = best
    o_span = s0 + (xs - t_first) * span_w - ys
    span_med = float(np.median(np.abs(o_span)))
    span_band = int((np.abs(o_span) <= 0.50).sum())
    # Prefer the endpoint-anchored SPAN placement unless the grid beats it on
    # band count, or on median by >= 0.10s with equal band (SPAN is the
    # conservative, better-understood default; a marginal median gain on a
    # 4-word scene is Whisper noise).
    if band < span_band or (band == span_band and med + 0.10 >= span_med):
        warp, trim = span_w, t_first
        placed = s0 + (xs - trim) * warp
        offs = placed - ys
        med = float(np.median(np.abs(offs)))
        mx = float(np.max(np.abs(offs)))
        first_off = float(placed[0] - ys[0])
        last_end = float(s0 + (t_last - trim) * warp - s1)
        band = span_band
        mode = "SPAN"
    else:
        mode = "GRID"
    agr = sum(1 for i, j in pairs if norm(take[i]["word"]) == norm(song[j]["word"])) / max(len(song), 1)
    note = ""
    if abs(warp - span_w) > 0.05:
        note = "warp!=span"
    if med > 0.5:
        note += " WEAK-MEDIAN"
    results[sc] = {"file": f, "warp": round(float(warp), 3), "trim": round(float(trim), 3),
                   "mode": mode, "song_start": s0, "song_end": s1, "seg_end": SEG_END[sc],
                   "take_first": t_first, "take_last": t_last, "agreement": round(float(agr), 3),
                   "median_abs_off": round(med, 3), "max_abs_off": round(mx, 3),
                   "band": band, "span_band": span_band, "span_median": round(span_med, 3),
                   "first_word_off": round(float(first_off), 3),
                   "last_end_resid": round(float(last_end), 3),
                   "span_warp": round(float(span_w), 3), "n_take": len(take),
                   "n_song": len(song), "pairs": len(pairs)}
    print(f"{sc:4} {warp:>6.3f} {trim:>6.2f} {band:>3}/{len(pairs):<2} {med:>6.3f} {mx:>6.2f} {first_off:>6.2f} {last_end:>7.2f} {span_w:>6.3f}  {mode}{note}")

json.dump(results, open(os.path.join(PROJ, "work", "assembly_fit.json"), "w"), indent=1)
print("\nwrote work/assembly_fit.json")
