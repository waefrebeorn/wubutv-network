#!/usr/bin/env python3
"""Swing-keyframe analyzer — take audio swing -> per-word warp keyframes.

The method (user order 2026-11-06; see SWING_METHOD.md): a generated
take sings its line at its OWN tempo, not the song's. Transcribe the
take's own sample audio per word, align it to the song's measured word
times, and the per-word offsets (the take's "swing") become warp
keyframes: each interval between word anchors is warped so every take
word lands on its song word. Words the take gets WRONG / drops /
repeats / can only place with a >2x slowdown become fast montage cuts —
out on a beat, back on the next good word's onset, onto a proper
lipsync take.

Built on the crosscheck method (MV-3 recut_work/sync_proto/
crosscheck_sync.py + CROSSCHECK_SYNC_METHOD.md), SLERM'd forward:
same fw-venv faster-whisper path, same dual decode, same mishear-map
discipline; new here = swing-offset keyframes, per-word verdicts,
beat-snapped montage spans.

Adjudication traps handled (all established, none invented):
  * Split-half recheck: a zero-word full-clip decode is NOT a no-line
    verdict (MV-2 rule) — halves are re-decoded and offsets added back.
  * Mishear classes are decoding artifacts, applied to BOTH sides
    before matching (MV-2/MV-3 map: told/tall/toe->toll, paid->pay,
    tell->sell, done->dumb, game->dad, dogs->hooks, see->say,
    face->phrase). MV-5's documented systematic class (Whisper hears
    the hook word "easy" as "is it", 28x in the song dictation) is
    applied ONLY when the line contains "easy" and no real "is", and
    the split "it" is then counted as part of the mishear, not a
    repeat. The applied map is recorded in the output.
  * Prompted vs unprompted disagreement: the unprompted decode is the
    floor. A word ONLY the prompted decode hears is credited only if
    the audio RMS in its span supports it (>= 0.35x the median RMS of
    confirmed words); otherwise it is a prompt hallucination and the
    song word stays BAD-missing. (Unprompted + RMS wins.)
  * Mouth-lag caution: take AUDIO word times can lead the visible
    mouth by up to ~1s (MV-2 v6 lesson). Keyframes are assembly HINTS;
    the master gate still verifies mouth state at song onsets.

Warp law (user, 2026-11-06): per-word warping is the method. Speedups
are unrestricted (flag >3x as a hard squeeze to disclose). Slowdowns
are capped at 2x slow = playback speed 0.5; an interval needing slower
is BAD-out-of-caps and goes to montage, never a >2x slow stretch.

Usage:
  swing_keyframes.py --take takes/mv5_s07_t2.mp4 \
      --line "One small look from you" --line-id L15
  swing_keyframes.py --take takes/mv5_s01_t1.mp4 \
      --line "Easy now, easy now, we ride, we ride, easy now, easy now, till the morning comes" \
      --window 1.66 10.04
Options: --project DIR (default: the project this script lives in),
--song-words FILE (default <project>/SONG_WORDS.json; the MV-5 dict
shape and the MV-3 list-of-[word,start,end] shape both load),
--beat-grid FILE (default <project>/work/swing/beat_grid.json),
--out FILE (default: work/swing/<take>_swing.json),
--fw-python PATH (default ~/workspace/fw-venv/bin/python).
Plain python3 stdlib in this file; faster-whisper runs in the fw-venv
subprocess exactly as crosscheck_sync.py does. No video generation.
"""
import argparse
import difflib
import json
import math
import os
import re
import subprocess
import sys
import tempfile
import wave

BASE_MISHEAR = {"told": "toll", "tall": "toll", "toe": "toll",
                "paid": "pay", "tell": "sell", "done": "dumb",
                "game": "dad", "dogs": "hooks", "see": "say",
                "face": "phrase"}
PUNCT = ".,!?\"'’‘;:—–-"

GOOD_SWING = 0.25          # s — anchored offset tier for GOOD
BAND_LO, BAND_HI = 0.80, 1.25   # generation band (GOOD warp window)
SLOW_CAP = 0.5             # playback speed floor (2x slow law)
HARD_SQUEEZE = 3.0         # speedup flag threshold (disclose)
RMS_CREDIT = 0.35          # prompted-only credit: RMS support ratio


