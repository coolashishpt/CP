def countingSort(arr):
    count = [0] * (len(arr) + 2)
    output = [0] * (len(arr)  + 2)
    n = 0
    for i in arr:
        count[i] += 1

    for j in range(len(count)):
        n = n + count[j]
        count[j] = n

    for k in arr:
        output[count[k]] = k
        count[k] -= 1

    return output, arr, count


arr = [1, 4, 1, 2, 7, 5, 2]
n, a, t = countingSort(arr)
print(a)
print(t)
print(n)
