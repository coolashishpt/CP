def lastOccur(arr, x):
    f = 0
    l = len(arr) - 1

    while f <= l:

        mid = (f + l) // 2

        if x < arr[mid]:
            l = mid - 1

        elif x > arr[mid]:
            f = mid + 1

        else:
            if mid == len(arr) - 1 or arr[mid] != arr[mid + 1]:
                return mid
            else:
                f = mid + 1
    return -1


arr = [1, 2, 3, 4, 4, 5, 6, 6, 6, 6, 6, 8, 9, 9]
print(lastOccur(arr, 9))
