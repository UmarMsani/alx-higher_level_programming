#!/usr/bin/python3
def uppercase(str):
    output = ""
    for char in str:
        if 'a' <= char <= 'z':
            char = chr(ord(char) - 32)
        output += char
    
    print("{}".format(output))
