import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def dda(x1,y1,x2,y2):
    dx=x2 - x1
    dy=y2 - y1

    steps=int(max(abs(dx),abs(dy)))

    x_inc=dx/steps
    y_inc=dy/steps

    x=x1
    y=y1
    x_points=[]
    y_points=[]

    for i in range(steps +1):
        x_points.append(round(x))
        y_points.append(round(y))
        x=x+x_inc
        y=y+y_inc
    plt.plot(x_points,y_points)
    plt.title("DDA Line Drawing")
    plt.show()

x1 =int(input("Enter x1: ")) 
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

dda(x1, y1, x2, y2)
