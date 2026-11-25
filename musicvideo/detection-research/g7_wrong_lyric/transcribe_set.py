#!/usr/bin/env python3
"""Transcribe every fixture item once, checkpointed per take.

For each item in fixture.json: extract 16k mono wav (ffmpeg) into work/wav/
if missing, transcribe with the house config (g7_check.transcribe) into
work/asr/<id>.json if missing. One model load, sequential — the blade runs
ONE heavy job at a time. Safe to re-run after a reboot: completed takes
are skipped, so at most one take's work is lost.
"""
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import g7_check  # noqa: E402

WAV = os.path.join(HERE, "work", "wav")
ASR = os.path.join(HERE, "work", "asr")
os.makedirs(WAV, exist_ok=True)
os.makedirs(ASR, exist_ok=True)


def main():
    fixture = json.load(open(os.path.join(HERE, "fixture.json")))
    items = fixture["items"]
    for i, it in enumerate(items, 1):
        out = os.path.join(ASR, it["id"] + ".json")
        if os.path.exists(out):
            print(f"[{i}/{len(items)}] {it['id']} cached", flush=True)
            continue
        wav = os.path.join(WAV, it["id"] + ".wav")
        if not os.path.exists(wav):
            subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", it["file"],
                            "-vn", "-ac", "1", "-ar", "16000", wav], check=True)
        t0 = time.time()
        segments = g7_check.transcribe(wav)
        json.dump({"file": it["file"], "segments": segments},
                  open(out, "w"), indent=1)
        text = " ".join(s["text"] for s in segments).strip()
        print(f"[{i}/{len(items)}] {it['id']} {time.time()-t0:.1f}s "
              f"asr={text!r}", flush=True)
    print("ALL DONE", flush=True)


if __name__ == "__main__":
    main()
