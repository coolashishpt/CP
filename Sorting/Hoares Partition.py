def hoarepartition(arr, l, h):
    pivot = arr[l]
    i = l - 1
    j = h + 1

    while True:
        i = i + 1
        while arr[i] < pivot:
            i = i + 1

        j = j - 1

        while arr[j] > pivot:
            j = j - 1

        if i >= j:
            return j
        # print(i, j)
        arr[i], arr[j] = arr[j], arr[i]
        # print(arr)


def quickSort(arr, l, h):
    if l < h:
        p = hoarepartition(arr, l, h)
        quickSort(arr, l, p)
        quickSort(arr, p + 1, h)




if __name__ == "__main__":
    arr = [5, 3, 8, 4, 2, 7, 1, 10]
    quickSort(arr, 0, len(arr) - 1)
    print()
    print(arr)
