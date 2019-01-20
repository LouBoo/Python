"""
Author:  Louis Booth
Name:    Homework Week 13 Assignment 11.py
Purpose: to practice graphics with turtle
Date:    4/21/2018
"""

import turtle
yValues = [59, 74, 73, 77]
yValues2 = [60, 43, 44, 51]

def main():
    """
    create turle object, call on various functions to create graphics
    """
    t = turtle.Turtle()
    t.hideturtle()
    drawLine(t, 0, 0, 170, 0)
    drawLine(t, 0, 0, 0, 110)
    drawLine(t, -200, 0, -30, 0)
    drawLine(t, -200, 0, -200, 110)
    for i in range(3):
        drawLineWithDots(t, 40 + (40 * i), yValues[i], 40 + (40 * (i + 1)), yValues[i+1], "red")
    for i in range(3):
        drawLineWithDots(t, -160 + (40 * i), yValues2[i], -160 + (40 * (i + 1)), yValues2[i+1], "blue")
    drawTickMarks(t)
    displayText(t)
    

def drawLine(t, x1, y1, x2, y2, colorP="black"):
    """
    function to draw line between two points
    """
    t.pencolor(colorP)
    t.up()
    t.goto(x1, y1)
    t.down()
    t.goto(x2, y2)
    
def drawLineWithDots(t, x1, y1, x2, y2, colorP="black"):
    """
    function to draw line between two points with dots at each point
    """
    t.pencolor(colorP)
    t.up()
    t.goto(x1, y1)
    t.dot(5)
    t.down()
    t.goto(x2, y2)
    t.dot(5)

def drawTickMarks(t):
    """
    function to draw tick marks
    """
    for i in range(1, 5):
        drawLine(t, 40 * i, 0, 40 * i, 10)
    for i in range(1, 5):
        drawLine(t, (-200 + (40 * i)), 0, (-200 + (40 * i)), 10)
    drawLine(t, 0, max(yValues), 10, max(yValues))
    drawLine(t, 0, min(yValues), 10, min(yValues))
    drawLine(t, -200, max(yValues2), -190, max(yValues2))
    drawLine(t, -200, min(yValues2), -190, min(yValues2))
    drawLine(t, 0, 100, 10, 100)
    drawLine(t, -200, 100, -190, 100)

def displayText(t):
    """
    function to write text for labeling graphics (label tick marks,
    add title, create legend)
    """
    t.pencolor("black")
    t.up()
    t.goto(-3, max(yValues) - 10)
    t.write(max(yValues), align="right")
    t.goto(-3, min(yValues) - 10)
    t.write(min(yValues), align="right")
    t.goto(-3, 0 - 10)
    t.write(0, align="right")
    t.goto(-3, 100 - 10)
    t.write(100, align="right")
    x = 40
    for i in range(1978, 2009, 10):
        t.goto(x, -20)
        t.write(str(i), align="center")
        x += 40
    drawLineWithDots(t, 15, -44, 25, -44, "red")
    t.up()
    t.goto(30, -50)
    t.write("Be Very Well Off Financially")
    
    t.pencolor("black")
    t.goto(-203, max(yValues2) - 10)
    t.write(max(yValues2), align="right")
    t.goto(-203, min(yValues2) - 10)
    t.write(min(yValues2), align="right")
    t.goto(-203, 0 - 10)
    t.write(0, align="right")
    t.goto(-203, 100 - 10)
    t.write(100, align="right")
    x = -160
    for i in range(1978, 2009, 10):
        t.goto(x, -20)
        t.write(str(i), align="center")
        x += 40
    drawLineWithDots(t, -225, -44, -215, -44, "blue")
    t.up()
    t.goto(-210, -50)
    t.write("Develop a Meaningful Philosophy of Life")
    t.up()
    t.down()
    drawRect(t, -230, -50, 425, 15)
    t.up()

    t.pencolor("black")
    t.goto(-260, 50)
    t.down()
    t.write("Percent")
    t.up()
    t.goto(85, -35)
    t.down()
    t.write("Year")
    t.up()
    t.goto(-115, -35)
    t.down()
    t.write("Year")
    t.up()
    t.goto(-100, 150)
    t.down()
    t.write("Percentage of Freshmen Committed to Goal")

def drawRect(t, x, y, w, h, colorP="black"):
    """
    function to draw rectangle starting with bottom-left point, using input
    height and width
    """
    t.pencolor(colorP)
    t.up()
    t.goto(x, y)
    t.down()
    t.goto(x+w, y)
    t.goto(x+w, y+h)
    t.goto(x, y+h)
    t.goto(x, y)    

main()
