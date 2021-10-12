class Node:
    def __init__(self, k):
        self.key = k
        self.next = None


temp1 = Node(22)
temp2 = Node(23)
temp3 = Node(24)
temp4 = Node(25)

temp1.next = temp2
temp2.next = temp3
temp3.next = temp4
head = temp1

while head is not None:
    print(head.key)
    head = head.next


# Alternate Way
head1 = Node(10)
head1.next = Node(20)
head1.next.next = Node(30)

print(head1)

