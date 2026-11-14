#!/usr/bin/env python3
"""MV-8 rebuild Stage 1 adjudication: medium (Pass A) + small-prompted (Pass B2)
+ v1 small (SONG_WORDS.json) + tiny -> canonical SONG_WORDS_v2.json.

Rules applied (see LYRIC_TIMELINE_v2.md for the full reasoning):
- Base = medium, unprompted, beam 5 (strongest model, cleanest timing).
- Medium's systematic "White" -> "Wipe" mishear corrected wherever the line
  is the hook ("White and you're still there" / "Endless white forever").
  B2 + v1 both hear "Wipe" at those spots; "White" makes no lyric sense.
- Medium's "Fence" -> "Phantom" (sheet lines "Phantom residue stays" /
  "Phantom wiper never stops"; both passes garble the head word, tails solid).
- Zero-duration words dropped (ASR boundary artifacts).
- Everything after 146.02 dropped: Outro is instrumental. Medium's 157-183
  spans are zero-duration pile-ups with p~0.00; B2's "Turn it. Turn it.
  Brown brown." at 157.72-159.46 is the same artifact class; v1's Outro
  "I'm gonna" loop is a known hallucination. Sheet's Outro "Brown" is
  sheet-only, no performed witness with credible timing.
- L1 onset 7.98 (B2 + tiny agree; medium 8.52 p=0.36 is the outlier).
- Verse onset 60.46 (v1; medium 60.64, "Sitting" p=0.02).
- Drop shout "Wipe" 105.94-106.36 added from v1 (single witness, p=0.43).
- Hook-2 fragment 81.66-83.74 added from v1, identity-corrected to the hook
  line (v1's "Wipe in the stool" is its known "and it's still" mishear).
  CONTESTED: sheet+B2 say "Brown brown (Still brown)" here; B2 probs ~0.00
  (prompt echo), medium hears silence. v1's high-prob hook words win.
- Performed variant kept as medium heard it: later hooks sing "you're"
  ("Wipe and you're still there", medium p 0.87-0.99 at 87.16/125.46/140.72)
  vs sheet "it's". B2's "it's" at 125.28 is prompt-biased. Flagged in timeline.
"""
import json

R = "work/rebuild/"
med = json.load(open(R + "SONG_WORDS_v2_medium.json"))["words"]
v1 = json.load(open("SONG_WORDS.json"))["words"]

words = []
for w in med:
    s, e, txt, p = float(w["start"]), float(w["end"]), w["word"], float(w.get("prob", 0))
    if e <= 146.02 or s < 146.02:
        pass
    if s >= 146.02:
        continue  # Outro junk spans dropped
    if e - s == 0:
        continue  # zero-duration boundary artifact
    # systematic corrections
    if txt in ("White", "white"):
        txt = "Wipe" if txt == "White" else "wipe"
    if txt == "Fence":
        txt = "Phantom"
    if txt == "on," and 66.0 < s < 66.5:
        continue  # garble fragment of the "(Phantom)" backing tag
    words.append({"word": txt, "start": round(s, 2), "end": round(e, 2),
                  "prob": round(p, 2), "source": "medium"})

# L1 onset: B2 + tiny say 7.98, medium says 8.52 (p=0.36)
for w in words:
    if w["word"] == "Wipe" and abs(w["start"] - 8.52) < 0.01:
        w["start"] = 7.98
        w["source"] = "adjudicated(B2+tiny)"
        break
# Verse onset: v1 60.46
for w in words:
    if w["word"] == "Sitting":
        w["start"] = 60.46
        w["source"] = "adjudicated(v1)"
        break

# Drop shout (v1 only)
words.append({"word": "Wipe", "start": 105.94, "end": 106.36,
              "prob": 0.43, "source": "v1-only"})
# Hook-2 fragment 81.66-83.74 (v1 only, identity-corrected)
for txt, s, e, p in (("Wipe", 81.66, 82.48, 0.86), ("and", 82.48, 83.30, 0.89),
                     ("it's", 83.30, 83.74, 0.98), ("still", 83.74, 83.74, 0.99)):
    words.append({"word": txt, "start": s, "end": e, "prob": p,
                  "source": "v1-only-corrected"})

words.sort(key=lambda w: (w["start"], w["end"]))
out = {"track": "track.mp4 md5 8a4834d2e647fffce6782a3461baa936, 187.2s",
       "method": "faster-whisper medium (Pass A, no prompt, no VAD, beam 5) as base; "
                 "small+sheet-prompt (Pass B2) and v1 small as witnesses; "
                 "tiny corroboration for Hook 1 onset. See LYRIC_TIMELINE_v2.md.",
       "words": words}
json.dump(out, open(R + "SONG_WORDS_v2.json", "w"), indent=1)
print("canonical words:", len(words))
print("span: %.2f - %.2f" % (words[0]["start"], words[-1]["end"]))
# line spans for the timeline doc
for w in words:
    print(f"{w['start']:7.2f}-{w['end']:7.2f}  {w['word']:10s} p={w['prob']:.2f} {w['source']}")
