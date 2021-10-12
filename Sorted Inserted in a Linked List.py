class Node:
    def __init__(self, k):
        self.key = k
        self.next = None


# Time Complexity is O(n)
def sortInsert(head, x):
    temp = Node(x)
    if head == None:
        return temp
    if head.key > x:
        temp.next = head
        return temp

    curr = head
    while curr.next != None and curr.next.key < x:
        curr = curr.next

    temp.next = curr.next
    curr.next = temp

    return head


def printl(head):
    curr = head
    while curr != None:
        print(curr.key, end=" ")
        curr = curr.next


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
print("Full Sex")
head = sortInsert(head, 50)
printl(head)
