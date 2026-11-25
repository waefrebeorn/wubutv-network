#!/usr/bin/env python3
"""Validate c11_tsm against the Python prototype (tsm_proto.py / tsm_m4b.py).

Bars covered here (no ASR): 1 (hit identity), 6 (parity: gap alphas
identical, stretched-audio corr >= 0.99 vs prototype M7), 7 (runtime).
ASR bars (2, 3, 4, 5) are graded by c11_grade.py (faster-whisper) into
the same JSON. Outputs land in c11_tsm/out/ (validation artifacts only,
never committed).
"""
import json, os, subprocess, sys, time
import numpy as np
import soundfile as sf

ROOT = '/home/hatch/workspace/wubutv-network/musicvideo/detection-research/c11_tsm'
SRC = '/home/hatch/workspace/research_notes/tsm-driedger-2014'
BASE = '/home/hatch/workspace/wubutv-network/musicvideo/MV-14_clip-it'
SR = 16000
BIN = f'{ROOT}/c11_tsm'
ASAN = f'{ROOT}/c11_tsm_asan'

TAKES = {
 'S47': dict(file='work/qc_S47_t1/audio.wav', win=(1.16, 2.82),
             song_on=[106.24, 106.66, 107.10, 107.44, 107.70, 108.04, 108.30],
             take_on=[1.16, 1.56, 1.96, 2.10, 2.26, 2.40, 2.56],
             words=['this', 'is', 'how', 'you', 'do', 'it', 'now'], alpha=1.518),
 'S49': dict(file='work/qc_S49_t1/audio.wav', win=(0.00, 1.56),
             song_on=[112.16, 112.68, 113.00, 113.40],
             take_on=[0.00, 0.50, 0.86, 1.30],
             words=['clip', 'it', 'post', 'it'], alpha=0.9487),
 'S50': dict(file='work/qc_S50_t1/audio.wav', win=(4.02, 5.74),
             song_on=[113.72, 113.98, 114.22, 114.58],
             take_on=[4.02, 4.70, 4.92, 5.24],
             words=['keep', 'the', 'work', 'alive'], alpha=0.8023),
 'S52': dict(file='work/qc_S52_t1/audio.wav', win=(0.00, 2.94),
             song_on=[117.40, 117.92, 118.06, 118.66, 118.88, 119.16, 119.38, 119.72],
             take_on=[0.00, 0.48, 0.90, 1.20, 1.92, 2.06, 2.24, 2.48],
             words=['clip', 'it', 'post', 'it', 'help', 'me', 'stay', 'online'], alpha=1.0748),
}
# Owed moderate-squeeze take (bar 4): S49 audio, song grid re-set so the
# gap after 'post' (hit 2) squeezes to alpha 0.60 — the untested 0.5-0.87
# band. Overall alpha = (113.284-112.16)/1.30 = 0.8646.
TAKES['S49MOD'] = dict(file='work/qc_S49_t1/audio.wav', win=(0.00, 1.56),
             song_on=[112.16, 112.68, 113.00, 113.284],
             take_on=[0.00, 0.50, 0.86, 1.30],
             words=['clip', 'it', 'post', 'it'], alpha=0.8646)


def corr(a, b):
    n = min(len(a), len(b))
    a, b = a[:n].astype(np.float64), b[:n].astype(np.float64)
    a, b = a - a.mean(), b - b.mean()
    d = np.sqrt((a * a).sum() * (b * b).sum())
    return float((a * b).sum() / d) if d > 0 else 1.0


def run(cmd, **kw):
    t0 = time.time()
    r = subprocess.run(cmd, capture_output=True, text=True, **kw)
    return r, time.time() - t0


