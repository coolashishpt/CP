def countOne(arr, N):
    f = 0
    l = N - 1

    while f <= l:
        mid = (f + l) // 2
        if arr[len(arr) - 1] == 1:
            return len(arr)
        elif arr[mid] == 1:
            f = mid + 1
        else:
            l = mid - 1

    return l + 1


arr = [1, 1, 0, 0, 0, 0]
N = len(arr)
print(countOne(arr, N))
