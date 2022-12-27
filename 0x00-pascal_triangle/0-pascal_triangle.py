#!/usr/bin/python3
"""pascal triangle module
"""


def pascal_triangle(n):
    """
    Returns a list of lists of a pascal triangle.
    """
    if n <= 0:
        return []

    result = [[1]]
    while len(result) is not n:
        tmp = [1]
        for i in range(len(result[-1]) - 1):
            tmp.append(result[-1][i] + result[-1][i + 1])
        tmp.append(1)
        result.append(tmp)
    return result
