#!/usr/bin/env python3
"""Calculates the integral of a polynomial."""


def poly_integral(poly, C=0):
    """
    Calculates the integral of a polynomial.
    """
    if (not isinstance(poly, list) or len(poly) == 0 or
            not isinstance(C, int)):
        return None
    if len(poly) == 1:
        return [C, poly[0]]

    integral = [C]
    for i in range(len(poly)):
        coeff = poly[i] / (i + 1)
        if coeff.is_integer():
            integral.append(int(coeff))
        else:
            integral.append(coeff)
    return integral
