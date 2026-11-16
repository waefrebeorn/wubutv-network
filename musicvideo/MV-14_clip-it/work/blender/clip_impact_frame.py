# MV-14 content-aware impact frame — the glowing CLIP in the cutting room at night.
# Blender 4.5.15, Cycles CPU, 1280x720. No generated imagery: all geometry +
# materials are built here. Run:
#   ~/workspace/tools/blender/blender-4.5.15-linux-x64/blender -b --python clip_impact_frame.py
# Output: clip_impact_frame.png (same dir).
import bpy
import math

# ---- clean scene ------------------------------------------------------------
bpy.ops.wm.read_factory_settings(use_empty=True)

# ---- render / world ---------------------------------------------------------
scene = bpy.context.scene
scene.render.engine = "CYCLES"
scene.cycles.device = "CPU"
scene.cycles.samples = 64
scene.cycles.use_denoising = True
scene.cycles.denoiser = "OPENIMAGEDENOISE"
scene.render.resolution_x = 1280
scene.render.resolution_y = 720
scene.render.resolution_percentage = 100
scene.render.image_settings.file_format = "PNG"
scene.render.filepath = "/home/hatch/workspace/wubutv-network/musicvideo/MV-14_clip-it/work/blender/clip_impact_frame.png"
scene.view_settings.exposure = 0.6  # look left at default (AgX in 4.5; Filmic removed)

world = bpy.data.worlds.get("World") or bpy.data.worlds.new("World")
scene.world = world
world.use_nodes = True
bg = world.node_tree.nodes["Background"]
bg.inputs["Color"].default_value = (0.008, 0.011, 0.028, 1.0)
bg.inputs["Strength"].default_value = 1.0


def mat(name, color, roughness=0.8, metallic=0.0, emission=None, e_strength=0.0):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    bsdf = m.node_tree.nodes["Principled BSDF"]
    bsdf.inputs["Base Color"].default_value = (*color, 1.0)
    bsdf.inputs["Roughness"].default_value = roughness
    bsdf.inputs["Metallic"].default_value = metallic
    if emission is not None:
        bsdf.inputs["Emission Color"].default_value = (*emission, 1.0)
        bsdf.inputs["Emission Strength"].default_value = e_strength
    return m


def box(name, loc, scale, material, rot=(0, 0, 0)):
    bpy.ops.mesh.primitive_cube_add(location=loc, rotation=rot)
    o = bpy.context.object
    o.name = name
    o.scale = scale
    o.data.materials.append(material)
    return o


def cyl(name, loc, radius, depth, material, rot=(0, 0, 0)):
    bpy.ops.mesh.primitive_cylinder_add(radius=radius, depth=depth,
                                        location=loc, rotation=rot, vertices=48)
    o = bpy.context.object
    o.name = name
    o.data.materials.append(material)
    return o


# ---- materials --------------------------------------------------------------
floor_mat = mat("Floor", (0.05, 0.045, 0.06), roughness=0.9)
wall_mat = mat("Wall", (0.07, 0.06, 0.10), roughness=0.95)
desk_mat = mat("DeskWood", (0.16, 0.10, 0.05), roughness=0.7)
metal_mat = mat("DarkMetal", (0.10, 0.10, 0.11), roughness=0.45, metallic=0.8)
reel_mat = mat("Reel", (0.14, 0.13, 0.12), roughness=0.4, metallic=0.7)
paper_mat = mat("Paper", (0.75, 0.72, 0.62), roughness=0.9)
monitor_mat = mat("MonitorScreen", (0.02, 0.05, 0.06), roughness=0.3,
                  emission=(0.10, 0.55, 0.60), e_strength=1.2)
clip_mat = mat("ClipGlow", (0.05, 0.03, 0.01), roughness=0.3,
               emission=(1.0, 0.72, 0.22), e_strength=7.0)
clip_inner_mat = mat("ClipInner", (0.03, 0.02, 0.01), roughness=0.4,
                     emission=(1.0, 0.68, 0.20), e_strength=0.55)
lamp_mat = mat("LampShade", (0.20, 0.12, 0.04), roughness=0.6)
mug_mat = mat("Mug", (0.10, 0.16, 0.28), roughness=0.5)

# ---- room -------------------------------------------------------------------
box("Floor", (0, 0, -0.05), (7, 6, 0.05), floor_mat)
box("BackWall", (0, 3.0, 1.6), (7, 0.1, 1.65), wall_mat)
box("LeftWall", (-5.5, 0, 1.6), (0.1, 6, 1.65), wall_mat)

# ---- desk + props -----------------------------------------------------------
box("DeskTop", (0, 0.6, 0.74), (2.4, 0.85, 0.06), desk_mat)
box("DeskLegL", (-2.1, 0.6, 0.37), (0.08, 0.7, 0.37), desk_mat)
box("DeskLegR", (2.1, 0.6, 0.37), (0.08, 0.7, 0.37), desk_mat)
# film reels leaning on the desk, left side
cyl("Reel1", (-1.7, 0.7, 1.05), 0.34, 0.06, reel_mat, rot=(math.radians(90), 0, 0))
cyl("Reel1Hub", (-1.7, 0.7, 1.05), 0.09, 0.09, metal_mat, rot=(math.radians(90), 0, 0))
cyl("Reel2", (-1.15, 0.75, 0.98), 0.26, 0.05, reel_mat, rot=(math.radians(78), 0, math.radians(12)))
# splicer block, right side
box("Splicer", (1.75, 0.7, 0.88), (0.32, 0.22, 0.10), metal_mat)
box("SplicerArm", (1.75, 0.7, 1.02), (0.05, 0.20, 0.06), metal_mat,
    rot=(0, 0, math.radians(-18)))
