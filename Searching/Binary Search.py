class BinarySearch:
    # Binary Search Only work on sorted array's

    def __init__(self, arr, x):

        self.arr = arr
        self.search = x

    # Iterative Way for Binary Search
    def iterativeWay(self):
        arr = self.arr
        search = self.search

        first = 0
        last = len(arr) - 1
        while first <= last:

            mid = (first + last) // 2

            if arr[mid] == search:
                return mid

            elif search > arr[mid]:
                first = mid + 1

            else:
                last = mid - 1

        return -1

    # Recursive Way for Binary Search
    def recursiveWay(self, arr, first, last):

        search = self.search

        if first > last:
            return -1

        mid = (first + last) // 2

        if arr[mid] == search:
            return mid

        elif search > arr[mid]:
            return self.recursiveWay(arr, mid + 1, last)

        else:
            return self.recursiveWay(arr, first, mid - 1)


arr = [1, 2, 5, 8, 12, 56, 78, 112]
x = 12
obj = BinarySearch(arr, x)

print(obj.iterativeWay())
print(obj.recursiveWay(arr, 0, len(arr) - 1))

print(BinarySearch(arr, 13).iterativeWay())
