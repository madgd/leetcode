class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        #取绝对值的str，并反转，转化为int
        m = int(str(abs(x))[::-1])
        #判断是否越界
        if m > 2147483647:
            return 0
        if x < 0:
            return -m
        return m
