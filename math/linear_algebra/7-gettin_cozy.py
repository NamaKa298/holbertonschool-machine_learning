#!/usr/bin/env python3
"""Function that concatenates two matrices along a specific axis"""

def cat_matrices2D(mat1, mat2, axis=0):
    """
    Concatenates two matrices along a specific axis.

    Args:
        mat1 (list): A list of lists of integers/floats.
        mat2 (list): A list of lists of integers/floats.
        axis (int): The axis to concatenate along.

    Returns:
        list: A new list of lists containing the concatenation of
        mat1 and mat2 along the specified axis, or None if the matrices cannot be concatenated.
    """
    if axis == 0 and len(mat1[0]) != len(mat2[0]):
        return None
    if axis == 1 and len(mat1) != len(mat2):
        return None
    if axis == 0:
        return [row.copy() for row in mat1] + [row.copy() for row in mat2]
    return [mat1[i].copy() + mat2[i].copy() for i in range(len(mat1))]
