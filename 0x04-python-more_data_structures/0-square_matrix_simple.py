#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix[:]
    map_matrix = list(map(lambda x: list(map(lambda y: (y**2), x)), new_matrix))
    return map_matrix
