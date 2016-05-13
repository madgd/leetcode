class Solution1(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        #递归
        if not root:
            return False
        if root.left == root.right == None and root.val == sum:
            return True

        sum -= root.val
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

class Solution2(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        #深度搜索
        if not root:
            return False

        q = [(root, root.val)]
        while q:
            curr, val = q.pop()
            if curr.left == None and curr.right == None and val == sum:
                return True
            if curr.left:
                q.append((curr.left, val + curr.left.val))
            if curr.right:
                q.append((curr.right, val + curr.right.val))

        return False
