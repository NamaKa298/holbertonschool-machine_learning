#!/usr/bin/env python3
"""Functionthat performs matrix multiplication"""


def mat_mul(mat1, mat2):
    """
    Multiplies two matrices.

    Args:
        mat1 (list): A list of lists of integers/floats.
        mat2 (list): A list of lists of integers/floats.

    Returns:
        list: A new list of lists containing the product of mat1 and mat2.
    """
    if len(mat1[0]) != len(mat2):
        return None

    result = []
    for i in range(len(mat1)):
        matrice_mult = []
        for k in range(len(mat2[0])):
            nouvelles_valeurs = 0
            for j in range(len(mat2)):
                nouvelles_valeurs += mat1[i][j] * mat2[j][k]
            matrice_mult.append(nouvelles_valeurs)
        result.append(matrice_mult)
    return result
