#!/usr/bin/env python3
"""One-shot extractor: ONNX -> flat fp32 weights + ORT reference activations for chunk 0.
Writes: weights.bin (fp32 LE, concatenated initializers), weights_index.json
(name -> {offset_elems, shape, dtype}), ref_chunk0.npz (input spek + checkpoint node outputs).
"""
import json, numpy as np, onnx
from onnx import numpy_helper, shape_inference

MODEL = '/home/hatch/workspace/wubuwizard-cpu-sep/UVR-MDX-NET-Voc_FT.onnx'
OUT = '/home/hatch/workspace/wubutv-network/musicvideo/detection-research/c11_sep'
CKPTS = [0, 3, 9, 12, 15, 30, 45, 60, 75, 90, 107, 124, 141, 158, 175, 177]

m = onnx.load(MODEL)
# --- weights ---
index, buf = {}, []
off = 0
for init in m.graph.initializer:
    a = numpy_helper.to_array(init).astype(np.float32)
    index[init.name] = {"offset": off, "shape": list(a.shape), "dtype": "float32"}
    buf.append(a.ravel()); off += a.size
w = np.concatenate(buf)
w.tofile(f'{OUT}/weights.bin')
json.dump(index, open(f'{OUT}/weights_index.json', 'w'), indent=1)
print("weights:", w.size, "elems,", w.nbytes/1e6, "MB;", len(index), "tensors")
# sanity: model file sha
import hashlib
print("onnx sha256:", hashlib.sha256(open(MODEL,'rb').read()).hexdigest()[:16])

# --- ORT reference: chunk 0, augmented model with checkpoint outputs ---
import sys
sys.path.insert(0, '/home/hatch/workspace/wubuwizard-cpu-sep')
from mdx_onnx_cpu import stft_complex, N_FFT, CHUNK_SIZE, TRIM
import onnxruntime as ort
from scipy.io import wavfile
sr, data = wavfile.read('/home/hatch/workspace/wubuwizard-cpu-sep/mv14_44k.wav')
assert sr == 44100
mix = data.astype(np.float32)
if data.dtype == np.int16: mix = mix / 32768.0
mix = mix.T  # [2, T]
peak = np.abs(mix).max(); mix_n = mix / peak
# first chunk exactly as demix() does: mixture = [zeros TRIM, mix, zeros pad]; chunk 0 = mixture[:, :CHUNK_SIZE]
mixture = np.concatenate((np.zeros((2, TRIM), dtype=np.float32), mix_n), axis=1)
part = mixture[:, :CHUNK_SIZE]
spek = stft_complex(part)[None, :, :, :]
spek[:, :, :3, :] = 0
print("spek:", spek.shape, spek.dtype, "range", float(spek.min()), float(spek.max()))

inf = shape_inference.infer_shapes(m)
vi = {v.name: v for v in inf.graph.value_info}
m2 = onnx.ModelProto(); m2.CopyFrom(m)
for c in CKPTS:
    node = m.graph.node[c]
    out_name = node.output[0]
    if out_name in vi:
        m2.graph.output.append(vi[out_name])
so = ort.SessionOptions(); so.intra_op_num_threads = 2; so.inter_op_num_threads = 1
sess = ort.InferenceSession(m2.SerializeToString(), providers=["CPUExecutionProvider"], sess_options=so)
outs = sess.run(None, {"input": spek})
save = {"input_spek": spek}
for c, o in zip(CKPTS, outs):
    save[f"node{c:03d}_{m.graph.node[c].op_type}"] = o
    print(f"node {c} {m.graph.node[c].op_type}: {o.shape} range [{o.min():.4f},{o.max():.4f}] mean {o.mean():.5f}")
np.savez(f'{OUT}/ref_chunk0.npz', **save)
print("saved ref_chunk0.npz")
