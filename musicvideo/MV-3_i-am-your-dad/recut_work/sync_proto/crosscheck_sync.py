#!/usr/bin/env python3
"""Cross-check lyric sync for MV-3 (prototype v1, 2026-11-05).

Implements the user's cross-check idea: transcribe the VIDEO side (take
audio, or the delivered master's audio) and the SONG side independently,
use the known PERFORMED lyrics as the context hint (Whisper
initial_prompt) that grounds both dictations, then align the two
dictations to each other per word and score agreement/disagreement.

Design (see CROSSCHECK_SYNC_METHOD.md for the full spec):
  * Dictation: faster-whisper base (~/workspace/fw-venv), word
    timestamps, numpy-array input; audio extracted with ffmpeg to a
    per-call temp wav (the venv's av decode path is broken; never share
    a temp wav between runs).
  * Lyrics hint: initial_prompt = the scene's performed line (take
    mode) or the full performed lyric text (master mode). The prompt
    biases decoding toward the known words; it does NOT force them --
    a take that sings something else still decodes as something else,
    and that disagreement is the signal.
  * Normalization before matching: lowercase, strip punctuation, and
    the MV-3 mishear map (game->dad, dogs->hooks, see->say,
    face->phrase, done->dumb). Mishears are a decoding artifact class,
    not a lyric difference.
  * Alignment: token-sequence alignment (difflib SequenceMatcher) of
    take words against the song words inside the scene window. No
    global shift, no slot matching: per-word offsets, because MV-3
    takes drift by TEMPO, not shift.
  * Placement: take word time t -> master time via the re-cut cutlist
    (imported SCENES table from assemble_mv3_recut.py -- scene start,
    per-piece warp w, trim start s): master = scene_start + (t - s) * w,
    accumulating across pieces for multi-piece scenes. Picture is
    warped, never the song.
  * Scoring per scene: matched/song words (agreement), median and max
    |offset|, drift (last - first offset), % of matched words within
    +/-0.125s / +/-0.25s / +/-0.50s. Zero-duration song words (Whisper
    pile-ups in the dense mantra blocks) are excluded from offset stats
    and counted separately -- they carry no usable time.

Read-only on all masters and delivered files: audio is extracted to
tmp/ and deleted after each transcription; nothing is re-encoded or
overwritten. Outputs (JSON + human-readable report) go to this dir.

Usage:
  crosscheck_sync.py takes [--takes mv3_s01_t2 ...] [--prompted-only]
  crosscheck_sync.py master [--skip-transcribe]   # uses cached master dictation if present
  crosscheck_sync.py placement                    # all-scene placement cross-check
                                                  # from recut_work/measure/*.json
"""
import difflib
import json
import os
import subprocess
import sys
import wave as _wave

import numpy as _np

PROJ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PROJ)
from assemble_mv3_recut import SCENES, SONG_END  # noqa: E402  (cutlist = placement truth)

FW_VENV_PY = os.path.expanduser("~/workspace/fw-venv/bin/python")
TAKES = os.path.join(PROJ, "takes")
MEASURE = os.path.join(PROJ, "recut_work", "measure")
MASTER_16X9 = os.path.join(PROJ, "masters", "mv3_i_am_your_dad_16x9_recut.mp4")
MASTER_MD5 = "300c89feaf5276763e0f8598bc2656d6"
SONG_WORDS = os.path.join(PROJ, "SONG_WORDS.json")
TRACK_MP3 = os.path.join(PROJ, "track.mp3")
TMP = os.path.join(HERE, "tmp")

MISHEAR = {"game": "dad", "dogs": "hooks", "see": "say",
           "face": "phrase", "done": "dumb", "told": "toll",
           "tall": "toll", "toe": "toll", "paid": "pay", "tell": "sell"}

