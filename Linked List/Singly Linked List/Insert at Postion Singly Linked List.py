class Node:
    def __init__(self, k):
        self.key = k
        self.next = None


def insertAtPos(head, data, pos):
    temp = Node(data)

    if pos == 1:
        temp.next = head
        return temp

    curr = head

    for i in range(pos - 2):
        curr = curr.next
        if curr == None:
            return head

    temp.next = curr.next
    curr.next = temp

    return head


def printl(head):
    curr = head
    while curr != None:
        print(curr.key, end=" ")
        curr = curr.next


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

insertAtPos(head, 15, 3)
printl(head)