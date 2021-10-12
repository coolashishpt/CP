class Node:
    def __init__(self, k):
        self.key = k
        self.next = None


    def search(self, x):
        curr = head
        position = 1
        while curr != None:
            if curr.key == x:
                return position
            else:
                curr = curr.next
                position += 1
        return -1


if __name__ == "__main__":

    head = Node(10)
    head.next = Node(5)
    head.next.next = Node(20)
    head.next.next.next = Node(15)

    res = Node.search(head, 2)
    print(res)