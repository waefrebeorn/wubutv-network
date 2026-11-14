import bpy, math
from mathutils import Vector

OUT = "/home/hatch/workspace/wubutv-network/musicvideo/visual-forms/blender-proof/wubu_still.png"

PALETTE = {
    "COBALT":   (0x1B/255, 0x3F/255, 0xD1/255, 1.0),
    "VERMILION":(0xE2/255, 0x3A/255, 0x1B/255, 1.0),
    "CADMIUM":  (0xFF/255, 0xC6/255, 0x1E/255, 1.0),
    "BONE":     (0xF4/255, 0xEE/255, 0xDC/255, 1.0),
    "INK":      (0x14/255, 0x14/255, 0x14/255, 1.0),
}

def srgb2lin(c):
    return ((c + 0.055) / 1.055) ** 2.4 if c > 0.04045 else c / 12.92

def mat(name, rgba):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    bsdf = m.node_tree.nodes["Principled BSDF"]
    lin = tuple(srgb2lin(c) for c in rgba[:3]) + (rgba[3],)
    bsdf.inputs["Base Color"].default_value = lin
    bsdf.inputs["Roughness"].default_value = 0.55
    return m

def look_at(obj, target):
    d = Vector(target) - obj.location
    obj.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()

# clean scene
bpy.ops.wm.read_factory_settings(use_empty=True)
scene = bpy.context.scene

# ground
bpy.ops.mesh.primitive_plane_add(size=30, location=(0, 0, 0))
bpy.context.active_object.data.materials.append(mat("INK", PALETTE["INK"]))

# cobalt cube
bpy.ops.mesh.primitive_cube_add(size=1.6, location=(-2.2, 0, 0.8))
bpy.context.active_object.data.materials.append(mat("COBALT", PALETTE["COBALT"]))

# vermilion sphere
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.85, location=(0, 0.3, 0.85))
bpy.context.active_object.data.materials.append(mat("VERMILION", PALETTE["VERMILION"]))

# cadmium cone
bpy.ops.mesh.primitive_cone_add(radius1=0.8, depth=1.8, location=(2.2, 0, 0.9))
bpy.context.active_object.data.materials.append(mat("CADMIUM", PALETTE["CADMIUM"]))

# WUBU text in bone
bpy.ops.object.text_add(location=(0, 0.6, 2.0), rotation=(math.radians(90), 0, 0))
txt = bpy.context.active_object
txt.data.body = "WUBU"
txt.data.align_x = 'CENTER'
txt.data.size = 1.0
txt.data.extrude = 0.06
txt.data.materials.append(mat("BONE", PALETTE["BONE"]))

# camera
cam_data = bpy.data.cameras.new("Cam")
cam = bpy.data.objects.new("Cam", cam_data)
scene.collection.objects.link(cam)
cam.location = (5.5, -8.5, 4.2)
look_at(cam, (0, 0, 1.0))
scene.camera = cam

# lights
ld = bpy.data.lights.new("Key", 'AREA')
ld.energy = 900; ld.shape = 'DISK'; ld.size = 6
lo = bpy.data.objects.new("Key", ld)
scene.collection.objects.link(lo)
lo.location = (4, -3, 7)
look_at(lo, (0, 0, 0.8))

world = bpy.data.worlds.new("W")
world.use_nodes = True
world.node_tree.nodes["Background"].inputs[0].default_value = (0.008, 0.008, 0.012, 1.0)
world.node_tree.nodes["Background"].inputs[1].default_value = 1.0
scene.world = world

scene.render.engine = 'CYCLES'
scene.cycles.device = 'CPU'
scene.cycles.samples = 16
scene.cycles.use_denoising = True
scene.render.resolution_x = 640
scene.render.resolution_y = 360
scene.render.resolution_percentage = 100
scene.render.image_settings.file_format = 'PNG'
scene.render.filepath = OUT
scene.frame_set(1)
bpy.ops.render.render(write_still=True)
print("STILL_DONE", OUT)
