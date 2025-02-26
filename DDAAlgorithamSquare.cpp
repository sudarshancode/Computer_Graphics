//Draw a Square using DDA Algoritham
#include<bits/stdc++.h>
#include<graphics.h>
using namespace std;

void lineDDA(int xa,int ya,int xb,int yb){
    int dx=xb-xa;
    int dy=yb-ya;
    int x=xa,y=ya;
    float xinc,yinc,steps,k=0;

    if(abs(dx)>abs(dy)){
        steps=abs(dx);
    }else{
        steps=abs(dy);
    }
    xinc=dx/(float) steps;
    yinc=dy/(float) steps;

    putpixel(round(x),round(y),WHITE);
    for(k=0;k<steps;k++){
        x=x+xinc;
        y=y+yinc;
        putpixel(round(x),round(y),WHITE);
    }

}
void drawSquare(int x,int y,int length){
    lineDDA(x,y,x+length,y);
    lineDDA(x+length,y,x+length,y+length);
    lineDDA(x+length,y+length,x,y+length);
    lineDDA(x,y+length,x,y);
}
int main()
{
    int gd=DETECT,gm;
    initgraph(&gd,&gm,NULL);

    int x,y,length;
    printf("Enter x and y :");
    scanf("%d %d",&x,&y);

    printf("Enter length of this square:");
    scanf("%d",&length);
    drawSquare(x,y,length);

    getch();
    closegraph();

    return 0;
}
