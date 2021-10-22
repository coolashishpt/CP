class Node:
    def __init__(self, k):
        self.key = k
        self.prev = None
        self.next = None


def insertEndDLL(head, x):
    temp = Node(x)
    if head == None:
        temp.next = head
        return temp

    curr = head
    while curr.next != None:
        curr = curr.next

    curr.next = temp
    temp.prev = curr

    return head


def PRINT(head):
    curr = head
    while curr != None:
        print(curr.key, end=" ")
        curr = curr.next

head = None

head = insertEndDLL(head, 1)
head = insertEndDLL(head, 2)
head = insertEndDLL(head, 3)

PRINT(head.next.next.prev)
