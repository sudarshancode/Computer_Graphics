# Brezier Curve

import matplotlib.pyplot as plt

def bezier_curve(P0, P1, P2, P3, num_points=1000):
    x_points = []
    y_points = []

    for t in [i/num_points for i in range(num_points+1)]:
        x = (1 - t)**3 * P0[0] + 3 * (1 - t)**2 * t * P1[0] + 3 * (1 - t) * t**2 * P2[0] + t**3 * P3[0]
        y = (1 - t)**3 * P0[1] + 3 * (1 - t)**2 * t * P1[1] + 3 * (1 - t) * t**2 * P2[1] + t**3 * P3[1]
        x_points.append(x)
        y_points.append(y)

    # Plotting the curve
    plt.plot(x_points, y_points, label='Bezier Curve', color='blue')
    
    # Plot control points
    control_x = [P0[0], P1[0], P2[0], P3[0]]
    control_y = [P0[1], P1[1], P2[1], P3[1]]
    plt.plot(control_x, control_y, 'ro--', label='Control Points')  # red points with dashed lines

    plt.title("Cubic Bézier Curve")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()
    plt.grid(True)
    plt.axis("equal")
    plt.show()

# --- Input section ---
print("Enter control points for the Bézier curve (x y):")
P0 = tuple(map(float, input("P0: ").split()))
P1 = tuple(map(float, input("P1: ").split()))
P2 = tuple(map(float, input("P2: ").split()))
P3 = tuple(map(float, input("P3: ").split()))

# --- Draw curve ---
bezier_curve(P0, P1, P2, P3)
