'''
基本数字 Ⅰ、X 、C 中的任何一个、自身连用构成数目、或者放在大数的右边连用构成数目、都不能超过三个；放在大数的左边只能用一个；
不能把基本数字 V 、L 、D 中的任何一个作为小数放在大数的左边采用相减的方法构成数目；放在大数的右边采用相加的方式构成数目、只能使用一个；
V 和 X 左边的小数字只能用 Ⅰ；
L 和 C 左边的小数字只能用X；
D 和 M 左边的小数字只能用 C
'''
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
