#!/usr/bin/env python3
"""PILOT-1 finisher: dialogue gate — transcribe the six SHIPPED segments
(work/segments/seg_U*.mp4, the exact audio in joined.mp4/master) with the
house G7 config (faster-whisper large-v3-turbo int8, NO VAD) and dump
per-unit JSON + a plain-text summary for GATE_LOG."""
import json
import os
import sys

G7 = os.path.expanduser(
    "~/workspace/wubutv-network/musicvideo/detection-research/g7_wrong_lyric")
sys.path.insert(0, G7)
import g7_check  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.dirname(os.path.dirname(HERE))

EXPECTED = {
    "U1": "The mouth moved, UNC. Nothing came out.",
    "U2": "Cut to the mouth, Laura. Mouth is the record.",
    "U3": "It sang a word that isn't written, UNC.",
    "U4": "File it under the singer. Singer's the record.",
    "U5": "It fixed a take we haven't broken yet.",
    "U6": "It knows our names now. Cut it anyway.",
}

results = {}
for unit in ("U1", "U2", "U3", "U4", "U5", "U6"):
    seg = os.path.join(PROJ, "work", "segments", f"seg_{unit}.mp4")
    segs = g7_check.transcribe(seg)
    text = " ".join(s["text"] for s in segs).strip()
    results[unit] = {"expected": EXPECTED[unit], "asr": text, "segments": segs}
    print(f"{unit} expected={EXPECTED[unit]!r}", flush=True)
    print(f"{unit} asr     ={text!r}", flush=True)

out = os.path.join(HERE, "dialogue_gate_asr.json")
json.dump(results, open(out, "w"), indent=1)
print("WROTE", out, flush=True)
print("ALL DONE", flush=True)
