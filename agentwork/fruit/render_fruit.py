#!/usr/bin/env python3
"""Fruit-drama renderer (Cantina pattern): one speaker per shot, 3D fruit with
horizontal brows, real horizontal mouth driven by the audio envelope, arms
RESTING STATIC, one clean silhouette hook each, nothing crossing the face.

Invoked by Blender:
  FRUIT_ENV=<session.json> FRUIT_OUT=<frame_dir> blender -b --factory-startup --python render_fruit.py
QC mode:
  FRUIT_STILLS="tomato:0.0,tomato:0.6,..." FRUIT_OUT=<dir> blender -b --factory-startup --python render_fruit.py
Prints FRUIT_RENDER_OK <count> on success.
"""
import bpy, math, os, json

FENV = os.environ.get("FRUIT_ENV") or os.environ.get("BRAIN_ENV")
OUT = os.environ.get("FRUIT_OUT") or os.environ.get("BRAIN_OUT")
if not OUT:
    raise SystemExit("render_fruit: FRUIT_OUT required")
os.makedirs(OUT, exist_ok=True)

# Default startup cube/camera/light MUST go; its cube sits at the origin and
# occludes the rig below z=1.0.
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

GEO = bpy.context.scene.collection


def s2l(c):
    """sRGB -> linear. Emission colours are linear; without this every palette
    value renders washed out (0.82 red displays as salmon pink)."""
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def emat(name, rgb):
    rgb = [s2l(c) for c in rgb]
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


KEY = (0.35, -0.80, 0.48)


def celmat(name, base, shade):
    """Two-tone cel: Geometry.Normal DOT key light through a threshold.
    Without this a pure-emission sphere renders as a flat disc (no volume)."""
    base = [s2l(c) for c in base]
    shade = [s2l(c) for c in shade]
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    nt = m.node_tree
    nt.nodes.clear()
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    geo = nt.nodes.new("ShaderNodeNewGeometry")
    dot = nt.nodes.new("ShaderNodeVectorMath")
    dot.operation = 'DOT_PRODUCT'
    dot.inputs[1].default_value = KEY
    nt.links.new(geo.outputs["Normal"], dot.inputs[0])
    gt = nt.nodes.new("ShaderNodeMath")
    gt.operation = 'GREATER_THAN'
    gt.inputs[1].default_value = 0.06
    nt.links.new(dot.outputs["Value"], gt.inputs[0])
    lit = tuple(min(1.0, c * 1.18) for c in base)

    def tone(col, nm):
        e = nt.nodes.new("ShaderNodeEmission")
        e.name = nm
        e.inputs["Color"].default_value = (*col, 1.0)
        return e

    e_dark = tone(shade, "dark")
    e_mid = tone(base, "mid")
    e_lit = tone(lit, "lit")
    # second threshold separates the shadow tone from the mid tone
    gt2 = nt.nodes.new("ShaderNodeMath")
    gt2.operation = 'GREATER_THAN'
    gt2.inputs[1].default_value = -0.28
    nt.links.new(dot.outputs["Value"], gt2.inputs[0])
    mix_inner = nt.nodes.new("ShaderNodeMixShader")
    nt.links.new(gt.outputs["Value"], mix_inner.inputs[0])
    nt.links.new(e_mid.outputs["Emission"], mix_inner.inputs[1])
    nt.links.new(e_lit.outputs["Emission"], mix_inner.inputs[2])
    mix_outer = nt.nodes.new("ShaderNodeMixShader")
    nt.links.new(gt2.outputs["Value"], mix_outer.inputs[0])
    nt.links.new(e_dark.outputs["Emission"], mix_outer.inputs[1])
    nt.links.new(mix_inner.outputs["Shader"], mix_outer.inputs[2])
    nt.links.new(mix_outer.outputs["Shader"], out.inputs["Surface"])
    return m


def sphere(name, loc, radius, mat, scale=(1, 1, 1), segs=24, rings=12):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=segs, ring_count=rings,
                                         radius=radius, location=loc)
    o = bpy.context.object
    o.name = name
    o.scale = scale
    o.data.materials.append(mat)
    bpy.ops.object.shade_smooth()
    return o


def box(name, loc, scale, mat):
    bpy.ops.mesh.primitive_cube_add(size=2, location=loc)
    o = bpy.context.object
    o.name = name
    o.scale = scale
    o.data.materials.append(mat)
    return o


def cone(name, loc, radius, depth, mat, rot=(0, 0, 0)):
    bpy.ops.mesh.primitive_cone_add(vertices=16, radius1=radius, radius2=0.0,
                                    depth=depth, location=loc, rotation=rot)
    o = bpy.context.object
    o.name = name
    o.data.materials.append(mat)
    bpy.ops.object.shade_smooth()
    return o

