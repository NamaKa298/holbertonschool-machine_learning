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
        mat1 and mat2 along the specified axis, or None if the matrices
        cannot be concatenated.
    """
    if axis == 0:
        # Vérifie si le nombre de colonnes est le même
        if len(mat1[0]) != len(mat2[0]):
            return None
        # Concaténation verticale avec copies manuelles
        concatenated = [row[:] for row in mat1] + [row[:] for row in mat2]
    elif axis == 1:
        # Vérifie si le nombre de lignes est le même
        if len(mat1) != len(mat2):
            return None
        # Concaténation horizontale avec copies manuelles
        concatenated = [mat1[i][:] + mat2[i][:] for i in range(len(mat1))]
    else:
        return None  # Si l'axe n'est ni 0 ni 1, retourne None

    return concatenated
