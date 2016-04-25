# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        #该树没有相等的节点
        #如果p,q中有节点等于根节点的值，或p,q分别在根节点两边，则最低公共祖先为root
        #否则根据大小递归处理root的左或右子树
        if p.val == root.val or q.val == root.val:
            return root
        if p.val < root.val:
            if q.val > root.val:
                return root
            else:
                return self.lowestCommonAncestor(root.left, p, q)
        else:
            if q.val < root.val:
                return root
            else:
                return self.lowestCommonAncestor(root.right, p, q)

class Solution2(object):
    def lowestCommonAncestor(self, root, p, q):
        res = root
        while res:
            if p.val > res.val and q.val > res.val:
                res = res.right
            elif p.val < res.val and q.val < res.val:
                res = res.left
            else:
                return res
