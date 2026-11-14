#!/usr/bin/env python3
"""Build durable v1 fire vehicles for the Q2 2026-10-20 1600 EDT stall-queue run.

Stall-queue banking: NO video API calls (budget outage opened 2026-10-20 ~13:37 EDT
persists; the 14:52 refusal's developer instruction forbids any further video
request now; a 429 is a hard stop). These vehicles are the durable resume queue.

1415-format (B-2630): verbatim PREPRO extract, Source paragraph stripped, hardened
citation-token strip (colon-class (B-45: prose) unwrapped keeping 6-tile QC prose
via regex; backstop kills any remaining (X-NNN...) form), ANTI-UNDERLINE-BAR
STACK exactly 2x section-scoped (SUBJECTS + NEGATIVE; LOAD-BEARING's
"(SUBJECTS + LOAD-BEARING + NEGATIVE pre-emptive stack)" reminder preserved
untouched — the 1430 double-application fix + 1515 substring-overlap
section-scoping), 0815 BUG anti-leak clause appended.

1515-format (B-2631, B-2632): the 1515 PREPRO drafts already carry the strong
bar wording natively ("ABSOLUTELY NO BAR, LINE, OR STRIPE ...") in SUBJECTS +
LOAD-BEARING (exactly 2x) — kept verbatim, no strengthening pass (their
NEGATIVE keeps the plain "no underline bar under the wordmark," per the Q1
1515 format). Same citation-token strip + BUG clause. B-2631's complex
(B-45: ...; B-588 watch: ...) token is removed whole by the backstop (a QC
pipeline note, not scene content). B-2632's directed line is RESTAGED AT CLAIM
from "Ground fine." to "To order." — the old line is owned by the live 1400
stall claim (1315 B-2610 "The Pestle", banked as B-1308, unshot); exactly one
replacement asserted.

Zero citation tokens asserted on all three.
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
    # Backstop: any remaining (X-NNN...) token form (covers (B-79), (S-16),
    # and complex multi-clause (B-45: ...) forms like B-2631's)
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

def finish(text, out, stack, restage=None):
    if stack:
        text = strengthen_bar_stack(text, out)
    else:
        n = text.count(STRONG)
        assert n == 2, f"expected native 2x bar stack in {out}, found {n}"
    if restage:
        old, new = restage
        c = text.count(old)
        assert c == 1, f"expected exactly 1x restage target {old!r} in {out}, found {c}"
        text = text.replace(old, new)
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

# --- B-1328 <- 1415 B-2630 "The Pitched Tent" (UNC draft, NO-LINE) ---
t = extract("PREPRO_2026-10-20_1415.md", 102, 108)
t = strip_tokens(t)            # (B-45: ...) unwrapped keeping 6-tile QC prose
finish(t, "fire_b1328_20261020_1600_v1.txt", stack=True)

# --- B-1329 <- 1515 B-2631 "The Bell That Broke Lightning" (UNC draft, line "They used to ring against it.") ---
t = extract("PREPRO_2026-10-20_1515.md", 16, 22)
t = strip_tokens(t)            # complex (B-45: ...; B-588 watch: ...) removed whole by backstop
finish(t, "fire_b1329_20261020_1600_v1.txt", stack=False)

# --- B-1330 <- 1515 B-2632 "The Ground Spice" (UNC draft, line RESTAGED at claim: "To order.") ---
t = extract("PREPRO_2026-10-20_1515.md", 24, 30)
t = strip_tokens(t)            # (B-45: ...) unwrapped keeping prose; (B-79) removed
finish(t, "fire_b1330_20261020_1600_v1.txt", stack=False,
       restage=('"Ground fine."', '"To order."'))

print("done \u2014 all vehicles TEXT-ONLY, zero citation tokens, stack 2x (1415 strengthened / 1515 native)")
