import bpy, traceback
from mathutils import Vector

OUT = "/home/hatch/workspace/wubutv-network/musicvideo/visual-forms/blender-proof/gp_frame.png"

def look_at(obj, target):
    d = Vector(target) - obj.location
    obj.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()

try:
    print("GP_TYPES:", [t for t in dir(bpy.types) if 'Grease' in t or 'GPencil' in t][:12])
    bpy.ops.wm.read_factory_settings(use_empty=True)
    scene = bpy.context.scene

    # Grease Pencil v3 object (4.5: must be created via the operator)
    bpy.ops.object.grease_pencil_add(type='EMPTY')
    gp_obj = bpy.context.active_object
    gp_data = gp_obj.data

    layer = gp_data.layers.new(name="Sketch", set_active=True)
    drawing = layer.frames.new(1).drawing

    # a simple storyboard-ish sketch: horizon line + box (panel) + sun circle, as polylines
    strokes_pts = [
        [(-3, 0, 0.2), (3, 0, 0.2)],                                        # horizon
        [(-2.2, 0, 0.2), (-2.2, 0, 2.0), (0.6, 0, 2.0), (0.6, 0, 0.2), (-2.2, 0, 0.2)],  # panel box
        [(1.8, 0, 1.9), (2.3, 0, 1.65), (2.05, 0, 1.15), (1.55, 0, 1.4), (1.8, 0, 1.9)], # sun blob
    ]
    drawing.add_strokes([len(p) for p in strokes_pts])
    for si, pts in enumerate(strokes_pts):
        stroke = drawing.strokes[si]
        for pi, co in enumerate(pts):
            pt = stroke.points[pi]
            pt.position = co
            pt.radius = 0.03

    # GP material (cadmium strokes)
    gmat = bpy.data.materials.new("GPMat")
    bpy.data.materials.create_gpencil_data(gmat)
    gmat.grease_pencil.color = (1.0, 0.776, 0.118, 1.0)
    gp_data.materials.append(gmat)

    cam_data = bpy.data.cameras.new("Cam")
    cam = bpy.data.objects.new("Cam", cam_data)
    scene.collection.objects.link(cam)
    cam.location = (0, -7, 1.2)
    look_at(cam, (0, 0, 1.0))
    scene.camera = cam

    ld = bpy.data.lights.new("Key", 'SUN')
    ld.energy = 3
    lo = bpy.data.objects.new("Key", ld)
    scene.collection.objects.link(lo)
    lo.location = (2, -3, 6)

    world = bpy.data.worlds.new("W")
    world.use_nodes = True
    world.node_tree.nodes["Background"].inputs[0].default_value = (0.95, 0.93, 0.86, 1.0)
    scene.world = world

    scene.render.engine = 'CYCLES'
    scene.cycles.device = 'CPU'
    scene.cycles.samples = 16
    scene.render.resolution_x = 640
    scene.render.resolution_y = 360
    scene.render.image_settings.file_format = 'PNG'
    scene.render.filepath = OUT
    scene.frame_set(1)
    bpy.ops.render.render(write_still=True)
    print("GP_OK", OUT)
except Exception:
    print("GP_FAIL")
    traceback.print_exc()
