#!/usr/bin/env python3
"""Intake match v3: lyrics.txt + SONG_WORDS.json -> LYRIC_TIMELINE.md +
work/lyrics_debug.json.
- Pass 1 (anchors): lyric lines with >=5 tokens that match the ASR stream
  at >=0.98 in exactly ONE place become fixed anchors (monotone chain).
- Pass 2: remaining lines matched sequentially inside each inter-anchor
  span (contraction-expanded tokens, earliest-good candidate preference,
  20s capped search with 0.5 threshold, uncapped fallback with 35s jump
  rejection, adjacent sheet-duplicates share the sung span).
Usage: intake_match.py PROJ [extra uncertainty note ...]
"""
import json, os, re, sys

PROJ = sys.argv[1]
WORK = os.path.join(PROJ, "work")

EXPAND = {"i'm": ["i", "am"], "it's": ["it", "is"], "don't": ["do", "not"],
          "can't": ["can", "not"], "won't": ["will", "not"],
          "i'll": ["i", "will"], "you're": ["you", "are"],
          "we're": ["we", "are"], "that's": ["that", "is"],
          "there's": ["there", "is"], "let's": ["let", "us"],
          "didn't": ["did", "not"], "doesn't": ["does", "not"],
          "isn't": ["is", "not"], "wasn't": ["was", "not"],
          "couldn't": ["could", "not"], "shouldn't": ["should", "not"],
          "i've": ["i", "have"], "we've": ["we", "have"],
          "you've": ["you", "have"], "i'd": ["i", "would"],
          "you'll": ["you", "will"], "he's": ["he", "is"],
          "she's": ["she", "is"], "what's": ["what", "is"],
          "gonna": ["going", "to"], "wanna": ["want", "to"],
          "gotta": ["got", "to"], "ain't": ["is", "not"]}

def norm(s):
    s = s.lower().replace("’", "'").replace("‘", "'")
    s = re.sub(r"[^a-z0-9' ]", " ", s)
    return re.sub(r"\s+", " ", s).strip()

def expand(tok):
    if tok in EXPAND:
        return EXPAND[tok]
    if tok.endswith("'s") and len(tok) > 2:
        return [tok[:-2], "is"]
    return [tok]

def tok_eq(a, b):
    if a == b:
        return True
    if len(a) > 3 and len(b) > 3 and a.rstrip("s") == b.rstrip("s"):
        return True
    if min(len(a), len(b)) >= 4 and (a.startswith(b) or b.startswith(a)):
        return True
    # 1-char suffix tolerance: 'bout~about
    return (abs(len(a) - len(b)) == 1 and min(len(a), len(b)) >= 4
            and (a.endswith(b) or b.endswith(a)))

with open(os.path.join(PROJ, "lyrics.txt")) as f:
    raw_lines = [ln.rstrip("\n") for ln in f if ln.strip()]
with open(os.path.join(PROJ, "SONG_WORDS.json")) as f:
    asr = json.load(f)

asr_toks, asr_tok_widx = [], []
for wi, w in enumerate(asr):
    base = norm(w["word"]).replace(" ", "")
    for t in expand(base):
        asr_toks.append(t.replace("'", ""))
        asr_tok_widx.append(wi)
NTOK = len(asr_toks)

def line_tokens(text):
    text = re.sub(r"\[[^\]]*\]", " ", text)  # per-line performance cues
    text = re.sub(r"^\s*\([^)]*\)\s*", "", text)  # leading (Ad-lib:...) cue
    out = []
    for t in norm(text).split():
        for x in expand(t):
            out.append(x.replace("'", ""))
    return out

def walk_score(cand, lt, hi):
    """Align line tokens against the ASR stream from cand, allowing up to
    2 inserted ASR tokens before each line token (ad-libs, echoes)."""
    matches, j = 0, cand
    for t in lt:
        hit = -1
        for k in (0, 1, 2):
            if j + k < hi and tok_eq(asr_toks[j + k], t):
                hit = k
                break
        if hit >= 0:
            matches += 1
            j += hit + 1
    score = matches / len(lt)
    consumed = j - cand
    if consumed > len(lt) + 4:  # too spread out to be this line
        score *= 0.85
    return score, j - 1

