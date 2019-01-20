"""
Author:  Louis Booth
Name:    Homework Week 13 Assignment 11-2.py
Purpose: to practice graphic with turtle
Date:    4/21/2018
"""

import turtle
yValues = [59, 74, 73, 77]
yValues2 = [60, 43, 44, 51]

def main():
    """
    create turle object, call on various functions to create graphic
    """
    t = turtle.Turtle()
    t.hideturtle()
    drawLine(t, 0, 0, 170, 0)
    drawLine(t, 0, 0, 0, 110)
    for i in range(3):
        drawLineWithDots(t, 40 + (40 * i), yValues[i], 40 + (40 * (i + 1)), yValues[i+1], "red")
    for i in range(3):
        drawLineWithDots(t, 40 + (40 * i), yValues2[i], 40 + (40 * (i + 1)), yValues2[i+1], "blue")
    drawTickMarks(t)
    displayText(t)
    drawRect(t, -15, -65, 237, 30, colorP="black")
    

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
    drawLine(t, 0, max(yValues), 10, max(yValues))
    drawLine(t, 0, min(yValues2), 10, min(yValues2))
    drawLine(t, 0, 100, 10, 100)

def displayText(t):
    """
    function to write text for labeling graphic (label tick marks,
    add title, create legend)
    """
    t.pencolor("black")
    t.up()
    t.goto(-3, max(yValues) - 10)
    t.write(max(yValues), align="right")
    t.goto(-3, min(yValues2) - 10)
    t.write(min(yValues2), align="right")
    t.goto(-3, 0 - 10)
    t.write(0, align="right")
    t.goto(-3, 100 - 10)
    t.write(100, align="right")
    x = 40
    for i in range(1978, 2009, 10):
        t.goto(x, -20)
        t.write(str(i), align="center")
        x += 40

    t.pencolor("red")
    drawLineWithDots(t, -10, -44, 0, -44, "red")
    t.up()
    t.goto(30, -50)
    t.down()
    t.write("Be Very Well Off Financially")

    t.pencolor("blue")
    drawLineWithDots(t, -10, -59, 0, -59, "blue")
    t.up()
    t.goto(30, -65)
    t.down()
    t.write("Develop a Meaningful Philosophy of Life")

    t.up()
    t.pencolor("black")
    t.goto(-60, 50)
    t.down()
    t.write("Percent")
    t.up()
    t.goto(85, -35)
    t.down()
    t.write("Year")
    t.up()
    t.goto(-60, 150)
    t.down()
    t.write("Percentage of Freshmen Committed to Goal", font=("arial", 10, "bold"))

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
