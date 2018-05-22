from grid import *
import math

def add(x, y):
    g.addPoint(x, y)

g = Grid(20, 10)
def rasterline(x1 , y1, x2, y2):
    if x1>x2:
        xtemp = x1-x2
        dirx = "Left"
    else:
        xtemp = x2-x1
        dirx = "Right"
    if y1>y2:
        ytemp = y1-y2
        diry = "Down"
    else:
        ytemp = y2-y1
        diry = "Up"
    if xtemp>ytemp:
        lineLength = xtemp
    else:
        lineLength = ytemp
    print("LineLength",lineLength)
    angle = math.degrees((math.atan(ytemp/xtemp)))
    angleTot = 0
    bonus = 0
    x = x1
    y = y1
    hasGone = False
    if dirx == "Right" and angle<=45:
        angle /= 45
        print("angle: ", angle)
        for i in range(0, lineLength):
            add(x, y)
            x += 1
            angleTot    += angle
            if angleTot > 0.5 and hasGone == False:
                y += 1
                hasGone = True
            if angleTot >= 1:
                angleTot -= 1
                hasGone = False
            print("AngleTot: ", angleTot, "hasGone: ", hasGone)

rasterline(0, 0, 10, 3)
g.draw()
