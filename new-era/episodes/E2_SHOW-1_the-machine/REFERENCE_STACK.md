# E2 SHOW-1 THE MACHINE — REFERENCE STACK (Panel Workflow Spec v2)

Bible: palette INK black / CADMIUM yellow-gold / COBALT screen-blue /
FOREST green accent · light = monitor glow key + one warm amber
practical · camera locked or slow push · texture: slight codec
softness, cinematic, never ad-clean.
LOOK — UNC: man late 40s, short dark hair flecked grey, weathered
deadpan face, light stubble, black hoodie, chest wordmark exactly
`~ WuBu ~` in bold yellow-gold. LOOK — LAURA: woman early 30s, dark
brown hair low ponytail, sharp curious expression, forest-green work
shirt, black studio headphones around her neck, never worn.
LOOK — THE SINGER (single large monitor only): black cat, red
collar, small gold bell, BLUE eyes (pilot PEAK-U3 eye-drift nit is
the named failure this kit guards: any panel or take showing the
cat with non-blue eyes is rebuilt/refired, never shipped).

## Panels

| file | type | md5 | snapshot_id | status | built-from | used-by | QC note |
|---|---|---|---|---|---|---|---|
| PNL-WORLD-cuttingroom.png | WORLD | dd0761b19932a8d44e78e5404bb7e57d | pilot kit | LOCKED (canon, carried from PILOT-1) | pilot | room anchor | empty room ✓ console ✓ |
| PNL-CHAR-UNC-hero.png | CHAR | f11f2c47b3ecf29d1e088921f8fe72c4 | pilot kit | LOCKED (canon) | pilot | identity | wordmark exact `~ WuBu ~` ✓ |
| PNL-CHAR-UNC-face.png | CHAR | 0d4bafc54a318cde1a326bbf0e7367fa | pilot kit | LOCKED (canon) | pilot | identity support | ✓ |
| PNL-CHAR-LAURA-hero.png | CHAR | 19149e1a341c9f6c82d682e119d4c384 | pilot kit | LOCKED (canon) | pilot | identity | ✓ |
| PNL-CHAR-LAURA-face.png | CHAR | 0cfd5d3516a94a4fe14286d7234bfb0d | pilot kit | LOCKED (canon) | pilot | identity support | ✓ |
| PNL-PROP-headphones.png | PROP | 404504f432d607d2c78264a39b04a23f | pilot kit | LOCKED (canon) | pilot | prop ref | exactly one pair ✓ |
| PNL-CHAR-BOTH.png | CHAR (combined) | 68a8bf25e2865bdbe33f605ae1fb3f75 | fba31aa7-6318-4ccf-bdf7-87d5ac832327:7j8wgc | LOCKED | anchored UNC-hero + LAURA-hero | U1, U4 image-2 (both faces carry both units) | both identities match canon ✓ wordmark exact `~ WuBu ~` bold yellow-gold ✓ headphones at neck ✓ hands empty ✓ |
| PNL-PEAK-U1.png | PEAK | 731c5ea7838b57857dbde7722a690666 | f479b38f-68fa-4d3e-8d38-054a6d184c95:gotwkg | LOCKED | anchored WORLD + UNC-face + LAURA-hero | U1 image-1 | THE IMPACT FRAME: UNC profile MID-WORD, mouth open shaping a word ✓ single large monitor BLACK behind him ✓ LAURA frozen at frame edge, eyes on his mouth, headphones at neck ✓ warm practical ✓ centre-cropped 2096×1184→2096×1179 (framing only) |
| PNL-PEAK-U4.png | PEAK | 0f33ccdbc93a12ddd2940587aea3ee83 | dfba95eb-1526-4e27-a19e-b61c90cba672:c91k0p | LOCKED | anchored WORLD + UNC-hero + LAURA-hero | U4 image-1 | LAURA lays the take-file folder on the desk between them ✓ UNC at frame edge in shadow, hands OFF the folder ✓ wordmark exact ✓ cat on monitor: black, red collar, gold bell, eye BLUE ✓ mouth closed ✓ |

## Boundary classification (J1/J2) + generation routes (J3/J7)

One room, one continuous scene, same cast throughout — every
boundary is a JOINT; the carry device is THE MOUTH HANDOFF (a sung
onset straddling every cut, J9). Chain runs capped at 3 units (J7):
U4 re-anchors.

| boundary | class | carry state at cut | route for downstream unit |
|---|---|---|---|
| U1→U2 | JOINT | monitor mouth opens on next word, following UNC | U2 = resume from U1 snapshot (J3a) |
| U2→U3 | JOINT | monitor mouth opens, still following | U3 = resume from U2 snapshot (J3a) |
| U3→U4 | JOINT | monitor opens behind UNC's back | U4 = RE-ANCHOR: image 1 = PNL-PEAK-U4, image 2 = PNL-CHAR-BOTH (J7) |
| U4→U5 | JOINT | monitor opens, indifferent | U5 = resume from U4 snapshot (J3a) |
| U5→U6 | JOINT (inverted) | the handoff FAILS to arrive — mouth stays closed; the deferred onset lands as U6's opening, triggered by UNC's return | U6 = resume from U5 snapshot (J3a) |

Fallback per joint (J3b): if a resume take fails QC (scene does not
continue / identity break), extract the joint frame (J4: last frame
before the deceleration zone, from the conformed segment), derive
the downstream PEAK from it (J5), and refire as a two-image chain.

## Rotation table (J20) — non-chain calls only

| unit | slot 1 | slot 2 | tag |
|---|---|---|---|
| U1 | PNL-PEAK-U1 | PNL-CHAR-BOTH | ROT-BOTH (cast-forced: both faces carry the unit) |
| U4 | PNL-PEAK-U4 | PNL-CHAR-BOTH | ROT-BOTH (cast-forced: volley unit, both faces carry) |

Invariants never rotate (J21): canonical CHAR set above, the
wordmark glyph string, the cat's BLUE eyes / red collar / gold bell,
LAURA's neck-worn headphones, 16:9 on every reference, the mouth
handoff as carry device.

## GFX card — THE MACHINE (kit lock, this episode)

- **Invariant device: THE DEAD CHANNEL** (Method C §2.1a). ffmpeg
  `showwaves` mode=line rendered from the episode's OWN conformed
  audio (post audio-conform, §5.5 order), COBALT line, thin strip
  1280×36 along the frame's lower edge, ambient in every unit.
  Story behaviour: the strip flatlines where the machine is silent
  — U1's silent mouthing head and U5's stall read as a dead line
  beside the moving/closed mouth, drawn from the real audio, never
  faked. Frame-0 law (§3.5): ambient presence from frame 0 is
  allowed; no graphic EVENT starts before ~1.5s of U1 — the strip's
  first spike is drawn by U1's designed first-second sound event
  (the console relay click), which is a picture/audio event, not a
  graphic ignition.
- **Bug:** `~ WuBu ~` bottom-right, drawtext DejaVu Sans Bold,
  cadmium #FFC400 (house practice, pilot-verified).
- No other devices fire this episode (density cap §3.5; the Early
  Readout and Volley Board stay unfired — the episode's paperwork
  is the physical folder in U4, in-picture).
