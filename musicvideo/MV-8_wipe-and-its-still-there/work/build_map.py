#!/usr/bin/env python3
"""Assemble work/crescendo_map.json from measured data: hit_list.json (tiered hits),
crescendo_raw.json (energy curve, peaks, silence), + the 2 intro stabs from the raw
onset pass. Section boundaries are the measured ones from LYRIC_TIMELINE.md."""
import json
import numpy as np

raw = json.load(open("work/crescendo_raw.json"))
hits = json.load(open("work/hit_list.json"))["hits"]
curve = raw["energy_curve_0p5s_win_0p25s_hop"]

SECTIONS = [
    ("Intro", 0.00, 5.97), ("Hook 1", 5.97, 34.40), ("Interlude", 34.40, 60.46),
    ("Verse", 60.46, 65.12), ("Pre-Hook", 65.12, 67.26), ("Hook 2", 67.26, 105.94),
    ("Drop", 105.94, 120.40), ("Final Hook", 120.40, 146.00), ("Outro (instrumental)", 146.00, 187.20),
]
def section_of(t):
    for name, a, b in SECTIONS:
        if a <= t < b:
            return name
    return "Outro (instrumental)"

def stats(a, b):
    vals = [c["rms_db"] for c in curve if a <= c["t"] < b]
    return {"mean_rms_db": round(float(np.mean(vals)), 2), "max_rms_db": round(float(np.max(vals)), 2),
            "min_rms_db": round(float(np.min(vals)), 2)} if vals else {}

out_hits = []
for h in hits:
    out_hits.append({"t": h["t"], "tier": h["tier"], "strength": h["strength"],
                     "peak_dbfs": h["peak_dbfs"], "on_downbeat": h["on_downbeat"],
                     "dt_beat": h["dt_beat"], "section": section_of(h["t"])})
# intro stabs: below the tier thresholds but structurally the sheet's beat-1 stab + build hit
for t in (0.546, 2.519):
    o = min(raw["onsets"], key=lambda o: abs(o["t"] - t))
    out_hits.append({"t": o["t"], "tier": "intro_stab", "strength": o["strength"],
                     "peak_dbfs": o["peak_dbfs"], "on_downbeat": False, "dt_beat": None, "section": "Intro"})
out_hits.sort(key=lambda h: h["t"])

blocks = []
for t0 in range(0, 190, 10):
    vals = [c["rms_db"] for c in curve if t0 <= c["t"] < t0 + 10]
    if vals:
        blocks.append({"t": t0, "mean_rms_db": round(float(np.mean(vals)), 2)})

def win_mean(a, b):
    vals = [c["rms_db"] for c in curve if a <= c["t"] < b]
    return round(float(np.mean(vals)), 2) if vals else None

result = {
    "track": "track.mp3", "md5": "63799741a41e9c2c9082d8c57b4f18d0", "duration_s": 187.2,
    "tempo_bpm": 123.05, "beat_interval_s": 0.4876,
    "method_hits": "librosa onset_strength hop256@22050, uncapped env/p99, clustered <=0.12s, beat-quantized vs work/beat_grid.json; hit_major: strength>=p90 & |dt_beat|<=0.10s & peak>=-6dBFS; stab: strength>=p75 & |dt_beat|<=0.12s; intro_stab: sheet-annotated intro hits below tier threshold, kept for structure",
    "n_hits": len(out_hits),
    "n_hit_major": sum(1 for h in out_hits if h["tier"] == "hit_major"),
    "n_stab": sum(1 for h in out_hits if h["tier"] == "stab"),
    "hits": out_hits,
    "energy_curve_0p5s_win_0p25s_hop_dbfs": curve,
    "macro_blocks_10s_mean_rms_db": blocks,
    "sections": [{"name": n, "start": a, "end": b, "dur": round(b - a, 2),
                  "n_hits": sum(1 for h in out_hits if a <= h["t"] < b),
                  "n_major": sum(1 for h in out_hits if h["tier"] == "hit_major" and a <= h["t"] < b),
                  **stats(a, b)} for n, a, b in SECTIONS],
    "ramps": [
        {"name": "Intro build", "span": [0.5, 5.97], "from_db": win_mean(1.0, 1.5), "to_db": win_mean(5.5, 5.97),
         "note": "after the beat-1 stab (0.546) the level climbs steadily into the groove entry hits at 5.96/6.44"},
        {"name": "Pre-Hook build", "span": [60.46, 67.26], "from_db": win_mean(58.0, 60.0), "to_db": win_mean(65.0, 67.0),
         "note": "sheet's [Building Snare] + rising drums: real but modest (+~2 dB); the build is textural (snare/hit density), not a level swell"},
        {"name": "Drop strip (NOT performed as a level drop)", "span": [105.94, 120.40], "from_db": win_mean(100.0, 105.94), "to_db": win_mean(106.0, 120.0),
         "note": "level stays flat (~-16.5 dBFS mean) through the Drop; no strip-down, no silence. The drop exists only as the vocal gap + the hit pair at 112.25/112.72"},
        {"name": "Outro decay", "span": [184.0, 187.20], "from_db": win_mean(184.0, 184.5), "to_db": win_mean(186.5, 187.0),
         "note": "final decay after the last stabs (~180.6-183.3); audio tail reaches ~-42 dBFS by 186.5 and ends at 187.2"},
    ],
    "silence": {
        "performed_gaps_below_-50dbfs_min_0p15s": raw["silence_gaps_below_-50dbfs_min_0p15s"],
        "sheet_drop_silence_half_bar": "NOT PERFORMED. Fine-RMS scan (0.05s windows) finds no dip below -38 dBFS lasting >=0.25s anywhere after the 0.52s leader; deepest mid-track fine window is -29.26 dBFS @ 63.7s (groove dip). The only true silence is the leader 0.00-0.50s before the intro stab.",
        "leader_silence_s": [0.0, 0.5],
    },
    "true_peak": raw["true_peak"],
    "loudest_0p5s_window": raw["loudest_0p5s_window"],
    "loudest_moment_note": "true peak sample 159.435s (-2.16 dBFS) and loudest 0.5s window @174.75s (-12.03 dBFS RMS) both sit in the performed instrumental Outro zone (146-187.2), which is louder than any chant section",
}
json.dump(result, open("work/crescendo_map.json", "w"), indent=1)
print("hits:", result["n_hits"], "major:", result["n_hit_major"], "stab:", result["n_stab"])
for s in result["sections"]:
    print(f'{s["name"]:24s} {s["start"]:7.2f}-{s["end"]:7.2f} mean {s.get("mean_rms_db")} max {s.get("max_rms_db")} hits {s["n_hits"]} major {s["n_major"]}')
print("ramps:", [(r["name"], r["from_db"], r["to_db"]) for r in result["ramps"]])
