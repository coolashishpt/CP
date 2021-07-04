def rotateArr(A,D,N):
    a = A[:D]
    a.reverse()
    b = A[D:len(A)]
    b.reverse()
    arr = a + b
    arr.reverse()
    return arr

A = [int(x) for x in input().strip().split()]

print(rotateArr(A, 2, 5))