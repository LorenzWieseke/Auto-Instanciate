import bpy
from bpy.props import *


bpy.types.Scene.do_instanciate = bpy.props.BoolProperty(
    name="Use Instanciation", default=False)
bpy.types.Scene.dimension_threshold = bpy.props.FloatProperty(default=0, name="Dim Threshold")

# class ST_Menu_Settigs(bpy.types.PropertyGroup):
#     open_menu_select_similar: BoolProperty(default=True)
#     open_menu_organize_scene: BoolProperty(default=True)


# bpy.utils.register_class(ST_Menu_Settigs)
# bpy.types.Scene.menu_settings = PointerProperty(type=ST_Menu_Settigs)
