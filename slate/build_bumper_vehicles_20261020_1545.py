#!/usr/bin/env python3
"""Build durable v1 fire vehicles for the Q2 2026-10-20 1545 EDT stall-queue run.

1415-format: verbatim PREPRO extracts, Source paragraph stripped, hardened
citation-token strip (bare (B-NNN) removed; colon-class (B-NNN: prose) unwrapped
keeping the 6-tile QC prose via regex; backstop kills any remaining (X-NNN...)
form), 0815 BUG anti-leak clause appended.
ANTI-UNDERLINE-BAR STACK: UNC drafts (B-2628, B-2629) get exactly 2x
section-scoped (SUBJECTS + NEGATIVE; the 1415 LOAD-BEARING pre-emptive-stack
reminder preserved untouched — the 1430 double-application fix + 1515
substring-overlap section-scoping); the hands-only draft (B-2627) keeps its 1x
NEGATIVE "no underline bar anywhere" verbatim per the 1445 hands-only
precedent (no stack strengthening — 1515 run's B-2622 precedent).
Zero citation tokens asserted.
"""
import re, hashlib

SLATE = "/home/hatch/workspace/wubutv-network/slate"

BUG = (" BUG-CLASS INSTRUCTION-SET HYGIENE: the generated take carries only the scene itself"
       " \u2014 no production-slate overlays, no version tokens, no number tokens, no meta-text"
       " describing the bug's spelling, no spelling-out of the tilde instruction as words;"
       " the corner bug renders as plain text only.")

STRONG = "ABSOLUTELY NO BAR, LINE, OR STRIPE"
SUBJ_BAR_OLD = "no underline bar under the wordmark, ever;"
SUBJ_BAR_NEW = ("no underline bar under the wordmark, ever \u2014 " + STRONG +
                " of any kind beneath the six glyphs; the bare black fabric runs uninterrupted"
                " directly under the ~WuBu~ glyphs;")
NEG_BAR_OLD = "no underline bar under the wordmark,"
NEG_BAR_NEW = ("no underline bar under the wordmark, " + STRONG + " of any kind"
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
    # Colon-class: unwrap, keep the inner QC prose (regex handles varying prose)
    text = re.sub(r"\(B-45: (.*?) \u2014 cluster-diff, never scalar\)", r"\1", text)
    # Backstop: any remaining (X-NNN...) token form (covers (B-79), (B-45: ...), (S-16))
    text = re.sub(r"\([A-Za-z]+-\d+[^)]*\)", "", text)
    text = re.sub(r"  +", " ", text)
    return text

def strengthen_bar_stack(text, out):
    # Section-scope the two replacements to avoid the 1515 substring-overlap artifact.
    # LOAD-BEARING's "(SUBJECTS + LOAD-BEARING + NEGATIVE pre-emptive stack)" reminder
    # is preserved untouched.
    assert "NEGATIVE:" in text, f"no NEGATIVE section in {out}"
    head, neg = text.split("NEGATIVE:", 1)
    assert SUBJ_BAR_OLD in head, f"SUBJECTS bar target missing in {out}"
    head = head.replace(SUBJ_BAR_OLD, SUBJ_BAR_NEW)
    assert NEG_BAR_OLD in neg, f"NEGATIVE bar target missing in {out}"
    neg = neg.replace(NEG_BAR_OLD, NEG_BAR_NEW)
    text = head + "NEGATIVE:" + neg
    n = text.count(STRONG)
    assert n == 2, f"expected exactly 2x bar stack in {out}, found {n}"
    return text

def finish(text, out, stack):
    if stack:
        text = strengthen_bar_stack(text, out)
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

# --- B-1325 <- 1415 B-2627 "The Chalked Cut" (hands-only, off-screen line "Cut true.") ---
t = extract("PREPRO_2026-10-20_1415.md", 78, 86)
t = strip_tokens(t)            # (B-79) removed; (B-45: cluster-diff, never scalar) backstop-removed
finish(t, "fire_b1325_20261020_1545_v1.txt", stack=False)

# --- B-1326 <- 1415 B-2628 "The Brushed Hat" (UNC draft, NO-LINE) ---
t = extract("PREPRO_2026-10-20_1415.md", 86, 94)
t = strip_tokens(t)            # (B-79) removed; (B-45: ...) unwrapped keeping prose
finish(t, "fire_b1326_20261020_1545_v1.txt", stack=True)

# --- B-1327 <- 1415 B-2629 "The Stacked Crates" (UNC draft, line "All stacked.") ---
t = extract("PREPRO_2026-10-20_1415.md", 94, 102)
t = strip_tokens(t)            # (B-79) removed; (B-45: ...) unwrapped keeping prose
finish(t, "fire_b1327_20261020_1545_v1.txt", stack=True)

print("done \u2014 all vehicles TEXT-ONLY, zero citation tokens, stack 2x UNC / verbatim hands-only")
