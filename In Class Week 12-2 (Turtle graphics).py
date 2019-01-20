"""
Author:  Louis Booth
Name:    In Class Week 12-2.py
Purpose: to practice graphics with turtle
Date:    4/19/2018
"""

import turtle

# global variable  (percent for each year of smokers)
yValues = [10.0, 7.4, 6.4, 5.3, 4.4, 3.7, 2.6]

def main():
    # create a turtle object
    t = turtle.Turtle()
    # hide the chevron
    t.hideturtle()
    # draw dot
    drawDot(t, -20, 0, 40, "green")
    # draw a rectangle
    drawRect(t, 0, 0, 100, 150)
    # draw rectangle using loop
    drawRect2(t, 120, 0, 100, 150, "purple")
    # draw a line between two points (x-axis)
    drawLine(t, 0, -250, 300, -250)
    # draw a line between two points (y-axis)
    drawLine(t, 0, -250, 0, -75)
    # draw a line between two points with dots (in graph)
    for i in range(6):
        drawLineWithDots(t, 40 + (40 * i), -250 + (15 * yValues[i]), 40 + (40 * (i + 1)), -250 + (15 * yValues[i+1]), "blue")
    drawTickMarks(t)

# mark ticks
def drawTickMarks(t):
    for i in range(1, 8):
        # tick marks on x-axis
        drawLine(t, 40 * i, -250, 40 * i, -250 + 10)

def drawLine(t, x1, y1, x2, y2, colorP="black"):
    t.pencolor(colorP)
    t.up()
    t.goto(x1, y1)
    t.down()
    t.goto(x2, y2)
    
def drawLineWithDots(t, x1, y1, x2, y2, colorP="black"):
    t.pencolor(colorP)
    t.up()
    t.goto(x1, y1)
    t.dot(5)
    t.down()
    t.goto(x2, y2)
    t.dot(5)

def drawDot(t, x, y, diameter, colorP):
    t.pencolor(colorP)
    t.up()
    t.goto(x, y)
    t.down()
    t.dot(diameter) # set size of dot

# one way to draw a rectangle
def drawRect(t, x, y, w, h, colorP="red"):
    # draw a rectangle with bottom-left corner (x, y),
    # with width w, height h, and pencolor colorP
    t.pencolor(colorP)
    # raise the pen up before going to the starting point
    t.up()
    # go to the starting point
    t.goto(x, y)
    # put the pen down for drawing
    t.down()
    # draw the bottom line first
    t.goto(x+w, y)
    # draw the right side line
    t.goto(x+w, y+h)
    # draw the top line
    t.goto(x, y+h)
    # draw left line
    t.goto(x, y)

# a different way to draw a rectangle
def drawRect2(t, x, y, w, h, colorP):
    t.fillcolor("yellow") # specify the fill color
    t.pencolor(colorP)
    t.up()
    t.goto(x, y)
    t.down()
    t.begin_fill() # need to indicate when to start coloring
    # use a loop to complete the drawing
    for i in range(2):
        t.forward(w) # horizontal line
        t.left(90)   # rotate 90 degree counterclockwise
        t.forward(h) # vertical line
        t.left(90)   # rotate 90 degree counterclockwise
    t.end_fill() # indicate when to stop coloring
        









main()
