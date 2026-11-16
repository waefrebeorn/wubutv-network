#!/usr/bin/env python3
"""Generate CUTLIST.md for MV-5 from work/assembly_fit_mv5.json + take md5s."""
import json, os

PROJ = os.path.dirname(os.path.abspath(__file__))
FIT = json.load(open(os.path.join(PROJ, "work", "assembly_fit_mv5.json")))
MD5 = json.load(open(os.path.join(PROJ, "work", "take_md5s.json")))
SCORES = FIT["scores"]

DISPOSITION = {
    "S01": "KEEP t1 — per-line placement (intro refrains; take gaps dropped, hard cut on line boundary). Leader freeze 40f (frame 0 held, pre-word only).",
    "S02": "KEEP t1 — cutaway @1.0x (intro repeat, CAT sings, girl listening).",
    "S03": "KEEP t1 — vocalise SPAN @0.889 (ta-da, GIRL).",
    "S04": "KEEP t1 — per-line placement (L03 rushed, L05 drags; whole-clip SPAN left L03 +1.0-1.5s late). L03/L05 at 1.25 band edge.",
    "S05": "KEEP t1 — SPAN @1.030.",
    "S06": "KEEP t1 — SPAN @0.80 band edge + tail-loop deficit (take tail, moving).",
    "S07": "KEEP t1 — per-line placement (whole-clip SPAN left L16's pickups +1.3-1.9s late). L13 @0.80, L16 @1.25 band edges; +0.30s lateness propagates L13→L16 (disclosed).",
    "S08": "KEEP t2 — per-refrain placement (R1/R2/R4 sung; R3 CAT reaction cover; response windows donor cover). R3 cover is a CAT reaction, not a mouth-sung slot.",
    "S09": "KEEP t1 — per-refrain placement (all 4 refrains in band); response windows donor cover. Warp rescue ≤1.5x carried (max warp 1.133).",
    "S10": "KEEP t1 — cutaway @1.0x (C1 tail tag, CAT sings, girl listening).",
    "S11": "KEEP t4 — L38 montage cover (0.17x, not a mouth-sung slot); L39 grey rescue @0.80 band edge; L40 CAT-half donor cover + girl tail @0.88. Take trimmed 10.00s → 7.84s slot.",
    "S12": "KEEP t1 — per-line placement (take's L43 far too slow for its 1.60s window; whole-clip SPAN left L43 +2-4s late). L41/L43 @0.80 band edge; L43 overruns 1.41s into L44 (disclosed). L42/L44 CAT lines donor cover.",
    "S13": "STRUCTURAL — 3 stagings, 7 takes, all delivery-failed. Chorus cover: static MCU girl + CAT reaction inserts + captions (not a mouth-sung slot). Donors: S13's own rejected tails first.",
    "S14": "STRUCTURAL — 3 takes, pace floor (0.42x). Dusk-rail CAT reaction / B-roll montage cover + captions (not a mouth-sung slot).",
    "S15": "KEEP t1 — GREY RESCUE: SPAN @0.914 over the whole slot incl. the held vocalise; fast pickups land +0.26 to +1.89 late (disclosed). Breath gap donor cover.",
    "S16": "STRUCTURAL — 6 takes, 3 stagings; the voice never restarts the refrain pattern after R1. Chorus cover like S13 (not a mouth-sung slot).",
    "S17": "KEEP t1 — GREY RESCUE: per-refrain (R1 @0.93, R2 @0.71 grey, R3 @0.65 grey, R4 @1.09 by RMS envelope 6.9-8.0s). R3/R4 times are QC's adjudication + RMS, not Whisper's (Whisper's R3/R4 times are wrong — RMS silence 4.6-5.5s and 8.0-10.0s).",
    "S18": "KEEP t1 — cutaway @1.0x (both mouths closed, locks hold).",
    "S19a": "STRUCTURAL — split half, 2 takes, delivery-failed. Grey-sky CAT reaction / B-roll cover + captions (not a mouth-sung slot). S19b stays as the sung half.",
    "S19b": "KEEP t1 — GREY RESCUE: SPAN @0.808 (L77 head re-measured by forced alignment / energy envelope; 'We still' placed as one unit at the head; caption as written).",
    "S20": "KEEP t1 — GREY RESCUE: SPAN @0.80 band edge; 'breeze' overruns 1.05s past the line end into L81 (disclosed). L81 listen tail donor cover.",
    "S21": "PARTIAL t3 — head L82-L86 by measured word times (SPAN @0.80 band edge; drift disclosed, last word +1.07s); tail L87-L89 montage cover + captions (not a mouth-sung slot).",
    "S22": "STRUCTURAL — 3 takes, pace floor (three distinct 'No' attacks need ~3.3s for a 1.66s slot). Head-shake reaction cover + caption (not a mouth-sung slot). Donor: S22 t3's own tail (after the attack, mouth closed).",
    "S23": "KEEP t1 — per-refrain placement by measured word times (R1 @0.96, R2 @0.92, R3 @1.12, 'No need to' @0.81). Unprompted 'No' onset 5.64s used (not prompted 5.24). Low-motion disclosure stands (vocal mean 0.558 @160x90, 0.727 @320x180).",
    "S24": "STRUCTURAL — 3 takes; third refrain never restarts (3/3). Chorus cover like S16 (not a mouth-sung slot).",
    "S25": "KEEP t1 — per-refrain placement by measured word times (R1 @0.80 band edge, R2 @1.09). L104 gap + L106 CAT reaction cover + breath gap donor cover.",
    "S26": "KEEP t1 — per-refrain placement by measured word times (pre-word donor cover 39f, SPAN @0.80, L108 cover from take tail). 'Is it' mishear adjudicated (take sings 'easy').",
    "S27": "KEEP t1 — SPAN @1.232 (held line; breath gap 1.74-2.72s). 3rd word 'easy' lands +1.75s late (the take's breath gap is longer than the song's — disclosed).",
    "S28": "KEEP t1 — GREY RESCUE: SPAN @0.80 band edge (trim 0.05s) + outro tail from take. Ratio 0.78 → 0.80.",
}

