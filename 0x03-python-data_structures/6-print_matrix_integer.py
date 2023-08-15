#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for column, value in enumerate(row):
            if column < len(row) - 1:
                print("{:d}".format(value), end=" ")
            else:
                print("{:d}".format(value))
