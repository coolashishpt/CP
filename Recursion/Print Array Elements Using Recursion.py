def printArrayRecursively(arr, n):
    if n <= 0:
        return

    l = len(arr)
    print(arr[l - n], end=" ")
    printArrayRecursively(arr, n - 1)


printArrayRecursively([1, 2, 3, 4, 5], 5)
