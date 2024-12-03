#!/usr/bin/env python3
"""
function that adds two arrays element-wise
"""


def add_arrays(arr1, arr2):
    """
    Adds two arrays element-wise.

    Args:
        arr1 (list): A list of integers/floats.
        arr2 (list): A list of integers/floats.

    Returns:
        list: A list containing the element-wise sum of arr1 and arr2.
    """
    sum_arr = []
    if len(arr1) != len(arr2):
        return None
    for i in range(len(arr1)):
        sum_arr.append(arr1[i] + arr2[i])
    return sum_arr
