#!/usr/bin/env python3
"""
function def matrix_transpose(matrix): that returns the
transpose of a 2D matrix, matrix"""


def matrix_transpose(matrix):
    """
    Transposes a matrix.

    Args:
        matrix (list): A list of lists representing the matrix.

    Returns:
        list: A list of lists representing the transpose of the matrix.
    """
    transpose_final = []
    for i in range(len(matrix[0])):
        transpose = []
        for j in range(len(matrix)):
            transpose.append(matrix[j][i])
        transpose_final += [transpose]
    return transpose_final
