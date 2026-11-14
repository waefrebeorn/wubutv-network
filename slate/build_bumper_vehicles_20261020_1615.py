#!/usr/bin/env python3
"""Build durable v1 fire vehicles for the Q2 2026-10-20 1615 EDT stall-queue run.

Stall-queue banking: NO video API calls (budget outage opened 2026-10-20 ~13:37 EDT
persists; the 14:52 refusal's developer instruction forbids any further video
request now; a 429 is a hard stop). These vehicles are the durable resume queue.

1515 hands-only format (B-2633/B-2634/B-2635): verbatim PREPRO extracts, Source
paragraph stripped (it sits before "Hand-painted"), hardened citation-token strip
(colon-class (B-45: prose) unwrapped keeping 6-tile QC prose via regex; backstop
kills any remaining (X-NNN...) form), NEGATIVE's "no underline bar anywhere" kept
VERBATIM 1x per the 1445/1545 hands-only precedent (no wordmark in frame, so no
2x SUBJECTS+NEGATIVE bar stack — that stack is for UNC drafts only), 0815 BUG
anti-leak clause appended. Zero citation tokens asserted on all three.
"""
import re, hashlib

SLATE = "/home/hatch/workspace/wubutv-network/slate"

BUG = (" BUG-CLASS INSTRUCTION-SET HYGIENE: the generated take carries only the scene itself"
       " \u2014 no production-slate overlays, no version tokens, no number tokens, no meta-text"
       " describing the bug's spelling, no spelling-out of the tilde instruction as words;"
       " the corner bug renders as plain text only.")

HANDS_BAR = "no underline bar anywhere"

def extract(prepro, start, end):
    """Pull the draft section lines [start, end) and keep from 'Hand-painted' on."""
    with open(f"{SLATE}/{prepro}") as f:
        lines = f.readlines()
    text = "".join(lines[start - 1:end - 1]).strip()
    idx = text.index("Hand-painted 2D cartoon")
    return text[idx:].strip()

def strip_tokens(text):
    # Colon-class: unwrap, keep the inner QC prose (regex handles varying prose)
    text = re.sub(r"\(B-45: (.*?) \u2014 cluster-diff, never scalar\)", r"\1", text)
    # Backstop: any remaining (X-NNN...) token form
    text = re.sub(r"\([A-Za-z]+-\d+[^)]*\)", "", text)
    text = re.sub(r"  +", " ", text)
    return text

def finish(text, out):
    # Hands-only: 1x NEGATIVE bar wording verbatim, no strengthening pass.
    n = text.count(HANDS_BAR)
    assert n == 1, f"expected exactly 1x hands-only bar wording in {out}, found {n}"
    assert "ABSOLUTELY NO BAR" not in text, f"unexpected strong bar stack in {out}"
    assert not re.search(r"\([A-Za-z]+-\d+", text), f"citation token leak in {out}"
    text = text.rstrip()
    if not text.endswith("."):
        text += "."
    text += BUG
    with open(f"{SLATE}/{out}", "w") as f:
        f.write(text)
    md5 = hashlib.md5(text.encode()).hexdigest()
    print(f"{out}: md5 {md5}, {len(text.encode())} bytes")
    return md5

# --- B-1331 <- 1515 B-2633 "The Hooped Barrel" (hands-only, off-screen voice line "It holds water.") ---
t = extract("PREPRO_2026-10-20_1515.md", 32, 40)
t = strip_tokens(t)
finish(t, "fire_b1331_20261020_1615_v1.txt")

# --- B-1332 <- 1515 B-2634 "The Tray Up" (hands-only, NO-LINE) ---
t = extract("PREPRO_2026-10-20_1515.md", 40, 48)
t = strip_tokens(t)
finish(t, "fire_b1332_20261020_1615_v1.txt")

# --- B-1333 <- 1515 B-2635 "The Gathered Blob" (hands-only, off-screen voice line "Still molten.") ---
t = extract("PREPRO_2026-10-20_1515.md", 48, 56)
t = strip_tokens(t)
finish(t, "fire_b1333_20261020_1615_v1.txt")

print("done \u2014 all vehicles TEXT-ONLY, zero citation tokens, hands-only 1x bar wording verbatim")
