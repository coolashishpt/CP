def firstOccur(arr, x):
    f = 0
    l = len(arr) - 1
    while f <= l:
        mid = (f + l) // 2

        if x < arr[mid]:
            l = mid - 1
        elif x > arr[mid]:
            f = mid + 1
        else:
            if mid == 0 or arr[mid - 1] != arr[mid]:
                return mid
            else:
                l = mid - 1
    return -1


arr = [1, 2, 10, 10, 10, 20, 20, 40]

print(firstOccur(arr, 10))

