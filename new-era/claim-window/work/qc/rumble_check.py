#!/usr/bin/env python3
"""Rumble-2-Flash checkpoint-B transcription for one media file.
Usage: rumble_check.py <media_file>  -> prints transcript text.
Pattern proven in research_notes/rumble2-flash-eval-20261119/rumble_test.py:
wav extracted by ffmpeg, apply_transcription_request, no trust_remote_code.
Run with the eval venv python:
  ~/workspace/research_notes/rumble2-flash-eval-20261119/venv/bin/python rumble_check.py <file>
"""
import subprocess
import sys

import torch
from transformers import AutoModelForMultimodalLM, AutoProcessor

MODEL_ID = "Reson8/Rumble-2-Flash"


def main():
    src = sys.argv[1]
    wav = "/tmp/rumble_check_work.wav"
    subprocess.run(
        ["ffmpeg", "-v", "error", "-y", "-i", src, "-vn", "-ac", "1",
         "-ar", "16000", "-f", "wav", wav],
        check=True)
    processor = AutoProcessor.from_pretrained(MODEL_ID)
    model = AutoModelForMultimodalLM.from_pretrained(MODEL_ID)
    inputs = processor.apply_transcription_request(audio=wav)
    inputs = inputs.to(model.device, dtype=model.dtype)
    with torch.no_grad():
        output = model.generate(**inputs, max_new_tokens=512)
    gen = output[:, inputs["input_ids"].shape[-1]:]
    try:
        text = processor.decode(gen, return_format="transcription_only")
    except TypeError:
        text = processor.decode(gen)
    print(text)


if __name__ == "__main__":
    main()
