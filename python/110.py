# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def maxDepth(root):
            if root is None:
                return 0
            else:
                left = maxDepth(root.left)
                right = maxDepth(root.right)
                if abs(left - right) > 1:
                    res[0] = False
                return max(left, right) + 1   
        res = [True]
        maxDepth(root)
        return res[0
