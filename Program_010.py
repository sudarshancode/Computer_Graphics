import matplotlib.pyplot as plt

def plot_points(xc, yc, x, y, x_list, y_list):
    # Using symmetry to plot 4 points
    x_list.extend([xc + x, xc - x, xc + x, xc - x])
    y_list.extend([yc + y, yc + y, yc - y, yc - y])

def midpoint_ellipse(xc, yc, rx, ry):
    x = 0
    y = ry

    rx2 = rx * rx
    ry2 = ry * ry

    x_list = []
    y_list = []

    # Decision parameter for region 1
    d1 = ry2 - (rx2 * ry) + (0.25 * rx2)
    dx = 2 * ry2 * x
    dy = 2 * rx2 * y

    # Region 1
    while dx < dy:
        plot_points(xc, yc, x, y, x_list, y_list)
        if d1 < 0:
            x += 1
            dx = dx + (2 * ry2)
            d1 = d1 + dx + ry2
        else:
            x += 1
            y -= 1
            dx = dx + (2 * ry2)
            dy = dy - (2 * rx2)
            d1 = d1 + dx - dy + ry2

    # Decision parameter for region 2
    d2 = (ry2) * ((x + 0.5)**2) + (rx2) * ((y - 1)**2) - (rx2 * ry2)

    # Region 2
    while y >= 0:
        plot_points(xc, yc, x, y, x_list, y_list)
        if d2 > 0:
            y -= 1
            dy = dy - (2 * rx2)
            d2 = d2 + rx2 - dy
        else:
            y -= 1
            x += 1
            dx = dx + (2 * ry2)
            dy = dy - (2 * rx2)
            d2 = d2 + dx - dy + rx2

    return x_list, y_list

def main():
    print("Midpoint Ellipse Drawing Algorithm")
    xc = int(input("Enter center x-coordinate: "))
    yc = int(input("Enter center y-coordinate: "))
    rx = int(input("Enter semi-major axis (rx): "))
    ry = int(input("Enter semi-minor axis (ry): "))

    x_vals, y_vals = midpoint_ellipse(xc, yc, rx, ry)

    # Plot the ellipse
    plt.figure()
    plt.plot(x_vals, y_vals, 'bo', markersize=2)
    plt.gca().set_aspect('equal')
    plt.title("Midpoint Ellipse")
    plt.grid(True)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

if __name__ == "__main__":
    main()
