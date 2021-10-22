class Node:
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None

def deleteTailDLL(head):
    if head == None or head.next == None:
        return None

    curr = head
    while curr.next.next != None:
        curr = curr.next

    curr.next = None
    return head

def PRINT(head):
    curr = head
    while curr != None:
        print(curr.key, end=" ")
        curr = curr.next


head = Node(1)
temp1 = Node(2)
temp2 = Node(3)
temp3 = Node(4)

head.next = temp1
temp1.prev = head

temp1.next = temp2
temp2.prev = temp1

temp2.next = temp3
temp3.prev = temp2

ans = deleteTailDLL(head)
PRINT(ans)