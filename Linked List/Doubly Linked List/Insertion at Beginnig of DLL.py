class Node:
    def __init__(self, k):
        self.key = k
        self.prev = None
        self.next = None


def insertBeginDLL(head, x):
    temp = Node(x)
    if head == None:
        return temp

    head.prev = temp
    temp.next = head

    return temp


def PRINT(head):
    curr = head
    while curr != None:
        print(curr.key, end=" ")
        curr = curr.next


head = None

head = insertBeginDLL(head, 1)
head = insertBeginDLL(head, 2)
head = insertBeginDLL(head, 3)

PRINT(head)
