class Solution:
    def detectCycle(self, head):
        if head is None:
            return None
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        if fast == slow:
            break

        if fast is None or fast.next is None:
            return None

        while head != slow:
            head = head.next
            slow = slow.next


        return head