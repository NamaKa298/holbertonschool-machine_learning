#!/usr/bin/env python3
"""Calculates the derivative of a polynomial."""


def poly_derivative(poly):
    deriv=[]
    for i in range(1,len(poly)):
        poly[i] *= i
        deriv.append(poly[i])
    return deriv
