#!/usr/bin/python3

if __name__ == "__main__":
    """Printing the number of and list of arguments."""

import sys

num_arguments = len(sys.argv) - 1

if num_arguments == 0:
    print("0 arguments.")
else:
    print("{} argument{}:".format(num_arguments, "s" if num_arguments != 1 else ""))
    for i in range(1, num_arguments + 1):
        print("{}: {}".format(i, sys.argv[i]))
