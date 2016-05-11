class Solution1(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        #迭代
        if not root:
            return []
        i = 0
        traversal = [[root.val]]
        q = [[root]]
        tempNodes = []
        tempValue = []
        while True:
            tempNodes = []
            tempValue = []
            for j in q[i]:
                if j.left:
                    tempNodes.append(j.left)
                    tempValue.append(j.left.val)
                if j.right:
                    tempNodes.append(j.right)
                    tempValue.append(j.right.val)
            i += 1
            if not tempNodes:
                return traversal
            q.append(tempNodes)
            traversal = [tempValue] + traversal

class Solution2(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        #递归
        if not root:
            return []
        levelValue = [[]]
        level = []
        if type(root) is not list:
            root = [root]
        for i in root:
            levelValue[0].append(i.val)
            if i.left:
                level.append(i.left)
            if i.right:
                level.append(i.right)

        rest = self.levelOrderBottom(level)
        if rest:
            return rest + levelValue
        else:
            return levelValue
