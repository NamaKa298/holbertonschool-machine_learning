#!/usr/bin/env python3
"""16. The Whole Barn"""


def add_matrices(mat1, mat2):
    """Fonction qui additionne 2 matrices"""
    if type(mat1) != type(mat2):
        return None
    if isinstance(mat1, (int, float)):
        return mat1 + mat2
    if len(mat1) != len(mat2):
        return None
    result = []
    for m1, m2 in zip(mat1, mat2):
        added = add_matrices(m1, m2)
        if added is None:
            return None
        result.append(added)
    return result
