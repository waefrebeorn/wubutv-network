import bpy, math
from mathutils import Vector

OUTDIR = "/home/hatch/workspace/wubutv-network/musicvideo/visual-forms/blender-proof/frames/frame_"

def srgb2lin(c):
    return ((c + 0.055) / 1.055) ** 2.4 if c > 0.04045 else c / 12.92

def mat(name, rgba):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    lin = tuple(srgb2lin(c) for c in rgba[:3]) + (rgba[3],)
    m.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = lin
    return m

def look_at(obj, target):
    d = Vector(target) - obj.location
    obj.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()

bpy.ops.wm.read_factory_settings(use_empty=True)
scene = bpy.context.scene
scene.frame_start = 1
scene.frame_end = 24
scene.render.fps = 24

bpy.ops.mesh.primitive_plane_add(size=30, location=(0, 0, 0))
bpy.context.active_object.data.materials.append(mat("INK", (0.078, 0.078, 0.078, 1)))

# cadmium cube: slides left->right while spinning
bpy.ops.mesh.primitive_cube_add(size=1.5, location=(-3.0, 0, 0.75))
cube = bpy.context.active_object
cube.data.materials.append(mat("CADMIUM", (1.0, 0.776, 0.118, 1)))
cube.keyframe_insert("location", frame=1)
cube.keyframe_insert("rotation_euler", frame=1)
cube.location.x = 3.0
cube.rotation_euler.z = math.radians(180)
cube.keyframe_insert("location", frame=24)
cube.keyframe_insert("rotation_euler", frame=24)

# cobalt sphere bouncing gently (scale/height arc via location z)
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.7, location=(0, 1.8, 0.7))
sph = bpy.context.active_object
sph.data.materials.append(mat("COBALT", (0.106, 0.247, 0.82, 1)))
sph.keyframe_insert("location", frame=1)
sph.location.z = 2.1
sph.keyframe_insert("location", frame=12)
sph.location.z = 0.7
sph.keyframe_insert("location", frame=24)

cam_data = bpy.data.cameras.new("Cam")
cam = bpy.data.objects.new("Cam", cam_data)
scene.collection.objects.link(cam)
cam.location = (5.5, -8.5, 4.2)
look_at(cam, (0, 0, 1.0))
scene.camera = cam

ld = bpy.data.lights.new("Key", 'AREA')
ld.energy = 900; ld.shape = 'DISK'; ld.size = 6
lo = bpy.data.objects.new("Key", ld)
scene.collection.objects.link(lo)
lo.location = (4, -3, 7)
look_at(lo, (0, 0, 0.8))

world = bpy.data.worlds.new("W")
world.use_nodes = True
world.node_tree.nodes["Background"].inputs[0].default_value = (0.008, 0.008, 0.012, 1.0)
scene.world = world

scene.render.engine = 'CYCLES'
scene.cycles.device = 'CPU'
scene.cycles.samples = 8
scene.cycles.use_denoising = True
scene.render.resolution_x = 640
scene.render.resolution_y = 360
scene.render.resolution_percentage = 100
scene.render.image_settings.file_format = 'PNG'
scene.render.filepath = OUTDIR
bpy.ops.render.render(animation=True)
print("ANIM_DONE")