# Performed lines per scene (from LYRIC_TIMELINE.md -- the PERFORMED song,
# not the abridged sheet in lyrics.txt). Used as the initial_prompt hint.
SCENE_LINES = {
    "S01": "Listen, all of you",
    "S02": "You already know, I am your dad",
    "S06": ("You walk by, you scroll by, you turn the radio on. "
            "And the voice in the speaker says the same thing all along"),
    "S07": ("I raised you in the dark, I raised you in the light. "
            "I raised every face that is listening tonight"),
    "S08": ("You don't have to like it, you don't have to stay, "
            "but the words keep coming and they won't go away"),
    "S09": "I am your dad, I am your dad, say it with me",
    "S10": "I am your dad, you're hearing once, you're hearing twice, now it lives inside",
    "S11": "I am your dad, I am your dad, don't fight the feeling, I am your dad",
    "S12": "I am your dad, I am your dad",
    "S13": "You got your real one maybe, or maybe you don't",
    "S14": "Matter to me, the message is the point",
    "S15": "You try to skip it, but you try to change the song, but the phrase comes back and it doesn't take long",
    "S16": "Short words, easy words, the kind that sticks fast, I am your dad, and the song will last",
    "S17": "I am your dad, I am your dad, say it with me",
    "S18": "I am your dad, you're hearing once, you're hearing twice, now it lives inside",
    "S19": "I am your dad, I am your dad, I am your dad, say it with me",
    "S20": "I am your dad, you're hearing twice, now it lives inside",
    "S22": "I am your dad, I am your dad, say it with me",
    "S23": "You can close your eyes, you can plug your ears, the words still bounce around inside your head",
    "S26": "They study the hooks, they study the loops, they say simple words",
    "S27": ("Make the brain stay true, repeat the same, I make it easy to sing, "
            "and the mind can play it on its own string"),
    "S28": ("I don't need a story, I don't need a name, "
            "just the one short claim that never changes"),
    "S29": "I am your dad, I am your dad, say it with me",
    "S34": "I am your dad, I am your dad, just a low voice",
    "S36": "All of you, every single one, I am your dad, you know it now",
    "S38": "Say it back to me, I am your dad, say it to yourself",
    "S39": "I am your dad",
}
FULL_PERFORMED_LYRICS = " ".join(SCENE_LINES[s] for s in sorted(SCENE_LINES))

# Mouth scenes in the re-cut (from CUTLIST_RECUT.md): scene -> (take file, cover flag)
MOUTH = {
    "S01": ("mv3_s01_t2.mp4", ""), "S02": ("mv3_s02_t2.mp4", ""),
    "S06": ("mv3_s06_t1.mp4", ""), "S07": ("mv3_s07_t1.mp4", "grey"),
    "S08": ("mv3_s08_t1.mp4", ""), "S09": ("mv3_s09_t1.mp4", "grey"),
    "S10": ("mv3_s10_t1.mp4", ""), "S11": ("mv3_s11_t2.mp4", "grey"),
    "S12": ("mv3_s12_t2.mp4", "grey"), "S13": ("mv3_s13_t1.mp4", ""),
    "S14": ("mv3_s14_t1.mp4", ""), "S15": ("mv3_s15_t1.mp4", ""),
    "S16": ("mv3_s16_t1.mp4", ""), "S17": ("mv3_s17_t1.mp4", ""),
    "S18": ("mv3_s18_t2.mp4", ""), "S19": ("mv3_s19_t1.mp4", ""),
    "S20": ("mv3_s20_t1.mp4", "grey"), "S22": ("mv3_s22_t1.mp4", ""),
    "S23": ("mv3_s23_t2.mp4", "grey"), "S26": ("mv3_s26_t1.mp4", ""),
    "S27": ("mv3_s27_t1.mp4", "phrasing-gap"), "S28": ("mv3_s28_t3.mp4", "grey"),
    "S29": ("mv3_s29_t1.mp4", "grey"), "S31": ("mv3_s31_t1.mp4", "mantra-slice"),
    "S32": ("mv3_s32_t1.mp4", "mantra-slice"), "S33": ("mv3_s33_t1.mp4", "mantra-slice"),
    "S34": ("mv3_s34_t1.mp4", "phrasing-gap"), "S36": ("mv3_s36_t2.mp4", "grey"),
    "S37": ("mv3_s37_t1.mp4", "mantra-opening"), "S38": ("mv3_s38_t2.mp4", "grey"),
    "S39": ("mv3_s39_t1.mp4", "montage-cover"),
}


def norm(w):
    t = w.strip().lower().strip(".,!?\"'’")
    return MISHEAR.get(t, t)


def extract_wav(src, tag):
    """ffmpeg -> mono 16k wav in tmp/ (per-call file, deleted by caller)."""
    wav = os.path.join(TMP, f"{tag}.wav")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src,
                    "-ac", "1", "-ar", "16000", "-vn", wav], check=True)
    return wav


