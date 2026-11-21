#!/usr/bin/env python3
"""G7 WRONG-LYRIC GATE — Slopcannon QC gate (loop 7 build, from loop 3 §2 #5 /
loop 4 §2 #4 / loop 5 §3 #3 / loop 6 §3 #2, unchanged spec).

WHAT IT CHECKS
    Whether a generated take sings the words its scene was planned for.
    QC already gates identity (G1), burned-in text (G2), motion and sync —
    but until G7 nothing read *what* the take sings. A take that sings a
    different segment of the song (or invented words) passed every gate.

METRIC (pre-stated in the loops; not tuned here)
    overlap = |ASR words ∩ planned words| / |planned words|   (word SETS)
    overlap < 0.5  ->  REJECT
    Planned words = the scene's planned lyric words (the scene plan's lyric
    fragment for the slot; the song word grid is the timing source).
    Wordless slot (planned set empty): overlap = 1.0 if the take's ASR word
    set is also empty, else 0.0 — singing words into a wordless slot is the
    same wrong-content failure in the other direction.

ASR WORD SET — what counts as "sung"
    Transcription is the house lyrics pipeline (proven config, copied from
    MV-14's work/mv14_take_asr.py): faster-whisper large-v3-turbo, int8,
    cpu_threads=2, NO VAD (VAD is fatal on chant singing), beam 1,
    condition_on_previous_text=False, repetition_penalty 1.1,
    no_repeat_ngram_size 3, compression_ratio_threshold 2.4,
    log_prob_threshold -1.0, no_speech_threshold 0.6, word timestamps on,
    numpy-array input, pinned "en".

    Whisper hallucinates words on musical/wordless audio (every MV-14
    wordless take produced junk: "so", "What's up?", "I don't know", ".").
    The project's own QC adjudicated sung-vs-hallucination on two numbers
    whisper itself reports: segment avg_logprob and per-word probability
    (real sung lines: avg_logprob -0.18..-0.69, word probs >= ~0.59;
    hallucinations: avg_logprob <= -1.08 or word probs <= ~0.26).
    A word therefore counts as SUNG iff:
        its segment avg_logprob >= -1.0   (the decoder's own house
                                            log_prob_threshold constant)
        AND its word probability >= 0.5   (the probability midpoint)
    The gate also reports the RAW set (every returned word) so the screen
    is never load-bearing in secret: validation reports both.

VERDICT / OVERRIDE (per the loop spec)
    overlap < 0.5 -> REJECT, with a hand-check override for homophones
    (ASR "told" for sung "toll" is a known mishear class) and
    near-identical choruses. Identical chorus lines repeated across the
    song are provenance-quarantined in the cross-pairing fixture: a take
    must not false-REJECT for singing the same line another scene owns.

USAGE
    python3 g7_check.py --audio take.wav --planned "clip it post it"
    python3 g7_check.py --audio take.mp4 --planned-file planned.json --scene S15
    python3 g7_check.py --audio take.wav --grid SONG_WORDS.json --window 36.56 37.86
    (--audio .mp4 is decoded to 16k mono wav via ffmpeg; --asr-json PATH
     caches/loads a transcription instead of re-running the model.)
"""
import argparse
import json
import re
import subprocess
import sys
import tempfile
import wave

import numpy as np

# --- gate constants (pre-stated; do not tune to a fixture) -------------------
GATE_THRESHOLD = 0.5          # overlap < 0.5 -> REJECT (loop 3-6 spec)
SCREEN_MIN_SEG_LOGPROB = -1.0  # == house decoder log_prob_threshold
SCREEN_MIN_WORD_PROB = 0.5    # probability midpoint

_MODEL = None


def normalize(word):
    """One token: lowercase, letters/digits only (apostrophes dropped, so
    don't == dont on both sides of the comparison). '' if nothing remains
    (punctuation-only ASR tokens like '.' are not words)."""
    return re.sub(r"[^a-z0-9]", "", word.lower())


def word_sets(segments):
    """(screened, raw) word sets from faster-whisper segments.

    segments: iterable of dicts with 'avg_logprob' and 'words'
    (each word: {'word': str, 'probability': float}) — the schema
    mv14_take_asr.py writes and transcribe() below returns.
    """
    screened, raw = set(), set()
    for seg in segments:
        seg_ok = seg.get("avg_logprob", 0.0) >= SCREEN_MIN_SEG_LOGPROB
        for w in seg.get("words") or []:
            tok = normalize(w["word"])
            if not tok:
                continue
            raw.add(tok)
            if seg_ok and w.get("probability", 0.0) >= SCREEN_MIN_WORD_PROB:
                screened.add(tok)
    return screened, raw


def overlap(asr_words, planned_words):
    """Word-set overlap (recall of the planned words in the take's ASR).
    Empty planned set (wordless slot): 1.0 iff the ASR set is empty too."""
    planned = set(planned_words)
    if not planned:
        return 1.0 if not asr_words else 0.0
    return len(set(asr_words) & planned) / len(planned)


