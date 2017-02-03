"""Create a Turtle Program that will draw a 3-dimensional cube"""

import turtle
Tim = turtle.Turtle()
def cube(lhw):
    for i in range(2):
        Tim.forward(lhw)
        Tim.left(90)
        Tim.fd(lhw)
        Tim.left(90)
    for i in range(2):
        Tim.left(30)
        Tim.fd(lhw)
        Tim.left(30)
    Tim.left(90)
    Tim.fd(lhw)
    Tim.home()
    Tim.fd(lhw)
    for i in range(2):
        Tim.left(30)
        Tim.fd(lhw)
        Tim.left(30)
    Tim.left(90)
    Tim.fd(lhw)
    Tim.left(180)
    Tim.fd(lhw)
    Tim.left(150)
    Tim.fd(lhw)
    Tim.left(90)
    Tim.fd(lhw)
    Tim.left(90)
    Tim.fd(lhw)
    input()
cube(50)

"""Import and Call the DrawRectangle(Anyturtle, l, w) function from the
file MyFile.py"""
