def AddTen(n):
    n = n + 10
    return (n)
print (AddTen(5))


import turtle
Tim = turtle.Turtle()
def DrawRectangle(Anyturtle, l, w):
    for i in range(2):
        Anyturtle.forward(l)
        Anyturtle.left(90)
        Anyturtle.forward(w)
        Anyturtle.left(90)
    input()
    Anyturtle.clear()
DrawRectangle(Tim,100,50)


def DrawPoly(Anyturtle, n):
    for i in range(n):
        Anyturtle.forward(50)
        Anyturtle.left(360/n)
    input()
    Anyturtle.clear()
DrawPoly(Tim,15)
