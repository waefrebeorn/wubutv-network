#!/usr/bin/env python3
"""Build the MV-7 mouth-state gate onset list.
Sources: LYRIC_TIMELINE.md line table + cutlist segment starts (1:1 with
lines, except S01b and S24-P2 which each hold 2 chant occurrences).
Scored = sung-picture phrase onsets (segment starts + 2 mid-segment hook
occurrences). COVER = montage/plate-covered line onsets (no mouth expected).
"""
import json
# (label, song_start, text, kind) kind: sing | cover ; hook = text has Nobody Man
LINES = [
    # intro chant: segment starts are the occurrence onsets
    ("I-occ1", 0.00, "I'm The Nobody Man", "sing"),
    ("I-occ2", 2.28, "I'm The Nobody Man", "sing"),
    ("I-occ3", 4.14, "I'm The Nobody Man", "sing"),
    ("I-occ4", 6.90, "I'm The Nobody Man", "sing"),
    ("I-occ5", 8.41, "I'm The Nobody Man (mid-S01b)", "sing"),
    ("I-occ6", 9.92, "I'm The Nobody Man", "sing"),
    ("I-occ7", 14.30, "I'm The Nobody Man", "sing"),
    ("V1.1", 19.58, "I got a profile, got a pile", "sing"),
    ("V1.2", 22.60, "Got a thousand posts in a folder file", "sing"),
    ("V1.3", 24.62, "Old meme face and a busted grin", "sing"),
    ("V1.4", 26.82, "Been here so long, I could sign back in", "sing"),
    ("V1.5", 29.42, "Made a joke at a quarter past eight", "sing"),
    ("V1.6", 31.74, "Watched it sit there while I wait", "sing"),
    ("PC1.1", 34.02, "I kept clicking, kept sticking around", "sing"),
    ("PC1.2", 36.50, "Little by little, I learned the sound", "sing"),
    ("PC1.3", 38.60, "Nobody noticing? Fine by me", "sing"),
    ("PC1.4", 42.90, "I built my kingdom quietly", "sing"),
    ("C1.1", 47.02, "I'm The Nobody Man", "sing"),
    ("C1.2", 49.40, "Still here, still stand", "sing"),
    ("C1.3", 51.76, "I post, I fade, I post again", "sing"),
    ("C1.4", 53.82, "I'm The Nobody Man", "sing"),
    ("C1.5", 56.18, "I got a thousand little sparks", "sing"),
    ("C1.6", 59.34, "Flicking in the dark", "sing"),
    ("C1.7", 61.46, "I'm The Nobody Man", "sing"),
    ("C1.8a", 63.72, "Nobody Man", "sing"),
    ("C1.8b", 66.26, "Nobody Man", "sing"),
    ("C1.T1", 67.80, "Nobody Man", "sing"),
    ("C1.T2", 70.48, "Nobody Man", "sing"),
    ("C1.T3", 73.16, "Nobody Man", "sing"),
    ("V2.1", 75.84, "I got drafts in the drawer like coins", "sing"),
    ("V2.2", 78.50, "Half-mad thoughts and a stack of joins", "sing"),
    ("V2.3", 80.58, "Tiny wins in a low-lit room", "sing"),
    ("V2.4", 82.94, "One more clip and one more zoom", "sing"),
    ("V2.5", 85.18, "Everybody chasing that giant shout", "sing"),
    ("V2.6", 87.66, "I got a small flame I won't put out", "sing"),
    ("PC2.1", 89.92, "I kept clicking, kept sticking around", "sing"),
    ("PC2.2", 93.08, "Little by little, I learned the sound", "sing"),
    ("PC2.3", 95.20, "No one crowned me, no one had to", "sing"),
    ("PC2.4", 99.82, "I made this mess on purpose too", "sing"),
    ("C2.1", 103.36, "I'm The Nobody Man", "sing"),
    ("C2.2", 105.50, "Still here, still stand", "sing"),
    ("C2.3", 108.28, "I post, I fade, I post again", "sing"),
    ("C2.4", 110.36, "I'm The Nobody Man", "cover"),
    ("C2.5", 112.86, "I got a thousand little sparks", "sing"),
    ("C2.6", 115.42, "Flicking in the dark", "sing"),
    ("C2.7", 117.86, "I'm The Nobody Man", "sing"),
    ("C2.8", 120.32, "Nobody Man", "sing"),
    ("B.1", 123.26, "Call me lost, call me late", "cover"),
    ("B.2", 126.46, "Call me anything you wanna say", "cover"),
    ("B.3", 128.10, "I got roots in the endless feed", "cover"),
    ("B.4", 130.46, "And every scar is a saved receipt", "cover"),
    ("B.5", 132.58, "If fame won't call, then let it pass", "cover"),
    ("B.6", 137.02, "I'm the joke that lasts and lasts", "cover"),
    ("FC.1", 143.40, "I'm The Nobody Man", "sing"),
    ("FC.2", 145.52, "Still here, still stand", "sing"),
    ("FC.3", 148.24, "I post, I fade, I post again", "sing"),
    ("FC.4", 150.38, "I'm The Nobody Man", "cover"),
    ("FC.5", 152.88, "I got a thousand little sparks", "sing"),
    ("FC.6", 155.40, "Flicking in the dark", "sing"),
    ("FC.7", 157.84, "I'm The Nobody Man", "sing"),
    ("FC.8", 160.02, "Nobody Man", "sing"),
    ("FC.9", 164.16, "I'm The Nobody Man", "sing"),
    ("FC.10", 168.16, "Yeah, I turn the small things grand", "sing"),
    ("FC.T1", 173.30, "I'm (tag chant)", "sing"),
    ("FC.T2", 176.26, "Nobody Man", "sing"),
    ("FC.T3", 179.75, "Nobody Man (mid-S24-P2)", "sing"),
]
out = []
for label, t, text, kind in LINES:
    out.append({"label": label, "onset": t, "text": text, "kind": kind,
                "hook": "nobody man" in text.lower(),
                "frame": round(t * 24), "frame_plus6": round(t * 24) + 6})
json.dump(out, open("work/gate_final/onsets.json", "w"), indent=1)
scored = [o for o in out if o["kind"] == "sing"]
hooks = [o for o in scored if o["hook"]]
covers = [o for o in out if o["kind"] == "cover"]
print(f"total {len(out)} | scored {len(scored)} | hooks {len(hooks)} | cover {len(covers)}")
