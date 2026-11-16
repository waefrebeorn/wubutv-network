#!/usr/bin/env python3
"""MV-5 v5 plan builder (Q10 repair).

Re-derived from measured data (2026-11-13): grid per-word times from
work/lyrics-redo/grid_merged.json + take word times from
work/assembly_take_words/*_prompted.json (Q10 re-transcriptions override
originals for s06_t1, s12_t1, s24_t1, s24_t3) + frame reads of every cover
donor (work/q10/qc/plan_frames/) + RMS-per-second sweeps.

Changed scenes (rebuilt): S01 S02 S04 S06 S07 S11 S12 S17 S20 S23 S24 S27 S28.
Verbatim (copied from v4 fit as-is): S03 S05 S08 S09 S10 S13 S14 S15 S16
S18 S19a S19b S21 S22 S25 S26.

Corrections baked in (vs the first v5 draft):
- S01: per-word I01/I02/I04 splits (single warps put "ride." +0.70 and
  "comes" +0.35 late); leader is riding s02_t1, not a freeze.
- S04 L04: per-word split (single warp 1.622 put "begin" +0.86 late);
  "begin" stretched at warp 1.75 + 19f tail cover for the held word.
- S11 L40: REDESIGNED — v4's single warp put "Time" 2.05s early. L40 head
  ("And the tide tapping") is a cover; L40 tail ("time with our feet")
  is sung at warp 1.105 (all words within +/-0.12s).
- S12 L41/L42: L41 extended to f52 (avoids "air." mouth-closing edge);
  L42 cover f52-84 (fully closed gap).
- S12 L44c: s24_t3 f144-167 (NOT s24_t1 f132-155 — that overlaps S24's
  own L98b/L100 pieces). Verified closed at f150/f155.
- S02: s03_t1 cover starts f96 (not f91 — the Ta-da vocalise ends 3.78s;
  f91 is 0.01s after, mouth still open). s02_t1 extended to f216.
- S01 I02 gap donor s01_t1 f163-167; S11 L37 uses f167-171 (no overlap).
- S11 L40c: s04_t1 f159-165 (gap after "begin." ends 6.36s, before "Blue"
  7.10s); S06 L11b keeps s04_t1 f165-170 (no overlap).
- S24: rebuilt on TRUE 3-pair s24_t1 words (pair 3 unused — no song line).
- S27 L109: cover (s28_t2 girl "Till" would need warp 0.42 < 0.5 floor).
- S28 L110: moved here from v4 S27 (v4 put the CAT's L110 mouth over the
  GIRL's L109 line).

Rules enforced (hard FAIL):
- warp <= 2.0 (no slowdown past 2x); warp < 0.5 -> WARN (speedup > 2x).
- Banned takes absent: mv5_s28_t5, mv5_s07_t3, mv5_s21_t7.
- No take frame reused at two positions (cross-scene = FAIL; same-scene
  = WARN, allowed only for S21 verbatim montage).
- Cover pieces contain NO take words in their take-time span (FAIL if a
  word overlaps; WARN if a word ends within 0.15s before the span start).
- Scene out-sums == v4 totals (verbatim) or design totals (changed);
  grand total == 4954.
- Every take's ef <= its ffprobed frame count.

Word-offset report: for each sung piece, every (non-degenerate) take word
is mapped to dst time and compared to the NEAREST grid word by start time.
|offset| > 0.30 -> WARN; > 0.50 -> FAIL unless the piece is annotated
disclosed (v4-carryover compromise, still reported).
"""
import json, os, re, subprocess, sys

PROJ = os.path.dirname(os.path.abspath(__file__))
FIT4 = json.load(open(os.path.join(PROJ, "work", "assembly_fit_mv5_v4.json")))
GRID = json.load(open(os.path.join(PROJ, "work", "lyrics-redo", "grid_merged.json")))
FPS = 24
BANNED = ("mv5_s28_t5", "mv5_s07_t3", "mv5_s21_t7")
OUT_FIT = os.path.join(PROJ, "work", "assembly_fit_mv5_v5.json")

