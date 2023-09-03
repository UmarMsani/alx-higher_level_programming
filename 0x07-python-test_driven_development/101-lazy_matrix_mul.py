#!/usr/bin/python3

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    # Validate m_a and m_b
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")
    
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists or m_b must be a list of lists")
    
    if not m_a or not m_b:
        raise ValueError("m_a can't be empty or m_b can't be empty")

    # Check if all elements in m_a and m_b are integers or floats
    for row in m_a:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError("m_b should contain only integers or floats")

    # Check if the matrices are rectangular (all rows have the same size)
    if any(len(row) != len(m_a[0]) for row in m_a) or any(len(row) != len(m_b[0]) for row in m_b):
        raise ValueError("each row of m_a must be of the same size or each row of m_b must be of the same size")

    # Convert lists to NumPy arrays
    np_a = np.array(m_a)
    np_b = np.array(m_b)

    # Check if m_a and m_b can be multiplied (columns of m_a == rows of m_b)
    if np_a.shape[1] != np_b.shape[0]:
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication using NumPy
    result = np.dot(np_a, np_b)

    return result.tolist()  # Convert the result back to a list of lists
