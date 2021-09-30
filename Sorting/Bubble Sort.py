def bubblesort(array):
    arr = array
    N = len(arr) - 1
    for i in range(N):

        for j in range(N - i):
            if arr[j] > arr[j + 1]:
                temp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = temp
                # arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


arr = [3, 2, 4, 1]
print(bubblesort(arr))