def main():
    os.makedirs(f'{ROOT}/out', exist_ok=True)
    out_json = f'{ROOT}/c11_tsm_validation.json'
    res = json.load(open(out_json)) if os.path.exists(out_json) else {}
    proto_m4b = json.load(open(f'{SRC}/m4b_measurements.json'))

    # ---- extract take windows (identical to tsm_m4b.py) ----
    for name, take in TAKES.items():
        y_full, _ = sf.read(os.path.join(BASE, take['file']))
        a, b = take['win']
        y = y_full[int(a * SR):int(b * SR)]
        sf.write(f'{ROOT}/out/{name}_in.wav', y, SR)
        take['_y'] = y

    bars = res.setdefault('bars', {})
    per_take = res.setdefault('per_take', {})

    # ---- ASan smoke: one m7 run under the ASan binary ----
    t = TAKES['S47']
    hits = ','.join(f'{o - t["win"][0]:.6f}' for o in t['take_on'])
    song = ','.join(f'{s:.6f}' for s in t['song_on'])
    r, dt = run([ASAN, 'm7', '--in', f'{ROOT}/out/S47_in.wav',
                 '--out', f'{ROOT}/out/S47_asan.wav', '--hits', hits,
                 '--song', song, '--alpha', str(t['alpha']),
                 '--words', ','.join(t['words']), '--take', 'S47',
                 '--json', f'{ROOT}/out/S47_asan.json'])
    res['asan'] = {'rc': r.returncode, 'stderr': r.stderr.strip()[-500:]}
    print('ASan S47 rc=', r.returncode, flush=True)
    if r.returncode != 0:
        print(r.stderr[-2000:], flush=True)

    # ---- per-take runs: m7 guard-off (parity), m7 guard-on, ola ----
    for name, take in TAKES.items():
        hits = ','.join(f'{o - take["win"][0]:.6f}' for o in take['take_on'])
        song = ','.join(f'{s:.6f}' for s in take['song_on'])
        words = ','.join(take['words'])
        pt = per_take.setdefault(name, {})
        # m7, guard OFF — pure DSP/scheduler parity vs prototype M7
        r, dt = run([BIN, 'm7', '--in', f'{ROOT}/out/{name}_in.wav',
                     '--out', f'{ROOT}/out/{name}_C11_M7_NOGUARD.wav',
                     '--hits', hits, '--song', song, '--alpha', str(take['alpha']),
                     '--words', words, '--take', name, '--no-guard',
                     '--json', f'{ROOT}/out/{name}_C11_M7_NOGUARD.json'])
        assert r.returncode == 0, r.stderr
        pt['m7_noguard_runtime_s'] = round(dt, 3)
        pt['m7_noguard'] = json.load(open(f'{ROOT}/out/{name}_C11_M7_NOGUARD.json'))
        # m7, guard ON (the shipped behaviour)
        r, dt = run([BIN, 'm7', '--in', f'{ROOT}/out/{name}_in.wav',
                     '--out', f'{ROOT}/out/{name}_C11_M7.wav',
                     '--hits', hits, '--song', song, '--alpha', str(take['alpha']),
                     '--words', words, '--take', name,
                     '--json', f'{ROOT}/out/{name}_C11_M7.json'])
        assert r.returncode == 0, r.stderr
        pt['m7_runtime_s'] = round(dt, 3)
        pt['m7'] = json.load(open(f'{ROOT}/out/{name}_C11_M7.json'))
        # ola256 uniform fallback
        r, dt = run([BIN, 'ola', '--in', f'{ROOT}/out/{name}_in.wav',
                     '--out', f'{ROOT}/out/{name}_C11_OLA256.wav',
                     '--alpha', str(take['alpha'])])
        assert r.returncode == 0, r.stderr
        pt['ola_runtime_s'] = round(dt, 3)
        print(f'{name}: m7 {dt:.2f}s gaps={pt["m7"]["gap_alphas"]} '
              f'flags={[g["flag"] for g in pt["m7"]["gaps"]]} '
              f'hit_id={pt["m7"]["hit_max_abs_diff"]:.2g}', flush=True)

    # ---- bar 1: hit identity (guard-on outputs; placement is identical) ----
    b1 = all(pt['m7']['hit_max_abs_diff'] == 0.0 and
             all(e == 0.0 for e in pt['m7']['hit_centre_err_s'])
             for pt in per_take.values())
    bars['1_hit_identity'] = {
        'pass': bool(b1),
        'detail': {n: {'max_abs_diff': pt['m7']['hit_max_abs_diff'],
                       'centre_err_s': pt['m7']['hit_centre_err_s']}
                   for n, pt in per_take.items()}}
    print('BAR 1 hit identity:', 'PASS' if b1 else 'FAIL', flush=True)

    # ---- bar 6: parity vs prototype M7 ----
    b6 = {'alphas_match': {}, 'corr_noguard': {}, 'corr_guard_on': {},
          'corr_guard_on_outside_flags': {}}
    all_alpha = True
    all_corr = True
    for name in ['S47', 'S49', 'S50', 'S52']:
        pt = per_take[name]
        proto_a = proto_m4b[name]['gap_alphas']
        c11_a = pt['m7_noguard']['gap_alphas']
        match = [round(a, 3) for a in proto_a] == [round(a, 3) for a in c11_a]
        b6['alphas_match'][name] = bool(match)
        all_alpha &= match
        ref, _ = sf.read(f'{SRC}/stretched/{name}_M7_SLICE_TGT.wav')
        nog, _ = sf.read(f'{ROOT}/out/{name}_C11_M7_NOGUARD.wav')
        grd, _ = sf.read(f'{ROOT}/out/{name}_C11_M7.wav')
        c_ng = corr(ref, nog)
        c_g = corr(ref, grd)
        b6['corr_noguard'][name] = round(c_ng, 6)
        b6['corr_guard_on'][name] = round(c_g, 6)
        all_corr &= c_ng >= 0.99
        # guard-on corr outside flagged spans: mask flagged output spans
        mask = np.ones(min(len(ref), len(grd)), dtype=bool)
        for gp in pt['m7']['gaps']:
            if gp['flag'] != 'none':
                a = int(gp['out_s'][0] * SR); b = int(gp['out_s'][1] * SR)
                mask[a:b] = False
        c_out = corr(ref[mask], grd[mask]) if mask.sum() > 100 else 1.0
        b6['corr_guard_on_outside_flags'][name] = round(c_out, 6)
        print(f'{name}: alphas_match={match} corr_noguard={c_ng:.6f} '
              f'corr_guard_on={c_g:.6f} corr_outside_flags={c_out:.6f}', flush=True)
    b6['pass'] = bool(all_alpha and all_corr)
    bars['6_parity'] = b6
    print('BAR 6 parity:', 'PASS' if b6['pass'] else 'FAIL', flush=True)

    # ---- bar 7: runtime ----
    worst_m7 = max(pt['m7_runtime_s'] for pt in per_take.values())
    worst_ola = max(pt['ola_runtime_s'] for pt in per_take.values())
    bars['7_runtime'] = {'pass': bool(worst_m7 < 10 and worst_ola < 10),
                         'worst_m7_s': worst_m7, 'worst_ola_s': worst_ola,
                         'bar_s': 10}
    print(f'BAR 7 runtime: worst m7 {worst_m7}s, worst ola {worst_ola}s',
          'PASS' if bars['7_runtime']['pass'] else 'FAIL', flush=True)

    # ---- bar 4 setup: S49MOD gap alphas ----
    pt = per_take['S49MOD']
    bars['4_guard'] = {
        'hard_flagged': {n: [g for g in pt2['m7']['gaps'] if g['flag'] == 'hard']
                         for n, pt2 in per_take.items()},
        'warn_flagged': {n: [g for g in pt2['m7']['gaps'] if g['flag'] == 'warn']
                         for n, pt2 in per_take.items()},
        's49mod_gap_alphas': pt['m7']['gap_alphas'],
        's49mod_expected': 'gap after post (index 2) alpha 0.60 in WARN band',
    }
    print('S49MOD gaps:', pt['m7']['gap_alphas'],
          [g['flag'] for g in pt['m7']['gaps']], flush=True)

    json.dump(res, open(out_json, 'w'), indent=1)
    print('wrote', out_json, flush=True)


if __name__ == '__main__':
    main()
