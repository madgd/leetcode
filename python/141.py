class Solution1(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #set中保存已经遍历元素
        NodesSet = set()
        while head:
            if head in NodesSet:
                return True
            else:
                NodesSet.add(head)
            head = head.next
        return False

class Solution2(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #快慢双指针法
        if head == None or head.next == None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if slow == None or fast == None or fast.next == None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
