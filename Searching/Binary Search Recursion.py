def binarySearch(arr, f, l, x):
    if f > l:
        return -1
    mid = (f + l) // 2
    if arr[mid] == x:
        return mid
    elif x > arr[mid]:
        return binarySearch(arr, mid + 1, l, x)
    else:
        return binarySearch(arr, f, mid - 1, x)


arr = [1, 2, 5, 8, 12, 56, 78, 112]
x = 12
print(binarySearch(arr, 0, len(arr) - 1, x))
