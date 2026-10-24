# Character Consistency Research — 2026-09-26

Question from the user: how do we keep characters consistent across generated clips,
researched against my own tools (web research + a live experiment on Muse Video).

## 1. What my tools actually offer (from ~/docs/media.md)

- **Muse Video** (Meta): ~10s fixed clips, synthesized sound from mood text.
- Prompt input: text AND images. Supports ordered text/image sequences.
- Can reference earlier generations by `snapshot_id` to carry visual context across calls.
- Output is always a fresh generation — never a frame-exact animation of a storyboard.
- No LoRA training, no identity-embedding modules, no per-frame face fixer. Those don't exist in my toolset.

## 2. Industry state of the art (web research, Sept 2026)

The field has converged on one core insight: **stop asking the model to invent AND
animate simultaneously. Lock identity FIRST (reference image), then animate.**

Main techniques in use:
1. **First-frame anchoring (two-stage pipeline)** — generate an identity-accurate
   still first (character portrait), then feed it as the first frame / reference to
   the video model with a "face must remain identical to the starting frame" instruction.
   Validated across 257 experiments to cut face distance ~70%. This is the single
   highest-leverage technique available without training.
2. **Hyper-detailed descriptions in EVERY prompt** — never rely on the model
   "remembering" a character; repeat the full appearance string (age, face, hair,
   build, clothing, distinguishing marks) verbatim in every generation.
3. **Multi-reference identity** — newer models accept up to 10 reference images;
   trained digital doubles (Soul ID style: 20+ photos, ~3 min training) for brand work.
4. **LoRA + identity adapters** (InstantID / PuLID / FaceDetailer per frame) —
   maximum consistency, but requires training infrastructure I don't have.
5. **Snapshot/context chaining** — carrying latent context across calls (my
   `snapshot_id` equivalent).

Sources: FLUX.2 / InfiniteYou / PuLID identity-preservation survey 2026;
happycapy ViMax face-identity guide (257 experiments); openmontage
character-consistency skill; cemini23 video-identity-inheritance notes
(CLIP Vision encoder vs raw pixel init); higgsfield Soul ID.

## 3. Empirical test on my own tools (this session)

**Setup:** Two 10s clips of UNC in a NEW setting (laundromat — tests cross-setting
identity hold, not just same-scene drift).
- `consistency-control`: text-only prompt with the full canonical UNC description.
- `consistency-test`: same text prompt + `unc_ref.png` (clean UNC frame extracted
  from shipped O-1) as a `kind: image` input, with the instruction "use ONLY as a
  character reference; do not copy the background."
- Frames extracted at 2s / 5s / 8s from each; compared to each other and to the O-1
  reference.

**Results:**
- **Within-clip drift: LOW in both.** Muse Video holds this 2D cartoon design
  well across 10s — afro, mustache+goatee, WuBu hoodie text, teal-orb staff all
  stable from 2s through 8s, including through a pose change (facing camera →
  loading the machine).
- **Cross-generation identity: image reference wins clearly.** The text-only take
  produced a same-archetype face that reads as UNC but differs slightly from the
  O-1 reference (rounder face). The image-reference take matches the reference
  face closely — same jaw, mustache shape, afro silhouette — in a completely new
  setting.
- **No background bleed.** The "character reference only" instruction worked:
  the laundromat scene contains no vending-machine elements from the reference.

**Files:** test clips and comparison frames live in `~/workspace/freeq/`
(`media-generation-consistency-{control,test}-*`, `unc_ref.png`, `cmp_{control,test}_{2,5,8}s.png`).

## 4. Recommended consistency playbook for the WuBu pipeline

1. **Build a canonical reference still per character.** Extract the cleanest
   front-facing frame from a shipped ACCEPTED piece (O-1 gave us UNC's). Store in
   the channel directory as the character's anchor.
2. **Pass the anchor image on every new generation** with the "character reference
   only, new setting" instruction — this is the first-frame-anchoring technique,
   implemented with the image-input path.
3. **Keep repeating the full canonical description in text anyway** — belt and
   suspenders; text alone already produces same-archetype results.
4. **Snapshot chaining (`resume_from_snapshot_id`) for direct sequels** — remember
   snapshots are single-use; always chain from the latest.
5. **Keep the 6-tile / multi-timestamp QC** as the substitute for frame-level
   fixing: we can't FaceDetailer a bad frame, so we reject and re-fire. The
   mandatory detail-tile rule stays.
6. **New characters (Laura, Colonel, Peter, Wizard):** do not introduce
   visually until we have either a canonical reference still or an approved
   design frame — per the playbook, the first accepted render BECOMES the anchor.

## 5. What I cannot do (honest limits)

- No LoRA/identity-embedding training on my side; no per-frame face correction.
- Output is always a fresh generation — pose, framing, and micro-expression will
  vary take to take. Consistency means *recognizably the same character*, not
  pixel-identical frames.
- ~10s fixed clip length; longer scenes are assemblies, and assembly seams are a
  separate continuity problem (match-on-action prompting, not solved here).
