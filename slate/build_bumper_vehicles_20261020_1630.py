#!/usr/bin/env python3
"""Build durable v1 fire vehicles for the Q2 2026-10-20 1630 EDT stall-queue run.

Stall-queue banking: NO video API calls (budget outage opened 2026-10-20 ~13:37 EDT
persists; the 14:52 refusal's developer instruction forbids any further video
request now; a 429 is a hard stop). These vehicles are the durable resume queue.

1515-format UNC drafts (B-2636/B-2638): verbatim PREPRO extracts, Source paragraph
stripped (it sits before "Hand-painted"), hardened citation-token strip
(colon-class (B-45: prose) unwrapped keeping 6-tile QC prose via regex; backstop
kills any remaining (X-NNN...) form), the native anti-underline-bar stack asserted
verbatim exactly 2x (SUBJECTS + LOAD-BEARING — no strengthening pass), 0815 BUG
anti-leak clause appended. Zero citation tokens asserted on both.

1515 hands-only format (B-2637): verbatim extract, Source stripped, same token
strip, NEGATIVE's "no underline bar anywhere" kept VERBATIM 1x per the 1445/1545
hands-only precedent (no wordmark in frame, no 2x stack), BUG clause appended.
Zero citation tokens asserted.
"""
import re, hashlib

SLATE = "/home/hatch/workspace/wubutv-network/slate"

BUG = (" BUG-CLASS INSTRUCTION-SET HYGIENE: the generated take carries only the scene itself"
       " \u2014 no production-slate overlays, no version tokens, no number tokens, no meta-text"
       " describing the bug's spelling, no spelling-out of the tilde instruction as words;"
       " the corner bug renders as plain text only.")

STRONG = "ABSOLUTELY NO BAR, LINE, OR STRIPE"
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

def finish_unc(text, out):
    n = text.count(STRONG)
    assert n == 2, f"expected native 2x bar stack in {out}, found {n}"
    assert HANDS_BAR not in text, f"unexpected hands-only bar wording in {out}"
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

def finish_hands(text, out):
    # Hands-only: 1x NEGATIVE bar wording verbatim, no strengthening pass.
    n = text.count(HANDS_BAR)
    assert n == 1, f"expected exactly 1x hands-only bar wording in {out}, found {n}"
    assert STRONG not in text, f"unexpected strong bar stack in {out}"
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

# --- B-1334 <- 1515 B-2636 "The Bled Valve" (UNC draft, boiler house, line "Bled.") ---
t = extract("PREPRO_2026-10-20_1515.md", 56, 64)
t = strip_tokens(t)
finish_unc(t, "fire_b1334_20261020_1630_v1.txt")

# --- B-1335 <- 1515 B-2637 "The Collated Stack" (hands-only, copy room, line "One stack.") ---
t = extract("PREPRO_2026-10-20_1515.md", 64, 72)
t = strip_tokens(t)
finish_hands(t, "fire_b1335_20261020_1630_v1.txt")

# --- B-1336 <- 1515 B-2638 "The Lit Buoy" (UNC draft, buoy store, line "The channel is lit.") ---
t = extract("PREPRO_2026-10-20_1515.md", 72, 80)
t = strip_tokens(t)
finish_unc(t, "fire_b1336_20261020_1630_v1.txt")

print("done \u2014 all vehicles TEXT-ONLY, zero citation tokens, UNC 2x bar stack / hands-only 1x verbatim")
