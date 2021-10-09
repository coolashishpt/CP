class Node:
    def __init__(self, k):
        self.key = k
        self.next = None


def insertBegin(head, k):
    temp = Node(k)
    temp.next = head
    return temp


def printLL(head):
    curr = head
    while curr != None:
        print(curr.key, end=" ")
        curr = curr.next


head = None
head = insertBegin(head, 1)
head = insertBegin(head, 2)
head = insertBegin(head, 3)

printLL(head)