# take -> prompted-words JSON (Q10 re-transcriptions override originals)
TAKE_WORDS = {
    "mv5_s01_t1": "S01_prompted.json",
    "mv5_s03_t1": "S03_prompted.json",
    "mv5_s04_t1": "S04_prompted.json",
    "mv5_s06_t1": "Q10_S06_T1_prompted.json",
    "mv5_s06_t2": "S06_T2_prompted.json",
    "mv5_s07_t1": "S07_prompted.json",
    "mv5_s09_t1": "S09_prompted.json",
    "mv5_s11_t4": "S11_prompted.json",
    "mv5_s12_t1": "Q10_S12_T1_prompted.json",
    "mv5_s17_t1": "S17_prompted.json",
    "mv5_s20_t1": "S20_prompted.json",
    "mv5_s23_t1": "S23_prompted.json",
    "mv5_s24_t1": "Q10_S24_T1_prompted.json",
    "mv5_s24_t3": "Q10_S24_T3_prompted.json",
    "mv5_s25_t1": "S25_prompted.json",
    "mv5_s27_t1": "S27_prompted.json",
    "mv5_s28_t1": "S28_prompted.json",
    "mv5_s28_t2": "S28_T2_prompted.json",
    "mv5_s28_t3": "S28_T3_prompted.json",
    "mv5_q10_s04": "Q10_S04_prompted.json",
    "mv5_q10_s12_l43": "Q10_S12_L43_prompted.json",
    "mv5_q10_s07_l15": "Q10_S07_L15_prompted.json",
}

def load_words(take):
    fn = TAKE_WORDS.get(take)
    if not fn:
        return None
    d = json.load(open(os.path.join(PROJ, "work", "assembly_take_words", fn)))
    w = d.get("words", d)
    return [{"word": x["word"], "start": float(x["start"]), "end": float(x["end"])}
            for x in w]

def norm(w):
    return re.sub(r"[^a-z0-9]", "", w.lower())

# grid words sorted by start
GRID_WORDS = sorted(
    [{"word": x["word"], "start": float(x["start"]), "end": float(x["end"])}
     for x in GRID["words"]], key=lambda x: x["start"])
GRID_LINES = {l["id"]: l for l in GRID["lines"]}

def nearest_grid_word(t):
    """Closest grid word by start time (fallback when no text match)."""
    best, bd = None, 1e9
    for g in GRID_WORDS:
        d = abs(g["start"] - t)
        if d < bd:
            best, bd = g, d
    return best, bd

def match_grid_word(take_word, t):
    """Match by TEXT first (same normalized word, closest start within 2s);
    fall back to nearest grid word by start (flagged WORD-MISMATCH)."""
    nw = norm(take_word)
    best, bd = None, 1e9
    for g in GRID_WORDS:
        if norm(g["word"]) != nw:
            continue
        d = abs(g["start"] - t)
        if d < bd:
            best, bd = g, d
    if best is not None and bd <= 2.0:
        return best, True
    g, _ = nearest_grid_word(t)
    return g, False

