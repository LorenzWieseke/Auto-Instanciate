import bpy
import numpy as np
import mathutils

O = bpy.ops


def select_object(obj):
    C = bpy.context

    O.object.select_all(action='DESELECT')
    C.view_layer.objects.active = obj
    obj.select_set(True)

def getChildren(obj): 
    children = [] 
    for ob in bpy.data.objects: 
        if ob.parent == obj: 
            children.append(ob) 
    return children 

def makeLinks():
    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')
    bpy.ops.object.make_links_data(type='OBDATA')
  

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
        # get_rotation_diff(activeObject,element)
        makeLinks()  

# Get Transformation from Points A to B
def getTransformation(pointsA, pointsB):
    pointsA = np.array(pointsA)
    pointsB = np.array(pointsB)

    #Calculate centroids
    ca = np.mean(pointsA,axis=0)
    cb = np.mean(pointsB,axis=0)

    R = np.dot(np.linalg.pinv(pointsA - ca), (pointsB - cb))
    t = cb - np.dot(R, ca)

    R = np.insert(R, 3, t, axis=0)
    R = np.insert(R, 3, [0,0,0,1], axis=1)
    return (R)



def get_rotation_diff(object_a,object_b):
    points_a = [vert.co for vert in object_a.data.vertices]
    points_b = [(object_b.matrix_world @ vert.co) for vert in object_b.data.vertices]

    vert_a = [vert.index for vert in object_a.data.vertices]
    vert_b = [vert.index for vert in object_b.data.vertices]

    print("I1 : \n")
    print(vert_a)

    print("I2 : \n")
    print(vert_b)
    
    # for i in range(len(vert_a)):
    #     vert_b[i].index = vert_a[i].index

    # Get Transformation from Points A to B
    new_matrix = getTransformation(points_a, points_b)
    new_matrix = mathutils.Matrix(new_matrix).transposed()


    object_b.matrix_world = new_matrix




