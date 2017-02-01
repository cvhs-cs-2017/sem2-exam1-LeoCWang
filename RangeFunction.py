"""Use the range function to print the numbers from 40 to 1 (backwards)"""

def forty_one():
    for i in range(40,0,-1):
        print (i)
print(forty_one())

"""Repeat the exercise but count by 5's"""

def forty_one5():
    for i in range(40,0,-5):
        print (i)
print(forty_one5())

"""Write a program that will count print first 10 multiples of (n) where n is
taken from user input.  Include necessary print statements."""
def mult10(n):
    x = 1
    for i in range(10):
        y = n * x
        x = x + 1
        print (y)
print(mult10(int(input('enter a number:'))))
