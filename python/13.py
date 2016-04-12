class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romanDict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        plus = 1
        if len(s) == 0:
            return 0
        t = 1
        n = 0
        for i in reversed(s):
            if romanDict[i] < t:
                plus = -1
            else:
                plus = 1
            n = n + plus * romanDict[i]
            t = romanDict[i]
        return n
