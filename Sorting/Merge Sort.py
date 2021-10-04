def merge(arr, l, mid, r):
    left = arr[l:mid + 1]
    right = arr[mid + 1: r + 1]

    m, n = len(left), len(right)
    i, j, k = 0, 0, l

    while i < m and j < n:

        if left[i] > right[j]:
            arr[k] = right[j]
            j += 1
            k += 1
        else:
            arr[k] = left[i]
            i += 1
            k += 1

    while i < m:
        arr[k] = left[i]
        i += 1
        k += 1

    while j < n:
        arr[k] = right[j]
        j += 1
        k += 1


def mergeSort(arr, l, r):
    if r > l:
        m = (r + l) // 2
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


if __name__ == "__main__":
    arr = [4, 1, 3, 9, 7]
    mergeSort(arr, 0, len(arr) - 1)
    print(arr)
