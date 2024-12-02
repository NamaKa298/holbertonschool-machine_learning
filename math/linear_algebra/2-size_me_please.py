#!/usr/bin/env python3


def matrix_shape(matrix):
    """Retourne la dimension d'une matrice sous forme de liste"""
    for i in range(len(matrix)):
        if type(matrix[i]) is list:
            return [len(matrix)] + matrix_shape(matrix[i])
        else:
            return [len(matrix)]