def transcribe_wav(wav, initial_prompt=None):
    """Transcribe one wav with faster-whisper base via the fw-venv python.

    Runs as a subprocess so the model loads fresh per file (sequential,
    no shared state). Returns list of [word, start, end]."""
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
        "        t = w.word.strip().lower().strip('.,!?\"\\'’')\n"
        "        if t:\n"
        "            words.append([t, round(w.start, 2), round(w.end, 2)])\n"
        "print(json.dumps(words))\n"
    )
    out = subprocess.run([FW_VENV_PY, "-c", code, wav, initial_prompt or ""],
                         capture_output=True, text=True, check=True)
    return json.loads(out.stdout.strip().splitlines()[-1])


def transcribe_file(src, tag, initial_prompt=None):
    wav = extract_wav(src, tag)
    try:
        return transcribe_wav(wav, initial_prompt)
    finally:
        if os.path.exists(wav):
            os.remove(wav)


def song_words():
    d = json.load(open(SONG_WORDS))
    return [[norm(w), s, e] for w, s, e in d["words"]]


def scene_bounds():
    """scene -> (start_s, end_s) from the SCENES table (song time)."""
    starts = [(sc, st) for sc, st, _ in SCENES]
    bounds = {}
    for i, (sc, st) in enumerate(starts):
        end = starts[i + 1][1] if i + 1 < len(starts) else SONG_END
        bounds[sc] = (st, end)
    return bounds


def _place_piece(scene, piece_words, piece_index, take_len=None):
    """Map one take's words through ONE piece of a multi-piece scene.

    Prior pieces' warped durations accumulate into the master offset, so
    a second take's words land in the second piece's master window."""
    _, _, pieces = next(x for x in SCENES if x[0] == scene)
    sc_start = next(st for sc, st, _ in SCENES if sc == scene)
    mlo = sc_start
    for pi, (fn, w, s, e) in enumerate(pieces):
        hi = e if e != "FULL" else (take_len if take_len else
                                    max(t[2] for t in piece_words))
        if pi == piece_index:
            out = []
            for word, ts, te in piece_words:
                if s - 0.01 <= ts < hi:
                    out.append([word, round(mlo + max(0.0, ts - s) * w, 2),
                                round(mlo + max(0.0, te - s) * w, 2)])
            return out
        mlo += (hi - s) * w
    return []


def place_take_words(scene, take_words):
    """Map take-local word times to master (song) times via the cutlist.

    Pieces concatenate: each piece contributes (end_src - start_src) * w
    seconds of master time. Returns [(word, master_start, master_end)]."""
    _, _, pieces = next(x for x in SCENES if x[0] == scene)
    sc_start = next(st for sc, st, _ in SCENES if sc == scene)
    out = []
    # piece boundaries in take time and master time
    segs = []  # (take_lo, take_hi, master_lo, w)
    m = sc_start
    for fn, w, s, e in pieces:
        # source span: s .. e (e="FULL" -> take file length; use max word end)
        hi = e if e != "FULL" else max(t[2] for t in take_words)
        segs.append((s, hi, m, w))
        m += (hi - s) * w
    for word, s, e in take_words:
        for lo, hi, mlo, w in segs:
            if lo - 0.01 <= s < hi or (s < lo and e > lo):
                ms = mlo + max(0.0, s - lo) * w
                me = mlo + max(0.0, e - lo) * w
                out.append([word, round(ms, 2), round(me, 2)])
                break
        else:
            # word outside every piece span (e.g. tail-loop region): drop, count it
            pass
    return out


