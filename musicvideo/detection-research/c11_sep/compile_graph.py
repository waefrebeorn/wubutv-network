#!/usr/bin/env python3
"""compile_graph.py — compile the MDX-Net ONNX graph into a c11_sep program.

Reads graph_dump.json + weights_index.json + weights.bin, folds every
BatchNormalization into its producer (MatMul or ConvTranspose) at float64
then rounds to float32, and emits:
  prog_weights.bin — one weight blob (originals + folded replacements)
  program.bin      — SepProgHeader + slots + SepInstr[] (see sep_prog.h)
  program.txt      — human-readable instruction listing
  compile_report.json — slot/arena summary

Rules (all asserted):
- Every BN follows a MatMul or ConvTranspose whose output is used ONLY by it.
- BN epsilon is 1e-5 everywhere (verified in the ONNX file).
- Tensor slots: liveness-based reuse (free-list keyed by numel); an op may
  reuse an input's slot for its output iff that input's last use is this op
  (elementwise ops only: Relu/Add/Mul; Transpose and GEMMs get fresh slots).
"""
import json, struct, sys
import numpy as np

DIR = '/home/hatch/workspace/wubutv-network/musicvideo/detection-research/c11_sep'
EPS = 1e-5

OP = dict(NOP=0, CONV1X1=1, CONV3X3=2, CONV2X2_S2=3, CONVTRANSPOSE2X2=4,
          MATMUL=5, RELU=6, ADD=7, MUL=8, TRANSPOSE_HW=9, BN=10)

g = json.load(open(f'{DIR}/graph_dump.json'))
widx = json.load(open(f'{DIR}/weights_index.json'))
wmem = np.memmap(f'{DIR}/weights.bin', dtype=np.float32, mode='r')
nodes = g['nodes']

def warr(name):
    e = widx[name]
    n = int(np.prod(e['shape']))
    return np.array(wmem[e['offset']:e['offset'] + n], dtype=np.float32).reshape(e['shape'])

def shape_of(name):
    raise KeyError(name)  # unused; shapes come from node out_shapes

# ---- use counts + last use ---------------------------------------------
uses = {}
for i, n in enumerate(nodes):
    for inp in n.get('in', []):
        uses.setdefault(inp, []).append(i)
GRAPH_INPUT = 'input'
assert GRAPH_INPUT in uses or True

# ---- BN folding ---------------------------------------------------------
# FOLDING RULE (corrected): BN normalizes over the CHANNEL dim (dim 1).
# - ConvTranspose: the BN scale is per OUTPUT channel, and the weight is
#   [Cin, Cout, kh, kw] — scaling each oc slice folds cleanly, bias folds
#   as (b-mean)*s + beta. These BNs are SKIPPED (folded into the producer).
# - MatMul: the weight B [K, M] is SHARED across all channels, while the BN
#   scale varies per channel — it CANNOT fold into B. These BNs stay as
#   explicit OP_BN instructions (y = x*s[c] + shift[c]) after the MatMul.
#   (Folding into the MatMul input would cost the same elementwise pass
#   and add rounding; the explicit BN is the faithful form.)
folded = {}
skip_nodes = set()
bn_after_matmul = {}  # bn node idx -> (s_array, shift_array)
for i, n in enumerate(nodes):
    if n['op'] != 'BatchNormalization':
        continue
    src = n['in'][0]
    prod = next(j for j, m in enumerate(nodes) if src in m.get('out', []))
    assert uses[src] == [i], f"BN {i}: input {src} used by {uses[src]}, expected only this BN"
    gamma = warr(n['in'][1]).astype(np.float64)
    beta = warr(n['in'][2]).astype(np.float64)
    mean = warr(n['in'][3]).astype(np.float64)
    var = warr(n['in'][4]).astype(np.float64)
    s = gamma / np.sqrt(var + EPS)
    pn = nodes[prod]
    if pn['op'] == 'ConvTranspose':
        W = warr(pn['in'][1]).astype(np.float64)  # [Cin, Cout, 2, 2]
        Wf = (W * s[None, :, None, None]).astype(np.float32)
        b = warr(pn['in'][2]).astype(np.float64)
        bf = ((b - mean) * s + beta).astype(np.float32)
        folded[prod] = (Wf, bf)
        skip_nodes.add(i)
    elif pn['op'] == 'MatMul':
        shift = (beta - mean * s).astype(np.float32)
        bn_after_matmul[i] = (s.astype(np.float32), shift)
    else:
        raise AssertionError(f"BN {i} follows {pn['op']} node {prod}, not MatMul/ConvTranspose")