def norm(tok, mishear):
    t = tok.strip().lower().strip(PUNCT)
    return mishear.get(t, t)


def tokens_of(text, mishear):
    return [norm(t, mishear) for t in text.split() if norm(t, mishear)]


# ---------------------------------------------------------------- song side
def load_song_words(path):
    """Return list of dicts {word,start,end,line} from either known shape."""
    d = json.load(open(path))
    out = []
    words = d["words"] if isinstance(d, dict) else d
    for w in words:
        if isinstance(w, dict):
            out.append({"word": w["word"], "start": float(w["start"]),
                        "end": float(w["end"]), "line": w.get("line")})
        else:  # [word, start, end]
            out.append({"word": w[0], "start": float(w[1]),
                        "end": float(w[2]), "line": None})
    lines = d.get("lines") if isinstance(d, dict) else None
    return out, lines


def select_line_words(words, lines, line_id, window, line_text, mishear):
    if line_id:
        sel = [w for w in words if w.get("line") == line_id]
        if sel:
            return sel, f"line-id {line_id}"
    if window:
        a, b = window
        sel = [w for w in words if a <= w["start"] < b]
        if sel:
            return sel, f"window {a}-{b}"
    if line_text and lines:
        want = tokens_of(line_text, {})
        for ln in lines:
            if tokens_of(ln.get("text", ""), {}) == want:
                sel = [w for w in words if w.get("line") == ln["id"]]
                if sel:
                    return sel, f"line-text match {ln['id']}"
    if line_id or window or line_text:
        raise SystemExit("could not select song words for the line "
                         "(check --line-id / --window / --line-text)")
    raise SystemExit("one of --line-id, --window, --line-text is required")


# ---------------------------------------------------------------- take side
def extract_wav(src, dst):
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src,
                    "-ac", "1", "-ar", "16000", "-vn", dst], check=True)
    return dst


def transcribe_wav(wav, fw_python, initial_prompt=None):
    """faster-whisper base via the fw-venv, exactly as crosscheck_sync."""
    code = (
        "import json, sys, wave, numpy as np\n"
        "from faster_whisper import WhisperModel\n"
        "wav, prompt = sys.argv[1], sys.argv[2]\n"
        "model = WhisperModel('base', device='cpu', compute_type='int8')\n"
        "with wave.open(wav) as wf:\n"
        "    frames = wf.readframes(wf.getnframes())\n"
        "audio = np.frombuffer(frames, dtype=np.int16).astype(np.float32) / 32768.0\n"
        "kw = dict(word_timestamps=True, language='en')\n"
        "if prompt:\n"
        "    kw['initial_prompt'] = prompt\n"
        "segments, _ = model.transcribe(audio, **kw)\n"
        "words = []\n"
        "for seg in segments:\n"
        "    for w in (seg.words or []):\n"
        "        t = w.word.strip()\n"
        "        if t:\n"
        "            words.append([t, round(w.start, 3), round(w.end, 3)])\n"
        "print(json.dumps(words))\n"
    )
    out = subprocess.run([fw_python, "-c", code, wav, initial_prompt or ""],
                         capture_output=True, text=True, check=True)
    return json.loads(out.stdout.strip().splitlines()[-1])


def wav_duration(wav):
    with wave.open(wav) as wf:
        return wf.getnframes() / wf.getframerate()


def slice_wav(wav, start, dur, dst):
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(start),
                    "-t", str(dur), "-i", wav, dst], check=True)
    return dst


def rms_span(wav, a, b):
    with wave.open(wav) as wf:
        sr = wf.getframerate()
        total = wf.getnframes()
        start = min(max(0, int(a * sr)), total)
        wf.setpos(start)
        n = max(1, int((b - a) * sr))
        raw = wf.readframes(min(n, total - start))
    if not raw:
        return 0.0
    vals = memoryview(raw).cast("h")
    return math.sqrt(sum(v * v for v in vals) / len(vals)) / 32768.0


