def removeNthFromEnd(self, head, n):
    l = []

    while head:
        l.append(head.val)
        head = head.next

    l.pop(len(l)-n)
    i = ListNode()
    temp = i
    for j in l:
        i.next = ListNode(j)
        i = i.next
    return temp.next