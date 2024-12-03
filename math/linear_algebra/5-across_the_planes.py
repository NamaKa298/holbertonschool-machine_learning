#!/usr/bin/env python3
"""function that adds two matrices element-wise"""


def add_matrices2D(mat1, mat2):
    """
    Adds two matrices element-wise.

    Args:
        mat1 (list): A list of lists of integers/floats.
        mat2 (list): A list of lists of integers/floats.

    Returns:
        list: A list of lists containing the element-wise sum of mat1 and mat2.
    """
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None
    sum_tot = []
    for i in range(len(mat1)):
        sum_mat = []
        for j in range(len(mat1[i])):
            sum_mat.append(mat1[i][j]+mat2[i][j])
        sum_tot.append(sum_mat)
    return(sum_tot)
