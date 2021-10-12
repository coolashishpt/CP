class Node:
    def __init__(self, k):
        self.key = k
        self.next = None


def reverseNaive(head):
    # Naive Solution
    stack = []
    curr = head
    while curr != None:
        stack.append(curr.key)
        curr = curr.next

    curr = head
    while curr != None:
        curr.key = stack.pop()
        curr = curr.next

    return head


def reverseOptimize(head):
    # Optimize Solution
    curr = head
    prev = None

    while curr != None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev


def reverseRecurr(curr, prev=None):
    if curr == None:
        return prev

    next = curr.next
    curr.next = prev
    return reverseRecurr(next, curr)


def PRINT(head):
    curr = head
    while curr != None:
        print(curr.key, end=" ")
        curr = curr.next


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
PRINT(head)
print()

head = reverseOptimize(head)

PRINT(head)
