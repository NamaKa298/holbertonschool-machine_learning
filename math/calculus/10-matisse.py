#!/usr/bin/env python3
"""Calculates the derivative of a polynomial."""


def poly_derivative(poly):
    """
    Calculates the derivative of a polynomial.

    Args:
        poly (list): A list of coefficients representing the polynomial. The index of each element represents the power of x.

    Returns:
        list: A list of coefficients representing the derivative of the polynomial.
    """
    deriv = []
    if len(poly) == 1:
        return [0]
    elif type(poly) is not list:
        return None
    else:
        for i in range(1, len(poly)):
            poly[i] *= i
            deriv.append(poly[i])
        return deriv
