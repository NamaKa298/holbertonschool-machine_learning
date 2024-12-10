#!/usr/bin/env python3
"""17. Squashed Like Sardines"""


def cat_matrices(mat1, mat2, axis=0):
    """Concatène deux matrices le long d'un axe donné."""
    # Vérifier que mat1 et mat2 sont des listes
    if not isinstance(mat1, list) or not isinstance(mat2, list):
        return None

    if axis == 0:
        # Vérifier que toutes les sous-listes (lignes) de mat1 et
        # mat2 ont la même longueur
        if any(len(row) != len(mat1[0]) for row in mat1 + mat2):
            return None
        return mat1 + mat2

    if len(mat1) != len(mat2):
        return None

    new_mat = []
    for sub1, sub2 in zip(mat1, mat2):
        concatenated = cat_matrices(sub1, sub2, axis - 1)
        if concatenated is None:
            return None
        new_mat.append(concatenated)

    return new_mat
