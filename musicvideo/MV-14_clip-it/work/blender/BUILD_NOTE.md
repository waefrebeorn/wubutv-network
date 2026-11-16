# Blender impact frame — MV-14 "the glowing CLIP in the cutting room at night"

Sprint 2026-11-11 (downtime-improvement, user msg 202). Proves the Blender
visual path for down-time work: a content-aware impact frame built as a
Blender scene — geometry + emission + Cycles render, zero generated imagery.

## Files

- `clip_impact_frame.py` — the scene script (build + render, run it again to
  reproduce). Run from this dir:
  `~/workspace/tools/blender/blender-4.5.15-linux-x64/blender -b --python clip_impact_frame.py -f 1`
- `clip_impact_frame.png` — the still, 1280x720, sha256
  `5559c87bf7f01d2f6d64cde191261dbbd7f9c1986be5d93ed162a0c24a75b99a`
- `clip_impact_frame.blend` — the saved scene (re-open to iterate).

## What is in the frame

- THE CLIP: a blank luminous film-frame rectangle (1.7 x 1.05 world units),
  four emissive gold bars (emission strength 7.0) + a blank luminous interior
  plane (emission 0.55) + perforation dots on the top/bottom bars. It floats
  above the desk, tilted back 12 deg, and is the key light (gold point light
  at its position, energy 25). The interior is BLANK by design — the MV-14
  carry stays blank in generation; the title is post-rendered.
- Cutting room at night: wooden desk, two film reels, splicer block, monitor
  with a faint cyan screen, scattered papers, a film strip, mug, warm desk
  lamp (practical point light). Dark blue-black world, cool moonlight area
  fill from the front-top. Camera 42mm, tracked to the CLIP.

## Measured

- Blender 4.5.15 LTS, Cycles CPU, 64 samples, OpenImageDenoise, 1280x720.
- Render time 4m46s on this VM (1.5 shared CPUs); peak memory 148 MB.
- Frame stats: mean RGB (0.221, 0.199, 0.189) — dark night scene; interior
  of the CLIP uniform warm (0.77–0.82) across rows 260–460 at frame centre;
  frame bars peak 0.98–0.99. Read back full-res and eye-verified.
- EEVEE was NOT used (blocked: no libEGL.so.1 on this VM, per MEMORY.md);
  Cycles CPU is the working path.

## Gotchas hit (so the next run doesn't re-hit them)

1. Blender 4.5 removed the "Filmic" view-transform look — `view_settings.look
   = "Filmic"` raises TypeError. Leave the look at default (AgX).
2. `bpy.ops.wm.read_factory_settings(use_empty=True)` wipes the World
   datablock — `bpy.data.worlds["World"]` KeyErrors after it. Create the
   world if missing (`bpy.data.worlds.get("World") or bpy.data.worlds.new(...)`).
3. A Blender plane lies FLAT (normal +Z). The first render's CLIP interior
   read as a thin horizontal band because the interior plane was nearly
   edge-on to the camera. Fix: rotate the plane 90 deg about X so it faces
   the camera, then apply the 12 deg tilt (`rotation=(radians(90)+tilt,0,0)`).
   The v1 render (band artifact) was discarded; the shipped PNG is the
   re-render.
4. `//` relative paths resolve against the .blend file — with `-b` and no
   saved .blend yet, they land at the filesystem root (`/clip_impact_frame.png0001.png`).
   The script now uses absolute paths for both the .blend save and the render
   output. Note also that `-f 1` appends the frame number
   (`clip_impact_frame.png0001.png`); the file was renamed to
   `clip_impact_frame.png` after the render.

## Next uses

- Same scene re-lit/re-framed per MV-14 scene (S49 splicer snap, S51 wire
  world, S62 peak) — change the camera + prop layout, keep the CLIP build.
- The CLIP geometry (frame bars + blank interior + perforations) is the
  reusable carry asset for Blender-side impact frames; a title card can be
  composited over the blank interior in post, same as the generated takes.
