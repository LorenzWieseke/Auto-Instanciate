import bpy

class SelectSimPanel(bpy.types.Panel):
    bl_idname = "Scene_Tools_PT_sel_sim"
    bl_label = "Select Similar"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    # bl_category = "Selection Tools"

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        row = layout.row()
        row.prop(scene, "do_instanciate")
        row.prop(scene, "dimension_threshold")
        row = layout.row()
        row.operator("my_operator.select_sim", text="Select Similar Objects")
        
        
class SceneToolsPanel(bpy.types.Panel):
    bl_idname = "Scene_Tools_PT_scene_tools"
    bl_label = "Organize Scene"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    # bl_category = "Selection Tools"

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        row = layout.row()
        row.operator("my_operator.select_children", text="Select Children")
        
        row = layout.row()
        row.operator("my_operator.empty_to_collection", text="Generate Collections")
        
        row = layout.row()
        row.operator("my_operator.clear_custom_normals", text="Clear Custom Normals")