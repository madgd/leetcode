class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        l = len(s)
        for i in range(l):
            num = num + 26 ** i * (ord(s[-i-1]) - 64) 
        return num
