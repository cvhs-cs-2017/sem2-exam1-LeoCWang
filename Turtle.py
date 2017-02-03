"""Create a Turtle Program that will draw a 3-dimensional cube"""

import turtle
Tim = turtle.Turtle()
def cube(lhw):
    for i in range(4):
        Tim.forward(lhw)
        Tim.left(90)
    Tim.left(45)
    Tim.fd(lhw/2)
    Tim.left(45)
    Tim.fd(lhw)
    Tim.left(135)
    Tim.fd(lhw/2)
    Tim.left(180)
    Tim.fd(lhw/2)
    Tim.right(45)
    Tim.fd(lhw)
    Tim.right(135)
    Tim.fd(lhw/2)
    Tim.left(45)
    Tim.fd(lhw)
    Tim.left(135)
    Tim.fd(lhw/2)
    Tim.left(45)
    Tim.fd(lhw)
    Tim.left(180)
    Tim.fd(lhw)
    Tim.right(90)
    Tim.fd(lhw)
    input()
    Tim.clear()
cube(50)

"""Import and Call the DrawRectangle(Anyturtle, l, w) function from the
file MyFile.py"""

from MyFile import DrawRectangle
DrawRectangle(Tim, 50, 25)
