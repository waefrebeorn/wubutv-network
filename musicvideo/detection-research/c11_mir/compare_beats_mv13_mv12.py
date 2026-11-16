#!/usr/bin/env python3
"""Step 0 validation: c11_mir onset floor + DP beats on MV-13 / MV-12.

Compares DP beats (floor 0 vs floor 1.0x median) against each track's
measured grid (MV-13: 97.0 BPM / 0.619s / 0.250s; MV-12: 131.5 BPM /
0.456s / 0.250s) and against librosa beat_track on the same audio.
Also prints the tempo-AC plateau from the C11 flux for each track.
"""
import json
import subprocess
import numpy as np
import librosa

D = "/home/hatch/workspace/wubutv-network/musicvideo/detection-research/c11_mir"
TRACKS = {
    "MV-13": {"wav": "/tmp/mv13_16k.wav", "bpm": 97.0, "period": 0.619, "phase": 0.250,
              "f0": "/tmp/c11_mir_mv13_f0b.json", "f1": "/tmp/c11_mir_mv13_f1b.json"},
    "MV-12": {"wav": "/tmp/mv12_16k.wav", "bpm": 131.5, "period": 0.456, "phase": 0.250,
              "f0": "/tmp/c11_mir_mv12_f0b.json", "f1": "/tmp/c11_mir_mv12_f1b.json"},
}


def grid_stats(b, period, phase, label):
    b = np.array(b)
    k = np.round((b - phase) / period)
    grid_t = phase + k * period
    off = b - grid_t
    slope, _ = np.polyfit(b, off, 1)
    print(f"  {label} vs grid: n={len(b)} median|off| {np.median(np.abs(off)):.4f}s "
          f"mean {np.mean(off):+.4f}s std {np.std(off):.4f}s max|off| {np.max(np.abs(off)):.4f}s "
          f"within50 {np.mean(np.abs(off) <= 0.05):.3f} within100 {np.mean(np.abs(off) <= 0.10):.3f} "
          f"drift {slope * (b[-1] - b[0]):+.3f}s")
    ibis = np.diff(b)
    print(f"    median IBI {np.median(ibis):.4f}s -> {60.0 / np.median(ibis):.2f} BPM; "
          f"first {b[0]:.3f}s last {b[-1]:.3f}s")
    return {"n": int(len(b)), "median_abs_offset_s": round(float(np.median(np.abs(off))), 4),
            "mean_offset_s": round(float(np.mean(off)), 4),
            "std_offset_s": round(float(np.std(off)), 4),
            "max_abs_offset_s": round(float(np.max(np.abs(off))), 4),
            "frac_within_50ms": round(float(np.mean(np.abs(off) <= 0.05)), 3),
            "frac_within_100ms": round(float(np.mean(np.abs(off) <= 0.10)), 3),
            "drift_s": round(float(slope * (b[-1] - b[0])), 3),
            "median_ibi_s": round(float(np.median(ibis)), 4),
            "median_ibi_bpm": round(60.0 / float(np.median(ibis)), 2)}


SUMMARY = {}


for name, cfg in TRACKS.items():
    print(f"== {name} (measured {cfg['bpm']} BPM, period {cfg['period']}s, phase {cfg['phase']}s)")
    # flux dump via the tool (beats mode, floor 0)
    flux_path = f"/tmp/c11_mir_{name.lower()}_flux.txt"
    subprocess.run([f"{D}/c11_mir", "beats", cfg["wav"], "/tmp/x.json",
                    "--dump-flux", flux_path],
                   check=True, capture_output=True)
    fl = np.loadtxt(flux_path)
    hop_s = 256 / 16000
    # tempo plateau
    cands = []
    for bpm in np.arange(60, 200.5, 0.5):
        lag = int(round(60.0 / bpm / hop_s))
        if lag < 5 or lag >= len(fl):
            continue
        ac = np.corrcoef(fl[:-lag], fl[lag:])[0, 1]
        cands.append((float(ac), float(bpm)))
    cands.sort(reverse=True)
    print(f"  flux: n={len(fl)} median {np.median(fl):.4f} mean {np.mean(fl):.4f} max {fl.max():.4f}")
    print("  top BPM (ac, bpm):", [(round(a, 4), b) for a, b in cands[:6]])
    # phase at the MEASURED period from the C flux
    scores = []
    dur = len(fl) * hop_s
    for ph in np.arange(0, cfg["period"], 0.01):
        beats = np.arange(ph, dur, cfg["period"])
        s = sum(fl[int(round(b / hop_s))] for b in beats
                if 0 <= int(round(b / hop_s)) < len(fl))
        scores.append(s)
    ph_canon = float(np.arange(0, cfg["period"], 0.01)[int(np.argmax(scores))])
    print(f"  phase at measured period {cfg['period']}s from C flux: {ph_canon:.2f}s "
          f"(measured {cfg['phase']}s)")
    f0 = json.load(open(cfg["f0"]))
    f1 = json.load(open(cfg["f1"]))
    print(f"  C tempo: {f0['tempo_bpm']} BPM ac {f0['tempo_ac']:.4f} "
          f"period {f0['period_s']}s phase {f0['phase_s']}s")
    print(f"  floor 0: {f0['n_beats']} beats; floor 1.0: {f1['n_beats']} beats "
          f"(dropped {f1['beats_dropped_by_floor']})")
    off0 = grid_stats(f0["beats_s"], cfg["period"], cfg["phase"], "DP floor0 ")
    off1 = grid_stats(f1["beats_s"], cfg["period"], cfg["phase"], "DP floor1.0")
    # librosa comparison
    y, sr = librosa.load(cfg["wav"], sr=16000, mono=True)
    tempo, lib_beats = librosa.beat.beat_track(y=y, sr=sr, hop_length=256,
                                               start_bpm=120.0)
    lib_beats = librosa.frames_to_time(lib_beats, sr=sr, hop_length=256)
    print(f"  librosa: tempo {tempo} BPM, {len(lib_beats)} beats")
    off_l = grid_stats(lib_beats, cfg["period"], cfg["phase"], "librosa   ")
    SUMMARY[name] = {
        "measured": {"bpm": cfg["bpm"], "period_s": cfg["period"], "phase_s": cfg["phase"]},
        "flux_median": round(float(np.median(fl)), 4),
        "tempo_plateau_top": [(round(a, 4), b) for a, b in cands[:6]],
        "phase_at_measured_period_s": ph_canon,
        "c_tempo_bpm": f0["tempo_bpm"], "c_tempo_ac": round(float(f0["tempo_ac"]), 4),
        "c_period_s": f0["period_s"], "c_phase_s": f0["phase_s"],
        "n_beats_floor0": int(f0["n_beats"]), "n_beats_floor1.0": int(f1["n_beats"]),
        "dropped_by_floor": int(f1["beats_dropped_by_floor"]),
        "dropped_beat_times_s": [round(float(b), 3) for b in
                                 sorted(set(f0["beats_s"]) - set(f1["beats_s"]))],
        "dp_floor0_vs_grid": off0, "dp_floor1_vs_grid": off1,
        "librosa_tempo_bpm": float(np.atleast_1d(tempo)[0]),
        "librosa_n_beats": int(len(lib_beats)),
        "librosa_vs_grid": off_l,
    }
    print()

with open(f"{D}/c11_mir_mv13_mv12.json", "w") as fh:
    json.dump(SUMMARY, fh, indent=2)
print("wrote", f"{D}/c11_mir_mv13_mv12.json")
