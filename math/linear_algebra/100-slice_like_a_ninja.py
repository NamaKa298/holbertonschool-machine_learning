#!/usr/bin/env python3
"""15. Slice Like A Ninja """


def np_slice(matrix, axes={}):
    """
    function that slices a matrix along specific axes
    axe 0 correspond à l'axe vertical
    axe 1 correspond à l'axe horizontal
    """
    slices = [slice(None)] * matrix.ndim
    for axis, slice_tuple in axes.items():
        slices[axis] = slice(*slice_tuple)
    return matrix[tuple(slices)]
