# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        elif not root.left is None and not root.right is None:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        elif root.left is None and not root.right is None:
            return self.minDepth(root.right) + 1
        elif (not root.left is None) and root.right is None:
            return self.minDepth(root.left) + 1
        else:
            return 1

class Solution2(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = [(root,1)] if root else []
        while q:
            n, depth = q.pop(0)
            if None == n.left == n.right:
                return depth
            if n.left: q.append((n.left, depth+1))
            if n.right: q.append((n.right, depth+1))
        return 0
