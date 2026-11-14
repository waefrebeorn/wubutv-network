#!/usr/bin/env python3
"""Build durable v1 fire vehicles for the Q2 2026-10-20 1515 EDT stall-queue run.

1315/1415-format: verbatim PREPRO extracts, Source paragraph stripped,
hardened citation-token strip (bare (B-NNN) removed; colon-class (B-NNN: prose)
unwrapped keeping the 6-tile QC prose, tail dropped — per the 1500-run
precedent), 0815 BUG anti-leak clause appended, ANTI-UNDERLINE-BAR STACK
exactly 2x (SUBJECTS + NEGATIVE, strengthened wording) per the 1430
double-application fix; hands-only B-2622 keeps its 1x NEGATIVE wording
verbatim per the 1445 hands-only precedent. Zero citation tokens asserted.
"""
import re, hashlib

SLATE = "/home/hatch/workspace/wubutv-network/slate"

BUG = (" BUG-CLASS INSTRUCTION-SET HYGIENE: the generated take carries only the scene itself"
       " \u2014 no production-slate overlays, no version tokens, no number tokens, no meta-text"
       " describing the bug's spelling, no spelling-out of the tilde instruction as words;"
       " the corner bug renders as plain text only.")

# Strengthened underline-bar stack, exactly 2x (SUBJECTS + NEGATIVE)
SUBJ_BAR_OLD = "no underline bar under the wordmark, ever;"
SUBJ_BAR_NEW = ("no underline bar under the wordmark, ever \u2014 ABSOLUTELY NO BAR, LINE, OR STRIPE"
                " of any kind beneath the six glyphs; the bare black fabric runs uninterrupted"
                " directly under the ~WuBu~ glyphs;")
NEG_BAR_OLD = "no underline bar under the wordmark,"
NEG_BAR_NEW = ("no underline bar under the wordmark, ABSOLUTELY NO BAR, LINE, OR STRIPE of any kind"
               " beneath the six glyphs, the bare black fabric running uninterrupted directly"
               " under the ~WuBu~ glyphs,")

def extract(prepro, start, end):
    """Pull the draft section lines [start, end) and keep from 'Hand-painted' on."""
    with open(f"{SLATE}/{prepro}") as f:
        lines = f.readlines()
    text = "".join(lines[start - 1:end - 1]).strip()
    idx = text.index("Hand-painted 2D cartoon")
    return text[idx:].strip()

def strip_tokens(text):
    # Colon-class: unwrap, keep the 6-tile QC prose, drop the tail
    text = text.replace("(B-45: 6-tile the joint at 6s/9.5s \u2014 cluster-diff, never scalar)",
                        "6-tile the joint at 6s/9.5s")
    # Backstop sweep for any other colon-class tokens
    text = re.sub(r"\([BS]-\d+: ", "", text)
    text = re.sub(r" \u2014 cluster-diff, never scalar\)", "", text)
    # Bare tokens removed entirely
    text = re.sub(r"\([BS]-\d+\)", "", text)
    text = re.sub(r"  +", " ", text)
    return text

def strengthen_bar_stack(text):
    text = text.replace(SUBJ_BAR_OLD, SUBJ_BAR_NEW)
    text = text.replace(NEG_BAR_OLD, NEG_BAR_NEW)
    return text

def finish(text, out):
    assert not re.search(r"\([A-Za-z]+-\d+", text), f"citation token leak in {out}"
    text = text.rstrip() + "." + BUG if not text.rstrip().endswith(".") else text.rstrip() + BUG
    # normalize: NEGATIVE ends with a period; BUG clause appended with space
    with open(f"{SLATE}/{out}", "w") as f:
        f.write(text)
    md5 = hashlib.md5(text.encode()).hexdigest()
    print(f"{out}: md5 {md5}, {len(text.encode())} bytes")
    return md5

# --- B-1319 <- 1315 B-2618 "The Folded Front" (UNC draft) ---
t = extract("PREPRO_2026-10-20_1315.md", 102, 108)
t = strip_tokens(t)            # (B-26) removed
t = strengthen_bar_stack(t)    # 2x stack
finish(t, "fire_b1319_20261020_1515_v1.txt")

# --- B-1320 <- 1415 B-2622 "The Clamped Joint" (hands-only, NO-LINE) ---
t = extract("PREPRO_2026-10-20_1415.md", 39, 45)
t = strip_tokens(t)            # (B-79) removed; (B-45: ...) unwrapped, prose kept
finish(t, "fire_b1320_20261020_1515_v1.txt")

# --- B-1321 <- 1415 B-2623 "The Sharpened Pencil" (UNC draft) ---
t = extract("PREPRO_2026-10-20_1415.md", 47, 53)
# reduce the 3x bar-stack to exactly 2x AND unwrap the token in one move
# (must run BEFORE strip_tokens eats the (B-45: ...) wrapper)
t = t.replace("(B-45: 6-tile the point at 6s/9.5s \u2014 cluster-diff, never scalar); no underline bar under the wordmark, ever (SUBJECTS + LOAD-BEARING + NEGATIVE pre-emptive stack)",
              "\u2014 6-tile the point at 6s/9.5s")
t = strip_tokens(t)            # (B-79) removed
t = strengthen_bar_stack(t)    # 2x stack
finish(t, "fire_b1321_20261020_1515_v1.txt")

print("done — all vehicles TEXT-ONLY, zero citation tokens")