def decode_take(take_path, fw_python, prompt, tmp):
    """Unprompted + prompted decodes; split-half recheck on zero words."""
    wav = extract_wav(take_path, os.path.join(tmp, "take.wav"))
    dur = wav_duration(wav)
    unp = transcribe_wav(wav, fw_python)
    split = False
    if not unp:
        split = True
        half = min(5.0, dur)
        words = []
        for (a, ln) in [(0.0, half), (half, dur - half)]:
            if ln <= 0:
                continue
            part = slice_wav(wav, a, ln, os.path.join(tmp, f"half_{a}.wav"))
            for w, s, e in transcribe_wav(part, fw_python):
                words.append([w, round(s + a, 3), round(e + a, 3)])
        unp = words
    pro = transcribe_wav(wav, fw_python, prompt)
    return wav, dur, unp, pro, split


# ---------------------------------------------------------------- alignment
def align(song_toks, take_toks):
    """difflib opcodes -> per-song-word match info + take extras."""
    sm = difflib.SequenceMatcher(a=song_toks, b=take_toks, autojunk=False)
    match = {}   # song idx -> take idx
    extras = []  # take idx with no song counterpart
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            for k in range(i2 - i1):
                match[i1 + k] = j1 + k
        elif tag == "replace":
            for k in range(min(i2 - i1, j2 - j1)):
                match[i1 + k] = ("replace", j1 + k)
            for j in range(j1 + min(i2 - i1, j2 - j1), j2):
                extras.append(j)
        elif tag == "insert":
            extras.extend(range(j1, j2))
        # delete: song word unmatched — nothing to record
    return match, extras


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    here = os.path.dirname(os.path.abspath(__file__))
    default_proj = os.path.dirname(os.path.dirname(here))
    ap.add_argument("--take", required=True)
    ap.add_argument("--line", required=True, help="the take's prompted line")
    ap.add_argument("--project", default=default_proj)
    ap.add_argument("--song-words", default=None)
    ap.add_argument("--line-id", default=None)
    ap.add_argument("--window", nargs=2, type=float, default=None)
    ap.add_argument("--line-text", default=None,
                    help="match a line in the song-words 'lines' table")
    ap.add_argument("--beat-grid", default=None)
    ap.add_argument("--out", default=None)
    ap.add_argument("--fw-python",
                    default=os.path.expanduser("~/workspace/fw-venv/bin/python"))
    args = ap.parse_args()

    proj = args.project
    take_path = args.take if os.path.isabs(args.take) else os.path.join(proj, args.take)
    song_path = args.song_words or os.path.join(proj, "SONG_WORDS.json")
    grid_path = args.beat_grid or os.path.join(proj, "work", "swing", "beat_grid.json")
    out_path = args.out or os.path.join(
        here, os.path.splitext(os.path.basename(take_path))[0] + "_swing.json")

    words_all, lines_table = load_song_words(song_path)

    # mishear map: base classes + conditional MV-5 'easy' class
    mishear = dict(BASE_MISHEAR)
    raw_line_toks = tokens_of(args.line, {})
    easy_class = ("easy" in raw_line_toks and "is" not in raw_line_toks)
    if easy_class:
        mishear["is"] = "easy"

    sel, how = select_line_words(words_all, lines_table, args.line_id,
                                 args.window, args.line_text or args.line,
                                 mishear)
    song = [{"word": w["word"], "start": w["start"], "end": w["end"],
             "tok": norm(w["word"], mishear)} for w in sel]
    song_toks = [w["tok"] for w in song]

    beats = []
    if os.path.exists(grid_path):
        beats = [b["t"] for b in json.load(open(grid_path))["beats"]]

    def beat_le(t):
        prev = None
        for b in beats:
            if b <= t:
                prev = b
            else:
                break
        return prev

    def beat_ge(t):
        for b in beats:
            if b >= t:
                return b
        return None

    tmp = tempfile.mkdtemp(prefix="swing_")
    wav, dur, unp_raw, pro_raw, split = decode_take(
        take_path, args.fw_python, args.line, tmp)

    def prep(raw):
        return [{"word": w, "start": s, "end": e, "tok": norm(w, mishear)}
                for w, s, e in raw]

    unp, pro = prep(unp_raw), prep(pro_raw)
    m_unp, ex_unp = align(song_toks, [w["tok"] for w in unp])
    m_pro, _ = align(song_toks, [w["tok"] for w in pro])

    # confirmed-word RMS baseline (unprompted matches) for hallucination test
    conf_rms = [rms_span(wav, unp[j]["start"], unp[j]["end"])
                for j in m_unp.values() if not isinstance(j, tuple)]
    med_rms = sorted(conf_rms)[len(conf_rms) // 2] if conf_rms else 0.0

    # resolve each song word: unprompted first, prompted+RMS credit second
    rows = []
    for i, sw in enumerate(song):
        row = {"song_word": sw["word"], "song_start": sw["start"],
               "song_end": sw["end"], "take_word": None, "take_start": None,
               "take_end": None, "source": None, "raw_offset": None,
               "swing_offset": None, "interval_to_next_anchor": None,
               "verdict": None, "notes": []}
        j = m_unp.get(i)
        if isinstance(j, int):
            tw = unp[j]
            row.update(take_word=tw["word"], take_start=tw["start"],
                       take_end=tw["end"], source="unprompted")
        elif isinstance(j, tuple):  # replace pair: different token heard
            tw = unp[j[1]]
            row.update(take_word=tw["word"], take_start=tw["start"],
                       take_end=tw["end"], source="unprompted",
                       verdict="BAD-wrong",
                       notes=[f"take sings '{tw['word']}' here"])
        else:
            jp = m_pro.get(i)
            cand = None
            if isinstance(jp, int):
                cand = pro[jp]
            elif isinstance(jp, tuple):
                cand = None
            if cand is not None:
                r = rms_span(wav, cand["start"], cand["end"])
                if med_rms and r >= RMS_CREDIT * med_rms:
                    row.update(take_word=cand["word"],
                               take_start=cand["start"],
                               take_end=cand["end"],
                               source="prompted+rms",
                               notes=[f"prompted-only, RMS {r:.3f} >= "
                                      f"{RMS_CREDIT}x median {med_rms:.3f} — credited"])
                else:
                    row.update(verdict="BAD-missing",
                               notes=[f"prompted decode alone hears "
                                      f"'{cand['word']}' but RMS {r:.3f} does "
                                      f"not support it — prompt hallucination"])
            else:
                row.update(verdict="BAD-missing",
                           notes=["no take word aligns to this song word"])
        if row["take_start"] is not None:
            row["raw_offset"] = round(row["take_start"] - sw["start"], 3)
        rows.append(row)

    # extras: repeats / mishear splits / other
    extras = []
    matched_take = {j for j in m_unp.values() if isinstance(j, int)}
    for j in ex_unp:
        tw = unp[j]
        if easy_class and tw["tok"] == "it" and j > 0 and (j - 1) in matched_take \
                and unp[j - 1]["tok"] == "easy":
            extras.append({**{k: tw[k] for k in ("word", "start", "end")},
                           "class": "mishear-split (is->easy + it)",
                           "counts_as": "nothing"})
        elif tw["tok"] in song_toks:
            extras.append({**{k: tw[k] for k in ("word", "start", "end")},
                           "class": "BAD-repeat",
                           "counts_as": "the take sings this word an extra time"})
        else:
            extras.append({**{k: tw[k] for k in ("word", "start", "end")},
                           "class": "extra",
                           "counts_as": "unmatched take word"})

    # swing offsets + interval warps between matched anchors
    anchors = [i for i, r in enumerate(rows) if r["take_start"] is not None]
    if anchors:
        a0 = anchors[0]
        for i in anchors:
            rows[i]["swing_offset"] = round(
                (rows[i]["take_start"] - rows[a0]["take_start"])
                - (rows[i]["song_start"] - rows[a0]["song_start"]), 3)
        for k, i in enumerate(anchors):
            r = rows[i]
            if k + 1 < len(anchors):
                j = anchors[k + 1]
                t_int = rows[j]["take_start"] - r["take_start"]
                s_int = rows[j]["song_start"] - r["song_start"]
                span_words = j - i
            else:
                t_int = r["take_end"] - r["take_start"]
                s_int = r["song_end"] - r["song_start"]
                span_words = 1
            if t_int > 0 and s_int > 0:
                speed = t_int / s_int
                r["interval_to_next_anchor"] = {
                    "take_interval_s": round(t_int, 3),
                    "song_interval_s": round(s_int, 3),
                    "playback_speed": round(speed, 3),
                    "setpts_factor": round(s_int / t_int, 4),
                    "spans_song_words": span_words}
                if r["verdict"] is None:
                    if speed < SLOW_CAP:
                        r["verdict"] = "BAD-out-of-caps"
                        r["notes"].append(
                            f"interval needs playback {speed:.2f}x — past the "
                            f"2x-slow cap; montage, never stretch")
                    elif BAND_LO <= speed <= BAND_HI and abs(r["swing_offset"]) <= GOOD_SWING:
                        r["verdict"] = "GOOD"
                    else:
                        r["verdict"] = "WARPABLE"
                        if speed > HARD_SQUEEZE:
                            r["notes"].append(
                                f"hard squeeze {speed:.2f}x speedup — legal, disclose")
            elif r["verdict"] is None:
                r["verdict"] = "WARPABLE"
                r["notes"].append("zero-length interval stamp — warp by neighbours")

    # montage spans for BAD words (grouped), beat-snapped out, onset return
    bad_idx = [i for i, r in enumerate(rows)
               if r["verdict"] and r["verdict"].startswith("BAD")]
    repeat_spans = [e for e in extras if e["class"] == "BAD-repeat"]
    cuts = []
    groups = []
    for i in bad_idx:
        if groups and i == groups[-1][-1] + 1:
            groups[-1].append(i)
        else:
            groups.append([i])
    for g in groups:
        start = rows[g[0]]["song_start"]
        end = rows[g[-1]]["song_end"]
        nxt = next((rows[i] for i in anchors if i > g[-1]), None)
        cuts.append({
            "covers_words": [rows[i]["song_word"] for i in g],
            "span_song": [start, end],
            "cut_out_beat": beat_le(start),
            "return_onset": nxt["song_start"] if nxt else None,
            "return_beat": beat_ge(end),
            "action": "fast montage over this span; cut out on the beat, "
                      "return on the next good word's onset"})
    for e in repeat_spans:
        cuts.append({
            "covers_words": [e["word"]],
            "span_song": None,
            "take_span": [e["start"], e["end"]],
            "cut_out_beat": None, "return_onset": None, "return_beat": None,
            "action": "take repeats this word — trim/montage over the "
                      "repeated instance in take time"})

    summary = {}
    for r in rows:
        summary[r["verdict"] or "NONE"] = summary.get(r["verdict"] or "NONE", 0) + 1
    take_span = (round(rows[anchors[-1]]["take_end"] - rows[anchors[0]]["take_start"], 3)
                 if anchors else None)
    song_span = round(song[-1]["end"] - song[0]["start"], 3) if song else None
    out = {
        "take": os.path.basename(take_path),
        "take_duration_s": round(dur, 3),
        "prompted_line": args.line,
        "song_words_source": os.path.basename(song_path),
        "song_word_selection": how,
        "mishear_map_applied": mishear,
        "decodes": {"unprompted": [[w["word"], w["start"], w["end"]] for w in unp],
                    "prompted": [[w["word"], w["start"], w["end"]] for w in pro],
                    "split_half_recheck_used": split},
        "line_ratio_song_over_take": (round(song_span / take_span, 3)
                                      if take_span else None),
        "words": rows,
        "extras": extras,
        "keyframes": [{"word": rows[i]["song_word"],
                       "song_time": rows[i]["song_start"],
                       "take_time": rows[i]["take_start"]}
                      for i in anchors
                      if rows[i]["verdict"] in ("GOOD", "WARPABLE")],
        "montage_cuts": cuts,
        "summary": summary,
        "caution": "keyframes are assembly hints from take AUDIO times; "
                   "mouth can lag audio by up to ~1s — the master gate "
                   "verifies mouth state at song onsets",
    }
    with open(out_path, "w") as f:
        json.dump(out, f, indent=1)
    print(f"wrote {out_path}")
    print("summary:", summary, "| line ratio:", out["line_ratio_song_over_take"])
    for r in rows:
        iv = r["interval_to_next_anchor"] or {}
        print(f"  {r['song_word']:<8} song {r['song_start']:>7} take "
              f"{r['take_start']} swing {r['swing_offset']} "
              f"speed {iv.get('playback_speed')} -> {r['verdict']}")


if __name__ == "__main__":
    main()
