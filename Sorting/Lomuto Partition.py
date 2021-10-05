def lomutoPartition(arr, l, h):
    pivot = arr[h]
    i = l - 1

    for j in range(l, h):
        if arr[j] < pivot:
            i = i + 1
            # print(i, j)

            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[h] = arr[h], arr[i + 1]

    return i + 1


if __name__ == "__main__":
    arr = [10, 80, 30, 90, 40, 50, 70]
    print(lomutoPartition(arr=arr, l=0, h=6))
    print(arr)
