#!/usr/bin/env python3
"""17. Squashed Like Sardines"""


def cat_matrices(mat1, mat2, axis=0):
    """Concatène deux matrices le long d'un axe donné."""
    # Si axis == 0, concatène directement les listes principales
    if axis == 0:
        return mat1 + mat2

    # Vérifier que mat1 et mat2 sont des listes
    if not isinstance(mat1, list) or not isinstance(mat2, list):
        return None

    # Vérifier que les sous-dimensions sont compatibles
    if len(mat1) != len(mat2):
        return None

    # Créer une nouvelle matrice pour la concaténation
    new_mat = []
    for sub1, sub2 in zip(mat1, mat2):
        concatenated = cat_matrices(sub1, sub2, axis - 1)
        if concatenated is None:
            return None
        new_mat.append(concatenated)
    return new_mat
