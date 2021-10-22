class Node:
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None

def reverseDLL(head):
    if head == None or head.next == None:
        return head

    curr = head
    prev = None

    while curr != None:
        prev = curr
        curr.next, curr.prev = curr.prev, curr.next
        curr = curr.prev

    return prev




def PRINT(head):
    curr = head
    while curr != None:
        print(curr.key, end=" ")
        curr = curr.next


head = Node(1)
temp = Node(2)
temp1 = Node(3)
temp2 = Node(4)

head.next = temp
temp.prev = head

temp.next = temp1
temp1.prev = temp

temp1.next = temp2
temp2.prev = temp1

rev = reverseDLL(head)
PRINT(rev)