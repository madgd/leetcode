class Solution1(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        q = [[head,head.next]]
        res = head.next
        while q:
            pairs = q.pop()
            Next = None
            if pairs[1].next != None:
                if pairs[1].next.next != None:
                    q.append([pairs[1].next,pairs[1].next.next])
                    Next = pairs[1].next.next
                else:
                    Next = pairs[1].next
            pairs[0].next = Next
            pairs[1].next = pairs[0]

        return res

class Solution2(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        else:
            p = head.next
            head.next.next, head.next = head, self.swapPairs(head.next.next)
            return p
