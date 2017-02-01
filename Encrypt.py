"""Write a code that will remove vowels from a string and run it for the sentence:

'Computer Science Makes the World go round but it doesn't make the world round itself!'

Print the save the result as the variable = NoVowels
"""

plainText = 'Computer Science Makes the World go round but it doesn\'t make the world round itself!'

def encrypt(plainText):
    NoVowels = ""
    for ch in plainText:
        if ch == 'a' or ch == 'i' or ch == 'e' or ch == 'o' or ch == 'u' or ch == 'y':
            NoVowels = NoVowels + ''
        else:
            NoVowels = NoVowels + ch
    return(NoVowels)
print (encrypt(plainText))

"""Write an encryption code that you make up and run it for the variable NoVowels"""
