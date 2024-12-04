#!/usr/bin/env python3
"""function that concatenates two matrices along a specific axis"""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """Concatenate two matrices along a specific axis"""
    concatenated = np.concatenate((mat1, mat2), axis=axis)
    return concatenated
