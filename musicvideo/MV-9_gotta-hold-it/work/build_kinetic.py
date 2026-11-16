#!/usr/bin/env python3
"""Build the MV-9 kinetic type layer (.ass) for assembly.

Adapted from MV-8 v3 build_kinetic_v3.py. Words from analysis/SONG_WORDS.json
(231 words) + the sheet; per-line presets from work/MV_PREPRO_MV-9.md.
Corner bug "~ WuBu ~" bottom-right, full duration (MV-8 v1 form verbatim).

Sheet-word corrections applied to ASR labels (times unchanged — ASR is the
timing record, the sheet is the lyric record):
  "light" -> "line" (idx 24); "pull the party light" -> "Porta potty line"
  (idx 31-34, 112-115, chorus only — idx 173-176 KEPT, S13a really sings
  "Pull the party light"); "festival party party" -> "Festival porta potty"
  (idx 46-48, 127-129, 192-194); "portal," -> "porta," (idx 103);
  "eating" -> "heat" (idx 83); "I've extended near" -> "Addicts standing near"
  (idx 157-159).
Excluded: idx 65 "hold" 52.00-63.96 — a 12s ASR merge artifact (chant tail +
instrumental), not a real held word; showing it for 12s would be wrong.
S12b block (134.42-145.72): the ASR collapsed the whole block into one 11.3s
"to" (idx 171) — unmeasurable, so the kinetic there follows the S12b take's
warped word times (3 "Need to go" pairs, from work/qc/s12b-t2/words.json),
NOT SONG_WORDS. Disclosed in work/assembly_notes.md.
Lists (S10, S14) are STACKed as three sub-lines each ("Four squares left" /
"QR code on the phone" / "Pay the ninety nine") — a 12-word STACK would run
off the bottom of the frame at fontsize 54.
"""
import json
import sys

sys.path.insert(0, "/home/hatch/workspace/wubutv-network/musicvideo/visual-forms/tools")
from kinetic_ass import Ass, emit_line  # noqa: E402

BASE = "/home/hatch/workspace/wubutv-network/musicvideo/MV-9_gotta-hold-it"
ASM = f"{BASE}/work/assembly"
OUT = f"{ASM}/mv9_kinetic.ass"

song = json.load(open(f"{BASE}/analysis/SONG_WORDS.json"))["words"]
words = [{"word": w["w"], "start": float(w["s"]), "end": float(w["e"])} for w in song]

# --- sheet-word corrections (by song-word index) ---
def relabel(i, new):
    words[i]["word"] = new

relabel(24, "line")

def collapse_pull_party(idx):
    """ASR 'pull the party light,' (4 words) -> sheet 'Porta potty line,' (3).
    Porta spans pull+the; potty = party; line, = light, (times unchanged)."""
    pull, the, party, light = (words[idx + j] for j in range(4))
    assert pull["word"] == "pull" and the["word"] == "the"
    assert party["word"] == "party" and light["word"].startswith("light")
    words[idx] = {"word": "Porta", "start": pull["start"], "end": the["end"]}
    words[idx + 1] = {"word": "potty", "start": party["start"], "end": party["end"]}
    words[idx + 2] = {"word": "line,", "start": light["start"], "end": light["end"]}
    del words[idx + 3]

collapse_pull_party(31)
# indices shift by -1 after the deletion; use a time-based map for the rest
def by_time(t):
    for i, w in enumerate(words):
        if abs(w["start"] - t) < 0.01:
            return i
    raise KeyError(f"no word at {t}")

# "festival party party" (38.94) -> "Festival porta potty"
for j, new in ((0, "Festival"), (1, "porta"), (2, "potty")):
    relabel(by_time(38.94) + j, new)
# "eating" (69.52) -> "heat"
relabel(by_time(69.52), "heat")
# "portal," (81.00) -> "porta,"
relabel(by_time(81.00), "porta,")
# "pull the party light," (89.48) -> "Porta potty line,"
collapse_pull_party(by_time(89.48))
# "festival party party," (96.84) -> "Festival porta potty,"
for j, new in ((0, "Festival"), (1, "porta"), (2, "potty,")):
    relabel(by_time(96.84) + j, new)
