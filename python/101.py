# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None or not root.left and not root.right:
            return True
            
        if None in [root.left, root.right]:
            return False
            
        stack = [(root.left, root.right)]
        while stack:
            node1, node2 = stack.pop(0)
            if not node1 and not node2:
                continue
            elif None in [node1, node2]:
                return False
            else:
                if node1.val != node2.val:
                    return False
                stack.append((node1.left, node2.right))
                stack.append((node1.right, node2.left))
        return True
class Solution2(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None or not root.left and not root.right:
            return True
            
        if None in [root.left, root.right]:
            return False
         
        return self.compare(root.left, root.right)
        
    def compare(self, p, q):
        if p is None and q is None:
            return True
        elif None in [p, q]:
            return False
        elif not p.val == q.val:
            return False
        else:
            return self.compare(p.left, q.right) and self.compare(p.right, q.left)
