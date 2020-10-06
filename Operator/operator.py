import bpy
from .. Functions import functions


C = bpy.context
D = bpy.data
O = bpy.ops


class SelectSimObjects(bpy.types.Operator):
    bl_idname = "my_operator.select_sim"
    bl_label = "Select Similar Objects"
    bl_description = ""

    def execute(self, context):
        # get selected object
        activeObject = bpy.context.active_object
        functions.selectSimilarObjects(activeObject, bpy.context.scene.objects, context.scene.do_instanciate)

        return {"FINISHED"}
    
class InstanceSelected(bpy.types.Operator):
    bl_idname = "my_operator.instance_sel"
    bl_label = "Origin to Geometry and instance selected objects"
    bl_description = ""

    def execute(self, context):
        functions.makeLinks()
        return {"FINISHED"}









bpy.types.Scene.do_instanciate = bpy.props.BoolProperty(
    name="Use Instanciation", default=False)
bpy.types.Scene.dimension_threshold = bpy.props.FloatProperty(default=0, name="Dim Threshold")


