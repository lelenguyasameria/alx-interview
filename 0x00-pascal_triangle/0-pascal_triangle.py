#!/usr/bin/python3
""" pascal triangle
"""


def pascal_triangle(n):
    """ returns pascal triangle
    """
    if n <= 0:
        return []

    pasTran = []

    for i in range(n):
        # first element
        my_List = [1]
        if i == 0:
            pasTran.append(my_List)
            continue

        k = i - 1
        for j in range(len(pasTran[k])):
            if j + 1 == len(pasTran[k]):
                # last element
                my_List.append(1)
                break
            # Add two previous values to get current next value
            nextVal = pasTran[k][j] + pasTran[k][j + 1]
            my_List.append(nextVal)
        pasTran.append(my_List)

    return pasTran