import numpy as np
from PIL import Image


def floodFill(matrix, row, coloumn, toFill, prevFill):
    r = len(matrix)
    c = len(matrix[0])

    if row < 0 or row >= r or coloumn < 0 or coloumn >= c:
        return

    if matrix[row][coloumn] != prevFill:
        return

    matrix[row][coloumn] = toFill

    floodFill(matrix, row, coloumn + 1, toFill, prevFill)
    floodFill(matrix, row, coloumn - 1, toFill, prevFill)
    floodFill(matrix, row - 1, coloumn, toFill, prevFill)
    floodFill(matrix, row + 1, coloumn, toFill, prevFill)

    return matrix


a = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 0],
    [1, 0, 0, 1, 1, 0, 1, 1],
    [1, 2, 2, 2, 2, 0, 1, 0],
    [1, 1, 1, 2, 2, 0, 1, 0],
    [1, 1, 1, 2, 2, 2, 2, 0],
    [1, 1, 1, 1, 1, 2, 1, 1],
    [1, 1, 1, 1, 1, 2, 2, 1]
]

# print(floodFill(a, 0, 0, 4, 1))
# print(a[2][2])
arr = np.array(a)
floodFill(arr, 3, 2, 200, 2)
print(arr)

# img = Image.fromarray(arr)
# img.show()
