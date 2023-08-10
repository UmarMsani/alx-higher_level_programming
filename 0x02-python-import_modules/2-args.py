#!/usr/bin/python3

if __name__ == "__main__":
    """Printing the number of and list of arguments."""

import sys

arguments = sys.argv[1:]
num_arguments = len(arguments)

if num_arguments == 0:
    print("0 argument:")
elif num_arguments == 1:
    print("1 argument:")
else:
    print("{} arguments:".format(num_arguments))

if num_arguments == 0:
    print(".")
else:
    for i, arg in enumerate(arguments, start=1):
        print("{}: {}".format(i, arg))