# ---------------------------------------------------------------- scene setup
STILLS = os.environ.get("FRUIT_STILLS")
if STILLS:
    S = dict(w=540, h=960, fps=24, nframes=1, bg=[0.11, 0.16, 0.26],
             bg2=[0.30, 0.24, 0.34], shelf=[0.16, 0.12, 0.10], chars={}, scenes=[])
    if FENV and os.path.exists(FENV):
        S = json.load(open(FENV))   # QC the REAL cast, not stand-in tomato/lemon/avocado
else:
    S = json.load(open(FENV))

W, H, FPS, N = int(S["w"]), int(S["h"]), int(S["fps"]), int(S["nframes"])
BG, BG2 = S["bg"], S["bg2"]
SHELF = S.get("shelf", [0.16, 0.12, 0.10])

scene = bpy.context.scene
scene.render.engine = "CYCLES"
scene.cycles.samples = 1
scene.cycles.use_denoising = False
scene.render.resolution_x, scene.render.resolution_y = W, H
scene.render.resolution_percentage = 100
scene.render.image_settings.file_format = "JPEG"
scene.render.image_settings.quality = 92
scene.view_settings.view_transform = "Standard"
scene.render.film_transparent = False
scene.world.color = (0.0, 0.0, 0.0)

# backdrop: stacked bands, gradient + shelf line behind the cast
bg_mats = []
for i in range(24):
    t = i / 23.0
    col = [BG[k] * (1 - t) + BG2[k] * t for k in range(3)]
    m = emat("bgband%02d" % i, col)
    box("bg%02d" % i, (0, 1.6, -1.6 + t * 3.6), (4.0, 0.02, 0.083), m)
box("shelf_top", (0, 0.9, -0.40), (4.0, 0.35, 0.05), emat("shelf_top", SHELF))
box("shelf_face", (0, 0.78, -0.62), (4.0, 0.05, 0.22), emat("shelf_face", [c * 0.7 for c in SHELF]))

cam = bpy.data.cameras.new("cam")
cam.type = "ORTHO"
cam.ortho_scale = 3.9
co = bpy.data.objects.new("cam", cam)
scene.collection.objects.link(co)
co.location = (0.0, -8.0, 0.18)
co.rotation_euler = (math.radians(90), 0.0, 0.0)
scene.camera = co

# ---------------------------------------------------------------- characters
BODY_Z = 0.52          # body centre
R = 0.80               # body radius


