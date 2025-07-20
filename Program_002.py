import matplotlib.pyplot as plt

def drawCircle(xc,yc,r):
    x=0
    y=r
    p=1-r
    x_points=[]
    y_points=[]
    
    def plot_points(xc,yc,x,y):
        x_points.extend([
            xc + x, xc - x, xc + x, xc - x,
            xc + y, xc - y, xc + y, xc - y
        ])
        y_points.extend([
            yc + y, yc + y, yc - y, yc - y,
            yc + x, yc + x, yc - x, yc - x
        ])
    plot_points(xc,yc,x,y)
    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1
        plot_points(xc,yc,x,y)

    plt.plot(x_points,y_points,'ro')
    plt.title("Midpoint Circel Draw")
    plt.show()
x=int(input("Enter x:"))
y=int(input("Enter y:"))
r=int(input("Enter radius:"))
drawCircle(x,y,r)

