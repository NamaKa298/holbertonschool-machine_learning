#!/usr/bin/env python3
"""This module contains a function to calculate\\
    the sum of squares of the first n natural numbers."""


def summation_i_squared(n):
    """
    Calculates the sum of squares of the first n natural numbers.

    Args:
        n (int): The number up to which the sum of squares is to be calculated.

    Returns:
        int: The sum of squares of the first n natural numbers,\\
            or None if n is less than 1.
    """
    if n < 1:
        return None
    else:
        sum = int(n*(n+1)*(2*n+1)/6)
        return (sum)