def align_score(song_win, take_placed):
    """Align take words (already placed in master time) to song window words.

    Returns dict with agreement, offsets, drift, tolerance buckets, and
    the disagreement lists. Zero-duration song words (pile-ups) excluded
    from offset stats."""
    song_toks = [norm(w) for w, _, _ in song_win]
    take_toks = [norm(w) for w, _, _ in take_placed]
    sm = difflib.SequenceMatcher(a=song_toks, b=take_toks, autojunk=False)
    pairs = []  # (song_idx, take_idx)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            pairs.extend(zip(range(i1, i2), range(j1, j2)))
    offsets = []
    usable_pairs = []
    wrong_repeat = []  # pairs matched by token order but implausibly far
    # apart in time. A pair counts as a WRONG-REPEAT matcher error (not a
    # timing error) ONLY if a nearer occurrence of the same token exists
    # in the song window (unmatched, within 0.5s of the take word's placed
    # time): the matcher credited the word to the wrong repeat. If no
    # nearer occurrence exists, the word is genuinely early/late (e.g. a
    # take tail ending 2-3s before the song's tail) and the pair is KEPT
    # -- dropping it would hide real error. (Method doc section 2c.)
    song_by_tok = {}
    for _i, (_w, _s, _e) in enumerate(song_win):
        song_by_tok.setdefault(norm(_w), []).append((_i, _s))
    matched_song_idx = {si for si, _ in pairs}
    for si, ti in pairs:
        sw, ss, se = song_win[si]
        tw, ts, te = take_placed[ti]
        if se - ss <= 0.0:
            continue  # pile-up stamp: no usable time
        off = round(ts - ss, 2)
        if abs(off) > 2.0:
            near = [s2 for (i2, s2) in song_by_tok.get(norm(sw), [])
                    if i2 not in matched_song_idx and abs(ts - s2) <= 0.5]
            if near:
                wrong_repeat.append([sw, ss, ts, off])
                continue
        offsets.append(off)
        usable_pairs.append((sw, ss, ts, off))
    n_song = len(song_win)
    n_pileup = sum(1 for _, s, e in song_win if e - s <= 0.0)
    matched_song_idx = {si for si, _ in pairs}
    missing = [song_win[i] for i in range(n_song) if i not in matched_song_idx]
    matched_take_idx = {ti for _, ti in pairs}
    extra = [take_placed[j] for j in range(len(take_placed)) if j not in matched_take_idx]
    if offsets:
        a = sorted(abs(o) for o in offsets)
        med = a[len(a) // 2]
        mx = a[-1]
        mean = round(sum(offsets) / len(offsets), 2)
        drift = round(offsets[-1] - offsets[0], 2) if len(offsets) > 1 else 0.0
    else:
        med = mx = mean = drift = None
    buckets = {}
    for tol in (0.125, 0.25, 0.50, 1.00):
        buckets[f"within_{tol}s"] = (sum(1 for o in offsets if abs(o) <= tol)
                                     if offsets else 0)
    return {
        "n_song_words": n_song, "n_song_pileup_zero_dur": n_pileup,
        "n_take_words": len(take_placed),
        "n_matched": len(pairs), "n_matched_usable_time": len(offsets),
        "n_wrong_repeat_pairs": len(wrong_repeat),
        "wrong_repeat_pairs": wrong_repeat,
        "agreement": round(len(pairs) / n_song, 3) if n_song else 0.0,
        "median_abs_offset": med, "max_abs_offset": mx,
        "mean_offset": mean, "drift_last_minus_first": drift,
        "tolerance_buckets": buckets,
        "missing_song_words": [[w, s, e] for w, s, e in missing],
        "extra_take_words": [[w, s, e] for w, s, e in extra],
        "per_word": [[w, s, t, o] for w, s, t, o in usable_pairs],
    }


def do_takes(take_files, prompted_only=False):
    sw = song_words()
    bounds = scene_bounds()
    results = {}
    for fn in take_files:
        scene = "S" + fn.split("_s")[1].split("_")[0]
        sc_start, sc_end = bounds[scene]
        song_win = [w for w in sw if sc_start <= w[1] < sc_end]
        line = SCENE_LINES.get(scene, "")
        src = os.path.join(TAKES, fn)
        tag = fn.replace(".mp4", "")
        for mode, prompt in ([("unprompted", None)] if not prompted_only else []) + [("prompted", line)]:
            words = transcribe_file(src, f"{tag}_{mode}", prompt)
            placed = place_take_words(scene, words)
            score = align_score(song_win, placed)
            results[f"{fn}:{mode}"] = {
                "scene": scene, "take": fn, "mode": mode,
                "prompt": line if mode == "prompted" else None,
                "take_word_count": len(words),
                "take_words": words,
                "song_window_words": len(song_win),
                "score": score,
            }
            print(f"{fn} [{mode}]: {len(words)} take words, "
                  f"agreement {score['agreement']}, "
                  f"median|off| {score['median_abs_offset']}, "
                  f"max|off| {score['max_abs_offset']}, "
                  f"drift {score['drift_last_minus_first']}", flush=True)
    return results


def do_master(transcribe=True):
    sw = song_words()
    cache = os.path.join(HERE, "master_dictation_prompted.json")
    if transcribe or not os.path.exists(cache):
        # read-only extract of the delivered master's audio; master untouched
        words = transcribe_file(MASTER_16X9, "master16x9_recut",
                                FULL_PERFORMED_LYRICS)
        json.dump({"file": "mv3_i_am_your_dad_16x9_recut.mp4",
                   "md5": MASTER_MD5, "prompt": "full performed lyrics",
                   "words": words}, open(cache, "w"), indent=1)
    else:
        words = json.load(open(cache))["words"]
    # master dictation vs the measured song dictation (SONG_WORDS.json):
    # same audio, so this bounds the method's own instability, not the picture.
    song_toks = [norm(w) for w, _, _ in sw]
    mast_toks = [norm(w) for w, _, _ in words]
    sm = difflib.SequenceMatcher(a=song_toks, b=mast_toks, autojunk=False)
    pairs = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            pairs.extend(zip(range(i1, i2), range(j1, j2)))
    offs = []
    wrong_repeat = 0
    # wrong-repeat test (same rule as align_score): a pair over 2s off is
    # a matcher error only if a nearer occurrence of the same token exists
    # in the song dictation; otherwise it is a real (if large) timing gap.
    song_by_tok = {}
    for _i, (_w, _s, _e) in enumerate(sw):
        song_by_tok.setdefault(norm(_w), []).append((_i, _s))
    matched_song_idx = {si for si, _ in pairs}
    for si, ti in pairs:
        _, ss, se = sw[si]
        _, ts, te = words[ti]
        if se - ss <= 0.0:
            continue
        off = round(ts - ss, 2)
        if abs(off) > 2.0:
            near = [s2 for (i2, s2) in song_by_tok.get(norm(sw[si][0]), [])
                    if i2 not in matched_song_idx and abs(ts - s2) <= 0.5]
            if near:
                wrong_repeat += 1
                continue
        offs.append(off)
    a = sorted(abs(o) for o in offs) if offs else []
    report = {
        "master": "mv3_i_am_your_dad_16x9_recut.mp4", "md5": MASTER_MD5,
        "master_word_count": len(words),
        "song_word_count": len(sw),
        "matched_words": len(pairs),
        "agreement_vs_song_words": round(len(pairs) / len(sw), 3) if sw else 0.0,
        "median_abs_offset_s": a[len(a) // 2] if a else None,
        "max_abs_offset_s": a[-1] if a else None,
        "within_0.25s": sum(1 for o in offs if abs(o) <= 0.25),
        "within_0.50s": sum(1 for o in offs if abs(o) <= 0.50),
        "usable_pairs": len(offs),
        "wrong_repeat_pairs_over_2s": wrong_repeat,
        "note": ("Same audio on both sides (master audio IS the song), so this "
                 "measures dictation stability only. Picture sync is scored by "
                 "the placement cross-check, not by this number."),
    }
    print(json.dumps(report, indent=1), flush=True)
    return report


def do_placement():
    """All-scene placement cross-check from the existing measured take
    dictations (recut_work/measure/*.json) + cutlist placement math.
    No new transcription; re-derives every scene's offsets from disk."""
    sw = song_words()
    bounds = scene_bounds()
    out = {}
    for scene, (fn, flag) in sorted(MOUTH.items()):
        sc_start, sc_end = bounds[scene]
        song_win = [w for w in sw if sc_start <= w[1] < sc_end]
        mp = os.path.join(MEASURE, fn.replace(".mp4", ".json"))
        if not os.path.exists(mp):
            out[scene] = {"error": f"missing {mp}"}
            continue
        d = json.load(open(mp))
        take_words = [[w, s, e] for w, s, e in d["words"]]
        # slice files hold burst-2 words the full-clip decode dropped
        sl = mp.replace(".json", "_slice.json")
        if os.path.exists(sl):
            sd = json.load(open(sl))
            take_words += [[w, s, e] for w, s, e in sd["words"]]
            take_words.sort(key=lambda t: t[1])
        placed = place_take_words(scene, take_words)
        # S25 / S35 are two-take scenes: place each take's words against
        # its own piece only (place_take_words maps one word list across
        # all pieces, which is wrong when pieces are different takes).
        if scene in ("S25", "S35"):
            _, _, pieces = next(x for x in SCENES if x[0] == scene)
            placed = []
            for pi, (pfn, w, s, e) in enumerate(pieces):
                pwords = json.load(open(os.path.join(
                    MEASURE, pfn.replace(".mp4", ".json"))))["words"]
                psl = os.path.join(MEASURE, pfn.replace(".mp4", "_slice.json"))
                if os.path.exists(psl):
                    pwords += json.load(open(psl))["words"]
                placed += _place_piece(scene, [[a, b, c] for a, b, c in pwords], pi)
            placed.sort(key=lambda t: t[1])
        score = align_score(song_win, placed)
        out[scene] = {"take": fn, "flag": flag, "score": score}
        print(f"{scene} {fn} [{flag or 'usable'}]: agreement {score['agreement']}, "
              f"median|off| {score['median_abs_offset']}, max|off| {score['max_abs_offset']}, "
              f"drift {score['drift_last_minus_first']}, "
              f"within0.25s {score['tolerance_buckets']['within_0.25s']}/{score['n_matched_usable_time']}",
              flush=True)
    return out


def picture_motion_spotcheck(n_per_scene=1):
    """Picture-side spot check on the delivered master: at each scene's
    first song-word time, is the picture actually moving (frame differs
    from the frame 0.5s earlier)? A moving picture is necessary, not
    sufficient, for mouth sync -- it rules out frozen coverage, nothing more.
    Uses ffmpeg frame extraction to raw RGB; master is read-only."""
    import io
    sw = song_words()
    bounds = scene_bounds()
    rows = []
    for scene in sorted(MOUTH):
        sc_start, sc_end = bounds[scene]
        win = [w for w in sw if sc_start <= w[1] < sc_end]
        if not win:
            continue
        t = win[0][1]
        diffs = []
        for tt in (t,):
            for dt in (0.0, -0.5):
                ts = max(0.0, tt + dt)
                p = subprocess.run(
                    ["ffmpeg", "-v", "error", "-ss", f"{ts:.2f}", "-i", MASTER_16X9,
                     "-frames:v", "1", "-vf", "scale=160:90",
                     "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
                    capture_output=True, check=True)
                arr = _np.frombuffer(p.stdout, dtype=_np.uint8).astype(_np.float32)
                diffs.append(arr)
        if len(diffs) == 2 and diffs[0].size and diffs[1].size:
            mad = round(float(_np.mean(_np.abs(diffs[0] - diffs[1]))), 2)
        else:
            mad = None
        rows.append({"scene": scene, "word_time": t, "word": win[0][0],
                     "mean_abs_frame_diff_vs_0.5s_earlier": mad,
                     "moving": (mad or 0) > 0.5})
        print(f"{scene} @{t}s '{win[0][0]}': frame diff {mad} "
              f"({'moving' if (mad or 0) > 0.5 else 'STILL?'})", flush=True)
    return rows


if __name__ == "__main__":
    os.makedirs(TMP, exist_ok=True)
    mode = sys.argv[1] if len(sys.argv) > 1 else "takes"
    if mode == "takes":
        files = sys.argv[2:] or ["mv3_s01_t2.mp4", "mv3_s06_t1.mp4", "mv3_s27_t1.mp4"]
        res = do_takes(files)
        json.dump(res, open(os.path.join(HERE, "take_crosscheck.json"), "w"), indent=1)
    elif mode == "master":
        skip = "--skip-transcribe" in sys.argv
        rep = do_master(transcribe=not skip)
        json.dump(rep, open(os.path.join(HERE, "master_dictation_report.json"), "w"), indent=1)
    elif mode == "placement":
        res = do_placement()
        json.dump(res, open(os.path.join(HERE, "placement_crosscheck.json"), "w"), indent=1)
    elif mode == "motion":
        rows = picture_motion_spotcheck()
        json.dump(rows, open(os.path.join(HERE, "master_motion_spotcheck.json"), "w"), indent=1)
    else:
        print("usage: takes|master|placement|motion", file=sys.stderr)
        sys.exit(2)
