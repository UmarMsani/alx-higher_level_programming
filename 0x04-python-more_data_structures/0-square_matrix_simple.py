#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return []

    rows = len(matrix)
    cols = len(matrix[0])
    
    result_matrix = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        result_matrix[i] = list(map(lambda x: x ** 2, matrix[i]))
    
    return result_matrix
