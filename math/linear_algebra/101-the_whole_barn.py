#!/usr/bin/env python3
"""16. The Whole Barn"""
import numpy as np


def add_matrices(mat1, mat2):
    """fonction qui additionne 2 matrices"""
    mat1 = np.array(mat1)
    mat2 = np.array(mat2)
    if mat1.shape != mat2.shape:
        return None
    else:
        new_matrice = mat1 + mat2
        return new_matrice.tolist()
