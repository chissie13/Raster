from grid import *
import math

def add(x, y):                  #easier function to add a point
    g.addPoint(x, y)

g = Grid(20, 20)                # the grid dimensions (x,y)

def rasterline(x1 , y1, x2, y2):#function to calculate where the points have to go and calls add function accordingly (x1, y1, x2, y2)
    if x1>x2:                   #checks to make sure x1 is on the left side of x2 and changes them if not true
        temp = x1
        x1 = x2
        x2 = temp
        temp = y1
        y1 = y2
        y2 = temp

    xtemp = x2 - x1

    dir_y = 0
    if y1>y2:                   #checks to see if y1 is above or below y2
        ytemp = y1-y2
        dir_y = "Down"
    else:
        ytemp = y2-y1

    if xtemp>ytemp:             #checks if x or y is bigger to determine the line length
        line_length = xtemp
    else:
        line_length = ytemp
    if x1 == x2:
        angle = 90
    else:
        angle = math.degrees((math.atan(ytemp/xtemp)))#calculates the angle of the line for y value
    angle_tot = 0
    x = x1
    y = y1
    has_gone = False
    anglex = 90 - angle                           #angle of line for calculations for the x value
    anglex_tot = 0
    has_gonex = False

    for i in range(0, line_length):
        add(x, y)

        if angle <= 45:                            #checks if the degree is more or less than 45
            x += 1
        else:
            anglex_tot += anglex                    #adds to total to see how far the line is in correlation to the gridsquares
            if anglex_tot > 22.5 and has_gonex == False:
                x += 1
                has_gonex = True
            if anglex_tot >= 45:
                anglex_tot -= 45
                has_gonex = False

        angle_tot += angle

        if angle_tot > 22.5 and has_gone == False:
            if dir_y == "Down":
                y -= 2
            y += 1
            has_gone = True

        if angle_tot >= 45:
            angle_tot -= 45
            has_gone = False

rasterline(10, 10, 0, 0)                            #testdata :)
rasterline(2, 0, 12, 10)
rasterline(0, 10, 10, 0)
rasterline(12, 0, 0, 12)
rasterline(0, 0, 15, 0)
rasterline(0, 0, 0, 15)

g.draw()
