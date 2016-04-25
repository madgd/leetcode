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
        base = 1
        n = 0
        for i in reversed(s):
            if romanDict[i] < base:
                plus = -1
            else:
                plus = 1
            n = n + plus * romanDict[i]
            base = romanDict[i]
        return n

class Solution2(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        #左边小于右边，必定是减去的；最后一位一定是加上的
        romanDict = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        n = 0
        for i in range(0, len(s) - 1):
            if romanDict[s[i]] < romanDict[s[i+1]]:
                n -= romanDict[s[i]]
            else:
                n += romanDict[s[i]]
        return n + romanDict[s[-1]]
