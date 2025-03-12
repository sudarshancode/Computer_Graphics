#include <graphics.h>
#include <bits/stdc++.h>
int main() {
    int x=0; 
    int gd = DETECT, gm;
    initgraph(&gd, &gm, NULL);

    circle(250, 250, 100);
    delay(5000);
    closegraph();

    return 0;
    
}

