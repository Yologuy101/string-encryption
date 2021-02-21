

s = input("Enter a string to encrypt: ")
x = int(input("Shift value: "))

def encipher(s, x):
    new_s = ''
    for i in s:
        if i != " ":
            new_char = warp(i)
            new_s = new_s+new_char
        else:
            new_s = new_s + " "

    return new_s

def warp (end_char):
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
    


print(encipher(s, x))





