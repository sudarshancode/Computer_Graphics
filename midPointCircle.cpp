#include <graphics.h>
#include <iostream>

using namespace std;

// Function to draw a circle using the Midpoint Circle Algorithm
void drawCircle(int xc, int yc, int r) {
    int x = 0, y = r;
    int p = 1 - r;  // Initial decision parameter

    while (x <= y) {
        // Plot symmetric points
        putpixel(xc + x, yc + y, WHITE);
        putpixel(xc - x, yc + y, WHITE);
        putpixel(xc + x, yc - y, WHITE);
        putpixel(xc - x, yc - y, WHITE);
        putpixel(xc + y, yc + x, WHITE);
        putpixel(xc - y, yc + x, WHITE);
        putpixel(xc + y, yc - x, WHITE);
        putpixel(xc - y, yc - x, WHITE);

        x++;  // Move right

        // Update decision parameter
        if (p < 0) {
            p += 2 * x + 1;
        } else {
            y--;  // Move downward
            p += 2 * (x - y) + 1;
        }
    }
}

int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");  // Initialize graphics mode

    int xc, yc, r;
    cout << "Enter the center of the circle (x, y): ";
    cin >> xc >> yc;
    cout << "Enter the radius of the circle: ";
    cin >> r;

    drawCircle(xc, yc, r);  // Draw the circle

    getch();  // Wait for user input
    closegraph();  // Close graphics mode
    return 0;
}