# "I've extended near" (113.00) -> "Addicts standing near"
for j, new in ((0, "Addicts"), (1, "standing"), (2, "near")):
    relabel(by_time(113.00) + j, new)
# "festival party party," (152.74) -> "Festival porta potty,"
for j, new in ((0, "Festival"), (1, "porta"), (2, "potty,")):
    relabel(by_time(152.74) + j, new)

# drop idx-65 artifact: the "hold" spanning 52.00-63.96
words = [w for w in words if not (abs(w["start"] - 52.00) < 0.01 and w["word"] == "hold")]
# drop zero/near-zero-duration ASR artifacts (unmeasurable words — the ASR
# collapsed them to a point; captioning them would flash for 0.05s).
# Drops idx 73 "hold" (66.26), idx 74 "it" (66.26-66.28), idx 218 "to" /
# idx 219 "go," (168.46), idx 172 "go" (145.72-145.74).
n0 = len(words)
words = [w for w in words if w["end"] - w["start"] >= 0.03]
print(f"dropped {n0 - len(words)} zero-duration artifact words")

# --- lyric lines: (id, preset, [word indices by time range]) ---
# Lines are selected by start-time window; the S12b block is built from the
# take's warped words instead (see below).
LINE_DEFS = [
    # Long HIGHLIGHT/CASCADE lines are split into phrase sub-lines: at
    # fontsize 54 a line wider than ~44 chars runs off the 1280px frame
    # (char advance ~28px). SLAM lines need no split (each word alone,
    # centered). STACK lines are short by construction.
    ("L1a", "HIGHLIGHT", 14.18, 17.00),    # S02 "The crowd is moving slow,"
    ("L1b", "HIGHLIGHT", 17.12, 18.72),    # S02 "the stage is far away,"
    ("L1c", "HIGHLIGHT", 18.82, 20.38),    # S02 "need to go so bad"
    ("L2", "SLAM", 20.90, 27.00),          # S03 "Hold it" hook
    ("L3", "SLAM", 29.02, 36.34),          # S04a hook block 1
    ("L4", "SLAM", 36.34, 45.24),          # S04b hook block 2 (tail "it," ends 45.24)
    ("L5", "CASCADE", 45.24, 52.00),       # S05 "Hold it" chant
    ("L6", "CASCADE", 63.96, 66.28),       # S06 pickup chant
    ("L7a", "HIGHLIGHT", 66.28, 67.80),    # S07 "Door is open now,"
    ("L7b", "HIGHLIGHT", 68.02, 69.48),    # S07 "step inside the box,"
    ("L7c", "HIGHLIGHT", 69.52, 70.80),    # S07 "the heat and smell is thick"
    ("L8", "SLAM", 73.10, 78.16),          # S08a "Lock"
    ("L9", "HIGHLIGHT", 78.16, 85.28),     # S08b "Inside the porta"
    ("L10", "SLAM", 86.80, 94.10),         # S09a hook (tail "it" ends 94.10)
    ("L11", "SLAM", 94.10, 102.16),        # S09b hook (tail "it" ends 102.16)
    ("L12a", "STACK", 102.16, 103.88),     # S10 list 1 "Four squares left"
    ("L12b", "STACK", 104.14, 105.98),     # S10 list 2 "QR code on the phone"
    ("L12c", "STACK", 106.04, 107.26),     # S10 list 3 "Pay the ninety nine"
    ("L13a", "HIGHLIGHT", 109.36, 111.08), # S11 "Soap and water free,"
    ("L13b", "HIGHLIGHT", 111.28, 112.90), # S11 "outside by the fence,"
    ("L13c", "HIGHLIGHT", 113.00, 114.74), # S11 "Addicts standing near,"
    ("L13d", "HIGHLIGHT", 114.74, 115.76), # S11 "outside"
    ("L14", "SLAM", 120.86, 129.98),       # S12a final chorus block 1
    ("L15", "HIGHLIGHT", 129.98, 134.42),  # S12 gap: held "need"
    # L16 (S12b) built from the take below
    ("L17a", "HIGHLIGHT", 145.74, 147.00), # S13a "Pull the party light,"
    ("L17b", "HIGHLIGHT", 147.18, 149.04), # S13a "gotta hold it, hold it,"
    ("L17c", "HIGHLIGHT", 149.06, 150.56), # S13a "hold it, hold it"
    ("L18a", "CASCADE", 150.56, 152.48),   # S13b run "Need to go, need to go,"
    ("L18b", "CASCADE", 152.74, 154.68),   # S13b run "Festival porta potty,"
    ("L18c", "CASCADE", 154.74, 158.20),   # S13b run "hold it" x4
    ("L19a", "STACK", 158.20, 159.46),     # S14 list 1
    ("L19b", "STACK", 159.46, 160.88),     # S14 list 2
    ("L19c", "STACK", 160.88, 164.90),     # S14 list 3
    ("L20a", "HIGHLIGHT", 164.90, 168.46), # S14 tail "Need to go, need"
    ("L20b", "HIGHLIGHT", 168.46, 172.68), # S14 tail "hold it, hold it, hold it"
    ("L21", "HIGHLIGHT", 178.64, 182.34),  # S15 outro "Need to go, hold it"
]

