"""Write a program that will add 5 and loop until it reaches a number GREATER
than 100.  It should then spit out the result AND tell the user how many times
it had to add 5 (if any)"""

def add5(n):
    x = 0
    while n <= 100:
        n = n + 5
        x = x + 1
    else:
        print (n)
        print('I added five ',x,' times till it was over 100')
print (add5(int(input('Enter a number:'))))

"""Write a program that will prompt the user for an input value (n) and double
it IF is an ODD number, triple it if is an EVEN number and do nothing if it is
anything else (like a decimal or a string)"""

def triple(n):
    if n % 2 == 0:
        n = n * 3
    elif n % 2 is not 0:
        n = n * 2
    else:
        print(n,'is not a whole number!')
    return (n)
print (triple(int(input('Enter a whole number:'))))
