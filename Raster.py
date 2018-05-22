from grid import *
import math

def add(x, y):
    g.addPoint(x, y)

g = Grid(20, 10)
def rasterline(x1 , y1, x2, y2):
    if x1>x2:
        xtemp = x1-x2
        dirx = "L"
    else:
        xtemp = x2-x1
        dirx = "R"
    if y1>y2:
        ytemp = y1-y2
        diry = "L"
    else:
        ytemp = y2-y1
        diry = "H"
    if xtemp>ytemp:
        lineLength = xtemp
    else:
        lineLength = ytemp

    angle = math.degrees((math.atan(ytemp/xtemp)))
    angleTot = 0
    bonus = 0
    x = x1
    y = y1
    if dirx == "R" and angle<=45:
        print (angle)
        angle /= 45
        print("angle: ",angle)
        for i in range(0, lineLength):
            add(x, y)
            x += 1
            if angleTot>0.5:
                angleTot += angle
            else:
                angleTot += angle
                if angleTot > 0.5:
                    y+=1
            if angleTot >1:
                angleTot-=1
            print(angleTot)



    for x in range (0, lineLength):
        print()
    print(angle)
    print (dirx)
    print (diry)

rasterline(0 , 0 , 5 , 5)

g.draw()
