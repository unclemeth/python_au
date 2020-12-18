class Solution:
    def reorderList(self, head):
        if not head:
            return head
    a = []
    temp = head
    while(temp):
        a.append(temp)
        temp = temp.next
        temp = head
        i = 0
        n = len(a)//2
        m = -1
        n = 1
        o = -1
    for _ in range(len(a)-1):
        if o==1:
            temp.next = a[n]
            temp = temp.next
            o = -1
            n+=1
        else:
            temp.next = a[m]
            temp = temp.next
            o = 1
            m-=1
            temp.next = None
        return head