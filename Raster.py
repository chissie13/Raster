from grid import *
import math

def add(x, y):                  #easier function to add a point
    g.addPoint(x, y)

g = Grid(20, 20)                # the grid dimensions (x,y)

def rasterline(x1 , y1, x2, y2):#function to calculate where the points have to go and calls add function accordingly
    if x1>x2:                   #checks to make sure x1 is on the left side of x2 and changes them if not true
        temp = x1
        x1 = x2
        x2 = temp
        temp = y1
        y1 = y2
        y2 = temp
    xtemp = x2 - x1

    if y1>y2:                   #checks to see if y1 is above or below y2
        ytemp = y1-y2
        dir_y = "Down"
    else:
        ytemp = y2-y1
        dir_y = "Up"
    if xtemp>ytemp:
        line_length = xtemp
    else:
        line_length = ytemp
    angle = math.degrees((math.atan(ytemp/xtemp)))
    angle_tot = 0
    x = x1
    y = y1
    has_gone = False
    anglex = 90 - angle
    anglex_tot = 0
    has_gonex = False
    angle /= 45
    anglex /= 45
    for i in range(0, line_length):
        add(x, y)
        if angle <= 1:
            x += 1
        else:
            anglex_tot += anglex
            if anglex_tot > 0.5 and has_gonex == False:
                x += 1
                has_gonex = True
            if anglex_tot >= 1:
                anglex_tot -= 1
                has_gonex = False
        angle_tot += angle
        if angle_tot > 0.5 and has_gone == False:
            if dir_y == "Down":
                y -= 2
            y += 1
            has_gone = True
        if angle_tot >= 1:
            angle_tot -= 1
            has_gone = False

rasterline(0, 6, 10, 0)
g.draw()
