# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return
        m = ListNode(0)
        m.next = head
        while not m.next.next == None:
            if m.next.next.val == m.next.val:
                m.next.next = m.next.next.next
            else:
                m.next = m.next.next
        return head
