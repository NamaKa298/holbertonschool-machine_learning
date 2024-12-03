#!/usr/bin/env python3

def matrix_transpose(matrix):
    """
    Transposes a matrix.

    Args:
        matrix (list): A list of lists representing the matrix.

    Returns:
        list: A list of lists representing the transpose of the matrix.
    """
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]