def search(p, lt, time_cap, thresh=0.6, hi=None):
    """Earliest >=0.85 wins; else earliest >= thresh, upgradeable to a
    >=0.85 candidate starting within 8s after it."""
    hi = NTOK if hi is None else hi
    near, chosen = None, None
    for cand in range(p, min(p + 150, hi)):
        if not tok_eq(asr_toks[cand], lt[0]):
            continue
        cstart = asr[asr_tok_widx[cand]]["start"]
        if time_cap is not None and cstart > time_cap:
            continue
        score, eidx = walk_score(cand, lt, hi)
        if score >= 0.85:
            if near is None:
                chosen = (score, cand, eidx)
            else:
                nstart = asr[asr_tok_widx[near[1]]]["start"]
                chosen = (score, cand, eidx) if cstart <= nstart + 4 else near
            break
        if near is None and score >= thresh:
            near = (score, cand, eidx)
    return chosen or near

lines = []
for ln in raw_lines:
    if re.match(r"^\s*\[.*\]\s*$", ln):
        lines.append({"kind": "tag", "text": ln.strip()})
    else:
        lines.append({"kind": "lyric", "text": ln,
                      "toks": line_tokens(ln)})

# ---- pass 1: anchors
anchors = {}  # line index -> (sidx, eidx)
last_eidx = -1
n_lyric = sum(1 for l in lines if l["kind"] == "lyric")
lyric_no = -1
for i, l in enumerate(lines):
    if l["kind"] != "lyric":
        continue
    lyric_no += 1
    if len(l["toks"]) < 5:
        continue
    hits = []
    for cand in range(NTOK):
        if not tok_eq(asr_toks[cand], l["toks"][0]):
            continue
        score, eidx = walk_score(cand, l["toks"], NTOK)
        if score >= 0.98:
            hits.append((cand, eidx))
    if len(hits) == 1 and hits[0][0] > last_eidx:
        # position plausibility: a unique hit belonging to a later repeat
        # (ASR garbled the first pass) must not anchor this line
        expected = (lyric_no / max(n_lyric, 1)) * NTOK
        center = (hits[0][0] + hits[0][1]) / 2
        if abs(center - expected) <= 0.35 * NTOK:
            anchors[i] = hits[0]
            last_eidx = hits[0][1]

# ---- pass 2: sequential matching inside spans
results = [None] * len(lines)
for i, l in enumerate(lines):
    if l["kind"] == "tag":
        results[i] = {**l, "match": "section", "start": None, "end": None}
    elif i in anchors:
        sidx, eidx = anchors[i]
        results[i] = {**l, "match": "confirmed",
                      "start": asr[asr_tok_widx[sidx]]["start"],
                      "end": asr[asr_tok_widx[eidx]]["end"]}
uncertain = list(sys.argv[2:])

spans = []
prev_anchor_line, prev_anchor_eidx = -1, -1
for i in sorted(anchors) + [len(lines)]:
    spans.append((prev_anchor_line + 1, i,
                  prev_anchor_eidx + 1,
                  anchors[i][0] if i in anchors else NTOK,
                  asr[asr_tok_widx[anchors[prev_anchor_line][1]]]["end"]
                  if prev_anchor_line in anchors else None))
    if i in anchors:
        prev_anchor_line, prev_anchor_eidx = i, anchors[i][1]

