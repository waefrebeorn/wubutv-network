#!/usr/bin/env python3
"""Clean renderer: blocky 3D humanoid, horizontal brows/pupils, RMS-driven
horizontal mouth, STATIC arms, one silhouette feature, pure-emission Cycles.

Invoked by Blender: BRAIN_ENV=<session.json> BRAIN_OUT=<frame_dir> blender -b --python clean_render.py
Prints CLEAN_RENDER_OK <count> on success.
"""
import bpy, math, os, json, sys
from mathutils import Vector

ENV = os.environ.get("BRAIN_ENV")
OUT = os.environ.get("BRAIN_OUT")
if not ENV or not OUT:
    raise SystemExit("clean_render: BRAIN_ENV and BRAIN_OUT required")
S = json.load(open(ENV))
os.makedirs(OUT, exist_ok=True)

# Clear the default startup scene (cube/camera/light) — its cube occludes the rig.
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

W, H, FPS, N = int(S["w"]), int(S["h"]), int(S["fps"]), int(S["nframes"])
MOUTH = S.get("mouth", [0.0] * N)
CH = S["char"]
BG, BG2 = S["bg"], S["bg2"]

# ---------- scene ----------
scene = bpy.context.scene
scene.render.engine = "CYCLES"
scene.cycles.samples = 1
scene.cycles.use_denoising = False
scene.render.resolution_x, scene.render.resolution_y = W, H
scene.render.resolution_percentage = 100
scene.render.image_settings.file_format = "JPEG"
scene.render.image_settings.quality = 92
scene.view_settings.view_transform = "Standard"
scene.view_settings.look = "Medium High Contrast"
scene.render.film_transparent = False
scene.world.color = (0.0, 0.0, 0.0)

def emat(name, rgb):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    nt = m.node_tree
    nt.nodes.clear()
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    e = nt.nodes.new("ShaderNodeEmission")
    e.inputs["Color"].default_value = (rgb[0], rgb[1], rgb[2], 1.0)
    e.inputs["Strength"].default_value = 1.0
    nt.links.new(e.outputs["Emission"], out.inputs["Surface"])
    return m

def box(name, loc, scale, mat):
    bpy.ops.mesh.primitive_cube_add(size=2, location=loc)
    o = bpy.context.object
    o.name = name
    o.scale = scale
    o.data.materials.append(mat)
    return o

def ball(name, loc, radius, mat):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=12, ring_count=8, radius=radius, location=loc)
    o = bpy.context.object
    o.name = name
    o.data.materials.append(mat)
    return o

# ---------- palette ----------
head_m = emat("head", CH["head"])
body_m = emat("body", CH["body"])
acc_m = emat("accent", CH["accent"])
skin_m = emat("face", CH.get("face", [0.96, 0.80, 0.62]))
white_m = emat("white", [0.97, 0.97, 0.99])
dark_m = emat("dark", [0.05, 0.05, 0.08])
lip_m = emat("lip", CH.get("lip", [0.35, 0.07, 0.10]))
bg_m = emat("bg", BG)
bg2_m = emat("bg2", BG2)
teeth_m = emat("teeth", [0.98, 0.98, 0.94])
# arms in a slightly darker body tone + pushed out from the torso, so the
# silhouette does not fuse into one slab (silhouette-readability law)
arm_m = emat("arm", [c * 0.86 for c in CH["body"]])

# ---------- background (two-tone gradient via stacked bands) ----------
for i in range(24):
    t = i / 23.0
    r = BG[0] * (1 - t) + BG2[0] * t
    g = BG[1] * (1 - t) + BG2[1] * t
    b = BG[2] * (1 - t) + BG2[2] * t
    m = emat("bgband%02d" % i, [r, g, b])
    z = -2.4 + t * 5.4
    box("bg%02d" % i, (0, 1.2, z), (5.0, 0.02, 0.125), m)

