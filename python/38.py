class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for nth in range(n - 1):
            m = 0
            t = s[0]
            sNext = ''
            for i in s:
                if i == t:
                    m = m + 1
                else:
                    sNext = sNext + str(m) + t
                    t = i
                    m = 1
            sNext = sNext + str(m) + t
            s = sNext

        return s