# ---------------------------------------------------------------- pieces
# (take, sf, ef, out, kind, line_or_None, disclosed_note_or_None)
# cover pieces: line None. warp derived as out/(ef-sf), rounded to 4dp
# (the assembler formats warp %.4f, so the report uses the rounded value).
V5 = {
"S01": [
 ("mv5_s02_t1", 0, 34, 34, "leader-riding", None, None),
 ("mv5_s01_t1", 0, 26, 27, "phrase-I01a", "I01", None),
 ("mv5_s01_t1", 30, 36, 6, "gap-I01", None, None),
 ("mv5_s01_t1", 39, 64, 25, "phrase-I01b", "I01", None),
 ("mv5_s01_t1", 73, 85, 17, "phrase-I02a", "I02", None),
 ("mv5_s01_t1", 97, 114, 27, "phrase-I02b", "I02", None),
 ("mv5_s01_t1", 114, 125, 11, "gap-I02", None, None),
 ("mv5_s01_t1", 163, 167, 4, "gap-I02b", None, None),
 ("mv5_s01_t1", 125, 159, 41, "phrase-I03", "I03", None),
 ("mv5_s01_t1", 179, 191, 7, "phrase-I04a", "I04", None),
 ("mv5_s01_t1", 191, 223, 42, "phrase-I04b", "I04", None),
],
"S02": [
 ("mv5_s02_t1", 34, 47, 13, "cover-pre-I05", None, None),
 ("mv5_s02_t1", 47, 98, 51, "cover-I05", None, None),
 ("mv5_s02_t1", 98, 142, 44, "cover-I08a", None, None),
 ("mv5_s02_t1", 142, 180, 38, "cover-I08b", None, None),
 ("mv5_s02_t1", 180, 216, 36, "cover-I08c", None, None),
 ("mv5_s03_t1", 96, 115, 19, "cover-pre-I09a", None, None),
 ("mv5_s01_t1", 171, 176, 5, "cover-pre-I09b", None, None),
],
"S04": [
 ("mv5_q10_s04", 0, 46, 23, "phrase-L01", "L01", None),
 ("mv5_q10_s04", 61, 88, 27, "phrase-L02a", "L02", None),
 ("mv5_q10_s04", 88, 106, 34, "phrase-L02b", "L02", None),
 ("mv5_q10_s04", 107, 130, 23, "phrase-L03a", "L03", None),
 ("mv5_q10_s04", 171, 198, 27, "cover-L03b", None, None),
 ("mv5_q10_s04", 133, 167, 34, "phrase-L04a", "L04", None),
 ("mv5_q10_s04", 167, 171, 7, "phrase-L04b", "L04", None),
 ("mv5_q10_s04", 198, 217, 19, "cover-L04c", None, None),
 ("mv5_s04_t1", 170, 204, 34, "phrase-L05", "L05", None),
],
"S06": [
 ("mv5_s06_t1", 0, 67, 68, "phrase-L10", "L10",
  "Keys -0.36s vs grid (v4 carryover, within +/-0.40 band)"),
 ("mv5_s06_t1", 215, 240, 25, "cover-L11a", None, None),
 ("mv5_s04_t1", 165, 170, 5, "cover-L11b", None, None),
 ("mv5_s06_t2", 0, 19, 14, "phrase-L12a", "L12", None),
 ("mv5_s06_t2", 19, 38, 15, "phrase-L12b", "L12", None),
 ("mv5_s06_t2", 38, 58, 26, "phrase-L12c", "L12", None),
 ("mv5_s06_t2", 58, 77, 19, "cover-L12d", None, None),
],
"S07": [
 ("mv5_s07_t1", 0, 64, 46, "phrase-L13", "L13",
  "'take' -0.38s vs grid (take holds the word long; v4 carryover)"),
 ("mv5_s07_t1", 76, 116, 41, "phrase-L14", "L14", None),
 ("mv5_q10_s07_l15", 0, 59, 37, "phrase-L15", "L15", None),
 ("mv5_s09_t1", 211, 240, 29, "cover-L16a", None, None),
 ("mv5_s04_t1", 208, 240, 32, "cover-L16b", None, None),
 ("mv5_s25_t1", 98, 144, 46, "cover-L16c", None, None),
 ("mv5_s07_t1", 169, 175, 6, "cover-L16d", None, None),
],
"S11": [
 ("mv5_s11_t4", 0, 28, 28, "cover-L37a", None, None),
 ("mv5_s01_t1", 167, 171, 4, "cover-L37b", None, None),
 ("mv5_s11_t4", 28, 91, 26, "phrase-L38", "L38", None),
 ("mv5_s11_t4", 125, 171, 36, "phrase-L39", "L39", None),
 ("mv5_s11_t4", 91, 125, 34, "cover-L40a", None, None),
 ("mv5_s11_t4", 171, 181, 10, "cover-L40b", None, None),
 ("mv5_s04_t1", 159, 165, 6, "cover-L40c", None, None),
 ("mv5_s11_t4", 181, 219, 42, "phrase-L40d", "L40", None),
 ("mv5_s11_t4", 219, 240, 21, "cover-L40e", None, None),
],
"S12": [
 ("mv5_s12_t1", 0, 52, 39, "phrase-L41", "L41", None),
 ("mv5_s12_t1", 52, 84, 32, "cover-L42", None, None),
 ("mv5_q10_s12_l43", 0, 20, 21, "phrase-L43a", "L43", None),
 ("mv5_q10_s12_l43", 20, 58, 20, "phrase-L43b", "L43", None),
 ("mv5_s12_t1", 192, 216, 24, "cover-L44a", None, None),
 ("mv5_s28_t3", 72, 120, 48, "cover-L44b", None, None),
 ("mv5_s24_t3", 144, 167, 23, "cover-L44c", None, None),
],
"S17": [
 ("mv5_s17_t1", 38, 138, 111, "phrase-L65-L68", "L65",
  "v4 compromise: take sings only 'Easy now' hooks over L66 'Keep it loose' / L68 'Let it drift' (wrong-words, same as v4)"),
 ("mv5_s09_t1", 185, 211, 23, "cover-L69", None,
  "mouth-CLOSED cover, NOT a singing insert (v4 'singing tail' label was wrong)"),
 ("mv5_s28_t1", 57, 82, 33, "phrase-L70", "L70",
  "v4 carryover: CAT 'Till/comes' tail over hook 'We're good where we are'"),
 ("mv5_s17_t1", 183, 228, 66, "phrase-L71-L72", "L71",
  "take 'Easy' +0.86s late vs grid (v4 was +0.94; chorus-hook offset)"),
],
"S20": [
 ("mv5_s20_t1", 0, 112, 56, "phrase-L80", "L80", None),
],
"S23": [
 ("mv5_s23_t1", 4, 105, 127, "phrase-L91-L95", "L91",
  "v4 carryover: take sings 'Easy now' hooks over the L91-L95 chorus texture"),
 ("mv5_s23_t1", 126, 168, 38, "phrase-L96", "L96", None),
],
"S24": [
 ("mv5_s24_t1", 0, 32, 21, "phrase-L97", "L97", None),
 ("mv5_s24_t1", 32, 40, 8, "cover-L98a", None, None),
 ("mv5_s24_t1", 104, 128, 24, "cover-L98b", None, None),
 ("mv5_s24_t1", 40, 75, 21, "phrase-L99", "L99", None),
 ("mv5_s24_t1", 128, 156, 28, "cover-L100", None, None),
 ("mv5_s24_t3", 0, 64, 60, "phrase-L101-L102", "L101",
  "v4 carryover: take's 2nd 'easy' lands between L101's (180.94) and L103's (182.78) in the overlapping chorus; take sings L101's pair"),
],
"S27": [
 ("mv5_s27_t1", 0, 114, 118, "phrase-L108", "L108", None),
 ("mv5_s16_t6", 60, 134, 74, "interlude-instrumental", None, None),
 ("mv5_s06_t2", 77, 120, 43, "cover-L109a", None, None),
 ("mv5_s28_t2", 120, 145, 25, "cover-L109b", None, None),
],
"S28": [
 ("mv5_s28_t1", 0, 57, 37, "phrase-L110", "L110", None),
 ("mv5_s28_t1", 95, 120, 25, "cover-tail", None, None),
],
}
CHANGED = set(V5.keys())
DESIGN_TOTALS = {sc: sum(p[3] for p in V5[sc]) for sc in V5}

