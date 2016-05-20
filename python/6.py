class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        #之字型重新排列，numRows代表会排列成几行
        if numRows == 1:
            return s
        sig = 1
        l = 0
        res = [''] * numRows
        #对所以的字母，确定在哪一行，并添加
        for i in s:
            res[l] = res[l] + i

            #第一位，则下一次应该向下增加
            if l == 0:
                sig = 1
            #最后一位，则下一次应该向上增加
            if l == numRows - 1:
                sig = -1
            #下一位应该在哪一行
            l = l + sig

        return ''.join(res)
