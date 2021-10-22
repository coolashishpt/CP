class Node:
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None

def deleteHeadOfDLL(head):
    if head == None or head.next == None:
        return None

    head = head.next
    head.prev = None
    return head

def PRINT(head):
    curr = head
    while curr != None:
        print(curr.key, end=" ")
        curr = curr.next


head = Node(1)
temp1 = Node(2)
temp2 = Node(3)

head.next = temp1
temp1.prev = head

temp1.next = temp2
temp2.prev = temp1

ans = deleteHeadOfDLL(head)
PRINT(ans)