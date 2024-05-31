#!/usr/bin/python3
'''generates pascal's triangle of n rows'''


def pascal_triangle(n):
    '''generates pascal's triangle of n rows'''
    triangle = []
    if n <= 0:
        return triangle
    else:
        for i in range(n):
            row = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            triangle.append(row)
        return triangle
