def uppercase(s):
    for c in s:
        if 'a' <= c <= 'z':
            print(chr(ord(c) - 32), end="")
        else:
            print(c, end="")
    print()