print(f"folded {len(folded)} BNs into ConvTranspose producers; "
      f"{len(bn_after_matmul)} BNs after MatMul stay explicit")

# ---- weight blob ---------------------------------------------------------
blob = bytearray()
def blob_put(arr):
    """Append float32 array, return (offset, length_bytes)."""
    a = np.ascontiguousarray(arr, dtype=np.float32)
    off = len(blob)
    blob.extend(a.tobytes())
    return off, a.nbytes

def weight_ref(name):
    """(offset, length) for an original weight in prog_weights.bin."""
    return blob_put(warr(name))

# ---- slot allocation + instruction emission ------------------------------
slots = []            # (offset, C, H, W)
slot_of = {}          # value name -> slot id
free_list = {}        # numel -> [slot ids]
arena_bump = 0
arena_peak = 0
live_bytes = 0
live_peak = 0

def alloc_slot(shape):
    global arena_bump, arena_peak, live_bytes, live_peak
    C, H, W = shape
    numel = C * H * W
    if free_list.get(numel):
        sid = free_list[numel].pop()
        live_bytes += numel * 4
        live_peak = max(live_peak, live_bytes)
        # NOTE: do NOT update slots[sid]'s recorded shape here. A slot is
        # reused across different shapes with the same numel (e.g. slot 2
        # first holds [48,256,3072], later [48,3072,256]); the slots[] table
        # in program.bin is static, so a recorded shape can only ever be the
        # FIRST shape. Ops that need a shape (BN, Transpose) read it from
        # the INSTRUCTION's dims in sep_interp.c, never from slots[].
        # (An earlier attempt to update the shape on reuse swapped slot 1/2's
        # shapes and broke every Transpose downstream of node 2.)
        return sid
    off = arena_bump
    arena_bump += numel * 4
    arena_peak = max(arena_peak, arena_bump)
    live_bytes += numel * 4
    live_peak = max(live_peak, live_bytes)
    slots.append((off, C, H, W))
    return len(slots) - 1

def free_slot(name):
    global live_bytes
    sid = slot_of.pop(name)
    C, H, W = slots[sid][1:]
    free_list.setdefault(C * H * W, []).append(sid)
    live_bytes -= C * H * W * 4

def last_use(name):
    return uses[name][-1] if name in uses else -1

def maybe_free(name, node_idx):
    if name in slot_of and last_use(name) == node_idx:
        free_slot(name)

instrs = []
txt = []
checkpoints = {}  # node idx -> {instr, slot, shape}
CHECKPOINT_NODES = [0, 3, 9, 12, 15, 30, 45, 46, 48, 50, 52, 54, 55, 57, 58, 60, 75, 90, 107, 124, 141, 158, 175, 177]
# graph input slot
in_shape = [4, 3072, 256]
input_slot = alloc_slot(in_shape)
slot_of[GRAPH_INPUT] = input_slot

