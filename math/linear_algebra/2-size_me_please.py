#!/usr/bin/env python3
"""
This module contains a function to determine the shape of a matrix.
"""


def matrix_shape(matrix):
    """
    Returns the dimensions of a matrix as a list.

    Args:
        matrix (list): A list of lists representing the matrix.

    Returns:
        list: A list representing the dimensions of the matrix.
    """
    for i in range(len(matrix)):
        if type(matrix[i]) is list:
            return [len(matrix)] + matrix_shape(matrix[i])
        else:
            return [len(matrix)]
