#!/usr/bin/env python3
"""Merge the three Whisper passes into SONG_WORDS.json (v2).

Group-level normalization: several mishears are whole-phrase garbles, so
they are collapsed as groups, not single words:
- ["Future","rather","Spanish"] -> "Futurama's finished" (one occurrence)
- ["You","turn","around","the","spinach"] -> "Futurama's finished"
- ["all","three"] -> "'03,"
- ["Who","knew","it"] -> ["Hulu","hit"]  ("it" dropped)
- ["what's","the","memory"] -> ["muscle","memory"]
- "Or" -> "For" before "real this time" in Chorus 2
- "gut" -> "dark", "home" -> "on", "Cut" -> "Good", "Max" -> "Matt",
  "sky" -> "style.", "bring" -> "binge", "Code" -> "Quote",
  "critics" -> "credits"
"""
import json


def load_words(path):
    return json.load(open(path))["words"]


w1 = load_words("work/song_transcript_0_65_noprompt.json")
w2 = [w for w in load_words("work/song_transcript.json") if 63.0 <= w["start"] < 155.0]
w3 = load_words("work/song_transcript_155_end_noprompt.json")
raw = sorted(w1 + w2 + w3, key=lambda w: w["start"])

OUT = []
i = 0
n = len(raw)


def emit(word, s, e, prob, note=None):
    d = {"word": word, "start": round(s, 2), "end": round(e, 2), "prob": round(prob, 3)}
    if note:
        d["note"] = note
    OUT.append(d)


while i < n:
    w = raw[i]
    txt = w["word"].strip(",.").lower()
    # group: Future rather Spanish -> Futurama's finished
    if (i + 2 < n and raw[i]["word"].strip(",.").lower() == "future"
            and raw[i + 1]["word"].strip(",.").lower() == "rather"
            and raw[i + 2]["word"].strip(",.").lower() == "spanish"):
        emit("Futurama's", raw[i]["start"], raw[i + 1]["end"], raw[i]["prob"],
             "normalized mishear")
        emit("finished", raw[i + 2]["start"], raw[i + 2]["end"], raw[i + 2]["prob"],
             "normalized mishear")
        i += 3
        continue
    # group: You turn around the spinach -> Futurama's finished
    if (i + 4 < n and raw[i]["word"].strip(",.").lower() == "you"
            and raw[i + 1]["word"].strip(",.").lower() == "turn"
            and raw[i + 2]["word"].strip(",.").lower() == "around"
            and raw[i + 3]["word"].strip(",.").lower() == "the"
            and raw[i + 4]["word"].strip(",.").lower() == "spinach"):
        emit("Futurama's", raw[i]["start"], raw[i + 2]["end"], raw[i]["prob"],
             "normalized mishear")
        emit("finished", raw[i + 3]["start"], raw[i + 4]["end"], raw[i + 4]["prob"],
             "normalized mishear")
        i += 5
        continue
    # group: all three -> '03,
    if (i + 1 < n and raw[i]["word"].lower() == "all"
            and raw[i + 1]["word"].lower() == "three"):
        emit("'03,", raw[i]["start"], raw[i + 1]["end"], raw[i + 1]["prob"],
             "normalized mishear")
        i += 2
        continue
    # group: Who knew it -> Hulu hit
    if (i + 2 < n and raw[i]["word"].lower() == "who"
            and raw[i + 1]["word"].lower() == "knew"
            and raw[i + 2]["word"].lower() == "it"):
        emit("Hulu", raw[i]["start"], raw[i]["end"], raw[i]["prob"],
             "normalized mishear")
        emit("hit", raw[i + 1]["start"], raw[i + 1]["end"], raw[i + 1]["prob"],
             "normalized mishear")
        i += 3
        continue
    # group: what's the memory -> muscle memory
    if (i + 2 < n and raw[i]["word"].lower() == "what's"
            and raw[i + 1]["word"].lower() == "the"
            and raw[i + 2]["word"].lower() == "memory"):
        emit("muscle", raw[i]["start"], raw[i + 1]["end"], raw[i]["prob"],
             "normalized mishear")
        emit("memory", raw[i + 2]["start"], raw[i + 2]["end"], raw[i + 2]["prob"],
             "normalized mishear")
        i += 3
        continue
    # single-word fixes
    single = {
        "max": "Matt", "sky": "style.", "cut": "Good", "or": "For",
        "gut": "dark", "home": "on", "home,": "on", "bring": "binge",
        "code": "Quote", "critics": "credits",
    }
    low = w["word"].lower()
    if low in single:
        emit(single[low], w["start"], w["end"], w["prob"], "normalized mishear")
        i += 1
        continue
    emit(w["word"], w["start"], w["end"], w["prob"])
    i += 1

# dedupe exact overlaps at the seams
seen = []
for w in OUT:
    if seen and abs(w["start"] - seen[-1]["start"]) < 0.05 and w["word"] == seen[-1]["word"]:
        continue
    seen.append(w)

doc = {
    "track": "track.mp3",
    "track_md5": "d46af0ef2e5abfca97db16905d20fb7d",
    "duration": 238.8,
    "method": "faster-whisper base, word timestamps, mono 16k numpy input; "
              "0-65s and 155-238.8s re-decoded WITHOUT initial_prompt (the "
              "prompted full-track pass hallucinated chorus repeats over "
              "Verse 1); 63-159s from the prompted pass; cross-checked "
              "against the Suno lyric video frames (track.mp4) for line "
              "identity and boundaries; mishears normalized to performed "
              "words per sheet + video (see merge_words.py for the classes)",
    "words": seen,
}
with open("SONG_WORDS.json", "w") as f:
    json.dump(doc, f, indent=1)
print(f"wrote SONG_WORDS.json: {len(seen)} words, "
      f"{seen[0]['start']}s - {seen[-1]['end']}s")
