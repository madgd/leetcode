class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        while s and s[-1] == ' ':
            s = s[:-1]
        leng = len(s)
        if not leng:
            return 0            
        n = s.rfind(' ')

        return leng - n -1

class Solution2(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        leng = len(s)
        m = 1
        while m <= leng and s[-m] == ' ':
            m += 1
        n = m
        while n <= leng and s[-n] != ' ':
            n += 1
        return n - m