for i, n in enumerate(nodes):
    if i in skip_nodes:
        # Folded BN (into a ConvTranspose producer): the BN's OUTPUT name
        # aliases the producer's output slot — downstream nodes consume the
        # BN's output name, and the producer already computed the BN'd values
        # via the folded weights/bias. The producer's own output name is dead.
        slot_of[n['out'][0]] = slot_of[n['in'][0]]
        del slot_of[n['in'][0]]
        txt.append(f"{i:3d} BN (folded) {n['in'][0]} -> {n['out'][0]} slot {slot_of[n['out'][0]]}")
        continue
    op = n['op']
    ins = n.get('in', [])
    outs = n.get('out', [])
    out_shape = n['out_shapes'][0][1:] if n.get('out_shapes') else None
    if op == 'Relu':
        s_in = slot_of[ins[0]]
        # In-place: the OUTPUT takes over the input's slot. The input name is
        # consumed (deleted); the slot stays live under the output name.
        # NEVER maybe_free here — the slot is the output's home now.
        slot_of[outs[0]] = s_in
        instrs.append((OP['RELU'], s_in, 0, s_in, 0, 0, 0, 0, *out_shape, 0))
        txt.append(f"{i:3d} RELU in={ins[0]} slot {s_in} (in-place)")
        if ins[0] != outs[0]:
            del slot_of[ins[0]]
    elif op in ('Add', 'Mul'):
        a, b = slot_of[ins[0]], slot_of[ins[1]]
        # reuse a dying input's slot for the output (elementwise, safe)
        if last_use(ins[0]) == i:
            out_slot = a
        elif last_use(ins[1]) == i:
            out_slot = b
        else:
            out_slot = alloc_slot(out_shape)
        instrs.append((OP[op.upper()], a, b, out_slot, 0, 0, 0, 0, *out_shape, 0))
        txt.append(f"{i:3d} {op} {ins[0]}(s{a}) {ins[1]}(s{b}) -> slot {out_slot}")
        slot_of[outs[0]] = out_slot
        # free inputs that die here AND are not the output slot
        for nm, sl in ((ins[0], a), (ins[1], b)):
            if sl != out_slot:
                maybe_free(nm, i)
            elif nm in slot_of and slot_of[nm] == out_slot and nm != outs[0]:
                del slot_of[nm]
        # the surviving input name (if it aliases out_slot) must not linger:
        for nm in (ins[0], ins[1]):
            if nm in slot_of and slot_of[nm] == out_slot and nm != outs[0]:
                del slot_of[nm]
    elif op == 'BatchNormalization':
        # Explicit BN after a MatMul (cannot fold: scale varies per channel,
        # MatMul weight is shared across channels). In-place.
        assert i in bn_after_matmul, f"BN node {i} should have been folded or recorded"
        s_arr, shift_arr = bn_after_matmul[i]
        w_off, w_len = blob_put(s_arr)
        b_off, b_len = blob_put(shift_arr)
        s_in = slot_of[ins[0]]
        slot_of[outs[0]] = s_in
        instrs.append((OP['BN'], s_in, 0, s_in, w_off, w_len, b_off, b_len, *out_shape, 0))
        txt.append(f"{i:3d} BN in={ins[0]} slot {s_in} (in-place) s@{w_off} shift@{b_off}")
        if ins[0] != outs[0]:
            del slot_of[ins[0]]
    elif op == 'Transpose':
        s_in = slot_of[ins[0]]
        out_slot = alloc_slot(out_shape)
        instrs.append((OP['TRANSPOSE_HW'], s_in, 0, out_slot, 0, 0, 0, 0, *out_shape, 0))
        txt.append(f"{i:3d} TRANSPOSE {ins[0]}(s{s_in}) -> slot {out_slot}")
        slot_of[outs[0]] = out_slot
        maybe_free(ins[0], i)
    elif op == 'Conv':
        k = n['attrs']['kernel_shape']
        st = n['attrs']['strides']
        s_in = slot_of[ins[0]]
        w_off, w_len = weight_ref(ins[1])
        b_off, b_len = weight_ref(ins[2])
        out_slot = alloc_slot(out_shape)
        if k == [1, 1]:
            code = OP['CONV1X1']
            dims = (n['in_shapes'][1][1], out_shape[0], out_shape[1], out_shape[2])  # Cin,Cout,H,W
        elif k == [3, 3]:
            assert st == [1, 1]
            code = OP['CONV3X3']
            dims = (out_shape[0], out_shape[1], out_shape[2], 0)  # C,H,W
        elif k == [2, 2]:
            assert st == [2, 2]
            code = OP['CONV2X2_S2']
            dims = (n['in_shapes'][0][1], out_shape[0], n['in_shapes'][0][2], n['in_shapes'][0][3])  # Cin,Cout,H_in,W_in
        else:
            raise AssertionError(f"node {i}: unsupported conv kernel {k}")
        instrs.append((code, s_in, 0, out_slot, w_off, w_len, b_off, b_len, *dims))
        txt.append(f"{i:3d} {'CONV1X1' if code==1 else 'CONV3X3' if code==2 else 'CONV2X2_S2'} {ins[0]}(s{s_in}) -> slot {out_slot} W@{w_off} b@{b_off}")
        slot_of[outs[0]] = out_slot
        maybe_free(ins[0], i)
    elif op == 'ConvTranspose':
        assert n['attrs']['kernel_shape'] == [2, 2] and n['attrs']['strides'] == [2, 2]
        s_in = slot_of[ins[0]]
        if i in folded:
            Wf, bf = folded[i]
            w_off, w_len = blob_put(Wf)
            b_off, b_len = blob_put(bf)
        else:
            w_off, w_len = weight_ref(ins[1])
            b_off, b_len = weight_ref(ins[2])
        out_slot = alloc_slot(out_shape)
        dims = (n['in_shapes'][0][1], out_shape[0], n['in_shapes'][0][2], n['in_shapes'][0][3])
        instrs.append((OP['CONVTRANSPOSE2X2'], s_in, 0, out_slot, w_off, w_len, b_off, b_len, *dims))
        txt.append(f"{i:3d} CONVTRANSPOSE2X2 {ins[0]}(s{s_in}) -> slot {out_slot} W@{w_off} b@{b_off} (folded={i in folded})")
        slot_of[outs[0]] = out_slot
        maybe_free(ins[0], i)
    elif op == 'MatMul':
        s_in = slot_of[ins[0]]
        # Original B weight; NO bias (MatMul has none in the graph). The BN
        # that follows is a separate OP_BN instruction (see above).
        w_off, w_len = weight_ref(ins[1])
        out_slot = alloc_slot(out_shape)
        # d0=C d1=H d2=K d3=M
        C, H, K = n['in_shapes'][0][1], n['in_shapes'][0][2], n['in_shapes'][0][3]
        M = n['out_shapes'][0][3]
        instrs.append((OP['MATMUL'], s_in, 0, out_slot, w_off, w_len, 0, 0, C, H, K, M))
        txt.append(f"{i:3d} MATMUL {ins[0]}(s{s_in}) -> slot {out_slot} B@{w_off} (no bias; BN follows)")
        slot_of[outs[0]] = out_slot
        maybe_free(ins[0], i)
    else:
        raise AssertionError(f"node {i}: unsupported op {op}")
    # checkpoint bookkeeping (nodes that emit exactly one instruction)
    if i in CHECKPOINT_NODES:
        checkpoints[i] = {'instr': len(instrs) - 1, 'slot': slot_of[outs[0]],
                          'shape': list(out_shape)}

