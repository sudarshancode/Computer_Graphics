import numpy as np
import matplotlib.pyplot as plt

def flood_fill(image, seed_x, seed_y, fill_color):
    rows, cols = image.shape
    target_color = image[seed_y][seed_x]

    if target_color == fill_color:
        return

    stack = [(seed_x, seed_y)]

    while stack:
        x, y = stack.pop()

        if x < 0 or x >= cols or y < 0 or y >= rows:
            continue

        if image[y][x] != target_color:
            continue

        image[y][x] = fill_color

        # Push 4-connected neighbors
        stack.append((x + 1, y))
        stack.append((x - 1, y))
        stack.append((x, y + 1))
        stack.append((x, y - 1))

def main():
    # Create a simple 20x30 grid
    image = np.zeros((20, 30), dtype=int)

    # Draw a box region (value = 1)
    image[5:15, 10:20] = 1

    # Show before fill
    plt.imshow(image, cmap='gray')
    plt.title("Before Flood Fill")
    plt.show()

    # User input
    x = int(input("Enter seed point x (column): "))
    y = int(input("Enter seed point y (row): "))
    fill_color = int(input("Enter fill color (e.g., 2): "))

    flood_fill(image, x, y, fill_color)

    # Show after fill
    plt.imshow(image, cmap='gray')
    plt.title("After Flood Fill")
    plt.show()

if __name__ == "__main__":
    main()
