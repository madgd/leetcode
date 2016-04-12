class Solution1(object):
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
class Solution2(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        l = len(s)
        base = 1
        for i in range(l):
            num = num + base * (ord(s[-i-1]) - 64)
            base = base * 26
        return num
