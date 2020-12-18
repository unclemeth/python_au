def middleNode(self, head):
    a = b = head
    while b and b.next:
        a = a.next
        b = b.next.next
    return a