#!/usr/bin/python3

def print_square(size):
    # Check if size is an integer or a float (and not a negative float)
    if not isinstance(size, int) and (not isinstance(size, float) or size < 0):
        if isinstance(size, float):
            raise TypeError("size must be an integer")
        else:
            raise ValueError("size must be >= 0")

    # Check if size is less than 0 (integer case)
    if size < 0:
        raise ValueError("size must be >= 0")

    # Convert size to an integer (if it's a float)
    size = int(size)

    # Print the square
    for _ in range(size):
        print("#" * size)