def verdict(ov):
    return "PASS" if ov >= GATE_THRESHOLD else "REJECT"


# --- transcription (house pipeline) ------------------------------------------
def _model():
    global _MODEL
    if _MODEL is None:
        from faster_whisper import WhisperModel
        _MODEL = WhisperModel("large-v3-turbo", device="cpu",
                              compute_type="int8", cpu_threads=2)
    return _MODEL


def load_wav(path):
    with wave.open(path, "rb") as w:
        n, sr, ch = w.getnframes(), w.getframerate(), w.getnchannels()
        raw = w.readframes(n)
    audio = np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0
    if ch > 1:
        audio = audio.reshape(-1, ch).mean(axis=1)
    assert sr == 16000, f"{path}: sample rate {sr}, expected 16000"
    return audio


def to_wav16k(path):
    """Return a 16k mono wav path for any media file (ffmpeg decode)."""
    if path.endswith(".wav"):
        return path, None
    tmp = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    tmp.close()
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", path,
                    "-vn", "-ac", "1", "-ar", "16000", tmp.name], check=True)
    return tmp.name, tmp.name


def transcribe(path):
    """House-config transcription. Returns segment dicts in the
    mv14_take_asr.py schema (word entries use 'probability')."""
    wav, _tmp = to_wav16k(path)
    audio = load_wav(wav)
    segments, _info = _model().transcribe(
        audio,
        language="en",
        beam_size=1,
        vad_filter=False,
        condition_on_previous_text=False,
        word_timestamps=True,
        compression_ratio_threshold=2.4,
        log_prob_threshold=-1.0,
        no_speech_threshold=0.6,
        repetition_penalty=1.1,
        no_repeat_ngram_size=3,
    )
    out = []
    for seg in segments:
        words = [{"word": w.word, "start": round(w.start, 2),
                  "end": round(w.end, 2),
                  "probability": round(w.probability, 3)}
                 for w in (seg.words or [])]
        out.append({"start": round(seg.start, 2), "end": round(seg.end, 2),
                    "text": seg.text.strip(),
                    "avg_logprob": round(seg.avg_logprob, 3),
                    "no_speech_prob": round(seg.no_speech_prob, 3),
                    "words": words})
    return out


def planned_from_grid(grid_path, w0, w1):
    """Planned words = song-grid words whose start falls in [w0, w1).
    Accepts the SONG_WORDS.json shape ({'words': [{word,start,...}]}) and
    the MV-2 SONG_WORDS_BASE.json shape ([{word,t0,t1}])."""
    data = json.load(open(grid_path))
    words = data["words"] if isinstance(data, dict) else data
    out = []
    for w in words:
        start = w.get("start", w.get("t0"))
        if start is not None and w0 <= start < w1:
            tok = normalize(w["word"])
            if tok:
                out.append(tok)
    return out


def check(audio_path, planned_words, segments=None):
    """Full gate check. Returns a JSON-able result dict."""
    if segments is None:
        segments = transcribe(audio_path)
    screened, raw = word_sets(segments)
    planned = {normalize(w) for w in planned_words}
    planned.discard("")
    ov_s, ov_r = overlap(screened, planned), overlap(raw, planned)
    return {
        "audio": audio_path,
        "asr_text": " ".join(s["text"] for s in segments).strip(),
        "asr_words_screened": sorted(screened),
        "asr_words_raw": sorted(raw),
        "planned_words": sorted(planned),
        "overlap_screened": round(ov_s, 4),
        "overlap_raw": round(ov_r, 4),
        "verdict": verdict(ov_s),
        "verdict_raw": verdict(ov_r),
        "threshold": GATE_THRESHOLD,
    }


def main():
    ap = argparse.ArgumentParser(description="G7 wrong-lyric gate")
    ap.add_argument("--audio", required=True)
    ap.add_argument("--planned", help="planned words, space-separated")
    ap.add_argument("--planned-file", help="JSON {scene: [words]} or [words]")
    ap.add_argument("--scene", help="scene key for --planned-file")
    ap.add_argument("--grid", help="song word-grid JSON (with --window)")
    ap.add_argument("--window", nargs=2, type=float, metavar=("A", "B"))
    ap.add_argument("--asr-json", help="load/save transcription cache")
    args = ap.parse_args()

    if args.planned:
        planned = args.planned.split()
    elif args.planned_file:
        data = json.load(open(args.planned_file))
        planned = data[args.scene] if args.scene else data
    elif args.grid and args.window:
        planned = planned_from_grid(args.grid, *args.window)
    else:
        ap.error("one of --planned / --planned-file / --grid+--window is required")

    segments = None
    if args.asr_json:
        try:
            segments = json.load(open(args.asr_json))["segments"]
        except (FileNotFoundError, KeyError):
            segments = transcribe(args.audio)
            json.dump({"file": args.audio, "segments": segments},
                      open(args.asr_json, "w"), indent=1)
    result = check(args.audio, planned, segments)
    print(json.dumps(result, indent=1))
    return 0 if result["verdict"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
