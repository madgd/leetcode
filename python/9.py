class Solution1(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #转化为str，但是用了额外空间
        return str(x) == str(x)[::-1]

class Solution2(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or x != 0 and x % 10 == 0:
            return False
        q = 0
        while q < x:
            q = q * 10 + x % 10
            x /= 10
        return q == x or (q / 10) == x