# ---------- camera ----------
# Framing law (2026-11-25): the caption band starts at 74.5% of H, so at ortho
# 5.0 the feet (z=-1.25) fell at y=787px and were hidden by the captions. This
# song is about feet, so the figure is framed to put the whole body above the
# band: head top 90px, feet 700px, band 715px.
CAM_O = float(os.environ.get("CAM_ORTHO", "5.68"))
CAM_Z = float(os.environ.get("CAM_Z", "0.05"))
cam = bpy.data.cameras.new("cam")
cam.type = "ORTHO"
cam.ortho_scale = CAM_O
co = bpy.data.objects.new("cam", cam)
scene.collection.objects.link(co)
co.location = (0.0, -7.0, CAM_Z)
co.rotation_euler = (math.radians(90), 0.0, 0.0)
scene.camera = co

# ---------- character ----------
ROOT = [0.0, 0.0, 0.0]  # head-centered rig, body below

# torso + legs + feet (STATIC)
torso = box("torso", (0, 0, 0.30), (0.50, 0.34, 0.62), body_m)
TORSO_Z = 0.62
box("hip", (0, 0, -0.34), (0.46, 0.30, 0.14), acc_m)
for side in (-1, 1):
    box("leg_%d" % side, (side * 0.24, 0, -0.72), (0.17, 0.19, 0.42), body_m)
    box("foot_%d" % side, (side * 0.24, -0.10, -1.12), (0.20, 0.30, 0.13), dark_m)
    # arms touch the torso (inner edge 0.51 vs torso edge 0.50 = 1.7 px contact).
    # At x=0.80 they read as detached sleeves floating beside the body — measured
    # 26 px of background between arm and torso on the full frame 2026-11-25.
    box("arm_%d" % side, (side * 0.66, 0, 0.32), (0.15, 0.17, 0.56), arm_m)
    box("hand_%d" % side, (side * 0.66, 0, -0.24), (0.17, 0.18, 0.15), skin_m)

# head
HEAD_PARTS = []  # (object, base_z) — the whole head group can breathe together

def head_part(o):
    HEAD_PARTS.append((o, o.location.z))
    return o

head_part(box("head", (0, 0, 1.22), (0.74, 0.60, 0.76), head_m))
head_part(box("face_plate", (0, -0.612, 1.22), (0.66, 0.02, 0.66), skin_m))

# eyes: white plate + pupil, horizontal brows above
EYES, PUPS, BROWS = [], [], []
for side in (-1, 1):
    ex = side * 0.27
    e = head_part(box("eye_%d" % side, (ex, -0.64, 1.34), (0.15, 0.02, 0.12), white_m))
    p = head_part(box("pupil_%d" % side, (ex, -0.665, 1.33), (0.052, 0.012, 0.060), dark_m))
    b = box("brow_%d" % side, (ex, -0.652, 1.55), (0.17, 0.02, 0.032), dark_m)
    EYES.append(e); PUPS.append(p); BROWS.append(b)
BROW_Z = 1.55

# mouth: dark horizontal opening, anchored at top (jaw drops from upper lip line)
MOUTH_TOP = 1.20
MOUTH_W = 0.52
mouth = box("mouth", (0, -0.67, 1.16), (MOUTH_W / 2, 0.03, 0.02), lip_m)

# one clean silhouette feature
feat = CH.get("feature", "antenna")
if feat == "antenna":
    head_part(box("stalk", (0, 0, 2.10), (0.045, 0.045, 0.32), acc_m))
    head_part(ball("bulb", (0, 0, 2.46), 0.16, acc_m))
elif feat == "cap":
    # A uniform cap must be darker than the head, not an accent slab: with the
    # accent colour it read as a salmon roof across the whole skull (measured on
    # the 2026-11-25 THIRD SHIFT face sheet). CAP_DARK=0 restores accent.
    cap_m = arm_m if os.environ.get("CAP_DARK", "1") != "0" else acc_m
    head_part(box("cap", (0, 0, 2.02), (0.78, 0.62, 0.16), cap_m))
    head_part(box("brim", (0, -0.52, 1.98), (0.80, 0.30, 0.06), dark_m))
elif feat == "ears":
    for side in (-1, 1):
        head_part(box("ear_%d" % side, (side * 0.46, 0, 2.00), (0.16, 0.16, 0.28), acc_m))
elif feat == "fin":
    head_part(box("fin", (0, 0, 2.10), (0.10, 0.34, 0.38), acc_m))
