#!/usr/bin/env python3
"""ORT reference activations for chunk 0, saved as strided samples (stride 32)
+ full stats. Fixes the output-order bug: outs[0] is the original model output.
Writes ref_chunk0.npz (small: ~100 MB)."""
import json, numpy as np, onnx
from onnx import shape_inference

MODEL = '/home/hatch/workspace/wubuwizard-cpu-sep/UVR-MDX-NET-Voc_FT.onnx'
OUT = '/home/hatch/workspace/wubutv-network/musicvideo/detection-research/c11_sep'
CKPTS = [0, 3, 9, 12, 15, 30, 45, 60, 75, 90, 107, 124, 141, 158, 175, 177]
STRIDE = 32

m = onnx.load(MODEL)
inf = shape_inference.infer_shapes(m)
vi = {v.name: v for v in inf.graph.value_info}
m2 = onnx.ModelProto(); m2.CopyFrom(m)
for c in CKPTS:
    out_name = m.graph.node[c].output[0]
    if out_name in vi:
        m2.graph.output.append(vi[out_name])

import sys
sys.path.insert(0, '/home/hatch/workspace/wubuwizard-cpu-sep')
from mdx_onnx_cpu import stft_complex, CHUNK_SIZE, TRIM
import onnxruntime as ort
from scipy.io import wavfile
sr, data = wavfile.read('/home/hatch/workspace/wubuwizard-cpu-sep/mv14_44k.wav')
mix = data.astype(np.float32)
if data.dtype == np.int16: mix = mix / 32768.0
mix = mix.T
peak = np.abs(mix).max(); mix_n = mix / peak
mixture = np.concatenate((np.zeros((2, TRIM), dtype=np.float32), mix_n), axis=1)
part = mixture[:, :CHUNK_SIZE]
spek = stft_complex(part)[None, :, :, :]
spek[:, :, :3, :] = 0

so = ort.SessionOptions(); so.intra_op_num_threads = 2; so.inter_op_num_threads = 1
sess = ort.InferenceSession(m2.SerializeToString(), providers=["CPUExecutionProvider"], sess_options=so)
outs = sess.run(None, {"input": spek})
# outs[0] = original graph output (node 177); outs[1:] = checkpoints in CKPTS order
save = {"input_spek": spek, "final_output": outs[0]}
for c, o in zip(CKPTS, outs[1:]):
    flat = o.ravel()
    save[f"node{c:03d}_{m.graph.node[c].op_type}_sample"] = flat[::STRIDE].copy()
    save[f"node{c:03d}_{m.graph.node[c].op_type}_stats"] = np.array(
        [o.mean(), o.std(), o.min(), o.max(), flat.size], dtype=np.float64)
    print(f"node {c} {m.graph.node[c].op_type}: {o.shape} mean {o.mean():.5f} std {o.std():.4f} range [{o.min():.3f},{o.max():.3f}] sample_n {flat[::STRIDE].size}")
print("final output:", outs[0].shape, "range", float(outs[0].min()), float(outs[0].max()))
np.savez(f'{OUT}/ref_chunk0.npz', **save)
print("saved ref_chunk0.npz")