def build(name, spec):
    """Returns (objects, mouth_obj, mouth_top_z, mouth_w)."""
    objs = []
    body_m = celmat(name + "_body", spec["body"], spec["shade"])
    acc_m = emat(name + "_acc", spec["accent"])
    leaf_m = emat(name + "_leaf", spec["leaf"])
    white_m = emat(name + "_white", [0.98, 0.98, 0.96])
    dark_m = emat(name + "_dark", [0.06, 0.05, 0.09])
    lip_m = emat(name + "_lip", spec.get("lip", [0.24, 0.05, 0.07]))

    shape = spec.get("shape", "round")
    if shape == "lemon":
        objs.append(sphere(name + "_body", (0, 0, BODY_Z), R, body_m, (1.0, 1.0, 0.80)))
        for side in (-1, 1):
            objs.append(cone(name + "_nub%d" % side, (side * 1.02, 0, BODY_Z), 0.20, 0.44,
                             body_m, rot=(0, math.radians(90 * side), 0)))
    elif shape == "pear":
        objs.append(sphere(name + "_body", (0, 0, BODY_Z - 0.08), R, body_m, (1.0, 1.0, 0.86)))
        objs.append(sphere(name + "_neck", (0, 0, BODY_Z + 0.62), R * 0.62, body_m, (1.0, 1.0, 1.05)))
    else:  # round tomato-ish
        objs.append(sphere(name + "_body", (0, 0, BODY_Z), R, body_m, (1.0, 1.0, 0.86)))

    # ---- feet: planted on the shelf top (z=-0.35), dark shoes ----
    FOOT_Z = -0.245
    for side in (-1, 1):
        objs.append(sphere(name + "_foot%d" % side, (side * 0.30, -0.10, FOOT_Z),
                           0.17, dark_m, (1.05, 1.5, 0.62)))
    # ---- arms: shouldered just OUTSIDE the body silhouette, resting static ----
    def halfw(z):
        if shape == "lemon":
            hw, zc, zr = R, BODY_Z, R * 0.80
        elif shape == "pear":
            hw, zc, zr = R, BODY_Z - 0.08, R * 0.86
        else:
            hw, zc, zr = R, BODY_Z, R * 0.86
        u = (z - zc) / zr
        return hw * math.sqrt(max(0.02, 1.0 - u * u))

    ARM_X = halfw(BODY_Z + 0.06) + 0.035
    for side in (-1, 1):
        sx = side * ARM_X
        objs.append(sphere(name + "_shoulder%d" % side, (sx, 0, BODY_Z + 0.06),
                           0.115, body_m, (1, 1, 1), 14, 8))
        bpy.ops.mesh.primitive_cube_add(size=2, location=(sx, 0, BODY_Z - 0.20))
        o = bpy.context.object
        o.name = name + "_arm%d" % side
        o.scale = (0.052, 0.052, 0.26)
        o.rotation_euler = (0, math.radians(-10 * side), 0)
        o.data.materials.append(body_m)
        objs.append(o)
        objs.append(sphere(name + "_hand%d" % side, (sx + side * 0.045, -0.02, BODY_Z - 0.46),
                           0.098, body_m, (1, 1, 1), 14, 8))

    # ---- face: front surface of the body at eye height ----
    eye_z = BODY_Z + 0.20
    dz = (eye_z - BODY_Z) / (R * (0.86 if shape != "lemon" else 0.80))
    sy = 1.0 if shape != "lemon" else 1.0
    front = -R * sy * math.sqrt(max(0.02, 1.0 - dz * dz))
    for side in (-1, 1):
        ex = side * 0.245
        objs.append(sphere(name + "_eye%d" % side, (ex, front + 0.02, eye_z),
                           0.155, white_m, (1.0, 0.55, 0.85), 16, 8))
        objs.append(sphere(name + "_pupil%d" % side, (ex, front - 0.05, eye_z - 0.005),
                           0.062, dark_m, (1.0, 0.7, 1.15), 12, 8))
        # horizontal brow: box, never rotated, sits above the eye
        objs.append(box(name + "_brow%d" % side, (ex, front + 0.01, eye_z + 0.235),
                        (0.135, 0.035, 0.022), dark_m))

    # ---- mouth: dark horizontal opening anchored at the upper lip line ----
    mouth_top = eye_z - 0.30
    mdz = (mouth_top - BODY_Z) / (R * (0.86 if shape != "lemon" else 0.80))
    mfront = -R * math.sqrt(max(0.02, 1.0 - mdz * mdz))
    mouth = box(name + "_mouth", (0, mfront + 0.020, mouth_top - 0.01),
                (0.235, 0.045, 0.018), lip_m)
    objs.append(mouth)

    # ---- one clean silhouette hook ----
    hook = spec.get("hook", "crown")
    if hook == "crown":          # tomato: leafy crown + stem
        for k in range(6):
            a = k * math.pi / 3.0
            bpy.ops.mesh.primitive_cube_add(size=2, location=(
                math.cos(a) * 0.30, math.sin(a) * 0.30, BODY_Z + R * 0.80))
            o = bpy.context.object
            o.name = name + "_leaf%d" % k
            o.scale = (0.17, 0.06, 0.045)
            o.rotation_euler = (0, 0, a)
            o.data.materials.append(leaf_m)
            objs.append(o)
        objs.append(box(name + "_stem", (0, 0, BODY_Z + R * 0.92), (0.05, 0.05, 0.12), leaf_m))
    elif hook == "nubs":         # lemon: leaf sprig on top
        objs.append(box(name + "_stem", (0, 0, BODY_Z + R * 0.72), (0.045, 0.045, 0.10), leaf_m))
        bpy.ops.mesh.primitive_uv_sphere_add(segments=12, ring_count=6, radius=1,
                                             location=(0.20, 0, BODY_Z + R * 0.86))
        o = bpy.context.object
        o.name = name + "_sprig"
        o.scale = (0.22, 0.05, 0.10)
        o.rotation_euler = (0, 0, math.radians(-25))
        o.data.materials.append(leaf_m)
        objs.append(o)
    elif hook == "stem":         # apple: short stem, no crown
        objs.append(box(name + "_stem", (0, 0, BODY_Z + R * 0.86), (0.045, 0.045, 0.14), leaf_m))
        bpy.ops.mesh.primitive_uv_sphere_add(segments=12, ring_count=6, radius=1,
                                             location=(-0.19, 0, BODY_Z + R * 0.99))
        o = bpy.context.object
        o.name = name + "_leaf"
        o.scale = (0.20, 0.05, 0.09)
        o.rotation_euler = (0, 0, math.radians(22))
        o.data.materials.append(leaf_m)
        objs.append(o)
    elif hook == "leafcap":      # avocado: single broad leaf
        objs.append(box(name + "_stem", (0, 0, BODY_Z + R * 0.95), (0.05, 0.05, 0.14), leaf_m))
        bpy.ops.mesh.primitive_uv_sphere_add(segments=12, ring_count=6, radius=1,
                                             location=(0.26, 0, BODY_Z + R * 1.05))
        o = bpy.context.object
        o.name = name + "_leaf"
        o.scale = (0.30, 0.05, 0.12)
        o.rotation_euler = (0, 0, math.radians(-18))
        o.data.materials.append(leaf_m)
        objs.append(o)
    else:                        # band / cap
        objs.append(box(name + "_cap", (0, 0, BODY_Z + R * 0.74), (0.62, 0.55, 0.10), acc_m))

    return objs, mouth, mouth_top, 0.175