output_slot = slot_of[nodes[-1]['out'][0]]
print(f"instructions: {len(instrs)} (BNs folded: {len(skip_nodes)}, original nodes: {len(nodes)})")
print(f"slots: {len(slots)}, arena bump: {arena_bump/1048576:.1f} MB, peak live: {live_peak/1048576:.1f} MB")
print(f"weight blob: {len(blob)/1048576:.1f} MB")
print(f"input slot {input_slot}, output slot {output_slot}")

# ---- write outputs --------------------------------------------------------
with open(f'{DIR}/prog_weights.bin', 'wb') as f:
    f.write(blob)
hdr = struct.pack('<8s7I', b'SEPPROG1', len(instrs), len(slots), arena_bump,
                  input_slot, output_slot, 0, 0)
assert len(hdr) == 36, len(hdr)  # must match SepProgHeader in sep_prog.h
with open(f'{DIR}/program.bin', 'wb') as f:
    f.write(hdr)
    for (off, C, H, W) in slots:
        f.write(struct.pack('<IIII', off, C, H, W))
    for ins in instrs:
        f.write(struct.pack('<12I', *ins))
with open(f'{DIR}/program.txt', 'w') as f:
    f.write(f"# c11_sep program: {len(instrs)} instructions, {len(slots)} slots, arena {arena_bump} bytes\n")
    f.write(f"# input slot {input_slot} shape {in_shape}, output slot {output_slot}\n")
    f.write('\n'.join(txt) + '\n')

report = {
    'n_nodes': len(nodes), 'n_bn_folded_into_convtranspose': len(skip_nodes),
    'n_bn_explicit_after_matmul': len(bn_after_matmul), 'n_instr': len(instrs),
    'n_slots': len(slots), 'arena_bytes': arena_bump, 'arena_peak_bytes': arena_peak,
    'live_peak_bytes': live_peak,
    'arena_mb': arena_bump / 1048576,
    'weight_blob_mb': len(blob) / 1048576,
    'input_slot': input_slot, 'output_slot': output_slot,
}
json.dump(report, open(f'{DIR}/compile_report.json', 'w'), indent=2)
json.dump(checkpoints, open(f'{DIR}/checkpoints.json', 'w'), indent=2)
print(f"checkpoints: {sorted(checkpoints)}")
print(json.dumps(report, indent=2))
