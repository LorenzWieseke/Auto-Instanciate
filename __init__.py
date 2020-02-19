import os
import bpy
import mathutils
from .transfrom import *
import numpy as np
bl_info = {
    "name": "Select all Objects that have the same Polycount",
    "description": "",
    "author": "Lorenz Wieseke",
    "version": (0, 0, 1),
    "blender": (2, 80, 0),
    "location": "View3D -> Property Panel -> My Tools",
    "warning": "This addon is still in development.",
    "wiki_url": "",
    "category": "Object"}


os.system("cls")


class SelectSimObjects(bpy.types.Operator):
    bl_idname = "my_operator.select_sim"
    bl_label = "Select Similar Objects"
    bl_description = ""

    def execute(self, context):
        # get selected object
        activeObject = bpy.context.active_object
        selectSimilarObjects(
            activeObject, bpy.context.scene.objects, context.scene.do_instanciate)

        return {"FINISHED"}

def selectSimilarObjects(activeObject, objectsToIterate, doInstanciate):
    threshold = bpy.context.scene.dimension_threshold

    for element in objectsToIterate:
        if element.type != "MESH" or element == activeObject:
            continue
        if (len(element.data.vertices) == len(activeObject.data.vertices) and
            len(element.data.polygons) == len(activeObject.data.polygons) and
            len(element.data.edges) == len(activeObject.data.edges)):
            # threshold for dimension
            active_dim = activeObject.dimensions
            element_dim = element.dimensions
            diff = active_dim - element_dim

            if (diff.magnitude <= threshold):
                element.select_set(True)
                if doInstanciate:
                    get_rotation_diff(activeObject,element)
                    makeLinks()

def get_rotation_diff(object_a,object_b):

    points_a = [vert.co for vert in object_a.data.vertices]
    points_b = [(object_b.matrix_world @ vert.co) for vert in object_b.data.vertices]
    # Get Transformation from Points A to B
    new_matrix = getTransformation(points_a, points_b)
    new_matrix = mathutils.Matrix(new_matrix).transposed()
    print(object_b.matrix_world) 
    print(new_matrix)

    object_b.matrix_world = new_matrix
    # print(R[0])

def makeLinks():
        # set new Origin and make instances
    # bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
    bpy.ops.object.make_links_data(type='OBDATA')


bpy.types.Scene.do_instanciate = bpy.props.BoolProperty(
    name="Use Instanciation", default=False)
bpy.types.Scene.dimension_threshold = bpy.props.FloatProperty(default=0, name="Dim Threshold")


class SelectSimPanel(bpy.types.Panel):
    bl_idname = "Mesh_Tools_PT_sel_sim"
    bl_label = "Select Similar Object"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    # bl_category = "Selection Tools"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        col = layout.column()
        col.prop(scene, "do_instanciate")
        col.prop(scene, "dimension_threshold")
        col.operator("my_operator.select_sim", text="Select Similar Objects")

        # row = layout.row()
        # row.operator("my_operator.automate_instances", text="Instance Auto")


def register():
    bpy.utils.register_class(SelectSimPanel)
    bpy.utils.register_class(SelectSimObjects)
    # bpy.utils.register_class(AutomateInstances)


def unregister():
    bpy.utils.unregister_class(SelectSimPanel)
    bpy.utils.unregister_class(SelectSimObjects)
    # bpy.utils.unregister_class(AutomateInstances)