def fmt_warp(w):
    return f"{w:.3f}"

lines = []
lines.append("# MV-5 CUTLIST — \"Easy now, easy now (THE VOICE)\"")
lines.append("")
lines.append("Master: `masters/mv5_easy_now_easy_now_16x9.mp4` — ONE 16:9 only, 1280x720 h264 24fps,")
lines.append("AAC 48kHz stereo, faststart, 4954 frames, 206.400s. Sole master audio: `track.mp3`")
lines.append("(md5 `0c1bcafa568547e2d4fa36e133ad3626`, muxed untouched; generated clip audio dropped).")
lines.append("Captions: `captions_16x9.ass` (453 events, line-block + per-word cadmium highlight),")
lines.append("keyed to SONG word times. Bug `~ WuBu ~` burned on all frames.")
lines.append("")
lines.append("Method: WORD-SYNC (Slopcannon stage 6). Per-word offsets measured from fresh prompted")
lines.append("transcriptions of every KEEP take (`work/assembly_take_words/`) against SONG_WORDS.json,")
lines.append("placed by min-total-cost assignment. Warps in [0.80, 1.25] except the two sanctioned")
lines.append("S17 grey rescues (0.71/0.65). No frozen frame while words play (the one exception is")
lines.append("the S01 pre-word leader freeze, MV-3 precedent). Structural scenes are donor montage")
lines.append("(KEEP takes' post-word tails first, then REJECTED takes' silent tails — delivery-only")
lines.append("rejects, picture on-brief — used ONLY as silent reaction/B-roll, never as a sung take;")
lines.append("each slice motion-verified: mean diff >= 0.10 at 160x90 and longest near-dup run < 24f).")
lines.append("")
lines.append("## Scene map")
lines.append("")
lines.append("| Scene | Slot (s) | Take | md5 | Warp(s) | Disposition |")
lines.append("|---|---|---|---|---|---|")
for i, sc in enumerate(FIT["scenes"]):
    s0, s1 = FIT["bounds"][i], FIT["bounds"][i + 1]
    ps = FIT["plan"][sc]
    takes = sorted({p["take"] for p in ps})
    take_cell = "<br>".join(takes)
    md5_cell = "<br>".join(MD5[t] for t in takes)
    warps = sorted({p["warp"] for p in ps
                    if p["kind"] not in ("donor-tail", "donor-rej-tail", "cover-tail",
                                         "cover-rej-tail", "gap", "tail", "tail-loop",
                                         "tail-L106", "tail-gap", "tail-L108", "tail-outro",
                                         "freeze-leader", "arrival", "arrival-gap",
                                         "cover-L38")})
    warp_cell = ", ".join(fmt_warp(w) for w in warps) if warps else "cover"
    lines.append(f"| {sc} | {s0:.2f}-{s1:.2f} | {take_cell} | {md5_cell} | {warp_cell} | {DISPOSITION[sc]} |")
lines.append("")
lines.append("## Per-word sync scores (fit, placed-time min-cost assignment)")
lines.append("")
lines.append("Pairs = take words matched to song words (Whisper repeat-collapses each doubled")
lines.append("\"Easy now\" refrain to one pair, so refrain scenes show ~half the song words as")
lines.append("\"missing\" — those are the collapsed repeats, sung by the take, not missing words.")
lines.append("CAT-half words in split lines (S11 L40, S23 L96 'run') are covered, not sung.")
lines.append("")
lines.append("| Scene | Pairs | Median |off| | Max |off| | Within ±0.50s |")
lines.append("|---|---|---|---|---|")
for sc in FIT["scenes"]:
    s = SCORES.get(sc)
    if not s:
        lines.append(f"| {sc} | cover (no sung words) | — | — | — |")
        continue
    lines.append(f"| {sc} | {s['n_pairs']}/{s['n_song']} | {s['median_abs']:.3f}s | "
                 f"{s['max_abs']:.3f}s | {s['within_050']}/{s['n_pairs']} |")
lines.append("")
lines.append("Weakest scenes (disclosed): S15 median 0.897s (grey rescue, fast pickups +0.26 to +1.89);")
lines.append("S20 median 0.732s (band-edge 0.80, 'breeze' overruns 1.05s); S21 median 0.724s")
lines.append("(band-edge 0.80, drift to +1.37 on 'pace'); S27 'easy' +1.75s (breath gap longer than")
lines.append("the song's); S12 'bills' +1.27s (take's L43 too slow for its 1.60s window).")
lines.append("")
lines.append("## Donor ledger (all 68 donor slices, motion-verified)")
lines.append("")
lines.append("Format: scene | window (s) | donor take [frames] | kind. Donor ranges are disjoint")
lines.append("from every direct piece's source range. Two slices were skipped by the motion check")
lines.append("in the final fit (S14 t1 tail: 29f near-dup run; S21 t3 tail end: mean 0.07).")
lines.append("")
for sc in FIT["scenes"]:
    for p in FIT["plan"][sc]:
        if p["kind"].startswith(("donor-", "cover-")):
            lines.append(f"- {sc} {p['dst0']:.2f}-{p['dst1']:.2f}s: {p['take']}[{p['sf']}:{p['ef']}] "
                         f"({p['kind']}, md5 {MD5[p['take']]})")
lines.append("")
open(os.path.join(PROJ, "CUTLIST.md"), "w").write("\n".join(lines) + "\n")
print("wrote CUTLIST.md,", len(lines), "lines")
