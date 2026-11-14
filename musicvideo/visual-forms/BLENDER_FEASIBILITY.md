# BLENDER_FEASIBILITY — Blender on this VM, measured (2026-11-06)

Evidence file for Family G (code-rendered graphics), G3 row. User order
2026-11-06: "acquire blender and use cpu to make graphics and animations
and storyboards if needed". Everything below was run and measured on
this VM — no claims from docs.

## Install

- **Version:** Blender 4.5.15 LTS (build 2026-10-22, hash 5afeabba6097)
- **Binary:** `~/workspace/tools/blender/blender-4.5.15-linux-x64/blender`
- **Source:** official tarball `blender-4.5.15-linux-x64.tar.xz` from
  https://download.blender.org/release/Blender4.5/ (newest 4.x),
  378,036,492 bytes, tarball md5 `5b4c0ba6de99fe70567a849371b05984`,
  `tar tJf` listing verified before extract; extracted tree = 1.1 GB.
- Installed under `~/workspace/tools/` on purpose: home persists across
  deployments, system dirs do not. No sudo/apt/snap used.
- `blender --version` runs headless with no extra setup.
- VM: 4 cores, 7 GB RAM.

## Engine reality on this VM (the honest column)

- **EEVEE: BLOCKED.** Any EEVEE render aborts (SIGABRT) with
  `Couldn't open libEGL.so.1` — the VM has no libEGL/GL stack (ldconfig
  shows no EGL entries; system has libGL/libGLX but no libEGL.so.1).
  EEVEE is GPU/GL-based even headless; it cannot run here until a
  Mesa/EGL stack exists on the VM. One untested candidate noted for a
  future experiment: Chromium's bundled ANGLE library
  `/opt/meta-chromium/libEGL.so` exists on disk (wrong SONAME, built
  for Chromium — not tried with Blender, may not work).
- **Cycles CPU: WORKS.** All proofs below are Cycles on CPU.
- Consequence: Blender's fast engine is unavailable; every render pays
  path-tracing prices. Budget accordingly (see limits).

## Proof renders (all in `blender-proof/` next to this file)

### 1. Still — palette scene + "WUBU" text object
- Script: `blender-proof/proof_still.py` — ground plane (INK #141414),
  cube (COBALT #1B3FD1), sphere (VERMILION #E23A1B), cone (CADMIUM
  #FFC61E), extruded text object "WUBU" (BONE #F4EEDC), area light,
  Cycles CPU, 16 samples + OpenImageDenoise, 640×360 PNG.
  (Palette hexes converted sRGB→linear in the script; raw values render
  visibly washed out.)
- Command: `blender -b --factory-startup --python proof_still.py`
- **Render time: 21.3 s** (Blender's own `Time:` line; 24 s wall incl.
  startup).
- Output: `blender-proof/wubu_still.png` — 257,747 bytes,
  md5 `c02593f1571e438b9dbdafddc798434f`.
- Frame-audited by eye: all five palette colors read true, "WUBU" fully
  framed. PASS.

### 2. Animation — 24 frames, sliding/spinning cube + bouncing sphere
- Script: `blender-proof/proof_anim.py` — keyframed location/rotation,
  Cycles CPU, 8 samples + denoise, 640×360 PNG sequence, frames 1–24
  at 24 fps.
- Command: `blender -b --factory-startup --python proof_anim.py`
- **Render wall: 565 s for 24 frames (~23.5 s/frame average).**
  Caveat: a filesystem-wide search was running concurrently for part
  of this render, so treat per-frame time as an upper bound; the
  uncontended still of a similar scene at double the samples took
  ~21 s/frame.
- Encode: `ffmpeg -framerate 24 -i frames/frame_%04d.png -c:v libx264
  -pix_fmt yuv420p -crf 18 wubu_anim.mp4` (5 s).
- Output: `blender-proof/wubu_anim.mp4` — 55,571 bytes,
  md5 `6cc007a9ef1cdc6a353ff241f87be228`; ffprobe: 640×360, 24 frames,
  duration exactly 1.000 s.
- Motion verified by comparing frame_0001 (cube left, md5
  `8cdecf22db2166e98adbe1ec9877314a`) vs frame_0024 (cube right,
  md5 `ac34b0cf26a8470ac55bdc48e51ff85a`): real keyframed motion, PASS.

### 3. Storyboards — Grease Pencil
- Grease Pencil v3 is present in this build (types enumerated in
  background mode: `GreasePencilv3`, `GPencilLayer`, `GPencilStroke`,
  etc.). Object creation via `bpy.ops.object.grease_pencil_add()` and
  layer creation via the GPv3 API both work headless (verified across
  three attempts, each getting further).
- **A rendered GP frame is NOT verified:** the third attempt aborted
  (SIGABRT, same missing libEGL) before completing — GP's drawing path
  touches the GL stack even in background mode. GP authoring via API =
  verified present; GP rendering on this VM = unverified, presumed
  blocked by the same missing libEGL as EEVEE.
- Storyboard fallback that IS proven: storyboard panels as ordinary
  Cycles renders (proof 1 is effectively one), or ASS/PNG panels.

## Honest limits — what the numbers imply

- At 640×360, simple scenes cost ~10–25 s/frame on this 4-core VM
  (Cycles CPU, 8–16 samples). 1280×720 has 4× the pixels → roughly
  **1–2 min/frame**; a 10-second shot (240 frames) at 720p ≈ **4–8
  hours**. A full 3–4 minute MV in Blender 3D on this VM is not a
  plan; it is a week.
- What Blender CPU here is genuinely good for:
  - **Short 3D accents** (Family G3): a rotating token, a turntable of
    a motif object, a 3D title card — 1–3 s clips at 640×360 (or 720p
    stills / very short 720p moves with an overnight budget).
  - **Storyboard / animatic frames**: composed stills with exact
    camera, palette and text — cheap, frame-exact, no generator drift.
  - **Exact-repeat motif objects**: the same model file every return,
    which the video generator cannot promise.
- Sample counts above 16 and complex materials/shadows were not
  tested; times scale roughly linearly with samples.
- If EEVEE is ever unblocked (Mesa/libEGL appears on the VM), re-run
  proof 1 with EEVEE before promising anything — EEVEE would change
  the economics by ~10–50×, but today it does not run here at all.

## Reproduce

```
B=~/workspace/tools/blender/blender-4.5.15-linux-x64/blender
P=~/workspace/wubutv-network/musicvideo/visual-forms/blender-proof
$B --version
$B -b --factory-startup --python $P/proof_still.py
$B -b --factory-startup --python $P/proof_anim.py
ffmpeg -framerate 24 -i $P/frames/frame_%04d.png -c:v libx264 -pix_fmt yuv420p -crf 18 $P/wubu_anim.mp4
```