lines = []
for lid, preset, a, b in LINE_DEFS:
    ln = [w for w in words if a - 1e-9 <= w["start"] < b - 1e-9]
    assert ln, f"{lid}: no words in {a}-{b}"
    lines.append((lid, preset, ln))
    print(f"  {lid} {preset:9} {ln[0]['start']:.2f}-{max(w['end'] for w in ln):.2f} "
          f"n={len(ln)} {' '.join(w['word'] for w in ln)[:56]}")

# L16: S12b take's warped word times (ASR collapsed this block).
take12b = json.load(open(f"{BASE}/work/qc/s12b-t2/words.json"))
F = 271 / 24 / 7.02  # song span 271f / take span 7.02s
l16 = [{"word": ("Need" if w["w"].lower().startswith("need") else
                 "to" if w["w"].lower().startswith("to") else "go,"),
        "start": 134.42 + w["s"] * F, "end": 134.42 + w["e"] * F}
       for w in take12b]
lines.append(("L16", "SLAM", l16))
print(f"  L16 SLAM      {l16[0]['start']:.2f}-{l16[-1]['end']:.2f} n={len(l16)} "
      f"(take-warped; ASR collapsed this block)")

# sort lines by start (L16 slots between L15 and L17)
lines.sort(key=lambda t: t[2][0]["start"])
# L6 pickup chant: the ASR merged its opening "Hold" into the idx-65 artifact
# (dropped above), so the line starts with "it," — reconstruct the opening
# "Hold" at 63.70-63.96 (ends where "it," starts). Disclosed reconstruction.
for lid, preset, ln in lines:
    if lid == "L6":
        ln.insert(0, {"word": "Hold", "start": 63.70, "end": 63.96})
# Capitalize the first word of each line (caption practice; ASR case varies
# between "Hold" and "hold" mid-chant).
for lid, preset, ln in lines:
    ln[0]["word"] = ln[0]["word"][:1].upper() + ln[0]["word"][1:]
# drop the ASR's broken block-2 words (idx 171 "to" 134.42-145.72, idx 172 "go"
# 145.72-145.74) from the SONG-word lines — they are not in any LINE_DEF window
# (L16 covers 134.42-145.72 from the take), but verify none leaked in.
for lid, preset, ln in lines:
    for w in ln:
        assert not (w["word"] == "to" and abs(w["start"] - 134.42) < 0.01
                    and w["end"] - w["start"] > 5), f"broken ASR word leaked into {lid}"

a = Ass(1280, 720, "Noto Sans", 54)
for li, (lid, preset, ln) in enumerate(lines):
    nxt = lines[li + 1][2][0]["start"] if li + 1 < len(lines) else None
    emit_line(a, ln, preset, li, True, nxt)

# corner bug "~ WuBu ~" bottom-right, full duration (MV-8 v1 form verbatim)
a.add(0, 0.00, 184.00, "Bone",
      "{\\an3\\pos(1252,692)\\fs22\\alpha&H80&}~ WuBu ~")

with open(OUT, "w") as f:
    f.write(a.header())
    f.write("\n".join(a.events) + "\n")

n_words = sum(len(ln) for _, _, ln in lines)
print(f"{OUT}: {len(lines)} lyric lines, {n_words} words, {len(a.events)} events")
