class Solution1(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        m = 0
        l = 1
        for i in range(n):
            m, l = l, m + l
        return l

