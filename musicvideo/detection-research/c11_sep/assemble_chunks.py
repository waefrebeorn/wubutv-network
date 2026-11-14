#!/usr/bin/env python3
"""Assemble per-chunk ISTFT dumps (sep_main --dump-dir) into the final stems.

Replicates mdx_onnx_cpu.py's demix() OLA exactly, but reads the precomputed
per-chunk tar (raw ISTFT output) from <dump_dir>/chunk_%03d.bin instead of
running the model: for each chunk, tar *= np.hanning(actual), accumulate
into result/divider at [start:start+actual], then vocals = result /
max(divider, 1e-8), trim TRIM, truncate to the mix length, rescale by the
mix peak; instrumental = mix - vocals*1.01. Writes c11_vocals.wav +
c11_inst.wav (int16, clip to [-1, 1] * 32767, matching the Python recipe).

Usage: assemble_chunks.py --input <mv14_44k.wav> --dump-dir <dir>
         --out-vocals c11_vocals.wav [--out-inst c11_inst.wav]
"""
import argparse
import struct
from pathlib import Path

import numpy as np
from scipy.io import wavfile

N_FFT = 6144
HOP = 1024
CHUNK_SIZE = 261120
TRIM = 3072
GEN_SIZE = 254976
OVERLAP = 0.25
COMPENSATE = 1.01


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--dump-dir", required=True)
    ap.add_argument("--out-vocals", default="c11_vocals.wav")
    ap.add_argument("--out-inst", default="c11_inst.wav")
    args = ap.parse_args()

    sr, data = wavfile.read(args.input)
    assert sr == 44100, f"expected 44100 Hz, got {sr}"
    mix = data.astype(np.float32)
    if data.dtype == np.int16:
        mix = mix / 32768.0
    mix = mix.T  # [2, T]
    T = mix.shape[1]
    peak = float(np.abs(mix).max())
    print(f"mix: {T / sr:.2f}s, peak {peak:.4f}")

    pad = GEN_SIZE + TRIM - (T % GEN_SIZE)
    Tmix = TRIM + T + pad
    step = int((1 - OVERLAP) * CHUNK_SIZE)
    n_chunks = (Tmix + step - 1) // step
    print(f"mixture {Tmix} samples, step {step}, chunks {n_chunks}")

    result = np.zeros((2, Tmix), dtype=np.float64)
    divider = np.zeros((2, Tmix), dtype=np.float64)
    dump_dir = Path(args.dump_dir)
    found = 0
    for ci in range(n_chunks):
        p = dump_dir / f"chunk_{ci:03d}.bin"
        if not p.exists():
            print(f"  MISSING chunk {ci} ({p})")
            continue
        raw = p.read_bytes()
        start, actual = struct.unpack_from("<2i", raw, 0)
        body = np.frombuffer(raw, dtype=np.float32, offset=8)
        assert len(body) == 2 * actual, f"chunk {ci}: {len(body)} != 2*{actual}"
        tarL = body[:actual].astype(np.float64)
        tarR = body[actual:].astype(np.float64)
        win = np.hanning(actual).astype(np.float64)
        result[0, start:start + actual] += tarL * win
        result[1, start:start + actual] += tarR * win
        divider[0, start:start + actual] += win
        divider[1, start:start + actual] += win
        found += 1
    print(f"assembled {found}/{n_chunks} chunks")
    if found != n_chunks:
        print("WARNING: incomplete — output will be wrong outside dumped chunks")

    voc = result / np.maximum(divider, 1e-8)
    voc = voc[:, TRIM:TRIM + T] * peak  # [2, T]
    wavfile.write(args.out_vocals, sr,
                  (np.clip(voc.T, -1, 1) * 32767).astype(np.int16))
    print("wrote", args.out_vocals)
    inst = mix - voc * COMPENSATE
    wavfile.write(args.out_inst, sr,
                  (np.clip(inst.T, -1, 1) * 32767).astype(np.int16))
    print("wrote", args.out_inst)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