elif feat == "crown":
    for side in (-1, 0, 1):
        head_part(box("crown_%d" % side, (side * 0.30, 0, 2.06), (0.09, 0.12, 0.30), acc_m))
    head_part(box("crown_base", (0, 0, 1.98), (0.72, 0.55, 0.10), acc_m))

# ---------- set: stage line + contact shadow (staging law) ----------
# A character with no ground line floats. One thin stage line just under the
# feet plus a shadow ellipse behind them reads as standing, and it never
# crosses the face.
stage_m = emat("stage", [min(1.0, c * 1.9) for c in BG2])
shadow_m = emat("shadow", [BG2[0] * 0.30, BG2[1] * 0.30, BG2[2] * 0.30])
box("stage_line", (0, 0.9, -1.33), (5.0, 0.02, 0.018), stage_m)
bpy.ops.mesh.primitive_uv_sphere_add(segments=24, ring_count=8, radius=1.0,
                                     location=(0, 0.22, -1.285))
sho = bpy.context.object
sho.name = "contact_shadow"
sho.scale = (0.78, 0.34, 0.016)
sho.data.materials.append(shadow_m)

# ---------- living hold ----------
# Limited animation reads cheap as "lifeless mouth flaps" unless something in the
# hold is still moving, and a 3D standing figure that is byte-identical between
# accents looks like a robot (Pixune limited-animation study + moving-hold law,
# note: wizard_hut/studied/2026-11-25-limited-animation-living-hold.md). Two
# channels only, both inside the user's laws: a breathing torso and a brow accent
# on sentence onsets. The brow TRANSLATES VERTICALLY and keeps its horizontal bar
# — a rotated brow is the diagonal-brow rejection.
LIVING = os.environ.get("LIVING_HOLD", "1") != "0"
BROW_LIFT = 0.022
HEAD_BOB = float(os.environ.get("HEAD_BOB", "0.022"))  # 0.022 world = 3.7 px @540x960

# ---------- authored stillness + brow drop (Paez, 2026-11-26) ----------
# "Some of the strongest acting happens in a pause: a held moment before a reaction,
# when the character takes in the news and has not yet answered." The driver writes a
# still window onto the written pause before the button: bob, blink and brow accents go
# to zero so the figure is genuinely frozen, then the button lands with a brow DROP
# (translation only, never rotation) so the face change arrives on the last word.
# Note: wizard_hut/studied/2026-11-26-beat-before-the-reaction.md
_ST = S.get("still") or [0, 0]
STILL0, STILL1 = int(_ST[0]), int(_ST[1])
_BD = S.get("brow_pop") or S.get("brow_drop") or [0, 0]
DROP0, DROP1 = int(_BD[0]), int(_BD[1])
# The clean rig has NO headroom BELOW the brow: measured at 540x960 the eye plate
# top sits 1 px under the brow bar, so a downward drop fuses the brow into the eye
# (and cancels against the ordinary lift). There are ~47 px of clearance ABOVE, so
# the button's expression change is a BROW POP: the same lift at 2.4x, which reads
# as one clear change instead of a 3 px slide nobody sees.
BROW_POP = float(os.environ.get("BROW_POP_MULT", "2.4"))
if STILL1 > STILL0:
    print("STILL window %d-%d (%.2fs)" % (STILL0, STILL1, (STILL1 - STILL0) / FPS))
if DROP1 > DROP0:
    print("BROW POP %d-%d x%.1f" % (DROP0, DROP1, BROW_POP))
brow_lift = [0.0] * N
if LIVING:
    _onsets = []
    for i in range(2, N):
        _prev = MOUTH[max(0, i - 8):max(1, i - 1)]
        if MOUTH[i] > 0.15 and max(_prev or [0.0]) < 0.06:
            _onsets.append(i)
    for _o in _onsets:
        # A gesture that accents dialogue leads it: Lemay (Lip Sync Book) asks for
        # 4-6 frames of anticipation at 24 fps (2-3 drawings on twos). Two frames
        # is a twitch; four reads as the face deciding to speak before it does.
        for _k, _v in ((-4, 0.30), (-3, 0.55), (-2, 0.80), (-1, 0.95), (0, 1.0),
                       (1, 1.0), (2, 0.85), (3, 0.55), (4, 0.30)):
            _j = _o + _k
            if 0 <= _j < N:
                brow_lift[_j] = max(brow_lift[_j], _v)
    print("LIVING_HOLD on, brow onsets %d" % len(_onsets))

