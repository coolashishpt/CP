def insertionsort(arr):
    n = len(arr)

    for i in range(1, n):
        x = arr[i]
        j = i - 1
        while j >= 0 and x < arr[j]:
            arr[j + 1] = arr[j]

            j -= 1
        arr[j + 1] = x
    return arr


arr = [12, 45, 23, 51, 19, 8]
arr1 = [20, 5, 40, 60, 10, 30]

print(insertionsort(arr))
