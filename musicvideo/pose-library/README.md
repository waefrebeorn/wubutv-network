# WuBu pose library

WuBu's own pose system for music videos and STATION pieces. Original text
descriptions only — no copied gallery images, no copied prompts.

## How it works

- `POSE_VOCABULARY.md` holds the shared language: viewpoint set, joint
  language, depth-layering language, and the vehicle anatomy.
- Each project holds its own `POSE_CARDS.md`: signature poses for that
  project's character(s), with every scene assigned to one card.
- Anchors: the first accepted take of a signature pose files its first
  frame under the project's `anchors/` folder; later scenes name it.

## Rules (standing)

- SFW poses only (standard full-body, upper-body). Adult categories from
  public galleries are never used, browsed for a project, or described.
- Poses are body geometry, never identity. Never a real person's likeness.
- Browse public galleries by URL for ideas only; never copy an image,
  prompt, or workflow file into a WuBu project.
- One character per scene keeps its own card; a pose card never adds a person.

## Sources SLERM'd (workflow only, 2026-11-01)

- ai-pose-gallery-zh (pose / costume / portrait 3-in-1 recipe, viewpoint set)
- POSE-DB-02 depth pose gallery (depth map as layering reference)
- Stable Diffusion tutorial workflow writing (reference-driven conditioning,
  repeated verbatim blocks)
