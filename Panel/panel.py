import bpy

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

        row = layout.row()
        row.operator("my_operator.instance_sel", text="Instance Auto")