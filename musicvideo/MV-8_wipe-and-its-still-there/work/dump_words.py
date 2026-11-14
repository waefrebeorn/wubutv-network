#!/usr/bin/env python3
"""Dump SONG_WORDS.json segments + words readably for timeline building."""
import json, sys
d = json.load(open(sys.argv[1] if len(sys.argv) > 1 else "SONG_WORDS.json"))
print(f"model={d['model']} words={d['n_words']} segments={len(d['segments'])}")
for s in d["segments"]:
    print(f'SEG {s["start"]:8.3f} -> {s["end"]:8.3f}   {s["text"]}')
print("--- words ---")
for w in d["words"]:
    print(f'{w["start"]:8.3f} {w["end"]:8.3f} p={w["prob"]:.2f} {w["word"]}')
