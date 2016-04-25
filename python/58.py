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

        return len(s) - n -1
