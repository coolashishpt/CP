def Cyclesort(arr):
    i = 0
    while i < len(arr):
        correct = arr[i] - 1
        if arr[i] != arr[correct]:
            arr[i], arr[correct] = arr[correct], arr[i]
        else:
            i += 1


if __name__ == "__main__":
    arr = [6, 3, 5, 2, 4, 1, 7]
    Cyclesort(arr)
    print(arr)
