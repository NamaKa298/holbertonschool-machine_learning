#!/usr/bin/env python3

def matrix_shape(matrix):
    for i in range (len(matrix)):
        if type(matrix[i]) is list:
            return [len(matrix)] + matrix_shape(matrix[i])
        else:
            return [len(matrix)]
