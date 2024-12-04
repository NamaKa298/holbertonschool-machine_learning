#!/usr/bin/env python3
"""function that concatenates two matrices along a specific axis"""
import copy


def cat_matrices2D(mat1, mat2, axis=0):
    """
    Concatenates two matrices along a specific axis.

    Args:
        mat1 (list): A list of lists of integers/floats.
        mat2 (list): A list of lists of integers/floats.
        axis (int): The axis to concatenate along.

    Returns:
        list: A new list of lists containing the concatenation of
        mat1 and mat2 along the specified axis.
    """
    concatanated = []
    if axis == 0 and len(mat1[0]) != len(mat2[0]):
        return None
    elif axis == 1 and len(mat1) != len(mat2):
        return None
    if axis == 0:
        concatanated = copy.deepcopy(mat1 + mat2)
    elif axis == 1:
        for i in range(len(mat1)):
            concatanated.append(mat1[i] + mat2[i])
    return concatanated
