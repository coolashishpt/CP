class Node:
    def __init__(self, k):
        self.data = k
        self.next = None

def circularPrint(head):
    first = head.data
    curr = head
    while curr.next.data != first:
        print(curr.data, end=" ")
        curr = curr.next
    print(curr.data)

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

head.next.next.next.next.next = head

circularPrint(head)

