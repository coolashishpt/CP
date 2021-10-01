def selectionsort(arr):
    N = len(arr)

    for i in range(N-1):
        idx = i
        for j in range(i+1, N):
            if arr[idx] > arr[j]:
                idx = j

        arr[i], arr[idx] = arr[idx], arr[i]

    return arr


arr = [10, 5, 8, 20, 2, 18, 1]
print(selectionsort(arr))
