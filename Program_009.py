import matplotlib.pyplot as plt

def liang_barsky(xmin, xmax, ymin, ymax, x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    p = [-dx, dx, -dy, dy]
    q = [x1 - xmin, xmax - x1, y1 - ymin, ymax - y1]

    u1, u2 = 0.0, 1.0

    for i in range(4):
        if p[i] == 0:
            if q[i] < 0:
                return None  # Line is parallel and outside the clipping window
        else:
            u = q[i] / p[i]
            if p[i] < 0:
                u1 = max(u1, u)
            else:
                u2 = min(u2, u)

    if u1 > u2:
        return None  # Line is outside the window

    clipped_x1 = x1 + u1 * dx
    clipped_y1 = y1 + u1 * dy
    clipped_x2 = x1 + u2 * dx
    clipped_y2 = y1 + u2 * dy

    return (clipped_x1, clipped_y1, clipped_x2, clipped_y2)

def draw_clipping_window(xmin, xmax, ymin, ymax):
    plt.plot([xmin, xmax], [ymin, ymin], 'k')  # Bottom
    plt.plot([xmin, xmax], [ymax, ymax], 'k')  # Top
    plt.plot([xmin, xmin], [ymin, ymax], 'k')  # Left
    plt.plot([xmax, xmax], [ymin, ymax], 'k')  # Right

def main():
    # Input for clipping window
    xmin = float(input("Enter xmin: "))
    xmax = float(input("Enter xmax: "))
    ymin = float(input("Enter ymin: "))
    ymax = float(input("Enter ymax: "))

    # Input for line endpoints
    x1 = float(input("Enter x1 (start point): "))
    y1 = float(input("Enter y1 (start point): "))
    x2 = float(input("Enter x2 (end point): "))
    y2 = float(input("Enter y2 (end point): "))

    # Perform Liang-Barsky clipping
    result = liang_barsky(xmin, xmax, ymin, ymax, x1, y1, x2, y2)

    plt.figure()
    draw_clipping_window(xmin, xmax, ymin, ymax)

    # Draw original line
    plt.plot([x1, x2], [y1, y2], 'r--', label="Original Line")

    if result:
        cx1, cy1, cx2, cy2 = result
        plt.plot([cx1, cx2], [cy1, cy2], 'g', linewidth=2, label="Clipped Line")
        print(f"Clipped Line Coordinates: ({cx1:.2f}, {cy1:.2f}) to ({cx2:.2f}, {cy2:.2f})")
    else:
        print("Line is completely outside the clipping window.")

    plt.title("Liang-Barsky Line Clipping")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()

if __name__ == "__main__":
    main()
