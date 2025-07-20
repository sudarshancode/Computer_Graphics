import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Functions for transformations
def translate(points, tx, ty, tz):
    T = np.array([tx, ty, tz])
    return points + T

def scale(points, sx, sy, sz):
    S = np.diag([sx, sy, sz])
    return np.dot(points, S)

def rotate_x(points, angle):
    rad = np.radians(angle)
    R = np.array([
        [1, 0, 0],
        [0, np.cos(rad), -np.sin(rad)],
        [0, np.sin(rad), np.cos(rad)]
    ])
    return np.dot(points, R)

def rotate_y(points, angle):
    rad = np.radians(angle)
    R = np.array([
        [np.cos(rad), 0, np.sin(rad)],
        [0, 1, 0],
        [-np.sin(rad), 0, np.cos(rad)]
    ])
    return np.dot(points, R)

def rotate_z(points, angle):
    rad = np.radians(angle)
    R = np.array([
        [np.cos(rad), -np.sin(rad), 0],
        [np.sin(rad), np.cos(rad), 0],
        [0, 0, 1]
    ])
    return np.dot(points, R)

def plot_objects(original, transformed):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    ax.scatter(original[:,0], original[:,1], original[:,2], c='b', label='Original')
    ax.scatter(transformed[:,0], transformed[:,1], transformed[:,2], c='r', label='Transformed')
    
    ax.set_title('3D Transformations')
    ax.legend()
    plt.show()

# Main
if __name__ == "__main__":
    # Example object: cube with 8 vertices
    object_points = np.array([
        [0, 0, 0],
        [1, 0, 0],
        [1, 1, 0],
        [0, 1, 0],
        [0, 0, 1],
        [1, 0, 1],
        [1, 1, 1],
        [0, 1, 1]
    ])

    print("Original Object Points:\n", object_points)

    # Input: transformations
    tx, ty, tz = map(float, input("Enter translation (tx ty tz): ").split())
    sx, sy, sz = map(float, input("Enter scaling (sx sy sz): ").split())
    rx, ry, rz = map(float, input("Enter rotation angles (in degrees) for X Y Z: ").split())

    # Apply transformations
    transformed = object_points.copy()
    transformed = scale(transformed, sx, sy, sz)
    transformed = rotate_x(transformed, rx)
    transformed = rotate_y(transformed, ry)
    transformed = rotate_z(transformed, rz)
    transformed = translate(transformed, tx, ty, tz)

    print("Transformed Object Points:\n", transformed)

    # Plotting
    plot_objects(object_points, transformed)
