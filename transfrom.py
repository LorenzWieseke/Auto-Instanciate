import numpy as np

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

