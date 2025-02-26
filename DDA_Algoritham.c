//Draw a line using DDA algorithm
#include<stdio.h>
#include<graphics.h>
#include<stdlib.h>
#include<math.h>
#define ROUND(a) ((int)(a+0.5))
void lineDDA(int xa,int ya,int xb,int yb){
	int gd=DETECT,gm;
	initgraph(&gd,&gm,NULL);
	int dx=xb-xa;
	int dy=yb-ya;
	int steps,k;
	float xinc,yinc,x=xa,y=ya;

	if(abs(dx)>abs(dy)){
		steps=abs(dx);
	}else{
		steps=abs(dy);
	}
	xinc=dx/(float) steps;
	yinc=dy/(float) steps;

	putpixel(ROUND(x),ROUND(y),WHITE);
	for(k=0;k<steps;k++){
		x=x+xinc;
		y=y+yinc;
		putpixel(ROUND(x),ROUND(y),WHITE);
	}
	printf("Press any key to exit...");
    	while (!kbhit());
	closegraph();
}
int main(){

	int x1,y1,x2,y2;
	printf("Enter x1 and y1:");
	scanf("%d %d",&x1,&y1);
	printf("Enter x2 and y2:");
	scanf("%d %d",&x2,&y2);

	lineDDA(x1,y1,x2,y2);
	
	return 0;
}
