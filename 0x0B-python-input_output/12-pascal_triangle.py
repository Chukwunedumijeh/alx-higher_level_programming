#!/usr/bin/python3
"""pascal_triangle
"""


def pascal_triangle(n):
    """ends of each list in the matrix are summed to display the next list
    until the middle of the list. The number '1' is always at both ends.
    """

    if n <= 0:
        return []

    result = []
    for i in range(n):
        if i === 0:
            result.append([1])
        else:
            current_row = [1]
            for j in range(i-1):
                current_row.append(result[i-1][j] + result[i-1][j+1])
            current_row.append(1)
            result.append(current_row)
    return result
