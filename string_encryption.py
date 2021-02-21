

s = input("Enter a string to encrypt: ")
x = int(input("Shift value: "))

def encipher(s, x):
    """ encipher the string """
    new_s = ''
    for i in s:
        if i != " ":
            new_char = warp(i)
            new_s = new_s+new_char
        else:
            new_s = new_s + " "

    return new_s

def warp (end_char):
    """ helper function, when character goes pass z it resets to a """
    if end_char.isupper():
        if (ord(end_char) + x) > 90:
            y = x - (90 - ord(end_char)) -1
            return chr(65+y)
        else:
            return chr(ord(end_char) + x)
    elif end_char.islower():
        if (ord(end_char) + x) > 122:
            y = x - (122 - ord(end_char)) -1
            return chr(97+y)
        else:
            return chr(ord(end_char) + x)
    

def decipher(s, x):
    """ encipher the string """
    new_s = ''
    for i in s:
        if i != " ":
            new_char = unwarp(i)
            new_s = new_s+new_char
        else:
            new_s = new_s + " "

    return new_s

def unwarp(end_char):
    """ helper function, when character goes to a it resets to z """
    if end_char.isupper():
        if (ord(end_char) - x) < 65:
            y = x - (ord(end_char) - 65) - 1
            return chr(90-y)
        else:
            return chr(ord(end_char) - x)
    elif end_char.islower():
        if (ord(end_char) - x) < 97:
            y = x - (ord(end_char) - 97) - 1
            return chr(122-y)
        else:
            return chr(ord(end_char) - x)



#example code
print(encipher(s,x))
print(decipher(s, x))