CHARS = {}
SPECS = S.get("chars", {})
if STILLS and not SPECS:
    # QC stand-ins so the sheet can be built before the cast JSON exists
    SPECS = {
        "tomato": dict(body=[0.80, 0.16, 0.18], shade=[0.50, 0.08, 0.10], accent=[0.28, 0.50, 0.20],
                       leaf=[0.22, 0.46, 0.20], shape="round", hook="crown"),
        "lemon": dict(body=[0.95, 0.80, 0.20], shade=[0.64, 0.50, 0.10], accent=[0.30, 0.50, 0.22],
                      leaf=[0.24, 0.48, 0.22], shape="lemon", hook="nubs"),
        "avocado": dict(body=[0.30, 0.42, 0.16], shade=[0.16, 0.24, 0.09], accent=[0.30, 0.50, 0.22],
                        leaf=[0.24, 0.48, 0.22], shape="pear", hook="leafcap"),
    }

for nm, sp in SPECS.items():
    objs, mouth, mtop, mw = build(nm, sp)
    CHARS[nm] = dict(objs=objs, mouth=mouth, top=mtop, w=mw)
    # eyeline control: pupils translate in X together (still a symmetric pair);
    # the brow bar only ever TRANSLATES in Z (rotating it = the diagonal-brow reject)
    CHARS[nm]["pupil"] = [o for o in objs if "_pupil" in o.name]
    CHARS[nm]["brow"] = [o for o in objs if "_brow" in o.name]
    for o in CHARS[nm]["pupil"]:
        o["px"] = o.location.x
    for o in CHARS[nm]["brow"]:
        o["bz"] = o.location.z


def show_only(name):
    for nm, c in CHARS.items():
        vis = (nm == name)
        for o in c["objs"]:
            o.hide_render = not vis


def set_mouth(name, op):
    op = max(0.0, min(1.0, float(op)))
    h = 0.016 + 0.24 * op
    m = CHARS[name]["mouth"]
    m.scale.z = h / 2.0
    m.location.z = CHARS[name]["top"] - h / 2.0


# ---------------------------------------------------------------- QC stills
if STILLS:
    jobs = [j.split(":") for j in STILLS.split(",") if j.strip()]
    for k, (nm, op) in enumerate(jobs):
        nm = nm.strip()
        show_only(nm)
        set_mouth(nm, float(op))
        bpy.context.view_layer.update()
        scene.frame_set(0)
        scene.render.filepath = os.path.join(OUT, "qc_%02d_%s_%s.jpg" % (k, nm, op.replace(".", "")))
        bpy.ops.render.render(write_still=True)
        print("QCSTILL", nm, op)
    print("FRUIT_RENDER_OK", len(jobs))
    raise SystemExit(0)

# ---------------------------------------------------------------- render loop
scenes = S["scenes"]
for i in range(N):
    sc = None
    for s in scenes:
        if s["start"] <= i < s["end"]:
            sc = s
            break
    if sc is None:
        sc = scenes[-1]
    nm = sc["char"]
    show_only(nm)
    k = i - sc["start"]
    op = sc["mouth"][k] if 0 <= k < len(sc["mouth"]) else 0.0
    set_mouth(nm, op)
    # eyeline: both pupils translate together, so the pair stays symmetric
    for o in CHARS[nm].get("pupil", []):
        o.location.x = o["px"] + 0.045 * float(sc.get("gaze", 0.0))
    # reaction brow: vertical translation only
    for o in CHARS[nm].get("brow", []):
        o.location.z = o["bz"] + float(sc.get("brow", 0.0))
    bpy.context.view_layer.update()
    scene.frame_set(i)
    scene.render.filepath = os.path.join(OUT, "frame_%05d.jpg" % i)
    bpy.ops.render.render(write_still=True)
    if i < 6:
        print("MOUTHDBG", i, nm, round(float(op), 3))

print("FRUIT_RENDER_OK", N)
