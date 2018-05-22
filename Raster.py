from grid import *
import math

def add(x, y):
    g.addPoint(x, y)

g = Grid(20, 20)
def rasterline(x1 , y1, x2, y2):
    if x1>x2:
        temp = x1
        x1 = x2
        x2 = temp
        temp = y1
        y1 = y2
        y2 = temp
    xtemp = x2-x1

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
    anglex = 90 - angle
    anglexTot = 0
    hasGonex = False
    angle /= 45
    anglex /= 45
    print("angle: ", angle)
    for i in range(0, lineLength):
        add(x, y)
        if angle <= 1:
            x += 1
        else:
            anglexTot += anglex
            if anglexTot > 0.5 and hasGonex == False:
                x += 1
                hasGonex = True
            if anglexTot >= 1:
                anglexTot -= 1
                hasGonex = False
        angleTot += angle
        if angleTot > 0.5 and hasGone == False:
            if diry == "Down":
                y -= 2
            y += 1
            hasGone = True
        if angleTot >= 1:
            angleTot -= 1
            hasGone = False
        print("AnglexTot: ", anglexTot, "hasGonex: ", hasGonex)

rasterline(0, 6, 10, 0)
g.draw()
