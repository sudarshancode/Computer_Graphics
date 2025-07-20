import matplotlib.pyplot as plt

def perspective_projection(x, y, z, d=5):
    # Simple perspective projection
    factor = d / (z + d)
    x_proj = x * factor
    y_proj = y * factor
    return x_proj, y_proj

def draw_wireframe_cube(vertices, edges):
    projected_points = []

    for x, y, z in vertices:
        x2d, y2d = perspective_projection(x, y, z)
        projected_points.append((x2d, y2d))

    # Plotting
    plt.figure()
    for edge in edges:
        x_vals = [projected_points[edge[0]][0], projected_points[edge[1]][0]]
        y_vals = [projected_points[edge[0]][1], projected_points[edge[1]][1]]
        plt.plot(x_vals, y_vals, 'bo-')

    plt.title("3D Wireframe Cube (Projected to 2D)")
    plt.axis('equal')
    plt.grid(True)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

def main():
    print("Enter 8 vertices of the cube (x y z):")
    vertices = []
    for i in range(8):
        coords = input(f"Vertex {i + 1}: ").split()
        x, y, z = map(float, coords)
        vertices.append((x, y, z))

    # Define cube edges by vertex indices
    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0),  # Bottom face
        (4, 5), (5, 6), (6, 7), (7, 4),  # Top face
        (0, 4), (1, 5), (2, 6), (3, 7)   # Side edges
    ]

    draw_wireframe_cube(vertices, edges)

if __name__ == "__main__":
    main()
