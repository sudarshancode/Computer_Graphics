#Bresenha'ms line drawing algorithm
import matplotlib.pyplot as plt

def lineDrawing(x1,y1,x2,y2):
    x=x1
    y=y1
    dx=x2-x1
    dy=y2-y1
    p=2*dy -dx

    x_points=[]
    y_points=[]
    while x<=y:
        if p<0:
            x_points.append(x)
            y_points.append(y)
            x=x+1
            p=p+2*dy
        else:
            x_points.append(x)
            y_points.append(y)
            x=x+1
            y=y+1
            p=p+2*dy-2*dx
    plt.plot(x_points,y_points,'ro')
    plt.title("Bresenhams line draw")
    plt.show()


x1 =int(input("Enter x1: ")) 
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

lineDrawing(x1, y1, x2, y2)