import bpy
from .. Functions import functions


C = bpy.context
D = bpy.data
O = bpy.ops


class SelectSimObjects(bpy.types.Operator):
    bl_idname = "my_operator.select_sim"
    bl_label = "Select Similar Objects"
    bl_description = "Select Similar Objects"

    def execute(self, context):
        # get selected object
        activeObject = bpy.context.active_object
        functions.selectSimilarObjects(activeObject, bpy.context.scene.objects, context.scene.do_instanciate)

        return {"FINISHED"}


class SelectChildren(bpy.types.Operator):
    bl_idname = "my_operator.select_children"
    bl_label = "Select all childern of all selected Parents"
    bl_description = "Select all childern of all selected Parent"

    def execute(self, context):
        
        selection = bpy.context.selected_objects
        for obj in selection:
            bpy.context.view_layer.objects.active = obj
            bpy.ops.object.select_grouped(extend=True, type='CHILDREN_RECURSIVE')

        return {"FINISHED"}
    
class ClearCustomNormals(bpy.types.Operator):
    bl_idname = "my_operator.clear_custom_normals"
    bl_label = "Clear custom normals on selected objects"
    bl_description = "Clear custom normals on selected objects"

    def execute(self, context):
        
        selection = bpy.context.selected_objects

        for obj in selection:
            bpy.context.view_layer.objects.active = obj
            bpy.ops.mesh.customdata_custom_splitnormals_clear()

        return {"FINISHED"}

class EmptyToCollection(bpy.types.Operator):
    bl_idname = "my_operator.empty_to_collection"
    bl_label = "Create a Collection for each selected Empty and put it and its children inside the collection"
    bl_description = "Create a Collection for each selected Empty and put it and its children inside the collection"

    def execute(self, context):
        
        D = bpy.data
        C = bpy.context
        
        selection = bpy.context.selected_objects
        for obj in selection:
            
            # add collection
            col_name = obj.name

            if D.collections.get(col_name) is None:
                D.collections.new(col_name)
            
            new_col = D.collections.get(col_name)
            
            # link collection to scene
            if new_col.name not in context.scene.collection.children:
                context.scene.collection.children.link(new_col)

            # select all children
            children = functions.getChildren(obj)           

            # add to new colleciton
            for child in children:
                if child not in list(new_col.all_objects):
                    new_col.objects.link(child)
            
            # add parent to collection
            new_col.objects.link(obj)
            

        return {"FINISHED"}








