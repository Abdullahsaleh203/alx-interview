#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Given an n x n 2D matrix, rotate it 90 degrees clockwise.
    """
    n = len(matrix)
    for layer in range(n // 2):
        first, last, offset = layer, n - 1 - layer, 0
        for i in range(first, last):
            top = matrix[first][i]
            matrix[first][i] = matrix[last - offset][first]
            matrix[last - offset][first] = matrix[last][last - offset]
            matrix[last][last - offset] = matrix[i][last]
            matrix[i][last] = top
            offset += 1

# def rotate_2d_matrix(matrix):
#     n = len(matrix)

#     # Transpose the matrix (swap rows with columns)
#     for i in range(n):
#         for j in range(i, n):
#             matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

#     # Reverse the rows to complete the rotation
#     for i in range(n):
#         matrix[i].reverse()
