class Solution1(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        values = []
        while head:
            values.append(head.val)
            head = head.next
        return values == values[::-1]

class Solution2(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #反转后半段链表，使用O(1)额外空间
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        pre = None
        while slow:
            slow.next, pre, slow = pre, slow, slow.next

        while pre:
            if pre.val != head.val:
                return False
            pre = pre.next
            head = head.next

        return True
