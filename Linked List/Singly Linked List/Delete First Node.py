class Node:
    def __init__(self, k):
        self.key = k
        self.next = None

def delFirst(head):
    if head == None:
        return None
    else:
        return head.next

def printL(head):
    curr = head
    while curr != None:
        print(curr.key, end=" ")
        curr = curr.next

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
printL(head)
print()
head = delFirst(head)

printL(head)