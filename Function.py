"""Define a function that will take a parameter, n, and triple it and return
the result"""

def triple(n):
    n = n * 3
    return (n)
print(triple(5))

"""Write a program that will prompt the user for an input value (n) and print
the result of 3n by calling the function defined above.  Make sure you include
the necessary print statements and address any issues with whitespace. """

def usertriple(n):
    n = 3 *n
    return n
print (usertriple(int(input('Please enter a number'))))
