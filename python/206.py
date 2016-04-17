# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution1(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        t = ListNode(0)
        m = ListNode(0)
        m.next = head
        (m.next.next, t.next) = (t.next, m.next.next)
        (m.next, t.next) = (t.next, m.next)
        while not m.next == None:
            (m.next.next, t.next) = (t.next, m.next.next)
            (m.next, t.next) = (t.next, m.next)
        return t.next

class Solution2(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
