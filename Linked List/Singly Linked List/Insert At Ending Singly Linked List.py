class Node:
    def __init__(self, k):
        self.key = k
        self.next = None


def insertEnding(head, k):
    if head == None:
        return Node(k)

    current = head
    while current.next != None:
        current = current.next

    current.next = Node(k)
    return head


def printLL(head):
    curr = head
    while curr != None:
        print(curr.key, end=" ")
        curr = curr.next

head = None
head = insertEnding(head, 1)
head = insertEnding(head, 2)
head = insertEnding(head, 3)

printLL(head)
