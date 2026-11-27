#!/usr/bin/env python3
"""MV-29 scenes.json: windows from MV_PREPRO_MV-29.md, frames =
cumulative partition of 4445 (round(185.216*24)) at 24fps."""
import json, os

P = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
WINS = [
 (1, 0.00, 3.52, "INTRO", "L01-L02", "SINGING"),
 (2, 3.52, 10.08, "CHORUS 1", "L03-L04", "SINGING"),
 (3, 10.08, 16.98, "CHORUS 1", "L05-L06", "SINGING"),
 (4, 16.98, 25.28, "CHORUS 1", "L07-L08", "COVER"),
 (5, 25.28, 32.80, "ECHO GAP", "wordless", "CUTAWAY"),
 (6, 32.80, 40.48, "VERSE 1", "L09-L10", "SINGING"),
 (7, 40.48, 47.82, "VERSE 1", "L11-L12", "SINGING"),
 (8, 47.82, 57.36, "PRE-CHORUS 1", "L13-L14", "SINGING"),
 (9, 57.36, 66.00, "CHORUS 2", "L15-L16", "SINGING"),
 (10, 66.00, 73.86, "CHORUS 2", "L17-L18", "SINGING"),
 (11, 73.86, 82.42, "CHORUS 2", "L19-L20", "SINGING"),
 (12, 82.42, 86.12, "VERSE 2", "L21-L22", "SINGING"),
 (13, 86.12, 90.02, "VERSE 2", "L23-L24", "SINGING"),
 (14, 90.02, 96.66, "PRE-CHORUS 2", "L25-L26", "SINGING"),
 (15, 96.66, 102.08, "GAP", "wordless", "CUTAWAY"),
 (16, 102.08, 109.18, "CHORUS 3", "L27-L28", "SINGING"),
 (17, 109.18, 116.98, "CHORUS 3", "L29-L30", "SINGING"),
 (18, 116.98, 127.36, "CHORUS 3", "L31-L32", "SINGING"),
 (19, 127.36, 135.00, "BREAKDOWN", "L33-L35 captions", "CUTAWAY"),
 (20, 135.00, 142.86, "BREAKDOWN", "L36-L38 captions", "CUTAWAY"),
 (21, 142.86, 150.60, "FINAL CHORUS", "L39-L40", "SINGING"),
 (22, 150.60, 158.22, "FINAL CHORUS", "L41-L42", "SINGING"),
 (23, 158.22, 168.56, "FINAL CHORUS", "L43-L44", "SINGING"),
 (24, 168.56, 172.90, "FINAL CHORUS", "L45-L46", "SINGING"),
 (25, 172.90, 185.216, "OUTRO", "L47 chant captions", "CUTAWAY"),
]
TOTAL = 4445
scenes, prev = [], 0
for n, a, b, sec, lines, tag in WINS:
    f1 = TOTAL if n == 25 else round(b * 24)
    scenes.append({"n": n, "win": [a, b], "frames": [prev, f1],
                   "section": sec, "lines": lines, "tag": tag})
    prev = f1
assert prev == TOTAL, prev
json.dump(scenes, open(os.path.join(P, "work/scenes.json"), "w"), indent=1)
print("scenes.json:", len(scenes), "scenes,", TOTAL, "frames")
