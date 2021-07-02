
def insertAtIndex(arr, sizeOfArray, index, element):
    rest = arr[index: len(arr)-1]

    arr[index] = element
    del arr[index+1:]
    arr = arr+rest
    return arr

a =  [1, 2, 3, 4, 5, -1]
index = 5
element = 90

for i in range(len(a)-1, index, -1):
    # print(i)
    a[i] = a[i - 1]

a[index] = element

print(a)