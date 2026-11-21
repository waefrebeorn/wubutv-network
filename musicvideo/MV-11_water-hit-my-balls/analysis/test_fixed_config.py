#!/usr/bin/env python3
"""MV-11 lyrics test #1: fixed faster-whisper config, 3-model A/B.
Baseline: SONG_WORDS.json (small, int8, defaults, no VAD, 92 words, blank after 102s).
Config = research report §4 snippet MINUS the VAD: pinned language,
condition_on_previous_text=False, greedy beam 1, temperature ladder kept,
repetition_penalty 1.1, no_repeat_ngram_size 3, post-filter collapsing
degenerate repeat runs. VAD WAS TESTED FIRST and killed the run:
test1_small.json (vad_filter=True, 500ms/0.5) returned 3 words total,
0 in 102-172s, wall 7s — generic speech VAD gates out held-vowel chant
singing entirely (the Cukier bench warning, reproduced). VAD is OUT.
Writes per-model JSON + test1_summary.md. Resumable: skips models whose
JSON already exists (VM reboots ~2h).
"""
import json, os, time
import numpy as np
from scipy.io import wavfile

PROJ = "/home/hatch/workspace/wubutv-network/musicvideo/MV-11_water-hit-my-balls"
OUT = os.path.join(PROJ, "analysis", "tests")
os.makedirs(OUT, exist_ok=True)
sr, data = wavfile.read(f"{PROJ}/analysis/track_16k.wav")
y = data.astype(np.float32) / 32768.0

from faster_whisper import WhisperModel

MODELS = ["small", "large-v3-turbo", "distil-large-v3"]
results = {}
for name in MODELS:
    outp = os.path.join(OUT, f"test1_novad_{name}.json")
    if os.path.exists(outp):
        print(f"SKIP {name} (already done)", flush=True)
        results[name] = json.load(open(outp))
        continue
    t0 = time.time()
    model = WhisperModel(name, device="cpu", compute_type="int8", cpu_threads=2)
    segments, info = model.transcribe(
        y, language="en", word_timestamps=True,
        condition_on_previous_text=False, beam_size=1,
        temperature=(0.0, 0.2, 0.4, 0.6, 0.8, 1.0),
        compression_ratio_threshold=2.4, log_prob_threshold=-1.0, no_speech_threshold=0.6,
        repetition_penalty=1.1, no_repeat_ngram_size=3,
    )
    words = []
    text = []
    for s in segments:
        text.append(s.text)
        for w in (s.words or []):
            words.append({"word": w.word.strip(), "start": round(w.start, 3),
                          "end": round(w.end, 3), "prob": round(w.probability, 3)})
    # post-filter: collapse runs of the same word >=6 (degenerate loop guard)
    filtered = []
    run = 0
    prev = None
    for w in words:
        k = w["word"].lower().strip(",.")
        run = run + 1 if k == prev else 1
        prev = k
        if run <= 5:
            filtered.append(w)
    wall = time.time() - t0

    def span(a, b):
        return [w for w in filtered if a <= w["start"] < b]

    max_run = 0
    cur = 0
    prevw = None
    for w in filtered:
        k = w["word"].lower().strip(",.")
        cur = cur + 1 if k == prevw else 1
        prevw = k
        max_run = max(max_run, cur)
    long_words = [w for w in filtered if w["end"] - w["start"] > 2.0]
    rec = {"model": name, "wall_s": round(wall, 1), "words_total": len(filtered),
           "words_102_172": len(span(102, 172.42)), "words_110_155": len(span(110, 155)),
           "max_same_word_run": max_run, "words_over_2s": len(long_words),
           "words": filtered, "text": " ".join(text)}
    json.dump(rec, open(outp, "w"), indent=1)
    results[name] = rec
    print(f"{name}: {len(filtered)} words, 102-172s: {len(span(102, 172.42))}, "
          f"110-155s: {len(span(110, 155))}, max_run={max_run}, >2s={len(long_words)}, "
          f"wall={wall:.0f}s", flush=True)
    del model

base = json.load(open(f"{PROJ}/analysis/SONG_WORDS.json"))
bw = base["words"]


def bspan(a, b):
    return [w for w in bw if a <= w["start"] < b]


lines = ["# MV-11 lyrics test #1 — fixed faster-whisper config, NO VAD (vs baseline small/defaults/no-VAD)",
         "",
         f"Baseline (SONG_WORDS.json): {len(bw)} words, 102–172s: {len(bspan(102, 172.42))}, 110–155s: {len(bspan(110, 155))}",
         "VAD RUN (test1_small.json, vad_filter=True 500ms/0.5): 3 words total, 0 in 102–172s — VAD gates out held-vowel chant singing entirely; VAD is OUT.",
         "",
         "| model | words | 102–172s | 110–155s | max same-word run | words >2s | wall |",
         "|---|---|---|---|---|---|---|"]
for name in MODELS:
    r = results[name]
    lines.append(f"| {name} | {r['words_total']} | {r['words_102_172']} | {r['words_110_155']} | {r['max_same_word_run']} | {r['words_over_2s']} | {r['wall_s']}s |")
open(os.path.join(OUT, "test1_summary.md"), "w").write("\n".join(lines) + "\n")
print("WROTE test1_summary.md", flush=True)