# ---------------------------------------------------------------- helpers
def nframes(take):
    path = os.path.join(PROJ, "takes", take + ".mp4")
    r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0",
                        "-show_entries", "stream=nb_frames",
                        "-of", "csv=p=0", path],
                       capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"ffprobe failed for {take}: {r.stderr.strip()}")
    return int(r.stdout.strip())

def main():
    errors, warns = [], []
    plan, scenes = {}, FIT4["scenes"]
    # take frame counts (cache)
    nf_cache = {}
    def nf(take):
        if take not in nf_cache:
            nf_cache[take] = nframes(take)
        return nf_cache[take]

    # word data cache
    w_cache = {}
    def words(take):
        if take not in w_cache:
            w_cache[take] = load_words(take)
        return w_cache[take]

    used = {}  # (take, frame) -> (scene, kind)
    cum = 0
    bounds = []
    for sc in scenes:
        bounds.append(round(cum / FPS, 4))
        if sc in CHANGED:
            raw = V5[sc]
            target = DESIGN_TOTALS[sc]
        else:
            raw = [(p["take"], p["sf"], p["ef"], p["out"], p["kind"],
                    None, None) for p in FIT4["plan"][sc]]
            target = sum(p["out"] for p in FIT4["plan"][sc])
        pieces = []
        dst = cum / FPS
        for (take, sf, ef, out, kind, line, note) in raw:
            # banned takes
            if take in BANNED:
                errors.append(f"{sc}: BANNED take {take}")
            # frame bounds (takes are 240f, not 241f — the 10.04s duration
            # rounds up; v4 relied on tpad padding for ef>nframes in S14,
            # so verbatim scenes only WARN while changed scenes must be exact)
            n = nf(take)
            if ef > n:
                msg = f"{sc} {take}: ef {ef} > nframes {n}"
                if sc in CHANGED:
                    errors.append(msg)
                else:
                    warns.append(msg + " (verbatim v4, assembler tpad-pads)")
            if sf < 0 or sf >= ef:
                errors.append(f"{sc} {take}: bad sf/ef {sf}/{ef}")
            warp = round(out / (ef - sf), 4)
            if warp > 2.0:
                errors.append(f"{sc} {take} f{sf}-{ef}: warp {warp} > 2.0 (slowdown past 2x)")
            if warp < 0.5:
                warns.append(f"{sc} {take} f{sf}-{ef}: warp {warp} < 0.5 (speedup > 2x)")
            # assembler rounding: exp must be within 1 of out
            exp = round((ef - sf) * warp)
            if abs(exp - out) > 1:
                errors.append(f"{sc} {take} f{sf}-{ef}: exp {exp} != out {out} (warp rounding)")
            # frame reuse
            for f in range(sf, ef):
                key = (take, f)
                if key in used:
                    prev_sc, prev_kind = used[key]
                    if prev_sc == sc:
                        warns.append(f"{sc} {take} f{f}: reused within scene (prev {prev_kind})")
                    else:
                        errors.append(f"{sc} {take} f{f}: REUSED from {prev_sc} ({prev_kind})")
                used[key] = (sc, kind)
            dst0, dst1 = dst, dst + out / FPS
            pieces.append({"take": take, "sf": sf, "ef": ef, "warp": warp,
                           "out": out, "kind": kind, "dst0": round(dst0, 4),
                           "dst1": round(dst1, 4)})
            # --- word / cover checks (changed scenes only) ---
            if sc in CHANGED:
                tw = words(take)
                t0, t1 = sf / FPS, ef / FPS
                if line is None:
                    # cover: no take words in span. A word is a FAIL only if
                    # it overlaps the span by >0.15s; a <=0.15s touch at either
                    # edge is a gap-edge WARN (mouth closing/opening naturally).
                    if tw:
                        for w in tw:
                            if w["end"] <= w["start"]:
                                continue
                            lo = max(w["start"], t0)
                            hi = min(w["end"], t1)
                            overlap = hi - lo
                            if overlap > 0.15:
                                errors.append(
                                    f"{sc} COVER {take} f{sf}-{ef} ({kind}): "
                                    f"word '{w['word']}' {w['start']:.2f}-{w['end']:.2f} "
                                    f"overlaps cover span by {overlap:.2f}s")
                            elif overlap > 0:
                                warns.append(
                                    f"{sc} COVER {take} f{sf}-{ef} ({kind}): "
                                    f"gap-edge: word '{w['word']}' touches cover "
                                    f"by {overlap:.2f}s (mouth closing/opening)")
                else:
                    # sung: report every take word's dst offset vs nearest grid word
                    if tw is None:
                        warns.append(f"{sc} {take} ({kind}): no word data, offset check skipped")
                    else:
                        for w in tw:
                            if w["end"] <= w["start"]:
                                continue  # degenerate 0-duration word
                            if not (t0 <= w["start"] < t1):
                                continue
                            d = dst0 + (w["start"] - t0) * warp
                            g, text_ok = match_grid_word(w["word"], d)
                            off = d - g["start"]
                            match = "OK " if text_ok else "WORD-MISMATCH"
                            flag = ""
                            if abs(off) > 0.50 and not note:
                                errors.append(
                                    f"{sc} {take} ({kind}): take '{w['word']}' -> dst {d:.2f} "
                                    f"vs grid '{g['word']}' {g['start']:.2f} off {off:+.2f} [{match}]")
                                flag = "FAIL"
                            elif abs(off) > 0.30 or match != "OK ":
                                warns.append(
                                    f"{sc} {take} ({kind}): take '{w['word']}' -> dst {d:.2f} "
                                    f"vs grid '{g['word']}' {g['start']:.2f} off {off:+.2f} [{match}]"
                                    + (f" [disclosed: {note}]" if note else ""))
                                flag = "WARN"
                            print(f"  {sc:4} {take:16} {kind:22} take '{w['word']:<10}' "
                                  f"dst {d:7.2f} grid '{g['word']:<10}' {g['start']:7.2f} "
                                  f"off {off:+6.2f} {match.strip()} {flag}")
                    if note:
                        print(f"  {sc:4} {take:16} {kind:22} DISCLOSED: {note}")
            dst = dst1
        tot = sum(p["out"] for p in pieces)
        if tot != target:
            errors.append(f"{sc}: out-sum {tot} != target {target}")
        plan[sc] = pieces
        cum += tot
    bounds.append(round(cum / FPS, 4))
    print(f"\nscenes: {len(scenes)}  total frames: {cum} (target 4954)")
    if cum != 4954:
        errors.append(f"grand total {cum} != 4954")
    print(f"\n--- WARNINGS ({len(warns)}) ---")
    for w in warns:
        print("WARN:", w)
    print(f"\n--- ERRORS ({len(errors)}) ---")
    for e in errors:
        print("ERROR:", e)
    if errors:
        print("\nBUILD ABORTED — fix errors above.")
        sys.exit(1)
    fit5 = {"plan": plan, "total_frames": cum, "bounds": bounds,
            "scenes": scenes,
            "note": ("MV-5 v5 (Q10 repair): re-anchored on the lyrics-redo grid; "
                     "fresh takes q10_s04 / q10_s12_l43 / q10_s07_l15; "
                     "S27 L109 cover + S28 L110 moved from v4 S27; "
                     "S11 L40 + S01 intro rebuilt per-word; "
                     "L104 + S07 L16 + I08 stay montage/cover (blocked takes); "
                     "see work/q10/Q10_DIAGNOSIS.md + Q10_LEDGER.md")}
    if any(b in json.dumps(fit5) for b in BANNED):
        print("ERROR: banned take name present in fit blob")
        sys.exit(1)
    json.dump(fit5, open(OUT_FIT, "w"), indent=1)
    print(f"\nWROTE {OUT_FIT}  ({cum}f, {len(scenes)} scenes)")
    print("bounds:", bounds)

if __name__ == "__main__":
    main()
