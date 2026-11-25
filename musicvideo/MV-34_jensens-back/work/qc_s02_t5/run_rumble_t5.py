#!/usr/bin/env python3
"""MV-34 Checkpoint B: Reson8 Rumble-2-Flash adjudication (no timestamps —
word-exact verification only). Pattern copied from the 2026-11-19 eval
(rumble_test.py): AutoModelForMultimodalLM + apply_transcription_request,
language forced English, factory defaults."""
import json, time
import torch
from transformers import AutoProcessor, AutoModelForMultimodalLM

MODEL_ID = "Reson8/Rumble-2-Flash"
WAV = "/home/hatch/workspace/wubutv-network/musicvideo/MV-34_jensens-back/work/qc_s02_t5/audio.wav"
OUT = "/home/hatch/workspace/wubutv-network/musicvideo/MV-34_jensens-back/work/qc_s02_t5/asr_rumble.json"

processor = AutoProcessor.from_pretrained(MODEL_ID)
model = AutoModelForMultimodalLM.from_pretrained(MODEL_ID, device_map="cpu")
inputs = processor.apply_transcription_request(audio=WAV, language="English")
inputs = inputs.to(model.device, dtype=model.dtype)
t0 = time.time()
with torch.no_grad():
    output = model.generate(**inputs, max_new_tokens=1024)
wall = round(time.time() - t0, 2)
gen = output[:, inputs["input_ids"].shape[-1]:]
try:
    text = processor.decode(gen, return_format="transcription_only")
except TypeError:
    text = processor.decode(gen)
if not isinstance(text, str):
    text = str(text)
rec = {"model": MODEL_ID, "wall_s": wall, "text": text}
with open(OUT, "w") as f:
    json.dump(rec, f, indent=1)
print("WALL", wall)
print(text)
print("WROTE", OUT)