# monitor, back-left on the desk, faint cyan screen
box("Monitor", (-2.3, 1.15, 1.15), (0.45, 0.05, 0.32), metal_mat,
    rot=(math.radians(-6), 0, math.radians(14)))
box("MonitorScreen", (-2.3, 1.11, 1.15), (0.40, 0.02, 0.27), monitor_mat,
    rot=(math.radians(-6), 0, math.radians(14)))
# scattered papers + a film strip on the desk
box("Paper1", (0.9, 0.35, 0.815), (0.28, 0.20, 0.005), paper_mat, rot=(0, 0, math.radians(8)))
box("Paper2", (1.05, 0.75, 0.815), (0.24, 0.18, 0.005), paper_mat, rot=(0, 0, math.radians(-14)))
box("FilmStrip", (-0.5, 0.25, 0.815), (0.85, 0.09, 0.005), metal_mat, rot=(0, 0, math.radians(4)))
# mug
cyl("Mug", (2.05, 0.15, 0.92), 0.09, 0.18, mug_mat)
# desk lamp, back-right, warm practical
cyl("LampBase", (2.35, 1.05, 0.84), 0.11, 0.06, metal_mat)
cyl("LampStem", (2.35, 1.05, 1.05), 0.02, 0.42, metal_mat)
bpy.ops.mesh.primitive_cone_add(radius1=0.16, radius2=0.07, depth=0.18,
                                location=(2.35, 1.05, 1.32),
                                rotation=(math.radians(28), 0, 0))
lamp_shade = bpy.context.object
lamp_shade.name = "LampShade"
lamp_shade.data.materials.append(lamp_mat)

# ---- THE CLIP: blank luminous film-frame rectangle, floating over the desk --
# Frame: 1.7 wide x 1.05 tall, 0.09 border, tilted back slightly, centred
# just right of frame so the desk props read on the left.
clip = bpy.data.collections.new("CLIP")
scene.collection.children.link(clip)
cx, cy, cz = 0.35, 0.55, 1.85
tilt = math.radians(-12)


def clip_bar(name, loc, scale):
    bpy.ops.mesh.primitive_cube_add(location=loc, rotation=(tilt, 0, 0))
    o = bpy.context.object
    o.name = name
    o.scale = scale
    o.data.materials.append(clip_mat)
    for coll in o.users_collection:
        coll.objects.unlink(o)
    clip.objects.link(o)
    return o


clip_bar("ClipTop", (cx, cy, cz + 0.48), (0.85, 0.05, 0.045))
clip_bar("ClipBottom", (cx, cy, cz - 0.48), (0.85, 0.05, 0.045))
clip_bar("ClipLeft", (cx - 0.805, cy, cz), (0.045, 0.05, 0.435))
clip_bar("ClipRight", (cx + 0.805, cy, cz), (0.045, 0.05, 0.435))
# blank luminous interior (no text, no image — the carry stays blank).
# A Blender plane lies flat (normal +Z); rotate 90 deg about X so it faces
# the camera, then tilt back 12 deg to match the frame bars.
bpy.ops.mesh.primitive_plane_add(
    location=(cx, cy, cz), rotation=(math.radians(90) + tilt, 0, 0))
inner = bpy.context.object
inner.name = "ClipInner"
inner.scale = (0.76, 0.44, 1.0)
inner.data.materials.append(clip_inner_mat)
for coll in inner.users_collection:
    coll.objects.unlink(inner)
clip.objects.link(inner)
# perforation dots along top/bottom bars (film-frame read, still blank)
for sx in (-0.55, -0.18, 0.18, 0.55):
    for sz in (0.48, -0.48):
        clip_bar(f"Perf{sx:+.2f}_{sz:+.2f}", (cx + sx, cy - 0.001, cz + sz),
                 (0.035, 0.052, 0.02))

# ---- lights -----------------------------------------------------------------
# cool moonlight fill from the front-top
bpy.ops.object.light_add(type="AREA", location=(-2.5, -4.5, 4.5))
fill = bpy.context.object
fill.name = "MoonFill"
fill.data.energy = 60
fill.data.color = (0.55, 0.65, 1.0)
fill.data.shape = "DISK"
fill.data.size = 3.0
fill.rotation_euler = (math.radians(55), 0, math.radians(20))
# warm practical from the lamp
bpy.ops.object.light_add(type="POINT", location=(2.35, 1.0, 1.25))
lamp_light = bpy.context.object
lamp_light.name = "LampLight"
lamp_light.data.energy = 12
lamp_light.data.color = (1.0, 0.62, 0.28)
lamp_light.data.shadow_soft_size = 0.15
# the CLIP itself is the key light — gold spill onto the desk
bpy.ops.object.light_add(type="POINT", location=(cx, cy - 0.7, cz))
clip_light = bpy.context.object
clip_light.name = "ClipLight"
clip_light.data.energy = 25
clip_light.data.color = (1.0, 0.70, 0.25)
clip_light.data.shadow_soft_size = 0.3

# ---- camera -----------------------------------------------------------------
bpy.ops.object.camera_add(location=(0.1, -5.6, 2.05))
cam = bpy.context.object
cam.name = "Camera"
cam.data.lens = 42
scene.camera = cam
# look at the CLIP
bpy.ops.object.empty_add(location=(cx, cy, cz))
target = bpy.context.object
target.name = "LookAtClip"
con = cam.constraints.new("TRACK_TO")
con.target = target
con.track_axis = "TRACK_NEGATIVE_Z"
con.up_axis = "UP_Y"

bpy.ops.wm.save_as_mainfile(filepath="/home/hatch/workspace/wubutv-network/musicvideo/MV-14_clip-it/work/blender/clip_impact_frame.blend")
print("SCENE BUILT OK — rendering 1280x720 Cycles CPU")
