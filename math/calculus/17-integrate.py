#!/usr/bin/env python3
"""Calculates the integral of a polynomial."""


def poly_integral(poly, C=0):
    """
    Calculates the integral of a polynomial.
    """
    if not isinstance(poly, list) or len(poly) == 0 or not isinstance(C, (int)):
            return None
    if len(poly) == 1:
        return [0]

    deriv = [0]
    j=0
    for i in range(1, len(poly)+1):
        if poly[j] * 1/i == int(poly[j] * 1/i):
            deriv.append(int(poly[j] * 1/i))
        else:
            deriv.append(poly[j] * 1/i)
        j+= 1
    return deriv
