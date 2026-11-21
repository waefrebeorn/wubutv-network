# Q10 v5 — full-res burned-kinetic visual gate (2026-11-13 ~09:45 EST)

Master: `masters/mv5_easy_now_easy_now_16x9_v5.mp4` (md5 395c314080d7bfc33ff6f0808b7463cd).
Frames: `work/q10/qc/v5_frames/` — 26 planned + 8 follow-ups, all distinct md5s,
separate `-ss` calls, extracted at word_start+0.05s (the lyrics-gate +0.05s rule).

## Verdict: PASS (with disclosed nits below). All three user defects verified fixed on screen.

### Defect 1 — bad timing (picture now follows the new grid)
- S01 I01 "Easy" 1.45s: CAT mouth WIDE OPEN (tongue), caption "Easy now, easy now", "Easy" gold. PASS.
- S01 I02 "ride" 4.05s: CAT mouth open (small "o", eyes closed), "ride" gold. PASS.
- S04 L01 "Bare" 22.05s: mouth closed at the exact onset frame; 22.15s mouth WIDE OPEN
  (teeth/tongue). The take's first word opens ~0.1–0.15s in — onset-frame lag only. PASS.
- S04 L02 "Salt" 23.01s: CAT mouth slightly open, articulating "Salt". PASS.
- S04 L04 "begin" 29.09s: CAT mouth WIDE OPEN, "begin" gold. PASS.
- S11 L40 "time" 91.23s: GIRL mouth WIDE OPEN, "time" gold — v4 put "Time" 2.05s early; FIXED. PASS.
- S20 L80 "breeze" 156.47s: GIRL mouth WIDE OPEN, "breeze" gold. PASS.
- S23 L96 "No" 174.49s: closed at onset; 174.60s mouth OPEN singing "No". Same onset lag as L01. PASS.
- S24 L97 "easy" 176.50s: GIRL mouth OPEN, "easy" gold. PASS.
- S24 L99 "Easy" 178.29s: GIRL mouth OPEN (eyes closed), "Easy" gold. PASS.
- S28 L110 "Till" 203.89s: CAT mouth WIDE OPEN (teeth/tongue), "Till" gold. PASS.

### Defect 2 — cat talking when she is (correct singer's mouth now on screen)
- S06 L12 "Yeah" 44.63s: GIRL mouth WIDE OPEN singing "Yeah"; CAT mouth CLOSED in basket. FIXED. PASS.
- S07 L15 "One" 51.29s: GIRL ALONE, mouth in small "o" singing "One", eyes closed; NO CAT
  in frame (only a sliver of CAT ear at the bottom-right edge). FIXED. PASS.
- S12 L42 cover 95.60–96.70s: girl's mouth open ONLY at 95.60s (the L41 "air." tail, disclosed
  gap-edge WARN, 0.13s); 95.80s nearly closed; 96.10/96.40/96.70s FULLY CLOSED.
  v4 frame-96.0 defect FIXED. PASS.
- S12 L43 "I" 96.83s: GIRL lips slightly parted for "I" (take's word onset). PASS.
- S27 L109 cover 202.00s: GIRL mouth CLOSED, CAT eyes/mouth CLOSED — no CAT mouth over the
  girl's L109 (v4's S27 defect FIXED; L110 moved to S28). PASS.
- S17 L69 cover 135.70s: BOTH mouths CLOSED (v4's "singing tail" claim was wrong; cover is clean). PASS.
- S24 L98 cover 177.50s: GIRL mouth CLOSED, CAT closed. PASS.
- S06 L11 cover 43.50s: CAT eyes CLOSED, mouth CLOSED (structural line, caption carries it). PASS.

### Defect 3 — low grab for the intro
- 0.50s leader: girl RIDING, hair flying, ocean, CAT in basket — motion from frame 0.
  No frozen yawning CAT. PASS.
- I05 cover 10.65s / I08 cover 13.50s: riding montage (two different angles), both mouths
  closed, captions "Easy now, easy now" / "Till the morning comes". NO wrong-words inserts
  (v4's I05/I07 mouths are gone). PASS.

### Disclosed nits (not fails)
1. **L38 "Calling" (86.55–87.30s, S11) — weakest sung picture in v5.** Wide market shot;
   CAT's mouth never visible (back turned in basket); girl's lips slightly parted at 87.0s.
   Not a clear wrong-mouth (small parting, not a singing "o"), but the line is carried by the
   caption + the correct take's timing (words within ±0.10s). Take s11_t4 also carries a
   duplicate-cat generation artifact (a second black cat silhouette on the fruit crates).
   Disclosed; no fix available without a new take (cap exhausted).
2. **L16 cover cut frame (54.00s, S07):** CAT's mouth slightly open with tongue out on the
   L16b piece boundary (s04_t1 f208). Reads as a pant, not a word; the CAT is L16's singer,
   so no wrong-mouth. Nit only.
3. **L70 "good" (136.60s, S17):** CAT mouths the take's "comes" tail over "good" (v4 carryover,
   disclosed in the plan). Small opening only, not a wide wrong-word mouth.
4. **L81 head (157.20s, S20):** girl's mouth slightly open in a smile — the "breeze" tail
   closing (breeze ends 156.99 < L81 head 157.02). Not a wide singing mouth; v4's wide-open
   defect is fixed.
5. **S24 caption flicker (176.05–176.26s):** the .ass shows "We hold the sun" for 5 frames
   during L97's "Easy" — L97's "Easy" event is 0.01s (176.04–176.05) and the overlapping
   L98 "We" event (176.04–176.26) takes over. PRE-EXISTING lyrics-redo .ass overlap artifact
   (also in the delivered a3e65922 master), not a v5 regression. By 176.50s the caption is
   correctly "Easy now, easy now" with "easy" gold.
6. **Onset-frame lag:** L01 "Bare" and L96 "No" both show a closed mouth on the exact onset
   frame, opening 0.10–0.16s in. The take's first word starts from a closed mouth. Cosmetic.

### Carried disclosures (from the plan, unchanged)
- L104: CAT's lead line stays mouth-less (v4 picture kept; no take of the CAT singing it exists).
- I08 / L16 / L69 / L98 / L100 / L109: montage/cover (no singing picture; captions carry the words).
- S17 P1/P2 + S23 P1 + S24 P2: chorus compromises (take sings "Easy now" over other lines).
- S06 L10 words −0.36/−0.43/−0.41; S07 L13 "take" −0.38; S04 L05 "red" +0.30; S28 "comes" −0.32
  (cut 0.20s early); L102 "drift" disclosure as-is (unresolved tie, sheet+GEM).