# ---------- render loop ----------
import os as _os
if _os.environ.get("DUMP_OBJS"):
    for _o in bpy.data.objects:
        if _o.type == 'MESH':
            _mn = _o.data.materials[0].name if _o.data.materials else 'NONE'
            print("OBJDBG", _o.name, _mn,
                  [round(v, 3) for v in _o.location],
                  [round(v, 3) for v in _o.scale])

_FROM = int(os.environ.get("FRAME_FROM", "0") or 0)
if _FROM:
    print("PARTIAL RENDER from frame %d of %d" % (_FROM, N))
for i in range(_FROM, N):
    op = float(MOUTH[i]) if i < len(MOUTH) else 0.0
    op = max(0.0, min(1.0, op))
    _in_still = STILL1 > STILL0 and STILL0 <= i < STILL1
    # breathing rides on the head GROUP. The torso is fully occluded by the wider
    # head (head half-width 0.74 vs torso 0.50, and its top edge sits behind the
    # head), so scaling the torso produced a measured 0 px change — a living hold
    # that exists in code and nowhere on screen.
    _ph = 2 * math.pi * i / (FPS * 4.2)
    _bob = 0.0 if _in_still else (
        HEAD_BOB * (0.55 * math.sin(_ph) + 0.45 * math.sin(2 * _ph + 1.2)) if LIVING else 0.0)
    # keep the opening clearly WIDER than tall: 0.52 x <=0.22. A 0.36-tall
    # opening on a 0.38-wide mouth renders as a square block (reads as a nose).
    h = 0.016 + 0.20 * op
    mouth.scale.z = h / 2.0
    mouth.location.z = MOUTH_TOP - h / 2.0 + _bob
    # Blink (one action at a time: eyes act in the gaps, never under a loud
    # vowel). Scheduled after frame 48 so the face-QC frames are always open.
    # Close over 1 frame, hold 2, open over 2. Width stays constant: a blink is
    # a lid line, not a missing eye.
    bf = (i - 48) % 106
    # never END on a blink: the last frame is the one the viewer holds, and a squashed
    # eye plate there reads as a broken face rather than a blink.
    _no_blink = _in_still or i >= N - 8
    if (not _no_blink) and 48 <= i and bf in (0, 5):
        ez, pz = 0.055, 0.012
    elif (not _no_blink) and 48 <= i and bf in (1, 2, 3, 4):
        ez, pz = 0.006, 0.0008
    else:
        ez, pz = 0.12, 0.060
    for e in EYES:
        e.scale.z = ez
    for p in PUPS:
        p.scale.z = pz
    # slow push-in across the clip: 1.4% of frame — enough to stop the shot
    # reading as a locked-off slab, too small to notice as a move
    cam.ortho_scale = CAM_O - 0.08 * (i / max(1, N - 1))
    if LIVING:
        for _o, _z0 in HEAD_PARTS:
            _o.location.z = _z0 + _bob
        # Brow: the ordinary accent leads each sentence; inside the pop window the
        # SAME lift runs at BROW_POP so the button's face change is bigger than every
        # other accent without inventing a second brow control.
        _in_drop = DROP1 > DROP0 and DROP0 <= i < DROP1
        _lift = 0.0 if _in_still else BROW_LIFT * brow_lift[i]
        if _in_drop:
            _lift *= BROW_POP
            _lift = max(_lift, BROW_LIFT * BROW_POP * 0.85)
        for _b in BROWS:
            _b.location.z = BROW_Z + _lift + _bob
    bpy.context.view_layer.update()
    scene.frame_set(i)
    scene.render.filepath = os.path.join(OUT, "frame_%05d.jpg" % i)
    bpy.ops.render.render(write_still=True)
    if i < 8:
        print("MOUTHDBG", i, round(op, 3), round(h, 3))

if _FROM:
    print("CLEAN_RENDER_PARTIAL_OK", N - _FROM)
else:
    print("CLEAN_RENDER_OK", N)
