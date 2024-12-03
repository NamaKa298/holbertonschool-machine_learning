#!/usr/bin/env python3
"""function that concatenates two arrays"""


def cat_arrays(arr1, arr2):
    """
    Concatenates two arrays.

    Args:
        arr1 (list): A list of integers/floats.
        arr2 (list): A list of integers/floats.

    Returns:
        list: A new list containing the elements of
        arr1 followed by the elements of arr2.
    """
    concatenated = arr1 + arr2
    return concatenated