for lo_line, hi_line, tok_lo, tok_hi, start_prev_end in spans:
    p, prev_end, prev_text = tok_lo, start_prev_end, None
    if lo_line > 0 and lines[lo_line - 1]["kind"] == "lyric":
        prev_text = norm(lines[lo_line - 1]["text"])
    for i in range(lo_line, hi_line):
        l = lines[i]
        if l["kind"] != "lyric":
            continue
        lt = l["toks"]
        if not lt:  # fragment line with no words ('...', '!')
            results[i] = {**l, "match": "unmatched", "start": None, "end": None}
            prev_text = norm(l["text"])
            continue
        is_dup = prev_text is not None and norm(l["text"]) == prev_text
        if is_dup and prev_end is not None:
            pick = search(p, lt, prev_end + 8, hi=tok_hi)
            if pick is None and results[i - 1]["start"] is not None:
                prev = results[i - 1]
                results[i] = {**l, "match": "inferred",
                              "start": prev["start"], "end": prev["end"]}
                uncertain.append(
                    f"Sheet repeat sung as one phrase (shares previous "
                    f"line's span): '{l['text']}'")
                prev_text = norm(l["text"])
                continue
            if pick is None:
                results[i] = {**l, "match": "unmatched",
                              "start": None, "end": None}
                prev_text = norm(l["text"])
                continue
        else:
            pick = None
            if prev_end is not None:
                pick = search(p, lt, prev_end + 20, thresh=0.5, hi=tok_hi)
            if pick is None:
                pick = search(p, lt, None, hi=tok_hi)
                if pick is not None and prev_end is not None:
                    far = asr[asr_tok_widx[pick[1]]]["start"] - prev_end
                    if far > 20 and tok_hi >= NTOK:
                        pick = None  # unbounded span: a jump poisons the tail
                    else:
                        pick = (min(pick[0], 0.84), pick[1], pick[2])
        if pick:
            score, sidx, eidx = pick
            sw, ew = asr[asr_tok_widx[sidx]], asr[asr_tok_widx[eidx]]
            results[i] = {**l,
                          "match": "confirmed" if score >= 0.999 else "inferred",
                          "start": sw["start"], "end": ew["end"]}
            p = eidx + 1
            prev_end = ew["end"]
        else:
            results[i] = {**l, "match": "unmatched", "start": None, "end": None}
        prev_text = norm(l["text"])

for r in results:
    if r["kind"] == "lyric" and r["match"] == "unmatched":
        uncertain.append(f"UNMATCHED in ASR: '{r['text']}'")
for idx, r in enumerate(results):
    if r["kind"] == "tag":
        for r2 in results[idx + 1:]:
            if r2["kind"] == "lyric" and r2["start"] is not None:
                r["start"] = r2["start"]
                break

title = os.path.basename(PROJ)
with open(os.path.join(PROJ, "LYRIC_TIMELINE.md"), "w") as f:
    f.write(f"# {title} — LYRIC TIMELINE (measured, large-v3-turbo full-clip, "
            f"NO VAD; line text from burned-in lyric OCR)\n\n")
    f.write("| L | Section | Start | End | Match | Line |\n|---|---|---|---|---|---|\n")
    sec, n = "", 0
    for r in results:
        if r["kind"] == "tag":
            sec = r["text"].strip("[]")
            st = f"{r['start']:.2f}" if r["start"] is not None else "—"
            f.write(f"| — | **{sec}** | {st} | — | section | {r['text']} |\n")
            continue
        n += 1
        st = f"{r['start']:.2f}" if r["start"] is not None else "—"
        en = f"{r['end']:.2f}" if r["end"] is not None else "—"
        f.write(f"| L{n:02d} | {sec} | {st} | {en} | {r['match']} | {r['text']} |\n")

with open(os.path.join(WORK, "lyrics_debug.json"), "w") as f:
    json.dump({"lines": [{k: v for k, v in r.items() if k != "toks"}
                         for r in results],
               "uncertain": uncertain}, f, indent=1)
nc = sum(1 for r in results if r.get("match") == "confirmed")
ni = sum(1 for r in results if r.get("match") == "inferred")
nu = sum(1 for r in results if r.get("match") == "unmatched")
print(f"MATCHED {PROJ}: confirmed {nc}, inferred {ni}, unmatched {nu}, "
      f"uncertain {len(uncertain)}", flush=True)
