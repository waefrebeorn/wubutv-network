#!/usr/bin/env python3
"""Pilot-3 dialogue gate: transcribe takes with the house G7 config."""
import json
import os
import sys

G7 = os.path.expanduser(
    "~/workspace/wubutv-network/musicvideo/detection-research/g7_wrong_lyric")
sys.path.insert(0, G7)
import g7_check  # noqa: E402

for path in sys.argv[1:]:
    segs = g7_check.transcribe(path)
    text = " ".join(s["text"] for s in segs).strip()
    print(f"== {os.path.basename(path)}")
    print(json.dumps(segs, indent=1))
    print(f"FULL: {text!r}")
    sys.stdout.flush()
print("ASR DONE")
